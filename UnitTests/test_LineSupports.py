import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.dataTypes import inf
from RFEM.initModel import Model
from RFEM.enums import LineSupportType
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.TypesForLines.lineSupport import LineSupport

if Model.clientModel is None:
    Model()

def test_LineSupports():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5.0, 0.0, 0.0)
    Node(3, 10.0, 0.0, 0.0)
    Node(4, 15.0, 0.0, 0.0)
    Node(5, 20.0, 0.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 5')

    LineSupport(1, '1', [0, inf, 15000, inf, inf, inf])
    LineSupport(2, '2', LineSupportType.FIXED)
    LineSupport(3, '3', LineSupportType.HINGED)
    LineSupport(4, '4', LineSupportType.FREE)

    Model.clientModel.service.finish_modification()

    ls1 = Model.clientModel.service.get_line_support(1)
    assert ls1.spring.z == 15000.0
    assert ls1.rotational_restraint.z == inf

    ls2 = Model.clientModel.service.get_line_support(2)
    assert ls2.spring.x == inf
    assert ls2.spring.y == inf
    assert ls2.spring.z == inf
    assert ls2.rotational_restraint.x == inf
    assert ls2.rotational_restraint.y == inf
    assert ls2.rotational_restraint.z == inf

    ls3 = Model.clientModel.service.get_line_support(3)
    assert ls3.spring.x == inf
    assert ls3.spring.y == inf
    assert ls3.spring.z == inf
    assert ls3.rotational_restraint.x == 0.0
    assert ls3.rotational_restraint.y == 0.0
    assert ls3.rotational_restraint.z == 0.0

    ls4 = Model.clientModel.service.get_line_support(4)
    assert ls4.spring.x == 10000.0
    assert ls4.spring.y == 0.0
    assert ls4.spring.z == 0.0
    assert ls4.rotational_restraint.x == 0.0
    assert ls4.rotational_restraint.y == 0.0
    assert ls4.rotational_restraint.z == 0.0
