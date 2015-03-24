#!/usr/bin/env python3

import sys
import tornado.web
import json
import base64

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

    #@staticmethod
    def get_post_data(self):
        post_data = self.get_argument("data")
        post_data = base64.b64decode(post_data)
        post_data = post_data.decode("utf8")
        #print(post_data)
        #exit()
        return json.loads(post_data)


class GetKw(WebSearchBase):
    def get(self):
        try:
            kw = keyword.get(keyword.checked == 3)
            response = {'kwid': str(kw.id),
                        'kw': str(kw.kw)}
        except:
            print(":: ERR : GetKw ::> " + str(sys.exc_info()))
            response = {'kwid': None,
                        'kw': None}
        self.write(json.dumps(response))

    def post(self):
        ##- hang var 'data', paling puang na'an:
        #   [act], [kwid], [value]
        data = self.get_post_data()

        response = {'resp': 'OK'}
        ##- isi 'act' : DONE=haut luput, OK:info na tarime
        if data['act'] == 'OK':
            
            try:
                query = keyword.update(checked=2).\
                    where(keyword.id == data['kwid'])
                #query.execute()
            except:
                response = {'resp': 'REPEAT'}
        elif data['act'] == "DONE":
            try:
                keyword.update(checked=1).\
                    where(keyword.id == data['kwid'])
                keyword.execute()
            except:
                response = {'resp': 'REPEAT'}
        self.write(json.dumps(response))


class SearchResult(WebSearchBase):
    def post(self):
        ##- hang var 'data', paling puang na'an:
        #   [act], [kwid], [value]
        data = self.get_post_data()

        ##- jaka ni hang yati na pasang auth methode ni,
        ##  kude die ai lah..
        print(data)
        response = {'resp': 'OK'}
        #try:
        count_url = sresult.select().\
                    where(sresult == data['url']).\
                    count()
        if count_url == 0:
            query = sresult(url=data['url'], kw_id=data['kwid'])
            query.save()
        #except:
        #    print(":: ERR ::> " + str(sys.exc_info()))
        #    response = {'resp': 'REPEAT'}

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
            keywordtype(kwtype=data['kwtype'], \
                        app=data['app'], \
                        note=data['note'])
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
            keyword(kwtype_id=data['kwtype'], kw=data['kw'])
            keyword.save()
        except:
            response = {'resp': 'REPEAT'}
        self.write(response)
