# raw2xyN
Quick and easy BRUKER .raw converter into .xy and .xyn files.
The repository makes use of xylib library (https://github.com/wojdyr/xylib)

# Installation
The package can be used both from terminal and as standalone program (Windows user, .exe file is given in ... folder).

## Requirements
When used from terminal this repo needs the following packages:
 - glob
 - Tkinter
 - xylib-py (and its requirements (swig and boost)
 - numpy

For proper installation of xylib-py, please refer to https://github.com/wojdyr/xylib

# Use
raw2xyN can be executed both from terminal and as standalone program.

## execution from terminal
Once all the requirements are installed in a proper python environment, the program can be launched by typing raw2xyN.py in the commandline.  
A GUI will appear asking for selected files or a parent directory where .raw files should be present. 

## execution from .exe file
By this way there's no needs of python interpreter and of the required packages.  
Users can simply launch the program through the .exe file. At this point the same GUI will appear
