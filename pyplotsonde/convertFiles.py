'''
Takes the raw EDT message files and converts them to readable *.csv files

Repo: https://github.com/hlreev/sounding_plot

Version History can be found in VERSIONS.md
'''

# Global imports
import os
from progress.bar import IncrementalBar

# Metadata
__author__ = 'Hunter L Reeves'
__license__ = 'GPL3'
__maintainer__ = 'Hunter L Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'

# Level0 variables
level0_path = 'data\\level0\\'
level0_ext = '.txt'
# Level1 variables
level1_path = 'data\\level1\\'
level1_ext = '.txt'

# Convert processed data files to *.csv files
def convertToCSV(txtFiles):
    # Size for processed files
    txtSize = len(txtFiles)
    # Directory holding all of the *.csv files
    csvFiles = os.listdir(level1_path)
    # Check for when there are no files to convert in the level 0 directory
    if txtSize == 0:
        # Return - flag for checking if there were files or not
        return None
    # Convert files to *.csv
    for filename in csvFiles:
        infilename = os.path.join(level1_path, filename)
        if not os.path.isfile(infilename): continue
        # Change the extension to *.csv
        csv_ext = infilename.replace('.txt', '.csv')
        # Change the name of the file
        os.rename(infilename, csv_ext)
    # Return - the flag for found files and the progress bar
    return True

# Read all the lines in each raw *.txt file and filter the data
def processLevel0Files(fout, fp, progressBar):
    # Read all of the lines in the raw *.txt file
    lines = fp.readlines()
    # Go through the level0 data
    for row in lines:
        # Remove the space between 'Elapsed' and 'time' from the columns
        if row == lines[0]:
            row = row.replace('Elapsed time', 'ElapsedTime')
        # Skip the row that has the units (unnecessary) and skip rows with missing data
        if row != lines[1] and '/' not in row:
            # Repace the spaces with commas for *.csv reading
            fout.write(','.join(row.split()))
            fout.write('\n')
    # Continue the progress bar to the next state in the terminal console after each file is processed
    progressBar.next()
    # Close the file stream
    fout.close()

# Process the raw data from the EDT messages to comma delimited *.txt files
def openFiles(txtFiles, progressBar):
    # Get the number of files in the level 1 directory
    csvSize = len(os.listdir(level1_path))
    # Check to see if the files have already been processed
    if (csvSize == 0):
        # Process txt files to csv files
        for index in range(0, len(txtFiles)):
            # Open the file stream to write the processed level0 data
            fout = open(level1_path + txtFiles[index], 'wt')
            # Go through each line and format it properly to convert to level1 data
            with open(level0_path + txtFiles[index], 'r') as fp: processLevel0Files(fout, fp, progressBar)
        # Convert file extensions to *.csv
        flag = convertToCSV(txtFiles)
    # Files have already been processed, no need to process them again!
    else:
        flag = False
    # Return - the flag that checks if there are files or not
    return flag

# Looks through the level0 data for later reading and conversion
def findFiles():
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
    txtFiles = findFiles()
    # Open all of the level 0 files
    print('\nConverting *.txt files to *.csv files. This could take a few moments.\n')
    # Initializes incremental progress bar with the max size of the file length data
    progressBar = IncrementalBar('Converting', max = len(txtFiles), suffix='%(index)d/%(max)d files [%(elapsed_td)s / %(eta_td)s]')
    # Open files, check if there are files to convert
    flag = openFiles(txtFiles, progressBar)
    if flag == True:
        # Progress bar is finished!
        progressBar.finish()
        # Message when finished
        print('\nDone. Your data is ready to plot. The data can be found in ./sounding_plot/data/level1.')
    elif flag == False:
        # Message when files have already been converted
        print('WARNING: The files have already been converted!')
    elif flag == None:
        # Message when there are no files to convert
        print('ERROR: No files were found in ./sounding_plot/data/level0.')
    else:
        # Message when something unexpected occurs
        print('ERROR: Something unexpected has occurred. Please check the directories and the files.')
        return

# Run the program
main()