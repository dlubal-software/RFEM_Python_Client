from RFEM.initModel import Model, clearAtributes
from RFEM.enums import ActionCategoryType, ActionType

class Action():
    def __init__(self,
                 no: int = 1,
                 action_category = ActionCategoryType.ACTION_CATEGORY_PERMANENT_G,
                 action_type = ActionType.ACTING_SIMULTANEOUSLY,
                 action_items: list = None,
                 name: str = '',
                 is_active: bool = True,
                 comment: str = '',
                 params: dict = None):
        '''
        Combination Wizard Action

        Args:
            no (int, optional): Action number
            action_category (enum, optional): Action category
            action_type (enum, optional): Action type
            action_items (list of lists, optional): [[no, Load_case, acting_group],...]
            name (str, optional): Action name
            is_active (bool, optional): Define if active
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        '''

        # Client model | Result Combination
        clientObject = Model.clientModel.factory.create('ns0:action')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Result Combination No.
        clientObject.no = no

        # Action Category
        clientObject.action_category = action_category

        # Action Type
        clientObject.action_type = action_type

        items = []
        for i in action_items:
            item = {}
            item['no'] = i[0]
            item['load_case_item'] = i[1]
            item['acting_group_number'] = i[2]
            items.append(item)

        # Action Items
        clientObject.action_items = items

        # Active
        clientObject.is_active = is_active

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

        # Add Result Combination to client model
        Model.clientModel.service.set_action(clientObject)