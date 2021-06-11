from RFEM.initModel import *
from RFEM.enums import SetType

class ResultSection():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Result Section
        clientObject = clientModel.factory.create('ns0:result_section')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Result Section No.
        clientObject.no = no

        # Add Result Section to client model
        clientModel.service.set_result_section(clientObject)