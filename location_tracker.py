import requests
import folium

res = requests.get('https://ipinfo.io')
data = res.json()

location = data['loc'].split(',')
lat = float(location[0])
lon = float(location[1])

popupText = "<b>Location</b><br> Longitude: {lon}<br> Latitude: {lat}".format(lon=lon, lat=lat)
popup = folium.Popup(popupText, max_width=200)

feature_group = folium.FeatureGroup("map")
feature_group.add_child(folium.Marker(location=[lat,lon], popup=popup))

map = folium.Map(location=[lat,lon], zoom_start=9)
map.add_child(feature_group)
map.save("map.html")