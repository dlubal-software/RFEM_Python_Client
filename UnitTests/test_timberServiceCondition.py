import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn, TimberServiceConditionsMoistureServiceCondition
from RFEM.initModel import Model, SetAddonStatus, AddOn
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForTimberDesign.timberServiceCondition import TimberServiceConditions
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations

if Model.clientModel is None:
    Model()

def test_timberServiceConditions():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.timber_design_active, True)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Material(1, 'KLH (20 mm) | KLH')
    Section(1, 'R_M1 0.2/0.5', 1)
    Member(1, 1, 2, 0, 1, 1)

    LoadCasesAndCombinations(
        params = {
        "current_standard_for_combination_wizard": 6336,
        "activate_combination_wizard_and_classification": True,
        "activate_combination_wizard": True,
        "result_combinations_active": True,
        "result_combinations_parentheses_active": False,
        "result_combinations_consider_sub_results": False,
        "combination_name_according_to_action_category": True})

    TimberServiceConditions(1, members='1 2', moisture_service_condition=TimberServiceConditionsMoistureServiceCondition.TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_DRY)

    Model.clientModel.service.finish_modification()

    # tmc1 = Model.clientModel.service.get_timber_service_condition()

    # assert tmc1.member == '1 2'
    # assert tmc1.moisture_class == TimberServiceConditionsMoistureServiceCondition.TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_DRY
