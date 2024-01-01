'''
Convert Files Module

Takes the raw EDT message files and converts them to readable *.csv files
'''

# Imports
import os

# Modules/Classes
from pyplotsonde.file_paths import LEVEL0_DIRECTORY, LEVEL1_DIRECTORY
from classes.FilesAlreadyConvertedError import FilesAlreadyConvertedError

def find_files(extension, directory):
    """
    Finds all text files in the LEVEL0_DIRECTORY.

    Args:
        extension (string): Extension defined for the file.
        directory (string): Directory for the files

    Returns:
        list: List of text files to be processed.
    """

    files = []
    # Iterate over all the files in the directory, store into list
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(file)
        else:
            print('\nError: ' + file + ' is not in the correct format!')
            continue

    return files

def open_files(txtFiles, progressBar):
    """
    Processes and converts the raw EDT message files to readable *.csv files.

    Args:
        txtFiles (list): List of text files to be processed.
        progressBar: The progress bar for visual feedback during the conversion.

    Returns:
        bool: True if files are processed and converted successfully, otherwise False.
    
    Raises:
        FilesAlreadyConvertedError: If files have already been converted.
    """

    # Get the number of files in the level 1 directory
    csvSize = len(os.listdir(LEVEL1_DIRECTORY))
    # Check to see if the files have already been processed
    if (csvSize == 0):
        # Process txt files to csv files
        for index in range(0, len(txtFiles)):
            # Open the file stream to write the processed level0 data
            fout = open(LEVEL1_DIRECTORY + txtFiles[index], 'wt')
            # Go through each line and format it properly to convert to level1 data
            with open(LEVEL0_DIRECTORY + txtFiles[index], 'r') as fp: process_level0_files(fout, fp, progressBar)
        # Convert file extensions to *.csv
        flag = convert_to_csv(txtFiles)
    # Files have already been processed, no need to process them again!
    else:
        raise FilesAlreadyConvertedError("No conversion needed")

    return flag

def process_level0_files(fout, fp, progressBar):
    """
    Processes the raw *.txt file, formats the data, and writes it to a new *.csv file.

    Args:
        fout: File stream to write the processed data.
        fp: File stream of the raw *.txt file.
        progressBar: The progress bar for visual feedback.
    """

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

def convert_to_csv(txtFiles):
    """
    Renames processed data files to *.csv files.

    Args:
        txtFiles (list): List of text files that have been processed.
    """

    # Size for processed files
    txtSize = len(txtFiles)
    # Directory holding all of the *.csv files
    csvFiles = os.listdir(LEVEL1_DIRECTORY)
    # Check for when there are no files to convert in the level 0 directory
    if txtSize == 0:
        # Return - flag for checking if there were files or not
        raise FileNotFoundError("Missing file(s)")
    # Convert files to *.csv
    for filename in csvFiles:
        infilename = os.path.join(LEVEL1_DIRECTORY, filename)
        if not os.path.isfile(infilename): continue
        # Change the extension to *.csv
        csv_ext = infilename.replace('.txt', '.csv')
        # Change the name of the file
        os.rename(infilename, csv_ext)

    return True