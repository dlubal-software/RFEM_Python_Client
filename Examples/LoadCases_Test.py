#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import name
import sys
sys.path.append(".")

# Import der Bibliotheken
from RFEM.Loads.lineLoad import LineLoad
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

	StaticAnalysisSettings()
	LoadCase(1, 'SW', True, AnalysisType.ANALYSIS_TYPE_STATIC, 1, 'Permanent | G', [True, 0, 0, 1])
	LoadCase(2, 'SDL', True, AnalysisType.ANALYSIS_TYPE_STATIC, 1, 'Permanent/Imposed | Gq', [True, 0.1, 0.1, 0])
	LoadCase(3, 'Snow', True, AnalysisType.ANALYSIS_TYPE_STATIC, 1, 'Snow / Ice loads - H &gt; 1000 m | Qs', [False])
	LoadCase(4, 'Wind', True, AnalysisType.ANALYSIS_TYPE_STATIC, 1, 'Wind | Qw', [False])


	clientModel.service.finish_modification()