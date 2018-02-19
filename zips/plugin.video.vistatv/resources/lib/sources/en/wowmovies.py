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

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['wowmovies.io']
        self.base_link = 'http://wowmovies.io'
        self.search_link = ('?s=%s')

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            clean_title = cleantitle.geturl(title).replace('-','+')
            url = self._search(clean_title, year)
            return url
        except:
            return

    def _search(self, title, year):
        try:
            url = urlparse.urljoin(self.base_link, self.search_link % (title))
            r = client.request(url)
            r = dom_parser2.parse_dom(r, 'div', {'data-movie-id': re.compile('.+?')})
            r = [(dom_parser2.parse_dom(i, 'a', req='href'),
                  dom_parser2.parse_dom(i, 'div', {'class': 'qtip-title'}),
                  dom_parser2.parse_dom(i, 'div', {'class': 'jtip-quality'}),
                  dom_parser2.parse_dom(i, 'a', req='rel')) for i in r]
            r = [(i[0][0].attrs['href'], i[1][0].content, i[2][0].content, i[3][0].content) for i in r]
            r = [(i[0], i[2]) for i in r if title.replace('+','') in cleantitle.get_simple(i[1]) and i[3] == year]
            if r: 
                url = r[0][0]
                self.quality = r[0][1]
                return url
            else: return
        except:
            return
                
    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url == None: return sources

            r = client.request(url)
            r = dom_parser2.parse_dom(r, 'source', req='src')[0]
            link = r.attrs['src']
            qual, info = source_utils.get_release_quality(self.quality, self.quality)
            info = ' | '.join(info)
            url = client.replaceHTMLCodes(link)
            url = url.encode('utf-8')
            sources.append({'source': 'CDN', 'quality': qual, 'language': 'en', 'url': url, 'info': info, 'direct': True, 'debridonly': False})

            return sources
        except:
            return sources


    def resolve(self, url):
        return url