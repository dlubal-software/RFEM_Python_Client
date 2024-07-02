import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn, TimberServiceConditionsMoistureType, TimberServiceConditionsTreatmentType
from RFEM.initModel import Model, SetAddonStatus, AddOn, openFile, closeModel
from RFEM.connectionGlobals import url
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForTimberDesign.timberServiceCondition import TimberServiceConditions
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
import pytest

if Model.clientModel is None:
    Model()

@pytest.mark.skipif(url != 'http://127.0.0.1', reason="This test fails on remote PC due to incorrect file path. \
                    Althought it is easy to change, it would not be easy to update on every remote computer.\
                    It is not necessary to evaluate Client as functional. Localy this tests still gets executed.")

def test_timberServiceConditionsCSA():

    dirname = os.path.join(os.getcwd(), os.path.dirname(__file__))
    openFile(os.path.join(dirname, 'src', 'timberServiceConditionCSA.rf6'))

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
        "combination_name_according_to_action_category": False})

    TimberServiceConditions(no=1, standard = 6336, moisture_service_condition=TimberServiceConditionsMoistureType.TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_WET.name, \
                            treatment_csa = TimberServiceConditionsTreatmentType.TREATMENT_TYPE_PRESERVATIVE.name)

    Model.clientModel.service.finish_modification()

    tcs = Model.clientModel.service.get_timber_service_conditions(1)
    assert tcs.moisture_service_condition == "TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_WET"
    assert tcs.treatment == "TREATMENT_TYPE_PRESERVATIVE"

    closeModel('timberServiceConditionCSA.rf6')
