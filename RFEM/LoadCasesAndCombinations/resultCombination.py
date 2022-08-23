from RFEM.initModel import Model, clearAtributes

class ResultCombination():

    def __init__(self,
                 no: int = 1,
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
        model.clientModel.service.set_result_combination(clientObject)
