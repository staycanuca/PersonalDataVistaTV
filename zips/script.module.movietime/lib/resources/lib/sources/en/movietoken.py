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


import re,urllib,urlparse

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import dom_parser2
from resources.lib.modules import directstream


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['movietoken.to']
        self.base_link = 'http://movietoken.to'
        self.search_link = '/?s=%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            link, quality = self._search(title, year, type='movie')
            if link and quality:
                url = {'imdb': imdb, 'title': title, 'year': year, 'link': link, 'quality': quality, 'type': 'movie'}
                url = urllib.urlencode(url)
                return url
            else:
                return
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
            link = self._search(url['tvshowtitle'], season, type='tv')
            link = link[:-1] if link.endswith('/') else link
            t = link.split('/')[-1]
            link = self.base_link + '/episode/' + t + '-%d' % int(episode)
            url = {'imdb': imdb, 'title': title, 'link': link, 'type': 'tv'}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def _search(self, title, year, type):
        try:
            if type == 'movie':
                u = urlparse.urljoin(self.base_link, self.search_link % (urllib.quote_plus(title)))
                r = client.request(u)
                r = dom_parser2.parse_dom(r, 'div', {'class':'ml-item'})
                r = [(dom_parser2.parse_dom(i, 'a', req='href')[0],
                      dom_parser2.parse_dom(i, 'a', {'rel': 'tag'})[0],
                      dom_parser2.parse_dom(i, 'span', {'class': 'mli-quality'})) for i in r if r]
                r = [(i[0].attrs['href'], i[0].attrs['oldtitle'], i[1].content, i[2][0].content) for i in r if
                     i[0] and i[1] and i[2]]
                r = [(i[0], i[3]) for i in r if
                     cleantitle.get_simple(i[1]) == cleantitle.get_simple(title) and i[2] == year]
                return r[0][0], r[0][1]
            else:
                t = title + ' Season ' + year
                u = urlparse.urljoin(self.base_link, self.search_link % (urllib.quote_plus(t)))
                r = client.request(u)
                r = dom_parser2.parse_dom(r, 'div', {'class': 'ml-item'})
                r = dom_parser2.parse_dom(r, 'a', req='href')[0]
                return r.attrs['href']
        except:
            return None, None

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url == None: return sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            url = data['link']

            r = client.request(url)
            url = client.parseDOM(r, 'div', attrs={'id': 'tab1'})
            url = client.parseDOM(url, 'a' , ret='href')[0]
            if not data['imdb'] in url: raise Exception()

            q = client.parseDOM(r, 'a', attrs={'href':'#tab1'})[0]

            if q == 'HD':
                quality = "1080p"
            elif 'HD 720' in q:
                quality = '720p'
            elif 'SD' in q:
                quality = 'SD'
            else:
                quality = 'SD'

            sources.append({'source': 'DL', 'quality': quality, 'language': 'en', 'url': url,
                            'direct': True, 'debridonly': False})

            return sources
        except:
            return sources

    def resolve(self, url):
        return url
