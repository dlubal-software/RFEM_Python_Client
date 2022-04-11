import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.TypesForMembers.memberDefinableStiffness import MemberDefinableStiffness

if Model.clientModel is None:
    Model()

def test_all_member_types():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Material(2, 'C30/37')

    Section(1, 'IPE 300', 1)
    Section(2, 'IPE 500', 1)

    Thickness(1, '180 mm', 2, 0.18)

    node_tag_lst = list(range(1, 62, 1))
    node_x_lst = [0, 5]*(int(len(node_tag_lst)/2))
    node_y_lst = []
    for i in list(range(0, 61, 2)):
        node_y_lst.append(i)
        node_y_lst.append(i)

    for t,x,y in zip(node_tag_lst, node_x_lst, node_y_lst):
        Node(t, x, y, 0)

    # Initial Member Function
    Member(1, 1, 2, 0, 1, 1)

    # Beam Member with Angle Rotation
    Member.Beam(2, 3, 4, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [15], 1, 1)

    # Beam Member with Node Rotation
    Member.Beam(3, 5, 6, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE, [5, MemberRotationPlaneType.ROTATION_PLANE_XY], 1, 1)

    # Beam Member with Member Hinge
    MemberHinge(1, "Local", rotational_release_my= 0.0, rotational_release_mz=0.0)
    Member.Beam(4, 7, 8, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1, 1, params={'member_hinge_start': 1, 'member_hinge_end' : 1})

    # Beam Member with End Modifications
    Member.Beam(5, 9, 10, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1, 1,
    params={'end_modifications_member_start_extension': 1, 'end_modifications_member_start_slope_y': 0.03, 'end_modifications_member_start_slope_z': 0.05, 'end_modifications_member_end_extension': 4, 'end_modifications_member_end_slope_y': 0.08, 'end_modifications_member_end_slope_z': 0.1})

    # Beam Member with Linear Distribution
    Member.Beam(6, 11, 12, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_LINEAR, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1, 2, [MemberSectionAlignment.SECTION_ALIGNMENT_BOTTOM])

    # Beam Member with Tapered at Both Sides
    Member.Beam(7, 13, 14, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_BOTH_SIDES, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 2, 2, [True, True, 0.25, 0.25, MemberSectionAlignment.SECTION_ALIGNMENT_CENTRIC, 1])

    # Beam Member with Tapered at the Start
    Member.Beam(8, 15, 16, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_START_OF_MEMBER, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 2, 1, [True, 0.25, MemberSectionAlignment.SECTION_ALIGNMENT_CENTRIC])

    # Beam Member with Tapered at the End
    Member.Beam(9, 17, 18, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_END_OF_MEMBER, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1, 2, [True, 0.25, MemberSectionAlignment.SECTION_ALIGNMENT_CENTRIC])

    # Beam Member with Tapered at the End
    Member.Beam(10, 19, 20, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_SADDLE, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1, 1, [True, 0.5, MemberSectionAlignment.SECTION_ALIGNMENT_CENTRIC, 2])

    # Beam Member with Offset at Both End
    Member.Beam(11, 21, 22, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_BOTH_SIDES, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1, 1, [True, True, 0.25, 0.25, MemberSectionAlignment.SECTION_ALIGNMENT_CENTRIC, 2])

    # Beam Member with Offset at Start
    Member.Beam(12, 23, 24, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_START_OF_MEMBER, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1, 2, [True, 0.25, MemberSectionAlignment.SECTION_ALIGNMENT_CENTRIC])

    # Beam Member with Offset at End
    Member.Beam(13, 25, 26, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_END_OF_MEMBER, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1, 2, [True, 0.25, MemberSectionAlignment.SECTION_ALIGNMENT_CENTRIC])

    # Rigid Member
    Member.Rigid(14, 27, 28, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    # Rigid Member with Member Hinge
    Member.Rigid(15, 29, 30, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], params={'member_hinge_start' : 1, 'member_hinge_end': 1})

    # Truss Member
    Member.Truss(16, 31, 32, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    # Truss Only N Member
    Member.TrussOnlyN(17, 33, 34, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    # Tension Member
    Member.Tension(18, 35, 36, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    # Compression Member
    Member.Compression(19, 37, 38, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    # Buckling Member
    Member.Buckling(20, 39, 40, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    # Cable Member
    Member.Cable(21, 41, 42, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    # Result Beam 1
    Member.ResultBeam(22, 43, 44, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, MemberResultBeamIntegration.INTEGRATE_WITHIN_CUBOID_QUADRATIC, [0], 1, 1,  integration_parameters = [0.1])

    # Result Beam 2
    Member.ResultBeam(23, 45, 46, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, MemberResultBeamIntegration.INTEGRATE_WITHIN_CUBOID_GENERAL, [0], 1, 1, integration_parameters=[0.1, 0.2, 0.3, 0.4])

    # Result Beam 3
    Member.ResultBeam(24, 47, 48, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, MemberResultBeamIntegration.INTEGRATE_WITHIN_CYLINDER, [0], 1, 1, integration_parameters=[0.5])

    # Result Beam 4
    Member.ResultBeam(25, 49, 50, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, MemberResultBeamIntegration.INTEGRATE_FROM_LISTED_OBJECT, [0], 1, 1)

    # Member Definable Stiffness
    MemberDefinableStiffness(1)
    Member.DefinableStiffness(26, 51, 52, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1)

    # Member Coupling Rigid Rigid
    Member.CouplingRigidRigid(27, 53, 54)

    # Member Coupling Rigid Hinge
    Member.CouplingRigidHinge(28, 55, 56)

    # Member Coupling Hinge Rigid
    Member.CouplingHingeRigid(29, 57, 58)

    # Member Coupling Hinge Hinge
    Member.CouplingHingeHinge(30, 59, 60)

    Model.clientModel.service.finish_modification()
