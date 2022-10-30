'''
Takes the raw EDT message files and converts them to readable *.csv files

Repo: https://github.com/hlreev/sounding_plot_3D

Version History can be found in VERSIONS.md
'''

# Global imports
import os

# Metadata
__author__ = 'Hunter L Reeves'
__license__ = 'GPL3'
__version__ = '0.8.0-pre'
__maintainer__ = 'Hunter L Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'
__lastUpdated__ = '2022-10-29'

# Input variables
in_path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level0\\'
in_ext = '.txt'
# Level1 output variables
level1_path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level1\\'
level1_ext = '.txt'
# Level2 output variables
level2_path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level2\\'
level2_ext = '.csv'

# Looks through the level0 data for later reading and conversion
def findLevel0Files():
    # List of files that need to be read in
    level0 = []
    # Iterate over all the files in the directory, store into list
    for file in os.listdir(in_path):
        if file.endswith(in_ext):
            level0.append(file)
        else:
            print('Error: ' + file + ' is not in the correct format!')
            continue
    # Return: read files that need to be processed
    return level0

# Process the raw data from the EDT messages to comma delimited *.txt files
def processLevel0Files(level0):
    # To store the level1 processed files
    level1 = []
    for index in range(0, len(level0)):
        # Open the file stream to write the processed level0 data
        fout = open(level1_path + level0[index], 'wt')
        # Go through each line and format it properly to convert to level1 data
        with open(in_path + level0[index], 'r') as fp:
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
    level1 = level0
    # Return: The level1 processed *.txt files
    return level1

# Process the data
def main():
    # Obtain all level0 files in the directory
    level0 = findLevel0Files()
    # For console confirmation
    print('\nPath: ' + in_path + ' | Files found: ' + str(len(level0)))
    # Process level0 data
    processLevel0Files(level0)

# Run the program
main()