#  Author: Hunter L Reeves
#    Date: 10/19/2022
# Purpose: Takes level 0 data and converts it to level 1/level 2 data
#  Github: https://github.com/hlreev/sounding_plot_3D

# Imports for bash command usage
import subprocess

# Takes level 0 data (*.mwx) and processes it into level 1 data (*.nc)
def processLevel0():
    # The necessary command - for testing, NOT YET USABLE FOR RS41-NG SONDES
    bashCommand = "sounding_converter.exe -i data/level0/BCO_20200126_224454.mwx -o data/level1/BCO_20200126_224454.nc -c 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\config\\main.yaml'"
    process = subprocess.Popen(bashCommand.split(), stdout = subprocess.PIPE)
    output, error = process.communicate()
    # All is said and done
    return output, error

# Takes level 1 data (*.nc) and processes it into level 2 data (*.csv)
def processLevel1():
    # Local imports for *.nc files
    import numpy as np
    import netCDF4 as nc
    # Open the file
    path = "data/level1/"
    ext = ".nc"
    filename = input("\nPlease enter the name of the NetCDF file you want to process: ")
    ncfile = path + filename + ext
    print(ncfile)
    # Print out success message
    message = "Level 1 data successfully processed! \n\nThe Level 2 data has been saved in 'data/level2/*.csv'."
    # All is said and done
    return message

# Initialize main
def main():
    # Process level 0 data (*.mwx to *.nc)
    output, error = processLevel0()
    print("\nLevel 1 Output: " + str(output), "Error: " + str(error))
    # Process level 1 data (*.nc to *.mwx)
    message = processLevel1()
    print("Level 2 Output: " + str(message))

main()