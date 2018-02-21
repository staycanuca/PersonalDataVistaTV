import os
import xbmc,xbmcaddon,subprocess
import urlparse
import xbmcgui
import sfile
dp = xbmcgui.DialogProgress()
dialog = xbmcgui.Dialog()
dp.create("[COLOR gold]VistaTV House Keeper[/COLOR]","Removing temp /old files","Please Wait...")
xbmc.sleep(2000)
dp.update(10)




#CACHE
CACHE    = xbmc.translatePath('special://home/cache/')
#FILES
MZip     = xbmc.translatePath('special://home/_mega_temp.zip')
MZip2     = xbmc.translatePath('special://home/userdata/install.zip')
MZip3     = xbmc.translatePath('special://home/userdata/install2.zip')
MZip4     = xbmc.translatePath('special://home/userdata/install3.zip')
#THUMBS
thumbs     = xbmc.translatePath('special://home/userdata/Thumbnails/')


try: sfile.rmtree(CACHE)
except: pass
try: sfile.rmtree(thumbs)
except: pass

#TV GUIDE DATA
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/vistatv.xml"))
except: pass
dp.update(40)
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/source.db"))
except: pass


try: os.remove(MZip)
except: pass
try: os.remove(MZip2)
except: pass
try: os.remove(MZip3)
except: pass
try: os.remove(MZip4)
except: pass


#update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
#if update:
#    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
#else:
#    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
dp.update(80)
xbmc.sleep(1000)
dp.update(100)
dp.close()
dp.create("[COLOR gold]VistaTV House Keeper[/COLOR]","Closing Kodi","Please Wait...")
dp.update(100)
xbmc.sleep(3000)
os._exit(1)





