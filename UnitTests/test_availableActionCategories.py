import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/..')

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

    availableActionCategories = LoadCasesAndCombinations.getAvailableLoadActionCategoryTypes()

    Model.clientModel.service.finish_modification()

    assert len(availableActionCategories) == 19
