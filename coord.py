import  folium
import  webbrowser as wb

m = folium.Map(
    location=[38.53707, -77.02182],
    zoom_start=10
)
m.add_child(folium.LatLngPopup())


m.add_child(
    folium.ClickForMarker(popup='Waypoint')
)
m.save('f2.html')
wb.open('f2.html')
