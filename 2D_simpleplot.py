#!/usr/bin/python
#  Author: Hunter L Reeves
#    Date: 10/04/2022
# Purpose: Plots 2D data points of a weather balloon sounding on a simple basemap
#  Github: https://github.com/hlreev/sounding_plot_3D

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
from pyproj import geodesic_version_str
os.environ['PROJ_LIB'] = '/Users/hunlr/anaconda3/envs/cartopy_env/Library/share/proj'

# Read in data for usage
filename = input("\nPlease enter the name of the sounding you want to plot (format: YYYYMMDD_HHz): ")
data = pd.read_csv("data/" + filename + ".csv")
print("Plotting data... this may take a second or two.")

# Parse out the data for usage
lats = data["latitude"]
lons = data["longitude"]
fwd = [32.835088963714874, -97.29794483866789] # coordinates to the fort worth wfo

# How much to zoom from coordinates (in degrees)
lat_zoom_scale = 5
lon_zoom_scale = 10

# Setup the bounding box for the zoom and bounds of the map
bbox = [np.min(fwd[0]) - lat_zoom_scale, np.max(fwd[0]) + lat_zoom_scale,\
        np.min(fwd[1]) - lon_zoom_scale, np.max(fwd[1]) + lon_zoom_scale]

plt.figure(figsize=(12,6))
# Define the projection, scale, the corners of the map, and the resolution.
m = Basemap(projection = 'merc', llcrnrlat = bbox[0], urcrnrlat = bbox[1],\
            llcrnrlon = bbox[2], urcrnrlon = bbox[3], lat_ts = 10, resolution = 'h') # c = crude, l = low, i = intermediate, h = high, f = full

# Draw the world around us
m.fillcontinents(color = '#87d4c3', lake_color = '#c0e3fa') 
m.drawcoastlines()
m.drawcountries(color = '#595757', linewidth = 2)
m.drawstates(color = '#827f7f', linewidth = 1.5)
m.drawcounties()

# Draw parallels, meridians, and color boundaries
m.drawparallels(np.arange(bbox[0] ,bbox[1] ,(bbox[1] - bbox[0]) / 5), labels = [1, 0, 0, 0])
m.drawmeridians(np.arange(bbox[2], bbox[3], (bbox[3] - bbox[2]) / 5), labels = [0, 0 ,0 ,1], rotation = 45)
m.drawmapboundary(fill_color='#87b5d4')

# Build and plot coordinates onto map
x, y = m(fwd[1], fwd[0]) # starting coordinates
lats,lons = m(lons, lats) # sounding coordinates
m.plot(x, y, marker = '*', color = '#ffea00', markersize = 12)
m.plot(lats, lons, marker = '^', color = '#ed5a5a', markersize = 4)
plt.title("2D Balloon Trajectory")
plt.savefig('images/2D/' + filename + '.png', format = "png", dpi = 500)
print("\nSuccess! Here is your plotted sounding data.")
plt.show()