import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn, TimberMoistureClassMoistureClass
from RFEM.initModel import Model, SetAddonStatus, AddOn
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForTimberDesign.timberMoistureClass import TimberMoistureClass
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations

## Important!!
# First Run: Model set to True and Comments in the test set the way they are right now
# --> after First Run: In RFEM > Base Data > Standard I > Design | Standard Group > Timber Design: Set to SIA 265
# Second Run: 1. Set Model to False ( Model(True, "Test_Timber_Moisture") --> Model(False, "Test_Timber_Moisture") )
#             2. Uncomment TimberMoistureClass(no = 1, members='1', moisture_class=TimberMoistureClassMoistureClass.TIMBER_MOISTURE_CLASS_TYPE_2)
#             3. Uncomment: tmc1 = Model.clientModel.service.get_timber_moisture_class(1)
#                           assert tmc1.member == '1'
#                           assert tmc1.moisture_class == TimberMoistureClassMoistureClass.TIMBER_MOISTURE_CLASS_TYPE_2.name


Model(True, "Test_Timber_Moisture")

def test_timberMoistureClass():

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
        "current_standard_for_combination_wizard": 6226,
        "activate_combination_wizard_and_classification": True,
        "activate_combination_wizard": True,
        "result_combinations_active": True,
        "result_combinations_parentheses_active": False,
        "result_combinations_consider_sub_results": False,
        "combination_name_according_to_action_category": False})

    # TimberMoistureClass(no = 1, members='1', moisture_class=TimberMoistureClassMoistureClass.TIMBER_MOISTURE_CLASS_TYPE_2)

    Model.clientModel.service.finish_modification()

    # tmc1 = Model.clientModel.service.get_timber_moisture_class(1)
    # assert tmc1.member == '1'
    # assert tmc1.moisture_class == TimberMoistureClassMoistureClass.TIMBER_MOISTURE_CLASS_TYPE_2.name
