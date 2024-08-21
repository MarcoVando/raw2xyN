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
 - swig (required by xylib, pip installation)
 - Boost (required by xylib, pip installation)
 - glob
 - Qt5 (conda install pyqt)
 - xylib-py
 - numpy

For proper installation of xylib-py, please refer to https://github.com/wojdyr/xylib

### Mac M chip users with conda
I suggest to create a dedicated conda environment using the x86 architecture. This should avoid any problems with numpy and dependencies. Run this command:  
`CONDA_SUBDIR=osx-64 conda create -n rawconvx86_env numpy -c conda-forge`

#### Troubleshooting
If u get this error trying to install xylib via pip:
```
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [7 lines of output]
      running bdist_wheel
      running build
      running build_ext
      building '_xylib' extension
      swigging xylib.i to xylib_wrap.cpp
      swig -python -c++ -modern -modernargs -py3 -o xylib_wrap.cpp xylib.i
      error: command 'swig' failed: No such file or directory
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for xylib-py
  Running setup.py clean for xylib-py
Successfully built Boost
Failed to build xylib-py
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (xylib-py)
```
run the following command:   
`pip install git+https://github.com/wojdyr/xylib.git`


# Use
raw2xyN can be executed both from terminal and as standalone program.

## execution from terminal
Once all the requirements are installed in a proper python environment, the program can be launched by executing raw2xyN.py in the commandline.  
A GUI will appear asking for selected files or a parent directory where .raw files should be present. 

<img width="299" alt="image" src="https://github.com/user-attachments/assets/4b2edfec-9e97-48b2-beb2-7b11f5fa7ad5">


## execution from .exe file
By this way there's no needs of python interpreter and of the required packages.  
Users can simply launch the program through the .exe file. At this point the same GUI will appear
