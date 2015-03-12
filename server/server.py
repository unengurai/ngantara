#!/usr/bin/env python3


import tornado.escape
import tornado.ioloop
import tornado.web

from tornado import autoreload

from websearch import GetKw


app = tornado.web.Application([
                        (r"/ws/", GetKw)
                        ])


if __name__ == "__main__":
    app.listen(6969)
    app.debug = True
    IoLoop = tornado.ioloop.IOLoop.instance()
    autoreload.start(IoLoop)
    IoLoop.start()

