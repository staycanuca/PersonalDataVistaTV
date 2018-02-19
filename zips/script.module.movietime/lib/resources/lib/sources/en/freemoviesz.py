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

import re, urllib, urlparse, json, base64
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import aadecoder
from resources.lib.modules import directstream
from resources.lib.modules import jsunpack
from resources.lib.modules import dom_parser2
from resources.lib.modules import source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['freemoviesz.to']
        self.base_link = 'https://freemoviesz.to/'
        self.search_link = 'search?q=%s'
        self.token_link = 'https://embed.streamdor.co/token.php?v=5'
        self.source_link = 'https://api.streamdor.co/sources'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year, 'aliases': aliases}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year, 'aliases': aliases}
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

    def searchShow(self, title, season):
        try:
            sea = '%s Season %d' % (title, int(season))
            query = self.search_link % urllib.quote_plus(cleantitle.getsearch(sea))
            url = urlparse.urljoin(self.base_link, query)
            r = client.request(url)
            r = client.parseDOM(r, 'div', attrs={'class': 'block_1__info uk-position uk-position-bottom uk-overlay uk-overlay-primary'})
            r = [(dom_parser2.parse_dom(i, 'a', req='href')[0],
                  client.parseDOM(i, 'small')[0]) for i in r if i]
            r = [(i[0].attrs['href']) for i in r if  cleantitle.get_simple(sea) in cleantitle.get_simple(i[0].content)]

            url = r[0]
            return url
        except:
            return

    def searchMovie(self, title, year):
        try:
            query = self.search_link % urllib.quote_plus(cleantitle.getsearch(title+' '+year))
            url = urlparse.urljoin(self.base_link, query)
            r = client.request(url)
            r = client.parseDOM(r, 'div', attrs={'class': 'block_1__info uk-position uk-position-bottom uk-overlay uk-overlay-primary'})
            r = [(dom_parser2.parse_dom(i, 'a', req='href')[0],
                  client.parseDOM(i, 'small')[0]) for i in r if i]
            r = [(i[0].attrs['href'], i[0].content) for i in r if year in i[1]]
            r = [i[0] for i in r if cleantitle.get_simple(i[1]) == cleantitle.get_simple(title)]
            url = r[0]
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url is None: return sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            try:
                if 'tvshowtitle' in data:
                    episode = int(data['episode'])
                    url = self.searchShow(data['tvshowtitle'], data['season'])
                    url = url.replace('film', 'watch')
                    r = client.request(url)
                    links = client.parseDOM(r, 'div', attrs={'class': 'block_7'})
                    links = dom_parser2.parse_dom(r, 'option', req='value')
                    links = [(i.attrs['value'], i.content) for i in links if 'Episode %02d' % int(episode) in i.content]
                    links = [i[0] for i in links if i]

                else:
                    url = self.searchMovie(data['title'], data['year'])
                    url = url.replace('film', 'watch')
                    r = client.request(url)
                    links = client.parseDOM(r, 'div', attrs={'class':'block_7'})
                    links = client.parseDOM(links, 'div', attrs={'class':'uk-width-expand'})
                    links = [dom_parser2.parse_dom(i, 'a', req='href')[0] for i in links if i]
                    links = [(i.attrs['href'], i.attrs['title'], i.content) for i in links if i]
                    links = [(i[0])for i in links if i]
            except:
                pass


            for url in links:
                data = client.request(url)
                vid = aadecoder.decode(data)
                vid = client.parseDOM(vid, 'iframe', ret='src')[0]
                vid_id = re.findall('video/\w+$', vid)[0]
                p = client.request(vid, referer=url)
                try:
                    p = re.findall(r'JuicyCodes.Run\(([^\)]+)', p, re.IGNORECASE)[0]
                    p = re.sub(r'\"\s*\+\s*\"', '', p)
                    p = re.sub(r'[^A-Za-z0-9+\\/=]', '', p)
                    p = base64.b64decode(p)
                    p = jsunpack.unpack(p)
                    p = unicode(p, 'utf-8')
                except:
                    continue

                try:

                    fl = re.findall(r'file"\s*:\s*"([^"]+)', p)
                    if len(fl) > 0:
                        fl = fl[0]
                        post = {'episodeID': vid_id, 'file': fl, 'subtitle': 'false',
                                'referer': urllib.quote_plus(url)}
                        p = client.request(self.source_link, post=post, referer=vid, XHR=True)
                        js = json.loads(p)
                        src = js['sources']
                        p = client.request('http:' + src, referer=src)
                        js = json.loads(p)[0]
                        ss = js['sources']
                        ss = [(i['file'], i['label']) for i in ss if 'file' in i]

                    else:
                        try:
                            post = {'id': vid_id}
                            p2 = client.request(self.token_link, post=post, referer=vid, XHR=True)
                            js = json.loads(p2)
                            tok = js['token']
                            p = re.findall(r'var\s+episode=({[^}]+});', p)[0]
                            js = json.loads(p)
                            ss = []
                            if 'eName' in js and js['eName'] != '':
                                quali = source_utils.label_to_quality(js['eName'])
                            if 'fileEmbed' in js and js['fileEmbed'] != '':
                                ss.append([js['fileEmbed'], quali])
                            if 'fileHLS' in js and js['fileHLS'] != '':
                                ss.append(['https://hls.streamdor.co/%s%s' % (tok, js['fileHLS']), quali])
                        except:
                            pass

                    for i in ss:
                        try:
                            valid, hoster = source_utils.is_host_valid(i[0], hostDict)
                            direct = False
                            if not valid:
                                hoster = 'CDN'
                                direct = True
                            sources.append({'source': hoster, 'quality': quali, 'language': 'en', 'url': i[0],
                                            'direct': direct, 'debridonly': False})
                        except:
                            pass

                except:
                    url = re.findall(r'embedURL"\s*:\s*"([^"]+)', p)[0]
                    valid, hoster = source_utils.is_host_valid(url, hostDict)
                    if not valid: continue
                    urls, host, direct = source_utils.check_directstreams(url, hoster)
                    for x in urls:
                        sources.append(
                            {'source': host, 'quality': 'SD', 'language': 'en', 'url': x['url'], 'direct': direct,
                             'debridonly': False})


            return sources
        except:
            return sources

    def resolve(self, url):
        try:
            if self.embed_link in url:
                result = client.request(url, XHR=True)
                url = json.loads(result)['embed_url']
                return url
            elif 'google' in url and not 'googleapis' in url:
                return directstream.googlepass(url)
            else:
                return url
        except:
            return



