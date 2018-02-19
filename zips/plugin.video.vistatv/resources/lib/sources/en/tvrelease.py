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
from resources.lib.modules import debrid
from resources.lib.modules import source_utils
from resources.lib.modules import dom_parser2
from resources.lib.modules import workers

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['tv-release.net', 'tv-release.immunicity.st']
        self.base_link = 'http://tv-release.net'
        self.search_link = '?s=%s'
        self.search_link2 ='/search/%s/feed/rss2/'

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

            if not debrid.status(): raise Exception()

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']

            self.hdlr = 'S%02dE%02d' % (int(data['season']), int(data['episode'])) if 'tvshowtitle' in data else data['year']

            query = '%s S%02dE%02d' % (data['tvshowtitle'], int(data['season']), int(data['episode'])) if 'tvshowtitle' in data else '%s %s' % (data['title'], data['year'])
            query = re.sub('(\\\|/| -|:|;|\*|\?|"|\'|<|>|\|)', ' ', query)

            url = self.search_link % urllib.quote_plus(query)
            url = urlparse.urljoin(self.base_link, url)
            r = client.request(url)
            r = dom_parser2.parse_dom(r, 'table', {'class': 'posts_table'})
            r = [re.sub('(onmouseover.+?UnTip\(\);\')', '', i.content) for i in r]
            r = [dom_parser2.parse_dom(i, 'a', req='href') for i in r]
            if len(self.hdlr) == 4: r = [(i[1].attrs['href'], i[1].content) for i in r if i[0].content.lower() == 'movies']
            else: r = [(i[1].attrs['href'], i[1].content) for i in r if i[0].content.lower() != 'movies']

            filter = ['uhd','4k','1080','720']
            r = [(i[0], i[1]) for i in r if any(x in i[0] for x in filter)]
            hostDict = hostprDict + hostDict

            threads = []
            for i in r: threads.append(workers.Thread(self._get_sources, i, hostDict))
            for i in threads: i.start()
            
            alive = [x for x in threads if x.is_alive() == True]
            while alive:
                alive = [x for x in threads if x.is_alive() == True]
                time.sleep(0.5)
            return self._sources
        except:
            return self._sources
            
    def _get_sources(self, item, hostDict):
        try:
            items = []
            try:
                t = item[1]
                t = re.sub('(\[.*?\])|(<.+?>)', '', t)
                if len(self.hdlr) == 4: y = re.findall('[\.|\(|\[|\s](\d{4})[\.|\)|\]|\s]', t)[-1].upper()
                else: y = re.findall('[\.|\(|\[|\s](S\d*E\d*|S\d*)[\.|\)|\]|\s]', t)[-1].upper()
                if not y == self.hdlr: raise Exception()
                url = urlparse.urljoin(self.base_link, item[0])
                data = client.request(url)
                data = dom_parser2.parse_dom(data, 'tbody')[0]
                data = dom_parser2.parse_dom(data, 'a', req='href')
                data = [i.attrs['href'] for i in data]
                u = [(t, i) for i in data]
                items += u
            except:
                pass

            for item in items:
                try:
                    name = item[0]
                    name = client.replaceHTMLCodes(name)
                    url = item[1]
                    if not url.startswith('http'):continue
                    if any(x in url for x in ['.rar', '.zip', '.iso']): raise Exception()
                    url = client.replaceHTMLCodes(url)
                    url = url.encode('utf-8')
                    valid, host = source_utils.is_host_valid(url, hostDict)
                    if not valid: continue
                    host = client.replaceHTMLCodes(host)
                    host = host.encode('utf-8')

                    quality, info = source_utils.get_release_quality(name, item[1])

                    try:
                        size = re.findall('((?:\d+\.\d+|\d+\,\d+|\d+) (?:GB|GiB|MB|MiB))', name)[-1]
                        div = 1 if size.endswith(('GB', 'GiB')) else 1024
                        size = float(re.sub('[^0-9|/.|/,]', '', size))/div
                        size = '%.2f GB' % size
                        info.append(size)
                    except:
                        pass

                    info = ' | '.join(info)

                    self._sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': True})
                except:
                    pass
        except:
            raise Exception()
            
    def resolve(self, url):
        return url
