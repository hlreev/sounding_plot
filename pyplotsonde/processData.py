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
__maintainer__ = 'Hunter L Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'

# Level0 variables
level0_path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level0\\'
level0_ext = '.txt'
# Level1 variables
level1_path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level1\\'
level1_ext = '.txt'

# Convert processed data files to *.csv files
def convertToCSV(txtFiles):
    # Counter and size for processed files
    count = 0
    size = len(txtFiles)
    # Folder that holds files to change
    folder = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level1\\'
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename): continue
        # Change the extension to *.csv
        csv_ext = infilename.replace('.txt', '.csv')
        new_file = os.rename(infilename, csv_ext)
        csvFiles = new_file
        # Increment counter to keep track of how many files have been processed
        count += 1
        print(str(count) + '/' + str(size) + ' files processed.')
    return csvFiles

# Read all the lines in each raw *.txt file and filter the data
def processLevel0Files(fout, fp):
    # Read all of the lines in the raw *.txt file
    lines = fp.readlines()
    # Go through the level0 data
    for row in lines:
        # Remove the row that has the units (unnecessary)
        if row != lines[1]:
            # Remove the word 'time' from the columns
            row = row.replace('Elapsed time', 'ElapsedTime')
            # Repace the spaces with commas for *.csv reading
            fout.write(','.join(row.split()))
            fout.write('\n')

# Process the raw data from the EDT messages to comma delimited *.txt files
def openLevel0Files(txtFiles):
    # Process txt files to csv files
    for index in range(0, len(txtFiles)):
        # Open the file stream to write the processed level0 data
        fout = open(level1_path + txtFiles[index], 'wt')
        # Go through each line and format it properly to convert to level1 data
        with open(level0_path + txtFiles[index], 'r') as fp:
            # Process each of the files
            processLevel0Files(fout, fp)
        # Close the file stream
        fout.close()
    # Convert file extensions to *.csv
    convertToCSV(txtFiles)

# Looks through the level0 data for later reading and conversion
def findLevel0Files():
    # List of files that need to be read in
    txtFiles = []
    # Iterate over all the files in the directory, store into list
    for file in os.listdir(level0_path):
        if file.endswith(level0_ext):
            txtFiles.append(file)
        else:
            print('\nError: ' + file + ' is not in the correct format!')
            continue
    # Return: read files that need to be processed
    return txtFiles

# Process the data
def main():
    # Obtain all level0 files in the directory
    txtFiles = findLevel0Files()
    # For console debugging
    print('\nPath: ' + level0_path + ' | Files found: ' + str(len(txtFiles)) + '\n')
    # Open all of the level 0 files
    openLevel0Files(txtFiles)
    # Message when finished
    print('\nDone. Your data is now ready to plot. It can be found in /data/level1.')

# Run the program
main()