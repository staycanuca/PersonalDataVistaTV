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

import urllib, urlparse, re

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import dom_parser
from resources.lib.modules import directstream
from resources.lib.modules import cfscrape



class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['mehlizmovies.com']
        self.base_link = 'https://www.mehlizmovies.com/'
        self.search_link = 'search/%s/'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            query = self.search_link % (urllib.quote_plus(cleantitle.getsearch(title)))
            query = urlparse.urljoin(self.base_link, query)

            t = cleantitle.get(title)
            scraper = cfscrape.create_scraper()
            data = scraper.get(query).content
            data = client.parseDOM(data, 'div', attrs={'class': 'result-item'})
            r = client.parseDOM(data, 'div', attrs={'class': 'details'})
            r = [(dom_parser.parse_dom(i, 'a')[0], dom_parser.parse_dom(i, 'span', attrs={'class': 'year'})[0]) for i in
                 r]
            r = [(i[0].attrs['href'], i[0].content, i[1].content) for i in r if
                 (t == re.sub('(\d+p|4k|3d|hd)','',cleantitle.get(i[0].content)) and year == i[1].content and not 'Hindi' in i[0].content)]
            r = [(i[0]) for i in r if i]
            url = r

            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            query = self.search_link % (urllib.quote_plus(cleantitle.getsearch(tvshowtitle)))
            query = urlparse.urljoin(self.base_link, query)

            t = cleantitle.get(tvshowtitle)
            scraper = cfscrape.create_scraper()
            data = scraper.get(query).content
            data = client.parseDOM(data, 'div', attrs={'class': 'result-item'})
            r = client.parseDOM(data, 'div', attrs={'class': 'details'})
            r = [(dom_parser.parse_dom(r, 'a')[0], dom_parser.parse_dom(r, 'span', attrs={'class': 'year'})[0])]
            r = [(i[0].attrs['href'], i[0].content, i[1].content) for i in r if
                 (t == re.sub('(4k|3d|hd|season\d+)', '', cleantitle.get(i[0].content)) and year == i[1].content)]
            r = [(i[0]) for i in r if i]
            url = r[0]

            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if not url:
                return

            scraper = cfscrape.create_scraper()
            data = scraper.get(url).content
            data = client.parseDOM(data, 'ul', attrs={'class': 'episodios'})
            links  = client.parseDOM(data, 'div', attrs={'class': 'episodiotitle'})
            sp = zip(client.parseDOM(data, 'div', attrs={'class': 'numerando'}), client.parseDOM(links, 'a', ret='href'))

            Sea_Epi = '%dx%d'% (int(season), int(episode))
            for i in sp:
                sep = i[0]
                if sep == Sea_Epi:
                    url = i[1]

            return url
        except:
            return


    def sources(self, url, hostDict, hostprDict):
        sources = []

        try:
            if not url:
                return sources

            links = self.links_found(url)

            for url, quality in links:
                try:
                    valid, host = source_utils.is_host_valid(url, hostDict)
                    if 'mehliz' in url:
                        quality, info = source_utils.get_release_quality(quality, None)
                        host = 'MZ'; direct = True; urls = [{'quality': quality, 'url': url}]

                    elif 'ok.ru' in url:
                        host = 'vk'; direct = True; urls = (directstream.odnoklassniki(url))

                    else:
                        direct = False; urls = [{'quality': 'SD', 'url': url}]

                    for x in urls:
                        sources.append({'source': host, 'quality': x['quality'], 'language': 'en',
                                        'url': x['url'], 'direct': direct, 'debridonly': False})
                except:
                    pass

            return sources
        except:
            return sources

    def links_found(self,urls):
        try:
            scraper = cfscrape.create_scraper()
            links = []
            if type(urls) is list:
                for item in urls:
                    r = scraper.get(item).content
                    data = client.parseDOM(r, 'div', attrs={'id': 'playex'})
                    data1 = client.parseDOM(data, 'div', attrs={'id': 'option-\d+'})
                    q = client.parseDOM(data, 'span', attrs={'class': 'qualityx'})[0]
                    links += [(client.parseDOM(i, 'iframe', ret='src')[0], q) for i in data1]

            else:
                r = scraper.get(urls).content
                data = client.parseDOM(r, 'div', attrs={'id': 'playex'})
                data1 = client.parseDOM(data, 'div', attrs={'id': 'option-\d+'})
                q = client.parseDOM(data, 'span', attrs={'class': 'qualityx'})[0]
                links += [(client.parseDOM(i, 'iframe', ret='src')[0], q) for i in data1]

            return links
        except:
            return urls

    def resolve(self, url):
        if 'mehliz' in url:
            data = client.request(url, referer=url)
            sources = re.findall('''file:\s*["']([^"']+).+?label:\s*["']([^"']+)''', data)
            if sources:
                sources = [(source[1], source[0]) for source in sources]
                if len(sources) > 1:
                    try: sources.sort(key=lambda x: int(re.sub("\D", "", x[0])), reverse=True)
                    except: pass
                    url = sources[0][1]
        return url
