from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import ResultCombinationType, OperatorType, ActionLoadType, CaseObjectSubResultType

class ResultCombination():

    def __init__(self,
                 no: int = 1,
                 name: str = '',
                 design_situation: int = 1,
                 combination_type = ResultCombinationType.COMBINATION_TYPE_GENERAL,
                 combination_items: list = [
                    [1, OperatorType.OPERATOR_OR, False, False, 1.2, CaseObjectSubResultType.SUB_RESULT_INCREMENTAL_FINAL_STATE, ActionLoadType.LOAD_TYPE_TRANSIENT],
                    [2, OperatorType.OPERATOR_NONE, False, False, 1.6, CaseObjectSubResultType.SUB_RESULT_INCREMENTAL_FINAL_STATE, ActionLoadType.LOAD_TYPE_TRANSIENT]
                    ],
                 srss_combination: list = [False],
                 generate_subcombinations: bool = False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Result Combination Tag
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Result Combination
        clientObject = model.clientModel.factory.create('ns0:result_combination')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Result Combination No.
        clientObject.no = no

        # Result Combination Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Assigned Design Situation
        clientObject.design_situation = design_situation

        # Result Combination Type
        clientObject.combination_type = combination_type.name

        # Combination Items
        clientObject.items = model.clientModel.factory.create('ns0:result_combination.items')
        for i,j in enumerate(combination_items):
            rci = model.clientModel.factory.create('ns0:result_combination_items_row')
            rci.no = i+1
            rci.row = model.clientModel.factory.create('ns0:result_combination_items')
            rci.row.case_object_item = combination_items[i][0]
            rci.row.operator_type = combination_items[i][1].name
            rci.row.left_parenthesis = combination_items[i][2]
            rci.row.right_parenthesis = combination_items[i][3]
            rci.row.case_object_factor = combination_items[i][4]
            rci.row.case_object_sub_result_type = combination_items[i][5].name
            rci.row.case_object_load_type = combination_items[i][6].name

            deleteEmptyAttributes(rci)
            clientObject.items.result_combination_items.append(rci)

        # SRSS Combinations
        if srss_combination[0] == False:
            clientObject.srss_combination = False
        else:
            clientObject.srss_combination = True
            clientObject.srss_use_equivalent_linear_combination = srss_combination[1]
            clientObject.srss_extreme_value_sign = srss_combination[2].name
            if srss_combination[2].name == "EXTREME_VALUE_SIGN_ACCORDING_TO_LC_CO":
                clientObject.srss_according_load_case_or_combination = srss_combination[3]

        # Subcombinations
        clientObject.generate_subcombinations = generate_subcombinations

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Result Combination to client model
        model.clientModel.service.set_result_combination(clientObject)

        # print(clientObject)

