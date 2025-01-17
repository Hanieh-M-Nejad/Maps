pip install ipyleaflet

from ipyleaflet import Map, TileLayer, ScaleControl

#create map
leaf_map = Map(center=[0, 0], zoom=2)

#add layers to map
topo_layer = TileLayer(url= 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                       attribution= 'Map data: &copy; <a href="https://opentopomap.org>OpenTopoMap<\a> contributors')
leaf_map.add_layer(topo_layer)
scale = ScaleControl(position = "bottomleft")
leaf_map.add_control(scale)
leaf_map