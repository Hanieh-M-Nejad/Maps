pip install ipyleaflet

pip install geopy

from ipyleaflet import Map, Marker, CircleMarker, basemaps, LayersControl
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

# a function that returns cities latitude and longitude
def city_coordinates(city_name):
  geo_locator = Nominatim(user_agent = "geo_analysis")
  location = geo_locator.geocode(city_name)
  return (location.latitude, location.longitude)

# a function that returns the distance between two given cities
def calculate_distance (first_city, second_city):
  return great_circle(first_city, second_city).kilometers

big_cities = {
      "New York": (40.7128, -74.0060),
       "Los Angeles": (34.0522, -118.2437),
       "Chicago": (41.8781, -87.6298),
       "Houston": (29.7604, -95.3698),
       "Phoenix": (33.4484, -112.0740),
       "Philadelphia": (39.9526, -75.1652),
       "Jacksonville": (30.3321838, -81.655651),
       "Columbus": (39.9622601, -83.0007065),
       "Charlotte": (35.2272086, -80.8430827),
       "Indianapolis": (39.7683331, -86.1583502),
       "Seattle": (47.6061, -122.3328),
       "Denver": (39.7392364, -104.984862),
       "Oklahoma City": (35.4729886, -97.5170536),
       "Nashville": (36.1622767, -86.7742984),
       "Washington D.C.": (38.9072, -77.0369),
       "Las Vegas": (36.1672559, -115.148516),
       "Boston": (42.3601, -71.0589),
       "San Antonio": (29.4241, -98.4936),
       "San Diego": (32.7157, -117.1611),
       "Dallas": (32.7767, -96.7970),
       "San Jose": (37.3382, -121.8863),
       "Austin": (30.2672, -97.7431),
       "San Francisco": (37.7749, -122.4194),
       "Albuquerque": (35.0841034, -106.650985),
       "Honolulu": (21.304547, -157.855676),
       "Anchorage": (61.2163129, -149.894852),
       "Salt Lake City": (40.7596198, -111.886797)
  }

max_distance = 500
if __name__ == "__main__":
  # asking user for a city name and returning its coordinates
  city_name = input("Write down the name of a city to find its nearby big cities: ")
  city_coords = city_coordinates(city_name)
  print(f"Coordinates of {city_name}: {city_coords}")

  # identifying the nearby cities
  near_cities = {}
  for city, coords in big_cities.items():
    distance = calculate_distance(city_coords, coords)
    if distance < max_distance:
      near_cities [city] = coords

print(f"near cities are: {near_cities}")

# creating map
my_map = Map(center= (city_coords[0], city_coords[1]), zoom = 6, basemap = basemaps.OpenStreetMap.Mapnik)

# adding markers for user's city
user_city_marker = Marker(location = (city_coords[0], city_coords[1]), title= city_name)
my_map.add_layer(user_city_marker)

# adding markers for big cities
for city, coords in near_cities.items():
  marker = CircleMarker(location = (coords[0], coords[1]), radius= int(max_distance/2) , color= "MediumSeaGreen", fill_color= "MediumSeaGreen", fill_opacity= 0.1)
  my_map.add_layer(marker)

# add map scale
my_map.add_control(LayersControl())

#display map
my_map