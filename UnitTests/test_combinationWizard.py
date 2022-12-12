import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import NodalSupportType, LoadDirectionType, AddOn
from RFEM.initModel import Model, SetAddonStatus

from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.Loads.nodalLoad import NodalLoad

from RFEM.LoadCasesAndCombinations.combinationWizard import CombinationWizard

if Model.clientModel is None:
    Model()

def test_combinationWizard():

    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, addOn = AddOn.structure_stability_active, status = True)

    #Setting up the model to test the combination wizard
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5, 0.0, 0.0)
    Line(1, '1 2')
    NodalSupport(1, '1', NodalSupportType.FIXED)


    #setting up the loading of the model, with differnet loading cases and calculatiion settings
    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
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

    LoadCase(1, 'Self-Weight', [True, 0.0, 0.0,1.0])
    NodalLoad(1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 1000)

    #setting up the combination wizard
    CombinationWizard(1, 'Wizard 1', 1, 'this is Wizard no. 1')

    #going through each setting of the combination wizard

    CombinationWizard.Imperfection(1, True, True, model = Model)

    CombinationWizard.StaticAnalysisSettings(1, 1, model = Model)

    CombinationWizard.StabilityAnalyis(1, True, 1, model = Model)

    CombinationWizard.OptionsII(1, False, True, True, True, model = Model)

    CombinationWizard.ResultCombination(1, True, model = Model)

    CombinationWizard.SetInitialState(1, True, 1, 'DEFINITION_TYPE_FINAL_STATE', model = Model)

    CombinationWizard.StructureModification(1, True, 1, model = Model)

    Model.clientModel.service.finish_modification()

    config = Model.clientModel.service.get_combination_wizard(1)

    assert config.no == 1
    assert config.name == 'Wizard 1'
    assert config.static_analysis_settings == 1
    assert config.has_stability_analysis == True
    assert config.stability_analysis_settings == 1
    #assert config.consider_imperfection_case == True
    #assert config.generate_same_CO_without_IC == True
    #assert config.consider_construction_stages == True
    assert config.user_defined_action_combinations == False
    assert config.comment == 'this is Wizard no. 1'
    assert config.consider_initial_state == True
    assert config.structure_modification_enabled ==  True
    assert config.structure_modification == 1