import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model
from RFEM.BasicObjects.node import Node
from RFEM.TypesForMembers.memberDefinableStiffness import MemberDefinableStiffness

if Model.clientModel is None:
    Model()

### Member Definable Stiffness Test ###
def test_memberDefinableStiffness():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0,0,0)
    Node(2, 5,0,0)
    Node(3, 0,5,0)
    Node(4, 5,5,0)

    MemberDefinableStiffness()
    MemberDefinableStiffness(2, [True, "Stiffness"], '2', 100, 200, 300, 400, 500, 600, 700, 800, 90, 900, 1000, 1100)

    Model.clientModel.service.finish_modification()

    memberDefinableStiffness_1 = Model.clientModel.service.get_member_definable_stiffness(1)
    memberDefinableStiffness_2 = Model.clientModel.service.get_member_definable_stiffness(2)

    assert memberDefinableStiffness_1.no == 1
    assert memberDefinableStiffness_2.thermal_expansion_height == 1100

