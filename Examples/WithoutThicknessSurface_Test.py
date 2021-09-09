#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import der Bibliotheken
from os import name
from RFEM.enums import *
#from RFEM.window import *
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
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.surfaceLoad import *

if __name__ == '__main__':

    clientModel.service.begin_modification('new')

    # Prüfung der vorgegebenen Flächefunktion
    Node(1, 0, -30, 0), Node(2, 10, -30, 0), Node(3, 10, -20, 0), Node(4, 0, -20, 0)
    Line(1, '1 2'), Line(2, '2 3'), Line(3, '3 4'), Line(4, '4 1')
    Material(name='C30/37')
    Thickness()
    Surface()

    # STANDARD EBENE FLÄCHE
    Node(5, 0, -15, 0), Node(6, 10, -15, 0), Node(7, 10, -5, 0), Node(8, 0, -5, 0)
    Line(5, '5 6'), Line(6, '6 7'), Line(7, '7 8'), Line(8, '8 5')
    Surface.WithoutThickness(1, 2, boundary_lines_no= '5 6 7 8')

    # STANDARD NURBS FLÄCHE

    ## Knoten definieren
    Node(9, 0.0, 0.0, 0.0)
    Node(10, 5.0, 0.0, -2.5)
    Node(11, 10.0, 0.0, 0.0)
    Node(12, 0.0, 10.0, 0.0)
    Node(13, 5.0, 10.0, -2.5)
    Node(14, 10.0, 10.0, 0.0)
    Node(15, 0.0, 5.0, -2,5)
    Node(16, 10.0, 5.0, -2.5)

    ## NURBS-Kurve definieren
    Line.NURBS(Line, 9, '9 10 11', control_points= [[0, 0, 0], [5, 0, -2.5], [10, 0, 0]], weights= [1, 1, 1],params= {'nurbs_order':3})
    Line.NURBS(Line, 10, '12 13 14', control_points= [[0, 10, 0], [5, 10, -2.5], [10, 10, 0]], weights= [1, 1, 1], params= {'nurbs_order':3})
    Line.NURBS(Line, 11, '9 15 12', control_points= [[0, 0, 0], [0, 5, -2.5], [0, 10, 0]], weights= [1, 1, 1], params= {'nurbs_order':3})
    Line.NURBS(Line, 12, '11 16 14', control_points= [[10, 0, 0], [10, 5, -2.5], [10, 5, -2.5]], weights= [1, 1, 1], params= {'nurbs_order':3})

    # Fläche definieren
    Surface.WithoutThickness(1, 3, SurfaceGeometry.GEOMETRY_NURBS, [3,3,3,3], '9 10 11 12')

    # STANDARD QUADRANGEL FLÄCHE

    # Knoten definieren
    Node(17, 0, 15, 0)
    Node(18, 10, 15, 0)
    Node(19, 0, 20, 0)
    Node(20, 10, 20, 0)

    # Grenzenlinien definieren
    Line.Arc(1, 13, [17, 18], [5, 15, -2])
    Line.Arc(1, 14, [19, 20], [5, 20, -2])
    Line(15, '17 19')
    Line(16, '18 20')

    # Quadrangel definieren
    Surface.WithoutThickness(1, 4, SurfaceGeometry.GEOMETRY_QUADRANGLE, [17, 18, 19, 20], '13 14 15 16')

    clientModel.service.finish_modification()

