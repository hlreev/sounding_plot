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
__version__ = '0.9.1-pre'
__maintainer__ = 'Hunter L Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'
__lastUpdated__ = '2022-10-30'

# Takes in level2 *.csv data and reads it into a pandas dataframe
def readData():
    # Local imports
    import pandas as pd
    # Read in data for usage
    path = "data/level1/"
    ext = ".csv"
    filename = input("\nPlease enter the name of the sounding you want to plot (edt_YYYYMMDD_HHMM): ")
    data = pd.read_csv(path + filename + ext)
    print("\nPlotting data... this may take a second or two.")
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
        icon = fm.Icon(color = "darkblue", icon_color = "white", icon = "glyphicon glyphicon-home")
    ).add_to(sounding_plot)
    # Return: basemap
    return sounding_plot

# Takes in base data and then parses the data in the pandas dataframe for plotting onto the basemap
def parseData(data):
    # Obtain and organize the data for the locations of balloon data
    altitudes = data['GpsHeightMSL']
    altitudeList = altitudes.values.tolist() # Use for altitudes
    locations = data[['Lat', 'Lon']]
    locationList = locations.values.tolist() # Use for locations
    pressures = data['P']
    pressureList = pressures.values.tolist() # Use for pressure heights
    # Return: parsed data
    return locationList, altitudeList, pressureList

# Takes in the parsed data and base map and then plots the parsed data onto the folium basemap
def plotData(locationList, altitudeList, pressureList, sounding_plot):
    # Get the size of the list of locations for index information
    size = len(locationList)
    # Flags to check if pressure level has been reached
    flags = {
        '925mb': False,
        '850mb': False,
        '700mb': False,
        '500mb': False,
        '400mb': False,
        '300mb': False,
        '250mb': False,
        '200mb': False,
        '150mb': False,
        '100mb': False,
        '70mb': False,
        '50mb': False,
        '30mb': False,
        '20mb': False,
        '10mb': False,
    }
    # Mandatory settings
    _color = 'blue'
    _iconcolor = 'white'
    _icon = 'glyphicon glyphicon-star'
    # Cycle through the data and add the balloon data points to the folium map
    for point in range(0, size):
    # Clean up the code for accessing the data later on...
        lats = locationList[point][0] # latitude values from the list
        lons = locationList[point][1] # longitude values from the list
        pres = pressureList[point] # pressure values
        alts = altitudeList[point] # altitude values
        # Information for each new data point in the plot
        _location = (str(lats) + '°N, ' + str(lons) + '°W, ' + str(pres) + 'mb, ' + str(alts) + 'm')
        # Plot the ascending balloon data points
        if flags['925mb'] == False:
            # Sounding made it to 925mb
            if pressureList[point] == 925.0 or (pressureList[point] > 924 and pressureList[point] < 925):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon )
                ).add_to(sounding_plot)
                # Debug message
                print('925mb reached')
                # 925mb reached, no longer need to plot this point
                flags['925mb'] = True
        elif flags['850mb'] == False:
            # Sounding made it to 850mb
            if pressureList[point] == 850.0 or (pressureList[point] > 849 and pressureList[point] < 850):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon )
                ).add_to(sounding_plot)
                # Debug message
                print('850mb reached')
                # 850mb reached, no longer need to plot this point
                flags['850mb'] = True
        elif flags['700mb'] == False:
            # Sounding made it to 700mb
            if pressureList[point] == 700.0 or (pressureList[point] > 699 and pressureList[point] < 700):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('700mb reached')
                # 700mb reached, no longer need to plot this point
                flags['700mb'] = True
        elif flags['500mb'] == False:
            # Sounding made it to 500mb
            if pressureList[point] == 500.0 or (pressureList[point] > 499 and pressureList[point] < 500):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('500mb reached')
                # 500mb reached, no longer need to plot this point
                flags['500mb'] = True
        elif flags['400mb'] == False:
            # Sounding successful to 400mb, within a typical altitude range of this pressure height
            if pressureList[point] == 400.0 or (pressureList[point] > 399 and pressureList[point] < 400):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Successful to 400mb",
                icon = fm.Icon(color = "green", icon_color = _iconcolor, icon = "glyphicon glyphicon-ok")
                ).add_to(sounding_plot)
                # Debug message
                print('400mb reached')
                # 400mb reached, no longer need to plot successful points
                flags['400mb'] = True
        elif flags['300mb'] == False:
            # Sounding made it to 300mb
            if pressureList[point] == 300.0 or (pressureList[point] > 299 and pressureList[point] < 300):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('300mb reached')
                # 300mb reached, no longer need to plot this point
                flags['300mb'] = True
        elif flags['250mb'] == False:
            # Sounding made it to 250mb
            if pressureList[point] == 250.0 or (pressureList[point] > 249 and pressureList[point] < 250):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('250mb reached')
                # 250mb reached, no longer need to plot this point
                flags['250mb'] = True
        elif flags['200mb'] == False:
            # Sounding made it to 200mb
            if pressureList[point] == 200.0 or (pressureList[point] > 199 and pressureList[point] < 200):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('200mb reached')
                # 200mb reached, no longer need to plot this point
                flags['200mb'] = True
        elif flags['150mb'] == False:
            # Sounding made it to 150mb
            if pressureList[point] == 150.0 or (pressureList[point] > 149 and pressureList[point] < 150):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('150mb reached')
                # 150mb reached, no longer need to plot this point
                flags['150mb'] = True
        elif flags['100mb'] == False:
            # Sounding made it to 100mb
            if pressureList[point] == 100.0 or (pressureList[point] > 99 and pressureList[point] < 100):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('100mb reached')
                # 100mb reached, no longer need to plot this point
                flags['100mb'] = True
        elif flags['70mb'] == False:
            # Sounding made it to 70mb
            if pressureList[point] == 70.0 or (pressureList[point] > 69 and pressureList[point] < 70):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Messages Sent!",
                icon = fm.Icon(color = 'cadetblue', icon_color = _iconcolor, icon = "glyphicon glyphicon-envelope")
                ).add_to(sounding_plot)
                # Debug message
                print('70mb reached')
                # 70mb reached, no longer need to plot this point
                flags['70mb'] = True
        elif flags['50mb'] == False:
            # Sounding made it to 50mb
            if pressureList[point] == 50.0 or (pressureList[point] > 49 and pressureList[point] < 50):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('50mb reached')
                # 50mb reached, no longer need to plot this point
                flags['50mb'] = True
        elif flags['30mb'] == False:
            # Sounding made it to 30mb
            if pressureList[point] == 30.0 or (pressureList[point] > 29 and pressureList[point] < 30):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('30mb reached')
                # 30mb reached, no longer need to plot this point
                flags['30mb'] = True
        elif flags['20mb'] == False:
            # Sounding made it to 20mb
            if pressureList[point] == 20.0 or (pressureList[point] > 19 and pressureList[point] < 20):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('20mb reached')
                # 20mb reached, no longer need to plot this point
                flags['20mb'] = True
        elif flags['10mb'] == False:
            # Sounding made it to 10mb
            if pressureList[point] == 10.0 or (pressureList[point] > 9 and pressureList[point] < 10):
                fm.Marker(
                locationList[point], popup = _location, tooltip = "Mandatory Level",
                icon = fm.Icon(color = _color, icon_color = _iconcolor, icon = _icon)
                ).add_to(sounding_plot)
                # Debug message
                print('10mb reached')
                # 10mb reached, no longer need to plot this point
                flags['10mb'] = True
        elif point == (size - 1):
            # Termination location (The last point of the dataset)
            fm.Marker(
            locationList[point], popup = _location, tooltip = "Termination",
            icon = fm.Icon(color = "red", icon_color = _iconcolor, icon = "glyphicon glyphicon-remove-circle")
            ).add_to(sounding_plot)
            print('Termination.')
    # Create the trajectory of the weather balloon
    fm.PolyLine(
        locationList, color = "grey", weight = "4", tooltip = "Balloon Path"
        ).add_to(sounding_plot)
            
# Work with the data, and then plot the sounding data onto the basemap
def main():
    # Function calls for the program to function
    data = readData()
    sounding_plot = createBasemap()
    locationList, altitudeList, pressureList = parseData(data)
    plotData(locationList, altitudeList, pressureList, sounding_plot)
    # Display the map in a web browser
    sounding_plot.save("viewer/sounding_plot_2D.html")

# Run the program
main()