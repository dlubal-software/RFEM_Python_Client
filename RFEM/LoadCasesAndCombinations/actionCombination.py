from RFEM.initModel import Model, clearAtributes

class ActionCombination():
    def __init__(self,
                 no: int = 1,
                 design_situation: int = 1,
                 action_items: list = None,
                 name: str = '',
                 is_active: bool = True,
                 comment: str = '',
                 params: dict = None):

        '''
        Args:
            no (int): Result Combination Tag
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        '''

        # Client model | Result Combination
        clientObject = Model.clientModel.factory.create('ns0:result_combination')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Result Combination No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Result Combination to client model
        Model.clientModel.service.set_result_combination(clientObject)