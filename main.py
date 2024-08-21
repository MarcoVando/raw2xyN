#!/usr/bin/env python

#TODO save also the log file
#TODO Show the window when the conversion is complete
#-- TODO open file as latin-1, if RAW4.0 is read, discard the file, filetype not supported.
#-- TODO error hangling to avoid crashing the program
#TODO fix the double ..xy format
#TODO implement same application but with the option to plot the data and work on the plot.

import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QLabel, QLineEdit, QPushButton
import numpy as np
import xylib as xy

#SECTION ####################### XYLIB ########################
def load_file(path):
    if os.path.isfile(path):
        print("file accepted")
        try:
            file = xy.load_file(path)
        except:
            raise Exception("Filetype not supported")
        return file
    else:
        return 0

def extract_file(file):
    print('trying to extract the file')
    #usually raws are made of 1 block
    block = file.get_block(0)
    col1 = block.get_column(1)
    col2 = block.get_column(2)

    # Get metadata from which u can obtain the x a  xis (seems that col1 is not accessible"""
    meta = block.meta
    keys = []

    #get the keys name
    for i in range(0,meta.size()):
        keys.append(meta.get_key(i))

    #loop over keys to get their values
    for key in keys:
        print(key ,meta.get(key))

    if meta.has_key("START_2THETA"):
        start2th = float(meta.get('START_2THETA'))
    elif meta.has_key("THETA_START"):
        start2th = 2*float(meta.get('THETA_START'))
    else:
        return 0, 0, 0, 0, 0, 0
    if meta.has_key('STEP_SIZE'):
        stepsize = float(meta.get('STEP_SIZE'))
    else:
        stepsize = col1.get_step()
    if meta.has_key("STEPS"):
        nstep = float(meta.get('STEPS'))
    else:
        nstep = col2.get_point_count()
    return col1, col2, meta, start2th, stepsize, nstep

def save_as_np(path, meta, col2, start, step, nstep):
    filename = os.path.basename(path)
    path = os.path.dirname(path)

    print('analyzed file: ', filename)
    if not path.endswith('/'):
        path = path + '/'

    # creat np array for x
    npx = np.arange(start,start+step*nstep,step)

    # Extract y values
    valy = []
    for index in range(1, col2.get_point_count()):
        valy.append(col2.get_value(index))
    npy = np.array(valy)    # create numpy array
    npdataset = np.array([npx[:-1], npy]).T    #build the dataset

    #construct the head of the final file 
    if meta.has_key("TIME_PER_STEP") and meta.has_key('USED_LAMBDA'):
        tps = meta.get('TIME_PER_STEP')
        lam = meta.get('USED_LAMBDA')
        head = f"time per step: {tps}\nlambda: {lam}\n2theta Counts"
    else:
        head = ""

    # Export and save
    # create and clean export folder
    if not os.path.exists(path+'export/'): 
        os.mkdir(path+'export')
    np.savetxt(fname=path+'export/'+filename[:-3]+".xy", X=npdataset, header=head)


#SECTION ####################### GUI CLASSES ####################################
class DragAndDropBox(QWidget):
    def __init__(self):
        super().__init__()
        self.paths = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Drag and Drop Box')
        self.nFiles = 0
        
        layout = QVBoxLayout()

        self.frame = QFrame()
        self.frame.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.frame.setAcceptDrops(True)
        self.frame.dragEnterEvent = self.dragEnterEvent
        self.frame.dropEvent = self.dropEvent
        label = QLabel('Drag and Drop Here')
        self.label_nItems = QLabel(f'{self.nFiles} files dropped')

        confirm_button = QPushButton("Confirm")
        confirm_button.clicked.connect(self.run_conversion)
        
        layout.addWidget(self.frame)
        layout.addWidget(label)
        layout.addWidget(self.label_nItems)
        layout.addWidget(confirm_button)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 150)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.nFiles +=1
            self.paths.append(url.toLocalFile())
            print('Dropped file:', url.toLocalFile())
            self.label_nItems.setText(f'{self.nFiles} files dropped')

    def run_conversion(self):
        errors = []
        # Convert files
        print("start conversion")
        for path in self.paths:
            print("getting files")
            file = load_file(path)
            if file != 0:
                col1, col2, meta, start, step, nstep = extract_file(file)
                if start != 0 and step != 0 and nstep != 0:
                    save_as_np(path, meta, col2, start, step, nstep)
                else:
                    errors.append(path)
            else:
                errors.append(path)
        conversion_complete_window = ConversionCompleteWindow(len(errors), len(self.paths))
        conversion_complete_window.show()
        errors = []
        self.nFiles = 0
        self.label_nItems.setText(f'{self.nFiles} files dropped')
        return errors

class ConversionCompleteWindow(QWidget):
    def __init__(self, nerrors, ndata):
        super().__init__()
        self.nerrors = nerrors
        self.ndata = ndata
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Conversion Complete')
        layout = QVBoxLayout()
        label = QLabel('Conversion Complete')
        layout.addWidget(label)
        conv_results = QLabel(f"{self.ndata} files converted, {self.nerrors} files with errors")
        layout.addWidget(conv_results)
        self.setLayout(layout)
        self.setGeometry(400, 400, 200, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DragAndDropBox()
    ex.show()

    sys.exit(app.exec_())