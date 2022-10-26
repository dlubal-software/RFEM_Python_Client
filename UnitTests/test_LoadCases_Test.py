import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.enums import ActionCategoryType

if Model.clientModel is None:
    Model()

def test_load_case():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    StaticAnalysisSettings()
    LoadCase.StaticAnalysis(1, 'SW', True, 1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_G, [True, 0, 0, 1])
    LoadCase.StaticAnalysis(2, 'SDL', True,  1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_IMPOSED_GQ, [True, 0.1, 0.1, 0])
    LoadCase.StaticAnalysis(3, 'Snow', True,  1, ActionCategoryType.ACTION_CATEGORY_SNOW_ICE_LOADS_H_LESS_OR_EQUAL_TO_1000_M_QS, [False])
    LoadCase.StaticAnalysis(4, 'Wind', False,  1, ActionCategoryType.ACTION_CATEGORY_WIND_QW, [False])

    Model.clientModel.service.finish_modification()

    lc_1 = Model.clientModel.service.get_load_case(1)
    assert lc_1.to_solve == True
    assert lc_1.action_category == 'ACTION_CATEGORY_PERMANENT_G'
    assert lc_1.self_weight_active == True
    assert lc_1.self_weight_factor_x == 0
    assert lc_1.self_weight_factor_z == 1

    lc_2 = Model.clientModel.service.get_load_case(2)
    assert lc_2.action_category == 'ACTION_CATEGORY_PERMANENT_IMPOSED_GQ'
    assert lc_2.self_weight_factor_x == 0.1
    assert lc_2.self_weight_factor_z == 0

    lc_3 = Model.clientModel.service.get_load_case(3)
    assert lc_3.action_category == 'ACTION_CATEGORY_SNOW_ICE_LOADS_H_LESS_OR_EQUAL_TO_1000_M_QS'
    assert lc_3.self_weight_active == False

    assert Model.clientModel.service.get_load_case(4).self_weight_active == False
