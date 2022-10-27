#  Author: Hunter L Reeves
#    Date: 10/19/2022
# Purpose: Plots 2D data points of a weather balloon on an advanced map with streeview data
#  Github: https://github.com/hlreev/sounding_plot_3D

# Global imports
import folium as fm
from netCDF4 import Dataset

# Takes in level2 *.csv data and reads it into a pandas dataframe
def readData():
    # Local imports
    import pandas as pd
    # Read in data for usage
    path = "data/level2/old/"
    ext = ".csv"
    filename = input("\nPlease enter the name of the sounding you want to plot (format: YYYYMMDD_HHz): ")
    data = pd.read_csv(path + filename + ext) # DELETEME - debug/testing
    print("Plotting data... this may take a second or two.")
    # Return: base data
    return data

# Creates a basemap with folium and some starting points for the FWD office and upper-air building
def createBasemap():
    # Create the base map
    fwd = [32.8350, -97.2986] # coordinates to the fort worth wfo
    sounding_plot = fm.Map(location = fwd,  zoom_start = 18, control_scale = True, tiles = False)
    # Add some additional map layers
    fm.TileLayer('openstreetmap', name = "OpenStreetMap").add_to(sounding_plot)
    fm.TileLayer('cartodbpositron', name = "CartoDB Positron").add_to(sounding_plot)
    fm.TileLayer('cartodbdark_matter', name = "CartoDB DarkMatter").add_to(sounding_plot)
    fm.LayerControl().add_to(sounding_plot)
    # Release point for the balloon and location of FWD office
    upperair = [32.83508, -97.29794] # coordinates to the upper air bldg
    _location = "Latitude: " + str(upperair[0]) + ", Longitude: " + str(upperair[1])
    fm.Marker(
        upperair, popup = _location, tooltip = "FWD Upper Air", 
        icon = fm.Icon(color = "darkblue", icon_color = "white", icon = "glyphicon glyphicon-star")
    ).add_to(sounding_plot)
    # Return: basemap
    return sounding_plot

# Takes in base data and then parses the data in the pandas dataframe for plotting onto the basemap
def parseData(data):
    # Obtain and organize the data for the locations of balloon data
    altitudes = data["raw_geometric_altitude"]
    altitudeList = altitudes.values.tolist() # Use for altitudes
    locations = data[['latitude', 'longitude']]
    locationList = locations.values.tolist() # Use for locations
    # Return: parsed data
    return locationList, altitudeList

# Takes in the parsed data and base map and then plots the parsed data onto the folium basemap
def plotData(locationList, altitudeList, sounding_plot):
    # Get the size of the list of locations for index information
    size = len(locationList)
    # Flag to check if 400mb has been reached
    check400mb = False
    # Cycle through the data and add the balloon data points to the folium map
    for point in range(0, size):
        # Clean up the code for accessing the data later on...
        lats = locationList[point][0] # latitude values from the list
        lons = locationList[point][1] # longitude values from the list
        alts = altitudeList[point] # altitude values
        # Information for each new data point in the plot
        _location = ("Lat. (°N): " + str(lats) + 
                    ", Lon. (°E): " + str(lons) + 
                    ", Alt. (m): " + str(alts))
        # Plot the ascending balloon data points
        fm.Marker(
            locationList[point], popup = _location, tooltip = "Ascending Balloon",
            icon = fm.Icon(color = "blue", icon_color = "white", icon = "glyphicon glyphicon-arrow-up")
            ).add_to(sounding_plot)
        if check400mb == False:
            # Sounding successful to 400mb, within a typical altitude range of this pressure height
            if altitudeList[point] > 7200 and altitudeList[point] < 7600:
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Successful to 400mb",
                icon = fm.Icon(color = "green", icon_color = "white", icon = "glyphicon glyphicon-ok")
                ).add_to(sounding_plot)
                # 400mb reached, no longer need to plot successful points
                check400mb = True
        # Termination location (for now, it is the last data point - not entirely accurate)
        if point == (size - 1):
            fm.Marker(
            locationList[point], popup = _location, tooltip = "Termination",
            icon = fm.Icon(color = "red", icon_color = "white", icon = "glyphicon glyphicon-remove-circle")
            ).add_to(sounding_plot)
        # Create the trajectory of the weather balloon
        fm.PolyLine(
            locationList, color = "lightblue", weight = "6", tooltip = "Balloon Path"
            ).add_to(sounding_plot)

# Work with the data, and then plot the sounding data onto the basemap
def main():
    # Function calls for the program to function
    data = readData()
    sounding_plot = createBasemap()
    locationList, altitudeList = parseData(data)
    plotData(locationList, altitudeList, sounding_plot)
    # Display the map in a web browser
    sounding_plot.save("viewer/sounding_plot_2D.html")

# Run the program
main()