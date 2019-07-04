# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:43:24 2019

@author: mojiway
"""

import urllib
from urllib.request import urlopen
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

while True:

    address = input("Enter location: ")

    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false','address':address})

    print('Retrieving',url)

    uh = urlopen(url)
    data = uh.read()
    print('Retrived',len(data),'characters')

    try: js = json.loads(str(data))
    except: js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue

    placeid = js["results"][0]['place_id']
    print ("Place id",placeid)