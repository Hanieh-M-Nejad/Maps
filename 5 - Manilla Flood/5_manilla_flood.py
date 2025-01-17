pip install folium

# importing libraries
import pandas as pd
import folium
from folium.plugins import HeatMap

# importing data
data = pd.read_csv("/content/AEGISDataset.csv")

# cleaning data
cols = ["lat",	"lon",	"flood_heig",	"elevation",	"precipitat"]
data[cols] = data[cols].apply(pd.to_numeric, errors = "coerce")
data_clean = data.dropna()
##print(f"Checking Cleaned Data: {data_clean.isnull().sum()}")

# normalizing data
data_clean["flood_height_normal"] = (data_clean["flood_heig"] - data_clean["flood_heig"].min()) / (data_clean["flood_heig"].max() - data_clean["flood_heig"].min())
data_clean["elevation_normal"] = (data_clean["elevation"] - data_clean["elevation"].min()) / (data_clean["elevation"].max() - data_clean["elevation"].min())
data_clean["precipitat_normal"] = (data_clean["precipitat"] - data_clean["precipitat"].min()) / (data_clean["precipitat"].max() - data_clean["precipitat"].min())

# flood risk and elevation have inverse relationship
data_clean["elevation_normal"] = 1 - data_clean["elevation_normal"]

# calculating flood risk score
data_clean["Flood_Risk_Score"] = (data_clean["flood_height_normal"] * 0.3) + (data_clean["elevation_normal"] * 0.3) + (data_clean["precipitat_normal"] * 0.4)

# map coloring function
def map_color(Flood_Risk_Score):
  if Flood_Risk_Score < 0.2:
    return "green"
  elif 0.2 <= Flood_Risk_Score < 0.4:
    return "yellow"
  elif 0.4<= Flood_Risk_Score < 0.6:
    return "orange"
  elif 0.6<= Flood_Risk_Score < 0.8:
    return "red"
  else:
    return "darkred"

# add color column to data_clean using map_color function
data_clean["Risk_Color"] = data_clean["Flood_Risk_Score"].apply(map_color)

# creating map
manila_coordinates = [14.5995, 120.9842]
map_flood_risk = folium.Map(location = manila_coordinates, zoom_start= 11)
heatmap_data = data_clean[["lat", "lon", "Flood_Risk_Score"]].values.tolist()
HeatMap(heatmap_data, radius=15, max_zoom=13).add_to(map_flood_risk)
map_flood_risk



