Hall Example
%import libraries*
import sys

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
from RFEM.TypesForSurfaces.surfaceSupport import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.lineLoad import *
from RFEM.Loads.surfaceLoad import *

if __name__ == '__main__':

	l = float(input('Length of the clear span in m: '))
	x = float(input('Number of frames: '))
	a = float(input('Distance between frames in m: '))
   
   clientModel.service.begin_modification('new')

   Material (1 , 'S235')
   Material (2, 'C25/30')
   Material (3, 'EN AW-3004 H14')
   
   Section (1, 'HEM 700')
   Section (2, 'IPE 500')
   Section (3, 'IPE 80')

   NodalSupport(1, '1' , NodalSupportType.FIXED)
   NodalSupport(2, '3' , NodalSupportType.FIXED)
   NodalSupport(3, '9' , NodalSupportType.FIXED)
   NodalSupport(4, '12' , NodalSupportType.FIXED)

   
   Node (2, 0 , 0 , -15)
   Node (10, 15 , 0 , -15)
   Node (11, 15 , -30 , -15)
   Node (4, 0 , -30 , -15)

   %Between2Nodes:??

  

   %MembersDefinition
     %ColumnsDefinition
   Member (1, MemberType.TYPE_BEAM, 1, 2, 0.0, 1, 1)
   Member (2, MemberType.TYPE_BEAM, 3, 4, 0.0, 1, 1)
   Member (12, MemberType.TYPE_BEAM, 9, 10, 0.0, 1, 1)
   Member (15, MemberType.TYPE_BEAM,  12, 11, 0.0, 1, 1)
     %BeamsDefinition
   Member (9, MemberType.TYPE_BEAM, 2, 10, 0.0, 2, 2)
   Member (8, MemberType.TYPE_BEAM, 10, 11, 0.0, 2, 2)
   Member (11, MemberType.TYPE_BEAM, 11, 4, 0.0, 2, 2)
   Member (6, MemberType.TYPE_BEAM , 4, 2, 0.0, 2, 2)

   %Surfaces  ???
   Surface (1, '5 6 7 8', 1)
 
   %Bracing ??
   
  %Analysis
  StaticAnalysisSettings(1, '1. Order', StaticAnalysisType.GEOMETRICALLY_LINEAR)
  LoadCase(1 , 'Eigengewicht', SelfWeight.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)
  
  %Loads
  NodalLoad(1, 1, '# # # #', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z, 2.5 )
  
      
      Calculate_all()
      print('Ready!')


   clientModel.service.finish_modification()
   
