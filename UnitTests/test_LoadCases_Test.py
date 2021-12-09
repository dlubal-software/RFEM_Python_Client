import sys
sys.path.append(".")

# Import der Bibliotheken
from RFEM.Loads.lineLoad import LineLoad
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

def test_load_case():
	Model(True, "LoadCases")
	Model.clientModel.service.begin_modification('new')

	StaticAnalysisSettings()
	LoadCase.StaticAnalysis(LoadCase, 1, 'SW', True, 1, DIN_Action_Category['1A'], [True, 0, 0, 1])
	LoadCase.StaticAnalysis(LoadCase, 2, 'SDL', True,  1, DIN_Action_Category['1C'], [True, 0.1, 0.1, 0])
	LoadCase.StaticAnalysis(LoadCase, 3, 'Snow', True,  1, DIN_Action_Category['4A'], [False])
	LoadCase.StaticAnalysis(LoadCase, 4, 'Wind', False,  1, DIN_Action_Category['5'], [False])

	Model.clientModel.service.finish_modification()
