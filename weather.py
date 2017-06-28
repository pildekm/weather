# -*- coding: utf-8 -*-
import requests
import folium
import json

city_id = []
co_code = 'hr'
citys = ['Zagreb', 'Rijeka', 'Varazdin', 'Dubrovnik', 'Rovinj', 'Osijek', 'Split']
apiKey = '194e2d2dcdd41a19a1f4b08920a897d0'

weather_data = []

for city in citys:
    #response = requests.get('http://api.openweathermap.org/data/2.5/weather?id=3186886&APPID='+apiKey, auth=('user', 'password'))
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+','+co_code+'&appid='+apiKey, auth=('user', 'password'))
    data = response.json()
    weather_data.append(data)

#T(°C) = T(K) - 273.15


map = folium.Map(location=None, zoom_start=11)

fg = folium.FeatureGroup(name='Weather Map')
for data in weather_data:

    fg.add_child(folium.Marker(location=[data['coord']['lat'], data['coord']['lon']],
                               popup=str(data['name'])+'\n'+'Temperatura: '+str(data['main']['temp'] - 273.15)+' C'+'\n',
                               icon=folium.Icon(color='green')))
    map.add_child(fg)
map.save('Weather_map.html')