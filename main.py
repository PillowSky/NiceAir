from tornado.ioloop import IOLoop
from index import application

application.listen(9000)
IOLoop.instance().start()
