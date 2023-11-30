from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertStrToListOfInt
from RFEM.enums import ObjectTypes

def ActionCombinationItem(model = Model, **kwargs):
    '''
    Set Action Combination Item.

    Args:
        model (RFEM Class): Model to be edited
        **kwargs - pass a keyworded, variable-length argument list. Following are all possible keywords:

        action_item, operator_type, left_parenthesis, right_parenthesis, group_factor, action_factor,
        action_load_type, group_load_type, action, is_leading, gamma, psi, xi, k_fi, c_esl, k_def,
        psi_0, psi_1, psi_2, fi, gamma_0, alfa, k_f, phi, omega_0, gamma_l_1, k_creep, gamma_n, j_2

    '''

    # Action Combination Item
    clientObject = model.clientModel.factory.create('ns0:action_combination_items')
    clearAttributes(clientObject)

    for key, value in kwargs.items():
        if key in clientObject.__keylist__:
            clientObject[key] = value

    deleteEmptyAttributes(clientObject)

    return clientObject


class ActionCombination():
    def __init__(self,
                 no: int = 1,
                 design_situation: int = 1,
                 action_combination_items: list = None,
                 name: str = '',
                 active: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        '''
        Combination Wizard Action

        Object: Action Combination No. 18
        Attribute: Design Situation
        Error: Only design situations with an assigned combination wizard where a user-defined action combination is set are valid.

        Args:
            no (int, mandatory): Action number
            action_category (enum, mandatory): Action category
            action_type (enum, mandatory): Action type
            action_items (list, mandatory): List of ActionCombinationItem objects
            name (str, optional): Action name
            active (bool, optional): Define if active
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Action
        clientObject = model.clientModel.factory.create('ns0:action_combination')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Action Combination No.
        clientObject.no = no

        # Design Situation
        clientObject.design_situation = design_situation

        # Action Combination Items
        if action_combination_items:
            items = model.clientModel.factory.create('ns0:array_of_action_combination_items')
            for i,j in enumerate(action_combination_items):
                item = model.clientModel.factory.create('ns0:action_combination_items_row')
                item.no = i+1
                item.row = j

                items.action_combination_items.append(item)

            clientObject.items = items
        # Active
        clientObject.active = active

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Clearing unused attributes
        deleteEmptyAttributes(clientObject)

        # Add Action to client model
        model.clientModel.service.set_action_combination(clientObject)

    @staticmethod
    def DeleteActionCombination(action_combination_no: str = '1 2', model = Model):
        '''
        Delete Action Combination objects

        Args:
            actions_no (str): Numbers of Action Combinations to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete Action Combinations from client model
        for ac in ConvertStrToListOfInt(action_combination_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_ACTION_COMBINATION.name, ac)

    @staticmethod
    def GetActionCombination(object_index: int = 1, model = Model):

        '''
        Args:
            obejct_index (int): Action Combination Index
            model (RFEM Class, optional): Model to be edited
        '''

        # Get Action Combination from client  model
        return model.clientModel.service.get_action_combination(object_index)
