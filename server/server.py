#!/usr/bin/env python3

## python2 perlu ini nih
#import os, sys
#mbahPath = os.getcwd()
#sys.path.append(mbahPath+'/handler')
#from websearch import GetKw

import tornado.escape
import tornado.ioloop
import tornado.web

from tornado import autoreload

from handler.websearch import GetKw


app = tornado.web.Application([
                        (r"/ws/", GetKw)
                        #(r"/ws/", GetKw)
                        ])


if __name__ == "__main__":
    app.listen(6969)
    app.debug = True
    IoLoop = tornado.ioloop.IOLoop.instance()
    autoreload.start(IoLoop)
    IoLoop.start()

