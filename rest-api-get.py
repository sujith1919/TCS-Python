"""
http://api.open-notify.org/iss-now.json

{
  "message": "success", 
  "timestamp": UNIX_TIME_STAMP, 
  "iss_position": {
    "latitude": CURRENT_LATITUDE, 
    "longitude": CURRENT_LONGITUDE
  }
}
"""










import requests
import json
import pprint

#get the current position of international space station
url="http://api.open-notify.org/iss-now.json"
print("Getting ISS lat long")
r = requests.get(url)
print(r.text)
response=json.loads(r.text)

pprint.pprint(response)

print(response.get('iss_position'))
lat=response.get('iss_position').get('latitude')
long=response.get('iss_position').get('longitude')

print(lat,long)





#map that place on globe
latlng="{},{}".format(lat,long)
payload = {'latlng':latlng}

mapurl='http://maps.googleapis.com/maps/api/geocode/json'
print("Getting ISS location")
r = requests.get(mapurl, params=payload)
response=json.loads(r.text)
pprint.pprint(response)
print("*"*50)

