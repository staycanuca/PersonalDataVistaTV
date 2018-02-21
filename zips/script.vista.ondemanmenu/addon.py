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
        
    call = dialog.select('[B][COLOR=yellow]On Demand Menu[/COLOR][/B]', [ 
    '[B][COLOR=gold]Movies[/COLOR][/B]' ,	
    '[B][COLOR=gold]TV Shows[/COLOR][/B]',
	'[B][COLOR=gold]Latest TV Episodes[/COLOR][/B]',
	'[B][COLOR=gold]Vidics[/COLOR][/B]',
	'[B][COLOR=gold]Sky Cinema on Demand[/COLOR][/B]',
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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatv/?action=movieNavigator",return)')
	
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatv/?action=tvNavigator",return)')
	
def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.tvheaven/?description&iconimage=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.tvheaven%5cresources%5cart%5clatest.png&mode=1&name=New%20Latest%20Episodes&url=http%3a%2f%2fwatchepisodeseries.unblockall.org%2f",return)')
	
def function4():
    xbmc.executebuiltin('RunAddon(plugin.video.vistavidics)')
	
def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatv/?action=channels",return)')
		  
menuoptions()