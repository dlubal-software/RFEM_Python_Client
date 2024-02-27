import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.member import Member
from RFEM.Results.meshTables import MeshTables

if Model.clientModel is None:
    Model()

def test_mesh_tables():

    Model.clientModel.service.begin_modification()

    Node(1, 0,0,0)
    Node(2, 0,10,0)
    Node(3, 10,10,0)
    Node(4, 10,0,0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Material(1, "S235")

    Thickness(1, 'Thickness', 1, 0.02)

    Surface(1, '1 2 3 4', 1)

    Section(1, "IPE 300", 1)

    Node(5, 0,20,0)
    Node(6, 20,20,0)

    Member(1, 5, 6, 0, 1, 1)

    Model.clientModel.service.generate_mesh(True)
    Model.clientModel.service.finish_modification()

    allFeNodes = MeshTables.GetAllFENodes()
    assert allFeNodes

    customNode = MeshTables.getFENodeOriginalMesh(8)
    assert customNode['y'] == 1.5

    all1DElements = MeshTables.getAllFE1DElements()
    assert all1DElements[12]['FE_node1_no'] == 454

    all2DElemets = MeshTables.getAllFE2DElements()
    assert all2DElemets[5]['surface_no'] == 1

    custom1DElement = MeshTables.getFE1DElement(5)
    assert custom1DElement['FE_node2_no'] == 447

    custom2DElement = MeshTables.getFE2DElement(18)
    assert custom2DElement['FE_node3_no'] == 37
