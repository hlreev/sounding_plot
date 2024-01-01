'''
Plot Data Module

Plots 2D data points of a weather balloon on an advanced map with streetview data
'''

# Imports
import matplotlib.pyplot as plt
import folium as fm

# Modules
from pyplotsonde.file_paths import LEVEL1_DIRECTORY, GEOJSON_PATH, SOUNDING_PATH, COMPASS_ROSE_PATH

# Global Settings
_color = 'blue'
_icon = 'glyphicon glyphicon-star'
_iconcolor = 'white'
_polyColor = {'fillColor': '#00ddff', 'color': '#adaaaa'}

# Location of Fort Worth's NWS Office
_fwd = [32.83488493770296, -97.29873660246302]
_upperair = [32.83508, -97.29794]

# Flag to check for missing data
missingDataFlag = False

def reset_flags(flags):
    """
    Helper Function

    Reset flags for the next plot.
    """

    return {flag: False for flag in flags}

def save_trajectory_html(sounding_plot, cleaned_name):
    """
    Helper Function

    Save the folium map as an HTML file.
    """

    sounding_plot.save('viewer/' + cleaned_name + '.html')

def add_sounding_marker(sounding_plot, current_sounding):
    """
    Helper Function

    Add marker for SkewT sounding to the folium map.
    """

    # Imports
    import base64
    from folium import IFrame

    encoded = base64.b64encode(open(current_sounding, 'rb').read())
    html = '<img src="data:image/png;base64,{}">'.format
    iframe = IFrame(html(encoded.decode('UTF-8')), width = 670, height = 650)
    popup = fm.Popup(iframe, max_width = 800)
    fm.Marker(location = _fwd, tooltip = "Click to show sounding.", popup = popup, icon = fm.Icon(color = 'gray')).add_to(sounding_plot)

def save_skewt_sounding(cleaned_name):
    """
    Helper Function

    Save the SkewT sounding as a PNG file.
    """

    current_sounding = SOUNDING_PATH + cleaned_name + '.png'
    plt.savefig(current_sounding)
    plt.close()

    return current_sounding

def plot_skewt(temp, dewp, pres, cleanedName):
    """
    Helper Function

    Plot the SkewT sounding.
    """
        
    # Imports
    import numpy as np
    from classes.SkewT import register_projection, SkewXAxes

    # Register the projection for the SkewT plot
    register_projection(SkewXAxes)
    # Clean name further for use in title
    soundingName = cleanedName.replace('_', '/')
    # Create a new figure. The dimensions here give a good aspect ratio
    fig = plt.figure(figsize = (6.5875, 6.2125))
    ax = fig.add_subplot(111, projection = "skewx")
    # Add the grid and title
    plt.grid(True, ls = '--')
    plt.title(' FWD ' + soundingName + ' (Observed)', fontsize = 14, loc = 'left')
    # Plot data using the log-p axes
    ax.semilogy(temp, pres, color = 'C3', lw = 2)
    ax.semilogy(dewp, pres, color = 'C2', lw = 2)
    # Disables the log-formatting that comes with semilogy
    ax.yaxis.set_major_formatter(plt.ScalarFormatter())
    ax.set_yticks(np.linspace(100, 1000, 10))
    ax.set_ylim(1050, 100)
    ax.xaxis.set_major_locator(plt.MultipleLocator(10))
    ax.set_xlim(-50, 50)
    # Add lines for 0C and -20C (ice growth region)
    ax.axvline(0, color = 'C0', ls = '--', lw = 1)
    ax.axvline(-20, color = 'C0', ls = '--', lw = 1)

def clean_up_name(file_name):
    """
    Helper Function

    Clean up the name for use in the title.
    """

    remove_front = file_name.replace('edt_', '')

    return remove_front.replace('.csv', '')

def check_missing_data(currentPoint, previousPoint):
    """
    Helper Function

    Checks for missing data by seeing if there was a previous point compared to the current point
    """

    return abs((currentPoint) - (previousPoint))

# Plots the first valid point for each mandatory level on the sounding
def plot_mandatory_points(index, pressureList, locationList, info, point, previousPoint, sounding_plot, _flags, currentFile):
    """
    Helper Function

    Plot mandatory points on the sounding.
    """

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
    if check_missing_data(point, previousPoint) != 1 and point != 9998: # Do not include the termination point
        global missingDataFlag
        # Flag for missing data, only notify user once of missing data (ignore otherwise)
        if missingDataFlag == False:
            # Message to console
            print('\nWARNING: Missing data found in \'' + currentFile + '\'')
            # Trip the missing data flag
            missingDataFlag = True
    elif point == 9998:
        # Termination location (The last point of the dataset)
        fm.Marker(
        locationList[index], popup = info, tooltip = "Termination",
        icon = fm.Icon(color = "red", icon_color = _iconcolor, icon = "glyphicon glyphicon-remove-circle")
        ).add_to(sounding_plot)

def plot_trajectory(location_list, pressure_list, points_list, sounding_plot, flags, current_file):
    """
    Helper Functionc

    Plot the balloon trajectory on the folium map.
    """

    size = len(location_list)
    for index in range(0, size):
        point = points_list[index]
        if point == 1:
            previous_point = 0
        else:
            previous_point = points_list[index - 1]
        info = str(pressure_list[index]) + 'mb'
        plot_mandatory_points(index, pressure_list, location_list, info, point, previous_point, sounding_plot, flags, current_file)

    fm.PolyLine(location_list, color = "grey", weight = "4").add_to(sounding_plot)

def parse_data(data):
    """
    Helper Function

    Parse data into required format for plotting.
    """

    locations = data[['Lat', 'Lon']]
    location_list = locations.values.tolist()
    pressures = data['P']
    pressure_list = pressures.values.tolist()
    points = data['n']
    points_list = points.values.tolist()
    temp = data['Temp']
    dewp = data['Dewp']
    pres = data['P']

    return location_list, pressure_list, points_list, temp, dewp, pres

def create_basemap():
    """
    Helper Function

    Create the base map using folium.
    """

    # Imports
    from folium.plugins import FloatImage

    # Create the base map
    sounding_plot = fm.Map(location = _fwd,  zoom_start = 15, control_scale = True, tiles = None)
    # Adds the county polygons for the FWD CWA from a geojson file
    fm.GeoJson(GEOJSON_PATH + 'FWD.geojson', name = 'Fort Worth CWA').add_to(sounding_plot)
    # Add the backup office polygon CWAs from geojson files
    fm.GeoJson(GEOJSON_PATH + 'SHV.geojson', name = 'Shreveport CWA', show = False, style_function = lambda x:_polyColor).add_to(sounding_plot)
    fm.GeoJson(GEOJSON_PATH + 'OUN.geojson', name = 'Norman CWA', show = False, style_function = lambda x:_polyColor).add_to(sounding_plot)
    fm.GeoJson(GEOJSON_PATH + 'OHX.geojson', name = 'Nashville CWA', show = False, style_function = lambda x:_polyColor).add_to(sounding_plot)
    # Add some additional map layers
    fm.TileLayer('openstreetmap', name = "OpenStreetMap").add_to(sounding_plot)
    fm.TileLayer('cartodbpositron', name = "CartoDB Positron").add_to(sounding_plot)
    # Add a static rose compass to the bottom right of the plotted map
    FloatImage(COMPASS_ROSE_PATH, bottom = 2, left = 89).add_to(sounding_plot)
    # Add the tile layer control
    fm.LayerControl().add_to(sounding_plot)
    # Adds the release point for the balloon and location of FWD office (upper air building)
    _location = "Latitude: " + str(_upperair[0]) + ", Longitude: " + str(_upperair[1])
    fm.Marker(_upperair, popup = _location, tooltip = "FWD Upper Air", icon = fm.Icon(color = "darkblue", icon_color = "white", icon = "glyphicon glyphicon-home")).add_to(sounding_plot)

    return sounding_plot

def read_data(current_file):
    """
    Helper Function

    Read *.csv file and return data.
    """

    # Imports
    import pandas as pd

    file_path = LEVEL1_DIRECTORY + current_file
    data = pd.read_csv(file_path)

    return data, current_file

def generate_plots(files, flags, progress_bar):
    """
    Helper Function

    Generate plots for each *.csv file.
    """

    for current_file in files:
        data, file_name = read_data(current_file)
        sounding_plot = create_basemap()
        location_list, pressure_list, points_list, temp, dewp, pres = parse_data(data)

        if len(data) >= 1500:
            plot_trajectory(location_list, pressure_list, points_list, sounding_plot, flags, current_file)
            cleaned_name = clean_up_name(file_name)
            plot_skewt(temp, dewp, pres, cleaned_name)
            current_sounding = save_skewt_sounding(cleaned_name)
            add_sounding_marker(sounding_plot, current_sounding)
            save_trajectory_html(sounding_plot, cleaned_name)
            progress_bar.next()
            flags = reset_flags(flags)
        else:
            print(f'\nERROR: The radiosonde data in \'{current_file}\' was not successful to 400mb. The data will not be plotted.')