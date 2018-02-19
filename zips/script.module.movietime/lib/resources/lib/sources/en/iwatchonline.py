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

from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import dom_parser2

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['watchonline.to']
        self.base_link = 'https://www.watchonline.to'
        self.search_link = 'https://www.watchonline.to/search/'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = self._search(imdb, 'm')
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = self._search(imdb, 't')
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            url = url.replace('tv-shows/','episode/')
            url += '-s%02de%02d' % (int(season), int(episode))
            return url
        except:
            return

    def _search(self, imdb, type):
        try:

            post = ('searchquery=%s&searchin=%s' % (imdb, type))
            r = client.request(self.search_link, post=post)
            r = dom_parser2.parse_dom(r, 'div', {'class': ['widget','search-page']})[0]
            r = dom_parser2.parse_dom(r, 'tbody')[0]
            r = dom_parser2.parse_dom(r, 'a', req='href')[0]
            if r: 
                url = r.attrs['href']
                return url
            else: return
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url == None: return sources

            r = client.request(url)

            r = dom_parser2.parse_dom(r, 'tbody')[0]
            r = dom_parser2.parse_dom(r, 'tr')
            r = [(dom_parser2.parse_dom(i, 'a', req='href'), \
                  dom_parser2.parse_dom(i, 'img', req='src'), \
                  i.content) for i in r if i]
            r = [(i[0][0].attrs['href'], i[1][0].attrs['src'], i[2]) for i in r if i[0] and i[1] and i[2]]
            
            for i in r:
                try:
                    url = i[0]
                    host = i[1].split('domain=')[-1]
                    info = []
                    if '<td>3D</td>' in i[2]: info.append('3D')
                    if '<td>hd</td>' in i[2].lower(): quality = '1080p'
                    elif '<td>hdtv</td>' in i[2].lower(): quality = '720p'
                    elif '<td>cam</td>' in i[2].lower(): quality = 'CAM'
                    elif '<td>dvd</td>' in i[2].lower(): quality = 'SD'
                    elif '<td>3d</td>' in i[2].lower(): quality = '1080p'
                    else: quality = 'SD'
                    info = ' | '.join(info)
                    url = client.replaceHTMLCodes(url)
                    url = url.encode('utf-8')
                    valid, host = source_utils.is_host_valid(host, hostDict)
                    if not valid: raise Exception()
                    host = client.replaceHTMLCodes(host)
                    host = host.encode('utf-8')
                    sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'info': info, 'direct': False, 'debridonly': False})
                except:
                    pass

            return sources
        except:
            return sources


    def resolve(self, url):
        try:
            u = client.request(url, output='extended')
            url = re.findall("url=([^']+)", str(u[2]))[0]
            return url
        except:
            return