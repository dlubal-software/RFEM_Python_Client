import os
import sys

baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)

sys.path.append(dirName + r'/../..')

from RFEM.initModel import Model
from RFEM.initModel import saveFile

if __name__ == '__main__':

    Model(True, "Model 1")
    saveFile(r'C:\temp\test1')

