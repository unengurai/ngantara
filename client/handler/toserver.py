#!/usr/bin/env python3

import urllib
#import urllib2
import urllib.request as urllib2

class PostGet:
    url = 'http://127.0.0.1:6969/ws/'
    uagent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    
    
    def post(self, post_data, url=None, uagent=None):
        if url is None:
            url = self.url
        
        if uagent is None:
            uagent = self.uagent
        
        
        headers = { 'User-Agent' : uagent }
        data = urllib.urlencode(post_data)
        req = urllib2.Request(url, data, headers)
        return urllib2.urlopen(req)
    
    
    def get(self, url):
        if url is None:
            url = self.url
        
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        mesg = response.read()
        return mesg.decode('ascii')
