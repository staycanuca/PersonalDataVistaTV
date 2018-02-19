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
        self.domains = ['imdark.com']
        self.base_link = 'http://imdark.com'
        self.search_link = '/?s=%s&darkestsearch=4a4830de92&_wp_http_referer= &quality=&genre=&year=&lang=en'
        self.ajax_link = '/wp-admin/admin-ajax.php'
       

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return None

    def sources(self, url, hostDict, locDict):
        sources = []

        try:
            if url == None: return sources
            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            title = data['title']
            y = data['year']
            tit = title +' '+ y
            query = self.search_link % (urllib.quote_plus(tit)).replace(' ','%2F')
            query = urlparse.urljoin(self.base_link, query)
            result = client.request(query)
            r = client.parseDOM(result, 'div', attrs={'id':'showList'})
            r = client.parseDOM(r, 'h4')[0]
            r = dom_parser2.parse_dom(r, 'a', req='href')
            r = [i.attrs['href'] for i in r if cleantitle.get(title) == cleantitle.get(i.content) and y in i.content]

            url = r[0]
            result = client.request(url)
            r = re.findall(r'''\{['"]src['"]:['"]([^"']+)['"].+?data-res['"]:['"](\d+)['"]\}''',result,re.DOTALL)
            for i in r:
                try:
                    sources.append({'source': 'CDN', 'quality': source_utils.label_to_quality(i[1]), 'language': 'en', 'url': i[0].replace('\/','/'), 'direct': True, 'debridonly': False})
                except:
                    pass

            return sources
        except Exception as e:
            return sources

    def resolve(self, url):
        return url