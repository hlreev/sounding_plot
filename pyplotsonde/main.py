'''
Main Module | Sounding Plot Viewer

This module guides the user through the process of processing the data for the sonde plot and then generates files for viewing the sounding trajectory.

Repo: https://github.com/hlreev/sounding_plot

Version History can be found in VERSIONS.md
'''

# Imports
from progress.bar import IncrementalBar

# Modules/Classes
from pyplotsonde.convert_files import find_files, open_files
from pyplotsonde.file_paths import LEVEL0_DIRECTORY, LEVEL1_DIRECTORY
from pyplotsonde.logger import debug
from pyplotsonde.plot_data import generate_plots
from classes.FilesAlreadyConvertedError import FilesAlreadyConvertedError

# Metadata
__author__ = 'Hunter Reeves'
__license__ = 'GPL3'
__maintainer__ = 'Hunter Reeves, NWS Fort Worth'
__email__ = 'hunter.reeves@noaa.gov'
__status__ = 'In Production'
__lastmodified__ = '2023-11-28'

# Flags to check if pressure level has been reached
FLAGS = { '925mb': False, '850mb': False, '700mb': False, '500mb': False, '400mb': False, 
          '300mb': False, '250mb': False, '200mb': False, '150mb': False, '100mb': False,
           '70mb': False,  '50mb': False,  '30mb': False,  '20mb': False,  '10mb': False }

def plot_data():
    """
    Plot trajectories and skew-T soundings.
    """

    csvFiles = find_files(".csv", LEVEL1_DIRECTORY)

    # Message to indicate the start
    print('\nPlotting trajectories and skew-T soundings...\n')
    # Initializes incremental progress bar with the max size of the file length data
    progressBar = IncrementalBar('Plotting', max = len(csvFiles), suffix = '%(index)d/%(max)d files [%(elapsed_td)s / %(eta_td)s]')
    # Generate each soudning plot - bulk of the code is executed here
    generate_plots(csvFiles, FLAGS, progressBar)
    # Check if there are files in the level1 directory
    if len(csvFiles) != 0:
        # Progress bar is finished!
        progressBar.finish()
        # Print the message for debugging at the end of the program running
        print("\nThe trajectories and soundings have been plotted. They can be viewed in the browser from './viewer/YYYYMMDD_HHmm.html'.")
    else:
        # No files found!
        print('\nERROR: No files were found in the /level1/ directory.')

    return

def process_data():
    """
    Convert data files from *.txt to *.csv
    """

    # Start to process the level 0 data
    print('\nConverting *.txt file(s) to *.csv file(s). This could take a few moments.\n')

    txtFiles = find_files(".txt", LEVEL0_DIRECTORY)
    progressBar = IncrementalBar('Converting', max = len(txtFiles), suffix = '%(index)d/%(max)d file(s) [%(elapsed_td)s / %(eta_td)s]')
    flag = open_files(txtFiles, progressBar)

    if flag:
        progressBar.finish()
        debug("Your files have been successfully processed. They are now being plotted.", "INFO")

    return

def main():
    """
    Starting point for Sounding Plot Viewer
    """

    try:
        process_data()
        plot_data()
    except FileNotFoundError as error:
        debug(f"No files were found. Please add the EDT files to the Level 0 directory. Code: {error}", "ERROR")
    except FilesAlreadyConvertedError as error:
        debug(f"The files have already been converted! Code: {error}", "WARNING")
    except Exception as error:
        debug(f"Something unexpected has occurred. Code: {error}", "ERROR")