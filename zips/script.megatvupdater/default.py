import utils
import xbmc
import os
import xbmcgui
import zipfile
import sfile
import download
import urllib
import urllib2
import time 

#dp = xbmcgui.DialogProgress()
#dp.create("[COLOR tomato]VistaTV[/COLOR]","Connection to Server","Please Wait.....")
#xbmc.sleep(1000)



HOME2     = xbmc.translatePath('special://userdata')
file2 = os.path.join(HOME2, 'vistatv.xml')

HOME     = xbmc.translatePath('special://home')
file4 = os.path.join(HOME2, 'networksettings.xml')

file98 = os.path.join(HOME2, 'vistatv.xml') 

#with open(file98, 'r') as myfile:
#        data=float(myfile.read())
		
with open(file98, 'r') as myfile:
    data=float(myfile.read())

megaver = float(data)

LOCATION     = "http://cerebrotv.co.uk/TV-DATA/updatervista.php?v="+str(megaver)

ROOT     = xbmc.translatePath('special://home')
file     = os.path.join(HOME, '_mega_temp.zip')
GETTEXT  = utils.GETTEXT

file3 = os.path.join(HOME, 'mchangelog.xml')

    
 
def killxbmc():
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]Mega TV[/COLOR]","SPMC/Kodi is now Closing","This make take a while.")
    with open(file4, 'r') as myfile:
        boxid=myfile.read()
    response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&die=1').read()
    xbmc.executebuiltin("Notification(VistaTV,Closing SPMC/Kodi, Will take a few seconds,7000,)")
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    os._exit(1)
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

def noconnection():
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to download needed data....", "Will Try Again.","Press OK to Continue")
    xbmc.sleep(1000)
    #DownloaderClass(LOCATION,file)


def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]VistaTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]VistaTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)


def DownloaderClass(url,dest):
    start_time=time.time()
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]VistaTV Updater[/COLOR]","Downloading New Update","This make take a while.")
    try:
        #urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
        dp.create("[COLOR tomato]VistaTV Updater[/COLOR]","Installing New Update","Please Wait. [COLOR red]DO NOT TURN OFF!!![/COLOR]")
        if os.path.exists(file):
            file3 = os.path.join(HOME, 'mchangelog.xml')
            open(file3, 'w+')
            userdata = "test|test"
            with open(file3, 'w') as f:
                f.write(userdata)
            zfile = zipfile.ZipFile(file, 'r')	
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
        

        utils.DeleteFile(file)	
        #dp.create("[COLOR tomato]VistaTV[/COLOR]","Update Complete","Closing Kodi....")	
        xbmc.executebuiltin("Action(Close)")
        os._exit(1)
        #exit()

    except Exception, e:
        noconnection()
        #print(e)
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
 

 
if os.path.exists(file):
    utils.DeleteFile(file)



def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0

	
if ping("www.google.co.uk"):
    import re, uuid
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    if os.path.exists(file4):
        pass
    else:
        fo = open(iddata, "w")
        fo.write('install01');
        fo.close()
        xbmc.sleep(1000)
    with open(file4, 'r') as myfile:
        boxid=myfile.read()
    response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&ok=OK&mac='+str(mac))
    data3=response.read()
    auth = str(data3)
    if auth == "BAD":
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR=red][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]Only buy from www.cerebrotv.co.uk[/B]")
        xbmc.sleep(15000)
        dp.close()
        dp.create("[COLOR=yellow][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]Only buy from www.cerebrotv.co.uk[/B]")	
        xbmc.sleep(15000)
        intro()
        killxbmc()
        xbmc.executebuiltin("Action(Close)")
        os._exit(1)
        exit()
    if auth == "INUSE":
        dp = xbmcgui.DialogProgress()
        dialog.ok("[COLOR=yellow][B]INFORMATION[/COLOR][/B]", "Your Code is in use by someone else.", "Or your have just crashed....","Please Wait 10 minuets and try again or Contact you seller......")
        dp.create("[COLOR=red][B]INFORMATION[/COLOR][/B]","Your Code is in use by someone else","Please Wait 10 minuets and try again or Contact you seller......")
        xbmc.sleep(15000)
        intro()
        killxbmc()
        xbmc.executebuiltin("Action(Close)")
        os._exit(1)
        exit()
		
    dialog = xbmcgui.Dialog()
    if dialog.yesno("[COLOR yellow]VistaTV[/COLOR]"," " ,"[COLOR yellow]Start The Update Now?[/COLOR]", " ",'[COLOR red]NO[/COLOR]','[COLOR lime]YES[/COLOR]'):
        DownloaderClass(LOCATION,file)
        #xbmc.executebuiltin('RunAddon(script.program.megatvpopup)')
    else:
        dialog.ok("[COLOR yellow]VistaTV[/COLOR]", "Update Cancled", "Somethings will not work right......","Press OK to Continue")
else:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to connect to the internet", "","Press OK to Continue")
    myplatform = platform()
    if myplatform == 'windows': # Windows
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        intro()
        killxbmc()
    elif myplatform == 'linux': #Linux
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        intro()
        killxbmc()
    elif myplatform == 'osx': # OSX
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        intro()
        killxbmc()
    elif myplatform == 'android': # Android  
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "We will now try and open network settings..", "","Press OK to Continue")
        xbmc.executebuiltin(StartAndroidActivity('com.mbx.settingsmbox'))
        if dialog.yesno("[COLOR yellow]VistaTV[/COLOR]"," " ,"[COLOR yellow]Start The Update Now?[/COLOR]", " ",'[COLOR red]NO[/COLOR]','[COLOR lime]YES[/COLOR]'):
            dialog.ok("[COLOR=yellow][B] ## yes ##[/COLOR][/B]", "We will now try and open network settings..", "","Press OK to Continue")
        else:
            dialog.ok("[COLOR=yellow][B] ## no ##[/COLOR][/B]", "We will now try and open network settings..", "","Press OK to Continue")             		
        exit();
        		






