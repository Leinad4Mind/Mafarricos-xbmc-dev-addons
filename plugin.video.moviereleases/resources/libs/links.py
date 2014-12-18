﻿# -*- coding: UTF-8 -*-
# by Mafarricos
# email: MafaStudios@gmail.com
# This program is free software: GNU General Public License

class link:
	def __init__(self):
		import base64
		self.omdbapi_info = 'http://www.omdbapi.com/?plot=short&r=json&i=%s'
		
		self.tmdb_base = 'http://api.themoviedb.org/3/movie/%s'
		self.tmdb_image = 'http://image.tmdb.org/t/p/%s'
		self.tmdb_key = base64.urlsafe_b64decode('ODFlNjY4ZTdhMzdhM2Y2NDVhMWUyMDYzNjg3ZWQ3ZmQ=')
		self.tmdb_info = self.tmdb_base % ('%s?language=%s&api_key='+self.tmdb_key)
		self.tmdb_info_default = self.tmdb_base % ('%s?append_to_response=trailers,credits&api_key='+self.tmdb_key)
		self.tmdb_info_default_alt = self.tmdb_base % ('%s?language=ge&append_to_response=trailers,credits&api_key='+self.tmdb_key)
		self.tmdb_theaters = self.tmdb_base % ('now_playing?page=%s&api_key='+self.tmdb_key)
		self.tmdb_upcoming = self.tmdb_base % ('upcoming?page=%s&api_key='+self.tmdb_key)
		self.tmdb_popular = self.tmdb_base % ('popular?page=%s&api_key='+self.tmdb_key)
		self.tmdb_top_rated = self.tmdb_base % ('top_rated?page=%s&api_key='+self.tmdb_key)			
		self.tmdb_backdropbase = self.tmdb_image % ('original%s')
		self.tmdb_posterbase = self.tmdb_image % ('w500%s')

		self.youtube_trailer_search = 'http://gdata.youtube.com/feeds/api/videos?q=%s-trailer&start-index=1&max-results=1&v=2&alt=json&hd'
		self.youtube_plugin = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'