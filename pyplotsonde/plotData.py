'''
Plots 2D data points of a weather balloon on an advanced map with streeview data

Repo: https://github.com/hlreev/sounding_plot

Version History can be found in VERSIONS.md
'''

# Global imports
import os
import pandas as pd
import folium as fm
from folium.plugins import FloatImage

# Metadata
__author__ = 'Hunter L Reeves'
__license__ = 'GPL3'
__maintainer__ = 'Hunter L Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'

# Global Settings for plotted points
_color = 'blue'
_icon = 'glyphicon glyphicon-star'
_iconcolor = 'white'
# Styles for the Backup Offices
_polyColor = {'fillColor': '#00ddff', 'color': '#adaaaa'}
# For file management
_csvPath = "C:\\Users\\hunlr\\Desktop\\sounding_plot\\data\\level1\\"
_jsonPath = "C:\\Users\\hunlr\\Desktop\\sounding_plot\\data\\geojson\\"
# Static Images for plotting
_compassRose = ("C:\\Users\\hunlr\\Desktop\\sounding_plot\\images\\rose.png")

# Check for sections of missing data points (if difference is greater than 1, there is missing data!)
def checkMissingData(currentPoint, previousPoint):
    # Return - the absolute difference between the two point indexes in question
    return abs((currentPoint) - (previousPoint))

# Plots the first valid point for each mandatory level on the sounding
def plotMandatoryPoints(index, pressureList, locationList, info, point, previousPoint, sounding_plot, _flags, currentFile):
    # Plot the ascending balloon data points
    if _flags['925mb'] == False:
        # Sounding made it to 925mb
        if pressureList[index] == 925.0 or (pressureList[index] >= 924.0 and pressureList[index] <= 926.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon )
            ).add_to(sounding_plot)
            _flags['925mb'] = True
    elif _flags['850mb'] == False:
        # Sounding made it to 850mb
        if pressureList[index] == 850.0 or (pressureList[index] >= 849.0 and pressureList[index] <= 851.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon )
            ).add_to(sounding_plot)
            _flags['850mb'] = True
    elif _flags['700mb'] == False:
        # Sounding made it to 700mb
        if pressureList[index] == 700.0 or (pressureList[index] >= 699.0 and pressureList[index] <= 701.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['700mb'] = True
    elif _flags['500mb'] == False:
        # Sounding made it to 500mb
        if pressureList[index] == 500.0 or (pressureList[index] >= 499.0 and pressureList[index] <= 501.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['500mb'] = True
    elif _flags['400mb'] == False:
        # Sounding successful to 400mb, within a typical altitude range of this pressure height
        if pressureList[index] == 400.0 or (pressureList[index] >= 399.0 and pressureList[index] <= 401.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Successful to 400mb",
            icon = fm.Icon(color = "green", icon_color = _iconcolor, icon = "glyphicon glyphicon-ok")
            ).add_to(sounding_plot)
            _flags['400mb'] = True
    elif _flags['300mb'] == False:
        # Sounding made it to 300mb
        if pressureList[index] == 300.0 or (pressureList[index] >= 299.0 and pressureList[index] <= 301.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['300mb'] = True
    elif _flags['250mb'] == False:
        # Sounding made it to 250mb
        if pressureList[index] == 250.0 or (pressureList[index] >= 249.0 and pressureList[index] <= 251.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['250mb'] = True
    elif _flags['200mb'] == False:
        # Sounding made it to 200mb
        if pressureList[index] == 200.0 or (pressureList[index] >= 199.0 and pressureList[index] <= 201.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['200mb'] = True
    elif _flags['150mb'] == False:
        # Sounding made it to 150mb
        if pressureList[index] == 150.0 or (pressureList[index] >= 149.0 and pressureList[index] <= 151.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['150mb'] = True
    elif _flags['100mb'] == False:
        # Sounding made it to 100mb
        if pressureList[index] == 100.0 or (pressureList[index] >= 99.0 and pressureList[index] <= 101.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['100mb'] = True
    elif _flags['70mb'] == False:
        # Sounding made it to 70mb
        if pressureList[index] == 70.0 or (pressureList[index] >= 69.0 and pressureList[index] <= 71.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Messages Sent!",
            icon = fm.Icon(color = 'cadetblue', icon_color = _iconcolor, icon = "glyphicon glyphicon-envelope")
            ).add_to(sounding_plot)
            _flags['70mb'] = True
    elif _flags['50mb'] == False:
        # Sounding made it to 50mb
        if pressureList[index] == 50.0 or (pressureList[index] >= 29.0 and pressureList[index] <= 51.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['50mb'] = True
    elif _flags['30mb'] == False:
        # Sounding made it to 30mb
        if pressureList[index] == 30.0 or (pressureList[index] >= 29.0 and pressureList[index] <= 31.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['30mb'] = True
    elif _flags['20mb'] == False:
        # Sounding made it to 20mb
        if pressureList[index] == 20.0 or (pressureList[index] >= 19.0 and pressureList[index] <= 21.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['20mb'] = True
    elif _flags['10mb'] == False:
        # Sounding made it to 10mb
        if pressureList[index] == 10.0 or (pressureList[index] >= 9.0 and pressureList[index] <= 11.0):
            fm.Marker(
            locationList[index], popup = info, tooltip = "Mandatory Level",
            icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
            ).add_to(sounding_plot)
            _flags['10mb'] = True
    # This checks the absolute difference between the current and previous point, if its greater than 1 - its missing data there!
    if checkMissingData(point, previousPoint) != 1 and point != 9998: # Do not include the termination point
        # Message to console
        print('WARNING: Missing data found at ' + str(pressureList[previousPoint]) + 'mb in \'' + currentFile + '\'.')
    elif point == 9998:
        # Termination location (The last point of the dataset)
        fm.Marker(
        locationList[index], popup = info, tooltip = "Termination",
        icon = fm.Icon(color = "red", icon_color = _iconcolor, icon = "glyphicon glyphicon-remove-circle")
        ).add_to(sounding_plot)

# Takes in the parsed data and base map and then plots the parsed data onto the folium basemap
def plotData(locationList, pressureList, pointsList, sounding_plot, _flags, currentFile):
    # Get the size of the list of locations for index information
    size = len(locationList)
    # Cycle through the data and add the balloon data points to the folium map
    for index in range(0, size):
        # Points for keeping track of termination
        point = pointsList[index]
        # Check for initializing the previous point at the start (there is no point before 1...)
        if point == 1:
            # Set previous point to -1, otherwise it would be 9998...
            previousPoint = 0
        else:
            # Previous points for keeping track of missing data
            previousPoint = pointsList[index - 1]
        # Information for each new data point in the plot
        info = (str(pressureList[index]) + 'mb')
        # Plot mandatory points on the sounding
        plotMandatoryPoints(index, pressureList, locationList, info, point, previousPoint, sounding_plot, _flags, currentFile)
    # Create the trajectory of the weather balloon
    fm.PolyLine(
        locationList, color = "grey", weight = "4").add_to(sounding_plot)

# Takes in base data and then parses the data in the pandas dataframe for plotting onto the basemap
def parseData(data):
    # Obtain and organize the data for the locations of balloon data 
    locations = data[['Lat', 'Lon']]
    locationList = locations.values.tolist() # Use for locations
    pressures = data['P']
    pressureList = pressures.values.tolist() # Use for pressure heights
    points = data['n'] 
    pointsList = points.values.tolist() # Use for data point count
    # Return: parsed data
    return locationList, pressureList, pointsList

# Creates a basemap with folium and some starting points for the FWD office and upper-air building
def createBasemap():
    # Create the base map
    fwd = [32.8350, -97.2986] # coordinates to the fort worth wfo
    sounding_plot = fm.Map(location = fwd,  zoom_start = 15, control_scale = True, tiles = None)
    # Adds the county polygons for the FWD CWA from a geojson file
    fm.GeoJson(_jsonPath + 'FWD.geojson', name = 'Fort Worth CWA').add_to(sounding_plot)
    # Add the backup office polygon CWAs from geojson files
    fm.GeoJson(_jsonPath + 'SHV.geojson', name = 'Shreveport CWA', show = False, style_function = lambda x:_polyColor).add_to(sounding_plot)
    fm.GeoJson(_jsonPath + 'OUN.geojson', name = 'Norman CWA', show = False, style_function = lambda x:_polyColor).add_to(sounding_plot)
    fm.GeoJson(_jsonPath + 'OHX.geojson', name = 'Nashville CWA', show = False, style_function = lambda x:_polyColor).add_to(sounding_plot)
    # Add some additional map layers
    fm.TileLayer('openstreetmap', name = "OpenStreetMap").add_to(sounding_plot)
    fm.TileLayer('cartodbpositron', name = "CartoDB Positron").add_to(sounding_plot)
    fm.TileLayer('stamentoner', name = "Stamen Toner").add_to(sounding_plot)
    fm.TileLayer('stamenwatercolor', name = "Stamen Watercolor").add_to(sounding_plot)
    # Add a static rose compass to the bottom right of the plotted map
    FloatImage(_compassRose, bottom = 2, left = 89).add_to(sounding_plot)
    # Add the tile layer control
    fm.LayerControl().add_to(sounding_plot)
    # Adds the release point for the balloon and location of FWD office (upper air building)
    upperair = [32.83508, -97.29794]
    _location = "Latitude: " + str(upperair[0]) + ", Longitude: " + str(upperair[1])
    fm.Marker(upperair, popup = _location, tooltip = "FWD Upper Air", icon = fm.Icon(color = "darkblue", icon_color = "white", icon = "glyphicon glyphicon-home")).add_to(sounding_plot)
    # Return: basemap
    return sounding_plot

# Takes in level1 *.csv data and reads it into a pandas dataframe
def readData(currentFile):
    # Data for reading files in the level1 directory
    fileName = _csvPath + currentFile
    # Open the csv file and return the data for plotting
    data = pd.read_csv(fileName)
    # Return: base data
    return data, currentFile

# Generate each sounding plot
def generatePlots(files, _flags):
    # Go through each *.csv file and plot the data on a new html page
    for currentFile in files:
        # Function calls for the program to function
        data, file = readData(currentFile)
        sounding_plot = createBasemap()
        locationList, pressureList, pointsList = parseData(data)
        # Check if sounding data made it beyond 400mb (was successful ~1500 points)
        if len(data) >= 1500:
            # Plot the data
            plotData(locationList, pressureList, pointsList, sounding_plot, _flags, currentFile)
            # Clean up the name and then save the html file in the directory
            removeFront = file.replace('edt_', '')
            cleanedName = removeFront.replace('.csv', '')
            # Save each sounding plot
            sounding_plot.save('viewer/' + cleanedName + '.html')
            # Message to console
            print(currentFile + " has been saved.")
            # Reset flags to plot the mandatory levels for the next plot
            _flags = {flag: False for flag in _flags}
        # Not enough data for successful release!
        else:
            print('ERROR: The radiosonde data in \'' + currentFile + '\' was not successful to 400mb. The data will not be plotted.')

# Looks through the level1 files to obtain the filename and the count
def findFiles():
    # List of files that need to be read in
    filenames = []
    # Iterate over all the files in the directory, store into list
    for name in os.listdir(_csvPath):
        # Add the file and increment the counter
        filenames.append(name)
    # Return: read files that need to be processed and the size of the files read in
    return filenames
            
# Bulk of code is ran here
def main():
    # Flags to check if pressure level has been reached
    _flags = { '925mb': False, '850mb': False, '700mb': False, '500mb': False, '400mb': False, 
               '300mb': False, '250mb': False, '200mb': False, '150mb': False, '100mb': False,
                '70mb': False,  '50mb': False,  '30mb': False,  '20mb': False,  '10mb': False }
    # Obtain the file names for use later when saving the plots
    files = findFiles()
    # Message for the console
    print('\nPath: ' + _csvPath + ' | Files found: ' + str(len(files)) + '\n')
    # Generate each soudning plot - bulk of the code is executed here
    generatePlots(files, _flags)
    # Check if there are files in the level1 directory
    if len(files) != 0:
        # Print the message for debugging at the end of the program running
        print("\nThe soundings have been plotted. It can be viewed in the browser from the '/viewer/' directory.")
    else:
        # No files found!
        print('ERROR: No files were found in the /level1/ directory.')

# Run the program
main()