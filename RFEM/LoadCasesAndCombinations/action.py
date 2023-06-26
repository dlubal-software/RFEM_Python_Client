from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import ActionCategoryType, ActionType

class Action():
    def __init__(self,
                 no: int = 1,
                 action_category = ActionCategoryType.ACTION_CATEGORY_PERMANENT_G,
                 action_type = ActionType.ACTING_ALTERNATIVELY,
                 action_items: list = None,
                 name: str = '',
                 is_active: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
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
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Action
        clientObject = model.clientModel.factory.create('ns0:action')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Action No.
        clientObject.no = no

        # Action Category
        clientObject.action_category = action_category.name

        # Action Type
        clientObject.action_type = action_type.name

        # Action Items
        if action_items:
            items = model.clientModel.factory.create('ns0:array_of_action_items')
            for i,j in enumerate(action_items):
                item = model.clientModel.factory.create('ns0:action_items_row')
                item.no = i+1
                item.row = model.clientModel.factory.create('ns0:action_items')
                clearAttributes(item.row)
                #item.row.no = i[0]
                item.row.load_case_item = action_items[i]
                #item.row.acting_group_number = i[2]

                items.append(item)

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

        # Clearing unused attributes
        deleteEmptyAttributes(clientObject)

        # Add Action to client model
        model.clientModel.service.set_action(clientObject)
