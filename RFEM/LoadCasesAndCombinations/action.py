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
            action_items (list or list of lists, optional):
                - if action_type == 'ACTING_DIFFERENTLY': [[Load_case, acting_group], ...]
                - else: [Load_case, Load_case, ...]
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
            # Sanity check
            sCheck = True
            for i in action_items:
                if action_type == ActionType.ACTING_DIFFERENTLY:
                    if not isinstance(i, list) or len(i) != 2:
                        ValueError('WARNING: Object Action, parameter action_items, size of the nested list must be 2.')
                    if isinstance(i[0], int) or isinstance(i[1], int):
                        pass
                    else:
                        ValueError('WARNING: Object Action, parameter action_items, items in the nested list must be integers.')
                else:
                    if not isinstance(ï, int):
                        ValueError('WARNING: Object Action, parameter action_items must be list of integers.')


            if action_type == ActionType.ACTING_DIFFERENTLY and isinstance(action_items[0], list) and len(action_items[])

            items = model.clientModel.factory.create('ns0:array_of_action_items')
            for i,j in enumerate(action_items):
                item = model.clientModel.factory.create('ns0:action_items_row')
                item.no = i+1
                item.row = model.clientModel.factory.create('ns0:action_items')
                clearAttributes(item.row)
                if action_type == ActionType.ACTING_DIFFERENTLY:
                    item.row.load_case_item = i[1]
                    item.row.acting_group_number = i[2]
                else:
                    item.row.load_case_item = i

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
