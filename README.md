# raw2xyN
Quick and easy BRUKER .raw converter into .xy and .xyn files.
The repository makes use of xylib library (https://github.com/wojdyr/xylib)

## Release v0.0.1 
The package can be used as a Jupyter notebook.
Please, be aware that installation of xylib-py package on windows machine can be difficult/impossible. 
Package works well on UNIX systems. I suggest to install jupyter on a WSL in linux.
Alternatively, .ipynb file can be loaded in google colab and used there.

## Release v0.1.0 
Bug fixes  
Added some functionalities  
Added generation of .log file  

# Installation
## Requirements
When used from terminal this repo needs the following packages:
 - glob
 - Tkinter
 - xylib-py (and its requirements (swig and boost)
 - numpy

For proper installation of xylib-py, please refer to https://github.com/wojdyr/xylib

### Mac M chip users with conda
I suggest to create a dedicated conda environment using the x86 architecture. This should avoid any problems with numpy and dependencies. Run this command:  
`CONDA_SUBDIR=osx-64 conda create -n rawconvx86_env numpy -c conda-forge`

# Use
raw2xyN can be executed both from terminal and as standalone program.

## execution from terminal
Once all the requirements are installed in a proper python environment, the program can be launched by typing raw2xyN.py in the commandline.  
A GUI will appear asking for selected files or a parent directory where .raw files should be present. 

## execution from .exe file
By this way there's no needs of python interpreter and of the required packages.  
Users can simply launch the program through the .exe file. At this point the same GUI will appear
