import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface
from RFEM.SpecialObjects.intersection import Instersection
from RFEM.BasicObjects.thickness import Thickness


if Model.clientModel is None:
    Model()

def test_intersections():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Thickness(1, 'Thick', 1, 0.35)

    Node(1, 0.1, 0, 0)
    Node(2, 4.9, 0, 0)
    Node(3, 4.9, 5, 0)
    Node(4, 0.1, 5, 0)

    Node(5, 0, 4, -3)
    Node(6, 5, 4, -3)
    Node(7, 5, 4, 3)
    Node(8, 0, 4, 3)

    Node(9, 3, 2.5, 1)
    Node(10, 2.5, 2.5, -2)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '5 6')
    Line(6, '6 7')
    Line(7, '7 8')
    Line(8, '8 5')

    Line(9, '9 10')

    Surface(1, '1-4')
    Surface(2, '5-8')
    Surface.Standard(3,SurfaceGeometry.GEOMETRY_PIPE, params={'pipe_radius':0.3, 'pipe_center_line':9})

    Instersection(1,1,2)
    Instersection(2,1,3)

    Model.clientModel.service.finish_modification()

    int_1 = Model.clientModel.service.get_intersection(1)
    assert int_1.generated_lines == '13'
    assert int_1.generated_nodes == '15 16'
    assert int_1.surface_a == 1
    assert int_1.surface_b == 2

    int_2 = Model.clientModel.service.get_intersection(2)
    assert int_2.generated_lines == '14'
    assert int_2.generated_nodes == '17'
    assert int_2.surface_a == 1
    assert int_2.surface_b == 3
