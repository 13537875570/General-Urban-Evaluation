import  folium
import  webbrowser
m=folium.Map(location=[-79.257789,37.332496],zoom_start=10) 


folium.Marker([-79.257789,37.332496],popup='<b</b>').add_to(m)  
folium.Marker([-79.257789,37.332496],popup='<b></b>',icon=folium.Icon(color='red')).add_to(m)

folium.Marker([40.24,116.74],popup='<b></b>',icon=folium.Icon(color='green',icon='info-sign')).add_to(m)



folium.Circle(
    location=[-79.257789,37.3324960],
    radius=10000,
    color='crimson',
    popup='popup',
    fill=False
).add_to(m)
