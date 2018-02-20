# -*- coding: utf-8 -*-
#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#      Modified for FTV Guide (09/2014 onwards)
#      by Thomas Geppert [bluezed] - bluezed.apps@gmail.com
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import gui
from utils import reset_playing
import xbmc
import os
import xbmcgui
import download
import urllib
import urllib2
import zipfile
import sfile
import utils
import time
from shutil import copyfile
import webbrowser
import xbmcaddon
dp = xbmcgui.DialogProgress()
dp.create("[COLOR tomato]Cerebero TV[/COLOR]","Please Wait","......") 

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')


ipaddy="0.0.0.0"
HOME     = xbmc.translatePath('special://userdata/')
addonicon = xbmc.translatePath('special://addons/plugin.video.wargames/icon.png')
iddata   = os.path.join(HOME, 'networksettings.xml')
#with open(iddata, 'r') as myfile:
#    data300=str(myfile.read())
#response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(data300)+'&ok=OK&ip='+ipaddy).read()
#if not response == "OK":
#    xbmc.executebuiltin("Notification([COLOR=gold]CerebroTV[/COLOR],NO CODE FOUND, ..,4000,"+__icon__+")")
#    exit()
#xbmc.executebuiltin("Notification([COLOR=gold]CerebroTV[/COLOR],Opening TV Guide,2000,"+__icon__+")")



#try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/cerebrouk.xml"))
#except: pass
#try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/source.db"))
#except: pass

#xbmc.executebuiltin('PlayMedia("plugin://plugin.video.tvone11/refresh")')
 


LOCATION     = "https://github.com/biglad/BUILDONLY/blob/master/build_data/uk-new.zip?raw=true"
HOME     = xbmc.translatePath('special://home')
ROOT     = xbmc.translatePath('special://home')
file2     = os.path.join(ROOT, 'uk.zip')

file    = "master.xml"

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR tomato]TV Guide Auto Update[/COLOR]","Downloading New TV Guide Data","This will take a few seconds.")
        dp.update(0)
    start_time=time.time()
    try:
        urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
        urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
        dp.close()
        dp.create("[COLOR tomato]TV Guide Auto Update[/COLOR]","Installing New TV Guide Data","Please Wait. [COLOR red]www.cerebrotv.co.uk[/COLOR]")
        if os.path.exists(file2):
            zfile = zipfile.ZipFile(file2, 'r')	
            nItem = float(len(zfile.infolist()))
            index = 0
            for item in zfile.infolist():
                index += 1
            
                percent  = int(index / nItem *100)
                filename = item.filename
                dp.update(percent)
                try:
                    zfile.extract(item, ROOT)
                except Exception, e:
                    utils.log('Changelog error in extractAll')
                    utils.log(e)
                        
        dp.close()
        try:
            xbmc.executebuiltin("Notification(CerebroTV,Some Channels May Take a Few Tries,3000,"+__icon__+")")
            w = gui.TVGuide()
            w.doModal()
            del w

        except:
            import sys
            import traceback as tb
            (etype, value, traceback) = sys.exc_info()
            tb.print_exception(etype, value, traceback)
    except Exception, e:
        dp.close()
        noconnection()
     
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60)
            dp.update(percent, mbs, e,' ')
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 

def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]CerebroTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]CerebroTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)


def DownloaderClass(url,dest, dp = None):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]TV Guide Auto Update[/COLOR]","Downloading New TV Guide Data","This will take a few seconds.")
    try:
        start_time=time.time()
        urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
        urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
        dp.close()
        dp.create("[COLOR tomato]TV Guide Auto Update[/COLOR]","Installing New TV Guide Data","Please Wait. [COLOR red]www.cerebrotv.co.uk[/COLOR]")
        if os.path.exists(file2):
            zfile = zipfile.ZipFile(file2, 'r')	
            nItem = float(len(zfile.infolist()))
            index = 0
            for item in zfile.infolist():
                index += 1
			
                percent  = int(index / nItem *100)
                filename = item.filename
                dp.update(percent)
                try:
                    zfile.extract(item, ROOT)
                except Exception, e:
                    utils.log('Changelog error in extractAll')
                    utils.log(e)
        
        dp.close()
        dialog = xbmcgui.Dialog()

        xbmc.sleep(2000)
        try:
            #xbmc.executebuiltin("Notification(CerebroTV,Some Channels May Take a Few Tries, ..,3000,)")
            w = gui.TVGuide()
            w.doModal()
            del w

        except:
            import sys
            import traceback as tb
            (etype, value, traceback) = sys.exc_info()
            tb.print_exception(etype, value, traceback)


    except Exception, e:
        noconnection()

        exit()
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60)
            dp.update(percent, mbs, e,' ')
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 
 

def noconnection():
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to download needed data....", "Will Try Again.","Press OK or Back to Continue")
    #xbmc.sleep(1000)
    exit()



def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

# After a restart the proc file should be wiped!
reset_playing()
dp.close()
update = xbmcgui.Dialog().yesno("[COLOR tomato]TV Guide Helper[/COLOR]","[COLOR yellow][/COLOR]","" ,"","Open Guide","Update Guide")
#download(LOCATION,file2) 
if update:
    try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/source.db"))
    except: pass
    utils.DeleteFile(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/source.db"))
    try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/cerebrouk.xml"))
    except: pass
    utils.DeleteFile(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/cerebrouk.xml"))
    #xbmc.executebuiltin('PlayMedia("plugin://plugin.video.streamhub")')
    #xbmc.sleep(1000)
    download(LOCATION,file2) 
else:
    try:
        w = gui.TVGuide()
        w.doModal()
        del w

    except:
        import sys
        import traceback as tb
        (etype, value, traceback) = sys.exc_info()
        tb.print_exception(etype, value, traceback)

