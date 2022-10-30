'''
Takes the raw EDT message files and converts them to readable *.csv files

Repo: https://github.com/hlreev/sounding_plot_3D

Version History can be found in VERSIONS.md
'''

# Global imports
import os
import sys
import pandas as pd

# Metadata
__author__ = 'Hunter L Reeves'
__license__ = 'GPL3'
__version__ = '0.8.0-pre'
__maintainer__ = 'Hunter L Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'
__lastUpdated__ = '2022-10-29'

# Level0 variables
level0_path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level0\\'
level0_ext = '.txt'
# Level1 variables
level1_path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level1\\'
level1_ext = '.txt'

# Looks through the level0 data for later reading and conversion
def findLevel0Files():
    # List of files that need to be read in
    level0 = []
    # Iterate over all the files in the directory, store into list
    for file in os.listdir(level0_path):
        if file.endswith(level0_ext):
            level0.append(file)
        else:
            print('Error: ' + file + ' is not in the correct format!')
            continue
    # Return: read files that need to be processed
    return level0

# Process the raw data from the EDT messages to comma delimited *.txt files
def processLevel0Files(level0):
    # Message for processing level0
    print('Processing Level 0 data...')
    # To store the level1 processed files
    level1 = []
    for index in range(0, len(level0)):
        # Open the file stream to write the processed level0 data
        fout = open(level1_path + level0[index], 'wt')
        # Go through each line and format it properly to convert to level1 data
        with open(level0_path + level0[index], 'r') as fp:
            # Read all of the lines in the raw *.txt file
            lines = fp.readlines()
            # Go through the level0 data
            for row in lines:
                # Remove the row that has the units (unnecessary)
                if row != lines[1]:
                    # Remove the word 'time' from the columns
                    row = row.replace('Elapsed time', 'Elapsed')
                    # Repace the spaces with commas for *.csv reading
                    fout.write(','.join(row.split()))
                    fout.write('\n')
        # Close the file stream
        fout.close()
    # Store into level1 files
    print('DONE.')
    level1 = level0
    # Return: The level1 processed *.txt files
    return level1

# Convert processed data files to *.csv files
def convertToCSV(level1):
    # Folder that holds files to change
    folder = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level1\\'
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename): continue
        csv_ext = infilename.replace('.txt', '.csv')
        new_file = os.rename(infilename, csv_ext)
        level1 = new_file
    return level1

# Process the data
def main():
    # Obtain all level0 files in the directory
    level0 = findLevel0Files()
    # For console debugging
    print('\nPath: ' + level0_path + ' | Files found: ' + str(len(level0)))
    # Process level0 data
    level1 = processLevel0Files(level0)
    # Convert file extensions to *.csv
    convertToCSV(level1)

# Run the program
main()