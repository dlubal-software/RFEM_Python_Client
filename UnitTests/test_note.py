import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import NoteType, NoteOffsetType, NoteMemberReferenceType, NoteSurfaceReferenceType
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.GuideObjects.note import Note

if Model.clientModel is None:
    Model()

def test_note():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material()
    Section()
    Thickness()
    Node(1, 0, 0, 0)
    Node(2, 10, 0, 0)
    Node(3, 10, 10, 0)
    Node(4, 0, 10, 0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Member(1, 1, 2)
    Surface(1, '1 2 3 4')

    Note(1, 'Point 1', NoteType.NOTE_TYPE_POINT, [5, 0, -5], None, 0, 0)
    Note(2, 'Node 2', NoteType.NOTE_TYPE_NODE, 2, [NoteOffsetType.OFFSET_TYPE_XYZ, 3, -2, -3], 0.1, 1, 'Node', True)
    Note(3, 'Line 2', NoteType.NOTE_TYPE_LINE, [2, NoteMemberReferenceType.REFERENCE_TYPE_L, True, 0.5], [NoteOffsetType.OFFSET_TYPE_XY, 2, 1], 0, 2, 'Line')
    Note(4, 'Member 1', NoteType.NOTE_TYPE_MEMBER, [1, NoteMemberReferenceType.REFERENCE_TYPE_XY, False, 7], [NoteOffsetType.OFFSET_TYPE_XZ, -2, -2], 0, 3)
    Note(5, 'Surface 1', NoteType.NOTE_TYPE_SURFACE, [1, NoteSurfaceReferenceType.OFFSET_TYPE_XY, 5, 5], [NoteOffsetType.OFFSET_TYPE_YZ, 2, -2], 0, 4)

    Model.clientModel.service.finish_modification()

    note1 = Model.clientModel.service.get_note(1)
    assert note1.type == 'NOTE_TYPE_POINT'
    assert note1.offset == False

    note2 = Model.clientModel.service.get_note(2)
    assert note2.node == 2
    assert note2.offset_type == 'OFFSET_TYPE_XYZ'
    assert note2.name == 'Node'

    note3 = Model.clientModel.service.get_note(3)
    assert note3.line == 2
    assert note3.display_properties_index == 2

    note4 = Model.clientModel.service.get_note(4)
    assert note4.member == 1
    assert note4.member_distance_absolute == 7

    note5 = Model.clientModel.service.get_note(5)
    assert note5.surface_first_coordinate == 5
    assert note5.offset_coordinate_y == 2
