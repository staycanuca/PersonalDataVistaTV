import time
import xbmc
import os
import xbmcgui
import urllib2
import utils
import sfile

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4,
		function5
        )
        
    call = dialog.select('[B][COLOR=yellow]Live TV Menu[/COLOR][/B]', [ 
    '[B]      >> [COLOR=gold]Open[/COLOR] [COLOR=red]UK[/COLOR] [COLOR=gold]TV Guide[/COLOR] << [/B]' ,
	'[B]      >> [COLOR=yellow]Open[/COLOR] [COLOR=red]USA[/COLOR] [COLOR=gold]TV Guide[/COLOR] << [/B]' , 	
	'[B]      >> [COLOR=gold]Open[/COLOR] [COLOR=red]Kids[/COLOR] [COLOR=gold]TV Guide[/COLOR] << [/B]' , 	
	'[B]      >> [COLOR=yellow]Open[/COLOR] [COLOR=red]Sports[/COLOR] [COLOR=gold]TV Guide[/COLOR] << [/B]' , 	
    '[B]      >> [COLOR=yellow]View IPTV Lists[/COLOR] << Live TV (Many Options)[/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin('RunAddon(script.cerebro.tvguide.open)')
	
def function2():
    xbmc.executebuiltin('RunAddon(script.cerebro.tvguide.open4)')
	
def function3():
    xbmc.executebuiltin('RunAddon(script.cerebro.tvguide.open3)')
	
def function4():
    xbmc.executebuiltin('RunAddon(script.cerebro.tvguide.open2)')
	   
def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fCerebroTVRepo%2fmaster%2fconfigs%2fLive.xml",return)')
    
	  
menuoptions()