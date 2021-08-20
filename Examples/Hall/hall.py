#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import math
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.Loads.surfaceLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.lineLoad import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.BasicObjects.solidSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.frame import *
from RFEM.initModel import *
from RFEM.dataTypes import *
from RFEM.enums import *

# Import der Bibliotheken
#from RFEM.window import *

if __name__ == '__main__':

    l = float(input('Length of the clear span in m: '))
    n = float(input('Number of frames: '))
    d = float(input('Distance between frames in m: '))
    h = float(input('Height of frame in m: '))


    clientModel.service.begin_modification('new')
    
    # Geometry

    Material (1 , 'S235')
    Material (2, 'C25/30')
    Material (3, 'EN AW-3004 H14')
    
    Section (1, 'HEM 700',1)
    Section (2, 'IPE 500',1)
    Section (3, 'IPE 80',3)
    
    Node (1, 0 , 0 , 0)
    Node (2, 0 , 0 , -15)
    Node (3, 30 , 0 , -15)
    Node (4, 30 , 0 , 0)
    
    NodalSupport(1, '1 4' , NodalSupportType.FIXED)
    
    Surface(1, "1", 1)

    Frame(1,1,2,1,1,2,3,2,2,3,4,1,1)

    # Frames n
    i = 1
    while i <= n:
        j = (i-1) * 5
        Node(j+1, 0.0           , -(i-1) * d)
        Node(j+2, 0.0           , -(i-1) * d, -h)
        Node(j+3, l/2, -(i-1) * d, -h)
        Node(j+4, l  , -(i-1) * d, -h)
        Node(j+5, l  , -(i-1) * d)
        i += 1
     
   # Nodes n
   i = 1
   while i <= n:
        j = (i-1) * 5
        Node(j+1, 0.0           , -(i-1) * d)
        Node(j+2, 0.0           , -(i-1) * d, -h)
        Node(j+3, l/2, -(i-1) * d, -h)
        Node(j+4, l  , -(i-1) * d, -h)
        Node(j+5, l  , -(i-1) * d)
        i += 1
  
    # Nodal supports n
    i = 1
    nodes_no = ""
    while i <= ns:
        j = (i-1) * 5
        nodes_no += str(j+1) + " "
        nodes_no += str(j+5) + " "
        i += 1

    # Load
    StaticAnalysisSettings(1, '1. Order', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1 , 'Eigengewicht', SelfWeight.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)

   
    Calculate_all()
    print('Ready!')

    clientModel.service.finish_modification()
