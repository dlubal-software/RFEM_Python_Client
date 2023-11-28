import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import NodalSupportType, AddOn, ActionCategoryType, ActionType, DesignSituationType, OperatorType, InitialStateDefintionType
from RFEM.initModel import Model, SetAddonStatus
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation
from RFEM.LoadCasesAndCombinations.combinationWizard import CombinationWizard
from RFEM.LoadCasesAndCombinations.action import Action
from RFEM.LoadCasesAndCombinations.actionCombination import ActionCombination, ActionCombinationItem
from RFEM.LoadCasesAndCombinations.stabilityAnalysisSettings import StabilityAnalysisSettings

if Model.clientModel is None:
    Model()

def test_action():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, addOn = AddOn.structure_stability_active)
    SetAddonStatus(Model.clientModel, addOn = AddOn.modal_active)

    LoadCasesAndCombinations({
                    "current_standard_for_combination_wizard": 6207,
                    "activate_combination_wizard_and_classification": True,
                    "activate_combination_wizard": True,
                    "result_combinations_active": False,
                    "result_combinations_parentheses_active": False,
                    "result_combinations_consider_sub_results": False,
                    "combination_name_according_to_action_category": False
                 },
                 model= Model)

    LoadCase(params={'no': 80, 'analysis_type': 'ANALYSIS_TYPE_STATIC', 'name': 'Self weight', 'calculate_critical_load': False, 'static_analysis_settings': 1, 'consider_imperfection': False, 'consider_initial_state': False, 'to_solve': True, 'action_category': 'ACTION_CATEGORY_PERMANENT_G', 'self_weight_active': False, 'comment': 'Self weight', 'is_generated': False, 'structure_modification_enabled': False})
    LoadCase(params={'no': 81, 'analysis_type': 'ANALYSIS_TYPE_STATIC', 'name': 'Permanent / Imposed', 'calculate_critical_load': False, 'static_analysis_settings': 1, 'consider_imperfection': False, 'consider_initial_state': False, 'to_solve': True, 'action_category': 'ACTION_CATEGORY_PERMANENT_IMPOSED_GQ', 'self_weight_active': False, 'is_generated': False, 'structure_modification_enabled': False})
    LoadCase(params={'no': 82, 'analysis_type': 'ANALYSIS_TYPE_STATIC', 'name': 'Imposed - category A', 'calculate_critical_load': False, 'static_analysis_settings': 1, 'consider_imperfection': False, 'consider_initial_state': False, 'to_solve': True, 'action_category': 'ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_A_DOMESTIC_RESIDENTIAL_AREAS_QI_A', 'self_weight_active': False, 'factor_phi': 'FACTOR_PHI_1', 'is_generated': False, 'structure_modification_enabled': False})
    LoadCase(params={'no': 83, 'analysis_type': 'ANALYSIS_TYPE_STATIC', 'name': 'Imposed - category A', 'calculate_critical_load': False, 'static_analysis_settings': 1, 'consider_imperfection': False, 'consider_initial_state': False, 'to_solve': True, 'action_category': 'ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_A_DOMESTIC_RESIDENTIAL_AREAS_QI_A', 'self_weight_active': False, 'factor_phi': 'FACTOR_PHI_2', 'is_generated': False, 'structure_modification_enabled': False})
    LoadCase(params={'no': 84, 'analysis_type': 'ANALYSIS_TYPE_STATIC', 'name': 'Imposed - category A', 'calculate_critical_load': False, 'static_analysis_settings': 1, 'consider_imperfection': False, 'consider_initial_state': False, 'to_solve': True, 'action_category': 'ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_A_DOMESTIC_RESIDENTIAL_AREAS_QI_A', 'self_weight_active': False, 'factor_phi': 'FACTOR_PHI_3', 'is_generated': False, 'structure_modification_enabled': False})
    DesignSituation(params={'no': 20, 'user_defined_name_enabled': False, 'name': 'Seismic/Mass Combination - psi-E,i', 'design_situation_type': 'DESIGN_SITUATION_TYPE_SEISMIC_MASS', 'active': True, 'is_generated': False, 'combination_wizard': 10, 'consider_inclusive_exclusive_load_cases': False, 'case_objects': {'design_situation_case_objects': [{'no': 1, 'row': 1}]}})
    CombinationWizard(params={'no': 10, 'user_defined_name_enabled': False, 'name': 'Load combinations | SA1 - Geometrically linear', 'static_analysis_settings': 1, 'generate_combinations': 'GENERATE_LOAD_COMBINATIONS', 'has_stability_analysis': False, 'consider_imperfection_case': False, 'user_defined_action_combinations': True, 'favorable_permanent_actions': False, 'reduce_number_of_generated_combinations': False, 'consider_initial_state': False, 'structure_modification_enabled': False})

    Action(1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_G, ActionType.ACTING_SIMULTANEOUSLY, [80], 'Permanent')
    Action(2, ActionCategoryType.ACTION_CATEGORY_PERMANENT_IMPOSED_GQ, ActionType.ACTING_SIMULTANEOUSLY, [81], 'Permanent/Imposed')
    Action(2, ActionCategoryType.ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_A_DOMESTIC_RESIDENTIAL_AREAS_QI_A, ActionType.ACTING_SIMULTANEOUSLY, [82, 83, 84], 'Imposed loads')

    aci1 = ActionCombinationItem(Model, action_item=1, operator_type=OperatorType.OPERATOR_AND.name, action_factor=1.0, action=1)
    aci2 = ActionCombinationItem(Model, action_item=2, operator_type=OperatorType.OPERATOR_AND.name, action_factor=0.3, action=2, psi=0.3)
    aci3 = ActionCombinationItem(Model, action_item=3, operator_type=OperatorType.OPERATOR_NONE.name, action_factor=1.2)
    ActionCombination(1, 20, [aci1, aci2, aci3], 'new combination')

    Model.clientModel.service.finish_modification()

    action_com = Model.clientModel.service.get_action_combination(1)
    assert action_com.design_situation == 20
    assert len(action_com.items.action_combination_items) == 3
    assert round(action_com.items.action_combination_items[1].row.action_factor, 3) == 0.3
    assert round(action_com.items.action_combination_items[2].row.action_factor, 3) == 1.2
