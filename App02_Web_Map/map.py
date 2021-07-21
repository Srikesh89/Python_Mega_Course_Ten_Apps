import folium
import pandas

def color_elevation_marker(ht):
    if ht < 1000:
        return 'green'
    elif 1000 <= ht and ht < 2500:
        return 'orange'
    elif 2500 <= ht:
        return 'red'

#basic webmap object
map = folium.Map(
    location=[43.4719009,-120.7509995], 
    zoom_start=5, 
    tiles = "Stamen Terrain")

#use panda to read data from csv file
#create lists of LAT and LON data
volcano_locations = pandas.read_csv("C:/Repos/Udemy_Python_Mega_Course_10_Apps/App02_Web_Map/Webmap_datasources/Volcanoes.txt")
lat = list(volcano_locations['LAT'])
lon = list(volcano_locations['LON'])
elev = list(volcano_locations['ELEV'])
name = list(volcano_locations['NAME'])

#using feature groups helps organize the code better and aids in creating control features

#add children via feature groups to the map to denote volcanoes on the map
feature_group_one = folium.FeatureGroup(name='USA Volcanoes')
for latit,longit,el,na in zip(lat,lon,elev,name):    #zip function allows you to iterate through two lists
    col = color_elevation_marker(el)
    feature_group_one.add_child(folium.CircleMarker(
            location=[latit,longit],
            popup=folium.Popup(html=f'{na}\nElevation: {el}'),
            radius=5,
            fill_color = col,
            color='gray',
            fill_opacity=0.8))

#adding a polygon overlay that encircles each country using GeoJson
#lambda function changes country color based on POP2005 property
feature_group_two = folium.FeatureGroup(name='Country Population')
feature_group_two.add_child(folium.GeoJson(
    data=open("C:/Repos/Udemy_Python_Mega_Course_10_Apps/App02_Web_Map/Webmap_datasources/world.json", 'r', encoding='UTF-8-sig').read(),
    style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] > 150000000 else 'orange' if 75000000 > x['properties']['POP2005'] else 'green'}
    ))

#adding layer control but have to add after the feature_group(s)
map.add_child(feature_group_one)
map.add_child(feature_group_two)
map.add_child(folium.LayerControl())

#creates webmap file
map.save("mapFile.html")
