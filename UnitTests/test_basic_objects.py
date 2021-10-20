import sys
sys.path.append(".")
from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.solidSet import *
from RFEM.BasicObjects.memberByLine import *

def test_line_init():
    
    clientModel.service.reset()
    clientModel.service.begin_modification()

    Node(1, 2, 0, 0)
    Node(2, 4, 0, 0)

    Line(1, '1 2')

    clientModel.service.finish_modification()

    line = clientModel.service.get_line(1)

    assert line.no == 1
    assert line.length == 2

def test_line_polyline():
    
    clientModel.service.reset()
    clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Line.Polyline(0, 1, '1 2')

    clientModel.service.finish_modification()

    line = clientModel.service.get_line(1)

    assert line.no == 1
    assert line.length == 5

def test_line_arc():
    
    clientModel.service.reset()
    clientModel.service.begin_modification()

    Node(1, 2, 0, 0)
    Node(2, 4, 0, 0)

    Line.Arc(0, 1, [1, 2], [3, 3, 0], LineArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC)

    clientModel.service.finish_modification()

    line = clientModel.service.get_line(1)

    assert line.no == 1
    assert line.type == "TYPE_ARC"

def test_line_circle():
    
    clientModel.service.reset()
    clientModel.service.begin_modification()

    Line.Circle(0, 1, '1', [0, 0, 0], 3, [0, 0, 1])

    clientModel.service.finish_modification()

    line = clientModel.service.get_line(1)

    assert line.no == 1
    assert line.circle_radius == 3

def test_lineSet():
    
    clientModel.service.reset()
    clientModel.service.begin_modification()

    Node(1, 2, 0, 0)
    Node(2, 4, 0, 0)
    Node(3, 6, 0, 0)

    Line(1, '1 2')
    Line(2, '2 3')

    LineSet(1, '1 2', SetType.SET_TYPE_CONTINUOUS)
    
    clientModel.service.finish_modification()

    line_set = clientModel.service.get_line_set(1)

    assert line_set.no == 1
    assert line_set.length == 4

def test_material():
    
    clientModel.service.reset()
    clientModel.service.begin_modification()

    Material(1, 'S235')
    
    clientModel.service.finish_modification()

    material = clientModel.service.get_material(1)
    assert material.no == 1
    assert material.name == 'S235'

def test_node_init():

    clientModel.service.reset()
    clientModel.service.begin_modification()
    
    Node(1, 2, 0, 0)
   
    node = clientModel.service.get_node(1)

    assert node.no == 1
    assert node.coordinate_1 == 2

def test_memberbyline_init():

    clientModel.service.reset()
    clientModel.service.begin_modification()
    
    Material(1, 'S235')
    Node(1, 0, 0, 0)
    Node(2, 4, 0, 0)
    Node(3, )

    Line(1, '1 2')

    Section(1, 'IPE 240', 1)

    MemberByLine(1, MemberType.TYPE_BEAM, 1, 0, 1, 1)
    
    clientModel.service.finish_modification()

    member = clientModel.service.get_member(1)

    assert member.analytical_length == 4
    assert member.section_start == 1


def test_member_init():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')

    Section(1, 'IPE 300', 1)

    Member(1, MemberType.TYPE_BEAM, 1, 2, 0, 1, 1)
    
    clientModel.service.finish_modification()

    member = clientModel.service.get_member(1)

    assert member.analytical_length == 5
    assert member.section_start == 1

def test_member_beam():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 6, 0, 0)

    Material(1, 'S235')

    Section(1, 'IPE 300', 1)

    Member.Beam(0, 1, 1, 2, 0, 1, 1)
    
    clientModel.service.finish_modification()

    member = clientModel.service.get_member(1)

    assert member.analytical_length == 6
    assert member.type == "TYPE_BEAM"
    
## Other Member Types must be added to the main code.

def test_member_set():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 10, 0, 0)

    Material(1, 'S235')

    Section(1, 'IPE 300', 1)

    Member(1, MemberType.TYPE_BEAM, 1, 2, 0, 1, 1)
    Member(2, MemberType.TYPE_BEAM, 2, 3, 0, 1, 1)

    MemberSet(1, '1 2', SetType.SET_TYPE_GROUP)

    clientModel.service.finish_modification()

    member_set = clientModel.service.get_member_set(1)

    assert member_set.members == '1 2'
    assert member_set.length == 10

## Bugs must be solved in Node.py

def test_opening():
    
    clientModel.service.reset()
    clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 4, 0, 0)
    Node(3, 0, 4, 0)
    Node(4, 4, 4, 0)

    Node(5, 2, 2, 0)
    Node(6, 3, 2, 0)
    Node(7, 3, 3, 0)
    Node(8, 2, 3, 0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Line(5, '5 6')
    Line(6, '5 8')
    Line(7, '8 7')
    Line(8, '7 6')

    Material(1, 'S235')
    Thickness(1, '20 mm', 1, 0.02)

    Surface(1, '1 2 3 4', 1)

    Opening(1, '5 6 7 8')

    clientModel.service.finish_modification()

    opening = clientModel.service.get_opening(1)

    assert opening.area == 1
    assert opening.center_of_opening_x == 2.5

def test_section():
    
    clientModel.service.reset()
    clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300')

    clientModel.service.finish_modification()

    section = clientModel.service.get_section(1)

    assert section.no == 1
    assert section.name == 'IPE 300'


## Solid Class should be updated.

## SolidSet Class should be updated.

## Surface Class should be update. Thickness no can't be assigned.

def test_thickness_init():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '20 mm', 1, 0.02)

    clientModel.service.finish_modification()

    thickness = clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_UNIFORM"
    assert thickness.uniform_thickness == 0.02

def test_thickness_uniform():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness.Uniform(0, 1, '1', 1, [0.03])


    clientModel.service.finish_modification()

    thickness = clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_UNIFORM"
    assert thickness.uniform_thickness == 0.03

def test_thickness_3nodes():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 4, 0, 0)
    Node(2, 2, 2, 0)
    Node(3, 3, 4, 0)

    Thickness.Variable_3Nodes(0, 1, '2', 1, [0.2, 1, 0.1, 2, 0.05, 3])

    clientModel.service.finish_modification()

    thickness = clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_VARIABLE_THREE_NODES"
    assert thickness.thickness_1 == 0.2

def test_thickness_2nodes():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 4, 0, 0)
    Node(2, 2, 2, 0)

    Thickness.Variable_2NodesAndDirection(0, 1, '3', 1, [0.2, 1, 0.1, 2, ThicknessDirection.THICKNESS_DIRECTION_IN_X])    
    clientModel.service.finish_modification()

    thickness = clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_VARIABLE_TWO_NODES_AND_DIRECTION"
    assert thickness.thickness_2 == 0.1

def test_thickness_4corners():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0, 0, 0)
    Node(2, 3, 0, 0)
    Node(3, 3, 3, 0)
    Node(4, 0, 3, 0)

    Thickness.Variable_4SurfaceCorners
    clientModel.service.finish_modification()

    Thickness.Variable_4SurfaceCorners(0, 1, '4', 1, [0.2, 1, 0.15, 2, 0.1, 3, 0.05, 4])

    thickness = clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_VARIABLE_FOUR_SURFACE_CORNERS"
    assert thickness.thickness_2 == 0.15

def test_thickness_circle():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness.Variable_Circle(0, 1, '5', 1, [0.2, 0.1])

    clientModel.service.finish_modification()


    thickness = clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_VARIABLE_CIRCLE"
    assert thickness.thickness_circle_line == 0.1

def test_thickness_layers():

    clientModel.service.reset()
    clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness.Layers(0, 1, '6', [[0, 1, 0.1, 0, ''], [0, 1, 0.2, 0, '']])
    clientModel.service.finish_modification()


    thickness = clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_LAYERS"
    assert round(thickness.layers_total_thickness, 2) == 0.3

## Thickness type Shape Orthotropy has bugs. Need to be updated

