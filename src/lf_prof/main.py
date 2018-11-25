#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: azulu
"""

import urllib.request
import json

class Request:
    'Request to the last.fm server'
    credentials = json.loads(open("./resources/lastfm_credentials.json").read())
    key = credentials['api_key']
    
    def __init__(self, method_name, params):
        self.method_name = method_name
        self.params = params
        
    def build_url(self):
        'Builds a request url from supplied properties'
        domain = "http://ws.audioscrobbler.com"
        base = "/2.0/?"
        method = "method=" + self.method_name
        api_key = "api_key=" + Request.key
        form = "format=json"
        
        url = domain + base + method + "&" + self.params + "&" + api_key + "&" + form
    
        return url


def get_json(method_name, user_name):
    
    with urllib.request.urlopen(url_builder(method_name, user_name)) as url:
        data = json.loads(url.read().decode())
        
    return data