import urllib
import xml.etree.ElementTree as ET

# extract all the comment/count values from the url and get the sum of all of them
url = '  http://py4e-data.dr-chuck.net/comments_238622.xml'

# get the content of the url as a string
data = urllib.request.urlopen(url).read()

# transform the string content into a xml tree
tree = ET.fromstring(data)

# find all count elements
counts = tree.findall('comments/comment/count')

# extract the value of each count element and add it to the total
total = 0
for count in counts:
    total += int(count.text)

print ('total: ', total)




# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
# import ssl
#
# api_key = False
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro
#
# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#
#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)
#
#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text
#
#     print('lat', lat, 'lng', lng)
#     print(location)