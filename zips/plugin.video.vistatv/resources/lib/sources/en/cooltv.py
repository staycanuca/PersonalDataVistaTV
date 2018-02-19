# -*- coding: UTF-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# #Cerebro ShowBox Scraper
#Cerebro ShowBox Scraper
# Addon Provider: MuadDib

import re,urllib,urlparse,base64
import requests

from resources.lib.modules import client

session = requests.Session()

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['cooltvseries.com']
        self.base_link = 'https://cooltvseries.com'
        self.show_link = '%s/%s/season-%s/'

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
            urldata = urlparse.parse_qs(url)
            urldata = dict((i, urldata[i][0]) for i in urldata)
            tvshowtitle = urldata['tvshowtitle'].replace(' ', '-').lower()
            start_url = self.show_link  % (self.base_link,tvshowtitle,season)

            headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                       'Accept-Encoding':'gzip, deflate, sdch', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
            html = requests.get(start_url,headers=headers,timeout=5).content
            links = html.split('class="sidebar"')
            media_title = title.replace(' ', '')
            medial_links = re.compile('href="([^"]+)"').findall(links[1])
            for media_url in medial_links:
                if media_title.lower() in media_url.lower():
                    return media_url
        except Exception, argument:
            return
        return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            if url == None: return sources
            headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                       'Accept-Encoding':'gzip, deflate, sdch', 'Accept-Language':'en-US,en;q=0.8',
                        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
            html = client.request(url,headers=headers)
            divs = client.parseDOM(html, 'div', attrs = {'class': 'dwn-box'})
            for divcontent in divs:
                link = client.parseDOM(divcontent, 'a', ret='href')
                res = 'SD'
                if '1080' in link[0]:
                    res='1080p'                   
                elif '720' in link[0]:
                    res='720p'
                elif 'HD' in link[0]:
                    res='HD'
                redirect = client.request(link[0], output='geturl')
                sources.append({'source':'CoolTV','quality':res,'language': 'en','url':redirect,'info':[],'direct':True,'debridonly':False})
            return sources
        except:
            return sources

    def resolve(self, url):
        return url


