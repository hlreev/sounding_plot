#!/usr/bin/python
#  Author: Hunter L Reeves
#    Date: 10/05/2022
# Purpose: Plots 2D data points of a weather balloon on an advanced map with streeview data
#  Github: https://github.com/hlreev/sounding_plot_3D
 
from json import tool
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

# Create the base map
fwd = [32.834885591464165, -97.29878202159327] # coordinates to the fort worth wfo
sounding_plot = folium.Map(location = fwd,  zoom_start = 18, control_scale = True, tiles = None)

# Add some additional map layers
folium.TileLayer('openstreetmap', name = "OpenStreetMap").add_to(sounding_plot)
folium.TileLayer('cartodbpositron', name = "CartoDB Positron").add_to(sounding_plot)
folium.TileLayer('cartodbdark_matter', name = "CartoDB DarkMatter").add_to(sounding_plot)
folium.LayerControl().add_to(sounding_plot)

# Release point for the balloon and location of FWD office
upperair = [32.835088963714874, -97.29794483866789] # coordinates to the upper air bldg
_location = "Latitude: " + str(upperair[0]) + ", Longitude: " + str(upperair[1])
folium.Marker(
    upperair, popup = _location, tooltip = "FWD Upper Air", 
    icon = folium.Icon(color = "darkblue", icon_color = "white", icon = "glyphicon glyphicon-star")
).add_to(sounding_plot)

# Obtain and organize the data for the locations of balloon data
altitudes = data["geometric_altitude"]
altitudeList = altitudes.values.tolist() # Use for altitudes
locations = data[['latitude', 'longitude']]
locationList = locations.values.tolist() # Use for locations

# Cycle through the data and add the balloon data points to the folium map
size = len(locationList)
for point in range(0, size):
    # Clean up the code for accessing the data later on...
    lats = locationList[point][0]
    lons = locationList[point][1]
    alts = altitudeList[point]
    # New location message
    _location = ("Lat. (°N): " + str(lats) + 
                 ", Lon. (°E): " + str(lons) + 
                 ", Alt. (m): " + str(alts))
    # Plot the ascending balloon data points
    folium.Marker(
        locationList[point], popup = _location, tooltip = "Ascending Balloon",
        icon = folium.Icon(color = "blue", icon_color = "white", icon = "glyphicon glyphicon-arrow-up")
        ).add_to(sounding_plot)
    # Sounding successful to 400mb
    if point == (size - 4): # fix hardcore lol this is for testing
        folium.Marker(
        locationList[point], popup = _location, tooltip = "Successful to 400mb",
        icon = folium.Icon(color = "green", icon_color = "white", icon = "glyphicon glyphicon-ok")
        ).add_to(sounding_plot)
    # Termination location
    if point == (size - 1):
        folium.Marker(
        locationList[point], popup = _location, tooltip = "Termination",
        icon = folium.Icon(color = "red", icon_color = "white", icon = "glyphicon glyphicon-remove-circle")
        ).add_to(sounding_plot)

# Create the trajectory of the weather balloon
folium.PolyLine(
    locationList, color = "lightblue", weight = "6", tooltip = "Balloon Path"
    ).add_to(sounding_plot)

# Display the map in a web browser
sounding_plot.save("viewer/sounding_plot_2D.html")