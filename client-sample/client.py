#!/usr/bin/env python3

import urllib
#import urllib2
import urllib.request as urllib2
import json
from pprint import pprint

from handler import toserver


##- GET -----------------------------------------------------------------
data = {'kw': '',
        'kwid': ''}

ts = toserver.PostGet()

url = "http://127.0.0.1:6969/gk/"
mesg = ts.get(url)
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
