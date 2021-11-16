import sys
sys.path.append(".")

# Import der Bibliotheken
from RFEM.Loads.lineLoad import LineLoad
from RFEM.enums import *
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
	Model(True, "LoadCases")
	Model.clientModel.service.begin_modification('new')

	StaticAnalysisSettings()
	LoadCase.StaticAnalysis(LoadCase, 1, 'SW', True, 1, DIN_Action_Category['1A'], [True, 0, 0, 1])
	LoadCase.StaticAnalysis(LoadCase, 2, 'SDL', True,  1, DIN_Action_Category['1C'], [True, 0.1, 0.1, 0])
	LoadCase.StaticAnalysis(LoadCase, 3, 'Snow', True,  1, DIN_Action_Category['4A'], [False])
	LoadCase.StaticAnalysis(LoadCase, 4, 'Wind', False,  1, DIN_Action_Category['5'], [False])

	Model.clientModel.service.finish_modification()