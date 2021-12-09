import sys
sys.path.append(".")

# Import der Bibliotheken
from RFEM.enums import *
from RFEM.initModel import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase

def test_load_case():
    Model(True, "LoadCases")
    Model.clientModel.service.begin_modification('new')

    StaticAnalysisSettings()
    LoadCase.StaticAnalysis(LoadCase, 1, 'SW', True, 1, DIN_Action_Category['1A'], [True, 0, 0, 1])
    LoadCase.StaticAnalysis(LoadCase, 2, 'SDL', True,  1, DIN_Action_Category['1C'], [True, 0.1, 0.1, 0])
    LoadCase.StaticAnalysis(LoadCase, 3, 'Snow', True,  1, DIN_Action_Category['4A'], [False])
    LoadCase.StaticAnalysis(LoadCase, 4, 'Wind', False,  1, DIN_Action_Category['5'], [False])

    Model.clientModel.service.finish_modification()
