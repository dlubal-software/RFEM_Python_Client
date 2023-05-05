import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import NodalSupportType, LoadDirectionType, OperatorType, ResultCombinationType
from RFEM.enums import DesignSituationType, ActionLoadType, ResultCombinationExtremeValueSign, CaseObjectSubResultType
from RFEM.initModel import Model
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.resultCombination import ResultCombination
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation

if Model.clientModel is None:
    Model()

def test_resultCombination():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5, 0.0, 0.0)
    Line(1, '1 2')
    NodalSupport(1, '1', NodalSupportType.FIXED)

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
    LoadCasesAndCombinations({
                    "current_standard_for_combination_wizard": 6207,
                    "activate_combination_wizard_and_classification": True,
                    "activate_combination_wizard": False,
                    "result_combinations_active": True,
                    "result_combinations_parentheses_active": False,
                    "result_combinations_consider_sub_results": True,
                    "combination_name_according_to_action_category": False
                 },
                 model= Model)

    LoadCase(1, 'Self-Weight', [True, 0.0, 0.0,1.0])
    NodalLoad(1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 1000)

    DesignSituation(1, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_CHARACTERISTIC)
    ResultCombination(2, 1, ResultCombinationType.COMBINATION_TYPE_GENERAL, [[1, OperatorType.OPERATOR_NONE, 1.1, ActionLoadType.LOAD_TYPE_TRANSIENT]], False, [True, ResultCombinationExtremeValueSign.EXTREME_VALUE_SIGN_NEGATIVE], 'Res Comb')

    Model.clientModel.service.finish_modification()

    config = Model.clientModel.service.get_result_combination(2)

    assert config.no == 2
    assert config.name == 'Res Comb'
    assert config.design_situation == 1
    assert config.combination_type == ResultCombinationType.COMBINATION_TYPE_GENERAL.name
    assert config.srss_combination == True
    assert config.generate_subcombinations == False
