import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from UnitTests.test_loadCombination import test_loadCombination

if Model.clientModel is None:
    Model()

def test_load_cases_and_combinations():

    ac = [6207, 6034, 6035, 6036, 6037, 6038, 6039, 6360, 6548, 6040, 6042, 6041, 6043, 6044, 6045, 6046, 6047, 6048, 6049, 6050, 6051, 6052, 6053, 6054, 6055, 6056, \
        6057, 6414, 6058, 6059, 6060, 6061, 6208, 6062, 6063, 6064, 6065, 6066, 6067, 6068, 6070, 6069, 6071, 6072, 6073, 6074, 6075, 6076, 6077, 6078, 6079, 6080, \
        6081, 6082, 6083, 6084, 6415, 6085, 6351, 6086, 6087, 6088, 6209, 6089, 6210, 6232, 6230, 6225, 6226, 6227, 6555, 6238, 6237, 6236, 6235,6579, 6350, 6241, \
        6240, 6239, 6403, 6269, 6268, 6267, 6361, 6273, 6272, 6271, 6270, 6317, 6325, 6331, 6336, 6358, 6380, 6435, 6436, 6514, 6516, 6517, 6518, 6522, 6523, 6524, \
        6525, 6526, 6527, 6529, 6528, 6530, 6531, 6532, 6533, 6534, 6535, 6536, 6537, 6538, 6539, 6541, 6521, 6542, 6543, 6544, 6546]
    failedAC = []

    for i in ac:
        Model.clientModel.service.delete_all()
        Model.clientModel.service.begin_modification()

        LoadCasesAndCombinations(
            params = {
            "current_standard_for_combination_wizard": i,
            "activate_combination_wizard_and_classification": True,
            "activate_combination_wizard": True,
            "result_combinations_active": True,
            "result_combinations_parentheses_active": False,
            "result_combinations_consider_sub_results": False,
            "combination_name_according_to_action_category": False})

        Model.clientModel.service.finish_modification()
        try:
            test_loadCombination()
        except:
            failedAC.append(i)

    combConfig = Model.clientModel.service.get_load_cases_and_combinations()

    assert combConfig.current_standard_for_combination_wizard == 6230
    assert combConfig.result_combinations_parentheses_active == False

    if failedAC:
        print('\nFollowing are the failing Standards for Combination Wizard:')
        print(failedAC)
