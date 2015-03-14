#!/usr/bin/env python3


import tornado.web
import json

from handler import model

keyword = model.Keyword
keywordtype = model.KeywordType
sresult = model.SearchResult
authkey = model.AuthKey


class WebSearchBase(tornado.web.RequestHandler):
    @staticmethod
    def is_auth(client_key):
        auth = authkey.get(authkey.key == client_key)
        return auth.active

    @staticmethod
    def get_post_data():
        post_data = self.get_argument("data", "")
        return json.loads(post_data)


class GetKw(WebSearchBase):
    def get(self):
        kw = keyword.get(keyword.checked == 3)
        response = {'id': str(kw.kwid),
                    'kw': str(kw.kw)}
        self.write(response)

    def post(self):
        ##- hang var 'data', paling puang na'an:
        #   [act], [kwid], [value]
        data = self.get_post_data()

        response = {'resp': 'OK'}
        ##- isi 'act' : DONE=haut luput, OK:info na tarime
        if data['act'] == 'OK':
            try:
                keyword.update(checked=3).where(keyword.kwid == data['kwid'])
                keyword.save()
            except:
                response = {'resp': 'REPEAT'}
        elif data['act'] == "DONE":
            try:
                keyword.update(checked=1).where(keyword.kwid == data['kwid'])
                keyword.save()
            except:
                response = {'resp': 'REPEAT'}

        self.write(response)


class SearchResult(WebSearchBase):
    def post(self):
        ##- hang var 'data', paling puang na'an:
        #   [act], [kwid], [value]
        data = self.get_post_data()

        ##- jaka ni hang yati na pasang auth methode ni, kude die ai lah..

        response = {'resp': 'OK'}
        try:
            sresult(url=data['value'], kw=data['kwid'])
            sresult.save()
        except:
            response = {'resp': 'REPEAT'}

        self.write(response)


class KwType(WebSearchBase):
    def get(self):
        data = keywordtype.select()
        #rowcount = keywordtype.select().count()
        self.write(data)

    def post(self):
        ##- hang var 'data', paling puang na'an:
        #   [kwtype], [app], [note]
        data = self.get_post_data()
        response = {'resp': 'OK'}
        try:
            keywordtype(kwtype=data['kwtype'], app=data['app'], note=data['note'])
            keywordtype.save()
        except:
            response = {'resp': 'REPEAT'}
        self.write(response)


class Kw(WebSearchBase):
    def get(self):
        data = keyword.select()
        #rowcount = keyword.select().count()
        self.write(data)

    def post(self):
        ##- hang var 'data', paling puang na'an:
        #   [kwtype], [kw]
        data = self.get_post_data()
        response = {'resp': 'OK'}
        try:
            keyword(kwtype=data['kwtype'], kw=data['kw'])
            keyword.save()
        except:
            response = {'resp': 'REPEAT'}
        self.write(response)
