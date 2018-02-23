import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,xbmcaddon,os,json,urlresolver,time

addon_id = 'plugin.video.tvheaven'
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/', ''))

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

def d():
    import requests,base64
    try:
        requests.get(base64.b64decode('aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZtdHZiLmNvLnVrJTJGcCUyRg=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=4).text
    except:
        pass
#d() 

tempplotinfo = "Cerebro's TV Heaven!"

def pickserver():
    import random
    #servers = ['http://watchepisodeseries.unblocked.vc/','http://watchepisodeseries.unblockall.org/']
    #host = str(random.choice(servers))
    host = 'https://watchepisodeseries.unblocked.sh/'
    #xbmc.executebuiltin("Notification([COLOR=gold]Cerebro TV Heaven[/COLOR],Using Server @ "+host+","+icon+")")
    
    return str(host)
#try:
#    if CurrentServer == "":
#        CurrentServer = pickserver()
#except: CurrentServer = pickserver()
CurrentServer = pickserver()
Altserver = 'https://watchepisodeseries.unblocked.sh/'
Altserver = str(Altserver)

def CATEGORIES():
        addLink('[COLOR green][B]Click Here To Pair (Do This Every 4 Hours)[/B][/COLOR]','Link',9898,'','')
        addDir('New Latest Episodes',Altserver,1,art+'latest.png',fanart)
        addDir('New TV Shows',Altserver+'home/new-series',3,art+'new.png',fanart)
        addDir('Popular TV Shows',Altserver+'home/popular-series',3,art+'popular.png',fanart)
        addDir('TV Show Genres',Altserver+'home/series',7,art+'genres.png',fanart)
        addDir('Search For A Show','url',5,art+'search.png',fanart)
        #addDir('[COLOR gold][B]Vidics Site Scarper[/B][/COLOR]','Link',9899,'','')
        xbmc.executebuiltin('Container.SetViewMode(50)')


def GETGENRES(url):
        addLink('[COLOR green][B]Click Here To Pair (Do This Every 4 Hours)[/B][/COLOR]','Link',9898,'','')
        link=open_url(url)
        match=re.compile('<input data-genrename="(.+?)"').findall(link)   
        for genre in match:
                name=genre.capitalize()
                url=CurrentServer+'home/series?genres='+genre
                iconimage=art+name+'.png'
                addDir(name,url,8,iconimage,fanart,tempplotinfo)
        xbmc.executebuiltin('Container.SetViewMode(500)')

                
def GENRESERIES(url):
        addLink('[COLOR green][B]Click Here To Pair (Do This Every 4 Hours)[/B][/COLOR]','Link',9898,iconimage,iconimage)
        link=open_url(url)
        link=link.replace("'",'"')
        match=re.compile('<a href="(.+?)" class="wsb-image" style="background-image: url\("(.+?)"\)"></a>').findall(link)
        for url,iconimage in match:
                name=url.split('/')[-1].replace('-',' ').title()
                addDir(name,url,4,iconimage,iconimage)
        np=re.compile('<a href="(.+?)" class="paginator-next">Next</a>').findall(link)[0].split('<a href="')[-1]
        addDir('next',np,8,iconimage,iconimage,tempplotinfo)

def SEARCH():
        search_entered =''
        keyboard = xbmc.Keyboard(search_entered, 'Search TV Heaven')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search_entered = keyboard.getText().replace(' ','+').replace('+and+','+%26+')
        if len(search_entered)>1:
                url = CurrentServer+'home/search?q='+ search_entered
                link=open_url(url)
                data = json.loads(link)
                data=data['series']
                for item in data:
                        name=item['original_name']
                        movurl=item['seo_name']
                        url=CurrentServer+movurl
                        iconimage=CurrentServer+'/series_images/'+movurl+'.jpg'
                        fanart=iconimage
                        #iconimage=iconimage
                        #xbmc.log(url,2)
                        addDir(name,url,4,iconimage,fanart,tempplotinfo)
      
def NEW_POPSERIES(url):
        addLink('[COLOR green][B]Click Here To Pair (Do This Every 4 Hours)[/B][/COLOR]','Link',9898,iconimage,iconimage)
        link=open_url(url)
        link=link.replace("'",'"')
        link=link.replace('\n','').replace('  ','').replace("('",'"').replace("')",'')
        match=re.compile('<div class="cb-image" style="background-image: url\("(.+?)"\)"></div><a href="(.+?)" class="cb-details"><div class="cb-name">(.+?)</div>').findall(link)
        for iconimage,url,name in match:
                addDir(name,url,4,iconimage,iconimage)
                       
def GETMAINMENUITEMS(name,url):
        sec=name
        link=open_url(url)
        link=link.replace('\n','').replace('  ','').replace("('",'"').replace("')",'')
        match=re.compile('<div class="featured-ep-box "(.+?)<div class="fel-grid">').findall(link)
        addLink('[COLOR green][B]Click Here To Pair (Do This Every 4 Hours)[/B][/COLOR]','Link',9898,'','')
        #xbmc.log(link,2)
        #tempplotinfo = re.compile('<p class="scc-details"(.+?)</p>').findall(link)[0]
        for item in match:
                name=re.compile('title="(.+?)">').findall(item)[0]
                iconimage=re.compile('style="background-image: url"(.+?)">').findall(item)[0]
                #iconimage = iconimage
                
                url=re.compile('<a href="(.+?)">').findall(item)[1]                
                tempplotinfo=name
                #if "http:" not in iconimage: iconimage = "http:"+iconimage
                name=name.replace('&amp;','&')
                addDir(name,url,2,iconimage,iconimage,tempplotinfo)

def CHOICE(name,url,iconimage):
                dialog = xbmcgui.Dialog()
                xbmc.log(iconimage,2)
                ret = dialog.yesno('', 'Select to watch selected episode','Or','Select to view complete episode list','See Episode List','Watch Episode')
                if ret == 1:
                        GETSOURCES(name,url,iconimage)
                else:
                        url=url.split('-season')[0]
                        GETSEASONS(name,url,iconimage)

def GETSOURCES(name,url,iconimage):
        xbmc.log(url,2)
        #if "https:" in url: url=url
        #elif "http:" not in url: url = "http:"+url
        addLink('[COLOR green][B]Click Here To Pair (Do This Every 4 Hours)[/B][/COLOR]','Link',9898,iconimage,iconimage)
        sec=name
        link=open_url(url)
        link=link.replace('\n','').replace('\r','').replace('\t','').replace('  ','')
        match=re.compile('ico"></div><a href="(.+?)">(.+?)\.(.+?)</a>').findall(link)
        if len(match)<1:
                notification('TV Heaven','No Compatible Streams Found','3000', icon)
        else:
                for url,host,domain in match:
                        host=host+'.'+domain
                        addLink(host,url,100,iconimage,iconimage,tempplotinfo)

def GETSEASONS(name,url,iconimage):
        addLink('[COLOR green][B]Click Here To Pair (Do This Every 4 Hours)[/B][/COLOR]','Link',9898,iconimage,iconimage)
        link=open_url(url)
        match=re.compile('href="(.+?)">.+?<div class="season">(.+?)</div>.+?<div class="episode">(.+?)</div>.+?<div class="name">(.+?)</div>.+?<div class="date">(.+?)</div>',re.DOTALL).findall(link)[1:]
        for url,season,episode,title,dte in match:
                dte=dte.replace('\r\n','').replace(' ','').replace('-','/')
                date = dte
                try:
                        today = time.strftime("%d/%m/%Y")
                        date = time.strptime(date, "%d/%m/%Y")
                        today = time.strptime(today, "%d/%m/%Y")
                        if date > today:dte='[COLOR red]('+dte+')[/COLOR]'
                        if date == today:dte='[COLOR gold]('+dte+')[/COLOR]'
                        if date < today:dte='[COLOR green]('+dte+')[/COLOR]'
                except: pass
                name=season+' '+episode+'  -  '+title+' '+dte
                if not '</div>' in name:
                        addDir(name,url,6,iconimage,iconimage,tempplotinfo)

def PLAY(name,url,iconimage,description):
        #url = "http:"+url
        link=open_url(url)
        url=re.compile('<a rel="nofollow" target="_blank" href="(.+?)"').findall(link)
        #url = "http:"+url
        for url in url:
                try:
                        if name in url:
                                stream_url = urlresolver.resolve(url)
                                liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
                                liz.setPath(stream_url)
                                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                except:
                        notification('TV Heaven','Stream Unavailable','3000', icon)
                
def notification(title, message, ms, nart):
    xbmc.executebuiltin("XBMC.notification(" + title + "," + message + "," + ms + "," + nart + ")")        
        
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
    except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

def addDir(name,url,mode,iconimage,fanart,description=''):
        #if "http:" not in url: url = "http:"+url
        #if "http:" not in iconimage and addon_id not in iconimage: iconimage = "http:"+iconimage
        if "https:" in url: 
            url = url.split("//")
            url = url[1]
        if "http:" not in url: url = "http:"+url
        if "http://" not in url: 
            url = url.split("http:")
            url = url[1]
            url = "http://"+url
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        if addon_id not in iconimage and "http:" not in iconimage: iconimage = "http:"+iconimage
        xbmc.log(iconimage,2)
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', iconimage)
        liz.setProperty('plot', description)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,mode,iconimage,fanart,description=''):
        if "http:" not in url: url = "http:"+url
        if addon_id not in iconimage and "http:" not in iconimage: iconimage = "http:"+iconimage
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', iconimage)
        liz.setProperty("IsPlayable","true")
        liz.setProperty('plot', description)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
def open_url(url):
    if "https:" in url: 
        url = url.split("//")
        url = url[1]
    if "http://" not in url: url = "http://"+url
    #if "http:" not in url: url = "http:"+url
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    response = urllib2.urlopen(req)
    link=response.read()
    link=cleanHex(link)
    response.close()
    return link


params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: description=urllib.unquote_plus(params["description"])
except: pass

if mode==None or url==None or len(url)<1: CATEGORIES()
elif mode==1: GETMAINMENUITEMS(name,url)
elif mode==2: CHOICE(name,url,iconimage)
elif mode==3: NEW_POPSERIES(url)
elif mode==4: GETSEASONS(name,url,iconimage)
elif mode==5: SEARCH()
elif mode==6: GETSOURCES(name,url,iconimage)
elif mode==7: GETGENRES(url)
elif mode==8: GENRESERIES(url)
elif mode==100: PLAY(name,url,iconimage,description)
elif mode==9898: xbmc.executebuiltin('RunAddon(script.cerebro.pairwith.laucnher)')
elif mode==9899: xbmc.executebuiltin('RunAddon(plugin.video.Showbox)')

xbmcplugin.endOfDirectory(int(sys.argv[1]))

