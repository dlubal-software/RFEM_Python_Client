import sys
sys.path.append(".")
from RFEM.LoadCasesAndCombinations.modalAnalysisSettings import ModalAnalysisSettings
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
from RFEM.dataTypes import *
from RFEM.enums import *


if __name__ == '__main__':

    clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Static Analysis Settings
    StaticAnalysisSettings(1, 'Geometrically Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Modal Analysis Settings
    ModalAnalysisSettings(2, 'Modal Analysis Settings', ModalSolutionMethod.METHOD_LANCZOS, ModalMassMatrixType.MASS_MATRIX_TYPE_DIAGONAL, \
    ModalMassConversionType.MASS_CONVERSION_TYPE_Z_COMPONENTS_OF_LOADS_IN_DIRECTION_OF_GRAVITY, 4, [False, False, False, True, True, True])

    # Dead Load Case
    LoadCase(1, 'DEAD', AnalysisType.ANALYSIS_TYPE_STATIC, 1, 1, True, 0, 0, 1)

    #Modal Load Case
    LoadCase(2, 'MODAL', AnalysisType.ANALYSIS_TYPE_MODAL, 2, 1, False)

    print('Ready!')

    clientModel.service.finish_modification()

