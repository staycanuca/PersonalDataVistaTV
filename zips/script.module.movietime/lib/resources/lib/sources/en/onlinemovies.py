# NEEDS FIXING

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

import re,urllib,urlparse

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import directstream
from resources.lib.modules import cfscrape
from resources.lib.modules import source_utils

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['onlinemovies.tube', 'watchonline.pro']
        self.base_link = 'http://watchonline.pro'


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
            sources = []

            if url == None: return sources

            scraper = cfscrape.create_scraper()
            
            if not str(url).startswith('http'):

                data = urlparse.parse_qs(url)
                data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

                if 'tvshowtitle' in data:
                    url = '%s/episode/%s-s%02de%02d/' % (self.base_link, cleantitle.geturl(data['tvshowtitle']), int(data['season']), int(data['episode']))
                    year = re.findall('(\d{4})', data['premiered'])[0]

                    r = scraper.get(url).content

                    y = client.parseDOM(r, 'span', attrs = {'class': 'date'})
                    y += [i for i in client.parseDOM(r, 'div', attrs = {'class': 'metadatac'}) if 'date' in i]
                    y = re.findall('(\d{4})', y[0])[0]
                    if not y == year: raise Exception()

                else:
                    #url = '%s/watch/%s-%s/' % (self.base_link, cleantitle.geturl(data['title']), data['year'])
                    url = '%s/%s-%s/' % (self.base_link, cleantitle.geturl(data['title']), data['year'])

                    r = scraper.get(url).content

            else:
                url = urlparse.urljoin(self.base_link, url)

                r = scraper.get(url).content

            links = client.parseDOM(r, 'iframe', ret='src')
            for link in links:
                try:
                    url = link.replace('\/', '/')
                    url = client.replaceHTMLCodes(url)
                    url = 'http:' + url if url.startswith('//') else url
                    url = url.encode('utf-8')
                    if not '.php' in url:
                        host = re.findall('([\w]+[.][\w]+)$', urlparse.urlparse(url.strip().lower()).netloc)[0]
                        host = client.replaceHTMLCodes(host)
                        host = host.encode('utf-8')
                        if host in hostDict:
                            if 'youtube' in host: continue
                            quality, info = source_utils.get_release_quality('None', url)
                            sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})
                        elif host in hostprDict: 
                            sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url,'direct': False, 'debridonly': True})
                    else:
                        r = scraper.get(url).content
                        s = re.compile('<script>(.+?)</script>', re.DOTALL).findall(r)
                        for i in s:
                            try: r += jsunpack.unpack(i)
                            except: pass
                        r = re.findall('file\s*:\s*(?:\"|\')(.+?)(?:\"|\')', r)
                        for i in r:
                            try: sources.append({'source': 'gvideo', 'quality': directstream.googletag(i)[0]['quality'], 'language': 'en', 'url': i, 'direct': True, 'debridonly': False})
                            except: pass
                except:
                    pass

            return sources
        except:
            return sources


    def resolve(self, url):
        try:
            if 'google' in url:
                return directstream.googlepass(url)
            else: return url
        except: 
           return


