from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import ResultCombinationType, OperatorType, ActionLoadType

class ResultCombination():

    def __init__(self,
                 no: int = 1,
                 design_situation: int = 1,
                 combination_type = ResultCombinationType.COMBINATION_TYPE_GENERAL,
                 combination_items: list = [
                    [1, OperatorType.OPERATOR_OR, 1.2, ActionLoadType.LOAD_TYPE_TRANSIENT],
                    [2, OperatorType.OPERATOR_NONE, 1.6, ActionLoadType.LOAD_TYPE_TRANSIENT]
                    ],
                 generate_subcombinations: bool = False,
                 srss_combination: list = None,
                 name: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Result Combination tag
            design_situation (int): Assign Design Situation
            combination_type (enum): Result Combination Type Enumeration
            combination_items (list of lists): Combination Items Table
                combination_item[0](int) = case_object_item
                combination_item[1](enum) = operator_type enumeration
                combination_item[2](float) = case_object_factor
                combination_item[3](enum) = case_object_load_type enumeration
                combination_item[4](bool) = left_parenthesis (if parenthesis active in LoadCaseandCombination)
                combination_item[5](bool) = right_parenthesis (if parenthesis active in LoadCaseandCombination)
                combination_item[6](float) = group_factor (if left_parenthesis is True then value else None)
                combination_item[7](enum) = group_load_type (if right_parenthesis is True then enumeration else None)
            srss_combination (list, optional): SRSS Combination. If None then False.
                srss_combination = [srss_use_equivalent_linear_combination(bool), srss_extreme_value_sign(enum), srss_according_load_case_or_combination(int)]
            name (str, optional): User Defined Result Combination Name
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
        if combination_items:
            clientObject.items = model.clientModel.factory.create('ns0:result_combination.items')
            for i,j in enumerate(combination_items):
                rci = model.clientModel.factory.create('ns0:result_combination_items_row')
                rci.no = i+1
                rci.row = model.clientModel.factory.create('ns0:result_combination_items')
                clearAttributes(rci.row)
                rci.row.case_object_item = combination_items[i][0]
                rci.row.operator_type = combination_items[i][1].name
                rci.row.case_object_factor = combination_items[i][2]
                rci.row.case_object_load_type = combination_items[i][3].name
                if len(combination_items[i]) > 4:
                    rci.row.left_parenthesis = combination_items[i][4]
                    rci.row.right_parenthesis = combination_items[i][5]
                    if combination_items[i][4]:
                        rci.row.group_factor = combination_items[i][6]
                    if combination_items[i][5]:
                        rci.row.group_load_type = combination_items[i][7].name

                clientObject.items.result_combination_items.append(rci)

        # SRSS Combinations
        if not srss_combination:
            clientObject.srss_combination = False
        else:
            clientObject.srss_combination = True
            clientObject.srss_use_equivalent_linear_combination = srss_combination[0]
            clientObject.srss_extreme_value_sign = srss_combination[1].name
            if srss_combination[1].name == "EXTREME_VALUE_SIGN_ACCORDING_TO_LC_CO":
                clientObject.srss_according_load_case_or_combination = srss_combination[2]

        # Subcombinations
        clientObject.generate_subcombinations = generate_subcombinations

        clientObject.to_solve = True

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
