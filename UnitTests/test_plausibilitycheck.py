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
from RFEM.dataTypes import *
from RFEM.enums import *

if __name__ == '__main__':
    # modal analysis not yet implemmented in released RFEM6
    clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Sections
    Section(1, 'HEA 240', 1)
    Section(2, 'IPE 300', 1)

    # Create Nodes
    Node(1, 0, 0, 0)
    Node(3, 6, 0, -5)
    Node(4, 6, 0, 0)

    # Create Members
    Member(1, MemberType.TYPE_BEAM, 1, 2, 0, 1, 1)
    Member(2, MemberType.TYPE_BEAM, 2, 3, 0, 2, 2)
    Member(3, MemberType.TYPE_BEAM, 4, 3, 0, 1, 1)

    # Create Nodal Supports
    NodalSupport(1, '1 4', NodalSupportType.FIXED)

    plausibilityCheck()

    print('Ready!')

    clientModel.service.finish_modification()




