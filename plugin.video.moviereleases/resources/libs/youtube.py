﻿# -*- coding: UTF-8 -*-
# by Mafarricos
# email: MafaStudios@gmail.com
# This program is free software: GNU General Public License
import xbmcgui,xbmc,urllib
import basic,links

def searchtrailer(name):
	ytpage = open_url(links.link().youtube_trailer_search % (urllib.unquote_plus(name)))
	youtubeid = re.findall('(\d+) min', ytpage, re.DOTALL)
	return youtubeid[0]
	
def playtrailer(url,name):
	if url == None: return	
	url = youtube_plugin % (url)
	item = xbmcgui.ListItem(path=url)
	item.setProperty("IsPlayable", "true")
	xbmc.Player().play(url, item)