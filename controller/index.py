# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-


from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
	def get(self):
		self.render('index.html')
