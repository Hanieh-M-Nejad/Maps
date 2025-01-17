pip install folium

import folium

# create a map object
def create_map(location, zoom_start=10):
  map_object = folium.Map(location= location, zoom_start= zoom_start)
  return map_object

#create map instance
nyc_map = create_map([40.7128, -74.0060])
nyc_map