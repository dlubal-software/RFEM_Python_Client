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
from math import *

# Import der Bibliotheken
#from RFEM.window import *

if __name__ == '__main__':

  l = float(input('Length of the clear span in m: '))
  n = int(input('Number of frames: '))
  d = float(input('Distance between frames in m: '))
  h = float(input('Height of frame in m: '))

  Model(False)
  Model.clientModel.service.reset()
  Model.clientModel.service.begin_modification()

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
    Member(k+1,  j+1, j+2, 0.0,  1, 1)
    Member(k+2,  j+2, j+3, 0.0,  2, 2)
    Member(k+3,  j+3, j+4, 0.0,  2, 2)
    Member(k+4,  j+4, j+5, 0.0,  1, 1)
    i += 1

  #members y direction
  i = 1
  while i <= n-1:
    j = (i-1) * 5
    Member(4*n+i,  j+2, j+7, 0.0, 2, 2)
    Member(4*n+i + n-1,  j+4, j+9, 0.0, 2, 2)
    i += 1

  #vertical bracing
  #add a question about repeating in every block, one yes one no, only beginning and end

  BracingV = input('Would you like to include vertical bracing? (Y/N)')
  if BracingV.lower() == 'yes' or BracingV.lower() == 'y':
   BracingV_C1 = input('Would you like to repeat a vertical bracing in every block? (Y/N)')
   if BracingV_C1.lower() == 'yes' or BracingV_C1.lower() == 'y':
    Material (3, 'EN AW-3004 H14')
    Section (3, 'IPE 80',3)
    i = 1
    j = 4*n + 3*(n-1)
    while i <= n-1:
     k = n*4+(n-1)*2
     Member(k+1+4*(i-1), (i-1)*5+1, (i-1)*5+7, 0.0, 3, 3)
     Member(k+2+4*(i-1), (i-1)*5+2, (i-1)*5+6, 0.0, 3, 3)
     Member(k+3+4*(i-1), (i-1)*5+5, (i-1)*5+9, 0.0, 3, 3)
     Member(k+4+4*(i-1), (i-1)*5+4, (i-1)*5+10, 0.0, 3, 3)
     # print(k+1+4*(i-1), k+2+4*(i-1), k+3+4*(i-1), k+4+4*(i-1))
     i += 1
   BracingV_C2 = input('Would you like to repeat a vertical bracing only in the first and last block? (Y/N)')
   if BracingV_C2.lower() == 'yes' or BracingV_C2.lower() == 'y':
    Material (3, 'EN AW-3004 H14')
    Section (3, 'IPE 80',3)
    i = 1
    while i <= n-1:
     k = n*4+(n-1)*2
     if i == 1 or i == n-1:
      Member.Tension(0,k+1+4*(i-1), (i-1)*5+1, (i-1)*5+7, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
      Member.Tension(0,k+2+4*(i-1), (i-1)*5+2, (i-1)*5+6, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
      Member.Tension(0,k+3+4*(i-1), (i-1)*5+5, (i-1)*5+9, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
      Member.Tension(0,k+4+4*(i-1), (i-1)*5+4, (i-1)*5+10, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
     #  print(k+1+4*(i-1), k+2+4*(i-1), k+3+4*(i-1), k+4+4*(i-1))
     i += 1
   BracingV_C3 = input('Would you like to repeat a vertical bracing in even/odd blocks? (Y/N)') # MAKE IT MORE GENERAL!
   if BracingV_C3.lower() == 'yes' or BracingV_C3.lower() == 'y':
    Material (3, 'EN AW-3004 H14')
    Section (3, 'IPE 80',3)
    i = 1
    j = 4*n + 3*(n-1)
    while i <= n-1:
     if i% 2 != 0:
      k = n*4+(n-1)*2
      Member.Tension(0,k+1+4*(i-1), (i-1)*5+1, (i-1)*5+7, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
      Member.Tension(0,k+2+4*(i-1), (i-1)*5+2, (i-1)*5+6, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
      Member.Tension(0,k+3+4*(i-1), (i-1)*5+5, (i-1)*5+9, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
      Member.Tension(0,k+4+4*(i-1), (i-1)*5+4, (i-1)*5+10, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
     #  print(k+1+4*(i-1), k+2+4*(i-1), k+3+4*(i-1), k+4+4*(i-1))
     i += 1

  #horizontal bracing
  #add a question about repeating in every block, one yes one no, only beginning and end

  member_count = n*4+(n-1)*2
  BracingH = input('Would you like to include horizontal bracing? (Y/N)')
  if BracingV.lower() == 'yes' or BracingV.lower() == 'y':
   member_count += (n-1)*4
   BracingH = 'yes'
   if BracingH.lower() == 'yes' or BracingH.lower() == 'y':
    i = 1
    while i <= n-1:
     j = (i-1) * 5
     Member(int(member_count+1+4*(i-1)),  j+2, j+8, 0.0, 3, 3)
     Member(int(member_count+2+4*(i-1)),  j+3, j+7, 0.0, 3, 3)
     Member(int(member_count+3+4*(i-1)),  j+3, j+9, 0.0, 3, 3)
     Member(int(member_count+4+4*(i-1)),  j+4, j+8, 0.0, 3, 3)
     # print(int(member_count+1+4*(i-1)),int(member_count+2+4*(i-1)),int(member_count+3+4*(i-1)),int(member_count+4+4*(i-1)))
     i += 1
  print("Preparing...")
  print('Ready!')
  Model.clientModel.service.finish_modification()