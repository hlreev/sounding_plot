'''
Takes the raw EDT message files and converts them to readable *.csv files

Repo: https://github.com/hlreev/sounding_plot_3D

Version History can be found in VERSIONS.md
'''

# Global imports
import os
import pandas as pd

# Metadata
__author__ = 'Hunter L Reeves'
__license__ = 'GPL3'
__version__ = '0.8.0-pre'
__maintainer__ = 'Hunter L Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'
__lastUpdated__ = '2022-10-29'

# Looks through the level0 data for later reading and conversion
def findLevel0Files():
    # Open directory where all level 0 data is (*.txt)
    path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level0\\'
    # File extension (*.txt)
    ext = ('.txt')
    # List of files that need to be read in
    level0 = []
    # Iterate over all the files in the directory, store into list
    for file in os.listdir(path):
        if file.endswith(ext):
            level0.append(file)
        else:
            print('Error: ' + file + ' is not in the correct format!')
            continue
    # Return: read files that need to be processed
    return level0, path

# Opens all the level0 data and converts it to level1 *.csv data
""" def convertLevel0Files(level0, folder):
    # Obtain the length of the list
    size = len(level0)
    # Open and read all level0 data
    for i in range(size):
        #file = open(folder + level0[i], 'r')
        read_file = pd.read_csv(folder + level0[i]) """

# Process the data
def main():
    # Obtain all level0 files in the directory
    files_0, path = findLevel0Files()
    # For console confirmation
    print('\nPath: ' + path + ' | Files found: ' + str(len(files_0)))
    # Convert the level0 data into level1 data
    # convertLevel0Files(files_0, folder)

# Run the program
main()