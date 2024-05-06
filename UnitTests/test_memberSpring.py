import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import MemberSpringType, PartialActivityAlongType, MemberSpringSelfWeightDefinition, MemberSpringDiagramType
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForMembers.memberSpring import MemberSpring

if Model.clientModel is None:
    Model()

def test_DesignSituation():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0, 0, 0)
    Node(2, 10, 0, 0)
    Node(3, 20, 0, 0)

    Member.Spring(1, 1, 2)

    MemberSpring(1, '1', MemberSpringType.PARTIAL_ACTIVITY, [[PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 0.1], \
        [PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.15, 0.25]], 110, [MemberSpringSelfWeightDefinition.MASS_PER_LENGTH, 5], 'Spring 1')
    MemberSpring(2, '', MemberSpringType.DIAGRAM, [[True, MemberSpringDiagramType.DIAGRAM_ENDING_TYPE_FAILURE], \
        [[0.01, 1000], [0.02, 1100], [0.035, 500]]], 20, [MemberSpringSelfWeightDefinition.SPECIFIC_WEIGHT, 1500, 0.012], 'Spring 2')

    Member.Spring(2, 2, 3, spring_type=2)

    Model.clientModel.service.finish_modification()

    ms1 = Model.clientModel.service.get_member_spring(1)
    assert ms1.assigned_to == '1'
    assert ms1.mass_per_length == 5

    ms2 = Model.clientModel.service.get_member_spring(2)
    assert ms2.name == 'Spring 2'
    assert ms2.axial_stiffness == 20
