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
    # modal analysis not yet implemmented in released RFEM6
    Model(True, "ModalAnalysis")
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Crate Section
    Section(1, 'IPE 300', 1)

    # Create Nodes
    Node(1, 0, 0, 0)
    Node(2, 0, 0, -5)

    # Create Member
    Member(1, MemberType.TYPE_BEAM, 1, 2, 0, 1, 1)

    # Create Nodal Support
    NodalSupport(1, '1', NodalSupportType.FIXED) 

    # Static Analysis Settings
    StaticAnalysisSettings(1, 'Geometrically Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Modal Analysis Settings
    ModalAnalysisSettings(1, 'Modal Analysis Settings', ModalSolutionMethod.METHOD_LANCZOS, ModalMassConversionType.MASS_CONVERSION_TYPE_Z_COMPONENTS_OF_LOADS, 
    ModalMassMatrixType.MASS_MATRIX_TYPE_DIAGONAL, 2, [False, False, False, False, True, True])

    # Load Case Static
    LoadCase(1, 'DEAD', AnalysisType.ANALYSIS_TYPE_STATIC, 1, 1, True, 0, 0, 1)

    # Load Case Modal
    LoadCase(2, 'MODAL', AnalysisType.ANALYSIS_TYPE_MODAL, 1, 2, False)
    Calculate_all()

    print('Ready!')

    Model.clientModel.service.finish_modification()

