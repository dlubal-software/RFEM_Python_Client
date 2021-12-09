#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append(".")

# Import the relevant Libraries
from os import name
from RFEM.enums import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness 
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.solid import Solid
from RFEM.BasicObjects.opening import Opening
from RFEM.BasicObjects.lineSet import LineSet
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.BasicObjects.surfaceSet import SurfaceSet
from RFEM.BasicObjects.solidSet import SolidSet
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Loads.surfaceLoad import SurfaceLoad

def test_membrane_surface():
    Model(True, "MemberSurface")
    Model.clientModel.service.begin_modification('new')

    # Testing the standard surface function
    Node(1, 0, -30, 0), Node(2, 10, -30, 0), Node(3, 10, -20, 0), Node(4, 0, -20, 0)
    Line(1, '1 2'), Line(2, '2 3'), Line(3, '3 4'), Line(4, '4 1')
    Material(name='C30/37')
    Thickness()
    Surface()

    # Standard planar Surface
    Node(5, 0, -15, 0), Node(6, 10, -15, 0), Node(7, 10, -5, 0), Node(8, 0, -5, 0)
    Line(5, '5 6'), Line(6, '6 7'), Line(7, '7 8'), Line(8, '8 5')
    Surface.Membrane(Surface, 2, SurfaceGeometry.GEOMETRY_PLANE, boundary_lines_no= '5 6 7 8')

    # Standard NURBS Surface

    ## Define Nodes
    Node(9, 0.0, 0.0, 0.0)
    Node(10, 5.0, 0.0, -2.5)
    Node(11, 10.0, 0.0, 0.0)
    Node(12, 0.0, 10.0, 0.0)
    Node(13, 5.0, 10.0, -2.5)
    Node(14, 10.0, 10.0, 0.0)
    Node(15, 0.0, 5.0, -2,5)
    Node(16, 10.0, 5.0, -2.5)

    ## NURBS-Curve Definition
    Line.NURBS(Line, 9, '9 10 11', control_points= [[0, 0, 0], [5, 0, -2.5], [10, 0, 0]], weights= [1, 1, 1],params= {'nurbs_order':3})
    Line.NURBS(Line, 10, '12 13 14', control_points= [[0, 10, 0], [5, 10, -2.5], [10, 10, 0]], weights= [1, 1, 1], params= {'nurbs_order':3})
    Line.NURBS(Line, 11, '9 15 12', control_points= [[0, 0, 0], [0, 5, -2.5], [0, 10, 0]], weights= [1, 1, 1], params= {'nurbs_order':3})
    Line.NURBS(Line, 12, '11 16 14', control_points= [[10, 0, 0], [10, 5, -2.5], [10, 5, -2.5]], weights= [1, 1, 1], params= {'nurbs_order':3})

    # Surfaces Definition
    Surface.Membrane(Surface, 4, SurfaceGeometry.GEOMETRY_NURBS, [3,3,3,3], '9 10 11 12')

    # Standard Quadrangle

    # Define Nodes
    Node(17, 0, 15, 0)
    Node(18, 10, 15, 0)
    Node(19, 0, 20, 0)
    Node(20, 10, 20, 0)

    # Boundary Lines
    Line.Arc(1, 13, [17, 18], [5, 15, -2])
    Line.Arc(1, 14, [19, 20], [5, 20, -2])
    Line(15, '17 19')
    Line(16, '18 20')

    # Quadrangle Defintion
    Surface.Membrane(Surface, 5, SurfaceGeometry.GEOMETRY_QUADRANGLE, [17, 18, 19, 20], '13 14 15 16')

    Model.clientModel.service.finish_modification()

