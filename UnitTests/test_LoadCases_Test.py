import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

# Import der Bibliotheken
import pytest
from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase, DIN_Action_Category

if Model.clientModel is None:
    Model()

@pytest.mark.skip("all tests still WIP")
def test_load_case():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    StaticAnalysisSettings()
    # TODO: DIN_Action_Category will only work with German localization
    # The action cat. is language dependent, which needs to be corrected.
    LoadCase.StaticAnalysis(LoadCase, 1, 'SW', True, 1, DIN_Action_Category['1A'], [True, 0, 0, 1])
    LoadCase.StaticAnalysis(LoadCase, 2, 'SDL', True,  1, DIN_Action_Category['1C'], [True, 0.1, 0.1, 0])
    LoadCase.StaticAnalysis(LoadCase, 3, 'Snow', True,  1, DIN_Action_Category['4A'], [False])
    LoadCase.StaticAnalysis(LoadCase, 4, 'Wind', False,  1, DIN_Action_Category['5'], [False])

    Model.clientModel.service.finish_modification()
