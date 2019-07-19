from GeoAPI import *

address = 'Lady Shaw Building, Hong Kong'
geojs = getGeojs(address, verbose=True)

print('Place id', geojs['results'][0]['place_id'])

try:
    lat = geojs['results'][0]['geometry']['location']['lat']
    lng = geojs['results'][0]['geometry']['location']['lng']
except:
    lat = None
    lng = None

print('lat', lat, 'lng', lng)
location = geojs['results'][0]['formatted_address']
print(location)