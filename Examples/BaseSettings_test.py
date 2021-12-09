import sys
sys.path.append(".")
from RFEM.Loads.surfaceLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.nodalLoad import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.BasicObjects.solidSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.material import *
from RFEM.initModel import *
from RFEM.enums import *
from RFEM.baseSettings import *

if __name__ == '__main__':

    clientModel.service.begin_modification()

    # Set Base Settings
    BaseSettings(12, GlobalAxesOrientationType.E_GLOBAL_AXES_ORIENTATION_ZUP, LocalAxesOrientationType.E_LOCAL_AXES_ORIENTATION_ZUP, [0.001, 0.002, 0.003, 0.004])

    print('Ready!')

    clientModel.service.finish_modification()

