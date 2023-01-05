'''
Plots 2D data points of a weather balloon on an advanced map with streeview data

Repo: https://github.com/hlreev/sounding_plot_3D

Version History can be found in VERSIONS.md
'''

# Global imports
import folium as fm

# Metadata
__author__ = 'Hunter L Reeves'
__license__ = 'GPL3'
__version__ = '0.9.4-pre'
__maintainer__ = 'Hunter L Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'
__lastUpdated__ = '2023-01-05'

# Global Settings for plotted points
_color = 'blue'
_icon = 'glyphicon glyphicon-star'
_iconcolor = 'white'
# Flags to check if pressure level has been reached
flags = { '925mb': False, '850mb': False, '700mb': False, '500mb': False, '400mb': False, 
          '300mb': False, '250mb': False, '200mb': False, '150mb': False, '100mb': False,
           '70mb': False,  '50mb': False,  '30mb': False,  '20mb': False,  '10mb': False, }

# Plots the first valid point for each mandatory level on the sounding
def plotMandatoryPoint(index, pressureList, locationList, info, points, size, sounding_plot):
    # Plot the ascending balloon data points
    if flags['925mb'] == False:
        # Sounding made it to 925mb
        if pressureList[index] == 925.0 or (pressureList[index] > 924 and pressureList[index] < 925):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon )
            ).add_to(sounding_plot)
            # 925mb reached, no longer need to plot this index
            flags['925mb'] = True
    elif flags['850mb'] == False:
        # Sounding made it to 850mb
        if pressureList[index] == 850.0 or (pressureList[index] > 849 and pressureList[index] < 850):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon )
            ).add_to(sounding_plot)
            # 850mb reached, no longer need to plot this index
            flags['850mb'] = True
    elif flags['700mb'] == False:
        # Sounding made it to 700mb
        if pressureList[index] == 700.0 or (pressureList[index] > 699 and pressureList[index] < 700):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 700mb reached, no longer need to plot this index
            flags['700mb'] = True
    elif flags['500mb'] == False:
        # Sounding made it to 500mb
        if pressureList[index] == 500.0 or (pressureList[index] > 499 and pressureList[index] < 500):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 500mb reached, no longer need to plot this index
            flags['500mb'] = True
    elif flags['400mb'] == False:
        # Sounding successful to 400mb, within a typical altitude range of this pressure height
        if pressureList[index] == 400.0 or (pressureList[index] > 399 and pressureList[index] < 400):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Successful to 400mb",
            icon = fm.Icon(color = "green", icon_color = _iconcolor, icon = "glyphicon glyphicon-ok")
            ).add_to(sounding_plot)
            # 400mb reached, no longer need to plot successful indexs
            flags['400mb'] = True
    elif flags['300mb'] == False:
        # Sounding made it to 300mb
        if pressureList[index] == 300.0 or (pressureList[index] > 299 and pressureList[index] < 300):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 300mb reached, no longer need to plot this index
            flags['300mb'] = True
    elif flags['250mb'] == False:
        # Sounding made it to 250mb
        if pressureList[index] == 250.0 or (pressureList[index] > 249 and pressureList[index] < 250):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 250mb reached, no longer need to plot this index
            flags['250mb'] = True
    elif flags['200mb'] == False:
        # Sounding made it to 200mb
        if pressureList[index] == 200.0 or (pressureList[index] > 199 and pressureList[index] < 200):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 200mb reached, no longer need to plot this index
            flags['200mb'] = True
    elif flags['150mb'] == False:
        # Sounding made it to 150mb
        if pressureList[index] == 150.0 or (pressureList[index] > 149 and pressureList[index] < 150):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 150mb reached, no longer need to plot this index
            flags['150mb'] = True
    elif flags['100mb'] == False:
        # Sounding made it to 100mb
        if pressureList[index] == 100.0 or (pressureList[index] > 99 and pressureList[index] < 100):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 100mb reached, no longer need to plot this index
            flags['100mb'] = True
    elif flags['70mb'] == False:
        # Sounding made it to 70mb
        if pressureList[index] == 70.0 or (pressureList[index] > 69 and pressureList[index] < 70):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Messages Sent!",
            icon = fm.Icon(color = 'cadetblue', icon_color = _iconcolor, icon = "glyphicon glyphicon-envelope")
            ).add_to(sounding_plot)
            # 70mb reached, no longer need to plot this index
            flags['70mb'] = True
    elif flags['50mb'] == False:
        # Sounding made it to 50mb
        if pressureList[index] == 50.0 or (pressureList[index] > 49 and pressureList[index] < 50):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 50mb reached, no longer need to plot this index
            flags['50mb'] = True
    elif flags['30mb'] == False:
        # Sounding made it to 30mb
        if pressureList[index] == 30.0 or (pressureList[index] > 29 and pressureList[index] < 30):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 30mb reached, no longer need to plot this index
            flags['30mb'] = True
    elif flags['20mb'] == False:
        # Sounding made it to 20mb
        if pressureList[index] == 20.0 or (pressureList[index] > 19 and pressureList[index] < 20):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 20mb reached, no longer need to plot this index
            flags['20mb'] = True
    elif flags['10mb'] == False:
        # Sounding made it to 10mb
        if pressureList[index] == 10.0 or (pressureList[index] > 9 and pressureList[index] < 10):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            # 10mb reached, no longer need to plot this index
            flags['10mb'] = True
    elif points == 9998 or (index == (size - 1)):
        # Termination location (The last point of the dataset)
        fm.Marker(
        locationList[index], popup = info, tooltip = "Termination",
        icon = fm.Icon(color = "red", icon_color = _iconcolor, icon = "glyphicon glyphicon-remove-circle")
        ).add_to(sounding_plot)

# Takes in the parsed data and base map and then plots the parsed data onto the folium basemap
def plotData(locationList, altitudeList, pressureList, pointsList, sounding_plot):
    # Get the size of the list of locations for index information
    size = len(locationList)
    # Cycle through the data and add the balloon data points to the folium map
    for index in range(0, size):
        # Points for keeping track of termination
        points = pointsList[index]
        # Information for each new data point in the plot
        info = (str(locationList[index][0]) + '°N, ' + str(locationList[index][1]) + '°W, ' + str(pressureList[index]) + 'mb, ' + str(altitudeList[index]) + 'm')
        # Plot mandatory points on the sounding
        plotMandatoryPoint(index, pressureList, locationList, info, points, size, sounding_plot)
    # Create the trajectory of the weather balloon
    fm.PolyLine(
        locationList, color = "grey", weight = "4", tooltip = "Balloon Path"
        ).add_to(sounding_plot)

# Takes in base data and then parses the data in the pandas dataframe for plotting onto the basemap
def parseData(data):
    # Obtain and organize the data for the locations of balloon data
    altitudes = data['GpsHeightMSL']
    altitudeList = altitudes.values.tolist() # Use for altitudes
    locations = data[['Lat', 'Lon']]
    locationList = locations.values.tolist() # Use for locations
    pressures = data['P']
    pressureList = pressures.values.tolist() # Use for pressure heights
    points = data['n'] 
    pointsList = points.values.tolist() # Use for data point count
    # Return: parsed data
    return locationList, altitudeList, pressureList, pointsList

# Creates a basemap with folium and some starting points for the FWD office and upper-air building
def createBasemap():
    # Create the base map
    fwd = [32.8350, -97.2986] # coordinates to the fort worth wfo
    sounding_plot = fm.Map(location = fwd,  zoom_start = 10, control_scale = True, tiles = False)
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
        icon = fm.Icon(color = "darkblue", icon_color = "white", icon = "glyphicon glyphicon-home")
    ).add_to(sounding_plot)
    # Return: basemap
    return sounding_plot

# Takes in level2 *.csv data and reads it into a pandas dataframe
def readData():
    # Local imports
    import pandas as pd
    # Read in data for usage
    path = "data/level1/"
    ext = ".csv"
    filename = input("\nPlease enter the date and time of the sounding you want to plot (YYYYMMDD_HHMM): ")
    data = pd.read_csv(path + 'edt_' + filename + ext)
    # Return: base data
    return data
            
# Work with the data, and then plot the sounding data onto the basemap
def main():
    # Function calls for the program to function
    data = readData()
    sounding_plot = createBasemap()
    locationList, altitudeList, pressureList, pointsList = parseData(data)
    # Plot the data
    plotData(locationList, altitudeList, pressureList, pointsList, sounding_plot)
    # Print the message for debugging at the end of the program running
    print("\nSounding has been plotted. It can be viewed in the browser from '/viewer/sounding_plot.html'.")
    # Display the map in a web browser
    sounding_plot.save("viewer/sounding_plot.html")

# Run the program
main()