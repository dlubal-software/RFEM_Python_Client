import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCombination import *
from RFEM.enums import ActionCategoryType


if Model.clientModel is None:
    Model()

def test_loadCombination():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")

    LoadCase.StaticAnalysis(1, 'DEAD', True, 1, ActionCategoryType.ACTION_CATEGORY_NONE_NONE, [True, 0, 0, 10])
    LoadCase.StaticAnalysis(2, 'LIVE', True, 1, ActionCategoryType.ACTION_CATEGORY_NONE_NONE, [False])

    LoadCombination(1, AnalysisType.ANALYSIS_TYPE_STATIC, 1, 'LC1', 1, combination_items=[[1.2, 1, 0, True], [1.6, 1, 0, False]])

    Model.clientModel.service.finish_modification()

    combination = Model.clientModel.service.get_load_combination(1)

    assert round(combination.items[0][0].row.factor, 2) == 1.20
    assert combination.items[0][0].row.load_case == 1
