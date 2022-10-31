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
__version__ = '0.9.1-pre'
__maintainer__ = 'Hunter L Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'
__lastUpdated__ = '2022-10-30'

# Level0 variables
level0_path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level0\\'
level0_ext = '.txt'
# Level1 variables
level1_path = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level1\\'
level1_ext = '.txt'
# Temporal data resolution options - 0, 1, 2, 3, 4
resolution = ['poor', 'low', 'intermediate', 'high', 'ultra', 'full']

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
    # Select data resolution
    selectedRes = input('\nSelect the temporal resolution for the data (poor, low, intermediate, high, ultra, full): ')
    # Message for processing level0
    print('\nProcessing Level 0 data...')
    # To store the level1 processed files
    level1 = []
    for index in range(0, len(level0)):
        # Open the file stream to write the processed level0 data
        fout = open(level1_path + level0[index], 'wt')
        # Go through each line and format it properly to convert to level1 data
        with open(level0_path + level0[index], 'r') as fp:
            # Read all of the lines in the raw *.txt file
            lines = fp.readlines()
            # Counter for the row
            counter = 0
            # Go through the level0 data
            for row in lines:
                # Remove the row that has the units (unnecessary)
                if row != lines[1]:
                    # Remove the word 'time' from the columns
                    row = row.replace('Elapsed time', 'Elapsed')
                    if selectedRes == resolution[0]: # Poor
                        # Write every 100th line
                        if counter % 100 == 0:
                            # Repace the spaces with commas for *.csv reading
                            fout.write(','.join(row.split()))
                            fout.write('\n')
                    if selectedRes == resolution[1]: # Low
                        # Write every 50th line
                        if counter % 50 == 0:
                            # Repace the spaces with commas for *.csv reading
                            fout.write(','.join(row.split()))
                            fout.write('\n')
                    if selectedRes == resolution[2]: # Intermediate
                        # Write every 20th line
                        if counter % 20 == 0:
                            # Repace the spaces with commas for *.csv reading
                            fout.write(','.join(row.split()))
                            fout.write('\n')
                    if selectedRes == resolution[3]: # High
                        # Write every 5th line
                        if counter % 5 == 0:
                            # Repace the spaces with commas for *.csv reading
                            fout.write(','.join(row.split()))
                            fout.write('\n')
                    if selectedRes == resolution[4]: # Ultra
                        # Write every other line
                        if counter % 2 == 0:
                            # Repace the spaces with commas for *.csv reading
                            fout.write(','.join(row.split()))
                            fout.write('\n')  
                    if selectedRes == resolution[5]: # Full (all of the data)
                        # Repace the spaces with commas for *.csv reading
                        fout.write(','.join(row.split()))
                        fout.write('\n')
                # Increment row counter by 1
                counter += 1
        # Close the file stream
        fout.close()
    # Store into level1 files
    level1 = level0
    # Convert file extensions to *.csv
    toCSV(level1)
    # Return: selected resolution of the data and the level1 file names
    return selectedRes

# Convert processed data files to *.csv files
def toCSV(level1):
    # Folder that holds files to change
    folder = 'C:\\Users\\hunlr\\Desktop\\sounding_plot_3D\\data\\level1\\'
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename): continue
        # Change the extension to *.csv
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
    processLevel0Files(level0)
    # Message when finished
    print('\nDone. Your data is now ready to plot.')

# Run the program
main()