#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import der Bibliotheken
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
	l = float(input('Length of the cantilever in m: '))
	f = float(input('Force in kN: '))
	
	clientModel.service.begin_modification('new')
	
	Material(1, 'S235')
	
	Section(1, 'IPE 200')
	
	Node(1, 0.0, 0.0, 0.0)
	Node(2, l, 0.0, 0.0)
	
	Member(1, MemberType.TYPE_BEAM, 1, 2, 0.0, 1, 1)
	
	NodalSupport(1, '1', NodalSupportType.FIXED)
	
	StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)
	
	LoadCase(1 , 'Eigengewicht', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)
	
	NodalLoad(1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, f*1000)
	
	Calculate_all()
	print('Ready!')
	
	clientModel.service.finish_modification()
	
