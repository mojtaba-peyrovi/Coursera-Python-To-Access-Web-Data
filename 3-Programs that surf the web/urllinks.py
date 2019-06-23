# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:50:10 2019

@author: mojiway
"""
# and unzip it in the same directory as this file

import urllib
from bs4 import BeautifulSoup
url = " http://py4e-data.dr-chuck.net/known_by_Amberly.html"
count = 7
position = 18
for i in range(7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)
    
    print (s[17])
    print (t[17])
    url = s[17]

