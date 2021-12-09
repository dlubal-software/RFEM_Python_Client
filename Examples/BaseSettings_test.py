import sys
sys.path.append(".")
from RFEM.initModel import *
from RFEM.enums import *
from RFEM.baseSettings import BaseSettings

if __name__ == '__main__':

    clientModel.service.begin_modification()

    # Set Base Settings
    BaseSettings(12, GlobalAxesOrientationType.E_GLOBAL_AXES_ORIENTATION_ZUP, LocalAxesOrientationType.E_LOCAL_AXES_ORIENTATION_ZUP, [0.001, 0.002, 0.003, 0.004])

    print('Ready!')

    clientModel.service.finish_modification()

