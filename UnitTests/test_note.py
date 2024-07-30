import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import NoteType, NoteOffsetType, NoteMemberReferenceType
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.GuideObjects.note import Note

if Model.clientModel is None:
    Model()

def test_note():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material()
    Section()
    Node(1, 0, 0, 0)
    Node(2, 10, 0, 0)
    Node(3, 10, 10, 0)
    Node(4, 0, 10, 0)

    Member(1, 1, 2)

    Note(1, 'Point 1', NoteType.NOTE_TYPE_POINT, [5, 0, -5], None, 0, 0)
    Note(2, 'Node 2', NoteType.NOTE_TYPE_NODE, 2, [NoteOffsetType.OFFSET_TYPE_XYZ, 3, -2, -3], 0.1, 1, 'Node', True)
    Note(4, 'Member 1', NoteType.NOTE_TYPE_MEMBER, [1, NoteMemberReferenceType.REFERENCE_TYPE_XY, False, 7], [NoteOffsetType.OFFSET_TYPE_XZ, -2, -2], 0, 3)

    Model.clientModel.service.finish_modification()

    note1 = Model.clientModel.service.get_note(1)
    assert note1.type == 'NOTE_TYPE_POINT'
    assert note1.offset == False

    note2 = Model.clientModel.service.get_note(2)
    assert note2.node == 2
    assert note2.offset_type == 'OFFSET_TYPE_XYZ'
    assert note2.name == 'Node'

    note4 = Model.clientModel.service.get_note(4)
    assert note4.member == 1
    assert note4.member_distance_absolute == 7
