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


import re, urllib, urlparse, json, time

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import cfscrape


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['filmxy.me']
        self.base_link = 'http://www.filmxy.me'
        self.search_link = '%s/wp-json/wp/v2/posts?search=%s'
        self.scraper = cfscrape.create_scraper()

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        self.sources = []
        try:
            if url == None: return
            urldata = urlparse.parse_qs(url)
            urldata = dict((i, urldata[i][0]) for i in urldata)
            title = urldata['title'].replace(':', ' ').replace('-', ' ').lower()
            year = urldata['year']
            self.hostprDict = hostprDict

            query = self.search_link % (self.base_link, title.lower().replace(' ', '%20'))
            r = self.scraper.get(query).content
            r = json.loads(r)
            links = [(i['link'], i['title']['rendered']) for i in r if i]
            links = [(i[0], i[1]) for i in links if cleantitle.get_simple(i[1].split('(')[0]) in cleantitle.get_simple(title)]
            links = [i[0] for i in links if year in i[1]]

            for i in links:
                r = self.scraper.get(i).content
                url = client.parseDOM(r, 'a', ret='href', attrs={'id':'main-down'})[0]

                self.scrape_results(url)

            return self.sources
        except:
            return self.sources


    def scrape_results(self, url):
        try:

            r = self.scraper.get(url).content

            links720 = client.parseDOM(r, 'div', attrs={'class': 'links_720p'})
            links720 = client.parseDOM(links720, 'a', ret='href')
            for link in links720:
                valid, host = source_utils.is_host_valid(link, self.hostprDict)
                print host
                if host in self.hostprDict:
                    debrid = True
                else:
                    debrid = False
                self.sources.append(
                    {'source': host, 'quality': '720p', 'language': 'en', 'url': link, 'info': [],
                     'direct': False,
                     'debridonly': debrid})

            links1080 = client.parseDOM(r, 'div', attrs={'class': 'links_1080p'})
            links1080 = client.parseDOM(links1080, 'a', ret='href')
            for link in links1080:
                valid, host = source_utils.is_host_valid(link, self.hostprDict)
                print host
                if host in self.hostprDict:
                    debrid = True
                else:
                    debrid = False
                self.sources.append(
                    {'source': host, 'quality': '1080p', 'language': 'en', 'url': link, 'info': [],
                     'direct': False,
                     'debridonly': debrid})

        except:pass

    def resolve(self, url):
        return url