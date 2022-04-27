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
from RFEM.BasicObjects.memberSet import MemberSet

if Model.clientModel is None:
    Model()

def test_member_set():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 10, 0, 0)

    Material(1, 'S235')

    Section(1, 'IPE 300', 1)

    Member(1, 1, 2, 0, 1, 1)
    Member(2, 2, 3, 0, 1, 1)

    MemberSet(1, '1 2', SetType.SET_TYPE_CONTINUOUS)

    Model.clientModel.service.finish_modification()

    member_set = Model.clientModel.service.get_member_set(1)

    assert member_set.members == '1 2'
    assert member_set.length == 10
    assert member_set.set_type == SetType.SET_TYPE_CONTINUOUS.name

def test_member_set_continuous():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 5, 0, 5)

    Material(1, 'S235')

    Section(1, 'IPE 300', 1)

    Member(1, 1, 2, 0, 1, 1)
    Member(2, 2, 3, 0, 1, 1)

    MemberSet.ContinuousMembers(1, '1 2')

    Model.clientModel.service.finish_modification()

    member_set = Model.clientModel.service.get_member_set(1)

    assert member_set.members == '1 2'
    assert member_set.length == 10
    assert member_set.set_type == SetType.SET_TYPE_CONTINUOUS.name

def test_member_set_group():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 5, 5, 0)

    Material(1, 'S235')

    Section(1, 'IPE 300', 1)

    Member(1, 1, 2, 0, 1, 1)
    Member(2, 2, 3, 0, 1, 1)

    MemberSet.GroupOfmembers(1, '1 2')

    Model.clientModel.service.finish_modification()

    member_set = Model.clientModel.service.get_member_set(1)

    assert member_set.members == '1 2'
    assert member_set.length == 10
    assert member_set.set_type == SetType.SET_TYPE_GROUP.name