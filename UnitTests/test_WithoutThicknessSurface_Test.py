#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

## Import the relevant Libraries
from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface

if Model.clientModel is None:
    Model()

def test_without_thickness_surface():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Testing the standard surface function
    Node(1, 0, -30, 0), Node(2, 10, -30, 0), Node(3, 10, -20, 0), Node(4, 0, -20, 0)
    Line(1, '1 2'), Line(2, '2 3'), Line(3, '3 4'), Line(4, '4 1')
    Material(name='C30/37')
    Thickness()
    Surface()

    # Standard planar Surface
    Node(5, 0, -15, 0), Node(6, 10, -15, 0), Node(7, 10, -5, 0), Node(8, 0, -5, 0)
    Line(5, '5 6'), Line(6, '6 7'), Line(7, '7 8'), Line(8, '8 5')
    Surface.WithoutThickness(2, boundary_lines_no= '5 6 7 8')

    # Standard NURBS Surface

    # Define Nodes
    Node(9, 0.0, 0.0, 0.0)
    Node(10, 5.0, 0.0, -2.5)
    Node(11, 10.0, 0.0, 0.0)
    Node(12, 0.0, 10.0, 0.0)
    Node(13, 5.0, 10.0, -2.5)
    Node(14, 10.0, 10.0, 0.0)
    Node(15, 0.0, 5.0, -2,5)
    Node(16, 10.0, 5.0, -2.5)

    # NURBS-Curve Definition
    Line.NURBS(9, '9 10 11')
    Line.NURBS(10, '12 13 14')
    Line.NURBS(11, '9 15 12')
    Line.NURBS(12, '11 16 14')

    # Surfaces Definition
    Surface.WithoutThickness(3, SurfaceGeometry.GEOMETRY_NURBS, [3,3,3,3], '9 10 11 12')

    # Standard Quadrangle

    # Define Nodes
    Node(17, 0, 15, 0)
    Node(18, 10, 15, 0)
    Node(19, 0, 20, 0)
    Node(20, 10, 20, 0)

    # Boundary Lines
    Line.Arc(13, [17, 18], [5, 15, -2])
    Line.Arc(14, [19, 20], [5, 20, -2])
    Line(15, '17 19')
    Line(16, '18 20')

    # Quadrangle Defintion
    Surface.WithoutThickness(4, SurfaceGeometry.GEOMETRY_QUADRANGLE, [17, 18, 19, 20], '13 14 15 16')

    Model.clientModel.service.finish_modification()

    assert Model.clientModel.service.get_surface(1).type == 'TYPE_STANDARD'

    sur = Model.clientModel.service.get_surface(2)
    assert sur.type == 'TYPE_WITHOUT_THICKNESS'
    assert sur.boundary_lines == '5 6 7 8'

    sur = Model.clientModel.service.get_surface(3)
    assert sur.geometry == 'GEOMETRY_NURBS'
    assert sur.type == 'TYPE_WITHOUT_THICKNESS'
    assert sur.nurbs_control_point_count_in_direction_u == 3
    assert sur.nurbs_order_in_direction_v == 3

    sur = Model.clientModel.service.get_surface(4)
    assert sur.geometry == 'GEOMETRY_QUADRANGLE'
    assert sur.type == 'TYPE_WITHOUT_THICKNESS'
    assert sur.quadrangle_corner_node_2 == 18
    assert sur.quadrangle_corner_node_4 == 20
