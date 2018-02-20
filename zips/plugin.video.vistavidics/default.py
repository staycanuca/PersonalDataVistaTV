import httplib
import urlparse,urllib,urllib2,re,sys
import cookielib,os,string,cookielib,StringIO,gzip
import os,time,base64,logging
from t0mm0.common.net import Net
import xml.dom.minidom
import xbmcaddon,xbmcplugin,xbmcgui,xbmc
import json
import urlresolver
import time,datetime
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import SoupStrainer

from xml.dom.minidom import Document
from t0mm0.common.addon import Addon
import commands
import jsunpack
import xbmc
import random

#xbmc.sleep(1000)  
#import html
#d()
#from thetvdb import TheTvDb
#self.tvdb_key.decode('base64')
#tvdb_key = 'MUQ2MkYyRjkwMDMwQzQ0NA=='
#tvdb = TheTvDb(tvdb_key.decode('base64'))


addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')
__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')


__settings__ = xbmcaddon.Addon(id='plugin.video.vistavidics')
xbmc.executebuiltin("Container.SetViewMode(522)")
home = __settings__.getAddonInfo('path')
#addon = Addon('plugin.video.1channel', sys.argv)
datapath = xbmc.translatePath(os.path.join(home, 'resources', ''))
#langfile = xbmc.translatePath(os.path.join(home, 'resources', 'lang.txt'))
#vidicshost = ["https://vidics.unblocked.pl","https://vidics.to","https://vidics.ch"]
strdomain ="https://www.vidics.to/" 
#strdomain ="https://vidics.unblocked.pl/"
#strdomain ="https://vidics.to"
#strdomain ="https://vidics.ch"
#strdomain = random.choice(vidicshost)
AZ_DIRECTORIES = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z']
playablehost=[
'daclips',
'watchTv%20Shows',
'watchTv Shows',
'movpod',
'novamov',
'watchepisodes',
'thevideo',
'trollvid',
'vidzi',
'vk',
'vodlocker',
'watchfree',
'google',
'vidx',
'estream',
'putlocker',
'grifthost',
'bitvid',
'vidgg',
'vidzella',
'vidto',
'clipwatching',
'veoh',
'videoweed',
'youtube',
'dailymotion',
'cloudtime',
'novamov',
'flashx',
'vidup',
'openload',
'streamcloud',
'nowvideo',
'putstream',
'vidlox',
'netu',
'thevideobee',
'gorillavid',
'vidoza',
'cloudtime',
'netu',
'streamin'
]


import re,os

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.vistavidics/') #   * = plugins name
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')     #  path to addon_data folder
ADDON_DATA = USERDATA_PATH + '/plugin.video.vistavidics/'                                     #  * = whatever you want to call folder
if not os.path.exists(ADDON_DATA):                                           # check if folder doesnt exist
    os.makedirs(ADDON_DATA)                                                  # create if it doesnt 
watched = ADDON_DATA + 'watched.txt'                                         # define watched as the path to txt file to store data 
if not os.path.exists(watched):                                              # check if it doesnt exist
    open(watched,'w+')                                                       # create if it doesnt
watched_read = open(watched).read()            # define watched_read as a way to open and read the file later on



net = Net()
class InputWindow(xbmcgui.WindowDialog):# Cheers to Bastardsmkr code already done in Putlocker PRO resolver.
    def __init__(self, *args, **kwargs):
        self.cptloc = kwargs.get('captcha')
        self.img = xbmcgui.ControlImage(335,20,624,180,self.cptloc)
        self.addControl(self.img)
        self.kbd = xbmc.Keyboard()

    def get(self):
        self.show()
        self.kbd.doModal()
        if (self.kbd.isConfirmed()):
            text = self.kbd.getText()
            self.close()
            return text
        self.close()
        return False
        
def GetContent(url):
    try:
       url=url.replace("putlocker.com","putlocker.ac")
       net = Net()
       second_response = net.http_GET(url)
       rcontent=second_response.content
       try:
            rcontent =rcontent.encode("UTF-8")
       except: pass
       return rcontent
    except: 
       d = xbmcgui.Dialog()
       d.ok(url,"Can't Connect to site",'Try again in a moment')

try:

    DB_NAME =    ADDON.getSetting('db_name')
    DB_USER =    ADDON.getSetting('db_user')
    DB_PASS =    ADDON.getSetting('db_pass')
    DB_ADDRESS = ADDON.getSetting('db_address')

    if  ADDON.getSetting('use_remote_db')=='true' and DB_ADDRESS is not None and DB_USER is not None and DB_PASS is not None and DB_NAME is not None:
        import mysql.connector as database
        print 'Loading MySQL as DB engine'
        DB = 'mysql'
    else:
        print'MySQL not enabled or not setup correctly'
        raise ValueError('MySQL not enabled or not setup correctly')

except:

    try: 
        from sqlite3 import dbapi2 as database
        print 'Loading sqlite3 as DB engine'
    except: 
        from pysqlite2 import dbapi2 as database
        addon.log('pysqlite2 as DB engine')
    DB = 'sqlite'
    db_dir = os.path.join(xbmc.translatePath("special://database"), 'vidicsfav.db')

def initDatabase():
    if DB == 'mysql':
        db = database.connect(DB_NAME, DB_USER, DB_PASS, DB_ADDRESS, buffered=True)
        cur = db.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS favorites (type VARCHAR(10), name TEXT, url VARCHAR(255) UNIQUE, imgurl VARCHAR(255))')
    else:
        if not os.path.isdir(os.path.dirname(db_dir)):
            os.makedirs(os.path.dirname(db_dir))
        db = database.connect(db_dir)
        db.execute('CREATE TABLE IF NOT EXISTS favorites (type, name, url, imgurl)')
    db.commit()
    db.close()
    
def SaveData(SQLStatement): #8888
    if DB == 'mysql':
        db = database.connect(DB_NAME, DB_USER, DB_PASS, DB_ADDRESS, buffered=True)
    else:
        db = database.connect( db_dir )
    cursor = db.cursor()
    cursor.execute(SQLStatement)
    db.commit()
    db.close()

def HostResolver(url):
        print "in HostResolver"
        parsed_uri = urlparse.urlparse(url)
        server=str(parsed_uri.netloc)
        #server=server.replace("openload.co","oload.stream")

        server=server.split(".")
        if(len(server)>2):
            server=server[1]
        else:
            server=server[0]
        server=server.replace("180upload","one80upload")
        server=server.replace(":","")
        exec "from servers import "+server+" as server_connector"
        rtnstatus,msg = server_connector.test_video_exists( page_url=url )
        if(rtnstatus):
            video_urls = server_connector.get_video_url( page_url=url , video_password="" )
            return video_urls[0][1]
        else:
            return ""
        
def SaveFav(fav_type, name, url, img):
        if fav_type == '': fav_type = getVideotype(url)
        statement  = 'INSERT INTO favorites (type, name, url, imgurl) VALUES (%s,%s,%s,%s)'
        if DB == 'mysql':
            db = database.connect(DB_NAME, DB_USER, DB_PASS, DB_ADDRESS, buffered=True)
        else:
            db = database.connect( db_dir )
            statement = statement.replace("%s","?")
        cursor = db.cursor()
        try: 
            cursor.execute(statement, (fav_type, urllib.unquote_plus(unicode(name,'latin1')), url, img))
            builtin = 'XBMC.Notification(Save Favorite,Added to Favorites,2000,'+__icon__+')'
            xbmc.executebuiltin(builtin)
        except database.IntegrityError: 
            builtin = 'XBMC.Notification(Save Favorite,Item already in Favorites,2000,'+__icon__+')'
            xbmc.executebuiltin(builtin)
        db.commit()
        db.close()
        
def AddFavContext(vidtype, vidurl, vidname, vidimg):
        runstring = 'RunScript(plugin.video.vidics,%s,?mode=22&vidtype=%s&name=%s&imageurl=%s&url=%s)' %(sys.argv[1],vidtype,vidname,vidimg,vidurl)
        #runstring = 'RunPlugin(%s)' % addon.build_plugin_url({'mode':22, 'vidtype':vidtype, 'name':vidname, 'url':vidurl, 'imageurl':vidimg})
        cm = add_contextsearchmenu(vidname,vidtype)
        cm.append(('Add to Vidics Favorites', runstring))
        return cm
def ListFavorites():
      addDir('TV','tv',25,'')
      addDir('Movies','movie',25,'')
def BrowseFavorites(section):
    sql = 'SELECT type, name, url, imgurl FROM favorites WHERE type = ? ORDER BY name'
    if DB == 'mysql':
        db = database.connect(DB_NAME, DB_USER, DB_PASS, DB_ADDRESS, buffered=True)
        sql = sql.replace('?','%s')
    else: db = database.connect( db_dir )
    cur = db.cursor()
    cur.execute(sql, (section,))
    favs = cur.fetchall()
    for row in favs:
        title      = row[1]
        favurl      = row[2]
        img      = row[3]
        vtype= row[0]
        fanart = ''
        cm = add_contextsearchmenu(title,vtype)
        remfavstring = 'RunScript(plugin.video.vidics,%s,?mode=23&name=%s&url=%s)' %(sys.argv[1],urllib.quote_plus(title.encode("utf-8")),urllib.quote_plus(favurl))
        cm.append(('Remove from Favorites', remfavstring))
        nextmode=7
        if(vtype=="movie"):
              nextmode=4
        addDirContext(title,favurl,nextmode,img,"",vtype,cm)
    db.close()

def DeleteFav(name,url): 
    builtin = 'XBMC.Notification(Remove Favorite,Removed '+name+' from Favorites,2000,'+__icon__+')'
    xbmc.executebuiltin(builtin)
    sql_del = 'DELETE FROM favorites WHERE name=%s AND url=%s'
    if DB == 'mysql':
            db = database.connect(DB_NAME, DB_USER, DB_PASS, DB_ADDRESS, buffered=True)
    else:
            db = database.connect( db_dir )
            sql_del = sql_del.replace('%s','?')
    cursor = db.cursor()
    cursor.execute(sql_del, (name, url))
    db.commit()
    db.close()
        
def HOME():
        addLink('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)','Cerebro',9898,__icon__)
        addDir('Search Movies','search',9,__icon__)
        addDir('Search TV Shows','search',10,__icon__)
        addDir('Search Actor, Actress, Producer & Director','search',15,__icon__)
        addDir('Recently Added Movies',strdomain+'/Category-Movies/Genre-Any/Letter-Any/LatestFirst/1.htm',26,__icon__)
        addDir('Recently Added TV Shows',strdomain+'/Category-TvShows/Genre-Any/Letter-Any/LatestFirst/1.htm',27,__icon__)
        #addDir('Favorites','Category-Movies',24,'')
        addDir('Movies A-Z','Category-Movies',16,__icon__)
        addDir('TV Shows A-Z','Category-TvShows',17,__icon__)
        addDir('Movies Genres','Category-Movies',18,__icon__)
        addDir('TV Shows Genres','Category-TvShows',19,__icon__)
        addDir('7 Day TV Schedule','TV Schedule',20,__icon__)
        addDir('Top Movies',strdomain+'/top/films.html',5,__icon__)
        addDir('Top TV Shows',strdomain+'/top/tvshows.html',6,__icon__)
        addDir('Movies 2010-2017',strdomain+'/Category-Movies/Genre-Any/2010-2017/Letter-Any/LatestFirst/1.htm',26,__icon__)
        addDir('Movies 2000-2010',strdomain+'/Category-Movies/Genre-Any/2000-2010/Letter-Any/LatestFirst/1.htm',26,__icon__)
        addDir('TV Shows 2010-2017',strdomain+'/Category-TvShows/Genre-Any/2010-2017/Letter-Any/LatestFirst/1.htm',27,__icon__)
        addDir('TV Shows 2000-2010',strdomain+'/Category-TvShows/Genre-Any/2000-2010/Letter-Any/LatestFirst/1.htm',27,__icon__)
        addDir('TV Shows (Comedy) 1980-1990',strdomain+'/Category-TvShows/Genre-comedy/1980-1990/Letter-Any/LatestFirst/1.htm',27,__icon__)
def LangOption():
        addDir('Show Top Languages','Top',10,'')
        addDir('Show All Languages','All',10,'')
        
def CheckRedirect(url):
    try:
       net = Net()
       second_response = net.http_GET(url)
       cj = net.get_cookies()
       return (second_response,cj)
    except:
       d = xbmcgui.Dialog()
       d.ok(url,"Can't Connect to site",'Try again in a moment')

def getSchedule(sched_date): 
        url=strdomain+"/calendar/"+sched_date+ ".html"
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')
        listcontent=re.compile('<div class="indexClanedarDay left" id="date_'+sched_date+'">(.+?)</div>').findall(newlink)
        if(len(listcontent)>0):
                latestepi=re.compile('<h3 itemscope itemtype="http://schema.org/TVTv%20Shows" class="CalTvshow" title="(.+?)">(.+?)</h3>').findall(listcontent[0])
                for vtmp,vcontent in latestepi:
                        (sUrl,stmp,sName)=re.compile('<a itemprop="url" class="CalTVshowName pukeGreen" href="(.+?)" title="(.+?)">(.+?)</a>').findall(vcontent)[0]
                        (eUrl,eName)=re.compile('<a itemprop="url" class="CalTVshowEpisode blue" href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(vcontent)[0]
                        addDirContext(RemoveHTML(sName),strdomain+sUrl,7,"","","tv")
                        addDir("  --"+RemoveHTML(eName),strdomain+eUrl,4,"")  
def List4Days():
        sched_date=str(datetime.date.today())
        date_name=time.strftime("%A", time.strptime(sched_date, "%Y-%m-%d"))
        addDir("Today's("+sched_date+") TV Schedule",sched_date,21,"episode")
        sched_date=str(datetime.date.today()-datetime.timedelta(days=1))
        date_name=time.strftime("%A", time.strptime(sched_date, "%Y-%m-%d"))
        addDir(date_name+"'s("+sched_date+") TV Schedule",sched_date,21,"episode")
        sched_date=str(datetime.date.today()-datetime.timedelta(days=2))
        date_name=time.strftime("%A", time.strptime(sched_date, "%Y-%m-%d"))
        addDir(date_name+"'s("+sched_date+") TV Schedule",sched_date,21,"episode")
        sched_date=str(datetime.date.today()-datetime.timedelta(days=3))
        date_name=time.strftime("%A", time.strptime(sched_date, "%Y-%m-%d"))
        addDir(date_name+"'s("+sched_date+") TV Schedule",sched_date,21,"episode")
        sched_date=str(datetime.date.today()-datetime.timedelta(days=4))
        date_name=time.strftime("%A", time.strptime(sched_date, "%Y-%m-%d"))
        addDir(date_name+"'s("+sched_date+") TV Schedule",sched_date,21,"episode")
        sched_date=str(datetime.date.today()-datetime.timedelta(days=5))
        date_name=time.strftime("%A", time.strptime(sched_date, "%Y-%m-%d"))
        addDir(date_name+"'s("+sched_date+") TV Schedule",sched_date,21,"episode")
        sched_date=str(datetime.date.today()-datetime.timedelta(days=6))
        date_name=time.strftime("%A", time.strptime(sched_date, "%Y-%m-%d"))
        addDir(date_name+"'s("+sched_date+") TV Schedule",sched_date,21,"episode")
        
def Mirrors(url,name,image=""):
  #xbmc.PlayList(1).clear()
  #pl=xbmc.PlayList(1)
  #pl.clear()
  xbmcplugin.setContent(addon_handle, 'movies')
  link = GetContent(url)
  link=''.join(link.splitlines()).replace('\'','"')
  try:vimg=re.compile('<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[6]
  except: pass
  try:vimg=re.compile('<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[4]
  #vimg = vimg.encode("utf8")  
  except: pass
  ####xbmc.log("Name?? "+url,2)
  try:
	metaname = url.split('Serie/', 1)[1]
	metaname = metaname.split('Season', 1)[0]
  except: pass
  if "arrow.png" in vimg:
    vimg=re.compile('<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[6]
  ####xbmc.log("Image?? "+name,2)
  if "No_Poster" in vimg: 
    ####xbmc.log(vtitle+" Change For",2)
    try:
        ctitle = metaname.replace("-","%20")
        response = urllib2.urlopen('http://thetvdb.com/api/GetSeries.php?seriesname='+str(ctitle)).read()
        ####xbmc.log("NAME WE GETTING NOW"+ctitle,2)
        #####xbmc.log(response,2)
        sid=response.split('<seriesid>', 1)[1]
        sid=response.split('</seriesid>', 1)[0]
        sid=sid.split('<seriesid>', 1)[1]
        getimg=response.split('<Overview>', 1)[1]
        getimg=getimg.split('</Overview>', 1)[0]
        #getimg=getimg.split('</banner>', 1)[0]
        response = urllib2.urlopen('http://thetvdb.com/api/4144331619000000/series/'+sid+'/banners.xml').read()
        #####xbmc.log(response,2)
        gpost = response.split('<ThumbnailPath>', 1)[1]
        gpost = gpost.split('</ThumbnailPath>', 1)[0]
        #gpost = gpost.split('<BannerPath>', 1)[0]
        vimg = "http://www.thetvdb.com/banners/"+gpost
        #response = urllib2.urlopen('http://thetvdb.com/api/4144331619000000/series/'+sid+'/all/en.xml').read()
        ####xbmc.log("http://www.thetvdb.com/banners/posters"+gpost,2)
    except: pass
  soup = BeautifulSoup(link)
  listcontent=soup.findAll('a',{"href":re.compile("/Link/")})
  addLink('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)','Cerebro',9898,__icon__)
  #listcontent.sort() 
  for item in listcontent:
            vname=item.contents[0]
            vurl=item["href"]
            if(str(vname).split('.')[0].lower() in playablehost):
                vname = vname.split('.')[0].lower()
                name = name.replace("unknown","[I][COLOR grey]No Show Info[/COLOR][/I]")
                if vname == "thevideo":
                    vname = vname+" [COLOR lightblue](PAIR)[/COLOR]"
                if vname == "openload":
                    vname = vname+" [COLOR lightblue](PAIR)[/COLOR]"
                if vname == "vshare":
                    vname = vname+" [COLOR lightblue](PAIR)[/COLOR]"
                if vname == "flashx":
                    vname = vname+" [COLOR lightblue](PAIR)[/COLOR]"
                if vname == "vidup":
                    vname = vname+" [COLOR lightblue](PAIR)[/COLOR]"
                ####xbmc.log("Movie Image "+vimg,2)
                if "http" not in vimg: vimg = strdomain+vimg
                #addLink(" [COLOR gold]"+str(vname)+"[/COLOR] - [COLOR white]"+str(name)+"[/COLOR]",str(strdomain)+str(vurl),3,str(vimg),str(name))
                addLink(str(vname),str(strdomain)+str(vurl),3,str(vimg),str(name))
                #listitem = xbmcgui.ListItem(str(vname),thumbnailImage=str(vimg))
                #try: 
                #    resurl = ParseVideoLink(str(strdomain)+str(vurl),str(name),"TEST")
                #    xbmc.PlayList(1).add(resurl, listitem)
                #except: pass
                #xbmc.Player().play(pl)
                #except: pass
  #listcontent.insert(0,"addDir('[COLOR green][B]Pair For More HD Content[/B][/COLOR]','Link',9898,'')")
  #xbmc.Player().play(pl)  #playVideo(url,name,movieinfo)
  
def add_contextsearchmenu(title, video_type):
    title=urllib.quote(title)
    contextmenuitems = []
    #if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.1channel'):
    #    contextmenuitems.append(('Search 1channel',
    #                             'XBMC.Container.Update(%s?mode=%s&section=%s&query=%s)' % (
    #                                 'plugin://plugin.video.1channel/', '7000',video_type, title)))
    #if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.icefilms'):
    #    contextmenuitems.append(('Search Icefilms',
    #                             'XBMC.Container.Update(%s?mode=555&url=%s&search=%s&nextPage=%s)' % (
    #                                 'plugin://plugin.video.icefilms/', 'http://icefilms.unblocked.pro/', title, '1')))
    #if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.movie25'):
    #    contextmenuitems.append(('Search Mash Up',
    #                             'XBMC.Container.Update(%s?mode=%s&url=%s)' % (
    #                                 'plugin://plugin.video.movie25/', '4', title)))
    #if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.tubeplus'):
    #    if video_type == 'tv':
    #        section = 'None'
    #        serurl='http://www.tubeplus.me/search/tv-shows/%s/'%(title)
     #   else:
    #        serurl='http://www.tubeplus.me/search/movies/"%s"/'%(title)
    #        section = 'movie'
    #   
    #    contextmenuitems.append(('Search tubeplus', 'XBMC.Container.Update(%s?mode=150&types=%s&url=%s&linkback=latesttv)' % (
    #        'plugin://plugin.video.tubeplus/', section, serurl)))
    #if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.tvlinks'):
    #    if video_type == 'tv':
    #        contextmenuitems.append(('Search tvlinks', 'XBMC.Container.Update(%s?mode=Search&query=%s)' % (
    #            'plugin://plugin.video.tvlinks/', title)))
    #if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.solarmovie'):
    #    if video_type == 'tv':
    #        section = 'tv-shows'
    #    else:
    #        section = 'movies'
    #    contextmenuitems.append(('Search solarmovie', 'XBMC.Container.Update(%s?mode=Search&section=%s&query=%s)' % (
    #        'plugin://plugin.video.solarmovie/', section, title)))

    #contextmenuitems.insert(0,"addDir('[COLOR green][B]Pair For More HD Content[/B][/COLOR]','Link',9898,'')")
    xbmcplugin.setContent(addon_handle, 'movies')
    return contextmenuitems


        
def GetParts(vicontent,vidname):
        dialog = xbmcgui.Dialog()
        titles = []
        urlcontent=re.compile('<div class="movie_link1">(.+?)</div>').findall(vicontent)
        urllist=[]
        for ucontent in urlcontent:
            titletext=re.compile('<h4>(.+?)</h4>').findall(ucontent)[0]
            url=re.compile('<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>').findall(ucontent)[0]
            titles.append(titletext)
            urllist.append(url)
        #index = dialog.select('Choose your stream', titles)
        #win = xbmcgui.Window(10000)
        #win.setProperty('1ch.playing.episode', str(index))
        return CheckRedirect(urllist[0])
        
def ParseVideoLink(url,name,movieinfo):
    dialog = xbmcgui.DialogProgress()
    dialog.create('Resolving', 'Resolving video Link..........')    
    dialog.update(0)
    (respon,cj) = CheckRedirect(url)
    link=respon.content
    tmpcontent=link
    dialog.update(5)
    redirlink = respon.get_url() #.lower()
    #link=link.replace(":","&")
    link = ''.join(link.splitlines()).replace('\'','"')
    link=link.replace("openload.co","oload.stream")
    link=link.replace("openload.co","oload.stream")
    link=link.replace("putlocker.com","putlocker.unblocked.pl")
    #link=link.replace("https&","https:")
    #link=link.replace("http&","http:")
    #link2=link[:-1]
    #if "oload.stream" in link:
    #link[::-1].replace(':','',1)[::-1]


    dialog.update(10)
    if(redirlink.find("vidics") >-1):
            (respon,cj) = GetParts(link,name)
            link=respon.content
            tmpcontent=link
            redirlink = respon.get_url() #.lower()
            link = ''.join(link.splitlines()).replace('\'','"')
            #link=link[:-1]
    # end 1channel code
    print redirlink
    #try:
    dialog.update(20)
    if True:

        if (redirlink.find("youtube") > -1):
                vidmatch=re.compile('(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)').findall(redirlink)
                vidlink=vidmatch[0][len(vidmatch[0])-1].replace('v/','')
                vidlink='plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid='+vidlink
        elif (redirlink.find("yourupload") > -1):
                media_url= ""
                media_url = re.compile('<meta property="og:video" content="(.+?)"/>').findall(link)[0]
                vidlink = media_url
        elif (redirlink.find("video44") > -1):
                media_url= ""
                media_url = re.compile('url:\s*"(.+?)"').findall(link)[0]
                vidlink = media_url
        elif (redirlink.find("videobug") > -1):
                media_url= ""
                media_url = re.compile('playlist:\s*\[\s*\{\s*url:\s*"(.+?)",').findall(link)[0]
                vidlink = urllib.unquote(media_url)
        elif (redirlink.find("letwatch") > -1):
                paccked= re.compile('<script type=(?:"|\')text/javascript(?:"|\')>(eval\(function\(p,a,c,k,e,d\).*?)</script>').findall(link)
                if(len(paccked) > 0):
                      link=jsunpack.unpack(paccked[0].replace('"','\''))
                else:
                      idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                      op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                      hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                      fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                      posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":"","hash":hash})
                      link=postContent(redirlink,posdata+"&imhuman=Proceed+to+video",url)
                      link=''.join(link.splitlines()).replace('\'','"')
                      paccked= re.compile('<script type=(?:"|\')text/javascript(?:"|\')>(eval\(function\(p,a,c,k,e,d\).*?)</script>').findall(link)
                      if(len(paccked) > 0):
                             link=jsunpack.unpack(paccked[0].replace('"','\''))
                media_url = re.compile("sources:\s*\[\{file:\s*'(.+?)'").findall(link.replace('"','\''))[0]
                vidlink = urllib.unquote(media_url)
        elif (redirlink.find("video.google.com") > -1):
                match=redirlink.split("docid=")
                glink=""
                newlink=redirlink+"&dk"
                if(len(match) > 0):
                        glink = GetContent("http://www.flashvideodownloader.org/download.php?u=http://video.google.com/videoplay?docid="+match[1].split("&")[0])
                else:
                        match=re.compile('http://video.google.com/googleplayer.swf.+?docId=(.+?)&dk').findall(newlink)
                        if(len(match) > 0):
                                glink = GetContent("http://www.flashvideodownloader.org/download.php?u=http://video.google.com/videoplay?docid="+match[0])
                gcontent=re.compile('<div class="mod_download"><a href="(.+?)" title="Click to Download">').findall(glink)
                if(len(gcontent) > 0):
                        vidlink=gcontent[0]
                else:
                        vidlink=""
        elif (redirlink.find("vidx") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":"","hash":hash})
                dialog.close()
                do_wait('Waiting on link to activate', '', 10)
                dialog.create('Resolving', 'Resolving vidx Link...') 
                dialog.update(50)
                pcontent=postContent(redirlink,posdata+"&imhuman=Weiter+%2F+continue",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('setup\(\{\s*file:\s*"(.+?)",\s*').findall(pcontent)
                if(len(vidlink) == 0):
                        vidlink = re.compile('"file","(.+?)"').findall(pcontent)
                vidlink=vidlink[0]
        elif (redirlink.find("realvid") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":"","hash":hash})
                pcontent=postContent(redirlink,posdata+"&imhuman=Proceed+to+video",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                paccked= re.compile('<script type=(?:"|\')text/javascript(?:"|\')>(eval\(function\(p,a,c,k,e,d\).*?)</script>').findall(pcontent)
                if(len(paccked) > 0):
                      pcontent=jsunpack.unpack(paccked[0].replace('"','\''))
                vidlink = re.compile("file:\s*'(.+?)'").findall(pcontent.replace('"','\''))[0]
        elif (redirlink.find("happystreams") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":"","hash":hash})
                pcontent=postContent(redirlink,posdata+"&imhuman=Proceed+to+video",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                paccked= re.compile('<script type=(?:"|\')text/javascript(?:"|\')>(eval\(function\(p,a,c,k,e,d\).*?)</script>').findall(pcontent)
                if(len(paccked) > 0):
                      pcontent=jsunpack.unpack(paccked[0].replace('"','\''))
                vidlink = re.compile("file:\s*'(.+?)'").findall(pcontent)[0]

        elif (redirlink.find("playhd") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":"","hash":hash})
                pcontent=postContent(redirlink,posdata+"&imhuman=Proceed%20to%20video",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('file:\s*"(.+?)",').findall(pcontent)
                if(len(vidlink) == 0):
                        vidlink = re.compile('"file","(.+?)"').findall(pcontent)
                vidlink=vidlink[0]
        elif (redirlink.find("slickvid") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":"","hash":hash})
                dialog.close()
                do_wait('Waiting on link to activate', '', 5)
                dialog.create('Resolving', 'Resolving slickvid Link...') 
                dialog.update(50)
                pcontent=postContent(redirlink,posdata+"&imhuman=Watch",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('file:\s*"(.+?)",').findall(pcontent)
                if(len(vidlink) == 0):
                        vidlink = re.compile('"file","(.+?)"').findall(pcontent)
                vidlink=vidlink[0]
        elif (redirlink.find("vidpaid") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":"","hash":hash})
                dialog.close()
                do_wait('Waiting on link to activate', '', 1)
                dialog.create('Resolving', 'Resolving vidpaid Link...') 
                dialog.update(50)
                pcontent=postContent(redirlink,posdata+"&imhuman=Continue+to+Video",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('setup\(\{\s*file:\s*"(.+?)",\s*').findall(pcontent)
                if(len(vidlink) == 0):
                        vidlink = re.compile('"file","(.+?)"').findall(pcontent)
                vidlink=vidlink[0]
        elif (redirlink.find("filehoot") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download1","fname":fname,"id":idkey,"referer":url,"method_free":"Continue+to+watch+your+Video","down_direct":"1"})
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('file:\s*"(.+?)"').findall(pcontent)
                if(len(vidlink) == 0):
                        vidlink = re.compile('"file","(.+?)"').findall(pcontent)
                vidlink=vidlink[0]
        elif (redirlink.find("skyvid") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                rand = re.compile('<input type="hidden" name="rand" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download2","rand":rand,"id":idkey,"referer":url,"method_free":"","method_premium":"","down_direct":"1"})
                dialog.close()
                do_wait('Waiting on link to activate', '', 5)
                dialog.create('Resolving', 'Resolving cloudyvideos Link...') 
                dialog.update(50)
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                paccked= re.compile('<script type=(?:"|\')text/javascript(?:"|\')>(eval\(function\(p,a,c,k,e,d\).*?)</script>').findall(pcontent)
                if(len(paccked) > 1):
                      pcontent=jsunpack.unpack(paccked[1].replace('"','\''))
                vidlink = re.compile("file:\s*'(.+?)'").findall(pcontent.replace('"','\''))
                if(len(vidlink) == 0):
                        vidlink = re.compile('"file","(.+?)"').findall(pcontent)
                vidlink=vidlink[0] +"|"+urllib.urlencode( {'Referer':'http://skyvids.net/player/jw5.swf','User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; es-ES; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12'} )
        elif (redirlink.find("cloudyvideos") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                rand = re.compile('<input type="hidden" name="rand" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download2","rand":rand,"id":idkey,"referer":url,"method_free":"","method_premium":"","down_direct":"1"})
                dialog.close()
                do_wait('Waiting on link to activate', '', 2)
                dialog.create('Resolving', 'Resolving cloudyvideos Link...') 
                dialog.update(50)
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('file:\s*"(.+?)"').findall(pcontent)
                if(len(vidlink) == 0):
                        vidlink = re.compile('"file","(.+?)"').findall(pcontent)
                vidlink=vidlink[0]
        elif (redirlink.find("uploadnetwork") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                rand = re.compile('<input type="hidden" name="rand" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download2","rand":rand,"id":idkey,"referer":url,"method_free":"","method_premium":"","down_direct":"1"})
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('"file":\s*"(.+?)"').findall(pcontent)
                if(len(vidlink) == 0):
                        vidlink = re.compile('"file","(.+?)"').findall(pcontent)
                vidlink=vidlink[0]
        elif (redirlink.find("divxpress") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                rand = re.compile('<input type="hidden" name="rand" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download2","rand":rand,"id":idkey,"referer":url,"method_free":"","method_premium":"","down_direct":"1"})
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('swfobject.js"></script><script type="text/javascript">(.+?)</script>').findall(pcontent)
                if(len(packed) == 0):
                      packed = re.compile('<div id="player_code"><script type="text/javascript">(.+?)</script>').findall(pcontent)[0]
                      sUnpacked = unpackjs4(packed).replace("\\","")
                      vidlink = re.compile('src="(.+?)"').findall(sUnpacked)[0]
                else:
                      packed=packed[0]
                      sUnpacked = unpackjs4(packed).replace("\\","")
                      vidlink = re.compile('addVariable\("file",\s*"(.+?)"\)').findall(sUnpacked)

        elif (redirlink.find("videopremium") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                mfree = re.compile('<input type="submit" name="method_free" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download1","usr_login":"","id":idkey,"referer":"","method_free":mfree})
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('src="/swfobject.js"></script>\s*<script type="text/javascript">(.+?)</script>').findall(pcontent)[0]
                sUnpacked = unpackjs4(packed)  
                vidpart = re.compile('"file":"(.+?)",p2pkey:"(.+?)"').findall(sUnpacked)[0]
                vidswf = re.compile('embedSWF\("(.+?)",').findall(sUnpacked)[0]
                vidlink=""
                if(len(vidpart) > 0):
                        vidlink = "rtmp://e9.md.iplay.md/play/"+vidpart[1]+" swfUrl="+vidswf+" playPath="+vidpart[1] +" pageUrl=" + redirlink + " tcUrl=rtmp://e9.md.iplay.md/play"
                #vidlink="rtmp://e9.md.iplay.md/play/mp4:rx90tddtnfmc.f4v swfUrl=http://videopremium.tv/uplayer/uppod.swf pageUrl=http://videopremium.tv/rx90tddtnfmc playPath=mp4:rx90tddtnfmc.f4v tcUrl=rtmp://e9.md.iplay.md/play"
        elif (redirlink.find("faststream") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download1","usr_login":"","id":idkey,"fname":fname,"referer":url,"hash":hash})
                dialog.close()
                do_wait('Waiting on link to activate', '', 3)
                dialog.create('Resolving', 'Resolving faststream Link...') 
                dialog.update(50)
                pcontent=postContent(redirlink,posdata+"&imhuman=Continue+to+video",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('file:\s*"(.+?)",').findall(pcontent)[0]
        elif (redirlink.find("videomega") > -1):
                refkey= re.compile('\?ref=(.+?)&dk').findall(redirlink+"&dk")[0]
                vidcontent="http://videomega.tv/iframe.php?ref="+refkey
                pcontent=GetContent(vidcontent)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                urlcode = re.compile('else\{\s*document.write\(unescape\("(.+?)"\)\);').findall(pcontent)[0]
                vidcontent=urllib.unquote_plus(urlcode)
                vidlink = re.compile('file:\s*"(.+?)"\s*,').findall(vidcontent)[0]
        elif (redirlink.find("v-vids") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                rand = re.compile('<input type="hidden" name="rand" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download2","rand":rand,"id":idkey,"referer":url,"method_free":"","method_premium":"","down_direct":"1"})
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('file:\s*"(.+?)",').findall(pcontent)[0]
        elif (redirlink.find("thefile") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                rand = re.compile('<input type="hidden" name="rand" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download2","rand":rand,"id":idkey,"referer":url,"method_free":"","method_premium":"","down_direct":"1"})
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink = re.compile('<span>\s*<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>\s*</span>').findall(pcontent)[0][0]
        elif (redirlink.find("topvideo") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download1","usr_login":"","id":idkey,"fname":fname,"referer":url,"hash":hash})
                pcontent=postContent(redirlink,posdata+"&imhuman=Proceed+to+video",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('jwplayer.key="(.+?)";</script>\s*<script type="text/javascript">(.+?)</script>').findall(pcontent)[0][1]
                sUnpacked = unpackjs4(packed)
                unpacked = sUnpacked.replace("\\","")
                vidlink = re.compile('file:"(.+?)",').findall(unpacked)[0]
        elif (redirlink.find("gamovideo") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                hash = re.compile('<input type="hidden" name="hash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download1","usr_login":"","id":idkey,"fname":fname,"referer":url,"hash":hash})
                dialog.close()
                do_wait('Waiting on link to activate', '', 5)
                dialog.create('Resolving', 'Resolving gamovideo Link...') 
                dialog.update(50)
                pcontent=postContent(redirlink,posdata+"&imhuman=Proceed+to+video",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('/jwplayer.js"></script>\s*<script type="text/javascript">(.+?)</script>').findall(pcontent)[0]
                sUnpacked = unpackjs4(packed)
                unpacked = sUnpacked.replace("\\","")
                vidlink = re.compile('file:"(.+?)",').findall(unpacked)[0]

        elif (redirlink.find("exashare") > -1):
                packed = re.compile('/jwplayer.js"></script>\s*<script type="text/javascript">(.+?)</script>').findall(link)[0]
                sUnpacked = unpackjs4(packed)
                unpacked = sUnpacked.replace("\\","")
                vidlink = re.compile('file:"(.+?)",').findall(unpacked)[0]
        elif (redirlink.find("sharesix") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download1","usr_login":"","id":idkey,"fname":fname,"referer":url})
                pcontent=postContent(redirlink,posdata+"&method_free=Free",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('swfobject.js"></script>\s*<script type="text/javascript">(.+?)</script>').findall(pcontent)[0]
                unpacked = unpackjs4(packed)
                if unpacked=="":
                        unpacked = unpackjs3(packed,tipoclaves=2)
                        
                unpacked = unpacked.replace("\\","")
                vidlink = re.compile('.addVariable\("file",\s*"(.+?)"').findall(unpacked)[0]
        elif (redirlink.find("bonanzashare") > -1):
                capchacon =re.compile('<b>Enter code below:</b>(.+?)</table>').findall(link)
                capchar=re.compile('<span style="position:absolute;padding-left:(.+?);[^>]*>(.+?)</span>').findall(capchacon[0])
                capchar=sorted(capchar, key=lambda x: int(x[0].replace("px","")))
                capstring =""
                for tmp,aph in capchar:
                        capstring=capstring+chr(int(aph.replace("&#","").replace(";","")))
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                rand = re.compile('<input type="hidden" name="rand" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                ddirect = re.compile('<input type="hidden" name="down_direct" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"id":idkey,"referer":url,"method_free":"","rand":rand,"method_premium":"","code":capstring,"down_direct":ddirect})
                newpcontent=postContent(redirlink,posdata,url)
                newpcontent=''.join(newpcontent.splitlines()).replace('\'','"')
                vidlink=re.compile('<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>Download the file</a>').findall(newpcontent)[0] 
        elif (redirlink.find("videozed") > -1):
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" value="(.+?)">').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" value="(.+?)">').findall(link)[0]
                mfree = re.compile('<input type="submit" name="method_free"  value="(.+?)">').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":url,"method_free":mfree})
                pcontent=postContent(redirlink,posdata,strdomain+"/watch/120351/This-Is-40-2012.html")
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                capchacon =re.compile('<b>Enter code below:</b>(.+?)</table>').findall(pcontent)
                capchar=re.compile('<span style="position:absolute;padding-left:(.+?);[^>]*>(.+?)</span>').findall(capchacon[0])
                capchar=sorted(capchar, key=lambda x: int(x[0].replace("px","")))
                capstring =""
                for tmp,aph in capchar:
                        capstring=capstring+chr(int(aph.replace("&#","").replace(";","")))

                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(pcontent)[0]
                op = re.compile('<input type="hidden" name="op" value="(.+?)">').findall(pcontent)[0]
                mfree = re.compile('<input type="hidden" name="method_free" value="(.+?)">').findall(pcontent)[0]
                rand = re.compile('<input type="hidden" name="rand" value="(.+?)">').findall(pcontent)[0]
                ddirect = re.compile('<input type="hidden" name="down_direct" value="(.+?)">').findall(pcontent)[0]
                posdata=urllib.urlencode({"op":op,"id":idkey,"referer":url,"method_free":mfree,"rand":rand,"method_premium":"","code":capstring,"down_direct":ddirect})
                newpcontent=postContent(redirlink,posdata,url)
                newpcontent=''.join(newpcontent.splitlines()).replace('\'','"')
                packed = re.compile('<div id="player_code">(.+?)</div>').findall(newpcontent)[0]
                packed = packed.replace("</script>","")
                unpacked = unpackjs4(packed)  
                unpacked = unpacked.replace("\\","")
                vidsrc = re.compile('src="(.+?)"').findall(unpacked)
                if(len(vidsrc) == 0):
                         vidsrc=re.compile('"file","(.+?)"').findall(unpacked)
                vidlink=vidsrc[0]
        elif (redirlink.find("donevideo") > -1):
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(link)[0]
                op = re.compile('action=""><input type="hidden" name="op" value="(.+?)">').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" value="(.+?)">').findall(link)[0]
                mfree = re.compile('<input type="submit" name="method_free"  value="(.+?)">').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":url,"method_free":mfree})
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('<div id="player_code">(.+?)</div>').findall(pcontent)[0]
                packed = packed.replace("</script>","")
                unpacked = unpackjs4(packed)  
                unpacked = unpacked.replace("\\","")
                vidlink = re.compile('src="(.+?)"').findall(unpacked)
                if(len(vidlink) == 0):
                        vidlink = re.compile('"file","(.+?)"').findall(unpacked)
                vidlink=vidlink[0]
        elif (redirlink.find("clicktoview") > -1):
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" value="(.+?)">').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" value="(.+?)">').findall(link)[0]
                mfree = re.compile('<input type="submit" name="method_free" value="(.+?)">').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":url,"method_free":mfree})
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                capchacon =re.compile('another captcha</a>(.+?)</script>').findall(pcontent)[0]
                capchalink=re.compile('<script type="text/javascript" src="(.+?)">').findall(capchacon)
                strCodeInput="recaptcha_response_field"
                respfield=""
                if(len(capchalink)==0):
                         capchacon =re.compile('<b>Enter code below:</b>(.+?)</table>').findall(pcontent)
                         capchar=re.compile('<span style="position:absolute;padding-left:(.+?);[^>]*>(.+?)</span>').findall(capchacon[0])
                         capchar=sorted(capchar, key=lambda x: int(x[0].replace("px","")))
                         capstring =""
                         for tmp,aph in capchar:
                                  capstring=capstring+chr(int(aph.replace("&#","").replace(";","")))
                         puzzle=capstring
                         strCodeInput="code"
                else:
                         imgcontent=GetContent(capchalink[0])
                         respfield=re.compile("challenge : '(.+?)'").findall(imgcontent)[0]
                         imgurl="http://www.google.com/recaptcha/api/image?c="+respfield
                         solver = InputWindow(captcha=imgurl)
                         puzzle = solver.get()
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(pcontent)[0]
                op = re.compile('<input type="hidden" name="op" value="(.+?)">').findall(pcontent)[0]
                mfree = re.compile('<input type="hidden" name="method_free" value="(.+?)">').findall(pcontent)[0]
                rand = re.compile('<input type="hidden" name="rand" value="(.+?)">').findall(pcontent)[0]
                ddirect = re.compile('<input type="hidden" name="down_direct" value="(.+?)">').findall(pcontent)[0]
                #replace codevalue with capture screen
                posdata=urllib.urlencode({"op":op,"id":idkey,"referer":url,"method_free":mfree,"rand":rand,"method_premium":"","recaptcha_challenge_field":respfield,strCodeInput:puzzle,"down_direct":ddirect})
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('<div id="player_code">(.+?)</div>').findall(pcontent)[0]
                packed = packed.split("</script>")[1]
                unpacked = unpackjs4(packed)  
                unpacked = unpacked.replace("\\","")
                vidlink = re.compile('"file","(.+?)"').findall(unpacked)[0]
        elif (redirlink.find("vidbull") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                rand = re.compile('<input type="hidden" name="rand" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":"download2","rand":rand,"id":idkey,"referer":url,"method_free":"","method_premium":"","down_direct":"1"})
                #They need to wait for the link to activate in order to get the proper 2nd page
                dialog.close()
                do_wait('Waiting on link to activate', '', 3)
                dialog.create('Resolving', 'Resolving vidbull Link...') 
                dialog.update(50)
                pcontent=postContent2(redirlink,posdata,url)
                #pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink= re.compile('<!--RAM disable direct link<a href="(.+?)" target="_top">').findall(pcontent)
                if(len(vidlink) > 0):
                         filename = vidlink[0].split("/")[-1:][0]
                         vidlink=vidlink[0].replace(filename,"video.mp4")
                else:
                         sPattern =  '<script type=(?:"|\')text/javascript(?:"|\')>eval\(function\(p,a,c,k,e,[dr]\)(?!.+player_ads.+).+?</script>'
                         r = re.search(sPattern, pcontent, re.DOTALL + re.IGNORECASE)
                         if r:
                              sJavascript = r.group()
                              sUnpacked = jsunpack.unpack(sJavascript)
                              stream_url = re.search('[^\w\.]file[\"\']?\s*[:,]\s*[\"\']([^\"\']+)', sUnpacked)
                              if stream_url:
                                    vidlink= stream_url.group(1)

        elif (redirlink.find("nosvideo") > -1):
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" value="(.+?)">').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" value="(.+?)">').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","fname":fname,"rand":"","id":idkey,"referer":url,"method_free":"Continue+to+Video","method_premium":"","down_script":"1"})
                pcontent=postContent2(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                scriptcontent=re.compile('<div name="placeholder" id="placeholder">(.+?)</div></div>').findall(pcontent)[0]
                packed = scriptcontent.split("</script>")[1]
                unpacked = unpackjs4(packed)
                if unpacked=="":
                        unpacked = unpackjs3(packed,tipoclaves=2)
                        
                unpacked = unpacked.replace("\\","")

                xmlUrl=re.compile('"playlist=(.+?)&').findall(unpacked)[0]
                vidcontent = postContent2(xmlUrl,None,url)
                vidlink=re.compile('<file>(.+?)</file>').findall(vidcontent)[0]
        elif (redirlink.find("vidspot") > -1):
                idkey = re.compile('<input type="hidden" name="id" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":"","method_free":"1"})
                pcontent=postContent(redirlink,posdata+"&x=83&y=15",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                media_url = re.compile('"sources"\s*:\s*\[\s*\{\s*"file"\s*:\s*"(.+?)"\s*\}').findall(pcontent)[0]
                finalcontent=GetContent(redirlink.replace(idkey,"")+media_url)
                finalcontent=''.join(finalcontent.splitlines()).replace('\'','"')
                dmlink=re.compile('<meta [^>]*base=["\']?([^>^"^\']+)["\']?[^>]*>').findall(finalcontent)
                fillink=re.compile('<video [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(finalcontent)
                vidlink=dmlink[0]+fillink[0]+" app="+dmlink[0].split("/")[-2]+"/ swfUrl=http://p.jwpcdn.com/6/10/jwplayer.flash.swf playPath="+fillink[0] +" pageUrl=" + redirlink + " tcUrl="+dmlink[0]
        elif (redirlink.find("speedvid") > -1):
                keycode=re.compile('\|image\|(.+?)\|(.+?)\|file\|').findall(link)
                domainurl=re.compile('\[IMG\](.+?)\[/IMG\]').findall(link)[0]
                domainurl=domainurl.split("/i/")[0]
                vidlink=domainurl+"/"+keycode[0][1]+"/v."+keycode[0][0]
        elif (redirlink.find("vreer") > -1):
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)" />').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" value="(.+?)" />').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" value="(.+?)" />').findall(link)[0]
                rand = re.compile('<input type="hidden" name="hash" value="(.+?)" />').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","fname":fname,"hash":rand,"id":idkey,"referer":"","method_free":"Free Download"})
                #They need to wait for the link to activate in order to get the proper 2nd page
                dialog.close()
                do_wait('Waiting on link to activate', '', 20)
                dialog.create('Resolving', 'Resolving vreer Link...') 
                dialog.update(50)
                pcontent=postContent(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink=re.compile('file: "(.+?)",').findall(pcontent)[0]
        elif (redirlink.find("allmyvideos") > -1):
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" value="(.+?)">').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" value="(.+?)">').findall(link)[0]
                mfree = re.compile('<input type="hidden" name="method_free" value="(.+?)">').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":url,"method_free":mfree})
                pcontent=postContent2(redirlink,posdata,url)
                packed = get_match( pcontent , "(<script type='text/javascript'>eval\(.*?function\(p,\s*a,\s*c,\s*k,\s*e,\s*d.*?)</script>",1)
                unpacked = unpackjs(packed)
                if unpacked=="":
                        unpacked = unpackjs3(packed,tipoclaves=2)
                        
                unpacked = unpacked.replace("\\","")
                try:
                    vidlink = get_match(unpacked,"'file'\s*\:\s*'([^']+)'")+"?start=0"+"|"+urllib.urlencode( {'Referer':'http://allmyvideos.net/player/player.swf','User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; es-ES; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12'} )
                except:
                    vidlink = get_match(unpacked,'"file"\s*\:\s*"([^"]+)"')+"?start=0"+"|"+urllib.urlencode( {'Referer':'http://allmyvideos.net/player/player.swf','User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; es-ES; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12'} )

        elif (redirlink.find("cyberlocker") > -1):
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(link)[0]
                op = re.compile('action=""><input type="hidden" name="op" value="(.+?)">').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" value="(.+?)">').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","id":idkey,"fname":fname,"referer":url,"method_free":"Free Download"})
                pcontent=postContent2(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('<div id="player_code">(.+?)</div>').findall(pcontent)[0]
                packed = packed.replace("</script>","")
                unpacked = unpackjs4(packed)  
                unpacked = unpacked.replace("\\","")
                vidlink = re.compile('name="src"value="(.+?)"').findall(unpacked)[0]
        elif (redirlink.find("promptfile") > -1):
                chash = re.compile('<input type="hidden" name="chash" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"chash":chash})
                pcontent=postContent2(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink=re.compile('<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>Download File</a>').findall(pcontent)[0]
        elif (redirlink.find("veervid") > -1):
                posturl=re.compile('<form action="(.+?)" method="post">').findall(link)[0]
                pcontent=postContent(posturl,"continue+to+video=Continue+to+Video",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink=re.compile('so.addVariable\("file","(.+?)"').findall(pcontent)[0]
        elif (redirlink.find("sharerepo") > -1):
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" value="(.+?)">').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" value="(.+?)">').findall(link)[0]
                ddirect = re.compile('<input type="hidden" name="down_direct" value="(.+?)">').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","fname":fname.encode('utf-8'),"id":idkey,"referer":url,"method_free":"Free Download","down_direct":ddirect})
                pcontent=postContent2(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('<div id="player_code">(.+?)</div>').findall(pcontent)[0]
                packed=packed.split("</script>")[1]
                unpacked = unpackjs4(packed)  
                unpacked = unpacked.replace("\\","")
                vidlink = re.compile('"file","(.+?)"').findall(unpacked)[0]
        elif (redirlink.find("nowdownloa") > -1):
                ddlpage = re.compile('<a class="btn btn-danger" href="(.+?)">Download your file !</a>').findall(link)[0]
                mainurl = redirlink.split("/dl/")[0]
                ddlpage= mainurl+ddlpage
                #They need to wait for the link to activate in order to get the proper 2nd page
                dialog.close()
                do_wait('Waiting on link to activate', '', 30)
                dialog.create('Resolving', 'Resolving nowdownloads Link...') 
                dialog.update(50)
                pcontent=GetContent(ddlpage)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                linkcontent =re.compile('Slow download</span>(.+?)</div>').findall(pcontent)[0]
                vidlink = re.compile('<a href="(.+?)" class="btn btn-success">').findall(linkcontent)[0]
        elif (redirlink.find("youwatch") > -1):
                idkey = re.compile('<input type="hidden" name="id" value="(.+?)">').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" value="(.+?)">').findall(link)[0]
                fname = re.compile('<input type="hidden" name="fname" value="(.+?)">').findall(link)[0]
                rand = re.compile('<input type="hidden" name="hash" value="(.+?)">').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"usr_login":"","fname":fname,"hash":rand,"id":idkey,"referer":"","imhuman":"Slow Download","method_premium":""})
                #They need to wait for the link to activate in order to get the proper 2nd page
                dialog.close()
                do_wait('Waiting on link to activate', '', 10)
                dialog.create('Resolving', 'Resolving youwatch Link...') 
                dialog.update(50)
                pcontent=postContent2(redirlink,posdata,url)
                pcontent=''.join(pcontent.splitlines())
                packed = re.compile("<span id='flvplayer'></span>(.+?)</script>").findall(pcontent)[0]
                unpacked = unpackjs5(packed)  
                unpacked = unpacked.replace("\\","")
                vidlink = re.compile('file:"(.+?)"').findall(unpacked)[0]
        elif (redirlink.find("videoslasher") > -1):
                user=re.compile('user: ([^"]+),').findall(link)[0]
                code=re.compile('code: "([^"]+)",').findall(link)[0]
                hash1=re.compile('hash: "([^"]+)"').findall(link)[0]
                formdata = { "user" : user, "code": code, "hash" : hash1}
                data_encoded = urllib.urlencode(formdata)
                request = urllib2.Request('http://www.videoslasher.com/service/player/on-start', data_encoded) 
                response = urllib2.urlopen(request)
                ccontent = response.read()
                ckStr = cj['.videoslasher.com']['/']['authsid'].name+'='+cj['.videoslasher.com']['/']['authsid'].value
                playlisturl = re.compile('playlist: "(.+?)",').findall(link)[0]
                playlisturl = redirlink.split("/video/")[0]+playlisturl
                pcontent=postContent2(playlisturl,"",url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                vidlink= re.compile(':content url="([^"]+)" type="video/x-flv" [^>]*>').findall(pcontent)[0]
                vidlink= ( '%s|Cookie="%s"' % (vidlink,ckStr) )
        #elif (redirlink.find("billionuploads") > -1):
        #        vidlink=resolve_billionuploads(redirlink,tmpcontent)
        #elif (redirlink.find("movreel") > -1):
        #        vidlink=resolve_movreel(redirlink,tmpcontent)
        elif (redirlink.find("jumbofiles") > -1):
                vidlink=resolve_jumbofiles(redirlink,tmpcontent)
        elif (redirlink.find("glumbouploads") > -1):
                vidlink=resolve_glumbouploads(redirlink,tmpcontent)
        elif (redirlink.find("sharebees") > -1):
                vidlink=resolve_sharebees(redirlink,tmpcontent)
        elif (redirlink.find("uploadorb") > -1):
                vidlink=resolve_uploadorb(redirlink,tmpcontent)
        elif (redirlink.find("vidhog") > -1):
                vidlink=resolve_vidhog(redirlink,tmpcontent)
        elif (redirlink.find("speedyshare") > -1):
                vidlink=resolve_speedyshare(redirlink,tmpcontent)
        elif (redirlink.find("180upload") > -1):
                vidcode = re.compile('180upload.com/(.+?)dk').findall(redirlink+"dk")[0] 
                urlnew= 'http://180upload.com/embed-'+vidcode+'.html'
                link=GetContent(urlnew)
                file_code = re.compile('<input type="hidden" name="file_code" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                op = re.compile('<input type="hidden" name="op" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                embed_width = re.compile('<input type="hidden" name="embed_width" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                embed_height = re.compile('<input type="hidden" name="embed_height" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                test34 = re.compile('<input type="hidden" name="nwknj3" [^>]*value=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[0]
                posdata=urllib.urlencode({"op":op,"file_code":file_code,"referer":url,"embed_width":embed_width,"embed_height":embed_height,"nwknj3":test34})
                pcontent=postContent2(urlnew,posdata,url)
                pcontent=''.join(pcontent.splitlines()).replace('\'','"')
                packed = re.compile('/swfobject.js"></script><script type="text/javascript">(.+?)</script>').findall(pcontent)[0]
                unpacked = unpackjs4(packed)
                if unpacked=="":
                        unpacked = unpackjs3(packed,tipoclaves=2)
                unpacked=unpacked.replace("\\","")
                vidlink = re.compile('addVariable\("file",\s*"(.+?)"\)').findall(unpacked)[0]
                
        else:
                if(redirlink.find("putlocker") > -1 or redirlink.find("sockshare.com") > -1):
                        redir = redirlink.split("/file/")
                        redirlink = redir[0] +"/file/" + redir[1].upper()
                sources = []
                label=name
                #redirlink=redirlink.replace(":","")
                #redirlink=redirlink.replace("http","http:")
                #redirlink=redirlink.replace("https","https:")
                hosted_media = urlresolver.HostedMediaFile(url=redirlink, title=label)
                sources.append(hosted_media)
                source = urlresolver.choose_source(sources)
                print "inresolver=" + redirlink
                if source:
                        vidlink = source.resolve()
    #except:
    dialog.update(90)
    xbmc.sleep(1000)    
    dialog.close()
    return vidlink
               
def ListAZ(catname,mode):
        for character in AZ_DIRECTORIES:
                addDir(character,strdomain+"/"+catname+"/Genre-Any/Letter-"+character+"/ByPopularity/1.htm",mode,"")

def getVideotype(url):
        link = GetContent(url)
        link = ''.join(link.splitlines()).replace('\'','"')
        ssoninfo= re.compile('<h3 class="season_header">(.+?)</h3>').findall(link)
        if(len(ssoninfo) > 0):
                return "tv"
        else:
                return "movie"

def DetermineVideotype(url):
        if(getVideotype(url)=="tv"):
                Seasons(url)
        else:
                Mirrors(url,"Movie")
                
def SEARCHMOV():
        keyb = xbmc.Keyboard('', 'Enter search text')
        keyb.doModal()
        searchText = ''
        if (keyb.isConfirmed()):
                searchText = keyb.getText()
        
        searchText = string.capwords(searchText)
        if searchText == "":
            exit()
        dialog = xbmcgui.DialogProgress()
        dialog.create('VistaTV Vidics Searcher','Searching For Movie: ', '[COLOR red]'+str(searchText)+'[/COLOR]')       
        dialog.update(1)
        xbmc.sleep(1000)
        dialog.update(50)
        searchText.replace(" ","%20")
        SearchResult("movie",searchText)
        dialog.update(100)
        dialog.close()
        
def SEARCHMOV2(getmovie):
        getmovie=getmovie.replace("+"," ")
        getmovie=getmovie.replace("%27","'")
        keyb = xbmc.Keyboard(getmovie, 'Enter search text')
        keyb.doModal()
        searchText = ''
        if (keyb.isConfirmed()):
                searchText = keyb.getText()
        
        searchText = string.capwords(searchText)
        if searchText == "":
            exit()
        dialog = xbmcgui.DialogProgress()
        dialog.create('VistaTV Vidics Searcher','Searching For Movie: ', '[COLOR red]'+str(searchText)+'[/COLOR]')       
        dialog.update(1)
        xbmc.sleep(1000)
        dialog.update(50)
        searchText.replace(" ","%20")
        SearchResult("movie",searchText)
        dialog.update(100)
        dialog.close()
        
def SEARCHTV():
        keyb = xbmc.Keyboard('', 'Enter search text')
        keyb.doModal()
        searchText = ''
        if (keyb.isConfirmed()):
                searchText = keyb.getText()
        searchText = string.capwords(searchText)
        if searchText == "":
            exit()
        dialog = xbmcgui.DialogProgress()
        dialog.create('VistaTV Vidics Searcher','Searching For TV Show: ','[COLOR red]'+str(searchText)+'[/COLOR]')       
        dialog.update(0)
        xbmc.sleep(1000)
        dialog.update(50)
        searchText.replace(" ","%20")
        SearchResult("tv",searchText)
        dialog.update(100)
        dialog.close()
        
def SEARCHTV2(getmovie):
        getmovie=getmovie.replace("+"," ")
        getmovie=getmovie.replace("%27","'")
        keyb = xbmc.Keyboard(getmovie, 'Enter search text')
        keyb.doModal()
        searchText = ''
        if (keyb.isConfirmed()):
                searchText = keyb.getText()
        
        searchText = string.capwords(searchText)
        if searchText == "":
            exit()
        dialog = xbmcgui.DialogProgress()
        dialog.create('VistaTV Vidics Searcher','Searching For TV Show ', '[COLOR red]'+str(searchText)+'[/COLOR]')       
        dialog.update(1)
        xbmc.sleep(1000)
        dialog.update(50)
        searchText.replace(" ","%20")
        SearchResult("tv",searchText)
        dialog.update(100)
        dialog.close()
        
def SEARCHactor():
        keyb = xbmc.Keyboard('', 'Enter search text')
        keyb.doModal()
        searchText = ''
        if (keyb.isConfirmed()):
                searchText = keyb.getText()
        searchText = string.capwords(searchText)
        if searchText == "":
            exit()
        dialog = xbmcgui.DialogProgress()
        dialog.create('VistaTV Vidics Searcher','Searching By Actor Name: ','[COLOR red]'+str(searchText)+'[/COLOR]')       
        dialog.update(0)
        xbmc.sleep(1000)
        dialog.update(50)
        searchText.replace(" ","%20")
        SearchResult("actor",searchText)
        dialog.update(100)
        dialog.close()
		
def SEARCHactor2(getmovie):
        getmovie=getmovie.replace("+"," ")
        getmovie=getmovie.replace("%27","'")
        keyb = xbmc.Keyboard(getmovie, 'Enter search text')
        keyb.doModal()
        searchText = ''
        if (keyb.isConfirmed()):
                searchText = keyb.getText()
        searchText = string.capwords(searchText)
        if searchText == "":
            exit()
        dialog = xbmcgui.DialogProgress()
        dialog.create('VistaTV Vidics Searcher','Searching By Actor Name: ','[COLOR red]'+str(searchText)+'[/COLOR]')       
        dialog.update(0)
        xbmc.sleep(1000)
        dialog.update(50)
        searchText.replace(" ","%20")
        SearchResult("actor",searchText)
        dialog.update(100)
        dialog.close()

def SearchResult(searchType,Searchtext):
    Searchtext=urllib.quote_plus(Searchtext)
    if searchType=="movie":
            INDEX(strdomain+"/Category-Movies/Genre-Any/Letter-Any/ByPopularity/1/Search-"+urllib.quote_plus(Searchtext)+".htm",4,26,"movie",str(Searchtext))
    elif searchType=="actor":
            INDEX(strdomain+"/Category-People/Genre-Any/Letter-Any/ByPopularity/1/Search-"+urllib.quote_plus(Searchtext)+".htm",11,12,"",str(Searchtext))
    else:
            INDEX(strdomain+"/Category-TvShows/Genre-Any/Letter-Any/Relevancy/1/Search-"+urllib.quote_plus(Searchtext)+".htm",7,27,"tv",str(Searchtext))
    
            
def getstatic():
        f = open(langfile, "r")
        langs = f.read()
        return langs
def postContent(url,data,referr):
    opener = urllib2.build_opener()
    opener.addheaders = [('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                         ('Accept-Encoding','gzip, deflate'),
                         ('Referer', referr),
                         ('Content-Type', 'application/x-www-form-urlencoded'),
                         ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0'),
                         ('Connection','keep-alive'),
                         ('Accept-Language','en-us,en;q=0.5'),
                         ('Pragma','no-cache'),
                         ('Host','player.phim47.com')]
    usock=opener.open(url,data)
    if usock.info().get('Content-Encoding') == 'gzip':
        buf = StringIO.StringIO(usock.read())
        f = gzip.GzipFile(fileobj=buf)
        response = f.read()
    else:
        response = usock.read()
    usock.close()
    return response
    
def GenreList(catname,mode):
        url=strdomain+""+catname+"/Genre-Any/Letter-Any/LatestFirst/1.htm"
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')
        listcontent=re.compile('<span class="dir">Genre</span>(.+?)</ul>').findall(newlink)
        if(len(listcontent) > 0):
                glist=re.compile('<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(listcontent[0])
                for vurl,vname in glist:
                    addDir(vname.strip(),strdomain+vurl,mode,"")
                    
def ProfileMovie(url,typename):
        addLink('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)','Cerebro',9898,__icon__)
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')
        listcontent=re.compile('<h3 class="career_type_title" ?[^>]*>'+typename+'(.+?)<tr>').findall(newlink)
        if(len(listcontent) < 0):
            XBMC.Notification("VistaTV,Link not playable try another",2000,""+__icon__+"")
            xbmc.sleep(1000)
            exit()
        html_re = re.compile(r'<[^>]+>')
        if(len(listcontent) > 0):
                movielist=re.compile('<a class="green" [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(listcontent[0])
                for vurl,vname in movielist:
                    vname=html_re.sub('', vname)
                    addDirContext(vname.strip(),strdomain+vurl,13,"",plot="",vidtype="movie")
                    
def ActorProfile(url):
        addLink('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)','Cerebro',9898,__icon__)
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')
        listcontent=re.compile('<h3 class="career_type_title" id="(.+?)" ?[^>]*>(.+?)</h3>').findall(newlink)
        for profid,vtype in listcontent:
            addDir(vtype,url,14,"")
            
def postContent2(url,data,referr):
    req = urllib2.Request(url,data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    data=response.read()
    response.close()
    return data
        
def SearchChannelresults(url,searchtext):
        link = GetContent(url)
        link = ''.join(link.splitlines()).replace('\'','"')
        vidlist=re.compile('<div class="thumb-container big-thumb">        <a href="(.+?)">          <img alt="(.+?)" class="thumb-design" src="(.+?)" />').findall(link)
        addLink('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)','Cerebro',9898,__icon__)
        for vurl,vname,vimg in vidlist:
            vurl = vurl.split("/videos/")[0]
            addDir(vname.lower().replace("<em>"+searchtext+"</em>",searchtext),strdomain+vurl+"/videos",7,strdomain+""+vimg)
        pagelist=re.compile('<div class="pagination">(.+?)</li>').findall(link)
        if(len(pagelist) > 0):
                navlist=re.compile('<a[^>]* href="(.+?)">(.+?)</a>').findall(pagelist[0])
                for purl,pname in navlist:
                    addDir("page " + pname.decode("utf-8"),strdomain+purl,13,"")
                    

def Episodes(url,name):
    #try:
        xbmc.executebuiltin("Container.SetViewMode(522)")
        xbmcplugin.setContent(addon_handle, content="episodes")
        link = GetContent(url)
        try: metaname=url.split('Show/', 1)[1]
        except: metaname=url.split('Serie/', 1)[1]
        metaname = metaname.replace("%201","")
        metaname = metaname.replace("-","%20")
        metaname = metaname.replace("_","%20").title()
        if metaname=="X%20Files": metaname = "X-Files"
        if "Supergirl" in metaname: metaname = "Supergirl"
        if metaname=="Monsters%20Vs%20Aliens%20(2013)": metaname = "Monsters%20Vs%20Aliens"
        ####xbmc.log("Show Name?? "+metaname,2)
        ####xbmc.log("Show Season?? "+name,2)
        epcunter=0
        #ctitle = metaname
        newlink = ''.join(link.splitlines()).replace('\t','')
        try:
            response = urllib2.urlopen('http://thetvdb.com/api/GetSeries.php?seriesname='+str(metaname)).read()
            sid=response.split('<seriesid>', 1)[1]
            sid=response.split('</seriesid>', 1)[0]
            sid=sid.split('<seriesid>', 1)[1]
            getimg=response.split('<banner>', 1)[1]
            getimg=getimg.split('</banner>', 1)[0]
            #getimg=getimg.split('</banner>', 1)[0]
            response = urllib2.urlopen('http://thetvdb.com/api/4144331619000000/series/'+sid+'/banners.xml').read()
            gpost = response.split('posters', 1)[1]
            gpost = gpost.split('</BannerPath>', 1)[0]
            #gpost = gpost.split('<BannerPath>', 1)[0]
            vimg = "http://www.thetvdb.com/banners/posters"+gpost
            response = urllib2.urlopen('http://thetvdb.com/api/4144331619000000/series/'+sid+'/all/en.xml').read()
            ####xbmc.log("http://www.thetvdb.com/banners/posters"+gpost,2)
            #####xbmc.log(response,2)
            #epdata = response.split('posters', 1)[1]
        except : 
            vimg=re.compile('<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(newlink)[4]
            vimg = strdomain+""+vimg

        listcontent=re.compile('<div class="season season_[0-9]">(.+?)<br clear="all"\s*/>').findall(newlink)
        scount=-1
        #vimg = "http://www.thetvdb.com/banners/_cache/"+getimg
        metaname2 = metaname.replace("%20"," ")
        metaname2 = metaname2.replace("_"," ")
        metaname2 = metaname2.replace("-"," ")
        addDir('[COLOR gold]'+metaname2+'[/COLOR] : [COLOR lightblue]'+name+'[/COLOR]','Cerebro',9898,vimg)
        seasoncount = name.replace("Season ","")
        ####xbmc.log(seasoncount,2)
        if int(seasoncount) > 1: 
        #    epcunter=int(seasoncount)-1
            epcunter=0
        #if int(seasoncount) == 9: 
        #    epcunter=int(seasoncount)-2
         #    epcunter=1
        else: epcunter=0
        #if epcunter == 1: epcunter = 0
        addLink('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)','Cerebro',9898,__icon__)
        for listcontent2 in listcontent:
            if (listcontent2.find(">"+name+"</a></h3>") > -1):
                listcontent2=re.compile('>'+name+'</a></h3>(.+?)</div>').findall(listcontent2)[0]
                episodelist=re.compile('<a class="episode" [^s][^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(listcontent2)
                for (vurl,vname) in episodelist:
                     #if epcunter >= scount:
                     #   scount = epcunter
                     #else:
                        #scount = epcunter+1
                     ####xbmc.log("Episode?? "+str(epcunter),2)
                     try: epname = response.split('<Combined_season>'+str(seasoncount)+"", 1)[1]
                     except: epname = response.split('<Combined_season>'+str(seasoncount)+"", 1)[0]
                     try: epname = epname.split('<Combined_episodenumber>'+str(epcunter), 1)[1]
                     except: epname = epname.split('<Combined_episodenumber>'+str(epcunter), 1)[0]
                     ####xbmc.log(epname,2)
                     #exit()
                     try: epname2 = epname.split('<EpisodeNumber>'+str(scount), 1)[1]
                     except: epname2 = epname.split('<EpisodeNumber>'+str(scount)+"", 1)[0]
                     epname2 = epname.split('<Combined_season>'+str(seasoncount)+"", 1)[0]
                     epname2 = epname.split('<Combined_season>'+str(int(scount-epcunter))+"", 1)[0]
                     ####xbmc.log(epname,2)
                     try:
                        epname = epname2.split('<EpisodeName>', 1)[1]
                        epname = epname.split('</EpisodeName>', 1)[0]
                     except: epname = "NOTHING"
                     #epdata = epname.split('<Combined_episodenumber>'+str(scount), 1)[0]
                     ####xbmc.log(epname2,2)
                     try:
                        epdata = epname2.split('<Overview>', 1)[1]
                        epdata = epdata.split('</Overview>', 1)[0]
                     except: epdata="HMMMM"
                     ####xbmc.log(vname,2)

                     html_re = re.compile(r'<[^>]+>')
                     vname2=html_re.sub('', vname) 
                     #vname = vname.replace("unknown",epname)
                     vname=epname
                     iconimage = vimg
                     plot = epdata
                     ####xbmc.log(plot,2)
                     #ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
                     Watched = re.compile('url="(.+?)"\n').findall(str(watched_read))   # regex the file
                     ####xbmc.log(str(Watched),2)
                     ####xbmc.log(str(vimg),2)
                     for item in Watched:              # get url results
                         if item == vimg:               # check if the item matches the url you are pulling through(must be defined before somehow)
                             ####xbmc.log("URL"+str(url),2)
                             vname = '[COLORred]Watched - [/COLOR]'+(vname).replace('[COLORred]Watched - [/COLOR]','')                 # changes 'name' to add Watched in red before it
                             #adddir(name,etc,etc,etc)     # whatever your menu display code is here, aligned with for so itll pull others but run through and get new name if it gets a match
                             addDir2("S"+str(seasoncount)+"E"+str(epcunter+1)+": "+vname,strdomain+vurl,4,str(vimg)," | "+epdata)
                     addDir2("S"+str(seasoncount)+"E"+str(epcunter+1)+": "+vname,strdomain+vurl,4,str(vimg)," | "+epdata)
                     #u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str("8")+"&name="+urllib.quote_plus(name)+"&movieinfo=test"
                     #liz=xbmcgui.ListItem(vname, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
                     #liz.setInfo( type="Video", infoLabels={ "Title":vname, "Plot":plot})
                     #xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)    
                     #liz.setProperty('IsPlayable', 'true')                  
                     #xbmc.executebuiltin('Container.Refresh')
                     ####xbmc.log("ep counter"+str(epcunter),2)
                     ####xbmc.log("seas counter"+str(scount),2)
                     epcunter = epcunter+1
                     #seasoncount = int(seasoncount)+1
                     #scount = scount+1
                     

                     
                break


            #liz.setProperty('IsPlayable', 'true');         
            #xbmc.executebuiltin('Container.Refresh')
            #xbmcplugin.setContent(addon_handle, 'tvshows')    
    #except: pass
    
def Seasons(url):
        xbmc.executebuiltin("Container.SetViewMode(522)")
        xbmcplugin.setContent(addon_handle, 'tvshows')
        try: metaname=url.split('Show/', 1)[1]
        except: metaname=url.split('Serie/', 1)[1]
        name = metaname.replace("-"," ")
        ctitle = metaname.replace(" ","%20")
        ctitle = ctitle.replace("-","%20")
        ctitle = ctitle.replace("_","%20").title()
        ctitle = ctitle.replace("&macr;"," ")
        ctitle = ctitle.replace("-","%20")
        if ctitle=="X%20Files": ctitle = "The%20X-Files"
        if ctitle=="Monsters%20Vs%20Aliens%20(2013)": ctitle = "Monsters%20Vs%20Aliens"
        if "Supergirl" in metaname: 
            metaname = "Supergirl"
            ctitle = "Supergirl"
        link = GetContent(url)
        link = ''.join(link.splitlines()).replace('\'','"')
        ssoninfo= re.compile('<h3 class="season_header">(.+?)</h3>').findall(link)
        vimg=re.compile('<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[4]
        vimg = strdomain+""+vimg
        ###xbmc.log("Get Image "+ctitle,2)
        ####xbmc.log("Show Image "+vimg,2)
        try:
            response = urllib2.urlopen('http://thetvdb.com/api/GetSeries.php?seriesname='+str(ctitle)).read()
            ####xbmc.log(response,2)
            sid=response.split('<seriesid>', 1)[1]
            sid=response.split('</seriesid>', 1)[0]
            sid=sid.split('<seriesid>', 1)[1]
            getimg=response.split('<banner>', 1)[1]
            getimg=getimg.split('</banner>', 1)[0]
            #getimg=getimg.split('</banner>', 1)[0]
            response = urllib2.urlopen('http://thetvdb.com/api/4144331619000000/series/'+sid+'/banners.xml').read()
            ####xbmc.log(response,2)
            fansrtimg = response.split('<BannerPath>fanart', 1)[1]
            fansrtimg = fansrtimg.split('</BannerPath>', 1)[0]
            fansrtimg = "https://www.thetvdb.com/banners/fanart"+fansrtimg
            ###xbmc.log(fansrtimg,2)
            gpost = response.split('posters', 1)[1]
            gpost = gpost.split('</BannerPath>', 1)[0]
            #gpost = gpost.split('<BannerPath>', 1)[0]
            vimg = "http://www.thetvdb.com/banners/posters"+gpost
            #response = urllib2.urlopen('http://thetvdb.com/api/4144331619000000/series/'+sid+'/all/en.xml').read()
            ####xbmc.log("http://www.thetvdb.com/banners/posters"+gpost,2)
        except: pass #vimg=re.compile('<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[4]
        #vimg=re.compile('<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(link)[6]  
        metaname2 = metaname.replace("-"," ")
        metaname2 = metaname2.replace("_"," ")   
        metaname2 = metaname2.replace("&macr;"," ")      
        addDir('[COLOR gold]'+metaname2.title()+'[/COLOR]','Cerebro',9898,__icon__)     
        addLink('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)','Cerebro',9898,__icon__)
        for seas in ssoninfo:
                epsodlist=re.compile('<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(seas)[0]
                addDir(epsodlist[1]+"",url,8,str(vimg))

def INDEX(url,modenum,curmode,vidtype,ctitle):
    #try:
        ctitle = ctitle.replace("%20"," ")
        #ctitle = ctitle.replace("+"," ")
        ctitle = ctitle.replace("%25","+")
        xbmc.executebuiltin("Container.SetViewMode(522)")
        link = GetContent(url)
        try:
            link =link.encode("UTF-8")
        except: pass
        newlink = ''.join(link.splitlines()).replace('\t','')
        vcontent=re.compile('<td id="searchResults" [^>]*>(.+?)</td>').findall(newlink)
        #if not vcontent[0]:
        if len(vcontent) == 0:
            #xbmc.notification("VistaTV,Link not playable try another",2000)
            builtin = "XBMC.Notification(No Answer From Vidics,Or No Results Found. Trying Again! [COLOR red]Check For Typo's[/COLOR] You Searched for: [COLOR green]"+ctitle.replace("+"," ")+"[/COLOR],4000,"+__icon__+")"
            xbmc.executebuiltin(builtin)
            ####xbmc.log(vidtype,2)
            if vidtype == "movie":
                SEARCHMOV2(ctitle)
            elif vidtype == "tv":
                SEARCHTV2(ctitle)
            else:
                SEARCHactor2(ctitle)
            return 
        listcontent=re.compile('<div itemscope [^>]*class="searchResult">(.+?)}</div></div></div>').findall(vcontent[0])
        ##xbmc.log(str(url),2)
        vpot=""
        addLink('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)','Cerebro',9898,__icon__)
        for moveieinfo in listcontent:
            vtitle,vurl,vimg,vtmp1,vtmp2=re.compile('<a title="Watch(.+?)online free." href="(.+?)"><img itemprop="image" src="(.+?)" title="(.+?)" alt="(.+?)" /></a>').findall(moveieinfo)[0]
            vtitle=RemoveHTML(vtitle)
            #if vtitle == "Unknown" and vidtype== "actor": vtitle = "Movies"
            vtitle = vtitle.title()
            #if "Movies With" in vtitle: vtitle.replace("Movies With ", "Info About: ")
            ##xbmc.log(vtitle,2)
            vpot=re.compile('"description":"(.+?)"').findall(moveieinfo)[0] 
            #vpot ="plot??"
            vpot=urllib.unquote_plus(vpot)
            getimg = vpot
            if "No_Poster" in vimg: 
                ####xbmc.log(vtitle+" Change For",2)
                if vidtype == "tv":
                    try:
                        if ctitle=="Monsters%20Vs%20Aliens%20(2013)": ctitle = "Monsters%20Vs%20Aliens"
                        response = urllib2.urlopen('http://thetvdb.com/api/GetSeries.php?seriesname='+str(ctitle)).read()
                        ##xbmc.log(response,2)
                        sid=response.split('<seriesid>', 1)[1]
                        sid=response.split('</seriesid>', 1)[0]
                        sid=sid.split('<seriesid>', 1)[1]
                        getimg=response.split('<Overview>', 1)[1]
                        getimg=getimg.split('</Overview>', 1)[0]
                        #getimg=getimg.split('</banner>', 1)[0]
                        response = urllib2.urlopen('http://thetvdb.com/api/4144331619000000/series/'+sid+'/banners.xml').read()
                        #####xbmc.log(response,2)
                        gpost = response.split('<ThumbnailPath>', 1)[1]
                        gpost = gpost.split('</ThumbnailPath>', 1)[0]
                        #gpost = gpost.split('<BannerPath>', 1)[0]
                        vimg = "http://www.thetvdb.com/banners/"+gpost
                        #response = urllib2.urlopen('http://thetvdb.com/api/4144331619000000/series/'+sid+'/all/en.xml').read()
                        ####xbmc.log("http://www.thetvdb.com/banners/posters"+gpost,2)
                    except: vimg = strdomain+vimg
                else: vimg = strdomain+vimg
            if "http" not in vimg: vimg = strdomain+vimg
            ####xbmc.log(vimg,2)
            vpot=getimg
            ####xbmc.log(vpot+" PLOT??",2)
            if(vidtype==""):
                 addDir(vtitle,strdomain+vurl,modenum,vimg,vpot)
            else:
                 addDirContext(vtitle,strdomain+vurl,modenum,vimg,vpot,vidtype)
        paginacontent=re.compile('<table class="pagination" ?[^>]*>(.+?)</table>').findall(newlink)
        
        if(len(paginacontent)>0):
                pagelist=re.compile('<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(paginacontent[0])
                for vurl,vname in pagelist:
                    addDir("page: " + vname.replace("&rsaquo;",">").replace("&lsaquo;","<"),strdomain+vurl.replace(" ","%20"),curmode,"")
                    
def INDEXList(url,modenum,curmode,vidtype):
    #try:
        xbmc.executebuiltin("Container.SetViewMode(522)")
        link = GetContent(url)
        try:
            link =link.encode("UTF-8")
        except: pass
        newlink = ''.join(link.splitlines()).replace('\t','')
        listcontent=re.compile('<div itemscope [^>]*class="tvshow">(.+?)</td>').findall(newlink)
        vpot=""
        for moveieinfo in listcontent:
            vimg=re.compile('<img [^>]*src=["\']?([^>^"^\']+)["\']?[^>]*>').findall(moveieinfo)[0]
            urlcontent =re.compile('<h3>(.+?)</h3>').findall(moveieinfo)[0]
            titleurl=re.compile('<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(urlcontent)
            if(len(titleurl)>0):
                  vurl=titleurl[0][0]
                  vtitle=titleurl[0][1]
                  sumcontent=re.compile('</h3>(.+?)<span>').findall(moveieinfo)[0]
                  vsummary=re.compile('<div ?[^>]*>(.+?)</div>').findall(sumcontent)
            if(len(vsummary)>0):
                 vpot=vsummary[0]
            vtitle=RemoveHTML(vtitle)
            if(vidtype=="actor"):
                 
                 addDir(vtitle,strdomain+vurl.replace("/People/",strdomain+"/People/").replace("/Category-People/",strdomain+"/Category-People/"),modenum,strdomain+""+vimg,vpot)
            else:
                 addDirContext(vtitle,strdomain+vurl.replace("/People/",strdomain+"/People/").replace("/Category-People/",strdomain+"/Category-People/"),modenum,strdomain+""+vimg,vpot,vidtype)
        paginacontent=re.compile('<table class="pagination" ?[^>]*>(.+?)</table>').findall(newlink)
        
        if(len(paginacontent)>0):
                pagelist=re.compile('<a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a>').findall(paginacontent[0])
                for vurl,vname in pagelist:
                    addDir("page: " + vname.replace("&rsaquo;",">").replace("&lsaquo;","<"),strdomain+vurl.replace(" ","%20"),curmode,"")
    #except: pass


    
#borrowed from pelisalacarta
def get_match(data,patron,index=0):
    matches = re.findall( patron , data , flags=re.DOTALL )
    return matches[index]

def unpackjs(texto):

    # Extract the function body
    patron = "eval\(function\(p\,a\,c\,k\,e\,d\)\{[^\}]+\}(.*?)\.split\('\|'\)\)\)"
    matches = re.compile(patron,re.DOTALL).findall(texto)

    
    # Separate code conversion table
    if len(matches)>0:
        data = matches[0]

    else:
        return ""

    patron = "(.*)'([^']+)'"
    matches = re.compile(patron,re.DOTALL).findall(data)
    cifrado = matches[0][0]
    descifrado = ""
    
    # Create the Dictionary with the conversion table
    claves = []
    claves.extend(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    claves.extend(["10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","1g","1h","1i","1j","1k","1l","1m","1n","1o","1p","1q","1r","1s","1t","1u","1v","1w","1x","1y","1z"])
    claves.extend(["20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","2g","2h","2i","2j","2k","2l","2m","2n","2o","2p","2q","2r","2s","2t","2u","2v","2w","2x","2y","2z"])
    claves.extend(["30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","3g","3h","3i","3j","3k","3l","3m","3n","3o","3p","3q","3r","3s","3t","3u","3v","3w","3x","3y","3z"])
    palabras = matches[0][1].split("|")
    diccionario = {}

    i=0
    for palabra in palabras:
        if palabra!="":
            diccionario[claves[i]]=palabra
        else:
            diccionario[claves[i]]=claves[i]
        i=i+1

    # Substitute the words of the conversion table
    # Retrieved from http://rc98.net/multiple_replace
    def lookup(match):
        try:
            return diccionario[match.group(0)]
        except:
            return ""

    # Reverse key priority for having the longest
    claves.reverse()
    cadenapatron = '|'.join(claves)
    compiled = re.compile(cadenapatron)
    descifrado = compiled.sub(lookup, cifrado)


    return descifrado
    
def unpackjs5(texto):

    # Extrae el cuerpo de la funcion
    matches = texto.split("return p}")
    if len(matches)>0:
        data = matches[1].split(".split")[0]
    else:
        return ""

    patron = "(.*)\"([^\"]+)\""
    matches = re.compile(patron,re.DOTALL).findall(data)
    if len(matches)<2:
        matches=data.split(",'")
        cifrado = matches[0]+","
        palabras = "'"+matches[1]
        palabras = palabras.split("|")
    else:
        cifrado = matches[0][0]
        palabras = matches[0][1].split("|")
    descifrado = ""
    
    # Crea el dicionario con la tabla de conversion
    claves = []
    tipoclaves=0
    claves.extend(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    claves.extend(["10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","1g","1h","1i","1j","1k","1l","1m","1n","1o","1p","1q","1r","1s","1t","1u","1v","1w","1x","1y","1z"])
    claves.extend(["20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","2g","2h","2i","2j","2k","2l","2m","2n","2o","2p","2q","2r","2s","2t","2u","2v","2w","2x","2y","2z"])
    claves.extend(["30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","3g","3h","3i","3j","3k","3l","3m","3n","3o","3p","3q","3r","3s","3t","3u","3v","3w","3x","3y","3z"])
    
    diccionario = {}
   
    i=0
    for palabra in palabras:
        if palabra!="":
            
            diccionario[claves[i]]=palabra
        else:
            diccionario[claves[i]]=claves[i]
        i=i+1

    def lookup(match):
        try:
               retval=diccionario[match.group(0)]
        except:
                retval=""
        return retval

    claves.reverse()
    cadenapatron = '|'.join(claves)
    compiled = re.compile(cadenapatron)
    descifrado = compiled.sub(lookup, cifrado)

    return descifrado
    
def unpackjs4(texto):

    matches = texto.split("return p}")
    if len(matches)>0:
        data = matches[1].replace(".split(\"|\")))","")
    else:
        return ""

    patron = "(.*)\"([^\"]+)\""
    matches = re.compile(patron,re.DOTALL).findall(data)
    cifrado = matches[0][0]
    
    descifrado = ""
    
    claves = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","1g","1h","1i","1j","1k","1l","1m","1n","1o","1p","1q","1r","1s","1t","1u","1v","1w","1x","1y","1z"]
    palabras = matches[0][1].split("|")
    diccionario = {}
    i=0
    for palabra in palabras:
      try:
        if palabra!="":
            diccionario[claves[i]]=palabra
        else:
            diccionario[claves[i]]=claves[i]
      except: pass
      i=i+1


    def lookup(match):
        return diccionario[match.group(0)]


    claves.reverse()
    cadenapatron = '|'.join(claves)
    compiled = re.compile(cadenapatron)
    descifrado = compiled.sub(lookup, cifrado)

    return descifrado

def unpackjs3(texto,tipoclaves=1):

    
    patron = "return p\}(.*?)\.split"
    matches = re.compile(patron,re.DOTALL).findall(texto)

    if len(matches)>0:
        data = matches[0]
    else:
        patron = "return p; }(.*?)\.split"
        matches = re.compile(patron,re.DOTALL).findall(texto)
        if len(matches)>0:
            data = matches[0]
        else:
            return ""

    patron = "(.*)'([^']+)'"
    matches = re.compile(patron,re.DOTALL).findall(data)
    cifrado = matches[0][0]

    descifrado = ""
    
    # Create the Dictionary with the conversion table
    claves = []
    if tipoclaves==1:
        claves.extend(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
        claves.extend(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
    else:
        claves.extend(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
        claves.extend(["10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","1g","1h","1i","1j","1k","1l","1m","1n","1o","1p","1q","1r","1s","1t","1u","1v","1w","1x","1y","1z"])
        claves.extend(["20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","2g","2h","2i","2j","2k","2l","2m","2n","2o","2p","2q","2r","2s","2t","2u","2v","2w","2x","2y","2z"])
        claves.extend(["30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","3g","3h","3i","3j","3k","3l","3m","3n","3o","3p","3q","3r","3s","3t","3u","3v","3w","3x","3y","3z"])
        
    palabras = matches[0][1].split("|")
    diccionario = {}

    i=0
    for palabra in palabras:

        if palabra!="":
            diccionario[claves[i]]=palabra
        else:
            diccionario[claves[i]]=claves[i]
        i=i+1

     # Substitute the words of the conversion table
     # Retrieved from http://rc98.net/multiple_replace
    def lookup(match):
        try:
            return diccionario[match.group(0)]
        except:
            return ""

     # Reverse key priority for having the longest
    claves.reverse()
    cadenapatron = '|'.join(claves)

    compiled = re.compile(cadenapatron)
    descifrado = compiled.sub(lookup, cifrado)

    descifrado = descifrado.replace("\\","")


    return descifrado
    
#borrowed from icefilms
def do_wait(source, account, wait_time):
     # do the necessary wait, with  a nice notice and pre-set waiting time. I have found the below waiting times to never fail.
     
     if int(wait_time) == 0:
         wait_time = 1
         
     if account == 'platinum':    
          return handle_wait(int(wait_time),source,'Loading video with your *Platinum* account.')
               
     elif account == 'premium':    
          return handle_wait(int(wait_time),source,'Loading video with your *Premium* account.')
             
     elif account == 'free':
          return handle_wait(int(wait_time),source,'Loading video with your free account.')

     else:
          return handle_wait(int(wait_time),source,'Loading video.')

def handle_wait(time_to_wait,title,text):

    print 'waiting '+str(time_to_wait)+' secs'    

    pDialog = xbmcgui.DialogProgress()
    ret = pDialog.create(' '+title)

    secs=0
    percent=0
    increment = float(100) / time_to_wait
    increment = int(round(increment))

    cancelled = False
    while secs < time_to_wait:
        secs = secs + 1
        percent = increment*secs
        secs_left = str((time_to_wait - secs))
        remaining_display = ' Wait '+secs_left+' seconds for the video stream to activate...'
        pDialog.update(percent,' '+ text, remaining_display)
        xbmc.sleep(1000)
        if (pDialog.iscanceled()):
             cancelled = True
             break
    if cancelled == True:     
         print 'wait cancelled'
         return False
    else:
         print 'done waiting'
         return True

def resolve_billionuploads(url,inhtml=None):

    #try:

        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving BillionUploads Link...')       
        dialog.update(0)
        
        print 'BillionUploads - Requesting GET URL: %s' % url
        if(inhtml==None):
               html = net.http_GET(url).content
        else:
               html = inhtml
        #They need to wait for the link to activate in order to get the proper 2nd page
        dialog.close()
        do_wait('Waiting on link to activate', '', 3)
        dialog.create('Resolving', 'Resolving BillionUploads Link...') 
        dialog.update(50)
        
        #Check page for any error msgs
        if re.search('This server is in maintenance mode', html):
            print '***** BillionUploads - Site reported maintenance mode'
            raise Exception('File is currently unavailable on the host')

        # Check for file not found
        if re.search('File Not Found', html):
            print '***** BillionUploads - File Not Found'
            raise Exception('File Not Found - Likely Deleted')  

        #New CloudFlare checks
        jschl=re.compile('name="jschl_vc" value="(.+?)"/>').findall(html)
        if jschl:
            jschl = jschl[0]    
        
            maths=re.compile('value = (.+?);').findall(html)[0].replace('(','').replace(')','')

            domain_url = re.compile('(https?://.+?/)').findall(url)[0]
            domain = re.compile('https?://(.+?)/').findall(domain_url)[0]
            
            time.sleep(5)
            
            normal = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            normal.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36')]
            link = domain_url+'cdn-cgi/l/chk_jschl?jschl_vc=%s&jschl_answer=%s'%(jschl,eval(maths)+len(domain))
            print 'BillionUploads - Requesting GET URL: %s' % link
            final= normal.open(domain_url+'cdn-cgi/l/chk_jschl?jschl_vc=%s&jschl_answer=%s'%(jschl,eval(maths)+len(domain))).read()
            html = normal.open(url).read()
                    
        #Set POST data values
        data = {}
        r = re.findall(r'type="hidden" name="(.+?)" value="(.+?)">', html)
        for name, value in r:
            data[name] = value
        
        #Captcha
        captchaimg = re.search('<img src="(http://BillionUploads.com/captchas/.+?)"', html)
       
        #If Captcha image exists
        if captchaimg:
            
            dialog.close()
            #Grab Image and display it
            img = xbmcgui.ControlImage(550,15,240,100,captchaimg.group(1))
            wdlg = xbmcgui.WindowDialog()
            wdlg.addControl(img)
            wdlg.show()
            
            #Small wait to let user see image
            time.sleep(3)
            
            #Prompt keyboard for user input
            kb = xbmc.Keyboard('', 'Type the letters in the image', False)
            kb.doModal()
            capcode = kb.getText()
            
            #Check input
            if (kb.isConfirmed()):
              userInput = kb.getText()
              if userInput != '':
                  capcode = kb.getText()
              elif userInput == '':
                   Notify('big', 'No text entered', 'You must enter text in the image to access video', '')
                   return None
            else:
                return None
            wdlg.close()
            
            #Add captcha code to post data
            data.update({'code':capcode})
            
            #Re-create progress dialog
            dialog.create('Resolving', 'Resolving BillionUploads Link...') 

        #Some new data values
        data.update({'submit_btn':''})
        data.update({'geekref':'yeahman'})
             
        dialog.update(50)
        
        print 'BillionUploads - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content
        dialog.update(100)
        
        def custom_range(start, end, step):
            while start <= end:
                yield start
                start += step

        def checkwmv(e):
            s = ""
            
            # Create an array containing A-Z,a-z,0-9,+,/
            i=[]
            u=[[65,91],[97,123],[48,58],[43,44],[47,48]]
            for z in range(0, len(u)):
                for n in range(u[z][0],u[z][1]):
                    i.append(chr(n))
            #print i

            # Create a dict with A=0, B=1, ...
            t = {}
            for n in range(0, 64):
                t[i[n]]=n
            #print t

            for n in custom_range(0, len(e), 72):

                a=0
                h=e[n:n+72]
                c=0

                #print h
                for l in range(0, len(h)):            
                    f = t.get(h[l], 'undefined')
                    if f == 'undefined':
                        continue
                    a= (a<<6) + f
                    c = c + 6

                    while c >= 8:
                        c = c - 8
                        s = s + chr( (a >> c) % 256 )
            return s
        dll = re.compile('<input type="hidden" id="dl" value="(.+?)">').findall(html)[0]
        dl = dll.split('GvaZu')[1]
        print dl
        dl = checkwmv(dl)
        dl = checkwmv(dl)
        print 'Link Found: %s' % dl                

        return dl


    #except Exception, e:
    #    print '**** BillionUploads Error occured: %s' % e
    #    raise


def resolve_speedyshare(url,inhtml=None):

    try:    
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving SpeedyShare Link...')
        dialog.update(50)
        
        print 'SpeedyShare - Requesting GET URL: %s' % url
        if(inhtml==None):
               html = net.http_GET(url).content
        else:
               html = inhtml
        
        dialog.close()
        
        host = 'http://speedy.sh'
        #host = re.search("<input value='(http://www[0-9]*.speedy.sh)/.+?'", html).group(1)
        link = re.search("<a class=downloadfilename href='(.+?)'>", html).group(1)
        return host + link
    except Exception, e:
        print '**** SpeedyShare Error occured: %s' % e
        raise


def resolve_vidhog(url,inhtml=None):

    try:
        
        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving VidHog Link...')
        dialog.update(0)
        
        print 'VidHog - Requesting GET URL: %s' % url
        if(inhtml==None):
               html = net.http_GET(url).content
        else:
               html = inhtml

        dialog.update(33)
        
        #Check page for any error msgs
        if re.search('This server is in maintenance mode', html):
            print '***** VidHog - Site reported maintenance mode'
            raise Exception('File is currently unavailable on the host')
        
        #Set POST data values
        op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
        usr_login = re.search('<input type="hidden" name="usr_login" value="(.*?)">', html).group(1)
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        fname = re.search('<input type="hidden" name="fname" value="(.+?)">', html).group(1)
        method_free = re.search('<input type="submit" name="method_free" value="(.+?)" class="freebtn right">', html).group(1)
        
        data = {'op': op, 'usr_login': usr_login, 'id': postid, 'fname': fname, 'referer': url, 'method_free': method_free}
        
        print 'VidHog - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content
        
        dialog.update(66)
                
        #Set POST data values
        op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        rand = re.search('<input type="hidden" name="rand" value="(.+?)">', html).group(1)
        method_free = re.search('<input type="hidden" name="method_free" value="(.+?)">', html).group(1)
        down_direct = int(re.search('<input type="hidden" name="down_direct" value="(.+?)">', html).group(1))
        wait = int(re.search('<span id="countdown_str">Wait <span id=".+?">([0-9]*)</span>', html).group(1))
        
        data = {'op': op, 'id': postid, 'rand': rand, 'referer': url, 'method_free': method_free, 'down_direct': down_direct}
        
        dialog.close()
        
        #Do wait time for free accounts    
        finished = do_wait('VidHog', '', wait)

        if finished:
            print 'VidHog - Requesting POST URL: %s DATA: %s' % (url, data)
            
            dialog.create('Resolving', 'Resolving VidHog Link...')
            dialog.update(66)
            
            html = net.http_POST(url, data).content
            
            dialog.update(100)
            
            dialog.close()
        
            link = re.search('<strong><a href="(.+?)">Click Here to download this file</a></strong>', html).group(1)
            return link
        else:
            return None
        
    except Exception, e:
        print '**** VidHog Error occured: %s' % e
        raise


def resolve_uploadorb(url,inhtml=None):

    try:

        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving UploadOrb Link...')       
        dialog.update(0)
        
        print 'UploadOrb - Requesting GET URL: %s' % url
        if(inhtml==None):
               html = net.http_GET(url).content
        else:
               html = inhtml
        
        dialog.update(33)
        
        #Check page for any error msgs
        if re.search('This server is in maintenance mode', html):
            print '***** UploadOrb - Site reported maintenance mode'
            raise Exception('File is currently unavailable on the host')

        #Set POST data values
        op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
        usr_login = re.search('<input type="hidden" name="usr_login" value="(.*?)">', html).group(1)
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        fname = re.search('<input type="hidden" name="fname" value="(.+?)">', html).group(1)
        method_free = re.search('<input type="submit" name="method_free" value="(.+?)" class="btn2">', html).group(1)
        
        data = {'op': op, 'usr_login': usr_login, 'id': postid, 'fname': fname, 'referer': url, 'method_free': method_free}
        
        print 'UploadOrb - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content

        dialog.update(66)
        
        #Set POST data values
        op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        rand = re.search('<input type="hidden" name="rand" value="(.+?)">', html).group(1)
        method_free = re.search('<input type="hidden" name="method_free" value="(.+?)">', html).group(1)
        down_direct = int(re.search('<input type="hidden" name="down_direct" value="(.+?)">', html).group(1))
        
        data = {'op': op, 'id': postid, 'rand': rand, 'referer': url, 'method_free': method_free, 'down_direct': down_direct}
        print data
        
        print 'UploadOrb - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content
        
        dialog.update(100)
        link = re.search('ACTION="(.+?)">', html).group(1)
        dialog.close()
        
        return link

    except Exception, e:
        print '**** UploadOrb Error occured: %s' % e
        raise


def resolve_sharebees(url,inhtml=None):

    try:
        
        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving ShareBees Link...')       
        dialog.update(0)
        
        print 'ShareBees - Requesting GET URL: %s' % url
        if(inhtml==None):
               html = net.http_GET(url).content
        else:
               html = inhtml
        
        dialog.update(50)
        
        #Set POST data values
        #op = re.search('''<input type="hidden" name="op" value="(.+?)">''', html, re.DOTALL).group(1)
        op = 'download1'
        usr_login = re.search('<input type="hidden" name="usr_login" value="(.*?)">', html).group(1)
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        fname = re.search('<input type="hidden" name="fname" value="(.+?)">', html).group(1)
        method_free = "method_free"
        
        data = {'op': op, 'usr_login': usr_login, 'id': postid, 'fname': fname, 'referer': url, 'method_free': method_free}
        
        print 'ShareBees - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content
        
        dialog.update(100)

        link = None
        sPattern = '''<div id="player_code">.*?<script type='text/javascript'>(eval.+?)</script>'''
        r = re.search(sPattern, html, re.DOTALL + re.IGNORECASE)
        
        if r:
            sJavascript = r.group(1)
            sUnpacked = jsunpack.unpack(sJavascript)
            print(sUnpacked)
            
            #Grab first portion of video link, excluding ending 'video.xxx' in order to swap with real file name
            #Note - you don't actually need the filename, but for purpose of downloading via Icefilms it's needed so download video has a name
            sPattern  = '''("video/divx"src="|addVariable\('file',')(.+?)video[.]'''
            r = re.search(sPattern, sUnpacked)              
            
            #Video link found
            if r:
                link = r.group(2) + fname
                dialog.close()
                return link

        if not link:
            print '***** ShareBees - Link Not Found'
            raise Exception("Unable to resolve ShareBees")

    except Exception, e:
        print '**** ShareBees Error occured: %s' % e
        raise


def resolve_glumbouploads(url,inhtml=None):

    try:

        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving GlumboUploads Link...')       
        dialog.update(0)
        
        print 'GlumboUploads - Requesting GET URL: %s' % url
        if(inhtml==None):
               html = net.http_GET(url).content
        else:
               html = inhtml
        
        dialog.update(33)
        
        #Set POST data values
        op = 'download1'
        usr_login = re.search('<input type="hidden" name="usr_login" value="(.*?)">', html).group(1)
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        fname = re.search("""input\[name="fname"\]'\).attr\('value', '(.+?)'""", html).group(1)
        method_free = 'Free Download'
        
        data = {'op': op, 'usr_login': usr_login, 'id': postid, 'fname': fname, 'referer': url, 'method_free': method_free}
        
        print 'GlumboUploads - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content

        dialog.update(66)
        
        countdown = re.search('var cdnum = ([0-9]+);', html).group(1)

        #They need to wait for the link to activate in order to get the proper 2nd page
        dialog.close()
        do_wait('Waiting on link to activate', '', int(countdown))
        dialog.create('Resolving', 'Resolving GlumboUploads Link...') 
        dialog.update(66)

        #Set POST data values
        op = 'download2'
        rand = re.search('<input type="hidden" name="rand" value="(.+?)">', html).group(1)
        
        data = {'op': op, 'rand': rand, 'id': postid, 'referer': url, 'method_free': method_free, 'down_direct': 1}
        
        print 'GlumboUploads - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content
        
        dialog.update(100)
        link = re.search('This download link will work for your IP for 24 hours<br><br>.+?<a href="(.+?)">', html, re.DOTALL).group(1)
        dialog.close()
        
        return link

    except Exception, e:
        print '**** GlumboUploads Error occured: %s' % e
        raise

def resolve_jumbofiles(url,inhtml=None):

    try:

        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving JumboFiles Link...')       
        dialog.update(0)
        
        print 'JumboFiles - Requesting GET URL: %s' % url
        if(inhtml==None):
               html = net.http_GET(url).content
        else:
               html = inhtml
        
        dialog.update(33)
        
        #Check page for any error msgs
        if re.search('This server is in maintenance mode', html):
            print '***** JumboFiles - Site reported maintenance mode'
            raise Exception('File is currently unavailable on the host')

        #Set POST data values
        #op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
        op = 'download1'
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        fname = re.search('<input type="hidden" name="fname" value="(.+?)">', html).group(1)
        #method_free = re.search('<input type="hidden" name="method_free" value="(.*?)">', html).group(1)
        method_free = 'method_free'
                
        data = {'op': op, 'id': postid, 'referer': url, 'method_free': method_free}
        
        print 'JumboFiles - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content

        dialog.update(66)

        #Set POST data values
        #op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
        op = 'download2'
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        rand = re.search('<input type="hidden" name="rand" value="(.+?)">', html).group(1)
        method_free = 'method_free'
                
        data = {'op': op, 'id': postid, 'rand': rand, 'method_free': method_free}
        
        print 'JumboFiles - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content        

        dialog.update(100)        
        link = re.search('<FORM METHOD="LINK" ACTION="(.+?)">', html).group(1)
        dialog.close()
        
        return link

    except Exception, e:
        print '**** JumboFiles Error occured: %s' % e
        raise


def resolve_movreel(url,inhtml=None):

    try:

        #Show dialog box so user knows something is happening
        dialog = xbmcgui.DialogProgress()
        dialog.create('Resolving', 'Resolving Movreel Link...')       
        dialog.update(0)
        
        print 'Movreel - Requesting GET URL: %s' % url
        if(inhtml==None):
               html = net.http_GET(url).content
        else:
               html = inhtml
        
        dialog.update(33)
        
        #Check page for any error msgs
        if re.search('This server is in maintenance mode', html):
            print '***** Movreel - Site reported maintenance mode'
            raise Exception('File is currently unavailable on the host')

        #Set POST data values
        op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
        usr_login = re.search('<input type="hidden" name="usr_login" value="(.*?)">', html).group(1)
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        fname = re.search('<input type="hidden" name="fname" value="(.+?)">', html).group(1)
        method_free = re.search('<input type="submit" name="method_free" style=".+?" value="(.+?)">', html).group(1)
        
        data = {'op': op, 'usr_login': usr_login, 'id': postid, 'referer': url, 'fname': fname, 'method_free': method_free}
        
        print 'Movreel - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content

        #Check for download limit error msg
        if re.search('<p class="err">.+?</p>', html):
            print '***** Download limit reached'
            errortxt = re.search('<p class="err">(.+?)</p>', html).group(1)
            raise Exception(errortxt)

        dialog.update(66)
        
        #Set POST data values
        op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
        postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
        rand = re.search('<input type="hidden" name="rand" value="(.+?)">', html).group(1)
        method_free = re.search('<input type="hidden" name="method_free" value="(.+?)">', html).group(1)
        
        data = {'op': op, 'id': postid, 'rand': rand, 'referer': url, 'method_free': method_free, 'down_direct': 1}

        print 'Movreel - Requesting POST URL: %s DATA: %s' % (url, data)
        html = net.http_POST(url, data).content
        
        dialog.update(100)
        link = re.search('<a id="lnk_download" href="(.+?)">Download Original Video</a>', html, re.DOTALL).group(1)
        dialog.close()
        
        return link

    except Exception, e:
        print '**** Movreel Error occured: %s' % e
        raise
        
if os.path.isfile(db_dir)==False:
     initDatabase()
     
def playVideo(url,name,movieinfo):
        #pl=xbmc.PlayList(1)
        builtin = 'XBMC.Notification(VistaTV,Link not playable try another,2000,'+__icon__+')' 
        #url=url.replace("openload.co","oload.stream")  
        #url=url.replace(":","&")
        #url=url.replace("https&","https:")
        #url=url.replace("http&","http:")
        try: 
            vidurl=ParseVideoLink(url,name,movieinfo)                                # closes file 
        except: xbmc.executebuiltin(builtin)
        xbmcPlayer = xbmc.Player()
        try: 
            xbmcPlayer.play(vidurl)
            #xbmc.Player().play(pl)
            print_text_file = open(watched,"a")                      # sets it to append to watched.txt
            print_text_file.write('url="'+movieinfo+'"\n')                 # writes the url in a form easy to regex above
            print_text_file.close                                    # closes file 
        except:
            #xbmc.executebuiltin("SendClick(SkipNext)")
            #xbmc.executebuiltin('xbmc.ActivateWindow(10025)')
            #xbmc.executebuiltin('SendClick(10025,Down)')
            xbmc.executebuiltin(builtin)
        
def RemoveHTML(strhtml):
            html_re = re.compile(r'<[^>]+>')
            strhtml=html_re.sub('', strhtml)
            return strhtml

def addDirContext(name,url,mode,iconimage,plot="",vidtype="", cm=[]):
        #xbmc.log("addDirContext"+iconimage,2)
        from xml.etree import ElementTree as ET
        if "Movies With" in name: name = name.replace("Movies With ", "Info About: ")      
        response="INFO FOR ITEM WILL GO HERE"
        if vidtype=="movie":
            try: 
                ctitle = name.replace(" ","+")
                response = urllib2.urlopen('https://api.themoviedb.org/3/search/movie?api_key=51ad578391a6d2d799d8ee521dad9fca&query='+str(ctitle)).read()
                response=response.split('"overview":"', 1)[1]
                response=response.split('","release_date"', 1)[0]
                #response = urllib.quote_plus(response)
                response=response.decode('string_escape')
            except: response="Unable to Get Any Data!!!!"
            

        else:
            try: 
                ctitle = name.replace(" ","%20")
                ctitle = ctitle.replace("-","%20")
                ctitle = ctitle.replace("_","%20").title()
                if ctitle=="X%20Files": ctitle = "The%20X-Files"
                ####xbmc.log("Show Icon? "+ctitle,2)
                if ("vidics" not in ctitle) or ("Cerebro" not in ctitle):
                    if ctitle=="Monsters%20Vs%20Aliens%20(2013)": ctitle = "Monsters%20Vs%20Aliens"
                    response = urllib2.urlopen('http://thetvdb.com/api/GetSeries.php?seriesname='+str(ctitle)).read()
                    response=response.split('<Overview>', 1)[1]
                    response=response.split('</Overview>', 1)[0]
            except: response="Unable to Get Any Data!!!!"

        
        if "Info About:" in name: response = ""
		
        plot = "[COLOR gold]"+name+"[/COLOR] : "+str(response)
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&vidtype="+vidtype
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        #liz.setProperty('fanart_image',iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot": plot} )
        #if(len(cm)==0):
        #        contextMenuItems = AddFavContext(vidtype, url, name, iconimage)
        #else:
        #contextMenuItems=cm
        #liz.addContextMenuItems(contextMenuItems, replaceItems=False)
        #liz.setProperty('fanart_image',iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        #liz.setProperty('IsPlayable', 'true');
        #xbmcplugin.setContent(addon_handle, 'movies')
        return ok
        
def addLink(name,url,mode,iconimage,movieinfo=""):
        #xbmc.log("Add link icon image"+iconimage,2)
        if "Movies With" in name: name = name.replace("Movies With ", "Info About: ")
        #pl=xbmc.PlayList(1)
        #pl.clear()
        ####xbmc.log("MODE: "+str(name),2)
        #if "Pair For Best" in name:
        #    name = "WOOHOO"
        try:
            ctitle = name.split('hite] ', 1)[1]
            ctitle = ctitle.split(' [/COLOR]', 1)[0]                
            #ctitle = name.replace(" ","+")
            ####xbmc.log(ctitle,2)
            response = urllib2.urlopen('https://api.themoviedb.org/3/search/movie?api_key=51ad578391a6d2d799d8ee521dad9fca&query='+str(ctitle)).read()
            response=response.split('"overview":"', 1)[1]
            response=response.split('","release_date"', 1)[0]
            #response = urllib.quote_plus(response)
            response=response.decode('string_escape')
        except: 
            name2 = name.split('[COLOR gold]', 1)[0]
            ####xbmc.log(name2,2)
            try: 
                name2 = name2.split(': ', 1)[1]
                name2 = name2.split('[/COLOR]', 1)[0]
            except: pass
            
            response="Select a host to start watching . Hosts that need pairing are best quality and less buffering | Cerebro TV VoD | Find Us On Facebook!"
        #else:
        wname = iconimage.replace('/', '--')
        wname = wname.replace(':', '__')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&movieinfo="+iconimage
        ok=True
        #TheTvDb().search_Tv%20Shows("The20%Punisher")
        if "Click Here to Pair" in name:
            plot = "[COLOR green]For best results pair now, more HD content, less buffering. Brought to you by Cerebro TV[/COLOR]"
        else:
            plot = str(response)
        ####xbmc.log("Show Icon? "+iconimage,2)
        #fanart ="https://www.thetvdb.com/banners/fanart/original/328487-5.jpg"
        #iconimage="https://www.thetvdb.com/banners/fanart/original/328487-5.jpg"
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot": plot} )
        #contextMenuItems = []
        #liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        #listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
        #try: 
        #    resurl = ParseVideoLink(str(strdomain)+str(vurl),str(name),"TEST")
        #    xbmc.PlayList(1).add(resurl, listitem)
        #except: pass
        #xbmc.Player().play(pl)
		#except: pass
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty('fanart_image', iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        #xbmc.Player().play(pl)
        return ok
        
def addNext(formvar,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&formvar="+str(formvar)+"&name="+urllib.quote_plus('Next >')
        ok=True
        liz=xbmcgui.ListItem('Next >', iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": 'Next >' } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
def addDir(name,url,mode,iconimage,plot=""):
        #xbmc.log("Add DIR icon image"+iconimage,2)
        if "Movies With" in name: name = name.replace("Movies With ", "Info About: ")
        ##xbmc.log("Show Icon? "+iconimage,2)
        #fmode = True
        #if name == "Unknown" :
        #    iconimage = __icon__
        metaname="empty"
        response="empty"
        #metaname2="empty"
        if url == "search":
            url ="Cerebro/Show/Cerebro"
        if url == "Cerebro":
            url ="Cerebro/Show/Cerebro"
        if  url == " ":
            url ="Cerebro/Show/Cerebro"
        #plot="Pair now for best results!!"
        try:
            metaname=str(url).split('Show/', 1)[1]
        except: 
            try: metaname=str(url).split('Serie/', 1)[1] #metaname = "DONT SHOW"
            except: "MOVIE"
        metaname=metaname.replace("-"," ")
        metaname=str(metaname).split(' Season', 1)[0]
        metaname=metaname.replace("_","%20").title()
        if metaname=="X%20Files": metaname = "The%20X-Files"
        if metaname=="Supergirl 1": metaname = "Supergirl"
        metaname=metaname.replace("%20"," ")
        if "Cerebro" in url:
            ####xbmc.log("URL "+url,2)
            metaname2="Cerebro Pairing System.  Do this for best quality playback & less buffering... Brought to you by CereroTV!"
            response=""
        elif "DONT SHOW" in metaname:
            ####xbmc.log("URL "+url,2)
            metaname2="Cerebro Pairing System.  Do this for best quality playback & less buffering... Brought to you by CereroTV!"
            response=""
        elif "Empty" in metaname:
            ####xbmc.log("URL "+url,2)
            metaname2="Cerebro Pairing System.  Do this for best quality playback & less buffering... Brought to you by CereroTV!"
            metaname="VistaTV"
            response=""
        else:
            if "name" == "empty": name =""
            metaname2 = metaname+" "+name
            try:
                if metaname=="Monsters Vs Aliens (2013)": metaname = "Monsters Vs Aliens"
                #if "Empty" in metaname: continue			
                response = urllib2.urlopen('http://thetvdb.com/api/GetSeries.php?seriesname='+str(metaname.replace(" ","%20"))).read()
                response=response.split('<Overview>', 1)[1]
                response=response.split('</Overview>', 1)[0]
                response=" | "+response
            except: 
                pass
        ####xbmc.log("NEW DATA THIS ONE "+metaname2,2)

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot": "[COLOR gold]"+metaname+"[/COLOR] [COLOR green]"+name+"[/COLOR]"+response} )
        liz.setProperty('fanart_image', iconimage)
        liz.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
def addDir2(name,url,mode,iconimage,plot):
        ####xbmc.log("Show Icon? "+url,2)
        metaname="empty"
        response="empty"
        #metaname2="empty"
        if url == "search":
            url ="Cerebro/Show/Cerebro"
        if url == "Cerebro":
            url ="Cerebro/Show/Cerebro"
        if  url == " ":
            url ="Cerebro/Show/Cerebro"
        #plot="Pair now for best results!!"
        try:
            metaname=str(url).split('Show/', 1)[1]
        except: 
            try: metaname=str(url).split('Serie/', 1)[1] #metaname = "DONT SHOW"
            except: "MOVIE"
        metaname=metaname.replace("-"," ")
        metaname=str(metaname).split(' Season', 1)[0]
        metaname=metaname.replace("_","%20").title()
        if metaname=="X%20Files": metaname = "The%20X-Files"
        if metaname=="Supergirl 1": metaname = "Supergirl"
        metaname=metaname.replace("%20"," ")
        if "Cerebro" in url:
            ####xbmc.log("URL "+url,2)
            metaname2="Cerebro Pairing System.  Do this for best quality playback & less buffering... Brought to you by CereroTV!"
            response=""
        elif "DONT SHOW" in metaname:
            ####xbmc.log("URL "+url,2)
            metaname2="Cerebro Pairing System.  Do this for best quality playback & less buffering... Brought to you by CereroTV!"
            response=""
        elif "Empty" in metaname:
            ####xbmc.log("URL "+url,2)
            metaname2="Cerebro Pairing System.  Do this for best quality playback & less buffering... Brought to you by CereroTV!"
            metaname="VistaTV"
            response=""
        else:
            if "name" == "empty": name =""
            metaname2 = metaname+" "+name
            try:
                #if "Empty" in metaname: continue	
                response = urllib2.urlopen('http://thetvdb.com/api/GetSeries.php?seriesname='+str(metaname.replace(" ","%20"))).read()
                response=response.split('<Overview>', 1)[1]
                response=response.split('</Overview>', 1)[0]
                response=" | "+response
            except: 
                pass
        ####xbmc.log("NEW DATA THIS ONE "+metaname2,2)

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot": "[COLOR gold]"+metaname+"[/COLOR] [COLOR green]"+name+"[/COLOR]"+plot} )
        liz.setProperty('fanart_image', iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        #ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        #liz.setProperty('IsPlayable', 'true')
        return ok

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



params=get_params()
url=None
name=None
mode=None
formvar=None
subtitleurl=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        formvar=int(params["formvar"])
except:
        pass        
try:
        subtitleurl=urllib.unquote_plus(params["suburl"])
except:
        pass
try:
        vidtype=urllib.unquote_plus(params["vidtype"])
except:
        pass
try:
        imageurl=urllib.unquote_plus(params["imageurl"])
except:
        pass
try:
        movieinfo=urllib.unquote_plus(params["movieinfo"])
except:
        pass
        
sysarg=str(sys.argv[1]) 

print "currentmode" + str(mode)
if mode==None or url==None or len(url)<1:
        HOME()
elif mode==2:

        ListGenres(url,name) 
elif mode==3:
        #d()
        playVideo(url,name,movieinfo)
elif mode==4:
        #d()
        Mirrors(url,name,"IMAGE") 
elif mode==5:
        INDEXList(url,4,5,"movie")
elif mode==6:
        INDEXList(url,7,6,"tv")
elif mode==7:
        Seasons(url)
elif mode==8:
        Episodes(url,name)
elif mode==9:
        SEARCHMOV()
elif mode==10:
        SEARCHTV()
elif mode==11:
        ActorProfile(url)
elif mode==12:
        INDEX(url,11,12,"")
elif mode==13:
        DetermineVideotype(url)
elif mode==14:
        ProfileMovie(url,name)
elif mode==15:
        SEARCHactor()
elif mode==16:
        ListAZ(url,26)
elif mode==17:
        ListAZ(url,27)
elif mode==18:
        GenreList(url,26)
elif mode==19:
        GenreList(url,27)
elif mode==20:
        List4Days()
elif mode==21:
        getSchedule(url)
elif mode==22:
        SaveFav(vidtype, name, url, imageurl)
elif mode==23:
        DeleteFav(name,url)
elif mode==24:
        ListFavorites()
elif mode==25:
        BrowseFavorites(url)
elif mode==26:
        INDEX(url,4,26,"movie","")
elif mode==27:
        INDEX(url,7,27,"tv","")
elif mode==28:
        SearchResult(url,name)
elif mode==9898:
        xbmc.executebuiltin('RunAddon(script.cerebro.pairwith.laucnher)')
xbmc.executebuiltin("Container.SetViewMode(522)")
xbmcplugin.endOfDirectory(int(sysarg))
