#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:04:34 2018

@author: azulu
"""

import src.lf_prof

my_recent = get_json("user.getrecenttracks", "limit=5&user=azulu701")

for i in my_recent['recenttracks']['track']:
    print (i['name'])