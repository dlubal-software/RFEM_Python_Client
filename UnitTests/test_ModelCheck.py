import sys
from types import coroutine
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
from RFEM.Tools.ModelCheck import ModelCheck


if __name__ == '__main__':

    clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 0, 0, 0)
    Node(3, 1, 1, 1)
    Node(4, 1, 1, 1)
    
    Node(5, 10, 0, 0)
    Node(6, 10, 3, 0)
    Node(7, 9, 2, 0)
    Node(8, 11, 2, 0)

    Node(9, 13, 0, 0)
    Node(10, 13, 3, 0)
    Node(11, 12, 2, 0)
    Node(12, 14, 2, 0)

    Node(13, 5, 0, 0)
    Node(14, 5, 3, 0)

    Node(15, 7, 0, 0)
    Node(16, 7, 3, 0)
    
    Line(1, '5 6')
    Line(2, '7 8')

    Line(3, '13 14')
    Line(4, '13 14')

    Member(1, MemberType.TYPE_BEAM, 9, 10, 0, 1, 1)
    Member(2, MemberType.TYPE_BEAM, 11, 12, 0, 1, 1)
    Member(3, MemberType.TYPE_BEAM, 15, 16, 0, 1, 1)
    Member(4, MemberType.TYPE_BEAM, 15, 16, 0, 1, 1)

    print('Ready!')

    clientModel.service.finish_modification()


    identical_nodes = ModelCheck.GetIdenticalNodes(0, 0.0005)

    ModelCheck.DeleteUnusedNodes(0, 0.0005, identical_nodes)

    crossing_lines = ModelCheck.GetNotConnectedLines(0, 0.0005)

    ModelCheck.CrossLines(0, 0.0005, crossing_lines)

    crossing_members = ModelCheck.GetNotConnectedMembers(0, 0.0005)

    overlapping_lines = ModelCheck.GetOverlappingLines(0)

    print(overlapping_lines)

    overlapping_members = ModelCheck.GetOverlappingMembers(0)

    print(overlapping_members)