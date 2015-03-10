#!/usr/bin/env python3


import tornado.web
import json

from handler.model import *

from pprint import pprint

class GetKw(tornado.web.RequestHandler):
    def get(self):
        Kw = Keyword.get(Keyword.checked == 3)
        response = { 'id': str(Kw.kwid),
                     'kw': str(Kw.kw) }
        self.write(response)

    def post(self):
        data = self.get_argument("data", "")
        self.write(data)


#class KwType(tornado.web.RequestHandler):
#    def get(self):
        
        
#    def get(self):
        
        


#class Kw(tornado.web.RequestHandler):
#    def get(self):
        
        
#    def get(self):
        
