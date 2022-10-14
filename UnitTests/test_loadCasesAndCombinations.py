import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations

if Model.clientModel is None:
    Model()

def test_load_cases_and_combinations():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    LoadCasesAndCombinations(
        params = {
        "current_standard_for_combination_wizard": 6067,
        "activate_combination_wizard_and_classification": True,
        "activate_combination_wizard": True,
        "result_combinations_active": True,
        "result_combinations_parentheses_active": False,
        "result_combinations_consider_sub_results": False,
        "combination_name_according_to_action_category": False})

    Model.clientModel.service.finish_modification()

    combConfig = Model.clientModel.service.get_load_cases_and_combinations()

    assert combConfig.current_standard_for_combination_wizard == 6067
    assert combConfig.result_combinations_parentheses_active == False

