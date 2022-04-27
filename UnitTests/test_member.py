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
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member

if Model.clientModel is None:
    Model()

def test_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member(1, 1, 2, 0, 1, 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_member_beam():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Beam(1, 1, 2, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1, 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.analytical_length == 5
    assert member.type == "TYPE_BEAM"

def test_member_rigid():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.Rigid(1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_RIGID"

"""
def test_member_rib():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.Rib(5, 1, 2, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, 1, 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(5)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_RIGID"
"""

def test_member_truss():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.Truss(5, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(5)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_TRUSS"

def test_member_trussOnlyN():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.TrussOnlyN(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_TRUSS_ONLY_N"

def test_member_tension():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.Tension(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_TENSION"

def test_member_compression():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.Compression(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_COMPRESSION"

def test_member_buckling():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.Buckling(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_BUCKLING"

def test_member_cable():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.Cable(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_CABLE"

def test_member_resultBeam():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.ResultBeam(1, 1, 2, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM,
                      MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
                      MemberResultBeamIntegration.INTEGRATE_WITHIN_CUBOID_GENERAL,
                      [0.2618], 1, 1, [], [1,2,3,4])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.result_beam_z_minus == 4
    assert member.type == "TYPE_RESULT_BEAM"

def test_member_definableStiffness():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.DefinableStiffness(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_DEFINABLE_STIFFNESS"

def test_member_couplingRigidRigid():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.CouplingRigidRigid(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_COUPLING_RIGID_RIGID"

def test_member_couplingRigidHinge():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.CouplingRigidHinge(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_COUPLING_RIGID_HINGE"

def test_member_couplingHingeRigid():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, -3)

    Member.CouplingHingeRigid(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_COUPLING_HINGE_RIGID"

def test_member_couplingHingeHinge():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 3, 3, 3)

    Member.CouplingHingeHinge(4, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0.2618], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(4)

    assert round(member.analytical_length, 5) == 5.19615
    assert member.type == "TYPE_COUPLING_HINGE_HINGE"
