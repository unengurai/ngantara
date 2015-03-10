#!/usr/bin/env python3

import urllib
#import urllib2
import urllib.request as urllib2
import json
from pprint import pprint


class PostGet:
    url = 'http://127.0.0.1:6969/ws/'
    uagent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    
    
    def Post(self, post_data, url=self.url, uagent=self.uagent):
        headers = { 'User-Agent' : uagent }
        data = urllib.urlencode(post_data)
        req = urllib2.Request(url, data, headers)
        return urllib2.urlopen(req)
    
    
    def Get(self, url=self.url):
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        mesg = response.read()
        return mesg.decode('ascii')
        
        
##- GET-----------------------------------------------------------------
#data['kwid'] = ''
data = { 'kw' : '',
         'kwid' : '' }

mesg = PostGet.Get()
jmesg = json.loads(mesg)

data = jmesg
if data['kw'] is not '':
    pprint(data['kw'])
#print(json_mesg['kw'])


##- POST----------------------------------------------------------------
#url = 'http://127.0.0.1:6969/ws/'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#values = {'data' : 'test datanya'}
#headers = { 'User-Agent' : user_agent }

#data = urllib.urlencode(values)
#req = urllib2.Request(url, data, headers)
#response = urllib2.urlopen(req)
#mesg = response.read()
#print mesg
