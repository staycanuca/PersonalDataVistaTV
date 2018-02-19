# -*- coding: utf-8 -*-

'''
    Cerebro ShowBox Scraper

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''



import re,urllib,urlparse,time

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import debrid
from resources.lib.modules import source_utils
from resources.lib.modules import dom_parser2
from resources.lib.modules import workers

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['dl4all.unblocked.vc', 'www.dl4all.ws']
        self.base_link = 'http://www.dl4all.ws'
        self.search_link ='oll/tag/%s.html'
        self.search_link2 = 'app/tag/%s.html'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            url = urlparse.parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urllib.urlencode(url)
            return url
        except:
            return

    def _search_show(self, tvshowtitle, hdlr, premiered):
        try:

            query = self.search_link % (urllib.quote_plus(tvshowtitle) + '+' + hdlr)
            url = urlparse.urljoin(self.base_link, query)
            r = client.request(url)
            u = dom_parser2.parse_dom(r, 'div', {'style': re.compile('color:#0099FF.+?')})
            u = [dom_parser2.parse_dom(i, 'a', req='href')[1] for i in u]
            u = [i.attrs['href'] for i in u]
            u = [i for i in u if hdlr in i or premiered in i and '/' + cleantitle.geturl(tvshowtitle) in i]
            ur = []
            for i in u:
                pattern = '''\/\d+-(%s)''' % cleantitle.geturl(tvshowtitle)
                match = re.search(pattern, i)
                if match: ur += [i]
            if ur: return ur
            return
        except:
            return

    def _search_movie(self, title, imdb, year):
        try:
            query = self.search_link2 % (urllib.quote_plus(title))
            url = urlparse.urljoin(self.base_link, query)
            r = client.request(url)
            u = re.findall('color:#0099FF(.+?)background:\s*url', r, re.DOTALL)
            u = [i for i in u if imdb in i]
            u = [dom_parser2.parse_dom(i, 'a', req='href')[2] for i in u if 'h1' in i]
            u = [(i.attrs['href'], dom_parser2.parse_dom(i.content, 'h1')[0]) for i in u if year in i.content]
            u = [i[0] for i in u if i]
            return u
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            self._sources = []

            if url == None: return self._sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']
            premiered = data['premiered'] if 'tvshowtitle' in data else ''
            imdb = data['imdb']
            hdlr = 's%02de%02d' % (int(data['season']), int(data['episode'])) if 'tvshowtitle' in data else data['year']
            if 'tvshowtitle' in data:
                urls = self._search_show(title, hdlr, premiered)
            else:
                urls = self._search_movie(title, imdb, hdlr)

            threads = []
            for i in urls: threads.append(workers.Thread(self._get_sources, i, hostDict, hostprDict))
            for i in threads:
                i.start(); time.sleep(0.5)
            [i.join() for i in threads]
            
            alive = [x for x in threads if x.is_alive() == True]
            while alive:
                alive = [x for x in threads if x.is_alive() == True]
                time.sleep(0.5)
            return self._sources
        except:
            return self._sources

    def _get_sources(self, url, hostDict, hostprDict):
        try:
            r = client.request(url)
            u = dom_parser2.parse_dom(r, 'div', {'id': re.compile('news-id-.+?')})
            us = []
            for i in u:
                us += re.findall('<br\s*\/>(http[^<]+)', i.content)

            info = []
            try:
                size_raw = re.findall('Size:\s*([^|]+)', r)[0]
                size = re.findall('((?:\d+\.\d+|\d+\,\d+|\d+) (?:GB|GiB|MB|MiB))', size_raw)[-1]
                div = 1 if size.endswith(('GB', 'GiB')) else 1024
                size = float(re.sub('[^0-9|/.|/,]', '', size))/div
                size = '%.2f GB' % size
                info.append(size)
            except:
                pass
            info = ' | '.join(info)
            for url in us:
                try:
                    if any(x in url for x in ['.rar', '.zip', '.iso']): raise Exception()
                    url = client.replaceHTMLCodes(url)
                    url = url.encode('utf-8')
                    valid, host = source_utils.is_host_valid(url, hostDict)
                    if not valid:
                        valid, host = source_utils.is_host_valid(url, hostprDict)
                        if not valid: continue
                        debrid_only = True
                    else: debrid_only = False
                    host = client.replaceHTMLCodes(host)
                    host = host.encode('utf-8')

                    quality, info2 = source_utils.get_release_quality(url, url)

                    self._sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': debrid_only})
                except: pass
        except:
            pass
            
    def resolve(self, url):
        return url