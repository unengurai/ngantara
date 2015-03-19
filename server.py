#!/usr/bin/env python3


import tornado.escape
import tornado.ioloop
import tornado.web

from tornado import autoreload

from handler import websearch


app = tornado.web.Application([
    (r"/gk/", websearch.GetKw),
    (r"/sr/", websearch.SearchResult),
    (r"/kt/", websearch.KwType),
    (r"/k/", websearch.Kw)
])

if __name__ == "__main__":
    app.listen(6969)
    app.debug = True
    IoLoop = tornado.ioloop.IOLoop.instance()
    autoreload.start(IoLoop)
    IoLoop.start()
