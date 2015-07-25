import os
from tornado.web import Application
from controller.index import IndexHandler
from controller.api import APIHandler

route = [
	(r'/', IndexHandler),
	(r'/api/', APIHandler),
]

application = Application(
	handlers = route,
	template_path = os.path.join(os.path.dirname(__file__), 'view'),
	static_path = os.path.join(os.path.dirname(__file__), 'static'),
)
