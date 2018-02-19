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

import re,urllib,urlparse,json

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import directstream
from resources.lib.modules import jsunpack
from resources.lib.modules import source_utils
from resources.lib.modules import cfscrape
from resources.lib.modules import dom_parser2

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['pubfilmonline.net','getmypopcornnow.xyz']
        self.base_link = 'http://openloadmovies.tv'
        self.post_link = '/wp-admin/admin-ajax.php'
        self.search_link = '/?s=%s'
        r = client.request(self.base_link)
        self.cookie = re.findall('document\.cookie\s*=\s*"([^;]+)', r)[0]
       
    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url =  '%s/movies/%s-%s/' % (self.base_link, cleantitle.geturl(title),year)
            r = client.request(url, cookie=self.cookie)         
            if '<h2>ERROR <span>404</span></h2>' in r:
                url =  '%s/movies/%s/' % (self.base_link, cleantitle.geturl(title))
                r = client.request(url, cookie=self.cookie)
                if '<h2>ERROR <span>404</span></h2>' in r: return
            return url
        except Exception:
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
        except Exception:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url == None: return sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            if 'tvshowtitle' in data:
                url = '%s/episodes/%s-%01dx%01d/' % (self.base_link, cleantitle.geturl(data['tvshowtitle']), int(data['season']), int(data['episode']))
                year = re.findall('(\d{4})', data['premiered'])[0]
                r = client.request(url, cookie=self.cookie)
                y = client.parseDOM(r, 'span', attrs = {'class': 'date'})[0]
                y = re.findall('(\d{4})', y)[0]
                if not y == year: raise Exception()
            else:
                r = client.request(url, cookie=self.cookie)
            
            ref_url = url
            nonces = re.findall('"nonces":{"ajax_get_video_info":"([^"]+)', r)[0]
            r = dom_parser2.parse_dom(r, 'div', {'class': 'playex'})[0]
            r = dom_parser2.parse_dom(r.content, 'div', req=['data-servers','data-ids'])
            r = [(i.attrs['data-ids'].replace('=','%3D'), i.attrs['data-servers'], nonces) for i in r]
            
            headers = {'X-Requested-With': 'XMLHttpRequest',
                       'Referer': ref_url}
                       
            for i in r:
                post = 'action=ajax_get_video_info&ids=%s&server=%s&nonce=%s' % (i[0], i[1], i[2])
                url = urlparse.urljoin(self.base_link, self.post_link)
                u = client.request(url, post=post, headers=headers, cookie=self.cookie)
                links = re.findall('''file["']:["']([^'"]+).+?label["']:['"]([^"']+)''', u)
                for l in links:
                    url = l[0].replace('\/', '/')
                    sources.append({'source': 'gvideo', 'quality': source_utils.label_to_quality(l[1]), 'language': 'en', 'url': url, 'direct': True, 'debridonly': False})

            return sources
        except:
            return sources
            
    def resolve(self, url):
        try:
            if 'google' in url:
                return directstream.googlepass(url)
            else:
                return url
        except Exception:
            return