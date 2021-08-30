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
 
 print("Preparing...")
    
 clientModel.service.begin_modification()

 #nodes

 i = 1
 while i <= n:
  j = (i-1) * 5
  Node(j+1, 0.0, -(i-1)*d, 0.0)
  Node(j+2, 0.0, -(i-1)*d, -h)
  Node(j+3, l/2, -(i-1)*d, -h)
  Node(j+4, l, -(i-1)*d, -h)
  Node(j+5, l, -(i-1)*d, 0.0)
  i += 1

    
 # Nodal Supports
 i = 1
 nodes_no = ""
 while i <= n:
  j = (i-1) * 5
  nodes_no += str(j+1) + " "
  nodes_no += str(j+5) + " "
  i += 1
  nodes_no = nodes_no.rstrip(nodes_no[-1])    
  NodalSupport(1, nodes_no, NodalSupportType.HINGED, "Hinged support")

 #members
 Material (1 , 'S235')
 Material (2, 'C25/30')
 
    
 Section (1, 'HEM 700',1)
 Section (2, 'IPE 500',1)
 #members x direction 
 i = 1
 while i <= n:
  j = (i-1) * 5
  k = (i-1) * 4
  Member(k+1, MemberType.TYPE_BEAM, j+1, j+2, 0.0,  1, 1)
  Member(k+2, MemberType.TYPE_BEAM, j+2, j+3, 0.0,  2, 2)
  Member(k+3, MemberType.TYPE_BEAM, j+3, j+4, 0.0,  2, 2)
  Member(k+4, MemberType.TYPE_BEAM, j+4, j+5, 0.0,  1, 1)
  i += 1

 #members y direction 
 i = 1
 while i <= n-1:
  j = (i-1) * 5
  Member(int(4*n+i), MemberType.TYPE_BEAM, j+2, j+7, 0.0, 2, 2)
  Member(int(4*n+i + n-1), MemberType.TYPE_BEAM, j+4, j+9, 0.0, 2, 2)
  i += 1
 
 #VerticalBracing
 Material (3, 'EN AW-3004 H14')
 Section (3, 'IPE 80',3)
 i = 1
 j = int(4*n + 3*(n-1))
 while i <= n-1:
  k = j + (i-1)*4
  Member(k+1, MemberType.TYPE_TENSION, (i-1)*5+1, (i-1)*5+7, 0.0,  3, 3)
  Member(k+2, MemberType.TYPE_TENSION, (i-1)*5+2, (i-1)*5+6, 0.0,  3, 3)
  Member(k+3, MemberType.TYPE_TENSION, (i-1)*5+5, (i-1)*5+9, 0.0,  3, 3)
  Member(k+4, MemberType.TYPE_TENSION, (i-1)*5+4, (i-1)*5+10, 0.0, 3, 3)
  i += 1

 #HorizontalBracing
 i = 1
 j = (i-1) * 5 
 while i <= n-1:
  k = int(4*(n-1))
  Member(k+1, MemberType.TYPE_TENSION, j+2, j+8, 0.0,  3, 3)
  Member(k+2, MemberType.TYPE_TENSION, j+3, j+7, 0.0,  3, 3)
  Member(k+3, MemberType.TYPE_TENSION, j+3, j+9, 0.0,  3, 3)
  Member(k+4, MemberType.TYPE_TENSION, j+4, j+8, 0.0,  3, 3)

 
 print('Ready!')
 clientModel.service.finish_modification()
