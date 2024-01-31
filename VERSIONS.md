# Sounding Plot Viewer Patches and Updates
All versions of Sounding Plot Viewer will be documented here, along with the changelog and bug fixes

## Version 1.1.1 (Date Finished - ??/??/????)
- Adjusted how the moist adiabatic lapse rate is calculated for the parcel trace
- Changed the y-axis tick marks on the sounding to match the SPC sounding page
- Minor changes and tweaks

## Version 1.1.0 (Date Finished - 01/30/2024)
- Refactored code into modules to make it more reusable/modular
- Removed the Stamen series basemaps (deprecated?)
- Added some debugging support for future ease of use
- Adjusted how soundings are plotted
- Now plots a surface-based parcel trace by default for each sounding
- Minor changes and tweaks

## Version 1.0.1 (Date Finished - 08/06/2023)
- Edited the text for some of the console output to make more sense
- Tweaked/updated gitignore
- Added code for a progress bar that displays in console to let the user see what is going on (convertFiles.py and plotData.py)
- Minor changes and tweaks

## Version 1.0.0 (Date Finished - 01/16/2023)
- Cleaned up the code a bit and made it somewhat easier to read
- Can now plot simple soundings
- Edited the axes for the grid lines
- Updated absolute paths to relative paths
- Updated the sounding to be a skewT
- Minor changes and tweaks

## Version 0.9.8-pre (Date Finished - 01/08/2023)
- Cleaned up the code a bit and made it somewhat easier to read
- Can now check for missing data
- Message print to console about where the missing data is
- Adjusted some of the data ranges for plotting the mandatory levels
- Added a check to prevent plotting of sondes that did not make it to 400mb (unsuccessful releases)
- Changes to the config files
- Added more checks to prevent duplicate files from being generated in the level 1 directory
- Minor changes and tweaks

## Version 0.9.7-pre (Date Finished - 01/07/2023)
- Cleaned up the code a bit and made it somewhat easier to read
- Added a compass rose to the bottom right of the screen
- Removed CartoDB Dark Matter in favor of the Stamen series basemaps
- Minor changes and tweaks

## Version 0.9.6-pre (Date Finished - 01/06/2023)
- Cleaned up the code a bit and made it somewhat easier to read
- Can now process and plot multiple files at a time from the directory storing level1 data
- Removed some redundant and unnecessary script metadata

## Version 0.9.5-pre (Date Finished - 01/06/2023)
- Cleaned up the code a bit and made it somewhat easier to read
- Added county polygons for the FWD County Warning Area
- Added county polygons for the backup office CWAs
- Updated DEPENDENCIES.md
- Removed title from the top of the page
- Minor changes and tweaks to tools, title, zoom

## Version 0.9.4-pre (Date Finished - 01/05/2023)
- Cleaned up the code a bit and made it somewhat easier to read
- Added a title to the top of the page
- Minor changes and tweaks

## Version 0.9.3-pre (Date Finished - 11/08/2022)
- Change to initial zoom of map to data
- Removed the now deprecated "resolution" option for processing data, all data is now in 'full'
- Added some additional console messages to processData as well

## Version 0.9.2-pre (Date Finished - 11/05/2022)
- Minor change to how the *.html files are named and saved for viewing data
- Minor tweak to what data is available and some of the logic for plotting

## Version 0.9.1-pre (Date Finished - 10/30/2022)
- Minor tweaks and clean ups to code

## Version 0.9.0-pre (Date Finished - 10/30/2022)
- Reworked some of the files and structure
- Now can select the temporal resolution of the data that you want to plot
- Plots special points for mandatory levels
- Fix the logic for misc point plotting, 400mb, and termination

## Version 0.8.0-pre (Date Finished - 10/29/2022)
- More advanced functionality is beginning work
- Reorganized and cleaned up code
- Better structure and workflow for running scripts
- Added file to list usage and dependencies
- Reworked some functionality and obtained better data to use

## Version 0.7.0-pre (Date Finished - 10/17/2022)
- Added some more advanced checks to how the points are plotted

## Version 0.5.0-pre (Date Finished - 10/07/2022)
- Can plot 2D test data onto an interactive Folium map

## Version 0.1.0-pre (Date Finished - 10/03/2022)
- Base functionality for a 2D plot
- Some interactions were added
- Fixed some bugs and tweaked some colors/settings

## Version 0.0.1-pre (Date Finished - 10/02/2022)
- Started the project
- Added some basic test code for pre-production fun