pip install geopandas

import geopandas as gpd
import matplotlib.pyplot as plt

#create map with geopandas
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
world = gpd.read_file(url)
world.plot()
plt.show()

