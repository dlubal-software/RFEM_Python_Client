import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model, CheckIfMethodOrTypeExists
from RFEM.Tools.ModelCheck import ModelCheck
import pytest

if Model.clientModel is None:
    Model()

# TODO: US-8140
@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'model_check__get_object_groups_operation', True), reason="model_check__get_object_groups_operation not in RFEM GM yet")
def test_model_check():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

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

    Member(1, 9, 10, 0, 1, 1)
    Member(2, 11, 12, 0, 1, 1)
    Member(3, 15, 16, 0, 1, 1)
    Member(4, 15, 16, 0, 1, 1)

    Model.clientModel.service.finish_modification()

    identical_nodes = ModelCheck.GetIdenticalNodes(0.0005)
    assert identical_nodes[0][0] == "1,2"
    assert identical_nodes[0][1] == "3,4"
    ModelCheck.DeleteUnusedNodes(0.0005, identical_nodes)
    connected_lines = ModelCheck.GetNotConnectedLines(0.0005)
    assert connected_lines[0][0] == "1,2"
    assert connected_lines[0][1] == "5,6"
    ModelCheck.CrossLines(0.0005, connected_lines)
    ModelCheck.GetNotConnectedMembers(0.0005)
    overlapping_lines = ModelCheck.GetOverlappingLines()
    assert overlapping_lines[0][0] == "3,4"
    assert overlapping_lines[0][1] == "7,8"
    overlapping_members = ModelCheck.GetOverlappingMembers()
    assert overlapping_members[0][0] == "3,4"

