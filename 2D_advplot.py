#!/usr/bin/python
#  Author: Hunter L Reeves
#    Date: 10/04/2022
# Purpose: Plots 2D data points of a weather balloon on an advanced map with streeview data
#  Github: https://github.com/hlreev/sounding_plot_3D
 
from matplotlib.ft2font import FIXED_WIDTH
import matplotlib.pyplot as plt 
import numpy as np
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import io
import pandas as pd
import folium
from folium import plugins
from urllib.request import urlopen, Request
from PIL import Image

# Read in data for usage
filename = input("\nPlease enter the name of the sounding you want to plot (format: YYYYMMDD_HHz): ")
data = pd.read_csv("data/" + filename + ".csv")
print("Plotting data... this may take a second or two.")

# Parse out the data for usage
lats = data["latitude"]
lons = data["longitude"]
alts = data["geometric_altitude"]
fwd = [32.834885591464165, -97.29878202159327] # coordinates to the fort worth wfo
upperair = [32.835088963714874, -97.29794483866789] # coordinates to the upper air bldg

# Create a map using the Map() function
m = folium.Map(location = fwd,  zoom_start = 18)

# Release point for the balloon
tooltip = "Balloon Release Site"
folium.Marker(
    upperair, popup="<i>FWD Upper Air</i>", tooltip=tooltip
).add_to(m)

# Display the map in a web browser
m.save("viewer/sounding-viewer-2D.html")