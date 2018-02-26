# -*- coding: utf-8 -*-
import urllib
import urllib2
import datetime
import re
import os
import base64
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
from modules . jsunpack import unpack as packets
from modules . common import random_agent
from BeautifulSoup import BeautifulStoneSoup , BeautifulSoup , BeautifulSOAP
try :
 import json
except :
 import simplejson as json
import time
import requests
import _Edit
if 64 - 64: i11iIiiIii
OO0o = [ 'alldebrid.com' , 'allmyvideos.net' , 'allvid.ch' , 'auengine.com' , 'beststreams.net' , 'briskfile.com' , 'castamp.com' , 'clicknupload.com' , 'clicknupload.me' , 'clicknupload.link' , 'cloudy.ec' , 'cloudzilla.to' , 'neodrive.co' , 'crunchyroll.com' , 'daclips.in' , 'daclips.com' , 'dailymotion.com' , 'divxstage.eu' , 'divxstage.net' , 'divxstage.to' , 'couldtime.to' , 'ecostream.tv' , 'exashare.com' , 'estream.to' , 'facebook.com' , 'fastplay.cc' , 'fastplay.to' , 'fastplay.sx' , 'filehoot.com' , 'filenuke.com' , 'filepup.net' , 'filmshowonline.net' , 'flashx.tv' , 'plus.google.com' , 'googlevideo.com' , 'picasaweb.google.com' , 'googleusercontent.com' , 'googledrive.com' , 'gorillavid.in' , 'gorillavid.com' , 'gorillavid.in' , 'grifthost.com' , 'hugefiles.net' , 'idowatch.net' , 'indavideo.hu' , 'ishared.eu' , 'jetload.tv' , 'kingfiles.net' , 'letwatch.us' , 'letwatch.to' , 'vidshare.us' , 'mail.ru' , 'my.mail.ru' , 'videoapi.my.mail.ru' , 'api.video.mail.ru' , 'mega-debrid.eu' , 'megamp4.net' , 'mersalaayitten.com' , 'movdivx.com' , 'movpod.net' , 'movpod.in' , 'movshare.net' , 'wholecloud.net' , 'mp4engine.com' , 'mp4stream.com' , 'mp4upload.com' , 'myvidstream.net' , 'nosvideo.com' , 'noslocker.com' , 'auroravid.to' , 'novamov.com' , 'nowvideo.sx' , 'nowvideo.eu' , 'nowvideo.ch' , 'nowvideo.sx' , 'nowvideo.co' , 'nowvideo.li' , 'nowvideo.ec' , 'nowvideo.at' , 'nowvideo.fo' , 'ok.ru' , 'odnoklassniki.ru' , 'openload.io' , 'openload.co' , 'play44.net' , 'played.to' , 'playhd.video' , 'playhd.fo' , 'playu.net' , 'playu.me' , 'playwire.com' , 'Premiumize.me' , 'primeshare.tv' , 'promptfile.com' , 'purevid.com' , 'rapidvideo.ws' , 'rapidvideo.com' , 'api.real-debrid.com' , 'premium.rpnet.biz' , 'rutube.ru' , 'shared2.me' , 'shared.sx' , 'sharerepo.com' , 'sharesix.com' , 'simply-debrid.com' , 'speedplay.xyz' , 'speedplay.us' , 'speedplay3.pw' , 'speedvideo.net' , 'stagevu.com' , 'streamcloud.eu' , 'streamin.to' , 'stream.moe' , 'streamango.com' , 'streamcherry.com' , 'teramixer.com' , 'thevideo.me' , 'thevideos.tv' , 'toltsd-fel.tk' , 'trollvid.net' , 'tune.pk' , 'tusfiles.net' , 'twitch.tv' , 'up2stream.com' , 'upload.af' , 'uploadc.com' , 'uploadc.ch' , 'zalaa.com' , 'uploadx.org' , 'uptobox.com' , 'uptostream.com' , 'userfiles.com' , 'userscloud.com' , 'veehd.com' , 'veoh.com' , 'vid.ag' , 'vidbull.com' , 'vidcrazy.net' , 'uploadcrazy.net' , 'thevideobee.to' , 'videoboxer.co' , 'vidgg.to' , 'vid.gg' , 'videohut.to' , 'videomega.tv' , 'videoraj.to' , 'videorev.cc' , 'videosky.to' , 'video.tt' , 'videoweed.es' , 'bitvid.sx' , 'videoweed.com' , 'videowood.tv' , 'byzoo.org' , 'playpanda.net' , 'videozoo.me' , 'videowing.me' , 'videowing.me' , 'easyvideo.me' , 'play44.net' , 'playbb.me' , 'video44.net' , 'vidio.sx' , 'vidlox.tv' , 'vid.me' , 'vidspot.net' , 'vidto.me' , 'vidup.me' , 'vidup.org' , 'vidzi.tv' , 'vimeo.com' , 'vivo.sx' , 'vk.com' , 'vkpass.com' , 'vodlocker.com' , 'vshare.io' , 'vshare.eu' , 'watchers.to' , 'watchonline.to' , 'watchvideo.us' , 'watchvideo2.us' , 'watchvideo3.us' , 'watchvideo4.us' , 'watchvideo5.us' , 'watchvideo6.us' , 'watchvideo7.us' , 'watchvideo8.us' , 'watchvideo9.us' , 'weshare.me' , 'xvidstage.com' , 'youlol.biz' , 'shitmovie.com' , 'yourupload.com' , 'youtube.com' , 'youtu.be' , 'youwatch.org' , 'api.zevera.com' , 'zettahost.tv' , 'zstream.to' ]
Oo0Ooo = [ 'plugin.video.dramasonline' , 'plugin.video.f4mTester' , 'plugin.video.shahidmbcnet' , 'plugin.video.SportsDevil' , 'plugin.stream.vaughnlive.tv' , 'plugin.video.ZemTV-shani' ]
if 85 - 85: OOO0O0O0ooooo % IIii1I . II1 - O00ooooo00
class I1IiiI ( urllib2 . HTTPErrorProcessor ) :
 def http_response ( self , request , response ) :
  return response
 https_response = http_response
 if 27 - 27: iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o
I1IiI = _Edit . addon
o0OOO = I1IiI . getAddonInfo ( 'version' )
iIiiiI = xbmc . translatePath ( I1IiI . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
Iii1ii1II11i = xbmc . translatePath ( I1IiI . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
iI111iI = os . path . join ( iIiiiI , 'favorites' )
IiII = os . path . join ( iIiiiI , 'history' )
iI1Ii11111iIi = base64 . decodestring
i1i1II = os . path . join ( iIiiiI , 'list_revision' )
O0oo0OO0 = os . path . join ( Iii1ii1II11i , 'icon.png' )
I1i1iiI1 = os . path . join ( Iii1ii1II11i , 'fanart.jpg' )
iiIIIII1i1iI = os . path . join ( iIiiiI , 'source_file' )
o0oO0 = iIiiiI
oo00 = I1IiI . getSetting ( 'Adult' )
o00 = I1IiI . getSetting ( 'Porn_Pass' )
Oo0oO0ooo = I1IiI . getSetting ( 'debug' )
if os . path . exists ( iI111iI ) == True :
 o0oOoO00o = open ( iI111iI ) . read ( )
else : o0oOoO00o = [ ]
if os . path . exists ( iiIIIII1i1iI ) == True :
 i1 = open ( iiIIIII1i1iI ) . read ( )
else : i1 = [ ]
oOOoo00O0O = 'plugin.video.supremacy'
if 15 - 15: I11iii11IIi
def O00o0o0000o0o ( string ) :
 if Oo0oO0ooo == 'true' :
  xbmc . log ( "[addon.live.Supremacy Lists-%s]: %s" % ( o0OOO , string ) )
  if 88 - 88: o0ooo / OOO0O / I1ii * oOOOo0o0O + OoOoo0 % oOOoo
  if 43 - 43: OOooO % ooO00oo - o00ooooO0oO - IiIi11i - II1 + IiIi11i
def o0O0 ( url , headers = None ) :
 try :
  if headers is None :
   headers = { 'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0' }
  O00O0O0O0 = urllib2 . Request ( url , None , headers )
  ooO0O = urllib2 . urlopen ( O00O0O0O0 )
  oo = ooO0O . read ( )
  ooO0O . close ( )
  return oo
 except urllib2 . URLError , iii11iII :
  O00o0o0000o0o ( 'URL: ' + url )
  if hasattr ( iii11iII , 'code' ) :
   O00o0o0000o0o ( 'We failed with error code - %s.' % iii11iII . code )
   xbmc . executebuiltin ( "XBMC.Notification(Supremacy,We failed with error code - " + str ( iii11iII . code ) + ",10000," + O0oo0OO0 + ")" )
  elif hasattr ( iii11iII , 'reason' ) :
   O00o0o0000o0o ( 'We failed to reach a server.' )
   O00o0o0000o0o ( 'Reason: %s' % iii11iII . reason )
   xbmc . executebuiltin ( "XBMC.Notification(Supremacy,We failed to reach a server. - " + str ( iii11iII . reason ) + ",10000," + O0oo0OO0 + ")" )
   if 42 - 42: o00ooooO0oO + OOO0O
   if 70 - 70: IiIIi1I1Iiii % IiIIi1I1Iiii . ooO00oo % Ooo00oOo00o * o0ooo % I1ii
def iiI1IiI ( ) :
 if oOOoo00O0O == _Edit . name :
  O00o0o0000o0o ( "SKindex" )
  II ( '[COLOR blue]======[/COLOR][COLOR red]WELCOME TO SUPREMACY ADD-ON[/COLOR][COLOR blue]======[/COLOR]' , '' , '' , '' , '' , '' , '' )
  ooOoOoo0O ( '[COLOR red]Supremacy Movie Search[/COLOR]' , 'http://stephen-builds.uk/supremacy/Search%20Supremacy%20Movies/home.txt' , 41 , 'http://stephen-builds.uk/art/icon111.jpg' , I1i1iiI1 , '' , '' , '' , '' )
  II ( '[COLOR aqua]24/7 Shows[/COLOR]' , '' , 905 , 'http://stephen-builds.uk/art/24%207%20shows.png' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
  II ( '[COLORaqua]Scraper Movies[/COLOR]' , '' , 999997 , 'http://stephen-builds.uk/art/MOVIE%20SCRAPPER.png' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' , '' , '' )
  ooOoOoo0O ( '[COLORaqua]Scraper Tv Shows[/COLOR]' , '' , 400 , 'http://stephen-builds.uk/art/TV%20SHOWS%20SCRAPPER.png' , I1i1iiI1 , '' , '' , '' , '' , '' )
  ooOoOoo0O ( '[COLORaqua]Freeview[/COLOR]' , 'https://tvcatchup.com/channels' , 301 , 'http://stephen-builds.uk/art/FREEVEW.png' , I1i1iiI1 , '' , '' , '' , '' , '' )
  ooOoOoo0O ( '[COLORaqua]Sport Replays[/COLOR]' , 'http://fullmatchsports.com/' , 500 , 'http://stephen-builds.uk/art/football.png' , I1i1iiI1 , '' , '' , '' , '' , '' )
  #ooOoOoo0O ( '[COLORaqua]Sky Channels[/COLOR]' , '' , 510 , 'http://stephen-builds.uk/art/sky.png' , I1i1iiI1 , '' , '' , '' , '' , '' )
  OooO0 ( _Edit . MainBase , '' )
  if oo00 == o00 :
   ooOoOoo0O ( '[COLOR red]18 only[/COLOR]' , '' , 69 , 'http://stephen-builds.uk/art/18%20only.png' , I1i1iiI1 , '' , '' , '' , '' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 35 - 35: oOOOo0o0O % o00ooooO0oO % i11iIiiIii / II1
def Ii11iI1i ( ) :
 Ooo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 O0o0Oo = 'https://live.proxyportal.net'
 Oo00OOOOO = 'http://unblocked.lol/views/tv.php'
 O0O = requests . get ( O0o0Oo ) . content
 O00o0OO = re . compile ( '<div class="panel-body">.+?href="(.+?)".+?>(.+?)<' , re . DOTALL ) . findall ( O0O )
 for I11i1 , iIi1ii1I1 in O00o0OO :
  I11i1 = O0o0Oo + I11i1
  o0 ( iIi1ii1I1 , Ooo + I11i1 , 906 , '' , I1i1iiI1 , '' , '' )
 I11II1i = requests . get ( Oo00OOOOO ) . content
 IIIII = re . compile ( '<a class="btn btn-secondary btn-block spa".+?href=(.+?) target.+?>(.+?)<' , re . DOTALL ) . findall ( I11II1i )
 for I11i1 , ooooooO0oo in IIIII :
  IIiiiiiiIi1I1 = requests . get ( I11i1 ) . content
  I1IIIii = re . compile ( '"stream":.+?"(.+?)"' , re . DOTALL ) . findall ( IIiiiiiiIi1I1 )
  for oOoOooOo0o0 in I1IIIii :
   oOoOooOo0o0 = 'https:' + oOoOooOo0o0
   if 61 - 61: o0ooo / Ooo00oOo00o + IiIi11i * I1ii / I1ii
   o0 ( ooooooO0oo , Ooo + oOoOooOo0o0 , 906 , '' , I1i1iiI1 , '' , '' )
   if 75 - 75: O00ooooo00 / II1 - OOO0O0O0ooooo / I11iii11IIi . iIiiiI1IiI1I1 - O00ooooo00
   if 71 - 71: oOOOo0o0O + oOOoo * oOOOo0o0O - Ooo00oOo00o * o0ooo
   if 65 - 65: OOO0O0O0ooooo % IIiIiII11i . OOO0O % IIii1I / oOOOo0o0O % o00ooooO0oO
def ooii11I ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 if iconimage == '' :
  iconimage = O0oo0OO0
 if fanart == '' :
  fanart = I1i1iiI1
 if not 'http' in url :
  o0 ( name , url , mode , iconimage , fanart , description , extra )
 elif 'watchseries' in url :
  o0 ( name , url , mode , iconimage , fanart , description , extra )
 elif 'm3u' in url :
  o0 ( name , url , mode , iconimage , fanart , description , extra )
 else :
  Ooo0OO0oOO ( url , name , iconimage , fanart , description , '' , '' , True , '' , '' , 1 , '' )
def ii11i1 ( url ) :
 IIIii1II1II = [ 'How To Download' , 'Contact' , 'DMCA/Privacy Policy' , 'Sitemap' , 'Home' , 'Index' ]
 O0O = requests . get ( url ) . content
 i1I1iI = BeautifulSoup ( O0O )
 oo0OooOOo0 = i1I1iI . findAll ( 'nav' , attrs = { 'id' : 'site-navigation' } )
 for o0O in oo0OooOOo0 :
  O00oO = o0O . findAll ( 'li' )
  if 39 - 39: ooO00oo - iIiiiI1IiI1I1 * Ooo00oOo00o % o0ooo * iIiiiI1IiI1I1 % iIiiiI1IiI1I1
  for OoOOOOO in O00oO :
   if 33 - 33: OOO0O % O00ooooo00
   o00OO00OoO = OoOOOOO . findAll ( 'a' )
   for I11i1 in o00OO00OoO :
    if I11i1 . has_key ( 'href' ) :
     if I11i1 . has_key ( 'itemprop' ) :
      OOOO0OOoO0O0 = I11i1 [ 'href' ]
      O0Oo000ooO00 = I11i1 . findAll ( 'span' )
      for iIi1ii1I1 in O0Oo000ooO00 :
       ooooooO0oo = iIi1ii1I1 . text
       if not ooooooO0oo in IIIii1II1II :
        ooooooO0oo = ooooooO0oo . replace ( 'Full Match' , 'Recent Games' )
        if OOOO0OOoO0O0 == '#' :
         ooOoOoo0O ( '[COLORred]' + ooooooO0oo + '[/COLOR]' , '' , '' , '' , I1i1iiI1 , '' , '' , '' , '' , '' )
        else :
         ooOoOoo0O ( '[COLORaqua]' + ooooooO0oo + '[/COLOR]' , OOOO0OOoO0O0 , 501 , '' , I1i1iiI1 , '' , '' , '' , '' , '' )
         if 75 - 75: I1ii . Ooo00oOo00o * oOOOo0o0O
         if 91 - 91: oOOoo
def iII ( url ) :
 O0O = requests . get ( url ) . content
 i1I1iI = BeautifulSoup ( O0O )
 oo0OooOOo0 = i1I1iI . findAll ( 'div' , attrs = { 'class' : 'content-thumbnail' } )
 for o0O in oo0OooOOo0 :
  o00OO00OoO = o0O . findAll ( 'a' )
  for I11i1 in o00OO00OoO :
   if I11i1 . has_key ( 'href' ) :
    OOOO0OOoO0O0 = I11i1 [ 'href' ]
   o0ooOooo000oOO = I11i1 . findAll ( 'img' )
   for Oo0oOOo in o0ooOooo000oOO :
    O0oo0OO0 = Oo0oOOo [ 'src' ]
    ooooooO0oo = Oo0oOOo [ 'alt' ]
    ooOoOoo0O ( '[COLORaqua]' + ooooooO0oo + '[/COLOR]' , OOOO0OOoO0O0 , 502 , O0oo0OO0 , O0oo0OO0 , '' , '' , '' , '' , '' )
    if 58 - 58: iIiiiI1IiI1I1 * oOOOo0o0O * OOO0O / oOOOo0o0O
def oO0o0OOOO ( url ) :
 O0O = requests . get ( url ) . content
 O00o0OO = re . compile ( '<div class="streaming">(.+?)<div class="tab-content">' , re . DOTALL ) . findall ( O0O )
 if 68 - 68: OOooO - o00ooooO0oO - IIiIiII11i - OOO0O + OoOoo0
 for I11i1 in O00o0OO :
  IIIII = re . compile ( 'href="(.+?)">(.+?)<' , re . DOTALL ) . findall ( str ( I11i1 ) )
  for iiiI1I11i1 , IIi1i11111 in IIIII :
   ooOoOoo0O ( '[COLORaqua]' + IIi1i11111 + '[/COLOR]' , url + iiiI1I11i1 , 503 , '' , '' , '' , '' , '' , '' , '' )
   if 81 - 81: i11iIiiIii % I11iii11IIi - oOOOo0o0O
   if 68 - 68: o00ooooO0oO % O00ooooo00 . ooO00oo . OOO0O
def o0oo0oOo ( url ) :
 O0O = requests . get ( url ) . content
 I1IIIii = re . compile ( '<iframe.+?src="(.+?)"' , re . DOTALL ) . findall ( O0O )
 for I11i1 in I1IIIii :
  if not "facebook" in I11i1 :
   I11i1 = 'http:' + I11i1
   IIiiiiiiIi1I1 = requests . get ( I11i1 ) . content
   o000O0o = re . compile ( '<source src="(.+?)".+?label=\'(.+?)\'' , re . DOTALL ) . findall ( IIiiiiiiIi1I1 )
   for iI1iII1 , oO0OOoo0OO in o000O0o :
    o0 ( '[COLORaqua] link 1' + oO0OOoo0OO + '[/COLOR]' , iI1iII1 , 906 , '' , '' , '' , '' )
   O0 = I11i1 . replace ( 'mirror=1' , 'mirror=2' )
   IIiiiiiiIi1I1 = requests . get ( O0 ) . content
   o000O0o = re . compile ( '<iframe.+?src="(.+?)"' , re . DOTALL ) . findall ( IIiiiiiiIi1I1 )
   for ii1ii1ii in o000O0o :
    o0 ( '[COLORaqua] link 2 [/COLOR]' , ii1ii1ii , 906 , '' , '' , '' , '' )
    if 91 - 91: ooO00oo
    if 15 - 15: iIiiiI1IiI1I1
    if 18 - 18: i11iIiiIii . O00ooooo00 % II1 / OOO0O0O0ooooo
    if 75 - 75: I11iii11IIi % o0ooo % o0ooo . o00ooooO0oO
    if 5 - 5: o0ooo * IiIi11i + I11iii11IIi . oOOOo0o0O + I11iii11IIi
    if 91 - 91: OOO0O0O0ooooo
def oOOo0 ( url ) :
 O00o0o0000o0o ( "get_porn_data" )
 OooO0 ( _Edit . PornBase , '' )
def oo00O00oO ( url ) :
 O00O0O0O0 = urllib2 . Request ( url )
 O00O0O0O0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 ooO0O = ''
 I11i1 = ''
 try :
  ooO0O = urllib2 . urlopen ( O00O0O0O0 )
  I11i1 = ooO0O . read ( )
  ooO0O . close ( )
 except : pass
 if I11i1 != '' :
  return I11i1
 else :
  I11i1 = 'Opened'
  return I11i1
if 23 - 23: Ooo00oOo00o + Ooo00oOo00o . oOOOo0o0O
if 38 - 38: o00ooooO0oO
if 7 - 7: OOO0O0O0ooooo . OOooO % OOO0O - IIiIiII11i - IIii1I
if 36 - 36: ooO00oo % IiIi11i % IiIIi1I1Iiii - OOO0O
if 22 - 22: IIii1I / IiIIi1I1Iiii * OOO0O % OOooO
if 85 - 85: I1ii % i11iIiiIii - OOooO * II1 / IIiIiII11i % IIiIiII11i
if 1 - 1: Ooo00oOo00o - I1ii . OoOoo0 . Ooo00oOo00o / IiIIi1I1Iiii + OoOoo0
def OooOOOOo ( ) :
 II ( '[COLORaqua]New Movies[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/SCRAP%20MOVIES.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]People Watching[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/people%20watching.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]Full List Movies[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/full.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]Movies A - Z[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/A-Z/A-Z.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]Movies Genre[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/Genre/Genre.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]Most Popular[/COLOR]' , 'http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8' , 999996 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]Disaster movies[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/Disaster%20movies.xml' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]Kids Movies[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/Kids%20movies.xml' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]Movie Search[/COLOR]' , '' , 999900 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 if 76 - 76: Ooo00oOo00o
def I1iIIii ( url ) :
 O0O = requests . get ( url ) . text
 O00o0OO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( O0O )
 for ooooooO0oo , iii1i , I11i1ii1 , O0Oooo0O , O0o , OoOooO , II111iiiI1Ii in O00o0OO :
  if II111iiiI1Ii == ' ' :
   II111iiiI1Ii = I1i1iiI1
  if O0Oooo0O == ' ' :
   O0Oooo0O = O0oo0OO0
  O0o = O0o . replace ( '\\n' , ' ' )
  if iii1i == 'Movie Search' :
   o0 ( ooooooO0oo , OoOooO , 999998 , O0Oooo0O , II111iiiI1Ii , O0o , '' )
  elif iii1i == 'Menu' :
   II ( ooooooO0oo , I11i1ii1 , 999999 , O0Oooo0O , II111iiiI1Ii , O0o , '' )
   if 78 - 78: oOOoo % o00ooooO0oO + OOO0O
def OOooOoooOoOo ( url ) :
 O0O = requests . get ( url ) . text
 O00o0OO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<season>(.+?)</season>.+?<episode>(.+?)</episode>.+?<season_year>(.+?)</season_year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( O0O )
 for ooooooO0oo , iii1i , I11i1ii1 , O0Oooo0O , O0o , o0OOOO00O0Oo , ii , oOooOOOoOo , II111iiiI1Ii in O00o0OO :
  if II111iiiI1Ii == ' ' :
   II111iiiI1Ii = I1i1iiI1
  if O0Oooo0O == ' ' :
   O0Oooo0O = O0oo0OO0
  O0o = O0o . replace ( '\\n' , ' ' )
  if iii1i == 'tv search' :
   II ( ooooooO0oo + ' - SEASON -' + o0OOOO00O0Oo + '- EPISODE-' + ii + '-' + oOooOOOoOo , '' , 404 , O0Oooo0O , II111iiiI1Ii , '' , ooooooO0oo )
  elif iii1i == 'Menu' :
   II ( ooooooO0oo , I11i1ii1 , 410 , O0Oooo0O , II111iiiI1Ii , O0o , '' )
   if 41 - 41: oOOoo - OOO0O0O0ooooo - OOO0O0O0ooooo
def oO00OOoO00 ( ) :
 IiI111111IIII = xbmcgui . Dialog ( )
 i1Ii = IiI111111IIII . input ( 'Search your moive' , type = xbmcgui . INPUT_ALPHANUM )
 IIIii1II1II = [ 'http://stephen-builds.uk/supremacy/scrap%20movies/Kids%20movies.xml' , 'http://stephen-builds.uk/supremacy/scrap%20movies/SCRAP%20MOVIES.txt' , 'http://stephen-builds.uk/supremacy/scrap%20movies/A-Z/A-Z.txt' , 'http://stephen-builds.uk/supremacy/scrap%20movies/full.txt' ]
 for O0o0Oo in IIIii1II1II :
  O0O = requests . get ( O0o0Oo ) . content
  O00o0OO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( O0O )
  for ooooooO0oo , iii1i , I11i1ii1 , O0Oooo0O , O0o , OoOooO , II111iiiI1Ii in O00o0OO :
   if II111iiiI1Ii == ' ' :
    II111iiiI1Ii = I1i1iiI1
   if O0Oooo0O == ' ' :
    O0Oooo0O = O0oo0OO0
   O0o = O0o . replace ( '\\n' , ' ' )
   if iii1i == 'Movie Search' :
    if i1Ii . lower ( ) in ooooooO0oo . lower ( ) :
     o0 ( ooooooO0oo , OoOooO , 999998 , O0Oooo0O , II111iiiI1Ii , O0o , '' )
     if 14 - 14: OOooO
     if 11 - 11: ooO00oo * IIiIiII11i . IIii1I % II1 + OOooO
def OOO ( url ) :
 II ( '[COLORaqua]Most Popular By Genre[/COLOR]' , 'http://www.imdb.com/genre/?ref_=nv_ch_gr_3' , 999995 , '' , '' , '' , '' , '' , '' )
 oo0OOo0 = 'http://imdb.com'
 O0O = requests . get ( 'http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8' ) . content
 O00o0OO = re . compile ( '<td class="posterColumn">.+?title=.+?>(.+?)</a>.+?<span class="secondaryInfo">(.+?)</span>' , re . DOTALL ) . findall ( O0O )
 for iIi1ii1I1 , OoOooO in O00o0OO :
  I11IiI = OoOooO . replace ( '(' , '' ) . replace ( ')' , '' )
  o0 ( iIi1ii1I1 + '  [COLORred]' + OoOooO + '[/COLOR]' , I11IiI , 999998 , '' , '' , OoOooO , iIi1ii1I1 )
  if 53 - 53: OOooO % iIiiiI1IiI1I1 . ooO00oo - IIii1I - ooO00oo * iIiiiI1IiI1I1
def ooO0oOOooOo0 ( url ) :
 O0O = requests . get ( url ) . content
 O00o0OO = re . compile ( '<tr class=".+?".+?<h3>.+?href="(.+?)">(.+?)<.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( O0O )
 for i1I1ii11i1Iii , I1IiiiiI , o0OIiII in O00o0OO :
  II ( '[COLORaqua]' + I1IiiiiI . upper ( ) + '[/COLOR]' , i1I1ii11i1Iii , 999994 , '' , '' , '' , '' , '' , '' )
  if 25 - 25: OOO0O0O0ooooo - OOO0O0O0ooooo * o0ooo
def OOOO0oo0 ( url ) :
 if 35 - 35: oOOoo - IIiIiII11i % o0ooo . II1 % oOOoo
 O0O = requests . get ( url ) . content
 O00o0OO = re . compile ( '<td class="image">.+?title="(.+?)".+?<span class="year_type">(.+?)<' , re . DOTALL ) . findall ( O0O )
 for I1i1Iiiii , OOo0oO00ooO00 in O00o0OO :
  I1i1Iiiii = I1i1Iiiii . replace ( '&#x26;#x27;' , '' ) . replace ( '&#x26;' , '' ) . replace ( '&#x27;' , '' )
  I11IiI = OOo0oO00ooO00 [ 1 : 5 ]
  o0 ( I1i1Iiiii + '  [COLORred]' + OOo0oO00ooO00 + '[/COLOR]' , I11IiI , 999998 , '' , '' , OOo0oO00ooO00 , I1i1Iiiii )
  if 90 - 90: I11iii11IIi * o00ooooO0oO + o0ooo
def OO ( url ) :
 if 83 - 83: OOO0O0O0ooooo / IIiIiII11i - Ooo00oOo00o - oOOOo0o0O
 O0O = requests . get ( url ) . content
 i1I1iI = BeautifulSoup ( O0O )
 if 36 - 36: ooO00oo
 if 36 - 36: IiIi11i / OOO0O0O0ooooo * IiIIi1I1Iiii - oOOOo0o0O % IIii1I * I1ii
 oo0OooOOo0 = i1I1iI . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for o0O in oo0OooOOo0 :
  if 79 - 79: OOO0O0O0ooooo
  o00OO00OoO = o0O . findAll ( 'a' )
  for I11i1 in o00OO00OoO :
   if I11i1 . has_key ( 'href' ) :
    oOO00O = 'https://tvcatchup.com' + I11i1 [ 'href' ]
   OOOoo0OO = I11i1 . findAll ( 'img' , attrs = { 'style' : "" } )
   if 57 - 57: Ooo00oOo00o / IiIi11i
   for Ii1I1Ii in OOOoo0OO :
    Oo0oOOo = Ii1I1Ii [ 'src' ]
    OOoO0 = Ii1I1Ii [ 'alt' ]
   O00o0OO = re . compile ( '<br />(.+?)</a>' ) . findall ( str ( I11i1 ) )
   for OO0Oooo0oOO0O in O00o0OO :
    ooOoOoo0O ( '[COLORgold]' + OOoO0 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + OO0Oooo0oOO0O + '[/COLOR]' , oOO00O , 302 , '' , '' , '' , '' , '' , '' , '' )
    if 62 - 62: IIiIiII11i
def O00o0OO0 ( ) :
 if 35 - 35: I1ii % IiIi11i / o00ooooO0oO + IIii1I . II1 . IIiIiII11i
 ooOoOoo0O ( '[COLORaqua][B]Tv Shows List[/COLOR][/B]' , 'http://www.tvmaze.com/shows' , 402 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' , '' )
 ooOoOoo0O ( '[COLORred]SEARCH Tv Shows[/COLOR]' , '' , 405 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' , '' )
 ooOoOoo0O ( '[COLORaqua]Popular Tv Shows[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/tv%20shows/gotmain.txt' , 410 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' , '' )
 ooOoOoo0O ( '[COLORaqua]Netflix Original Tv Shows[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/Netflix%20Original%20Tv%20Shows/Netflix%20Original%20Tv%20Shows.txt' , 410 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' , '' )
 if 71 - 71: ooO00oo * iIiiiI1IiI1I1 * I1ii
 if 56 - 56: IIiIiII11i
def O0oO ( url ) :
 II ( '[COLORsteelblue]SEARCH[/COLOR]' , '' , 405 , '' , I1i1iiI1 , '' , '' )
 O0O = requests . get ( url ) . content
 O00o0OO = re . compile ( '<figure class="image small-12 cell">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( O0O )
 OO0ooOOO0OOO = re . compile ( '<li class="next"><a href="(.+?)"' ) . findall ( O0O )
 for url , Oo0oOOo , iIi1ii1I1 in O00o0OO :
  oO00oooOOoOo0 = 'http://www.tvmaze.com' + url . replace ( '"' , '' )
  IIiiiiiiIi1I1 = requests . get ( oO00oooOOoOo0 ) . content
  O00o0OO = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiiiiiiIi1I1 )
  for OoOOoOooooOOo in O00o0OO :
   if not '<div>' in OoOOoOooooOOo :
    oOo0O = OoOOoOooooOOo . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   Oo0oOOo = 'http:' + Oo0oOOo
   iIi1ii1I1 = iIi1ii1I1 . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if iIi1ii1I1 == '' :
    oo0O0 = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( url ) )
    for iIi1ii1I1 in oo0O0 :
     iIi1ii1I1 = iIi1ii1I1 . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  II ( iIi1ii1I1 , oO00oooOOoOo0 , 403 , Oo0oOOo , II111iiiI1Ii , oOo0O , '' )
  if 22 - 22: I11iii11IIi . oOOOo0o0O * I11iii11IIi
 for O000OOO in OO0ooOOO0OOO :
  url = 'http://www.tvmaze.com' + O000OOO
  II ( 'NEXT' , url , 402 , Oo0oOOo , II111iiiI1Ii , '' , '' )
  if 20 - 20: o0ooo . iIiiiI1IiI1I1 % oOOOo0o0O * IIii1I
def oO00oOOoooO ( url , name , iconimage ) :
 ooooooO0oo = name . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
 Oo0oOOo = iconimage
 O0O = requests . get ( url + '/episodes' ) . content
 IIiiiiiiIi1I1 = requests . get ( url ) . content
 IiIi11iI = re . compile ( "<h2 data-magellan-target='(.+?)'.+?<tbody>(.+?)</tbody>" , re . DOTALL ) . findall ( O0O )
 O00o0OO = re . compile ( '<span id="year">\((.+?)-' , re . DOTALL ) . findall ( IIiiiiiiIi1I1 )
 for oOooOOOoOo in O00o0OO :
  oOooOOOoOo = oOooOOOoOo . replace ( ' ' , '' )
 for o0OOOO00O0Oo , o0OIiII in IiIi11iI :
  if not 'special' in o0OOOO00O0Oo . lower ( ) :
   o0OOOO00O0Oo = o0OOOO00O0Oo . replace ( 'S' , '' ) . replace ( 's' , '' )
  Oo0O00O000 = re . compile ( '<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( str ( o0OIiII ) )
  for ii , i11I1IiII1i1i , ooI1111i in Oo0O00O000 :
   if not 'special' in ii . lower ( ) :
    II ( ooooooO0oo + ' - SEASON -' + o0OOOO00O0Oo + '- EPISODE-' + ii + '-' + oOooOOOoOo , '' , 404 , Oo0oOOo , II111iiiI1Ii , '' , ooooooO0oo )
    if 14 - 14: oOOOo0o0O / o0ooo
def iII11I1IiiIi ( ) :
 IiI111111IIII = xbmcgui . Dialog ( )
 i1Ii = IiI111111IIII . input ( 'Searching...' , type = xbmcgui . INPUT_ALPHANUM )
 oo0oO = 'http://www.tvmaze.com/search?q=' + ( i1Ii ) . replace ( ' ' , '+' )
 Oo0O0 = oo0oO . lower ( )
 Ooo0OOoOoO0 = requests . get ( Oo0O0 ) . content
 O00o0OO = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( Ooo0OOoOoO0 )
 for O0o0Oo , Oo0oOOo , iIi1ii1I1 in O00o0OO :
  oO00oooOOoOo0 = 'http://www.tvmaze.com' + O0o0Oo . replace ( '"' , '' )
  IIiiiiiiIi1I1 = requests . get ( oO00oooOOoOo0 ) . content
  O00o0OO = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiiiiiiIi1I1 )
  for OoOOoOooooOOo in O00o0OO :
   if not '<div>' in OoOOoOooooOOo :
    oOo0O = OoOOoOooooOOo . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   Oo0oOOo = 'http:' + Oo0oOOo
   iIi1ii1I1 = iIi1ii1I1 . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if iIi1ii1I1 == '' :
    oo0O0 = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( O0o0Oo ) )
    for iIi1ii1I1 in oo0O0 :
     iIi1ii1I1 = iIi1ii1I1 . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  II ( iIi1ii1I1 , oO00oooOOoOo0 , 403 , Oo0oOOo , II111iiiI1Ii , oOo0O , '' )
  if 70 - 70: I1ii
def oOOoO0o0oO ( name , extra ) :
 if 93 - 93: ooO00oo * II1 + IiIi11i
 IiII111i1i11 = xbmcgui . DialogProgress ( )
 IiII111i1i11 . create ( 'Checking for stream' )
 from modules import Scrape_Nan
 i111iIi1i1II1 = name + '<>'
 oooO = re . compile ( '(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>' ) . findall ( str ( i111iIi1i1II1 ) )
 for ooooooO0oo , i1I1i111Ii , ooo , oOooOOOoOo in oooO :
  ooooooO0oo = ooooooO0oo
  i1I1i111Ii = i1I1i111Ii
  ooo = ooo
  i1i1iI1iiiI = ''
  Scrape_Nan . scrape_episode ( ooooooO0oo , oOooOOOoOo , '' , i1I1i111Ii , ooo , '' )
  if 51 - 51: IIiIiII11i % o00ooooO0oO . I1ii / IIii1I / OoOoo0 . I1ii
def IIIii11 ( url ) :
 import base64
 iI1Ii11111iIi = base64 . decodestring
 O0O = requests . get ( url ) . content
 O00o0OO = re . compile ( 'var.+?=.+?"(.+?)"' , re . DOTALL ) . findall ( O0O )
 for IIi1i11111 in O00o0OO :
  if not 'text' in IIi1i11111 :
   url = iI1Ii11111iIi ( iI1Ii11111iIi ( IIi1i11111 ) )
   iiIiIIIiiI ( '' , url )
   if 12 - 12: OOO0O0O0ooooo - o0ooo
def oOoO00O0 ( url ) :
 import resolveurl
 try :
  OOIi1iI111II1I1 = resolveurl . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( OOIi1iI111II1I1 , xbmcgui . ListItem ( iIi1ii1I1 ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( iIi1ii1I1 ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "ERROR" , "unplayable stream" )
   sys . exit ( )
   if 91 - 91: oOOOo0o0O % oOOOo0o0O - IIiIiII11i
def I1iiii1I ( extra , url ) :
 from modules import Scrape_Nan
 iIi1ii1I1 = str ( extra )
 OoOooO = str ( url )
 IiII111i1i11 = xbmcgui . DialogProgress ( )
 IiII111i1i11 . create ( 'Checking for stream' )
 Scrape_Nan . scrape_movie ( iIi1ii1I1 , OoOooO , '' )
 if 54 - 54: IIiIiII11i / o00ooooO0oO / IIii1I % Ooo00oOo00o % oOOoo
def oooOoOoo0oOo00 ( url ) :
 IiI111111IIII = xbmcgui . Dialog ( )
 IiiiIiii11 = IiI111111IIII . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0000o = IiiiIiii11 . lower ( )
 if OO0000o == '' :
  pass
 else :
  i1I1i1 ( OO0000o , url )
  if 81 - 81: IiIi11i - IIii1I - O00ooooo00 / o00ooooO0oO - OOO0O0O0ooooo * OoOoo0
def i1I1i1 ( Search_name , url ) :
 Ooo0OOoOoO0 = oo00O00oO ( url )
 if Ooo0OOoOoO0 != 'Failed' :
  O00o0OO = re . compile ( '<channel>.+?<name>(.+?)</name>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>.+?<fanart>(.+?)</fanart>.+?</channel>' , re . DOTALL ) . findall ( Ooo0OOoOoO0 )
  for iIi1ii1I1 , o0ooOooo000oOO , url , II111iiiI1Ii in O00o0OO :
   if not 'http:' in url :
    pass
   else :
    i1I1i1 ( Search_name , url )
  I1IIIii = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( Ooo0OOoOoO0 )
  for iIi1ii1I1 , url , o0ooOooo000oOO , II111iiiI1Ii in I1IIIii :
   if 'http:' in url :
    if Search_name . lower ( ) in iIi1ii1I1 . lower ( ) :
     Ooo0OO0oOO ( url , iIi1ii1I1 , o0ooOooo000oOO , II111iiiI1Ii , '' , '' , '' , '' , None , '' , 1 )
     if 20 - 20: I1ii % ooO00oo
     if 19 - 19: OOO0O % ooO00oo + IiIi11i / o00ooooO0oO . IiIi11i
def IiIi1I1 ( ) :
 if os . path . exists ( iI111iI ) == True :
  ooOoOoo0O ( 'Favorites' , 'url' , 4 , os . path . join ( Iii1ii1II11i , 'resources' , 'favorite.png' ) , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "browse_xml_database" ) == "true" :
  ooOoOoo0O ( 'XML Database' , 'http://xbmcplus.xb.funpic.de/www-data/filesystem/' , 15 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "browse_community" ) == "true" :
  ooOoOoo0O ( 'Community Files' , 'community_files' , 16 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if os . path . exists ( IiII ) == True :
  ooOoOoo0O ( 'Search History' , 'history' , 25 , os . path . join ( Iii1ii1II11i , 'resources' , 'favorite.png' ) , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "searchyt" ) == "true" :
  ooOoOoo0O ( 'Search:Youtube' , 'youtube' , 25 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "searchDM" ) == "true" :
  ooOoOoo0O ( 'Search:dailymotion' , 'dmotion' , 25 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "PulsarM" ) == "true" :
  ooOoOoo0O ( 'Pulsar:IMDB' , 'IMDBidplay' , 27 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if os . path . exists ( iiIIIII1i1iI ) == True :
  IiIIi1 = json . loads ( open ( iiIIIII1i1iI , "r" ) . read ( ) )
  if 47 - 47: IiIIi1I1Iiii * OOO0O + IIii1I / o00ooooO0oO / Ooo00oOo00o - II1
  if len ( IiIIi1 ) > 1 :
   for iII1i11IIi1i in IiIIi1 :
    if 73 - 73: o0ooo * OOO0O0O0ooooo - i11iIiiIii
    if isinstance ( iII1i11IIi1i , list ) :
     ooOoOoo0O ( iII1i11IIi1i [ 0 ] . encode ( 'utf-8' ) , iII1i11IIi1i [ 1 ] . encode ( 'utf-8' ) , 1 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' , 'source' )
    else :
     O0O0o0oOOO = O0oo0OO0
     II111iiiI1Ii = I1i1iiI1
     OoOOoOooooOOo = ''
     OOoOoOo = ''
     credits = ''
     o000ooooO0o = ''
     if iII1i11IIi1i . has_key ( 'thumbnail' ) :
      O0O0o0oOOO = iII1i11IIi1i [ 'thumbnail' ]
     if iII1i11IIi1i . has_key ( 'fanart' ) :
      II111iiiI1Ii = iII1i11IIi1i [ 'fanart' ]
     if iII1i11IIi1i . has_key ( 'description' ) :
      OoOOoOooooOOo = iII1i11IIi1i [ 'description' ]
     if iII1i11IIi1i . has_key ( 'date' ) :
      OOoOoOo = iII1i11IIi1i [ 'date' ]
     if iII1i11IIi1i . has_key ( 'genre' ) :
      o000ooooO0o = iII1i11IIi1i [ 'genre' ]
     if iII1i11IIi1i . has_key ( 'credits' ) :
      credits = iII1i11IIi1i [ 'credits' ]
     ooOoOoo0O ( iII1i11IIi1i [ 'title' ] . encode ( 'utf-8' ) , iII1i11IIi1i [ 'url' ] . encode ( 'utf-8' ) , 1 , O0O0o0oOOO , II111iiiI1Ii , OoOOoOooooOOo , o000ooooO0o , OOoOoOo , credits , 'source' )
     if 40 - 40: OOO0O + O00ooooo00 * oOOOo0o0O
  else :
   if len ( IiIIi1 ) == 1 :
    if isinstance ( IiIIi1 [ 0 ] , list ) :
     OooO0 ( IiIIi1 [ 0 ] [ 1 ] . encode ( 'utf-8' ) , I1i1iiI1 )
    else :
     OooO0 ( IiIIi1 [ 0 ] [ 'url' ] , IiIIi1 [ 0 ] [ 'fanart' ] )
     if 85 - 85: oOOoo * IiIIi1I1Iiii . OOO0O0O0ooooo - i11iIiiIii
     if 18 - 18: oOOoo + ooO00oo - OOO0O0O0ooooo
def o00O ( url = None ) :
 if url is None :
  if not I1IiI . getSetting ( "new_file_source" ) == "" :
   i1Ii1i1I11Iii = I1IiI . getSetting ( 'new_file_source' ) . decode ( 'utf-8' )
  elif not I1IiI . getSetting ( "new_url_source" ) == "" :
   i1Ii1i1I11Iii = I1IiI . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  i1Ii1i1I11Iii = url
 if i1Ii1i1I11Iii == '' or i1Ii1i1I11Iii is None :
  return
 O00o0o0000o0o ( 'Adding New Source: ' + i1Ii1i1I11Iii . encode ( 'utf-8' ) )
 if 25 - 25: ooO00oo + oOOoo / IiIi11i . o0ooo % OOO0O0O0ooooo * Ooo00oOo00o
 o0O0oo0OO0O = None
 if 68 - 68: I1ii . OoOoo0 % II1 . OoOoo0
 oo = OoooO ( i1Ii1i1I11Iii )
 print 'source_url' , i1Ii1i1I11Iii
 if isinstance ( oo , BeautifulSOAP ) :
  if oo . find ( 'channels_info' ) :
   o0O0oo0OO0O = oo . channels_info
  elif oo . find ( 'items_info' ) :
   o0O0oo0OO0O = oo . items_info
 if o0O0oo0OO0O :
  iIII = { }
  iIII [ 'url' ] = i1Ii1i1I11Iii
  try : iIII [ 'title' ] = o0O0oo0OO0O . title . string
  except : pass
  try : iIII [ 'thumbnail' ] = o0O0oo0OO0O . thumbnail . string
  except : pass
  try : iIII [ 'fanart' ] = o0O0oo0OO0O . fanart . string
  except : pass
  try : iIII [ 'genre' ] = o0O0oo0OO0O . genre . string
  except : pass
  try : iIII [ 'description' ] = o0O0oo0OO0O . description . string
  except : pass
  try : iIII [ 'date' ] = o0O0oo0OO0O . date . string
  except : pass
  try : iIII [ 'credits' ] = o0O0oo0OO0O . credits . string
  except : pass
 else :
  if '/' in i1Ii1i1I11Iii :
   iIi = i1Ii1i1I11Iii . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in i1Ii1i1I11Iii :
   iIi = i1Ii1i1I11Iii . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in iIi :
   iIi = urllib . unquote_plus ( iIi )
  ii111I = xbmc . Keyboard ( iIi , 'Displayed Name, Rename?' )
  ii111I . doModal ( )
  if ( ii111I . isConfirmed ( ) == False ) :
   return
  iiI = ii111I . getText ( )
  if len ( iiI ) == 0 :
   return
  iIII = { }
  iIII [ 'title' ] = iiI
  iIII [ 'url' ] = i1Ii1i1I11Iii
  iIII [ 'fanart' ] = II111iiiI1Ii
  if 7 - 7: I11iii11IIi + iIiiiI1IiI1I1 . O00ooooo00
 if os . path . exists ( iiIIIII1i1iI ) == False :
  Ooo0 = [ ]
  Ooo0 . append ( iIII )
  I1IiiiiI = open ( iiIIIII1i1iI , "w" )
  I1IiiiiI . write ( json . dumps ( Ooo0 ) )
  I1IiiiiI . close ( )
 else :
  IiIIi1 = json . loads ( open ( iiIIIII1i1iI , "r" ) . read ( ) )
  IiIIi1 . append ( iIII )
  I1IiiiiI = open ( iiIIIII1i1iI , "w" )
  I1IiiiiI . write ( json . dumps ( IiIIi1 ) )
  I1IiiiiI . close ( )
 I1IiI . setSetting ( 'new_url_source' , "" )
 I1IiI . setSetting ( 'new_file_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(Supremacy,New source added.,5000," + O0oo0OO0 + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : I1IiI . openSettings ( )
 if 34 - 34: IIiIiII11i % OOooO + IiIi11i * IIii1I
 if 33 - 33: IIiIiII11i / IiIi11i * oOOOo0o0O / OOO0O + IiIIi1I1Iiii / OOooO
def iII1I1I1 ( name ) :
 IiIIi1 = json . loads ( open ( iiIIIII1i1iI , "r" ) . read ( ) )
 for i11IIIiI11 in range ( len ( IiIIi1 ) ) :
  if isinstance ( IiIIi1 [ i11IIIiI11 ] , list ) :
   if IiIIi1 [ i11IIIiI11 ] [ 0 ] == name :
    del IiIIi1 [ i11IIIiI11 ]
    I1IiiiiI = open ( iiIIIII1i1iI , "w" )
    I1IiiiiI . write ( json . dumps ( IiIIi1 ) )
    I1IiiiiI . close ( )
    break
  else :
   if IiIIi1 [ i11IIIiI11 ] [ 'title' ] == name :
    del IiIIi1 [ i11IIIiI11 ]
    I1IiiiiI = open ( iiIIIII1i1iI , "w" )
    I1IiiiiI . write ( json . dumps ( IiIIi1 ) )
    I1IiiiiI . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 8 - 8: Ooo00oOo00o + o00ooooO0oO - o0ooo % IiIIi1I1Iiii % o0ooo * I1ii
 if 9 - 9: IiIIi1I1Iiii - i11iIiiIii - oOOOo0o0O * oOOoo + IiIi11i
 if 44 - 44: iIiiiI1IiI1I1
def OOOO0OOO ( url , browse = False ) :
 if url is None :
  url = 'http://xbmcplus.xb.funpic.de/www-data/filesystem/'
 i1I1iI = BeautifulSoup ( o0O0 ( url ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 for iII1i11IIi1i in i1I1iI ( 'a' ) :
  oOO00O = iII1i11IIi1i [ 'href' ]
  if not oOO00O . startswith ( '?' ) :
   iIi1ii1I1 = iII1i11IIi1i . string
   if iIi1ii1I1 not in [ 'Parent Directory' , 'recycle_bin/' ] :
    if oOO00O . endswith ( '/' ) :
     if browse :
      ooOoOoo0O ( iIi1ii1I1 , url + oOO00O , 15 , O0oo0OO0 , II111iiiI1Ii , '' , '' , '' )
     else :
      ooOoOoo0O ( iIi1ii1I1 , url + oOO00O , 14 , O0oo0OO0 , II111iiiI1Ii , '' , '' , '' )
    elif oOO00O . endswith ( '.xml' ) :
     if browse :
      ooOoOoo0O ( iIi1ii1I1 , url + oOO00O , 1 , O0oo0OO0 , II111iiiI1Ii , '' , '' , '' , '' , 'download' )
     else :
      if os . path . exists ( iiIIIII1i1iI ) == True :
       if iIi1ii1I1 in i1 :
        ooOoOoo0O ( iIi1ii1I1 + ' (in use)' , url + oOO00O , 11 , O0oo0OO0 , II111iiiI1Ii , '' , '' , '' , '' , 'download' )
       else :
        ooOoOoo0O ( iIi1ii1I1 , url + oOO00O , 11 , O0oo0OO0 , II111iiiI1Ii , '' , '' , '' , '' , 'download' )
      else :
       ooOoOoo0O ( iIi1ii1I1 , url + oOO00O , 11 , O0oo0OO0 , II111iiiI1Ii , '' , '' , '' , '' , 'download' )
       if 3 - 3: Ooo00oOo00o
       if 97 - 97: o00ooooO0oO
def iiIII1i ( browse = False ) :
 O0o0Oo = 'http://community-links.googlecode.com/svn/trunk/'
 i1I1iI = BeautifulSoup ( o0O0 ( O0o0Oo ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 I1I = i1I1iI ( 'ul' ) [ 0 ] ( 'li' ) [ 1 : ]
 for iII1i11IIi1i in I1I :
  iIi1ii1I1 = iII1i11IIi1i ( 'a' ) [ 0 ] [ 'href' ]
  if browse :
   ooOoOoo0O ( iIi1ii1I1 , O0o0Oo + iIi1ii1I1 , 1 , O0oo0OO0 , II111iiiI1Ii , '' , '' , '' , '' , 'download' )
  else :
   ooOoOoo0O ( iIi1ii1I1 , O0o0Oo + iIi1ii1I1 , 11 , O0oo0OO0 , II111iiiI1Ii , '' , '' , '' , '' , 'download' )
   if 68 - 68: IiIi11i
   if 25 - 25: OOO0O . IiIi11i
def OoooO ( url , data = None ) :
 print 'getsoup' , url , data
 if url . startswith ( 'http://' ) or url . startswith ( 'https://' ) :
  data = o0O0 ( url )
  if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
   print 'found m3u data' , data
   return data
   if 24 - 24: I1ii / i11iIiiIii + I1ii
 elif data == None :
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    I1i11i = xbmcvfs . copy ( url , os . path . join ( iIiiiI , 'temp' , 'sorce_temp.txt' ) )
    if I1i11i :
     data = open ( os . path . join ( iIiiiI , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( iIiiiI , 'temp' , 'sorce_temp.txt' ) )
    else :
     O00o0o0000o0o ( "failed to copy from smb:" )
   else :
    data = open ( url , 'r' ) . read ( )
    if re . match ( "#EXTM3U" , data ) or 'm3u' in url :
     print 'found m3u data' , data
     return data
  else :
   O00o0o0000o0o ( "Soup Data not found!" )
   return
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 11 - 11: IIiIiII11i / iIiiiI1IiI1I1 + o0ooo * OOO0O - OOO0O - IIiIiII11i
 if 85 - 85: OoOoo0 % I1ii / IIii1I . IIii1I
def OooO0 ( url , fanart ) :
 print 'url-getData' , url
 iIIiIiI1I1 = "List"
 if 56 - 56: IIiIiII11i . OOO0O0O0ooooo + IiIIi1I1Iiii
 i1I1iI = OoooO ( url )
 if 1 - 1: OOooO
 if isinstance ( i1I1iI , BeautifulSOAP ) :
  if len ( i1I1iI ( 'layoutype' ) ) > 0 :
   iIIiIiI1I1 = "Thumbnail"
   if 97 - 97: oOOOo0o0O + OOooO + OOO0O0O0ooooo + i11iIiiIii
  if len ( i1I1iI ( 'channels' ) ) > 0 :
   oOoO0 = i1I1iI ( 'channel' )
   for Oo0 in oOoO0 :
    if 83 - 83: i11iIiiIii % o0ooo % IiIi11i
    if 11 - 11: iIiiiI1IiI1I1 % Ooo00oOo00o * OOooO + IiIi11i + oOOoo
    II1Iiiiii = ''
    ii1ii111 = 0
    try :
     II1Iiiiii = Oo0 ( 'externallink' ) [ 0 ] . string
     ii1ii111 = len ( Oo0 ( 'externallink' ) )
    except : pass
    if 10 - 10: o00ooooO0oO % ooO00oo * ooO00oo . OoOoo0 / oOOoo % oOOOo0o0O
    if ii1ii111 > 1 : II1Iiiiii = ''
    if 49 - 49: Ooo00oOo00o / I1ii + OOO0O0O0ooooo * o0ooo
    iIi1ii1I1 = Oo0 ( 'name' ) [ 0 ] . string
    I1ii11 = Oo0 ( 'thumbnail' ) [ 0 ] . string
    if I1ii11 == None :
     I1ii11 = ''
     if 74 - 74: IiIIi1I1Iiii - o0ooo . O00ooooo00
    try :
     if not Oo0 ( 'fanart' ) :
      if I1IiI . getSetting ( 'use_thumb' ) == "true" :
       i1III = I1ii11
      else :
       i1III = fanart
     else :
      i1III = Oo0 ( 'fanart' ) [ 0 ] . string
     if i1III == None :
      raise
    except :
     i1III = fanart
     if 49 - 49: i11iIiiIii % oOOoo . I11iii11IIi
    try :
     OoOOoOooooOOo = Oo0 ( 'info' ) [ 0 ] . string
     if OoOOoOooooOOo == None :
      raise
    except :
     OoOOoOooooOOo = ''
     if 13 - 13: i11iIiiIii + O00ooooo00 * IIii1I % II1 - iIiiiI1IiI1I1 * oOOOo0o0O
    try :
     o000ooooO0o = Oo0 ( 'genre' ) [ 0 ] . string
     if o000ooooO0o == None :
      raise
    except :
     o000ooooO0o = ''
     if 26 - 26: II1 * IIiIiII11i + oOOOo0o0O
    try :
     OOoOoOo = Oo0 ( 'date' ) [ 0 ] . string
     if OOoOoOo == None :
      raise
    except :
     OOoOoOo = ''
     if 24 - 24: i11iIiiIii % IIii1I + oOOOo0o0O / i11iIiiIii
    try :
     credits = Oo0 ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 70 - 70: Ooo00oOo00o * OOO0O0O0ooooo . OoOoo0 + IIiIiII11i . ooO00oo
    try :
     if II1Iiiiii == '' :
      ooOoOoo0O ( iIi1ii1I1 . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , I1ii11 , i1III , OoOOoOooooOOo , o000ooooO0o , OOoOoOo , credits , True )
     else :
      if 14 - 14: IIii1I % IIii1I * i11iIiiIii - Ooo00oOo00o - OoOoo0
      ooOoOoo0O ( iIi1ii1I1 . encode ( 'utf-8' ) , II1Iiiiii . encode ( 'utf-8' ) , 1 , I1ii11 , i1III , OoOOoOooooOOo , o000ooooO0o , OOoOoOo , None , 'source' )
    except :
     O00o0o0000o0o ( 'There was a problem adding directory from getData(): ' + iIi1ii1I1 . encode ( 'utf-8' , 'ignore' ) )
  else :
   O00o0o0000o0o ( 'No Channels: getItems' )
   o00oo0 ( i1I1iI ( 'item' ) , fanart )
 else :
  oooooOOO000Oo ( i1I1iI )
  if 52 - 52: iIiiiI1IiI1I1 % ooO00oo . I11iii11IIi * IIii1I
 if iIIiIiI1I1 == "Thumbnail" :
  I111i1II ( )
  if 69 - 69: oOOoo * OOO0O0O0ooooo . i11iIiiIii / oOOoo . o0ooo
  if 63 - 63: OoOoo0 + o0ooo . iIiiiI1IiI1I1 - IIiIiII11i
  if 52 - 52: o0ooo % IiIIi1I1Iiii
  if 64 - 64: OOO0O0O0ooooo % OoOoo0 % OOO0O0O0ooooo * Ooo00oOo00o . I1ii + IIiIiII11i
  if 75 - 75: OoOoo0 . II1 % o0ooo * OoOoo0 % II1
def oooooOOO000Oo ( data ) :
 I11i1iIiIIIIIii = data . rstrip ( )
 O00o0OO = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)' ) . findall ( I11i1iIiIIIIIii )
 OOo0 = len ( O00o0OO )
 print 'total m3u links' , OOo0
 for ii11I1 , oO0oo , Ii111iIi1iIi in O00o0OO :
  if 'tvg-logo' in ii11I1 :
   I1ii11 = IIIIIo0ooOoO000oO ( ii11I1 , 'tvg-logo=[\'"](.*?)[\'"]' )
   if I1ii11 :
    if I1ii11 . startswith ( 'http' ) :
     I1ii11 = I1ii11
     if 85 - 85: o0ooo . I11iii11IIi / IiIi11i . OOO0O0O0ooooo % o00ooooO0oO
    elif not I1IiI . getSetting ( 'logo-folderPath' ) == "" :
     OO0ooo0oOO = I1IiI . getSetting ( 'logo-folderPath' )
     I1ii11 = OO0ooo0oOO + I1ii11
     if 97 - 97: IIiIiII11i / OOooO
    else :
     I1ii11 = I1ii11
     if 71 - 71: iIiiiI1IiI1I1 / O00ooooo00 . OOO0O % II1 . I11iii11IIi
     if 41 - 41: O00ooooo00 * iIiiiI1IiI1I1 / II1 . oOOOo0o0O
  else :
   I1ii11 = ''
  if 'type' in ii11I1 :
   O0iII1 = IIIIIo0ooOoO000oO ( ii11I1 , 'type=[\'"](.*?)[\'"]' )
   if O0iII1 == 'yt-dl' :
    Ii111iIi1iIi = Ii111iIi1iIi + "&mode=18"
   elif O0iII1 == 'regex' :
    O0o0Oo = Ii111iIi1iIi . split ( '&regexs=' )
    if 27 - 27: Ooo00oOo00o . OoOoo0 + I11iii11IIi / IIii1I % OOooO . IiIi11i
    IIIIi1 = iIi11iiIiI1I ( OoooO ( '' , data = O0o0Oo [ 1 ] ) )
    if 3 - 3: O00ooooo00 / iIiiiI1IiI1I1 / i11iIiiIii * O00ooooo00 - iIiiiI1IiI1I1
    Ooo0OO0oOO ( O0o0Oo [ 0 ] , oO0oo , I1ii11 , '' , '' , '' , '' , '' , None , IIIIi1 , OOo0 )
    continue
  Ooo0OO0oOO ( Ii111iIi1iIi , oO0oo , I1ii11 , '' , '' , '' , '' , '' , None , '' , OOo0 )
  if 42 - 42: iIiiiI1IiI1I1 . II1 . o0ooo * I1ii
 xbmc . executebuiltin ( "Container.SetViewMode(50)" )
 if 81 - 81: oOOoo * o0ooo + o00ooooO0oO + IiIIi1I1Iiii - II1
def i1i1I111iIi1 ( name , url , fanart ) :
 i1I1iI = OoooO ( url )
 oo00O00oO000o = i1I1iI . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 OOo00OoO = oo00O00oO000o ( 'item' )
 try :
  i1III = oo00O00oO000o ( 'fanart' ) [ 0 ] . string
  if i1III == None :
   raise
 except :
  i1III = fanart
 for Oo0 in oo00O00oO000o ( 'subchannel' ) :
  name = Oo0 ( 'name' ) [ 0 ] . string
  try :
   I1ii11 = Oo0 ( 'thumbnail' ) [ 0 ] . string
   if I1ii11 == None :
    raise
  except :
   I1ii11 = ''
  try :
   if not Oo0 ( 'fanart' ) :
    if I1IiI . getSetting ( 'use_thumb' ) == "true" :
     i1III = I1ii11
   else :
    i1III = Oo0 ( 'fanart' ) [ 0 ] . string
   if i1III == None :
    raise
  except :
   pass
  try :
   OoOOoOooooOOo = Oo0 ( 'info' ) [ 0 ] . string
   if OoOOoOooooOOo == None :
    raise
  except :
   OoOOoOooooOOo = ''
   if 10 - 10: o0ooo / i11iIiiIii
  try :
   o000ooooO0o = Oo0 ( 'genre' ) [ 0 ] . string
   if o000ooooO0o == None :
    raise
  except :
   o000ooooO0o = ''
   if 92 - 92: OoOoo0 . o00ooooO0oO
  try :
   OOoOoOo = Oo0 ( 'date' ) [ 0 ] . string
   if OOoOoOo == None :
    raise
  except :
   OOoOoOo = ''
   if 85 - 85: OOO0O . o00ooooO0oO
  try :
   credits = Oo0 ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 78 - 78: IiIi11i * o00ooooO0oO + IIii1I + IIii1I / o00ooooO0oO . oOOoo
  try :
   ooOoOoo0O ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , I1ii11 , i1III , OoOOoOooooOOo , o000ooooO0o , credits , OOoOoOo )
  except :
   O00o0o0000o0o ( 'There was a problem adding directory - ' + name . encode ( 'utf-8' , 'ignore' ) )
 o00oo0 ( OOo00OoO , i1III )
 if 97 - 97: IiIi11i / o00ooooO0oO % O00ooooo00 % OOO0O
 if 18 - 18: IIii1I % OoOoo0
def O00oO0 ( name , url , fanart ) :
 i1I1iI = OoooO ( url )
 oo00O00oO000o = i1I1iI . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 OOo00OoO = oo00O00oO000o ( 'subitem' )
 o00oo0 ( OOo00OoO , fanart )
 if 97 - 97: o00ooooO0oO - IIii1I
 if 75 - 75: II1 * ooO00oo
def I1Iiiiiii ( name , url , iconimage , fanart ) :
 IIIii1II1II = [ ] ; I1IIIiI1I1ii1 = [ ] ; iiiI1I1iIIIi1 = 0
 Iii = I1iiiiI1iI ( url , 'sublink:' , '#' )
 for i1I1ii11i1Iii in Iii :
  if 'LISTSOURCE:' in i1I1ii11i1Iii :
   iIiiiii1i = iiIi1IIiI ( i1I1ii11i1Iii , 'LISTSOURCE:' , '::' )
   i1oO0OO0 = iiIi1IIiI ( i1I1ii11i1Iii , 'LISTNAME:' , '::' )
  else :
   iIiiiii1i = i1I1ii11i1Iii . replace ( 'sublink:' , '' ) . replace ( '#' , '' )
   i1oO0OO0 = name
  if len ( iIiiiii1i ) > 10 :
   iiiI1I1iIIIi1 = iiiI1I1iIIIi1 + 1 ; IIIii1II1II . append ( i1oO0OO0 ) ; I1IIIiI1I1ii1 . append ( iIiiiii1i )
   if 82 - 82: ooO00oo - ooO00oo + I11iii11IIi
 if iiiI1I1iIIIi1 == 1 :
  try :
   if 8 - 8: o0ooo % OOooO * I1ii % oOOoo . IiIi11i / IiIi11i
   o0O0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
   OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1IIIiI1I1ii1 [ 0 ] , listitem = o0O0O0o )
   xbmc . Player ( ) . play ( ooO000 ( I1IIIiI1I1ii1 [ 0 ] ) , o0O0O0o )
  except :
   pass
 else :
  oOOOO = xbmcgui . Dialog ( )
  Ii = oOOOO . select ( 'Supremacy Select A Source' , IIIii1II1II )
  if Ii >= 0 :
   Ii1ii111i1 = name
   i1i1i1I = str ( I1IIIiI1I1ii1 [ Ii ] )
   if 83 - 83: I1ii + II1
   try :
    o0O0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
    OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = o0O0O0o )
    xbmc . Player ( ) . play ( ooO000 ( i1i1i1I ) , o0O0O0o )
   except :
    pass
    if 22 - 22: oOOoo % OOooO * II1 - o0ooo / IIii1I
    if 86 - 86: II1 . OOooO % I11iii11IIi / OoOoo0 * OOooO / o0ooo
def oO ( ) :
 if 60 - 60: OOO0O * IIiIiII11i
 I1iIiI11I1 = 'Name of channel show or movie'
 i1oOOoo0o0OOOO = ''
 ii111I = xbmc . Keyboard ( i1oOOoo0o0OOOO , I1iIiI11I1 )
 ii111I . doModal ( )
 if ii111I . isConfirmed ( ) :
  i1oOOoo0o0OOOO = ii111I . getText ( ) . replace ( '\n' , '' ) . strip ( )
  if len ( i1oOOoo0o0OOOO ) == 0 :
   xbmcgui . Dialog ( ) . ok ( 'RobinHood' , 'Nothing Entered' )
   return
   if 26 - 26: OOooO % IIii1I + o0ooo
 i1oOOoo0o0OOOO = i1oOOoo0o0OOOO . lower ( )
 IIIii1II1II = [ ]
 IIIii1II1II . append ( _Edit . MainBase )
 OOOooo = 0
 Oo00oo0000OO = 1
 O0oOOo0Oo = 0
 o000O000 = 0
 ii1 = xbmcgui . DialogProgress ( )
 ii1 . create ( 'Supremacy Searching Please wait' , ' ' )
 if 77 - 77: IIiIiII11i % OOO0O0O0ooooo
 while Oo00oo0000OO <> O0oOOo0Oo :
  I1iii = IIIii1II1II [ O0oOOo0Oo ] . strip ( )
  print 'read this one from file list (' + str ( O0oOOo0Oo ) + ')'
  O0oOOo0Oo = O0oOOo0Oo + 1
  if 86 - 86: OOO0O * OOO0O0O0ooooo * ooO00oo
  Ooo0oo = ''
  try :
   Ooo0oo = net . http_GET ( I1iii ) . content
   Ooo0oo = Ooo0oo . encode ( 'ascii' , 'ignore' ) . decode ( 'ascii' )
   if 41 - 41: I11iii11IIi * OoOoo0 / I11iii11IIi % I1ii
  except :
   pass
   if 18 - 18: iIiiiI1IiI1I1 . II1 % I11iii11IIi % oOOoo
  if len ( Ooo0oo ) < 10 :
   Ooo0oo = ''
   OOOooo = OOOooo + 1
   print '*** PASSED ****' + I1iii + '  ************* Total Passed Urls: ' + str ( OOOooo )
   time . sleep ( .5 )
   if 9 - 9: Ooo00oOo00o - IiIIi1I1Iiii * II1 . IiIIi1I1Iiii
  ii1Ii1IiIIi = int ( ( O0oOOo0Oo / 300 ) * 100 )
  o0OO0 = '     Pages Read: ' + str ( O0oOOo0Oo ) + '        Matches Found: ' + str ( o000O000 )
  ii1 . update ( ii1Ii1IiIIi , "" , o0OO0 , "" )
  if 100 - 100: IiIIi1I1Iiii * o00ooooO0oO / o00ooooO0oO
  if ii1 . iscanceled ( ) :
   return
   if 41 - 41: IIii1I % OoOoo0
  if len ( Ooo0oo ) > 10 :
   oOo0oO = I1iiiiI1iI ( Ooo0oo , '<channel>' , '</channel>' )
   for i1I1ii11i1Iii in oOo0oO :
    iIiiiii1i = iiIi1IIiI ( i1I1ii11i1Iii , '<externallink>' , '</externallink>' )
    if 5 - 5: oOOOo0o0O - oOOOo0o0O . IiIIi1I1Iiii + I11iii11IIi - oOOOo0o0O . I1ii
    if 31 - 31: iIiiiI1IiI1I1 - IIii1I - IIii1I % OoOoo0
    if len ( iIiiiii1i ) > 5 :
     Oo00oo0000OO = Oo00oo0000OO + 1
     IIIii1II1II . append ( iIiiiii1i )
     if 12 - 12: IIii1I
     if 20 - 20: o0ooo / O00ooooo00
   oOIi111 = I1iiiiI1iI ( Ooo0oo , '<item>' , '</item>' )
   for i1I1ii11i1Iii in oOIi111 :
    iIiiiii1i = iiIi1IIiI ( i1I1ii11i1Iii , '<link>' , '</link>' )
    iIi1ii1I1 = iiIi1IIiI ( i1I1ii11i1Iii , '<title>' , '</title>' )
    oO0 = '  ' + iIi1ii1I1 . lower ( ) + '  '
    if 11 - 11: IiIi11i / iIiiiI1IiI1I1
    if len ( iIiiiii1i ) > 5 and oO0 . find ( i1oOOoo0o0OOOO ) > 0 :
     o000O000 = o000O000 + 1
     II111iiiI1Ii = ''
     I1ii11 = iiIi1IIiI ( i1I1ii11i1Iii , '<thumbnail>' , '</thumbnail>' )
     II111iiiI1Ii = iiIi1IIiI ( i1I1ii11i1Iii , '<fanart>' , '</fanart>' )
     if len ( II111iiiI1Ii ) < 5 :
      II111iiiI1Ii = O0oo0OO0
     if iIiiiii1i . find ( 'sublink' ) > 0 :
      ooOoOoo0O ( iIi1ii1I1 , iIiiiii1i , 30 , I1ii11 , II111iiiI1Ii , '' , '' , '' , '' )
     else :
      Ooo0OO0oOO ( str ( iIiiiii1i ) , iIi1ii1I1 , I1ii11 , II111iiiI1Ii , '' , '' , '' , True , None , '' , 1 )
      if 47 - 47: II1
      if 4 - 4: IIiIiII11i % OoOoo0
 ii1 . close ( )
 xbmc . executebuiltin ( "Container.SetViewMode(50)" )
 if 10 - 10: ooO00oo . II1 - Ooo00oOo00o + ooO00oo - OOO0O0O0ooooo
def o0oO00 ( data , Searchkey ) :
 I11i1iIiIIIIIii = data . rstrip ( )
 O00o0OO = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)' ) . findall ( I11i1iIiIIIIIii )
 OOo0 = len ( O00o0OO )
 print 'total m3u links' , OOo0
 for ii11I1 , oO0oo , Ii111iIi1iIi in O00o0OO :
  if 'tvg-logo' in ii11I1 :
   I1ii11 = IIIIIo0ooOoO000oO ( ii11I1 , 'tvg-logo=[\'"](.*?)[\'"]' )
   if I1ii11 :
    if I1ii11 . startswith ( 'http' ) :
     I1ii11 = I1ii11
     if 65 - 65: oOOOo0o0O . o00ooooO0oO . Ooo00oOo00o . OOooO - oOOOo0o0O
    elif not I1IiI . getSetting ( 'logo-folderPath' ) == "" :
     OO0ooo0oOO = I1IiI . getSetting ( 'logo-folderPath' )
     I1ii11 = OO0ooo0oOO + I1ii11
     if 19 - 19: i11iIiiIii + OOooO % IiIi11i
    else :
     I1ii11 = I1ii11
     if 14 - 14: Ooo00oOo00o . iIiiiI1IiI1I1 . OoOoo0 / oOOoo % OOO0O - IiIi11i
     if 67 - 67: OoOoo0 - oOOOo0o0O . O00ooooo00
  else :
   I1ii11 = ''
  if 'type' in ii11I1 :
   O0iII1 = IIIIIo0ooOoO000oO ( ii11I1 , 'type=[\'"](.*?)[\'"]' )
   if O0iII1 == 'yt-dl' :
    Ii111iIi1iIi = Ii111iIi1iIi + "&mode=18"
   elif O0iII1 == 'regex' :
    O0o0Oo = Ii111iIi1iIi . split ( '&regexs=' )
    if 35 - 35: OOooO + IiIi11i - I1ii . OOooO . ooO00oo
    IIIIi1 = iIi11iiIiI1I ( OoooO ( '' , data = O0o0Oo [ 1 ] ) )
    if 87 - 87: I11iii11IIi
    Ooo0OO0oOO ( O0o0Oo [ 0 ] , oO0oo , I1ii11 , '' , '' , '' , '' , '' , None , IIIIi1 , OOo0 )
    continue
  Ooo0OO0oOO ( Ii111iIi1iIi , oO0oo , I1ii11 , '' , '' , '' , '' , '' , None , '' , OOo0 )
  if 25 - 25: O00ooooo00 . Ooo00oOo00o - I11iii11IIi / Ooo00oOo00o % Ooo00oOo00o * IIii1I
def III ( text , pattern ) :
 iIiIi11Ii = ""
 try :
  iIII1i1i = re . findall ( pattern , text , flags = re . DOTALL )
  iIiIi11Ii = iIII1i1i [ 0 ]
 except :
  iIiIi11Ii = ""
  if 35 - 35: iIiiiI1IiI1I1 * OoOoo0 - II1 . OoOoo0 . OoOoo0
 return iIiIi11Ii
 if 11 - 11: o00ooooO0oO / I11iii11IIi + OoOoo0 % IIii1I
def I1iiiiI1iI ( text , start_with , end_with ) :
 II1II1iIIi11 = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return II1II1iIIi11
 if 49 - 49: II1 * OoOoo0 - IiIIi1I1Iiii . I1ii
def iiIi1IIiI ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : II1II1iIIi11 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : II1II1iIIi11 = ''
 else :
  try : II1II1iIIi11 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : II1II1iIIi11 = ''
 return II1II1iIIi11
 if 89 - 89: IiIi11i + oOOoo * IiIi11i / IiIi11i
def o00oo0 ( items , fanart ) :
 OOo0 = len ( items )
 print 'START GET ITEMS *****'
 O00o0o0000o0o ( 'Total Items: %s' % OOo0 )
 for i11i11 in items :
  OoOoO00O0 = False
  OoOOO = False
  try :
   iIi1ii1I1 = i11i11 ( 'title' ) [ 0 ] . string
   if iIi1ii1I1 is None :
    iIi1ii1I1 = 'unknown?'
  except :
   O00o0o0000o0o ( 'Name Error' )
   iIi1ii1I1 = ''
   if 67 - 67: OOooO % OOooO / OOooO
   if 53 - 53: IIii1I
  try :
   if i11i11 ( 'epg' ) :
    if i11i11 . epg_url :
     O00o0o0000o0o ( 'Get EPG Regex' )
     oooo00o0o0o = i11i11 . epg_url . string
     O0Oo00oO0O00 = i11i11 . epg_regex . string
     IiO000O0OO00oo = oOOO ( oooo00o0o0o , O0Oo00oO0O00 )
     if IiO000O0OO00oo :
      iIi1ii1I1 += ' - ' + IiO000O0OO00oo
    elif i11i11 ( 'epg' ) [ 0 ] . string > 1 :
     iIi1ii1I1 += ooo0oooo0 ( i11i11 ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   O00o0o0000o0o ( 'EPG Error' )
  try :
   O0o0Oo = [ ]
   if len ( i11i11 ( 'link' ) ) > 0 :
    if 62 - 62: OOO0O + oOOoo + O00ooooo00 / II1
    for iII1i11IIi1i in i11i11 ( 'link' ) :
     if not iII1i11IIi1i . string == None :
      O0o0Oo . append ( iII1i11IIi1i . string )
      if 7 - 7: o0ooo + O00ooooo00 . IIiIiII11i / IiIIi1I1Iiii
   elif len ( i11i11 ( 'sportsdevil' ) ) > 0 :
    for iII1i11IIi1i in i11i11 ( 'sportsdevil' ) :
     if not iII1i11IIi1i . string == None :
      I111i1I1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + iII1i11IIi1i . string
      O0o00OOo00O0O = i11i11 ( 'referer' ) [ 0 ] . string
      if O0o00OOo00O0O :
       if 5 - 5: o0ooo / II1 * o0ooo * OOO0O0O0ooooo . oOOoo % ooO00oo
       I111i1I1 = I111i1I1 + '%26referer=' + O0o00OOo00O0O
      O0o0Oo . append ( I111i1I1 )
   elif len ( i11i11 ( 'p2p' ) ) > 0 :
    for iII1i11IIi1i in i11i11 ( 'p2p' ) :
     if not iII1i11IIi1i . string == None :
      if 'sop://' in iII1i11IIi1i :
       i111I11i = 'plugin://plugin.video.p2p-streams/?url=' + iII1i11IIi1i . string + '&amp;mode=2&amp;' + 'name=' + iIi1ii1I1
       O0o0Oo . append ( i111I11i )
      else :
       ii1OoOO = 'plugin://plugin.video.p2p-streams/?url=' + iII1i11IIi1i . string + '&amp;mode=1&amp;' + 'name=' + iIi1ii1I1
       O0o0Oo . append ( ii1OoOO )
   elif len ( i11i11 ( 'vaughn' ) ) > 0 :
    for iII1i11IIi1i in i11i11 ( 'vaughn' ) :
     if not iII1i11IIi1i . string == None :
      iIII1I1i1i = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=' + iII1i11IIi1i . string
      O0o0Oo . append ( iIII1I1i1i )
   elif len ( i11i11 ( 'ilive' ) ) > 0 :
    for iII1i11IIi1i in i11i11 ( 'ilive' ) :
     if not iII1i11IIi1i . string == None :
      if not 'http' in iII1i11IIi1i . string :
       o0OIIiI1I1 = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/' + iII1i11IIi1i . string + '&amp;link=99&amp;mode=iLivePlay'
      else :
       o0OIIiI1I1 = 'plugin://plugin.video.tbh.ilive/?url=' + iII1i11IIi1i . string + '&amp;link=99&amp;mode=iLivePlay'
   elif len ( i11i11 ( 'yt-dl' ) ) > 0 :
    for iII1i11IIi1i in i11i11 ( 'yt-dl' ) :
     if not iII1i11IIi1i . string == None :
      I11I1IIiiII1 = iII1i11IIi1i . string + '&mode=18'
      O0o0Oo . append ( I11I1IIiiII1 )
   elif len ( i11i11 ( 'utube' ) ) > 0 :
    for iII1i11IIi1i in i11i11 ( 'utube' ) :
     if not iII1i11IIi1i . string == None :
      if len ( iII1i11IIi1i . string ) == 11 :
       IIIIIii1ii11 = 'plugin://plugin.video.youtube/play/?video_id=' + iII1i11IIi1i . string
      elif iII1i11IIi1i . string . startswith ( 'PL' ) and not '&order=' in iII1i11IIi1i . string :
       IIIIIii1ii11 = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + iII1i11IIi1i . string
      else :
       IIIIIii1ii11 = 'plugin://plugin.video.youtube/play/?playlist_id=' + iII1i11IIi1i . string
    O0o0Oo . append ( IIIIIii1ii11 )
   elif len ( i11i11 ( 'imdb' ) ) > 0 :
    for iII1i11IIi1i in i11i11 ( 'imdb' ) :
     if not iII1i11IIi1i . string == None :
      if I1IiI . getSetting ( 'genesisorpulsar' ) == '0' :
       OOOooo0OooOoO = 'plugin://plugin.video.genesis/?action=play&imdb=' + iII1i11IIi1i . string
      else :
       OOOooo0OooOoO = 'plugin://plugin.video.pulsar/movie/tt' + iII1i11IIi1i . string + '/play'
      O0o0Oo . append ( OOOooo0OooOoO )
   elif len ( i11i11 ( 'f4m' ) ) > 0 :
    for iII1i11IIi1i in i11i11 ( 'f4m' ) :
     if not iII1i11IIi1i . string == None :
      if '.f4m' in iII1i11IIi1i . string :
       oOoOOOo = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( iII1i11IIi1i . string )
      elif '.m3u8' in iII1i11IIi1i . string :
       oOoOOOo = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( iII1i11IIi1i . string ) + '&amp;streamtype=HLS'
       if 43 - 43: O00ooooo00
      else :
       oOoOOOo = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( iII1i11IIi1i . string ) + '&amp;streamtype=SIMPLE'
    O0o0Oo . append ( oOoOOOo )
   elif len ( i11i11 ( 'ftv' ) ) > 0 :
    for iII1i11IIi1i in i11i11 ( 'ftv' ) :
     if not iII1i11IIi1i . string == None :
      I1i11II = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( iIi1ii1I1 ) + '&url=' + iII1i11IIi1i . string + '&mode=125&ch_fanart=na'
     O0o0Oo . append ( I1i11II )
   if len ( O0o0Oo ) < 1 :
    raise
  except :
   O00o0o0000o0o ( 'Error <link> element, Passing:' + iIi1ii1I1 . encode ( 'utf-8' , 'ignore' ) )
   continue
   if 31 - 31: I1ii / ooO00oo * o0ooo . iIiiiI1IiI1I1
  OoOoO00O0 = False
  if 89 - 89: OOO0O0O0ooooo
  try :
   OoOoO00O0 = i11i11 ( 'externallink' ) [ 0 ] . string
  except : pass
  if 2 - 2: OOO0O . OOO0O + OOO0O * o0ooo
  if OoOoO00O0 :
   oOo00oOOOOO = [ OoOoO00O0 ]
   OoOoO00O0 = True
  else :
   OoOoO00O0 = False
  try :
   OoOOO = i11i11 ( 'jsonrpc' ) [ 0 ] . string
  except : pass
  if OoOOO :
   oOo00oOOOOO = [ OoOOO ]
   OoOOO = True
  else :
   OoOOO = False
  try :
   I1ii11 = i11i11 ( 'thumbnail' ) [ 0 ] . string
   if I1ii11 == None :
    raise
  except :
   I1ii11 = ''
  try :
   if not i11i11 ( 'fanart' ) :
    if I1IiI . getSetting ( 'use_thumb' ) == "true" :
     i1III = I1ii11
    else :
     i1III = fanart
   else :
    i1III = i11i11 ( 'fanart' ) [ 0 ] . string
   if i1III == None :
    raise
  except :
   i1III = fanart
  try :
   OoOOoOooooOOo = i11i11 ( 'info' ) [ 0 ] . string
   if OoOOoOooooOOo == None :
    raise
  except :
   OoOOoOooooOOo = ''
   if 85 - 85: II1 - Ooo00oOo00o - o00ooooO0oO / IiIi11i - OoOoo0
  try :
   o000ooooO0o = i11i11 ( 'genre' ) [ 0 ] . string
   if o000ooooO0o == None :
    raise
  except :
   o000ooooO0o = ''
   if 49 - 49: I11iii11IIi / IiIIi1I1Iiii . i11iIiiIii
  try :
   OOoOoOo = i11i11 ( 'date' ) [ 0 ] . string
   if OOoOoOo == None :
    raise
  except :
   OOoOoOo = ''
   if 21 - 21: I11iii11IIi + i11iIiiIii + IIiIiII11i * o0ooo % OOooO % iIiiiI1IiI1I1
  IIIIi1 = None
  if i11i11 ( 'regex' ) :
   try :
    oOO0OO0OO = i11i11 ( 'regex' )
    IIIIi1 = iIi11iiIiI1I ( oOO0OO0OO )
   except :
    pass
    if 87 - 87: I1ii + IIii1I - II1
  try :
   if len ( O0o0Oo ) > 1 :
    if 8 - 8: II1 / OoOoo0 + O00ooooo00 . OOooO
    OOoO0 = 0
    ooo0ooO = [ ]
    for iII1i11IIi1i in O0o0Oo :
     if I1IiI . getSetting ( 'ask_playlist_items' ) == 'true' :
      if IIIIi1 :
       ooo0ooO . append ( iII1i11IIi1i + '&regexs=' + IIIIi1 )
      elif any ( x in iII1i11IIi1i for x in OO0o ) and iII1i11IIi1i . startswith ( 'http' ) :
       ooo0ooO . append ( iII1i11IIi1i + '&mode=19' )
     else :
      ooo0ooO . append ( iII1i11IIi1i )
    if I1IiI . getSetting ( 'add_playlist' ) == "false" :
     for iII1i11IIi1i in O0o0Oo :
      OOoO0 += 1
      print 'ADDLINK 1'
      Ooo0OO0oOO ( iII1i11IIi1i , '%s) %s' % ( OOoO0 , iIi1ii1I1 . encode ( 'utf-8' , 'ignore' ) ) , I1ii11 , i1III , OoOOoOooooOOo , o000ooooO0o , OOoOoOo , True , ooo0ooO , IIIIi1 , OOo0 )
    else :
     Ooo0OO0oOO ( '' , iIi1ii1I1 . encode ( 'utf-8' , 'ignore' ) , I1ii11 , i1III , OoOOoOooooOOo , o000ooooO0o , OOoOoOo , True , ooo0ooO , IIIIi1 , OOo0 )
   else :
    if OoOoO00O0 :
     ooOoOoo0O ( iIi1ii1I1 . encode ( 'utf-8' ) , oOo00oOOOOO [ 0 ] . encode ( 'utf-8' ) , 1 , I1ii11 , fanart , OoOOoOooooOOo , o000ooooO0o , OOoOoOo , None , 'source' )
    elif OoOOO :
     ooOoOoo0O ( iIi1ii1I1 . encode ( 'utf-8' ) , oOo00oOOOOO [ 0 ] , 53 , I1ii11 , fanart , OoOOoOooooOOo , o000ooooO0o , OOoOoOo , None , 'source' )
    elif O0o0Oo [ 0 ] . find ( 'sublink' ) > 0 :
     ooOoOoo0O ( iIi1ii1I1 . encode ( 'utf-8' ) , O0o0Oo [ 0 ] , 30 , I1ii11 , fanart , '' , '' , '' , '' )
     if 17 - 17: OOO0O . iIiiiI1IiI1I1 . IiIi11i / OOO0O
    else :
     Ooo0OO0oOO ( O0o0Oo [ 0 ] , iIi1ii1I1 . encode ( 'utf-8' , 'ignore' ) , I1ii11 , i1III , OoOOoOooooOOo , o000ooooO0o , OOoOoOo , True , None , IIIIi1 , OOo0 )
     if 57 - 57: OoOoo0
     if 67 - 67: Ooo00oOo00o . IiIi11i
  except :
   O00o0o0000o0o ( 'There was a problem adding item - ' + iIi1ii1I1 . encode ( 'utf-8' , 'ignore' ) )
 print 'FINISH GET ITEMS *****'
 if 87 - 87: I1ii % oOOoo
def iIi11iiIiI1I ( reg_item ) :
 try :
  IIIIi1 = { }
  for iII1i11IIi1i in reg_item :
   IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] = { }
   if 83 - 83: iIiiiI1IiI1I1 - OoOoo0
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'expre' ] = iII1i11IIi1i ( 'expres' ) [ 0 ] . string
    if not IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'expre' ] :
     IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'expre' ] = ''
   except :
    O00o0o0000o0o ( "Regex: -- No Referer --" )
   IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'page' ] = iII1i11IIi1i ( 'page' ) [ 0 ] . string
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'refer' ] = iII1i11IIi1i ( 'referer' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No Referer --" )
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'connection' ] = iII1i11IIi1i ( 'connection' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No connection --" )
    if 35 - 35: O00ooooo00 - IIii1I + O00ooooo00
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'notplayable' ] = iII1i11IIi1i ( 'notplayable' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No notplayable --" )
    if 86 - 86: IIii1I + I11iii11IIi . i11iIiiIii - oOOoo
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'noredirect' ] = iII1i11IIi1i ( 'noredirect' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No noredirect --" )
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'origin' ] = iII1i11IIi1i ( 'origin' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No origin --" )
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'includeheaders' ] = iII1i11IIi1i ( 'includeheaders' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No includeheaders --" )
    if 51 - 51: I11iii11IIi
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'x-req' ] = iII1i11IIi1i ( 'x-req' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No x-req --" )
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'x-forward' ] = iII1i11IIi1i ( 'x-forward' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No x-forward --" )
    if 14 - 14: ooO00oo % I1ii % IiIIi1I1Iiii - i11iIiiIii
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'agent' ] = iII1i11IIi1i ( 'agent' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No User Agent --" )
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'post' ] = iII1i11IIi1i ( 'post' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a post" )
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'rawpost' ] = iII1i11IIi1i ( 'rawpost' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a rawpost" )
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'htmlunescape' ] = iII1i11IIi1i ( 'htmlunescape' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a htmlunescape" )
    if 53 - 53: oOOoo % IiIIi1I1Iiii
    if 59 - 59: oOOOo0o0O % IIii1I . O00ooooo00 + iIiiiI1IiI1I1 * ooO00oo
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'readcookieonly' ] = iII1i11IIi1i ( 'readcookieonly' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a readCookieOnly" )
    if 41 - 41: oOOoo % OOO0O
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = iII1i11IIi1i ( 'cookiejar' ) [ 0 ] . string
    if not IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] :
     IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = ''
   except :
    O00o0o0000o0o ( "Regex: -- Not a cookieJar" )
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'setcookie' ] = iII1i11IIi1i ( 'setcookie' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a setcookie" )
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'appendcookie' ] = iII1i11IIi1i ( 'appendcookie' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a appendcookie" )
    if 12 - 12: oOOOo0o0O
   try :
    IIIIi1 [ iII1i11IIi1i ( 'name' ) [ 0 ] . string ] [ 'ignorecache' ] = iII1i11IIi1i ( 'ignorecache' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- no ignorecache" )
    if 69 - 69: II1 + oOOOo0o0O
    if 26 - 26: IiIIi1I1Iiii + oOOOo0o0O / Ooo00oOo00o % I11iii11IIi % OOO0O + iIiiiI1IiI1I1
    if 31 - 31: OoOoo0 % oOOOo0o0O * OoOoo0
    if 45 - 45: O00ooooo00 . IIiIiII11i + oOOOo0o0O - II1 % IiIi11i
    if 1 - 1: IIii1I
  IIIIi1 = urllib . quote ( repr ( IIIIi1 ) )
  return IIIIi1
  if 93 - 93: O00ooooo00 . i11iIiiIii . IiIIi1I1Iiii
 except :
  IIIIi1 = None
  O00o0o0000o0o ( 'regex Error: ' + iIi1ii1I1 . encode ( 'utf-8' , 'ignore' ) )
  if 99 - 99: OoOoo0 - o00ooooO0oO - I1ii % Ooo00oOo00o
def IiiIIiiiiii ( url ) :
 try :
  for iII1i11IIi1i in range ( 1 , 51 ) :
   iIiIi11Ii = OOOO0o ( url )
   if "EXT-X-STREAM-INF" in iIiIi11Ii : return url
   if not "EXTM3U" in iIiIi11Ii : return
   xbmc . sleep ( 2000 )
  return
 except :
  return
  if 10 - 10: o00ooooO0oO % IIiIiII11i
  if 97 - 97: II1 - o00ooooO0oO
def oooo00 ( regexs , url , cookieJar = None , forCookieJarOnly = False , recursiveCall = False , cachedPages = { } , rawPost = False , cookie_jar_file = None ) :
 if not recursiveCall :
  regexs = eval ( urllib . unquote ( regexs ) )
  if 96 - 96: OOO0O % IiIi11i % oOOoo - IiIi11i % I11iii11IIi + OOO0O
  if 3 - 3: OOO0O0O0ooooo
 Ooo0Oo0oo0 = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 if 83 - 83: o00ooooO0oO
 ii111Ii11iii = True
 if 62 - 62: IIii1I
 if 93 - 93: I1ii - o0ooo % I11iii11IIi . I11iii11IIi - IiIi11i
 if 90 - 90: IiIi11i + iIiiiI1IiI1I1 * OOO0O / oOOoo . o0ooo + o0ooo
 if 40 - 40: IiIi11i / I11iii11IIi % i11iIiiIii % OOO0O / IIiIiII11i
 for ooOOOOo0 in Ooo0Oo0oo0 :
  if ooOOOOo0 in regexs :
   if 38 - 38: II1 / OOO0O . OOO0O0O0ooooo / O00ooooo00 / IiIIi1I1Iiii + IIii1I
   ooO00O00oOO = regexs [ ooOOOOo0 ]
   if 40 - 40: OOooO . I1ii + IIiIiII11i + OOO0O + o00ooooO0oO
   i11 = False
   if 20 - 20: II1 - IiIIi1I1Iiii % I11iii11IIi % OoOoo0
   if 89 - 89: I1ii / II1 . OOooO
   if 'cookiejar' in ooO00O00oOO :
    if 34 - 34: OOooO - II1 . IIiIiII11i / iIiiiI1IiI1I1
    i11 = ooO00O00oOO [ 'cookiejar' ]
    if '$doregex' in i11 :
     cookieJar = oooo00 ( regexs , ooO00O00oOO [ 'cookiejar' ] , cookieJar , True , True , cachedPages )
     i11 = True
    else :
     i11 = True
     if 27 - 27: Ooo00oOo00o / IiIIi1I1Iiii * IiIi11i - Ooo00oOo00o
   if i11 :
    if cookieJar == None :
     if 19 - 19: OoOoo0
     cookie_jar_file = None
     if 'open[' in ooO00O00oOO [ 'cookiejar' ] :
      cookie_jar_file = ooO00O00oOO [ 'cookiejar' ] . split ( 'open[' ) [ 1 ] . split ( ']' ) [ 0 ]
      if 67 - 67: OOO0O0O0ooooo % IIii1I / ooO00oo . i11iIiiIii - oOOoo + OOO0O0O0ooooo
     cookieJar = i1iiiIi1i ( cookie_jar_file )
     if cookie_jar_file :
      OO0Oo ( cookieJar , cookie_jar_file )
      if 45 - 45: II1 % I1ii - OOO0O - I1ii - IIiIiII11i / o0ooo
      if 81 - 81: iIiiiI1IiI1I1 + i11iIiiIii / OOooO
      if 85 - 85: i11iIiiIii + o00ooooO0oO * I11iii11IIi
    elif 'save[' in ooO00O00oOO [ 'cookiejar' ] :
     cookie_jar_file = ooO00O00oOO [ 'cookiejar' ] . split ( 'save[' ) [ 1 ] . split ( ']' ) [ 0 ]
     iiiII = os . path . join ( iIiiiI , cookie_jar_file )
     print 'complete_path' , iiiII
     OO0Oo ( cookieJar , cookie_jar_file )
     if 57 - 57: OoOoo0 . IiIIi1I1Iiii + iIiiiI1IiI1I1
     if 43 - 43: o00ooooO0oO % OOooO
   if ooO00O00oOO [ 'page' ] and '$doregex' in ooO00O00oOO [ 'page' ] :
    ooO00O00oOO [ 'page' ] = oooo00 ( regexs , ooO00O00oOO [ 'page' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 69 - 69: OOooO % Ooo00oOo00o
   if 'setcookie' in ooO00O00oOO and ooO00O00oOO [ 'setcookie' ] and '$doregex' in ooO00O00oOO [ 'setcookie' ] :
    ooO00O00oOO [ 'setcookie' ] = oooo00 ( regexs , ooO00O00oOO [ 'setcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if 'appendcookie' in ooO00O00oOO and ooO00O00oOO [ 'appendcookie' ] and '$doregex' in ooO00O00oOO [ 'appendcookie' ] :
    ooO00O00oOO [ 'appendcookie' ] = oooo00 ( regexs , ooO00O00oOO [ 'appendcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 86 - 86: I1ii / I1ii
    if 28 - 28: i11iIiiIii / o0ooo . IIii1I / iIiiiI1IiI1I1
   if 'post' in ooO00O00oOO and '$doregex' in ooO00O00oOO [ 'post' ] :
    ooO00O00oOO [ 'post' ] = oooo00 ( regexs , ooO00O00oOO [ 'post' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    print 'post is now' , ooO00O00oOO [ 'post' ]
    if 72 - 72: II1 / IIiIiII11i + oOOoo / I11iii11IIi * oOOoo
   if 'rawpost' in ooO00O00oOO and '$doregex' in ooO00O00oOO [ 'rawpost' ] :
    ooO00O00oOO [ 'rawpost' ] = oooo00 ( regexs , ooO00O00oOO [ 'rawpost' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages , rawPost = True )
    if 34 - 34: OOO0O0O0ooooo * OOO0O0O0ooooo % II1 + OOooO * IIii1I % oOOoo
    if 25 - 25: OoOoo0 + I11iii11IIi . o0ooo % I11iii11IIi * oOOOo0o0O
   if 'rawpost' in ooO00O00oOO and '$epoctime$' in ooO00O00oOO [ 'rawpost' ] :
    ooO00O00oOO [ 'rawpost' ] = ooO00O00oOO [ 'rawpost' ] . replace ( '$epoctime$' , ii1IiIi11 ( ) )
    if 22 - 22: I1ii
   if 'rawpost' in ooO00O00oOO and '$epoctime2$' in ooO00O00oOO [ 'rawpost' ] :
    ooO00O00oOO [ 'rawpost' ] = ooO00O00oOO [ 'rawpost' ] . replace ( '$epoctime2$' , ii1ii ( ) )
    if 79 - 79: IiIIi1I1Iiii - II1 . OOO0O0O0ooooo
    if 62 - 62: I1ii * I1ii . oOOoo % O00ooooo00 . oOOoo * oOOoo
   I11i1 = ''
   if ooO00O00oOO [ 'page' ] and ooO00O00oOO [ 'page' ] in cachedPages and not 'ignorecache' in ooO00O00oOO and forCookieJarOnly == False :
    I11i1 = cachedPages [ ooO00O00oOO [ 'page' ] ]
   else :
    if ooO00O00oOO [ 'page' ] and not ooO00O00oOO [ 'page' ] == '' and ooO00O00oOO [ 'page' ] . startswith ( 'http' ) :
     if '$epoctime$' in ooO00O00oOO [ 'page' ] :
      ooO00O00oOO [ 'page' ] = ooO00O00oOO [ 'page' ] . replace ( '$epoctime$' , ii1IiIi11 ( ) )
     if '$epoctime2$' in ooO00O00oOO [ 'page' ] :
      ooO00O00oOO [ 'page' ] = ooO00O00oOO [ 'page' ] . replace ( '$epoctime2$' , ii1ii ( ) )
      if 81 - 81: oOOOo0o0O / IIii1I + ooO00oo
      if 49 - 49: oOOOo0o0O / II1 / IIiIiII11i
     o0OooooOoOO = ooO00O00oOO [ 'page' ] . split ( '|' )
     i1i1IIIIIIIi = o0OooooOoOO [ 0 ]
     oo0o0oOo = None
     if len ( o0OooooOoOO ) > 1 :
      oo0o0oOo = o0OooooOoOO [ 1 ]
     O00O0O0O0 = urllib2 . Request ( i1i1IIIIIIIi )
     O00O0O0O0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
     if 'refer' in ooO00O00oOO :
      O00O0O0O0 . add_header ( 'Referer' , ooO00O00oOO [ 'refer' ] )
     if 'agent' in ooO00O00oOO :
      O00O0O0O0 . add_header ( 'User-agent' , ooO00O00oOO [ 'agent' ] )
     if 'x-req' in ooO00O00oOO :
      O00O0O0O0 . add_header ( 'X-Requested-With' , ooO00O00oOO [ 'x-req' ] )
     if 'x-forward' in ooO00O00oOO :
      O00O0O0O0 . add_header ( 'X-Forwarded-For' , ooO00O00oOO [ 'x-forward' ] )
     if 'setcookie' in ooO00O00oOO :
      print 'adding cookie' , ooO00O00oOO [ 'setcookie' ]
      O00O0O0O0 . add_header ( 'Cookie' , ooO00O00oOO [ 'setcookie' ] )
     if 'appendcookie' in ooO00O00oOO :
      print 'appending cookie to cookiejar' , ooO00O00oOO [ 'appendcookie' ]
      OO0oOOo0o = ooO00O00oOO [ 'appendcookie' ]
      OO0oOOo0o = OO0oOOo0o . split ( ';' )
      for I1 in OO0oOOo0o :
       IIi1i11111 , III11iiii11i1 = I1 . split ( '=' )
       ooOo0OoO , IIi1i11111 = IIi1i11111 . split ( ':' )
       i1iiIIi1I = cookielib . Cookie ( version = 0 , name = IIi1i11111 , value = III11iiii11i1 , port = None , port_specified = False , domain = ooOo0OoO , domain_specified = False , domain_initial_dot = False , path = '/' , path_specified = True , secure = False , expires = None , discard = True , comment = None , comment_url = None , rest = { 'HttpOnly' : None } , rfc2109 = False )
       cookieJar . set_cookie ( i1iiIIi1I )
       if 36 - 36: IIiIiII11i * IiIIi1I1Iiii
       if 77 - 77: I1ii % O00ooooo00 - oOOoo
       if 93 - 93: Ooo00oOo00o * IiIIi1I1Iiii
       if 73 - 73: o0ooo - IIiIiII11i * O00ooooo00 / i11iIiiIii * oOOOo0o0O % iIiiiI1IiI1I1
     if 'origin' in ooO00O00oOO :
      O00O0O0O0 . add_header ( 'Origin' , ooO00O00oOO [ 'origin' ] )
     if oo0o0oOo :
      oo0o0oOo = oo0o0oOo . split ( '&' )
      for I1 in oo0o0oOo :
       IIi1i11111 , III11iiii11i1 = I1 . split ( '=' )
       O00O0O0O0 . add_header ( IIi1i11111 , III11iiii11i1 )
       if 56 - 56: II1 * IiIIi1I1Iiii . IiIIi1I1Iiii . OOO0O
       if 24 - 24: IiIIi1I1Iiii . OoOoo0 * oOOoo % OOooO / oOOOo0o0O
     if not cookieJar == None :
      if 58 - 58: IIiIiII11i - OOO0O % OOO0O0O0ooooo . IIiIiII11i % Ooo00oOo00o % ooO00oo
      oOo0OooOo = urllib2 . HTTPCookieProcessor ( cookieJar )
      o0iIiiIiiIi = urllib2 . build_opener ( oOo0OooOo , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      o0iIiiIiiIi = urllib2 . install_opener ( o0iIiiIiiIi )
      if 'noredirect' in ooO00O00oOO :
       i1iiIIIi = urllib2 . build_opener ( I1IiiI )
       o0iIiiIiiIi = urllib2 . install_opener ( i1iiIIIi )
       if 62 - 62: OOO0O0O0ooooo / IIiIiII11i % OOO0O0O0ooooo * Ooo00oOo00o % IIiIiII11i
     if 'connection' in ooO00O00oOO :
      print '..........................connection//////.' , ooO00O00oOO [ 'connection' ]
      from keepalive import HTTPHandler
      IiOOoo0oO00oo00 = HTTPHandler ( )
      o0iIiiIiiIi = urllib2 . build_opener ( IiOOoo0oO00oo00 )
      urllib2 . install_opener ( o0iIiiIiiIi )
      if 87 - 87: oOOOo0o0O . I11iii11IIi . O00ooooo00 . O00ooooo00 - o0ooo
      if 26 - 26: IIii1I % i11iIiiIii % OOO0O
     oo0O = None
     if 6 - 6: IiIIi1I1Iiii . ooO00oo / ooO00oo - i11iIiiIii
     if 'post' in ooO00O00oOO :
      OO0oIiII1iiI = ooO00O00oOO [ 'post' ]
      if '$LiveStreamRecaptcha' in OO0oIiII1iiI :
       ( iIIoO0O000oOoo0O , iIIiii11iIiiI ) = O0Oo0 ( ooO00O00oOO [ 'page' ] )
       if iIIoO0O000oOoo0O :
        OO0oIiII1iiI += 'recaptcha_challenge_field:' + iIIoO0O000oOoo0O + ',recaptcha_response_field:' + iIIiii11iIiiI
      o0oO0oo0000OO = OO0oIiII1iiI . split ( ',' ) ;
      oo0O = { }
      for I1i1ii1IiIii in o0oO0oo0000OO :
       IIi1i11111 = I1i1ii1IiIii . split ( ':' ) [ 0 ] ;
       III11iiii11i1 = I1i1ii1IiIii . split ( ':' ) [ 1 ] ;
       oo0O [ IIi1i11111 ] = III11iiii11i1
      oo0O = urllib . urlencode ( oo0O )
      if 69 - 69: I11iii11IIi % I1ii - OoOoo0
     if 'rawpost' in ooO00O00oOO :
      oo0O = ooO00O00oOO [ 'rawpost' ]
      if '$LiveStreamRecaptcha' in oo0O :
       ( iIIoO0O000oOoo0O , iIIiii11iIiiI ) = O0Oo0 ( ooO00O00oOO [ 'page' ] )
       if iIIoO0O000oOoo0O :
        oo0O += '&recaptcha_challenge_field=' + iIIoO0O000oOoo0O + '&recaptcha_response_field=' + iIIiii11iIiiI
        if 38 - 38: IIii1I + i11iIiiIii / i11iIiiIii % Ooo00oOo00o / IiIi11i % oOOoo
        if 7 - 7: ooO00oo * IIiIiII11i + O00ooooo00 + i11iIiiIii + IiIIi1I1Iiii % IIiIiII11i
        if 62 - 62: o0ooo - oOOoo * I11iii11IIi - i11iIiiIii % IiIi11i
        if 52 - 52: OOO0O % I1ii - i11iIiiIii
     if oo0O :
      ooO0O = urllib2 . urlopen ( O00O0O0O0 , oo0O )
     else :
      ooO0O = urllib2 . urlopen ( O00O0O0O0 )
      if 30 - 30: OOooO / Ooo00oOo00o + I1ii
     I11i1 = ooO0O . read ( )
     I11i1 = I1Io00oOOoO0oO ( I11i1 )
     if 26 - 26: oOOoo * IIii1I % Ooo00oOo00o . o0ooo + IiIIi1I1Iiii
     if 'includeheaders' in ooO00O00oOO :
      I11i1 += str ( ooO0O . headers . get ( 'Set-Cookie' ) )
      if 80 - 80: IiIIi1I1Iiii * oOOoo + OOO0O * oOOOo0o0O
     ooO0O . close ( )
     cachedPages [ ooO00O00oOO [ 'page' ] ] = I11i1
     if 16 - 16: OoOoo0 / IIiIiII11i + Ooo00oOo00o % IIii1I - O00ooooo00 . I1ii
     if 26 - 26: o0ooo * ooO00oo . O00ooooo00
     if 59 - 59: OOO0O0O0ooooo + O00ooooo00 - o0ooo
     if forCookieJarOnly :
      return cookieJar
    elif ooO00O00oOO [ 'page' ] and not ooO00O00oOO [ 'page' ] . startswith ( 'http' ) :
     if ooO00O00oOO [ 'page' ] . startswith ( '$pyFunction:' ) :
      OooOo000o0o = iI1I1iII1i ( ooO00O00oOO [ 'page' ] . split ( '$pyFunction:' ) [ 1 ] , '' , cookieJar )
      if forCookieJarOnly :
       return cookieJar
      I11i1 = OooOo000o0o
     else :
      I11i1 = ooO00O00oOO [ 'page' ]
   if '$pyFunction:playmedia(' in ooO00O00oOO [ 'expre' ] or 'ActivateWindow' in ooO00O00oOO [ 'expre' ] or any ( x in url for x in Oo0Ooo ) :
    ii111Ii11iii = False
   if '$doregex' in ooO00O00oOO [ 'expre' ] :
    ooO00O00oOO [ 'expre' ] = oooo00 ( regexs , ooO00O00oOO [ 'expre' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 30 - 30: OOO0O0O0ooooo + OOO0O + iIiiiI1IiI1I1
    if 14 - 14: o0ooo / oOOOo0o0O - IIii1I - I1ii % IiIi11i
   if not ooO00O00oOO [ 'expre' ] == '' :
    print 'doing it ' , ooO00O00oOO [ 'expre' ]
    if '$LiveStreamCaptcha' in ooO00O00oOO [ 'expre' ] :
     OooOo000o0o = I1iIiI1IiIIII ( ooO00O00oOO , I11i1 , cookieJar )
     if 18 - 18: IiIi11i % i11iIiiIii . IIii1I - OOooO
     url = url . replace ( "$doregex[" + ooOOOOo0 + "]" , OooOo000o0o )
    elif ooO00O00oOO [ 'expre' ] . startswith ( '$pyFunction:' ) :
     if 80 - 80: IIiIiII11i + I1ii - O00ooooo00 . oOOoo / o0ooo / IIiIiII11i
     OooOo000o0o = iI1I1iII1i ( ooO00O00oOO [ 'expre' ] . split ( '$pyFunction:' ) [ 1 ] , I11i1 , cookieJar )
     if 'ActivateWindow' in ooO00O00oOO [ 'expre' ] : return
     print 'still hre'
     print 'url k val' , url , ooOOOOo0 , OooOo000o0o
     if 1 - 1: OoOoo0 + i11iIiiIii - IIiIiII11i / oOOOo0o0O + o00ooooO0oO
     url = url . replace ( "$doregex[" + ooOOOOo0 + "]" , OooOo000o0o )
    else :
     if not I11i1 == '' :
      OO0OO0O = re . compile ( ooO00O00oOO [ 'expre' ] ) . search ( I11i1 )
      OooOo000o0o = ''
      try :
       OooOo000o0o = OO0OO0O . group ( 1 ) . strip ( )
      except : traceback . print_exc ( )
     else :
      OooOo000o0o = ooO00O00oOO [ 'expre' ]
     if rawPost :
      print 'rawpost'
      OooOo000o0o = urllib . quote_plus ( OooOo000o0o )
     if 'htmlunescape' in ooO00O00oOO :
      if 75 - 75: OoOoo0 / o0ooo / oOOOo0o0O / ooO00oo % IiIi11i + iIiiiI1IiI1I1
      import HTMLParser
      OooOo000o0o = HTMLParser . HTMLParser ( ) . unescape ( OooOo000o0o )
     url = url . replace ( "$doregex[" + ooOOOOo0 + "]" , OooOo000o0o )
     if 4 - 4: OOooO - IiIIi1I1Iiii - ooO00oo - OoOoo0 % i11iIiiIii / Ooo00oOo00o
   else :
    url = url . replace ( "$doregex[" + ooOOOOo0 + "]" , '' )
 if '$epoctime$' in url :
  url = url . replace ( '$epoctime$' , ii1IiIi11 ( ) )
 if '$epoctime2$' in url :
  url = url . replace ( '$epoctime2$' , ii1ii ( ) )
  if 50 - 50: IiIi11i + O00ooooo00
 if '$GUID$' in url :
  import uuid
  url = url . replace ( '$GUID$' , str ( uuid . uuid1 ( ) ) . upper ( ) )
 if '$get_cookies$' in url :
  url = url . replace ( '$get_cookies$' , i11IiIIi11I ( cookieJar ) )
  if 78 - 78: ooO00oo
 if recursiveCall : return url
 print 'final url' , url
 if url == "" :
  return
 else :
  return url , ii111Ii11iii
  if 83 - 83: IIii1I % I11iii11IIi % o0ooo % o00ooooO0oO . OOO0O % OOO0O0O0ooooo
  if 47 - 47: o0ooo
  if 66 - 66: IIiIiII11i - ooO00oo
def iiIii ( t ) :
 import hashlib
 I1 = hashlib . md5 ( )
 I1 . update ( t )
 return I1 . hexdigest ( )
 if 28 - 28: I1ii
def ooo0oo ( encrypted ) :
 IIiI1i = ""
 for OooOo000o0o in encrypted . split ( ':' ) :
  IIiI1i += chr ( int ( OooOo000o0o . replace ( "0m0" , "" ) ) / 84 / 5 )
 return IIiI1i
 if 6 - 6: OOO0O / OOooO - oOOOo0o0O
def o00O00Oo00O ( media_url ) :
 try :
  import CustomPlayer
  IIii1I1I1I = CustomPlayer . MyXBMCPlayer ( )
  OoOOOo0 = xbmcgui . ListItem ( label = str ( iIi1ii1I1 ) , iconImage = "DefaultVideo.png" , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  IIii1I1I1I . play ( media_url , OoOOOo0 )
  xbmc . sleep ( 1000 )
  while IIii1I1I1I . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 return ''
 if 61 - 61: IIii1I
 if 82 - 82: I1ii / o0ooo % Ooo00oOo00o + o0ooo - IiIi11i
def iI1I1IiIi1I ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  II1i1ii = page_value
  page_value = OOOO0o ( page_value , headers = referer )
  if 82 - 82: I11iii11IIi + OOO0O0O0ooooo - ooO00oo % I1ii * i11iIiiIii
 iIIi1iI1 = "(eval\(function\(p,a,c,k,e,(?:r|d).*)"
 if 31 - 31: IiIi11i + OOO0O0O0ooooo + IiIi11i . IIii1I + IiIIi1I1Iiii / o0ooo
 II11i1IiIII = re . compile ( iIIi1iI1 ) . findall ( page_value )
 II1II1iIIi11 = ""
 if II11i1IiIII and len ( II11i1IiIII ) > 0 :
  for III11iiii11i1 in II11i1IiIII :
   oO00 = Iiii1II1iI ( III11iiii11i1 )
   iIIiIIIIiII = IIIIIo0ooOoO000oO ( oO00 , '\'(.*?)\'' )
   if 'unescape' in oO00 :
    oO00 = urllib . unquote ( iIIiIIIIiII )
   II1II1iIIi11 += oO00 + '\n'
  print 'final value is ' , II1II1iIIi11
  if 85 - 85: Ooo00oOo00o - o0ooo
  II1i1ii = IIIIIo0ooOoO000oO ( II1II1iIIi11 , 'src="(.*?)"' )
  if 37 - 37: OoOoo0 - I11iii11IIi . IIii1I % IiIi11i % oOOoo * I11iii11IIi
  page_value = OOOO0o ( II1i1ii , headers = referer )
  if 8 - 8: I11iii11IIi . IiIi11i % I1ii . IIiIiII11i % IIiIiII11i . oOOoo
  if 47 - 47: OoOoo0 + IiIi11i + iIiiiI1IiI1I1 % i11iIiiIii
  if 93 - 93: OOO0O % I11iii11IIi . OOO0O0O0ooooo / OOooO * I1ii
 i1iii1ii = IIIIIo0ooOoO000oO ( page_value , 'streamer\'.*?\'(.*?)\'\)' )
 II1I11Iii1 = IIIIIo0ooOoO000oO ( page_value , 'file\',\s\'(.*?)\'' )
 if 16 - 16: oOOoo * Ooo00oOo00o / I1ii
 if 22 - 22: I1ii + IIii1I % IiIIi1I1Iiii / OoOoo0 / oOOoo
 return i1iii1ii + ' playpath=' + II1I11Iii1 + ' pageUrl=' + II1i1ii
 if 54 - 54: I11iii11IIi % ooO00oo . i11iIiiIii
def o00o0O0O00 ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  page_value = OOOO0o ( page_value , headers = referer )
 iIIi1iI1 = "var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
 II11i1IiIII = re . compile ( iIIi1iI1 ) . findall ( page_value ) [ 0 ]
 if 34 - 34: oOOOo0o0O . IiIIi1I1Iiii
 i1I1ii11i1Iii , I1IiiiiI , iiiI1I1iIIIi1 , OOoO0oO00o , iiiiii1 , III11iiii11i1 = ( II11i1IiIII )
 iiiiii1 = int ( iiiiii1 )
 i1I1ii11i1Iii = int ( i1I1ii11i1Iii ) / iiiiii1
 I1IiiiiI = int ( I1IiiiiI ) / iiiiii1
 iiiI1I1iIIIi1 = int ( iiiI1I1iIIIi1 ) / iiiiii1
 OOoO0oO00o = int ( OOoO0oO00o ) / iiiiii1
 if 66 - 66: I1ii * IIii1I % IIii1I * ooO00oo - IiIi11i - ooO00oo
 o0O0oO0 = 'rtmp://' + str ( i1I1ii11i1Iii ) + '.' + str ( I1IiiiiI ) + '.' + str ( iiiI1I1iIIIi1 ) + '.' + str ( OOoO0oO00o ) + III11iiii11i1 ;
 return o0O0oO0
 if 77 - 77: OOO0O0O0ooooo . oOOoo
def i1i1IiIi1 ( url , useragent = None ) :
 str = '#EXTM3U'
 str += '\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=361816'
 str += '\n' + url + '&bytes=0-200000'
 iiIIIII1i1iI = os . path . join ( iIiiiI , 'testfile.m3u' )
 str += '\n'
 I1iiIiI1iI1I ( iiIIIII1i1iI , str )
 if 27 - 27: OOO0O * o00ooooO0oO - Ooo00oOo00o + oOOoo * oOOoo
 return iiIIIII1i1iI
 if 55 - 55: IiIi11i
def I1iiIiI1iI1I ( file_name , page_data , append = False ) :
 if append :
  iiiiii1 = open ( file_name , 'a' )
  iiiiii1 . write ( page_data )
  iiiiii1 . close ( )
 else :
  iiiiii1 = open ( file_name , 'wb' )
  iiiiii1 . write ( page_data )
  iiiiii1 . close ( )
  return ''
  if 82 - 82: o00ooooO0oO - oOOOo0o0O + Ooo00oOo00o
def OO0 ( file_name ) :
 iiiiii1 = open ( file_name , 'rb' )
 OOoO0oO00o = iiiiii1 . read ( )
 iiiiii1 . close ( )
 return OOoO0oO00o
 if 9 - 9: I1ii % i11iIiiIii / IiIIi1I1Iiii
def IIIiI1ii1IIi ( page_data ) :
 import re , base64 , urllib ;
 o0O0oo0o = page_data
 while 'geh(' in o0O0oo0o :
  if o0O0oo0o . startswith ( 'lol(' ) : o0O0oo0o = o0O0oo0o [ 5 : - 1 ]
  if 12 - 12: I11iii11IIi % ooO00oo % OOO0O . i11iIiiIii * IIii1I
  o0O0oo0o = re . compile ( '"(.*?)"' ) . findall ( o0O0oo0o ) [ 0 ] ;
  o0O0oo0o = base64 . b64decode ( o0O0oo0o ) ;
  o0O0oo0o = urllib . unquote ( o0O0oo0o ) ;
 print o0O0oo0o
 return o0O0oo0o
 if 66 - 66: i11iIiiIii * IIii1I % II1
def iIiI1iI1i1I ( page_data ) :
 print 'get_dag_url2' , page_data
 Oo0Oo000OO = OOOO0o ( page_data ) ;
 i1II1i = '(http.*)'
 import uuid
 I1iIiiiI1 = str ( uuid . uuid1 ( ) ) . upper ( )
 o00OO00OoO = re . compile ( i1II1i ) . findall ( Oo0Oo000OO )
 I1iIII1IiiI = [ ( 'X-Playback-Session-Id' , I1iIiiiI1 ) ]
 for OOoooOoO0Oo in o00OO00OoO :
  try :
   Oo000 = OOOO0o ( OOoooOoO0Oo , headers = I1iIII1IiiI ) ;
   if 48 - 48: i11iIiiIii % I1ii
  except : pass
  if 29 - 29: OOooO + i11iIiiIii % OoOoo0
 return page_data + '|&X-Playback-Session-Id=' + I1iIiiiI1
 if 93 - 93: I11iii11IIi % IIii1I
 if 90 - 90: IIiIiII11i - oOOOo0o0O / oOOoo / OOO0O0O0ooooo / OoOoo0
def oOO0 ( page_data ) :
 print 'get_dag_url' , page_data
 if page_data . startswith ( 'http://dag.total-stream.net' ) :
  I1iIII1IiiI = [ ( 'User-Agent' , 'Verismo-BlackUI_(2.4.7.5.8.0.34)' ) ]
  page_data = OOOO0o ( page_data , headers = I1iIII1IiiI ) ;
  if 15 - 15: IiIIi1I1Iiii + OoOoo0 . IiIi11i - IIii1I / OOO0O0O0ooooo % IIii1I
 if '127.0.0.1' in page_data :
  return oO0O ( page_data )
 elif IIIIIo0ooOoO000oO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  Oo00o0O0O = IIIIIo0ooOoO000oO ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + IIIIIo0ooOoO000oO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + IIIIIo0ooOoO000oO ( page_data , '\\?y=([^&]+)&' )
 else :
  Oo00o0O0O = IIIIIo0ooOoO000oO ( page_data , 'href="([^"]+)"[^"]+$' )
  if len ( Oo00o0O0O ) == 0 :
   Oo00o0O0O = page_data
 Oo00o0O0O = Oo00o0O0O . replace ( ' ' , '%20' )
 return Oo00o0O0O
 if 84 - 84: OoOoo0 % O00ooooo00
def IIIIIo0ooOoO000oO ( data , re_patten ) :
 O00o0OO = ''
 ooO00O00oOO = re . search ( re_patten , data )
 if ooO00O00oOO != None :
  O00o0OO = ooO00O00oOO . group ( 1 )
 else :
  O00o0OO = ''
 return O00o0OO
 if 33 - 33: OOO0O * OOO0O . IiIi11i . i11iIiiIii
def oO0O ( page_data ) :
 Oo00o0O0O = ''
 if '127.0.0.1' in page_data :
  Oo00o0O0O = IIIIIo0ooOoO000oO ( page_data , '&ver_t=([^&]+)&' ) + ' live=true timeout=15 playpath=' + IIIIIo0ooOoO000oO ( page_data , '\\?y=([a-zA-Z0-9-_\\.@]+)' )
  if 48 - 48: o0ooo . oOOoo + I11iii11IIi % OOO0O / i11iIiiIii
 if IIIIIo0ooOoO000oO ( page_data , 'token=([^&]+)&' ) != '' :
  Oo00o0O0O = Oo00o0O0O + '?token=' + IIIIIo0ooOoO000oO ( page_data , 'token=([^&]+)&' )
 elif IIIIIo0ooOoO000oO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  Oo00o0O0O = IIIIIo0ooOoO000oO ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + IIIIIo0ooOoO000oO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + IIIIIo0ooOoO000oO ( page_data , '\\?y=([^&]+)&' )
 else :
  Oo00o0O0O = IIIIIo0ooOoO000oO ( page_data , 'HREF="([^"]+)"' )
  if 74 - 74: iIiiiI1IiI1I1 . OOO0O0O0ooooo - IIiIiII11i + ooO00oo % i11iIiiIii % I11iii11IIi
 if 'dag1.asx' in Oo00o0O0O :
  return oOO0 ( Oo00o0O0O )
  if 78 - 78: oOOoo + I11iii11IIi + ooO00oo - ooO00oo . i11iIiiIii / Ooo00oOo00o
 if 'devinlivefs.fplive.net' not in Oo00o0O0O :
  Oo00o0O0O = Oo00o0O0O . replace ( 'devinlive' , 'flive' )
 if 'permlivefs.fplive.net' not in Oo00o0O0O :
  Oo00o0O0O = Oo00o0O0O . replace ( 'permlive' , 'flive' )
 return Oo00o0O0O
 if 27 - 27: oOOoo - OOO0O0O0ooooo % OoOoo0 * o00ooooO0oO . ooO00oo % IIii1I
 if 37 - 37: II1 + OOO0O0O0ooooo - O00ooooo00 % IiIi11i
def i1I1i1i ( str_eval ) :
 iiiIIIi11I = ""
 try :
  I111i1Ii1i1 = "w,i,s,e=(" + str_eval + ')'
  exec ( I111i1Ii1i1 )
  iiiIIIi11I = iI1IIi1IiI ( w , i , s , e )
 except : traceback . print_exc ( file = sys . stdout )
 if 45 - 45: OOO0O0O0ooooo / O00ooooo00 * I1ii * Ooo00oOo00o
 return iiiIIIi11I
 if 35 - 35: OOO0O / OOooO % IIiIiII11i + IIii1I
def iI1IIi1IiI ( w , i , s , e ) :
 oO00o = 0 ;
 i11I1IiiiiiiiIi = 0 ;
 iIii1I = 0 ;
 iii11i1 = [ ] ;
 i1IiI1I111iIi = [ ] ;
 while True :
  if ( oO00o < 5 ) :
   i1IiI1I111iIi . append ( w [ oO00o ] )
  elif ( oO00o < len ( w ) ) :
   iii11i1 . append ( w [ oO00o ] ) ;
  oO00o += 1 ;
  if ( i11I1IiiiiiiiIi < 5 ) :
   i1IiI1I111iIi . append ( i [ i11I1IiiiiiiiIi ] )
  elif ( i11I1IiiiiiiiIi < len ( i ) ) :
   iii11i1 . append ( i [ i11I1IiiiiiiiIi ] )
  i11I1IiiiiiiiIi += 1 ;
  if ( iIii1I < 5 ) :
   i1IiI1I111iIi . append ( s [ iIii1I ] )
  elif ( iIii1I < len ( s ) ) :
   iii11i1 . append ( s [ iIii1I ] ) ;
  iIii1I += 1 ;
  if ( len ( w ) + len ( i ) + len ( s ) + len ( e ) == len ( iii11i1 ) + len ( i1IiI1I111iIi ) + len ( e ) ) :
   break ;
   if 41 - 41: OOO0O0O0ooooo + I1ii . O00ooooo00 - iIiiiI1IiI1I1 * o0ooo . Ooo00oOo00o
 oooO00Oo = '' . join ( iii11i1 )
 ooO00o = '' . join ( i1IiI1I111iIi )
 i11I1IiiiiiiiIi = 0 ;
 o0o00O0oOooO0 = [ ] ;
 for oO00o in range ( 0 , len ( iii11i1 ) , 2 ) :
  if 99 - 99: IiIi11i
  o0OO00 = - 1 ;
  if ( ord ( ooO00o [ i11I1IiiiiiiiIi ] ) % 2 ) :
   o0OO00 = 1 ;
   if 14 - 14: OOO0O + i11iIiiIii
  o0o00O0oOooO0 . append ( chr ( int ( oooO00Oo [ oO00o : oO00o + 2 ] , 36 ) - o0OO00 ) ) ;
  i11I1IiiiiiiiIi += 1 ;
  if ( i11I1IiiiiiiiIi >= len ( i1IiI1I111iIi ) ) :
   i11I1IiiiiiiiIi = 0 ;
 o0O0oO0 = '' . join ( o0o00O0oOooO0 )
 if 'eval(function(w,i,s,e)' in o0O0oO0 :
  print 'STILL GOing'
  o0O0oO0 = re . compile ( 'eval\(function\(w,i,s,e\).*}\((.*?)\)' ) . findall ( o0O0oO0 ) [ 0 ]
  return i1I1i1i ( o0O0oO0 )
 else :
  print 'FINISHED'
  return o0O0oO0
  if 83 - 83: OOO0O / i11iIiiIii + iIiiiI1IiI1I1 . OOooO * oOOOo0o0O + ooO00oo
def Iiii1II1iI ( page_value , regex_for_text = '' , iterations = 1 , total_iteration = 1 ) :
 try :
  iiii1i1II1 = None
  if page_value . startswith ( "http" ) :
   page_value = OOOO0o ( page_value )
  print 'page_value' , page_value
  if regex_for_text and len ( regex_for_text ) > 0 :
   page_value = re . compile ( regex_for_text ) . findall ( page_value ) [ 0 ]
   if 63 - 63: IIii1I % OOO0O - OOooO
  page_value = i1iii ( page_value , iterations , total_iteration )
 except : traceback . print_exc ( file = sys . stdout )
 print 'unpacked' , page_value
 if 'sav1live.tv' in page_value :
  page_value = page_value . replace ( 'sav1live.tv' , 'sawlive.tv' )
  print 'sav1 unpacked' , page_value
 return page_value
 if 42 - 42: iIiiiI1IiI1I1 + o00ooooO0oO - oOOoo - OOO0O0O0ooooo / o0ooo % ooO00oo
def i1iii ( sJavascript , iteration = 1 , totaliterations = 2 ) :
 print 'iteration' , iteration
 if sJavascript . startswith ( 'var _0xcb8a=' ) :
  O00oOoOOO0ooo = sJavascript . split ( 'var _0xcb8a=' )
  I111i1Ii1i1 = "myarray=" + O00oOoOOO0ooo [ 1 ] . split ( "eval(" ) [ 0 ]
  exec ( I111i1Ii1i1 )
  I1III1iIi = 62
  OoO00O0 = int ( O00oOoOOO0ooo [ 1 ] . split ( ",62," ) [ 1 ] . split ( ',' ) [ 0 ] )
  I1Iii = myarray [ 0 ]
  i1i11ii1Ii = myarray [ 3 ]
  with open ( 'temp file' + str ( iteration ) + '.js' , "wb" ) as i1Oo0oOo000OoO0 :
   i1Oo0oOo000OoO0 . write ( str ( i1i11ii1Ii ) )
   if 25 - 25: OOO0O . O00ooooo00 . iIiiiI1IiI1I1 / o00ooooO0oO
 else :
  if 54 - 54: O00ooooo00 . OoOoo0 - OOO0O + IiIi11i + IiIIi1I1Iiii / IiIIi1I1Iiii
  O00oOoOOO0ooo = sJavascript . split ( "rn p}('" )
  print O00oOoOOO0ooo
  if 22 - 22: IiIi11i . IIii1I
  I1Iii , I1III1iIi , OoO00O0 , i1i11ii1Ii = ( '' , '0' , '0' , '' )
  if 12 - 12: oOOoo
  I111i1Ii1i1 = "p1,a1,c1,k1=('" + O00oOoOOO0ooo [ 1 ] . split ( ".spli" ) [ 0 ] + ')'
  exec ( I111i1Ii1i1 )
 i1i11ii1Ii = i1i11ii1Ii . split ( '|' )
 O00oOoOOO0ooo = O00oOoOOO0ooo [ 1 ] . split ( "))'" )
 if 71 - 71: IIiIiII11i . iIiiiI1IiI1I1 . IIiIiII11i - IiIi11i
 if 45 - 45: ooO00oo / OOO0O0O0ooooo / I11iii11IIi * oOOOo0o0O
 if 18 - 18: IIii1I + oOOOo0o0O + IIii1I . OOO0O + o00ooooO0oO . IiIi11i
 if 7 - 7: OOO0O + IIii1I * OoOoo0 * OoOoo0 / iIiiiI1IiI1I1 - oOOoo
 if 65 - 65: I1ii + I11iii11IIi + iIiiiI1IiI1I1
 if 77 - 77: iIiiiI1IiI1I1
 if 50 - 50: OOO0O0O0ooooo . OOO0O0O0ooooo . IiIi11i % IiIIi1I1Iiii
 if 68 - 68: I1ii
 if 10 - 10: oOOoo
 if 77 - 77: oOOOo0o0O / iIiiiI1IiI1I1 + ooO00oo + IiIi11i - i11iIiiIii
 if 44 - 44: IIiIiII11i + I11iii11IIi + OOO0O . IIiIiII11i * I11iii11IIi % IIii1I
 if 72 - 72: oOOOo0o0O . oOOOo0o0O - OOO0O
 if 48 - 48: IiIIi1I1Iiii - IiIi11i + IiIIi1I1Iiii - IIiIiII11i * i11iIiiIii . OOooO
 if 35 - 35: ooO00oo . OOO0O0O0ooooo + IiIIi1I1Iiii + oOOOo0o0O + O00ooooo00
 if 65 - 65: OOO0O0O0ooooo * IIiIiII11i / IIiIiII11i . I11iii11IIi
 if 87 - 87: iIiiiI1IiI1I1 * OOO0O % IiIIi1I1Iiii * IiIIi1I1Iiii
 if 58 - 58: oOOOo0o0O . o0ooo + IIiIiII11i % IiIIi1I1Iiii - Ooo00oOo00o
 if 50 - 50: OOooO % iIiiiI1IiI1I1 - IiIi11i . O00ooooo00 + OOO0O0O0ooooo % OOooO
 if 10 - 10: OOooO . O00ooooo00 + oOOoo
 if 66 - 66: Ooo00oOo00o % o0ooo
 if 21 - 21: I11iii11IIi - II1 % i11iIiiIii
 if 71 - 71: O00ooooo00 - OoOoo0 * o00ooooO0oO + I1ii - Ooo00oOo00o % OOO0O
 iii11iII = ''
 OOoO0oO00o = ''
 if 63 - 63: IIii1I + oOOOo0o0O . Ooo00oOo00o / IIiIiII11i
 if 84 - 84: O00ooooo00
 IiIIiii1I = str ( ooooo0Oo0 ( I1Iii , I1III1iIi , OoO00O0 , i1i11ii1Ii , iii11iII , OOoO0oO00o , iteration ) )
 if 97 - 97: ooO00oo . I1ii . ooO00oo
 if 91 - 91: oOOOo0o0O + o00ooooO0oO . OoOoo0
 if 15 - 15: OoOoo0
 if 94 - 94: o00ooooO0oO % iIiiiI1IiI1I1 * O00ooooo00 * IIii1I
 if 81 - 81: IiIIi1I1Iiii - OoOoo0
 if iteration >= totaliterations :
  if 24 - 24: II1 . Ooo00oOo00o * iIiiiI1IiI1I1
  return IiIIiii1I
 else :
  if 59 - 59: o00ooooO0oO + Ooo00oOo00o / oOOOo0o0O
  return i1iii ( IiIIiii1I , iteration + 1 )
  if 97 - 97: IiIIi1I1Iiii * OOooO % IiIi11i . OOooO - o00ooooO0oO - oOOOo0o0O
def ooooo0Oo0 ( p , a , c , k , e , d , iteration , v = 1 ) :
 if 79 - 79: IIiIiII11i - IiIi11i
 if 37 - 37: ooO00oo . IiIIi1I1Iiii * IiIIi1I1Iiii * iIiiiI1IiI1I1 * OOO0O0O0ooooo
 if 83 - 83: ooO00oo / o00ooooO0oO
 while ( c >= 1 ) :
  c = c - 1
  if ( k [ c ] ) :
   OOo000OO000 = str ( OOOO00OooO ( c , a ) )
   if v == 1 :
    p = re . sub ( '\\b' + OOo000OO000 + '\\b' , k [ c ] , p )
   else :
    p = OOOiI1 ( p , OOo000OO000 , k [ c ] )
    if 84 - 84: oOOOo0o0O * IIiIiII11i % OoOoo0 + oOOOo0o0O / OOooO
    if 80 - 80: II1 + ooO00oo
    if 95 - 95: o00ooooO0oO / I1ii * o00ooooO0oO - II1 * II1 % Ooo00oOo00o
    if 43 - 43: IiIIi1I1Iiii . o00ooooO0oO
    if 12 - 12: o00ooooO0oO + oOOOo0o0O + OoOoo0 . ooO00oo / oOOoo
    if 29 - 29: ooO00oo . IiIi11i - iIiiiI1IiI1I1
 return p
 if 68 - 68: IIii1I + iIiiiI1IiI1I1 / I1ii
 if 91 - 91: I11iii11IIi % IIii1I . IIiIiII11i
 if 70 - 70: OoOoo0 % iIiiiI1IiI1I1 % OOO0O0O0ooooo . O00ooooo00 / o00ooooO0oO
def OOOiI1 ( source_str , word_to_find , replace_with ) :
 OO0ooOoOO0OOo = None
 OO0ooOoOO0OOo = source_str . split ( word_to_find )
 if len ( OO0ooOoOO0OOo ) > 1 :
  OooOoooo0000 = [ ]
  I1ii1i11i = 0
  for Oooooo0O00o in OO0ooOoOO0OOo :
   if 36 - 36: I11iii11IIi + ooO00oo * OOO0O0O0ooooo . II1 * II1
   OooOoooo0000 . append ( Oooooo0O00o )
   OooOo000o0o = word_to_find
   if 51 - 51: OOO0O * OOO0O
   if 98 - 98: Ooo00oOo00o - oOOoo . ooO00oo % i11iIiiIii
   if I1ii1i11i == len ( OO0ooOoOO0OOo ) - 1 :
    OooOo000o0o = ''
   else :
    if len ( Oooooo0O00o ) == 0 :
     if ( len ( OO0ooOoOO0OOo [ I1ii1i11i + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( OO0ooOoOO0OOo [ I1ii1i11i + 1 ] ) > 0 and OO0ooOoOO0OOo [ I1ii1i11i + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) :
      OooOo000o0o = replace_with
      if 69 - 69: OOO0O + OOooO * OOO0O0O0ooooo . oOOOo0o0O % I11iii11IIi
    else :
     if ( OO0ooOoOO0OOo [ I1ii1i11i ] [ - 1 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) and ( ( len ( OO0ooOoOO0OOo [ I1ii1i11i + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( OO0ooOoOO0OOo [ I1ii1i11i + 1 ] ) > 0 and OO0ooOoOO0OOo [ I1ii1i11i + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) ) :
      OooOo000o0o = replace_with
      if 96 - 96: IiIi11i . IiIi11i - OoOoo0 / OoOoo0
   OooOoooo0000 . append ( OooOo000o0o )
   I1ii1i11i += 1
   if 96 - 96: i11iIiiIii / IIiIiII11i - OOO0O0O0ooooo . IiIi11i
  source_str = '' . join ( OooOoooo0000 )
 return source_str
 if 39 - 39: IiIi11i / OOO0O0O0ooooo * ooO00oo
def I1IiII1iI1 ( num , radix ) :
 if 52 - 52: I11iii11IIi * Ooo00oOo00o - oOOoo
 iIiIi11Ii = ""
 if num == 0 : return '0'
 while num > 0 :
  iIiIi11Ii = "0123456789abcdefghijklmnopqrstuvwxyz" [ num % radix ] + iIiIi11Ii
  num /= radix
 return iIiIi11Ii
 if 82 - 82: Ooo00oOo00o + IIiIiII11i . O00ooooo00 + oOOOo0o0O
def OOOO00OooO ( cc , a ) :
 OOo000OO000 = "" if cc < a else OOOO00OooO ( int ( cc / a ) , a )
 cc = ( cc % a )
 iIiI1Iii1 = chr ( cc + 29 ) if cc > 35 else str ( I1IiII1iI1 ( cc , 36 ) )
 return OOo000OO000 + iIiI1Iii1
 if 85 - 85: i11iIiiIii / i11iIiiIii . Ooo00oOo00o . OOO0O0O0ooooo
 if 67 - 67: iIiiiI1IiI1I1 / o0ooo . oOOOo0o0O . II1
def i11IiIIi11I ( cookieJar ) :
 try :
  i1I1Ii11i = ""
  for i11IIIiI11 , I1iIiiiI1OOO0O00Oo in enumerate ( cookieJar ) :
   i1I1Ii11i += I1iIiiiI1OOO0O00Oo . name + "=" + I1iIiiiI1OOO0O00Oo . value + ";"
 except : pass
 if 13 - 13: IIii1I
 return i1I1Ii11i
 if 2 - 2: O00ooooo00 * I1ii - I1ii + II1 % I11iii11IIi / I11iii11IIi
 if 3 - 3: II1
def OO0Oo ( cookieJar , COOKIEFILE ) :
 try :
  iiiII = os . path . join ( iIiiiI , COOKIEFILE )
  cookieJar . save ( iiiII , ignore_discard = True )
 except : pass
 if 71 - 71: ooO00oo + O00ooooo00 - OOooO - i11iIiiIii . OoOoo0 - IiIi11i
def i1iiiIi1i ( COOKIEFILE ) :
 if 85 - 85: OOO0O - I11iii11IIi / OOO0O + oOOOo0o0O - OOooO
 IIii1III = None
 if COOKIEFILE :
  try :
   iiiII = os . path . join ( iIiiiI , COOKIEFILE )
   IIii1III = cookielib . LWPCookieJar ( )
   IIii1III . load ( iiiII , ignore_discard = True )
  except :
   IIii1III = None
   if 94 - 94: i11iIiiIii % II1 / IIiIiII11i
 if not IIii1III :
  IIii1III = cookielib . LWPCookieJar ( )
  if 24 - 24: IIiIiII11i * I1ii
 return IIii1III
 if 85 - 85: iIiiiI1IiI1I1 . IiIi11i % oOOOo0o0O % OoOoo0
def iI1I1iII1i ( fun_call , page_data , Cookie_Jar ) :
 OOo00ooOoO0o = ''
 if o0oO0 not in sys . path :
  sys . path . append ( o0oO0 )
  if 21 - 21: i11iIiiIii
 print fun_call
 try :
  o00iIiiiII = 'import ' + fun_call . split ( '.' ) [ 0 ]
  print o00iIiiiII , sys . path
  exec ( o00iIiiiII )
  print 'done'
 except :
  print 'error in import'
  traceback . print_exc ( file = sys . stdout )
 print 'ret_val=' + fun_call
 exec ( 'ret_val=' + fun_call )
 print OOo00ooOoO0o
 if 5 - 5: II1 / o0ooo % OoOoo0 % Ooo00oOo00o * OOooO + IIii1I
 return str ( OOo00ooOoO0o )
 if 11 - 11: o00ooooO0oO % i11iIiiIii % I1ii . ooO00oo
def O0Oo0 ( url ) :
 oOO0o = OOOO0o ( url )
 o0OI1II = ""
 iIIi1Ii1III = ""
 Oooo00 = "<script.*?src=\"(.*?recap.*?)\""
 O00o0OO = re . findall ( Oooo00 , oOO0o )
 iii1II1iI1IIi = False
 Ii11iiI1 = None
 iIIi1Ii1III = None
 if 71 - 71: o0ooo / oOOOo0o0O % oOOOo0o0O
 if O00o0OO and len ( O00o0OO ) > 0 :
  OoooO0 = O00o0OO [ 0 ]
  iii1II1iI1IIi = True
  if 75 - 75: IiIi11i
  iI1ii1Ii = 'challenge.*?\'(.*?)\''
  OooOOOoOoo0O0 = '\'(.*?)\''
  O0OOOOo0 = OOOO0o ( OoooO0 )
  o0OI1II = re . findall ( iI1ii1Ii , O0OOOOo0 ) [ 0 ]
  OOooO0Oo00 = 'http://www.google.com/recaptcha/api/reload?c=' ;
  iIIIIIIIiIII = OoooO0 . split ( 'k=' ) [ 1 ]
  OOooO0Oo00 += o0OI1II + '&k=' + iIIIIIIIiIII + '&captcha_k=1&type=image&lang=en-GB'
  o0oo0o00ooO00 = OOOO0o ( OOooO0Oo00 )
  Ii11iiI1 = re . findall ( OooOOOoOoo0O0 , o0oo0o00ooO00 ) [ 0 ]
  IIiIiiI1i = 'http://www.google.com/recaptcha/api/image?c=' + Ii11iiI1
  if not IIiIiiI1i . startswith ( "http" ) :
   IIiIiiI1i = 'http://www.google.com/recaptcha/api/' + IIiIiiI1i
  import random
  IIi1i11111 = random . randrange ( 100 , 1000 , 5 )
  IIi = os . path . join ( iIiiiI , str ( IIi1i11111 ) + "captcha.img" )
  O0Oo = open ( IIi , "wb" )
  O0Oo . write ( OOOO0o ( IIiIiiI1i ) )
  O0Oo . close ( )
  III11I1 = OOOO0o0O ( captcha = IIi )
  iIIi1Ii1III = III11I1 . get ( )
  os . remove ( IIi )
 return Ii11iiI1 , iIIi1Ii1III
 if 41 - 41: o0ooo + IiIi11i
def OOOO0o ( url , cookieJar = None , post = None , timeout = 20 , headers = None ) :
 if 90 - 90: ooO00oo - OOO0O % OoOoo0 % IIii1I - OOO0O
 if 20 - 20: OOO0O0O0ooooo - II1 - ooO00oo + IIii1I
 oOo0OooOo = urllib2 . HTTPCookieProcessor ( cookieJar )
 o0iIiiIiiIi = urllib2 . build_opener ( oOo0OooOo , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 if 94 - 94: oOOoo . O00ooooo00
 O00O0O0O0 = urllib2 . Request ( url )
 O00O0O0O0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36' )
 if headers :
  for I1 , O0OOo0o in headers :
   O00O0O0O0 . add_header ( I1 , O0OOo0o )
   if 44 - 44: IIiIiII11i * IIii1I / OOO0O0O0ooooo
 ooO0O = o0iIiiIiiIi . open ( O00O0O0O0 , post , timeout = timeout )
 I11i1 = ooO0O . read ( )
 ooO0O . close ( )
 return I11i1 ;
 if 17 - 17: iIiiiI1IiI1I1
def iiIiii ( str , reg = None ) :
 if reg :
  str = re . findall ( reg , str ) [ 0 ]
 iiI1ii = urllib . unquote ( str [ 0 : len ( str ) - 1 ] ) ;
 O0OooOO = '' ;
 for iII1i11IIi1i in range ( len ( iiI1ii ) ) :
  O0OooOO += chr ( ord ( iiI1ii [ iII1i11IIi1i ] ) - iiI1ii [ len ( iiI1ii ) - 1 ] ) ;
 O0OooOO = urllib . unquote ( O0OooOO )
 print O0OooOO
 return O0OooOO
 if 49 - 49: ooO00oo / IiIi11i / oOOOo0o0O
def I1Io00oOOoO0oO ( str ) :
 IiIiIi1I11I = re . findall ( 'unescape\(\'(.*?)\'' , str )
 print 'js' , IiIiIi1I11I
 if ( not IiIiIi1I11I == None ) and len ( IiIiIi1I11I ) > 0 :
  for IiI1i1i in IiIiIi1I11I :
   if 94 - 94: OOooO - IiIIi1I1Iiii + I1ii
   str = str . replace ( IiI1i1i , urllib . unquote ( IiI1i1i ) )
 return str
 if 59 - 59: OoOoo0 . IIiIiII11i - IIii1I + IIii1I
oO0o0Oo = 0
def I1iIiI1IiIIII ( m , html_page , cookieJar ) :
 global oO0o0Oo
 oO0o0Oo += 1
 o0OO = m [ 'expre' ]
 II1i1ii = m [ 'page' ]
 oOoO00O000 = re . compile ( '\$LiveStreamCaptcha\[([^\]]*)\]' ) . findall ( o0OO ) [ 0 ]
 if 54 - 54: OOO0O0O0ooooo - OOooO . oOOOo0o0O % OOooO + OOooO
 OoooO0 = re . compile ( oOoO00O000 ) . findall ( html_page ) [ 0 ]
 print o0OO , oOoO00O000 , OoooO0
 if not OoooO0 . startswith ( "http" ) :
  i1iI1Iiii1I = 'http://' + "" . join ( II1i1ii . split ( '/' ) [ 2 : 3 ] )
  if OoooO0 . startswith ( "/" ) :
   OoooO0 = i1iI1Iiii1I + OoooO0
  else :
   OoooO0 = i1iI1Iiii1I + '/' + OoooO0
   if 9 - 9: OoOoo0 / I11iii11IIi / iIiiiI1IiI1I1 + o00ooooO0oO
 IIi = os . path . join ( iIiiiI , str ( oO0o0Oo ) + "captcha.jpg" )
 O0Oo = open ( IIi , "wb" )
 print ' c capurl' , OoooO0
 O00O0O0O0 = urllib2 . Request ( OoooO0 )
 O00O0O0O0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'refer' in m :
  O00O0O0O0 . add_header ( 'Referer' , m [ 'refer' ] )
 if 'agent' in m :
  O00O0O0O0 . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'setcookie' in m :
  print 'adding cookie' , m [ 'setcookie' ]
  O00O0O0O0 . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 71 - 71: OOooO / IiIIi1I1Iiii
  if 87 - 87: OOO0O + OOO0O - OOO0O % OOO0O0O0ooooo
  if 13 - 13: iIiiiI1IiI1I1
  if 57 - 57: oOOoo - II1
 urllib2 . urlopen ( O00O0O0O0 )
 ooO0O = urllib2 . urlopen ( O00O0O0O0 )
 if 68 - 68: o0ooo % OOO0O / o00ooooO0oO + o00ooooO0oO - o00ooooO0oO . Ooo00oOo00o
 O0Oo . write ( ooO0O . read ( ) )
 ooO0O . close ( )
 O0Oo . close ( )
 III11I1 = OOOO0o0O ( captcha = IIi )
 iIIi1Ii1III = III11I1 . get ( )
 return iIIi1Ii1III
 if 100 - 100: I11iii11IIi % IiIIi1I1Iiii
class OOOO0o0O ( xbmcgui . WindowDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . cptloc = kwargs . get ( 'captcha' )
  self . img = xbmcgui . ControlImage ( 335 , 30 , 624 , 60 , self . cptloc )
  self . addControl ( self . img )
  self . kbd = xbmc . Keyboard ( )
  if 76 - 76: iIiiiI1IiI1I1 / Ooo00oOo00o + II1 . OOO0O . OoOoo0 . IiIi11i
 def get ( self ) :
  self . show ( )
  time . sleep ( 2 )
  self . kbd . doModal ( )
  if ( self . kbd . isConfirmed ( ) ) :
   iiiI = self . kbd . getText ( )
   self . close ( )
   return iiiI
  self . close ( )
  return False
  if 10 - 10: OOO0O % IIiIiII11i - iIiiiI1IiI1I1
def ii1IiIi11 ( ) :
 import time
 return str ( int ( time . time ( ) * 1000 ) )
 if 11 - 11: OOO0O0O0ooooo + IIiIiII11i
def ii1ii ( ) :
 import time
 return str ( int ( time . time ( ) ) )
 if 80 - 80: I1ii % I1ii % OOO0O0O0ooooo - i11iIiiIii . OOooO / OOO0O0O0ooooo
def IiIi1Ii ( ) :
 iiIIiI11II1 = [ ]
 oooOo = sys . argv [ 2 ]
 if len ( oooOo ) >= 2 :
  oOoO0Oo0 = sys . argv [ 2 ]
  i11i11i = oOoO0Oo0 . replace ( '?' , '' )
  if ( oOoO0Oo0 [ len ( oOoO0Oo0 ) - 1 ] == '/' ) :
   oOoO0Oo0 = oOoO0Oo0 [ 0 : len ( oOoO0Oo0 ) - 2 ]
  iiI1iI = i11i11i . split ( '&' )
  iiIIiI11II1 = { }
  for iII1i11IIi1i in range ( len ( iiI1iI ) ) :
   Ooo00O0 = { }
   Ooo00O0 = iiI1iI [ iII1i11IIi1i ] . split ( '=' )
   if ( len ( Ooo00O0 ) ) == 2 :
    iiIIiI11II1 [ Ooo00O0 [ 0 ] ] = Ooo00O0 [ 1 ]
 return iiIIiI11II1
 if 70 - 70: IIiIiII11i - IiIi11i - Ooo00oOo00o - I11iii11IIi . i11iIiiIii % O00ooooo00
 if 1 - 1: I1ii / O00ooooo00
def O0oo0 ( ) :
 OOo00OoO = json . loads ( open ( iI111iI ) . read ( ) )
 OOo0 = len ( OOo00OoO )
 for iII1i11IIi1i in OOo00OoO :
  iIi1ii1I1 = iII1i11IIi1i [ 0 ]
  O0o0Oo = iII1i11IIi1i [ 1 ]
  iii1iiii11I = iII1i11IIi1i [ 2 ]
  try :
   i1III = iII1i11IIi1i [ 3 ]
   if i1III == None :
    raise
  except :
   if I1IiI . getSetting ( 'use_thumb' ) == "true" :
    i1III = iii1iiii11I
   else :
    i1III = II111iiiI1Ii
  try : ooo0ooO = iII1i11IIi1i [ 5 ]
  except : ooo0ooO = None
  try : IIIIi1 = iII1i11IIi1i [ 6 ]
  except : IIIIi1 = None
  if 56 - 56: OOooO . o00ooooO0oO
  if iII1i11IIi1i [ 4 ] == 0 :
   Ooo0OO0oOO ( O0o0Oo , iIi1ii1I1 , iii1iiii11I , i1III , '' , '' , '' , 'fav' , ooo0ooO , IIIIi1 , OOo0 )
  else :
   ooOoOoo0O ( iIi1ii1I1 , O0o0Oo , iII1i11IIi1i [ 4 ] , iii1iiii11I , II111iiiI1Ii , '' , '' , '' , '' , 'fav' )
   if 3 - 3: oOOoo + o00ooooO0oO . O00ooooo00 / oOOOo0o0O % o00ooooO0oO
   if 98 - 98: ooO00oo * IIii1I . oOOoo * IiIIi1I1Iiii / OOO0O + IiIi11i
def iiI1ii111 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OoOO = [ ]
 if not os . path . exists ( iI111iI + 'txt' ) :
  os . makedirs ( iI111iI + 'txt' )
 if not os . path . exists ( IiII ) :
  os . makedirs ( IiII )
 try :
  if 7 - 7: I1ii % I11iii11IIi - IIiIiII11i + IiIIi1I1Iiii
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iI111iI ) == False :
  O00o0o0000o0o ( 'Making Favorites File' )
  OoOO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  i1I1ii11i1Iii = open ( iI111iI , "w" )
  i1I1ii11i1Iii . write ( json . dumps ( OoOO ) )
  i1I1ii11i1Iii . close ( )
 else :
  O00o0o0000o0o ( 'Appending Favorites' )
  i1I1ii11i1Iii = open ( iI111iI ) . read ( )
  oo = json . loads ( i1I1ii11i1Iii )
  oo . append ( ( name , url , iconimage , fanart , mode ) )
  I1IiiiiI = open ( iI111iI , "w" )
  I1IiiiiI . write ( json . dumps ( oo ) )
  I1IiiiiI . close ( )
  if 70 - 70: iIiiiI1IiI1I1 + o00ooooO0oO + i11iIiiIii - O00ooooo00 / ooO00oo
  if 40 - 40: OOO0O * o00ooooO0oO
def IiI ( name ) :
 oo = json . loads ( open ( iI111iI ) . read ( ) )
 for i11IIIiI11 in range ( len ( oo ) ) :
  if oo [ i11IIIiI11 ] [ 0 ] == name :
   del oo [ i11IIIiI11 ]
   I1IiiiiI = open ( iI111iI , "w" )
   I1IiiiiI . write ( json . dumps ( oo ) )
   I1IiiiiI . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 36 - 36: I1ii + I11iii11IIi + OOooO + IIiIiII11i
def ooO000 ( url ) :
 if I1IiI . getSetting ( 'Updatecommonresolvers' ) == 'true' :
  OOoooOoO0Oo = os . path . join ( Iii1ii1II11i , 'genesisresolvers.py' )
  if xbmcvfs . exists ( OOoooOoO0Oo ) :
   os . remove ( OOoooOoO0Oo )
   if 39 - 39: I1ii / IiIIi1I1Iiii
  II11iiii = 'https://raw.githubusercontent.com/lambda81/lambda-addons/master/plugin.video.genesis/commonresolvers.py'
  i11i1 = urllib . urlretrieve ( II11iiii , OOoooOoO0Oo )
  I1IiI . setSetting ( 'Updatecommonresolvers' , 'false' )
 try :
  import genesisresolvers
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(Supremacy,Please enable Update Commonresolvers to Play in Settings. - ,10000)" )
  if 100 - 100: OoOoo0 % i11iIiiIii * OOooO / Ooo00oOo00o % OOO0O + oOOOo0o0O
 IiIi1II111I = genesisresolvers . get ( url ) . result
 if url == IiIi1II111I or IiIi1II111I is None :
  if 80 - 80: oOOoo / oOOOo0o0O
  xbmc . executebuiltin ( "XBMC.Notification(Supremacy,Is Finding Your Link - ,5000)" )
  import resolveurl
  iIIi1i11 = resolveurl . HostedMediaFile ( url )
  if iIIi1i11 :
   iI1Iii11i1 = resolveurl . resolve ( url )
   IiIi1II111I = iI1Iii11i1
 if IiIi1II111I :
  if isinstance ( IiIi1II111I , list ) :
   for ooOOOOo0 in IiIi1II111I :
    II11iIIii = I1IiI . getSetting ( 'quality' )
    if ooOOOOo0 [ 'quality' ] == 'HD' :
     iI1Iii11i1 = ooOOOOo0 [ 'url' ]
     break
    elif ooOOOOo0 [ 'quality' ] == 'SD' :
     iI1Iii11i1 = ooOOOOo0 [ 'url' ]
    elif ooOOOOo0 [ 'quality' ] == '1080p' and I1IiI . getSetting ( '1080pquality' ) == 'true' :
     iI1Iii11i1 = ooOOOOo0 [ 'url' ]
     break
  else :
   iI1Iii11i1 = IiIi1II111I
 return iI1Iii11i1
def oooOo0Ooo0oo ( name , mu_playlist ) :
 import urlparse
 if I1IiI . getSetting ( 'ask_playlist_items' ) == 'true' :
  O0Oo000ooO00 = [ ]
  for iII1i11IIi1i in mu_playlist :
   oOIiiIIi = urlparse . urlparse ( iII1i11IIi1i ) . netloc
   if oOIiiIIi == '' :
    O0Oo000ooO00 . append ( name )
   else :
    O0Oo000ooO00 . append ( oOIiiIIi )
  oOOOO = xbmcgui . Dialog ( )
  i11IIIiI11 = oOOOO . select ( 'Choose a video source' , O0Oo000ooO00 )
  if i11IIIiI11 >= 0 :
   if "&mode=19" in mu_playlist [ i11IIIiI11 ] :
    xbmc . Player ( ) . play ( ooO000 ( mu_playlist [ i11IIIiI11 ] . replace ( '&mode=19' , '' ) ) )
   elif "$doregex" in mu_playlist [ i11IIIiI11 ] :
    if 96 - 96: O00ooooo00 . OoOoo0 + I1ii + OOO0O * oOOOo0o0O - iIiiiI1IiI1I1
    iI = mu_playlist [ i11IIIiI11 ] . split ( '&regexs=' )
    if 81 - 81: ooO00oo * OOO0O + iIiiiI1IiI1I1 % ooO00oo
    O0o0Oo , ii111Ii11iii = oooo00 ( iI [ 1 ] , iI [ 0 ] )
    xbmc . Player ( ) . play ( O0o0Oo )
   else :
    O0o0Oo = mu_playlist [ i11IIIiI11 ]
    xbmc . Player ( ) . play ( O0o0Oo )
 else :
  ooo0ooO = xbmc . PlayList ( 1 )
  ooo0ooO . clear ( )
  i11i11 = 0
  for iII1i11IIi1i in mu_playlist :
   i11i11 += 1
   IiI1ii11I1 = xbmcgui . ListItem ( '%s) %s' % ( str ( i11i11 ) , name ) )
   ooo0ooO . add ( iII1i11IIi1i , IiI1ii11I1 )
   xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
   if 19 - 19: o00ooooO0oO + ooO00oo / I1ii / iIiiiI1IiI1I1
   if 92 - 92: O00ooooo00 % IiIi11i + IiIi11i - IIii1I . oOOoo
def iIIi1 ( name , url ) :
 if I1IiI . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('Supremacy','Choose a location to save files.',15000," + O0oo0OO0 + ")" )
  I1IiI . openSettings ( )
 oOoO0Oo0 = { 'url' : url , 'download_path' : I1IiI . getSetting ( 'save_location' ) }
 downloader . download ( name , oOoO0Oo0 )
 oOOOO = xbmcgui . Dialog ( )
 o0O0oO0 = oOOOO . yesno ( 'Supremacy' , 'Do you want to add this file as a source?' )
 if o0O0oO0 :
  o00O ( os . path . join ( I1IiI . getSetting ( 'save_location' ) , name ) )
  if 75 - 75: ooO00oo % i11iIiiIii + IIii1I
  if 92 - 92: I11iii11IIi % OOO0O0O0ooooo
def ooOoOoo0O ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False ) :
 if 55 - 55: IIii1I * OOooO
 ooIi11iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOiI11I = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 o0O0O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 o0O0O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii111I11Ii = [ ]
  if showcontext == 'source' :
   if name in str ( i1 ) :
    ii111I11Ii . append ( ( 'Remove from Sources' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'download' :
   ii111I11Ii . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'fav' :
   ii111I11Ii . append ( ( 'Remove from Add-on Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   if 6 - 6: oOOoo
  if not name in o0oOoO00o :
   ii111I11Ii . append ( ( 'Add to Add-on Favorites' , 'XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  o0O0O0o . addContextMenuItems ( ii111I11Ii )
 OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooIi11iI , listitem = o0O0O0o , isFolder = True )
 if 77 - 77: O00ooooo00 + Ooo00oOo00o . IIiIiII11i * oOOOo0o0O / ooO00oo / oOOoo
 return OOiI11I
def oOoo ( url , title , media_type = 'video' ) :
 if 57 - 57: o0ooo / o00ooooO0oO
 if 13 - 13: II1 + Ooo00oOo00o
 import youtubedl
 if not url == '' :
  if media_type == 'audio' :
   youtubedl . single_YD ( url , download = True , audio = True )
  else :
   youtubedl . single_YD ( url , download = True )
 elif xbmc . Player ( ) . isPlaying ( ) == True :
  import YDStreamExtractor
  if YDStreamExtractor . isDownloading ( ) == True :
   if 32 - 32: OOO0O0O0ooooo + I1ii % IiIIi1I1Iiii
   YDStreamExtractor . manageDownloads ( )
  else :
   iI1iI = xbmc . Player ( ) . getPlayingFile ( )
   if 100 - 100: IiIi11i / IiIi11i - oOOOo0o0O % oOOOo0o0O * I1ii / ooO00oo
   iI1iI = iI1iI . split ( '|User-Agent=' ) [ 0 ]
   IiI1ii11I1 = { 'url' : iI1iI , 'title' : title , 'media_type' : media_type }
   youtubedl . single_YD ( '' , download = True , dl_info = IiI1ii11I1 )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)" )
  if 32 - 32: IIiIiII11i + OOO0O - I1ii + OOO0O / O00ooooo00 * I1ii
def o0OoOoooo0 ( site_name , search_term = None ) :
 I1ii11 = ''
 if os . path . exists ( IiII ) == False or I1IiI . getSetting ( 'clearseachhistory' ) == 'true' :
  I1iiIiI1iI1I ( IiII , '' )
  I1IiI . setSetting ( "clearseachhistory" , "false" )
 if site_name == 'history' :
  I11i1iIiIIIIIii = OO0 ( IiII )
  O00o0OO = re . compile ( '(.+?):(.*?)(?:\r|\n)' ) . findall ( I11i1iIiIIIIIii )
  if 60 - 60: IIiIiII11i % I1ii / o0ooo % I1ii * i11iIiiIii / OOooO
  for iIi1ii1I1 , search_term in O00o0OO :
   if 'plugin://' in search_term :
    Ooo0OO0oOO ( search_term , iIi1ii1I1 , I1ii11 , '' , '' , '' , '' , '' , None , '' , total = int ( len ( O00o0OO ) ) )
   else :
    ooOoOoo0O ( iIi1ii1I1 + ':' + search_term , iIi1ii1I1 , 26 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if not search_term :
  ii111I = xbmc . Keyboard ( '' , 'Enter Search Term' )
  ii111I . doModal ( )
  if ( ii111I . isConfirmed ( ) == False ) :
   return
  search_term = ii111I . getText ( )
  if len ( search_term ) == 0 :
   return
 search_term = search_term . replace ( ' ' , '+' )
 search_term = search_term . encode ( 'utf-8' )
 if 'youtube' in site_name :
  if 34 - 34: o00ooooO0oO - oOOOo0o0O
  import _ytplist
  if 25 - 25: I1ii % IIiIiII11i + i11iIiiIii + OOO0O0O0ooooo * II1
  ooO0 = { }
  ooO0 = _ytplist . YoUTube ( 'searchYT' , youtube = search_term , max_page = 4 , nosave = 'nosave' )
  OOo0 = len ( ooO0 )
  for i11i11 in ooO0 :
   try :
    iIi1ii1I1 = ooO0 [ i11i11 ] [ 'title' ]
    OOoOoOo = ooO0 [ i11i11 ] [ 'date' ]
    try :
     o0Iiii = ooO0 [ i11i11 ] [ 'desc' ]
    except Exception :
     o0Iiii = 'UNAVAIABLE'
     if 45 - 45: oOOoo / IiIi11i . II1 + Ooo00oOo00o
    O0o0Oo = 'plugin://plugin.video.youtube/play/?video_id=' + ooO0 [ i11i11 ] [ 'url' ]
    I1ii11 = 'http://img.youtube.com/vi/' + ooO0 [ i11i11 ] [ 'url' ] + '/0.jpg'
    Ooo0OO0oOO ( O0o0Oo , iIi1ii1I1 , I1ii11 , '' , '' , '' , '' , '' , None , '' , OOo0 )
   except Exception :
    O00o0o0000o0o ( 'This item is ignored::' )
  O00oO000Oo0 = site_name + ':' + search_term + '\n'
  I1iiIiI1iI1I ( os . path . join ( iIiiiI , 'history' ) , O00oO000Oo0 , append = True )
 elif 'dmotion' in site_name :
  iIIiiIi = "https://api.dailymotion.com"
  if 19 - 19: o0ooo
  import _DMsearch
  o00OOOOOo0OOo = str ( I1IiI . getSetting ( 'familyFilter' ) )
  _DMsearch . listVideos ( iIIiiIi + "/videos?fields=description,duration,id,owner.username,taken_time,thumbnail_large_url,title,views_total&search=" + search_term + "&sort=relevance&limit=100&family_filter=" + o00OOOOOo0OOo + "&localization=en_EN&page=1" )
  if 44 - 44: OoOoo0 * o0ooo
  O00oO000Oo0 = site_name + ':' + search_term + '\n'
  I1iiIiI1iI1I ( os . path . join ( iIiiiI , 'history' ) , O00oO000Oo0 , append = True )
 elif 'IMDBidplay' in site_name :
  iIIiiIi = "http://www.omdbapi.com/?t="
  O0o0Oo = iIIiiIi + search_term
  if 49 - 49: oOOOo0o0O % OoOoo0 * i11iIiiIii / I1ii % oOOOo0o0O
  I1iIII1IiiI = dict ( { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; rv:33.0) Gecko/20100101 Firefox/33.0' , 'Referer' : 'http://joker.org/' , 'Accept-Encoding' : 'gzip, deflate' , 'Content-Type' : 'application/json;charset=utf-8' , 'Accept' : 'application/json, text/plain, */*' } )
  if 70 - 70: I11iii11IIi / iIiiiI1IiI1I1 % IiIi11i - OOooO
  II1II1iIIi11 = requests . get ( O0o0Oo , headers = I1iIII1IiiI )
  oo = II1II1iIIi11 . json ( )
  I1II1IiI1 = oo [ 'Response' ]
  if I1II1IiI1 == 'True' :
   iIIiI11iI1Ii1 = oo [ 'imdbID' ]
   iIi1ii1I1 = oo [ 'Title' ] + oo [ 'Released' ]
   oOOOO = xbmcgui . Dialog ( )
   o0O0oO0 = oOOOO . yesno ( 'Check Movie Title' , 'PLAY :: %s ?' % iIi1ii1I1 )
   if o0O0oO0 :
    O0o0Oo = 'plugin://plugin.video.pulsar/movie/' + iIIiI11iI1Ii1 + '/play'
    O00oO000Oo0 = iIi1ii1I1 + ':' + O0o0Oo + '\n'
    I1iiIiI1iI1I ( IiII , O00oO000Oo0 , append = True )
    return O0o0Oo
  else :
   xbmc . executebuiltin ( "XBMC.Notification(SimpleKore,No IMDB match found ,7000," + O0oo0OO0 + ")" )
   if 94 - 94: IiIi11i / i11iIiiIii % OOO0O0O0ooooo
def O0oO0oo0O ( string ) :
 if isinstance ( string , basestring ) :
  if isinstance ( string , unicode ) :
   string = string . encode ( 'ascii' , 'ignore' )
 return string
def oooOOO0ooOoOOO ( string , encoding = 'utf-8' ) :
 if isinstance ( string , basestring ) :
  if not isinstance ( string , unicode ) :
   string = unicode ( string , encoding , 'ignore' )
 return string
def o0IiIiI111IIII1 ( s ) : return "" . join ( filter ( lambda OOo0oO00ooO00 : ord ( OOo0oO00ooO00 ) < 128 , s ) )
if 100 - 100: oOOOo0o0O * OOO0O0O0ooooo + IIiIiII11i + I11iii11IIi . oOOOo0o0O
def OO0IIIIIIi111i ( command ) :
 oo = ''
 try :
  oo = xbmc . executeJSONRPC ( oooOOO0ooOoOOO ( command ) )
 except UnicodeEncodeError :
  oo = xbmc . executeJSONRPC ( O0oO0oo0O ( command ) )
  if 37 - 37: OOooO
 return oooOOO0ooOoOOO ( oo )
 if 33 - 33: Ooo00oOo00o - OOO0O0O0ooooo - Ooo00oOo00o
 if 94 - 94: ooO00oo * OoOoo0 * II1 / o0ooo . ooO00oo - o0ooo
def I111i1II ( ) :
 I1I1i = xbmc . getSkinDir ( )
 if I1I1i == 'skin.confluence' :
  xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 elif I1I1i == 'skin.aeon.nox' :
  xbmc . executebuiltin ( 'Container.SetViewMode(511)' )
 else :
  xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
  if 45 - 45: oOOOo0o0O
  if 25 - 25: oOOOo0o0O % OOO0O0O0ooooo
def I11 ( url ) :
 oO0ooO00 = oooOOO0ooOoOOO ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":["thumbnail","title","year","dateadded","fanart","rating","season","episode","studio"]},"id":1}' ) % url
 if 94 - 94: I1ii - OoOoo0 + IiIIi1I1Iiii % OOO0O - ooO00oo
 oooOoO00OooO0 = json . loads ( OO0IIIIIIi111i ( oO0ooO00 ) )
 for iII1i11IIi1i in oooOoO00OooO0 [ 'result' ] [ 'files' ] :
  url = iII1i11IIi1i [ 'file' ]
  iIi1ii1I1 = o0IiIiI111IIII1 ( iII1i11IIi1i [ 'label' ] )
  I1ii11 = o0IiIiI111IIII1 ( iII1i11IIi1i [ 'thumbnail' ] )
  try :
   II111iiiI1Ii = o0IiIiI111IIII1 ( iII1i11IIi1i [ 'fanart' ] )
  except Exception :
   II111iiiI1Ii = ''
  try :
   OOoOoOo = iII1i11IIi1i [ 'year' ]
  except Exception :
   OOoOoOo = ''
  try :
   ooo = iII1i11IIi1i [ 'episode' ]
   i1I1i111Ii = iII1i11IIi1i [ 'season' ]
   if ooo == - 1 or i1I1i111Ii == - 1 :
    o0Iiii = ''
   else :
    o0Iiii = '[COLOR yellow] S' + str ( i1I1i111Ii ) + '[/COLOR][COLOR hotpink] E' + str ( ooo ) + '[/COLOR]'
  except Exception :
   o0Iiii = ''
  try :
   o00OOo = iII1i11IIi1i [ 'studio' ]
   if o00OOo :
    o0Iiii += '\n Studio:[COLOR steelblue] ' + o00OOo [ 0 ] + '[/COLOR]'
  except Exception :
   o00OOo = ''
   if 40 - 40: IIii1I + OOooO * I11iii11IIi + I1ii
  if iII1i11IIi1i [ 'filetype' ] == 'file' :
   Ooo0OO0oOO ( url , iIi1ii1I1 , I1ii11 , II111iiiI1Ii , o0Iiii , '' , OOoOoOo , '' , None , '' , total = len ( oooOoO00OooO0 [ 'result' ] [ 'files' ] ) )
   if 15 - 15: OoOoo0 % IIiIiII11i - IIii1I * IiIi11i
   if 71 - 71: I11iii11IIi % IiIIi1I1Iiii % IiIi11i
  else :
   ooOoOoo0O ( iIi1ii1I1 , url , 53 , I1ii11 , II111iiiI1Ii , o0Iiii , '' , OOoOoOo , '' )
   if 34 - 34: OoOoo0 / OoOoo0 % ooO00oo . I11iii11IIi / IiIIi1I1Iiii
   if 99 - 99: IiIi11i * IIiIiII11i - IiIi11i % oOOoo
def Ooo0OO0oOO ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total , setCookie = "" ) :
 if 40 - 40: oOOOo0o0O / ooO00oo / IIii1I + oOOoo
 ii111I11Ii = [ ]
 try :
  name = name . encode ( 'utf-8' )
 except : pass
 OOiI11I = True
 if 59 - 59: OoOoo0 * II1 + oOOOo0o0O . IIii1I / O00ooooo00
 if regexs :
  iii1i = '17'
  if 75 - 75: OoOoo0 . oOOOo0o0O - IIii1I * Ooo00oOo00o * OOooO
  ii111I11Ii . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif any ( x in url for x in OO0o ) and url . startswith ( 'http' ) :
  iii1i = '19'
  if 93 - 93: IiIi11i
  ii111I11Ii . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . endswith ( '&mode=18' ) :
  url = url . replace ( '&mode=18' , '' )
  iii1i = '18'
  if 18 - 18: IiIi11i
  ii111I11Ii . append ( ( '[COLOR white]!!Download!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  if I1IiI . getSetting ( 'dlaudioonly' ) == 'true' :
   ii111I11Ii . append ( ( '!!Download [COLOR seablue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . startswith ( 'magnet:?xt=' ) or '.torrent' in url :
  if 66 - 66: I1ii * i11iIiiIii + I11iii11IIi / oOOOo0o0O
  if '&' in url and not '&amp;' in url :
   url = url . replace ( '&' , '&amp;' )
  url = 'plugin://plugin.video.pulsar/play?uri=' + url
  iii1i = '12'
  if 96 - 96: oOOOo0o0O + oOOOo0o0O % ooO00oo % oOOOo0o0O
 else :
  iii1i = '12'
  if 28 - 28: IIii1I + I11iii11IIi . o0ooo % i11iIiiIii
  ii111I11Ii . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 ooIi11iI = sys . argv [ 0 ] + "?"
 O00oOooo00o0o = False
 if 56 - 56: I11iii11IIi % OOO0O - oOOoo % IIii1I
 if playlist :
  if I1IiI . getSetting ( 'add_playlist' ) == "false" :
   ooIi11iI += "url=" + urllib . quote_plus ( url ) + "&mode=" + iii1i
  else :
   ooIi11iI += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) )
   name = name + '[COLOR magenta] (' + str ( len ( playlist ) ) + ' items )[/COLOR]'
   O00oOooo00o0o = True
 else :
  ooIi11iI += "url=" + urllib . quote_plus ( url ) + "&mode=" + iii1i
 if regexs :
  ooIi11iI += "&regexs=" + regexs
 if not setCookie == '' :
  ooIi11iI += "&setCookie=" + urllib . quote_plus ( setCookie )
  if 76 - 76: II1 * II1 - OOooO - IIii1I . II1 / OOO0O
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 o0O0O0o = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
 o0O0O0o . setProperty ( "Fanart_Image" , fanart )
 if 86 - 86: IiIi11i
 if ( not O00oOooo00o0o ) and not any ( x in url for x in Oo0Ooo ) :
  if regexs :
   if '$pyFunction:playmedia(' not in urllib . unquote_plus ( regexs ) and 'notplayable' not in urllib . unquote_plus ( regexs ) :
    if 51 - 51: Ooo00oOo00o - i11iIiiIii * IIiIiII11i
    o0O0O0o . setProperty ( 'IsPlayable' , 'true' )
  else :
   o0O0O0o . setProperty ( 'IsPlayable' , 'true' )
 else :
  O00o0o0000o0o ( 'NOT setting isplayable' + url )
  if 95 - 95: oOOOo0o0O % OOO0O + o0ooo % IiIi11i
 if showcontext :
  ii111I11Ii = [ ]
  if showcontext == 'fav' :
   ii111I11Ii . append (
 ( 'Remove from Add-on Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) )
 )
  elif not name in o0oOoO00o :
   Ii1i = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) )
 )
   if playlist :
    Ii1i += 'playlist=' + urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) )
   if regexs :
    Ii1i += "&regexs=" + regexs
   ii111I11Ii . append ( ( 'Add to Add-on Favorites' , 'XBMC.RunPlugin(%s)' % Ii1i ) )
  o0O0O0o . addContextMenuItems ( ii111I11Ii )
  if 19 - 19: IiIi11i % I1ii
 if not playlist is None :
  if I1IiI . getSetting ( 'add_playlist' ) == "false" :
   iIiiIiiI1Ii111i = name . split ( ') ' ) [ 1 ]
   IIIi1IiIiii = [
 ( 'Play ' + iIiiIiiI1Ii111i + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( iIiiIiiI1Ii111i ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) ) )
 ]
   o0O0O0o . addContextMenuItems ( IIIi1IiIiii )
   if 55 - 55: I1ii
   if 37 - 37: ooO00oo / i11iIiiIii / IiIIi1I1Iiii
 OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooIi11iI , listitem = o0O0O0o , totalItems = total )
 if 97 - 97: o00ooooO0oO . OoOoo0 / IIiIiII11i
 return OOiI11I
 if 83 - 83: OoOoo0 - OOO0O * I1ii
def oOO00OO0OooOo ( url , name , iconimage , setresolved = True ) :
 if setresolved :
  o0O0O0o = xbmcgui . ListItem ( name , iconImage = iconimage )
  o0O0O0o . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
  o0O0O0o . setProperty ( "IsPlayable" , "true" )
  o0O0O0o . setPath ( str ( url ) )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0O0O0o )
 else :
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  if 13 - 13: OOO0O0O0ooooo % IiIi11i % OoOoo0
  if 25 - 25: II1 % oOOoo * iIiiiI1IiI1I1 - Ooo00oOo00o
  if 95 - 95: IIiIiII11i % o00ooooO0oO * IIiIiII11i + OOO0O0O0ooooo . o00ooooO0oO % II1
  if 6 - 6: I11iii11IIi - IiIi11i * o0ooo + I11iii11IIi % o0ooo
def ooo0oooo0 ( link ) :
 O0o0Oo = urllib . urlopen ( link )
 OOO00000o0 = O0o0Oo . read ( )
 O0o0Oo . close ( )
 OOOO000Ooo0O = OOO00000o0 . split ( "Jetzt" )
 oOo0oOooo0O = OOOO000Ooo0O [ 1 ] . split ( 'programm/detail.php?const_id=' )
 iI1iIIIIIiIi1 = oOo0oOooo0O [ 1 ] . split ( '<br /><a href="/' )
 iIioOo = iI1iIIIIIiIi1 [ 0 ] [ 40 : len ( iI1iIIIIIiIi1 [ 0 ] ) ]
 ooOo0o = oOo0oOooo0O [ 2 ] . split ( "</a></p></div>" )
 IIIIiiI = ooOo0o [ 0 ] [ 17 : len ( ooOo0o [ 0 ] ) ]
 IIIIiiI = IIIIiiI . encode ( 'utf-8' )
 return "  - " + IIIIiiI + " - " + iIioOo
 if 75 - 75: II1 . oOOOo0o0O + Ooo00oOo00o / oOOoo - IIiIiII11i % oOOoo
def O0OooooO0o0O0 ( ) :
 II ( '[COLOR aqua] Featured 24/7[/COLOR]' , '' , 907 , 'http://stephen-builds.uk/art/24%207%20shows.png' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 II ( '[COLOR aqua] 24/7 Tv Shows[/COLOR]' , '' , 908 , 'http://stephen-builds.uk/art/rolling-stone-100-best-tv-shows-of-all-time-c76cdd0b-2e04-4769-84c1-0faab178ddbf.jpg' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 II ( '[COLOR aqua] 24/7 Movies[/COLOR]' , '' , 909 , 'http://stephen-builds.uk/art/24%20MOVIES.png' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 II ( '[COLOR aqua] 24/7 Cable[/COLOR]' , '' , 910 , 'http://stephen-builds.uk/art/cableheader-graypurple-590x236.jpg' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 II ( '[COLOR aqua] 24/7 Random Stream[/COLOR]' , '' , 911 , 'http://stephen-builds.uk/art/maxresdefault.jpg' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 if 74 - 74: I11iii11IIi / O00ooooo00 % II1
def o00o0o000Oo ( ) :
 O0o0Oo = 'http://arconaitv.me/'
 i11IIIiI11 = 'index.php#shows'
 O0O = BeautifulSoup ( requests . get ( O0o0Oo + i11IIIiI11 ) . content )
 oo0OooOOo0 = O0O . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for o0O in oo0OooOOo0 :
  o00OO00OoO = o0O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I11i1 in o00OO00OoO :
   Oooo00OOo = I11i1 . text
  iIiII = o0O . findAll ( 'a' )
  for I11i1 in iIiII :
   if I11i1 . has_key ( 'href' ) :
    oOO00O = O0o0Oo + I11i1 [ 'href' ]
   if I11i1 . has_key ( 'title' ) :
    iIi1ii1I1 = I11i1 [ 'title' ]
   OooOO = { 'User-Agent' : random_agent ( ) }
   iio0oo0Oo = requests . get ( oOO00O , headers = OooOO ) . content
   i1i1I1II = packets ( iio0oo0Oo )
   if 66 - 66: ooO00oo + IIii1I
   O00o0OO = re . compile ( "'https:(.+?)'" ) . findall ( i1i1I1II )
   for o0Oo00oOO in O00o0OO :
    o0Oo00oOO = o0Oo00oOO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    O0oo = 'https:' + o0Oo00oOO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    o0 ( iIi1ii1I1 , O0oo , 906 , '' , '' , '' , '' )
    if 56 - 56: ooO00oo * o00ooooO0oO
    if 98 - 98: OoOoo0 + OOO0O0O0ooooo * o00ooooO0oO + i11iIiiIii - oOOOo0o0O - IIii1I
def I11I111i1I1 ( ) :
 O0o0Oo = 'http://arconaitv.me/'
 i11IIIiI11 = 'index.php#movies'
 O0O = BeautifulSoup ( requests . get ( O0o0Oo + i11IIIiI11 ) . content )
 oo0OooOOo0 = O0O . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for o0O in oo0OooOOo0 :
  o00OO00OoO = o0O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I11i1 in o00OO00OoO :
   Oooo00OOo = I11i1 . text
  iIiII = o0O . findAll ( 'a' )
  for I11i1 in iIiII :
   if I11i1 . has_key ( 'href' ) :
    oOO00O = O0o0Oo + I11i1 [ 'href' ]
   if I11i1 . has_key ( 'title' ) :
    iIi1ii1I1 = I11i1 [ 'title' ]
   OooOO = { 'User-Agent' : random_agent ( ) }
   iio0oo0Oo = requests . get ( oOO00O , headers = OooOO ) . content
   i1i1I1II = packets ( iio0oo0Oo )
   if 41 - 41: II1 / O00ooooo00
   O00o0OO = re . compile ( "'https:(.+?)'" ) . findall ( i1i1I1II )
   for o0Oo00oOO in O00o0OO :
    o0Oo00oOO = o0Oo00oOO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    O0oo = 'https:' + o0Oo00oOO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    o0 ( iIi1ii1I1 , O0oo , 906 , '' , '' , '' , '' )
    if 70 - 70: I11iii11IIi % o0ooo % O00ooooo00 / OOO0O % i11iIiiIii / O00ooooo00
    if 4 - 4: ooO00oo
def oOo0OoOOOo0 ( ) :
 O0o0Oo = 'http://arconaitv.me/'
 i11IIIiI11 = 'index.php#cable'
 O0O = BeautifulSoup ( requests . get ( O0o0Oo + i11IIIiI11 ) . content )
 oo0OooOOo0 = O0O . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for o0O in oo0OooOOo0 :
  o00OO00OoO = o0O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I11i1 in o00OO00OoO :
   Oooo00OOo = I11i1 . text
  iIiII = o0O . findAll ( 'a' )
  for I11i1 in iIiII :
   if I11i1 . has_key ( 'href' ) :
    oOO00O = O0o0Oo + I11i1 [ 'href' ]
   if I11i1 . has_key ( 'title' ) :
    iIi1ii1I1 = I11i1 [ 'title' ]
   OooOO = { 'User-Agent' : random_agent ( ) }
   iio0oo0Oo = requests . get ( oOO00O , headers = OooOO ) . content
   i1i1I1II = packets ( iio0oo0Oo )
   if 55 - 55: I1ii + OOO0O0O0ooooo / OOooO % IiIi11i / II1
   O00o0OO = re . compile ( "'https:(.+?)'" ) . findall ( i1i1I1II )
   for o0Oo00oOO in O00o0OO :
    o0Oo00oOO = o0Oo00oOO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    O0oo = 'https:' + o0Oo00oOO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    o0 ( iIi1ii1I1 , O0oo , 906 , '' , '' , '' , '' )
    if 98 - 98: oOOoo * IIii1I % IiIIi1I1Iiii % oOOOo0o0O
def O0ooO00o ( ) :
 IIiiiiiiIi1I1 = 'http://arconaitv.me/stream.php?id=random'
 OooOO = { 'User-Agent' : random_agent ( ) }
 iio0oo0Oo = requests . get ( IIiiiiiiIi1I1 , headers = OooOO ) . content
 i1i1I1II = packets ( iio0oo0Oo )
 if 24 - 24: o00ooooO0oO + II1 . ooO00oo / I11iii11IIi / OoOoo0
 O00o0OO = re . compile ( "'https:(.+?)'" ) . findall ( i1i1I1II )
 for o0Oo00oOO in O00o0OO :
  o0Oo00oOO = o0Oo00oOO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
  O0oo = 'https:' + o0Oo00oOO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  o0 ( 'Random Pick' , O0oo , 906 , '' , '' , '' , '' )
  if 65 - 65: II1
def iiii11iI1 ( ) :
 O0o0Oo = 'http://arconaitv.me/'
 i11IIIiI11 = 'index.php#shows'
 if 81 - 81: i11iIiiIii + oOOoo % i11iIiiIii - O00ooooo00
 O0O = BeautifulSoup ( requests . get ( O0o0Oo + i11IIIiI11 ) . content )
 oo0OooOOo0 = O0O . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for o0O in oo0OooOOo0 :
  o00OO00OoO = o0O . findAll ( 'a' )
  for I11i1 in o00OO00OoO :
   if I11i1 . has_key ( 'href' ) :
    oOO00O = O0o0Oo + I11i1 [ 'href' ]
   if I11i1 . has_key ( 'title' ) :
    iIi1ii1I1 = I11i1 [ 'title' ]
   OOOoo0OO = I11i1 . findAll ( 'img' )
   for Ii1I1Ii in OOOoo0OO :
    Oo0oOOo = O0o0Oo + Ii1I1Ii [ 'src' ]
    OooOO = { 'User-Agent' : random_agent ( ) }
    iio0oo0Oo = requests . get ( oOO00O , headers = OooOO ) . content
    i1i1I1II = packets ( iio0oo0Oo )
    if 9 - 9: I1ii
    O00o0OO = re . compile ( "'https:(.+?)'" ) . findall ( i1i1I1II )
    for o0Oo00oOO in O00o0OO :
     o0Oo00oOO = o0Oo00oOO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
     O0oo = 'https:' + o0Oo00oOO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     o0 ( iIi1ii1I1 , O0oo , 906 , Oo0oOOo , Oo0oOOo , '' , '' )
     if 2 - 2: IIii1I * IIiIiII11i % O00ooooo00 % OOO0O + II1 + IIiIiII11i
def o0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 ooIi11iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description )
 OOiI11I = True
 o0O0O0o = xbmcgui . ListItem ( name , iconImage = " " , thumbnailImage = iconimage )
 o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0O0o . setProperty ( "Fanart_Image" , fanart )
 OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooIi11iI , listitem = o0O0O0o , isFolder = False )
 return OOiI11I
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 16 - 16: oOOOo0o0O
 if 63 - 63: OOooO
def II ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 ooIi11iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 OOiI11I = True
 o0O0O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0O0o . setProperty ( "Fanart_Image" , fanart )
 OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooIi11iI , listitem = o0O0O0o , isFolder = True )
 return OOiI11I
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 11 - 11: OOooO - IIii1I
def iiIiIIIiiI ( name , url ) :
 import resolveurl
 try :
  OOIi1iI111II1I1 = resolveurl . resolve ( url )
  xbmc . Player ( ) . play ( OOIi1iI111II1I1 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 92 - 92: Ooo00oOo00o
 if 15 - 15: ooO00oo / ooO00oo + IIii1I % II1
def oOOO ( url , regex ) :
 oo = o0O0 ( url )
 try :
  i11i11 = re . findall ( regex , oo ) [ 0 ]
  return i11i11
 except :
  O00o0o0000o0o ( 'regex failed' )
  O00o0o0000o0o ( regex )
  return
  if 12 - 12: IiIi11i
  if 36 - 36: o00ooooO0oO . ooO00oo * II1 - o0ooo
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 60 - 60: oOOOo0o0O . OOooO / IIii1I + oOOOo0o0O * o00ooooO0oO
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_UNSORTED )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_DATE )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_GENRE )
except :
 pass
 if 82 - 82: i11iIiiIii . IIii1I * IIiIiII11i - OoOoo0 + oOOoo
oOoO0Oo0 = IiIi1Ii ( )
if 48 - 48: OOO0O
O0o0Oo = None
iIi1ii1I1 = None
iii1i = None
ooo0ooO = None
iii1iiii11I = None
II111iiiI1Ii = I1i1iiI1
ooo0ooO = None
o0o = None
IIIIi1 = None
if 39 - 39: oOOOo0o0O + Ooo00oOo00o
try :
 O0o0Oo = urllib . unquote_plus ( oOoO0Oo0 [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 iIi1ii1I1 = urllib . unquote_plus ( oOoO0Oo0 [ "name" ] )
except :
 pass
try :
 iii1iiii11I = urllib . unquote_plus ( oOoO0Oo0 [ "iconimage" ] )
except :
 pass
try :
 II111iiiI1Ii = urllib . unquote_plus ( oOoO0Oo0 [ "fanart" ] )
except :
 pass
try :
 iii1i = int ( oOoO0Oo0 [ "mode" ] )
except :
 pass
try :
 ooo0ooO = eval ( urllib . unquote_plus ( oOoO0Oo0 [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 o0o = int ( oOoO0Oo0 [ "fav_mode" ] )
except :
 pass
try :
 IIIIi1 = oOoO0Oo0 [ "regexs" ]
except :
 pass
try :
 oOoOOOO0OOO = oOoO0Oo0 [ "extra" ]
except :
 pass
O00o0o0000o0o ( "Mode: " + str ( iii1i ) )
if not O0o0Oo is None :
 O00o0o0000o0o ( "URL: " + str ( O0o0Oo . encode ( 'utf-8' ) ) )
O00o0o0000o0o ( "Name: " + str ( iIi1ii1I1 ) )
if 58 - 58: OoOoo0 % i11iIiiIii / i11iIiiIii * IiIi11i - o00ooooO0oO
if iii1i == None :
 O00o0o0000o0o ( "Index" )
 iiI1IiI ( )
 if 6 - 6: ooO00oo * iIiiiI1IiI1I1 % IIii1I
elif iii1i == 1 :
 O00o0o0000o0o ( "getData" )
 OooO0 ( O0o0Oo , II111iiiI1Ii )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 86 - 86: O00ooooo00 * OOO0O0O0ooooo % IiIi11i . IiIIi1I1Iiii % IiIi11i . IiIIi1I1Iiii
elif iii1i == 2 :
 O00o0o0000o0o ( "getChannelItems" )
 i1i1I111iIi1 ( iIi1ii1I1 , O0o0Oo , II111iiiI1Ii )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 71 - 71: OOooO . i11iIiiIii * OOO0O0O0ooooo + OOO0O0O0ooooo
elif iii1i == 3 :
 O00o0o0000o0o ( "getSubChannelItems" )
 O00oO0 ( iIi1ii1I1 , O0o0Oo , II111iiiI1Ii )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 57 - 57: II1 . OoOoo0 % iIiiiI1IiI1I1 % IIiIiII11i + oOOoo
elif iii1i == 4 :
 O00o0o0000o0o ( "getFavorites" )
 O0oo0 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 70 - 70: ooO00oo . i11iIiiIii
elif iii1i == 5 :
 O00o0o0000o0o ( "addFavorite" )
 try :
  iIi1ii1I1 = iIi1ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIi1ii1I1 = iIi1ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiI1ii111 ( iIi1ii1I1 , O0o0Oo , iii1iiii11I , II111iiiI1Ii , o0o )
 if 76 - 76: OOooO . ooO00oo % OOooO - o00ooooO0oO
elif iii1i == 6 :
 O00o0o0000o0o ( "rmFavorite" )
 try :
  iIi1ii1I1 = iIi1ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIi1ii1I1 = iIi1ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 IiI ( iIi1ii1I1 )
 if 51 - 51: II1 + o0ooo * IIii1I * I1ii / O00ooooo00
elif iii1i == 7 :
 O00o0o0000o0o ( "addSource" )
 o00O ( O0o0Oo )
 if 19 - 19: OOooO - I11iii11IIi % I1ii / II1 % OOooO
elif iii1i == 8 :
 O00o0o0000o0o ( "rmSource" )
 iII1I1I1 ( iIi1ii1I1 )
 if 65 - 65: OOO0O0O0ooooo . I1ii
elif iii1i == 9 :
 O00o0o0000o0o ( "download_file" )
 iIIi1 ( iIi1ii1I1 , O0o0Oo )
 if 85 - 85: iIiiiI1IiI1I1
elif iii1i == 10 :
 O00o0o0000o0o ( "getCommunitySources" )
 iiIII1i ( )
 if 55 - 55: OOO0O
elif iii1i == 11 :
 O00o0o0000o0o ( "addSource" )
 o00O ( O0o0Oo )
 if 76 - 76: I1ii - i11iIiiIii
elif iii1i == 12 :
 O00o0o0000o0o ( "setResolvedUrl" )
 if not O0o0Oo . startswith ( "plugin://plugin" ) or not any ( x in O0o0Oo for x in Oo0Ooo ) :
  i11i11 = xbmcgui . ListItem ( path = O0o0Oo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11i11 )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + O0o0Oo + ')' )
  if 27 - 27: OOO0O - i11iIiiIii % o00ooooO0oO / IiIIi1I1Iiii . IiIIi1I1Iiii / II1
  if 76 - 76: OoOoo0 * Ooo00oOo00o . IIii1I % II1 % OOO0O
elif iii1i == 13 :
 O00o0o0000o0o ( "play_playlist" )
 oooOo0Ooo0oo ( iIi1ii1I1 , ooo0ooO )
 if 39 - 39: iIiiiI1IiI1I1 * I11iii11IIi . OOO0O0O0ooooo * OoOoo0
elif iii1i == 14 :
 O00o0o0000o0o ( "get_xml_database" )
 OOOO0OOO ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 89 - 89: oOOoo - IiIi11i . OoOoo0 - o00ooooO0oO - IIiIiII11i
elif iii1i == 15 :
 O00o0o0000o0o ( "browse_xml_database" )
 OOOO0OOO ( O0o0Oo , True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 79 - 79: ooO00oo + ooO00oo + oOOoo
elif iii1i == 16 :
 O00o0o0000o0o ( "browse_community" )
 iiIII1i ( True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 39 - 39: OOO0O0O0ooooo - II1
elif iii1i == 17 :
 O00o0o0000o0o ( "getRegexParsed" )
 O0o0Oo , ii111Ii11iii = oooo00 ( IIIIi1 , O0o0Oo )
 if O0o0Oo :
  oOO00OO0OooOo ( O0o0Oo , iIi1ii1I1 , iii1iiii11I , ii111Ii11iii )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(Supremacy ,Failed to extract regex. - " + "this" + ",4000," + O0oo0OO0 + ")" )
elif iii1i == 18 :
 O00o0o0000o0o ( "youtubedl" )
 try :
  import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(Supremacy,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 Ii111iIi1iIi = youtubedl . single_YD ( O0o0Oo )
 oOO00OO0OooOo ( Ii111iIi1iIi , iIi1ii1I1 , iii1iiii11I )
elif iii1i == 19 :
 O00o0o0000o0o ( "Genesiscommonresolvers" )
 oOO00OO0OooOo ( ooO000 ( O0o0Oo ) , iIi1ii1I1 , iii1iiii11I , True )
 if 63 - 63: IIii1I % o0ooo * IiIi11i
elif iii1i == 21 :
 O00o0o0000o0o ( "download current file using youtube-dl service" )
 oOoo ( '' , iIi1ii1I1 , 'video' )
elif iii1i == 23 :
 O00o0o0000o0o ( "get info then download" )
 oOoo ( O0o0Oo , iIi1ii1I1 , 'video' )
elif iii1i == 24 :
 O00o0o0000o0o ( "Audio only youtube download" )
 oOoo ( O0o0Oo , iIi1ii1I1 , 'audio' )
elif iii1i == 25 :
 O00o0o0000o0o ( "YouTube/DMotion" )
 o0OoOoooo0 ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 26 :
 O00o0o0000o0o ( "YouTube/DMotion From Search History" )
 iIi1ii1I1 = iIi1ii1I1 . split ( ':' )
 o0OoOoooo0 ( O0o0Oo , search_term = iIi1ii1I1 [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 27 :
 O00o0o0000o0o ( "Using IMDB id to play in Pulsar" )
 oo0 = o0OoOoooo0 ( O0o0Oo )
 xbmc . Player ( ) . play ( oo0 )
elif iii1i == 30 :
 I1Iiiiiii ( iIi1ii1I1 , O0o0Oo , iii1iiii11I , II111iiiI1Ii )
 if 17 - 17: OOO0O0O0ooooo + II1
elif iii1i == 40 :
 oO ( )
 I111i1II ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 41 :
 oooOoOoo0oOo00 ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 78 - 78: iIiiiI1IiI1I1 + ooO00oo
elif iii1i == 53 :
 O00o0o0000o0o ( "Requesting JSON-RPC Items" )
 I11 ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 66 - 66: IIii1I
elif iii1i == 69 :
 oOOo0 ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 907 :
 iiii11iI1 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 906 :
 iiIiIIIiiI ( iIi1ii1I1 , O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 905 :
 O0OooooO0o0O0 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 908 :
 o00o0o000Oo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 909 :
 I11I111i1I1 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 910 :
 oOo0OoOOOo0 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 911 :
 O0ooO00o ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 999900 :
 oO00OOoO00 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 999999 :
 I1iIIii ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 999998 :
 I1iiii1I ( iIi1ii1I1 , O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 999997 :
 OooOOOOo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 999996 :
 OOO ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 999995 :
 ooO0oOOooOo0 ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 999994 :
 OOOO0oo0 ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 301 :
 OO ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 302 :
 IIIii11 ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 400 :
 O00o0OO0 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 401 :
 mpop ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 402 :
 O0oO ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 403 :
 oO00oOOoooO ( O0o0Oo , iIi1ii1I1 , iii1iiii11I )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 404 :
 oOOoO0o0oO ( iIi1ii1I1 , oOoOOOO0OOO )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 405 :
 iII11I1IiiIi ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 406 :
 getseaseps ( iIi1ii1I1 , O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 407 :
 eps ( iIi1ii1I1 , O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 410 :
 OOooOoooOoOo ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 500 :
 ii11i1 ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 501 :
 iII ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 502 :
 oO0o0OOOO ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 503 :
 o0oo0oOo ( O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif iii1i == 510 :
 Ii11iI1i ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 57 - 57: ooO00oo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
