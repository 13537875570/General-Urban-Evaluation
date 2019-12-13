
import numpy as np
import pandas as pd
import seaborn as sns
import folium
from folium import plugins
import webbrowser
from folium.plugins import HeatMap
# posi=pd.read_csv("D:\\Files\\datasets\\CitiesLatLon_China.csv")
 
posi=pd.read_excel("Points.xlsx")
 
num = 30
 
lat = np.array(posi["lat"][0:num])                       
lon = np.array(posi["lon"][0:num])                       

 
data1 = [[lat[i],lon[i]] for i in range(num)]    
 
map_osm = folium.Map(location=[38,-77],zoom_start=5)    
HeatMap(data1).add_to(map_osm) 
 
file_path = r"D:\file.html"
map_osm.save(file_path)     
 
webbrowser.open(file_path)  




schools_map = folium.Map(location=[posi['lat'].mean(), posi['lon'].mean()], zoom_start=10)
marker_cluster = plugins.MarkerCluster().add_to(schools_map) 


for name,row in posi.iterrows():
     folium.Marker([row["lat"], row["lon"]]).add_to(marker_cluster)     

folium.RegularPolygonMarker([row["lat"], row["lon"]],number_of_sides=10,radius=5).add_to(marker_cluster)

schools_map.save('schools_map.html') 
webbrowser.open('schools_map.html') 