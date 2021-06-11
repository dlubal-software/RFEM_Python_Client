from RFEM.initModel import *
from RFEM.enums import SetType

class ResultCombination():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Result Combination
        clientObject = clientModel.factory.create('ns0:result_combination')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Result Combination No.
        clientObject.no = no

        # Add Result Combination to client model
        clientModel.service.set_result_combination(clientObject)