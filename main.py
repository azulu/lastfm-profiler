# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import json


def url_builder(method_name, params):
    
    cred_json = open("./lastfm_credentials.json")
    credentials = json.loads(cred_json.read())
    key = credentials['api_key']
    
    domain = "http://ws.audioscrobbler.com"
    base = "/2.0/?"
    method = "method=" + method_name
    api_key = "api_key=" + key
    form = "format=json"
    
    url = domain + base + method + "&" + params + "&" + api_key + "&" + form
    
    return url


def get_json(method_name, user_name):
    
    with urllib.request.urlopen(url_builder(method_name, user_name)) as url:
        data = json.loads(url.read().decode())
        
    return data

#my_recent = get_json("user.getrecenttracks", "limit=5&user=azulu701")

for i in my_recent['recenttracks']['track']:
    print (i['name'])