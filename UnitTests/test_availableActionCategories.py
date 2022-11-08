import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings

if Model.clientModel is None:
    Model()

def test_availableActionCategories():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    LoadCasesAndCombinations(params={
        "current_standard_for_combination_wizard" : 6042
    })

    StaticAnalysisSettings()

    Model.clientModel.service.finish_modification()

    availableActionCategories = LoadCasesAndCombinations.getAvailableLoadActionCategoryTypes()

    assert len(availableActionCategories) == 19
    assert type(availableActionCategories) == list
