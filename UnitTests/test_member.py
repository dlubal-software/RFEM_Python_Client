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
from RFEM.TypesForMembers.memberDefinableStiffness import MemberDefinableStiffness
import pytest

if Model.clientModel is None:
    Model()

pytestmark = pytest.mark.skip(False, reason="This test can be skipped/deleted since test_member_test does the same.")
def test_init():

    Model.clientModel.service.reset()
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

def test_beam():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Beam(0, 1, 1, 2, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [15], 1, 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_rigid():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Rigid(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_truss():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Truss(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_trussonlyn():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.TrussOnlyN(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_tension():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Tension(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_compression():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Compression(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_buckling():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Buckling(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_cable():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Cable(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_resultbeam():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.ResultBeam(0, 1, 1, 2, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, MemberResultBeamIntegration.INTEGRATE_WITHIN_CUBOID_QUADRATIC, [0], 1, 1,  integration_parameters = [0.1])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_definablestiffness():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    MemberDefinableStiffness(1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.DefinableStiffness(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_couplingrigidrigid():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.CouplingRigidRigid(0, 1, 1, 2)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_couplingrigidhinge():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.CouplingRigidHinge(0, 1, 1, 2)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_couplinghingerigid():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.CouplingHingeRigid(0, 1, 1, 2)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_couplinghingehinge():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.CouplingHingeHinge(0, 1, 1, 2)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5
