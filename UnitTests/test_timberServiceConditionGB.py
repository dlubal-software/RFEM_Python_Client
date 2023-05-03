import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn, TimberServiceConditionsMoistureServiceCondition, TimberServiceConditionsTreatment
from RFEM.initModel import Model, SetAddonStatus, AddOn
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForTimberDesign.timberServiceCondition import TimberServiceConditions
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations

## Important!!
# First Run: Model set to True and and Comments in the test set the way they are right now ---> Run
# --> after First Run: In RFEM > Base Data > Standard I > Design | Standard Group > Timber Design: Set to GB 50005
# Second Run: 1. Set Model to False ( Model(True, "Test_Timber_Service_GB") --> Model(False, "Test_Timber_Service_GB") )
#             2. Uncomment: TimberServiceConditions(no=1, standard=6514, moisture_service_condition=TimberServiceConditionsMoistureServiceCondition.TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_WET.name, \
#                                                   service_conditions = [True, False, False, False, False])
#             3. Uncomment: tcs1 = Model.clientModel.service.get_timber_service_conditions(1)
#                           assert tcs1.moisture_service_condition == "TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_WET"
#                           assert tcs1.outdoor_environment == True
#               ---> Run again !

Model(True, "Test_Timber_Service_GB")

def test_timberServiceConditionsCSA():

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
        "current_standard_for_combination_wizard": 6514,
        "activate_combination_wizard_and_classification": True,
        "activate_combination_wizard": True,
        "result_combinations_active": True,
        "result_combinations_parentheses_active": False,
        "result_combinations_consider_sub_results": False,
        "combination_name_according_to_action_category": False})

    # TimberServiceConditions(no=1, standard=6514, moisture_service_condition=TimberServiceConditionsMoistureServiceCondition.TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_WET.name, \
    #                         service_conditions = [True, False, False, False, False])

    Model.clientModel.service.finish_modification()

    # tcs1 = Model.clientModel.service.get_timber_service_conditions(1)
    # assert tcs1.moisture_service_condition == "TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_WET"
    # assert tcs1.outdoor_environment == True
