import sys
sys.path.append(".")
import pytest
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


def test_generation_mesh_implemented():

    exist = method_exists(clientModel,'generate_mesh')
    assert exist == False #test fail once method is in T9 master or GM

@pytest.mark.skip("all tests still WIP")
def test_generation_of_mesh_statistics():
    # modal analysis not yet implemmented in released RFEM6
    clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')
    Thickness(1, '20 mm', 1, 0.02)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 0, 5, 0)
    Node(4, 5, 5, 0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1 2 3 4', NodalSupportType.FIXED)

    GenerateMesh()

    print('Ready!')

    clientModel.service.finish_modification()

    mesh_stats = GetMeshStatics()

    print(mesh_stats)


