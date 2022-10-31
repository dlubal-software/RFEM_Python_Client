import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model
from RFEM.Calculate.meshSettings import GetMeshStatistics, GenerateMesh
from RFEM.enums import *

if Model.clientModel is None:
    Model()

def test_generation_of_mesh_statistics():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

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

    Model.clientModel.service.finish_modification()

    mesh_stats = GetMeshStatistics()

    assert mesh_stats['member_1D_finite_elements'] == 0
    assert mesh_stats['surface_2D_finite_elements'] == 100
    assert mesh_stats['solid_3D_finite_elements'] == 0
    assert mesh_stats['node_elements'] == 121
