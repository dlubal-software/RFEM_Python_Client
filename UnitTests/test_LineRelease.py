import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.dataTypes import inf
from RFEM.initModel import Model
from RFEM.enums import *
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.solid import Solid
from RFEM.SpecialObjects.lineReleaseType import LineReleaseType
from RFEM.SpecialObjects.lineRelease import LineRelease

if Model.clientModel is None:
    Model()

def test_LineRelease():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1)
    Section(1, 'IPE 120')
    Thickness(1, uniform_thickness_d= 0.1)

    Node(1,0,0,0)
    Node(2,10,0,0)
    Node(3,10,10,0)
    Node(4,0,10,0)
    Node(5,0,0,-10)
    Node(6,10,0,-10)
    Node(7,10,10,-10)
    Node(8,0,10,-10)

    Line(1,'1 2')
    Line(2,'2 3')
    Line(3,'3 4')
    Line(4,'4 1')
    Line(5,'5 6')
    Line(6,'6 7')
    Line(7,'7 8')
    Line(8,'8 5')
    Line(9,'1 5')
    Line(10,'2 6')
    Line(11,'3 7')
    Line(12,'4 8')

    Member(1, line=1)
    Member(2, line=2)
    Member(3, line=3)
    Member(4, line=4)
    Member(5, line=5)
    Member(6, line=6)
    Member(7, line=7)
    Member(8, line=8)
    Member(9, line=9)
    Member(10, line=10)
    Member(11, line=11)
    Member(12, line=12)

    Surface(1)
    Surface(2, '5 6 7 8')
    Surface(3, '1 5 9 10')
    Surface(4, '2 6 10 11')
    Surface(5, '3 7 11 12')
    Surface(6, '4 8 9 12')

    Solid(1, '1 2 3 4 5 6')

    LineReleaseType(1, [0, inf, inf, 0])
    LineReleaseType(2, [0, 0, 0, 0])

    LineRelease(1, '1', 1, LineReleaseReleaseLocation.RELEASE_LOCATION_ORIGIN, '1', '1 3', '1', '1 2', name='LR 1')
    LineRelease(2, '2 3', 2, LineReleaseReleaseLocation.RELEASE_LOCATION_RELEASED, '2 3 11', '1 4 5', '1', '2 4')

    Model.clientModel.service.finish_modification()

    lr1 = Model.clientModel.service.get_line_release(1)
    assert lr1.line_release_type == 1
    assert lr1.released_surfaces == '1 3'
    assert lr1.name == 'LR 1'

    lr2 = Model.clientModel.service.get_line_release(2)
    assert lr2.lines == '2 3'
    assert lr2.release_location == "RELEASE_LOCATION_RELEASED"
    assert lr2.use_nodes_as_definition_nodes == '2 4'
