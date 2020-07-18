# we work by folium to create a worldMap
import folium

map = folium.Map(location=[23.6850, 90.3563], zoom_start=6)
map.save("Map1.html")