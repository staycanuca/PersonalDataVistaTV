# -*- coding: utf-8 -*-

'''
    Cerebro ShowBox Scraper
    Credits to Exodus and Covenant; our thanks go to their creators

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
from resources.lib.modules import cache
from resources.lib.modules import debrid
from resources.lib.modules import dom_parser2
from resources.lib.modules import workers
from resources.lib.modules import source_utils
from resources.lib.modules import cfscrape

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['rlsbb.ru','rlsbb.unblocked.vc']
        self.base_link = 'https://rlsbb.unblocked.vc'
        self.search_link = 'searchp/lib/search526049.php?phrase=%s&pindex=1&rand=0.387893276798561'

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

    def sources(self, url, hostDict, hostprDict):
        try:
            self._sources = []
            if url == None: return self._sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            self.title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']

            self.hdlr = 'S%02dE%02d' % (int(data['season']), int(data['episode'])) if 'tvshowtitle' in data else data['year']

            query = '%s S%02dE%02d' % (data['tvshowtitle'], int(data['season']), int(data['episode'])) if 'tvshowtitle' in data else '%s %s' % (data['title'], data['year'])
            query = re.sub('(\\\|/| -|:|;|\*|\?|"|\'|<|>|\|)', ' ', query)

            query = urllib.quote_plus(query)
            url = urlparse.urljoin(self.base_link, self.search_link % (query.replace('+','%2B')))
            
            self.scraper = cfscrape.create_scraper()
            r = self.scraper.get(url).content
            posts = re.findall('"post_name":"([^"]+)', r)
            self.hostprDict = hostprDict
            self.hostDict = hostDict
            #filter = ['uhd','4k','1080','720']
            #posts = [i for i in posts if any(x in i for x in filter)]
            threads = []

            for i in posts: threads.append(workers.Thread(self._get_sources, i))
            [i.start() for i in threads]
            
            alive = [x for x in threads if x.is_alive() == True]
            while alive:
                alive = [x for x in threads if x.is_alive() == True]
                time.sleep(0.1)
            return self._sources
        except:
            return self._sources
            
    def _get_sources(self, item):
        try:
            u = urlparse.urljoin(self.base_link, item)
            r = self.scraper.get(u).content
            name = re.findall('<title>([^<]+)', r)[0]
            name = client.replaceHTMLCodes(name)
            main = dom_parser2.parse_dom(r, 'div', {'class': 'postContent'})
            main = [i.content for i in main]
            comments = dom_parser2.parse_dom(r, 'div', {'id': re.compile('commentbody-\d+')})
            main += [i.content for i in comments]
            for con in main:
                links = client.parseDOM(con, 'a', ret='href')
                for i in links:
                    try:
                        url = i
                        if 'youtube' in url: continue
                        if any(x in url for x in ['.rar', '.zip', '.iso']): raise Exception()
                        valid, host = source_utils.is_host_valid(url, self.hostDict)
                        if not valid:
                            valid, host = source_utils.is_host_valid(url, self.hostprDict)
                            if not valid: continue
                            else: rd = True
                        else: rd = False
                        host = client.replaceHTMLCodes(host)
                        host = host.encode('utf-8')
                        t = re.sub('(\.|\(|\[|\s)(\d{4}|S\d*E\d*|S\d*|3D)(\.|\)|\]|\s|)(.+|)', '', name)
                        if not cleantitle.get(t) == cleantitle.get(self.title): raise Exception()
                        y = re.findall('[\.|\(|\[|\s](\d{4}|S\d*E\d*|S\d*)[\.|\)|\]|\s]', name)[-1].upper()
                        if not y == self.hdlr: raise Exception()
                        if not self.hdlr.lower() in url.lower(): raise Exception()
                        quality, info = source_utils.get_release_quality(i, name)
                        try:
                            size = re.findall('((?:\d+\.\d+|\d+\,\d+|\d+)\s*(?:GiB|MiB|GB|MB))', con)[0]
                            div = 1 if size.endswith('GB') else 1024
                            size = float(re.sub('[^0-9|/.|/,]', '', size)) / div
                            size = '%.2f GB' % size
                            info.append(size)
                        except:
                            pass
                        info = ' | '.join(info)
                        if url in str(self._sources): continue
                        if rd:
                            self._sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': True})
                        else:
                            self._sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': False})
                    except:
                        pass
        except:
            pass

    def resolve(self, url):
        return url
