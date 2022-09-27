from RFEM.initModel import Model, clearAttributes

class ResultCombination():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Result Combination Tag
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Result Combination
        clientObject = Model.clientModel.factory.create('ns0:result_combination')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Result Combination No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Result Combination to client model
        Model.clientModel.service.set_result_combination(clientObject)
