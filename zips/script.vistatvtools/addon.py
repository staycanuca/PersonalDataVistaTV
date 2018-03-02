import time
import xbmc
import os
import xbmcgui
import urllib2
from urllib import urlopen
import re
import platform



def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4,
        function5,
        function6,
        function7,
        function8,
		function9
        )
        
    call = dialog.select('[B][COLOR=yellow]VistaTV[/COLOR][COLOR=yellow] Tools Menu[/COLOR][/B]', [
    '[B][COLOR=gold]Show Me My Wifi Signal[/COLOR][/B] - ([I]Andriod [/I])',
    '[B][COLOR=gold]Show My Info[/COLOR][/B]',
    '[B][COLOR=gold]VistaTV House Keeper[/COLOR][/B] (clean up system and reboot)', 
    '[B][COLOR=gold]Test My Connection Speed[/COLOR][/B]', 
    '[B][COLOR=gold]VistaTV Wizard[/COLOR][/B]', 
    '[B][COLOR=gold]Open Main Box Settings[/COLOR][/B]', 
    '[B][COLOR=gold]Update Addons & Repos[/COLOR][/B] (make sure your upto date)',
	'[B][COLOR=gold]Easy Advanced Settings[/COLOR][/B]',
	'[B][COLOR=gold]Accounts & URL Resolver Settings[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-9]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]VistaTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]VistaTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 

    
def function1():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]VistaTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('StartAndroidActivity("com.farproc.wifi.analyzer")')    

def function2():
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]VistaTV[/COLOR]","Collecting Data","Few Second.....")
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## MY BOX INFO ##[/COLOR][/B]", "[COLOR=red]My ID[/COLOR]: [COLOR=green]"+str(data300)+"[/COLOR]", "[COLOR=red]Build Version[/COLOR]: [COLOR=green]"+str(data)+"[/COLOR]","[COLOR=red]IP Address (public)[/COLOR]: [COLOR=green]"+str(getPublicIp())+"[/COLOR]")

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.program.megatvhousekeeper3?sf_options=desc%3DMega+TV+Box+Wait%26_options_sf",return)')

def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.speedtestnet?sf_options=fanart%3Dspecial%3A%2F%2Fhome%2Faddons%5Cscript.speedtestnet%5Cfanart.jpg%26desc%3DARNU+Box+Speed+Tester+powered+by+speedtest.net+will+give+you+accurate+Internet+speed%2Fping+test+results.+%5Cn+Brought+to+you+by+http%3A%2F%2Fwww.arnubox.com%26_options_sf",return)')

def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.vistatv-wizard",return)')


def function6():
    xbmc.executebuiltin('StartAndroidActivity("com.mbx.settingsmbox")')
    xbmc.executebuiltin('StartAndroidActivity("com.android.tv.settings")')
    xbmc.executebuiltin('StartAndroidActivity("com.mbox.settings")')
        
def function7():
    xbmc.executebuiltin('ActivateWindow(10040,"addons://outdated/",return)')
    xbmc.sleep(2000)
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]Vista TV[/COLOR]","Checking Repos for Updates","Please Wait (approx 45 secs)")
    xbmc.executebuiltin('xbmc.UpdateAddonRepos()')
    xbmc.sleep(35000)
    dp.create("[COLOR tomato]Vista TV[/COLOR]","Checking Add-ons for Updates","Please Wait (approx 45 secs)")
    xbmc.executebuiltin('xbmc.UpdateLocalAddons()')
    percent = 50
    dp.update(percent)
    xbmc.sleep(35000)
    
    dp.close()
    
def function8():
    xbmc.executebuiltin('RunAddon(plugin.program.advancedsettings)')  
	
def function9():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatv/?action=openSettings&query=5.0",return)')  
    
  
menuoptions()