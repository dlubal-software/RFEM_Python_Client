import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface
from RFEM.SpecialObjects.rigidLink import RigidLink
from RFEM.BasicObjects.thickness import Thickness


if Model.clientModel is None:
    Model()

def test_rigid_links():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Thickness(1, 'Thick', 1, 0.35)

    Node(1, 0.1, 0, 0)
    Node(2, 4.9, 0, 0)
    Node(3, 4.9, 5, 0)
    Node(4, 0.1, 5, 0)

    Node(5, 0, 6, 0)
    Node(6, 0, 6, -3)
    Node(7, 5, 6, -3)
    Node(8, 5, 6, 0)
    Node(9, 5, 6 , 3)
    Node(10, 0, 6, 3)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '10 6')
    Line(6, '6 7')
    Line(7, '7 9')
    Line(8, '9 10')

    Line(9, '5 8')

    Surface(1, '1-4')
    Surface(2, '5-8')

    RigidLink(1, 3, 6)
    RigidLink.LineToLine(2, 3, 8)
    RigidLink.LineToSurface(3, 3, 2)
    RigidLink.Diapragm(4,'3 4', '6 9')

    Model.clientModel.service.finish_modification()

    rl_1 = Model.clientModel.service.get_rigid_link(1)
    assert rl_1.type == 'TYPE_LINE_TO_LINE'
    assert rl_1.line1 == 3
    assert rl_1.line2 == 6

    rl_2 = Model.clientModel.service.get_rigid_link(2)
    assert rl_2.type == 'TYPE_LINE_TO_LINE'
    assert rl_2.line1 == 3
    assert rl_2.line2 == 8

    rl_3 = Model.clientModel.service.get_rigid_link(3)
    assert rl_3.type == 'TYPE_LINE_TO_SURFACE'
    assert rl_3.line1 == 3
    assert rl_3.line2 == 10

    rl_4 = Model.clientModel.service.get_rigid_link(4)
    assert rl_4.type == 'TYPE_DIAPHRAGM'
    assert rl_4.nodes == '3 4'
    assert rl_4.lines == '6 9'

