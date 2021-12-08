#pylint: disable=W0614, W0401, W0622, C0103, C0114, C0115, C0116, C0301, C0413, R0913, R0914, R0915, C0305, C0411, W0102, W0702, E0602, E0401
import sys
sys.path.append(".")
from RFEM.Loads.surfaceLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.nodalLoad import *
from RFEM.LoadCasesAndCombinations.loadCase import *
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
from RFEM.Tools.plausibilityCheck import PlausiblityCheck


if __name__ == '__main__':

    # modal analysis not yet implemmented in released RFEM6
    clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Sections
    Section(1, 'HEA 240', 1)

    # Create Nodes
    Node(1, 0, 0, 0)
    Node(2, 6, 0, 0)

    # Create Members
    Member(1, MemberType.TYPE_BEAM, 1, 2, 0, 1, 1)


    # Create Nodal Supports
    NodalSupport(1, '1', NodalSupportType.FIXED)

    print('Ready!')
    clientModel.service.finish_modification()

    check = PlausiblityCheck()
    print(check.GetErrorMessage())
