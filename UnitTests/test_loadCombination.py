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
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.enums import ActionCategoryType, AnalysisType


if Model.clientModel is None:
    Model()

def test_loadCombination():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")

    LoadCase.StaticAnalysis(1, 'DEAD', True, 1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_G, [True, 0, 0, 10])
    LoadCase.StaticAnalysis(2, 'LIVE', True, 1, ActionCategoryType.ACTION_CATEGORY_PRESTRESS_P, [False])
    LoadCase.StaticAnalysis(3)
    LoadCase(4)

    #LoadCombination(1, AnalysisType.ANALYSIS_TYPE_STATIC, 1, 'LC1', 1, combination_items=[[1.2, 1, 0, True], [1.6, 1, 0, False]])
    LoadCombination(no=1,
                    analysis_type=AnalysisType.ANALYSIS_TYPE_STATIC,
                    name='CO1',
                    static_analysis_settings=1,
                    to_solve=True,
                    combination_items=[
                        [1.35, 1, 0, False],
                        [1.50, 2, 0, False]
                    ])

    Model.clientModel.service.finish_modification()

    comb = Model.clientModel.service.get_load_combination(1)

    assert comb.no == 1
    assert comb.analysis_type == "ANALYSIS_TYPE_STATIC"
    assert comb.design_situation == 1
    assert comb.user_defined_name_enabled == True
    assert comb.name == "CO1"
    assert comb.static_analysis_settings == 1
    assert comb.consider_imperfection == False
    assert comb.consider_initial_state == False
    assert comb.structure_modification_enabled == False
    assert comb.to_solve == True
    assert round(comb.items[0][0].row.factor, 2) == 1.35
    assert comb.items[0][0].row.load_case == 1
