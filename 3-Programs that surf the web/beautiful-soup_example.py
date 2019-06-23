# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:14:26 2019

@author: mojiway
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

words=list()
url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
for i in range(1,4):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')   
    tags = soup('a')
    for tag in tags:
        word = tag.get('href', None)
        words.append(word)
    y= words[2]
    if len(words) < 3:  # no 3rd link
        break  # exit the loop
    else:
        url=y             
    print(words)           
    
    

#seq = []
#for i in range(0,20):
  #  word = tags[i].text
   # seq.append(word)
#print(tags)


#
#for i in range(1,4):
#    word=urllib.request.urlopen(url).read()
#    words.append(word)
#print(words) 
   
   