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
    # Check for when there are no files to convert
    if size == 0:
        print('ERROR: No files were found in the /level0/ directory.')
        # Return - flag for checking if there were files or not
        return False
    # Convert files to *.csv
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename): continue
        # Change the extension to *.csv
        csv_ext = infilename.replace('.txt', '.csv')
        # Change the name of the file
        os.rename(infilename, csv_ext)
        # Increment counter to keep track of how many files have been processed
        count += 1
        print(str(count) + '/' + str(size) + ' files converted.')
    # Return - the flag for found files
    return True

# Read all the lines in each raw *.txt file and filter the data
def processLevel0Files(fout, fp):
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
    # Close the file stream
    fout.close()

# Process the raw data from the EDT messages to comma delimited *.txt files
def openFiles(txtFiles):
    # Process txt files to csv files
    for index in range(0, len(txtFiles)):
        # Open the file stream to write the processed level0 data
        fout = open(level1_path + txtFiles[index], 'wt')
        # Go through each line and format it properly to convert to level1 data
        with open(level0_path + txtFiles[index], 'r') as fp:
            # Process each of the files
            processLevel0Files(fout, fp)
    # Convert file extensions to *.csv
    flag = convertToCSV(txtFiles)
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
    # For console debugging
    print('\nPath: ' + level0_path + ' | Files found: ' + str(len(txtFiles)) + '\n')
    # Open all of the level 0 files
    print('Converting *.txt files to *.csv files. This may take a second or two.\n')
    # Open files, check if there are files to convert
    flag = openFiles(txtFiles)
    if flag == True:
        # Message when finished
        print('\nDone. Your data is ready to plot. It can be found in /data/level1.')
    else:
        # No files to convert!
        return

# Run the program
main()