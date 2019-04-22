#!/usr/bin/python3

import requests
import json
from pprint import pprint
VIDEOS = {}

session = requests.Session()

brands = json.loads(session.get('http://nickapp.ilovegames.co.il/api/nicktogoapi/GetMainPage', params={'countryCode':'IL','deviceId':'0.vtxk2e2g42q','isApp':'0'}).text)['brands']
items = json.loads(session.get('http://nickapp.ilovegames.co.il/api/nicktogoapi/GetItems', params={'countryCode':'IL','deviceId':'0.vtxk2e2g42q','isApp':'0'}).text)['items']

for brand in brands:
    if b'\xf4\xf8\xf7\xe9\xed'.decode('cp1255') in brand['categories']:
        VIDEOS.update({brand['name']:[]})

for item in items:
    brand = item['brand_name']
    if brand in VIDEOS.keys() and item['item_type'] == 'Full Episode':
        VIDEOS[brand].append({'name':item['title'], 'video':item['url'],'thumb':item['image_1']})

pprint(VIDEOS)
