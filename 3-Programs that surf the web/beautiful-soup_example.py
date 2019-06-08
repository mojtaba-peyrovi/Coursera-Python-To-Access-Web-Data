# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:14:26 2019

@author: mojiway
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

for tag in tags:
    print(tag.get('href',None))
                              