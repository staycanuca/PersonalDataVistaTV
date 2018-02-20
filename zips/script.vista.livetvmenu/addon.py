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
        function2
        )
        
    call = dialog.select('[B][COLOR=yellow]Live TV Menu[/COLOR][/B]', [ 
    '[B]      >> [COLOR=gold]Open TV Guide[/COLOR] << [/B]' ,	
    '[B]      >> [COLOR=yellow]Open IPTV Lists[/COLOR] << [/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin('RunAddon(script.tvguide.vistatv)')
	
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatv/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fPersonalDataVistaTV%2fmaster%2fzips%2fto-be-cleaned-up-ed%2fsuper%2520old%2520stuff%2f9534958459845345%2fsdfdsfdsfdsfsdfsfdsf%2f1%2f2%2flol%2fwtf%2fLive.xml",return)')
		  
menuoptions()