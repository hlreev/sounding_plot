#!/usr/bin/python
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyproj import geodesic_version_str
os.environ['PROJ_LIB'] = '/Users/hunlr/anaconda3/envs/cartopy_env/Library/share/proj'
from mpl_toolkits.basemap import Basemap

# Read in data for usage
data = pd.read_csv("data/20221001_00z.csv")

# Parse out the data for usage
lats = data["latitude"]
lons = data["longitude"]

# How much to zoom from coordinates (in degrees)
lat_zoom_scale = 5
lon_zoom_scale = 10

# Setup the bounding box for the zoom and bounds of the map
bbox = [np.min(lats) - lat_zoom_scale, np.max(lats) + lat_zoom_scale,\
        np.min(lons) - lon_zoom_scale, np.max(lons) + lon_zoom_scale]

plt.figure(figsize=(12,6))
# Define the projection, scale, the corners of the map, and the resolution.
m = Basemap(projection = 'merc', llcrnrlat = bbox[0], urcrnrlat = bbox[1],\
            llcrnrlon = bbox[2], urcrnrlon = bbox[3], lat_ts = 10, resolution = 'f') # c = crude, l = low, i = intermediate, h = high, f = full

# Draw the world around us
m.fillcontinents(color = '#69b2a2', lake_color = '#A6CAE0') 
m.drawcoastlines()
m.drawcountries(color = 'grey', linewidth = 1.5)
m.drawstates(color = 'lightgrey', linewidth = 1)
m.drawcounties()

# draw parallels, meridians, and color boundaries
m.drawparallels(np.arange(bbox[0] ,bbox[1] ,(bbox[1] - bbox[0]) / 5), labels = [1, 0, 0, 0])
m.drawmeridians(np.arange(bbox[2], bbox[3], (bbox[3] - bbox[2]) / 5), labels = [0, 0 ,0 ,1], rotation = 45)
m.drawmapboundary(fill_color='dodgerblue')

# build and plot coordinates onto map
x,y = m(lons, lats)
m.plot(x, y, 'D', markersize = 5)
plt.title("2D Balloon Trajectory")
plt.savefig('2D-trajectory.png', format = 'png', dpi = 500)
plt.show()