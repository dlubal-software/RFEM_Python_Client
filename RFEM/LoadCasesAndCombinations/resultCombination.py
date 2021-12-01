from RFEM.initModel import *
from RFEM.enums import SetType

class ResultCombination():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Result Combination
        clientObject = Model.clientModel.factory.create('ns0:result_combination')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Result Combination No.
        clientObject.no = no

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Result Combination to client model
        Model.clientModel.service.set_result_combination(clientObject)