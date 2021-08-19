#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.Loads.surfaceLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.nodalLoad import *
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
from RFEM.BasicObjects.bracing import *
from RFEM.initModel import *
from RFEM.dataTypes import *
from RFEM.enums import *

if __name__ == '__main__':

	l = float(input('Length of the clear span in m: '))
	n = float(input('Number of frames: '))
	d = float(input('Distance between frames in m: '))
   
   clientModel.service.begin_modification('new')

   Material (1 , 'S235')
   Material (2, 'C25/30')
   Material (3, 'EN AW-3004 H14')
   
   Section (1, 'HEM 700',1)
   Section (2, 'IPE 500',1)
   Section (3, 'IPE 80',3)
  
   Node (1, 0 , 0 , 0)
   Node (2, 0 , 0 , -15)
   Node (3, 0 , 30 , -15)
   Node (4, 0 , 30 , 0)
	
   NodalSupport(1, '1 4' , NodalSupportType.FIXED)

   Frame(1,1,2,1,1,2,3,2,2,3,4,1,1)

   Bracing(1, BracingType.TYPE_VERTICAL, 2 , 5 , 0, 3, 3, 0, 0)
  
 XXX  %Surfaces 
   Surface (1, '5 6 7 8', 1)  XXXX
 
   
   
  %Analysis
  StaticAnalysisSettings(1, '1. Order', StaticAnalysisType.GEOMETRICALLY_LINEAR)
  LoadCase(1 , 'Eigengewicht', SelfWeight.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)
  
  %Loads
  NodalLoad(1, 1, '# # # #', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z, 2.5 )
  
      
      Calculate_all()
      print('Ready!')


   clientModel.service.finish_modification()
   
