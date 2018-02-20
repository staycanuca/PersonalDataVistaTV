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
        
    call = dialog.select('[B][COLOR=yellow]On Demand Menu[/COLOR][/B]', [ 
    '[B]      Movies[/B]' ,	
    '[B]      TV Shows[/B]',
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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatv/?action=movieNavigator",return)')
	
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatv/?action=tvNavigator",return)')
		  
menuoptions()