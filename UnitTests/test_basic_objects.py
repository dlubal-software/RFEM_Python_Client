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
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.opening import Opening
from RFEM.BasicObjects.lineSet import LineSet
from RFEM.BasicObjects.memberSet import MemberSet

if Model.clientModel is None:
    Model()

def test_line_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)
    Node(2, 4, 0, 0)

    Line(1, '1 2')

    Model.clientModel.service.finish_modification()

    line = Model.clientModel.service.get_line(1)

    assert line.no == 1
    assert line.length == 2

def test_line_polyline():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Line.Polyline(1, '1 2')

    Model.clientModel.service.finish_modification()

    line = Model.clientModel.service.get_line(1)

    assert line.no == 1
    assert line.length == 5

def test_line_arc():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)
    Node(2, 4, 0, 0)

    Line.Arc(1, [1, 2], [3, 3, 0], LineArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC)

    Model.clientModel.service.finish_modification()

    line = Model.clientModel.service.get_line(1)

    assert line.no == 1
    assert line.type == "TYPE_ARC"

def test_line_circle():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Line.Circle(1, [5, 6, 7], 3, [0, 0, 1])

    Model.clientModel.service.finish_modification()

    line = Model.clientModel.service.get_line(1)

    assert line.no == 1
    assert line.circle_radius == 3
    assert line.circle_center_coordinate_1 == 5
    assert line.circle_center_coordinate_2 == 6
    assert line.circle_center_coordinate_3 == 7

def test_line_ellipse():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1,2,0,0)
    Node(2,-2,0,0)
    Line.Ellipse(2,[1,2],[0,1,0])

    Model.clientModel.service.finish_modification()

    line = Model.clientModel.service.get_line(2)

    assert round(line.length, 4) == 9.6884

def test_line_parabola():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1,2,0,0)
    Node(2,-2,0,0)
    Line.Parabola(3,[1,2],[0,1,0],0.17453)

    Model.clientModel.service.finish_modification()

    line = Model.clientModel.service.get_line(3)

    assert round(line.length, 3) == 4.605

def test_line_spline():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1,2,0,0)
    Node(2,1,1,0)
    Node(3,0,-1,0)
    Node(4,-1,1,0)
    Node(5,-2,0,0)
    Line.Spline(1, "1-5")

    Model.clientModel.service.finish_modification()

    line = Model.clientModel.service.get_line(1)

    assert round(line.length, 4) == 8.42290

def test_line_elipticalArc():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Line.EllipticalArc(1)
    Line.EllipticalArc(2, [2,0,0], [-2,0,0], [0,-3,0], 0.17453, 2.79252)

    Model.clientModel.service.finish_modification()

    line = Model.clientModel.service.get_line(2)
    assert line.type == 'TYPE_ELLIPTICAL_ARC'

def test_lineSetInit():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)
    Node(2, 4, 0, 0)
    Node(3, 6, 0, 0)

    Line(1, '1 2')
    Line(2, '2 3')

    LineSet(1, '1 2')

    Model.clientModel.service.finish_modification()

    line_set = Model.clientModel.service.get_line_set(1)

    assert line_set.length == 4

def test_lineSetContinuous():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)
    Node(2, 4, 0, 0)
    Node(3, 6, 1, 0)

    Line(1, '1 2')
    Line(2, '2 3')

    LineSet.ContinuousLines(1, '1 2')

    Model.clientModel.service.finish_modification()

    line_set = Model.clientModel.service.get_line_set(1)

    assert round(line_set.length, 5) == 4.23607

def test_lineSetGroup():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)
    Node(2, 4, 1, 0)
    Node(3, 6, 0, 0)

    Line(1, '1 2')
    Line(2, '2 3')

    LineSet.GroupOfLines(2, '1 2')

    Model.clientModel.service.finish_modification()

    line_set = Model.clientModel.service.get_line_set(2)

    assert round(line_set.length, 6) == 4.472136

def test_line_delete():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 0, 0, -5)
    Node(3, 5, 0, -5)
    Node(4, 5, 0, 0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line.DeleteLine('2 4')

    Model.clientModel.service.finish_modification()

    modelInfo = Model.clientModel.service.get_model_info()

    assert modelInfo.property_line_count == 2

def test_material():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Model.clientModel.service.finish_modification()

    material = Model.clientModel.service.get_material(1)
    assert material.no == 1
    assert material.name == 'S235 | CYS EN 1993-1-1:2009-03'

def test_node_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)

    node = Model.clientModel.service.get_node(1)
    
    Model.clientModel.service.finish_modification()

    assert node.no == 1
    assert node.coordinate_1 == 2

def test_member_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')

    Section(1, 'IPE 300', 1)

    Member(1,  1, 2, 0, 1, 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.analytical_length == 5
    assert member.section_start == 1

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

    MemberSet(1, '1 2', SetType.SET_TYPE_GROUP)

    Model.clientModel.service.finish_modification()

    member_set = Model.clientModel.service.get_member_set(1)

    assert member_set.members == '1 2'
    assert member_set.length == 10

def test_member_delete():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 10, 0, 0)

    Material(1, 'S235')

    Section(1, 'IPE 300', 1)

    Member(1, 1, 2, 0, 1, 1)
    Member(2, 2, 3, 0, 1, 1)

    Member.DeleteMember('1')

    Model.clientModel.service.finish_modification()

    modelInfo = Model.clientModel.service.get_model_info()

    assert modelInfo.property_member_count == 1

## Bugs must be solved in Node.py

def test_opening():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

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

    Model.clientModel.service.finish_modification()

    opening = Model.clientModel.service.get_opening(1)

    assert opening.area == 1
    assert opening.center_of_opening_x == 2.5

def test_section():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300')

    Model.clientModel.service.finish_modification()

    section = Model.clientModel.service.get_section(1)

    assert section.no == 1
    assert section.name == 'IPE 300 | -- | British Steel'

## Solid Class should be updated.

## SolidSet Class should be updated.

## Surface Class should be update. Thickness no can't be assigned.

def test_thickness_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '20 mm', 1, 0.02)

    Model.clientModel.service.finish_modification()

    thickness = Model.clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_UNIFORM"
    assert thickness.uniform_thickness == 0.02

def test_thickness_uniform():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness.Uniform(1, '1', 1, [0.03])

    Model.clientModel.service.finish_modification()

    thickness = Model.clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_UNIFORM"
    assert thickness.uniform_thickness == 0.03

def test_thickness_3nodes():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 4, 0, 0)
    Node(2, 2, 2, 0)
    Node(3, 3, 4, 0)

    Thickness.Variable_3Nodes(1, '2', 1, [0.2, 1, 0.1, 2, 0.05, 3])

    Model.clientModel.service.finish_modification()

    thickness = Model.clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_VARIABLE_THREE_NODES"
    assert thickness.thickness_1 == 0.2

def test_thickness_2nodes():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 4, 0, 0)
    Node(2, 2, 2, 0)

    Thickness.Variable_2NodesAndDirection(1, '3', 1, [0.2, 1, 0.1, 2, ThicknessDirection.THICKNESS_DIRECTION_IN_X])
    Model.clientModel.service.finish_modification()

    thickness = Model.clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_VARIABLE_TWO_NODES_AND_DIRECTION"
    assert thickness.thickness_2 == 0.1

def test_thickness_4corners():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0, 0, 0)
    Node(2, 3, 0, 0)
    Node(3, 3, 3, 0)
    Node(4, 0, 3, 0)

    Thickness.Variable_4SurfaceCorners(1, '4', 1, [0.2, 1, 0.15, 2, 0.1, 3, 0.05, 4])

    Model.clientModel.service.finish_modification()

    thickness = Model.clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_VARIABLE_FOUR_SURFACE_CORNERS"
    assert thickness.thickness_2 == 0.15

def test_thickness_circle():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness.Variable_Circle(1, '5', 1, [0.2, 0.1])

    Model.clientModel.service.finish_modification()

    thickness = Model.clientModel.service.get_thickness(1)

    assert thickness.type == "TYPE_VARIABLE_CIRCLE"
    assert thickness.thickness_circle_line == 0.1

def test_thickness_shape_orthotropy():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')

    Thickness.ShapeOrthotropy(1, 'EFFECTIVE_THICKNESS', 1, ThicknessOrthotropyType.EFFECTIVE_THICKNESS, 7)
    Thickness.ShapeOrthotropy(2, 'COUPLING', 1, ThicknessOrthotropyType.COUPLING, 8, parameters=[0.15,0.18,0.16])
    Thickness.ShapeOrthotropy(3, 'UNIDIRECTIONAL_RIBBED_PLATE', 1, ThicknessOrthotropyType.UNIDIRECTIONAL_RIBBED_PLATE, 9, parameters=[0.15, 0.15,0.18,0.16])
    Thickness.ShapeOrthotropy(4, 'BIDIRECTIONAL_RIBBED_PLATE', 1, ThicknessOrthotropyType.BIDIRECTIONAL_RIBBED_PLATE, 10, parameters=[0.15, 0.3,0.25, 0.8,0.75,0.2,0.15])
    Thickness.ShapeOrthotropy(5, 'TRAPEZOIDAL_SHEET', 1, ThicknessOrthotropyType.TRAPEZOIDAL_SHEET, 11, parameters=[0.15, 0.45,0.4,0.14,0.14])
    Thickness.ShapeOrthotropy(6, 'HOLLOW_CORE_SLAB', 1, ThicknessOrthotropyType.HOLLOW_CORE_SLAB, 12, parameters=[0.2, 0.15, 0.1])
    Thickness.ShapeOrthotropy(7, 'GRILLAGE', 1, ThicknessOrthotropyType.GRILLAGE, 13,[ThicknessShapeOrthotropySelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, 0.15], [0.15,0.8,0.75,0.2,0.15])

    Model.clientModel.service.finish_modification()
