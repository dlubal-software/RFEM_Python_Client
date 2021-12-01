import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import *
#from RFEM.window import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.solidSet import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.TypesForSurfaces.surfaceSupport import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.lineLoad import *
from RFEM.Loads.surfaceLoad import *

try:
    from PyQt5 import QtWidgets, QtCore, uic
except:
    print('PyQt5 library is not installed in your Python env.')
    instPyQt5 = input('Do you want to install it (y/n)? ')
    instPyQt5 = instPyQt5.lower()
    if instPyQt5 == 'y':
        import subprocess
        try:
            subprocess.call('python -m pip install PyQt5 --user')
        except:
            print('WARNING: Installation of PyQt5 library failed!')
            print('Please use command "pip install PyQt5 --user" in your Command Prompt.')
            input('Press Enter to exit...')
            sys.exit()
    else:
        input('Press Enter to exit...')
        sys.exit()

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi(dirName + "/Main.ui", self)

        # Slots
        self.ui.buttonOK.clicked.connect(self.onOK)
        self.ui.buttonAbbrechen.clicked.connect(self.onCancel)

    def onOK(self):
        try:
            # There is missing error handling.
            l = float(self.ui.l.text())
            f = float(self.ui.f.text())

        except:
            print('Error in input.')
            input('Press Enter to exit...')
            sys.exit()

        # RFEM 6
        Model(True, "CantileverQt") # crete new model called CantileverQt
        Model.clientModel.service.begin_modification('new')

        Material(1, 'S235')

        Section(1, 'IPE 200')

        Node(1, 0.0, 0.0, 0.0)
        Node(2, l, 0.0, 0.0)

        Member(1,  1, 2, 0.0, 1, 1)

        NodalSupport(1, '1', NodalSupportType.FIXED)

        StaticAnalysisSettings(
            1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

        LoadCase(1, 'Eigengewicht',[True, 0.0, 0.0, 1.0])

        NodalLoad(
            1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, f*1000)

        Calculate_all()

        print('Ready!')

        Model.clientModel.service.finish_modification()

    def onCancel(self):
        print('Cancel')
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
