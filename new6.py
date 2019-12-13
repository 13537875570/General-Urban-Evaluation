import pandas as pd
import numpy as np
import os
import folium
from folium import plugins
import webbrowser
import geopandas as gp


full = pd.read_excel("G:\tweepy-master\tweepy\Points.xlsx")
full = full.dropna()


schools_map = folium.Map(location=[full['lat'].mean(), full['lon'].mean()], zoom_start=10)
marker_cluster = plugins.MarkerCluster().add_to(schools_map) 


for name,row in full.iterrows():
     folium.Marker([row["lat"], row["lon"]]).add_to(marker_cluster)     

folium.RegularPolygonMarker([row["lat"], row["lon"]],number_of_sides=10,radius=5).add_to(marker_cluster)

schools_map.save('schools_map.html') 
webbrowser.open('schools_map.html')  