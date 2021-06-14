from RFEM.initModel import *
from RFEM.enums import SetType

class DesignSituation():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Design Situation
        clientObject = clientModel.factory.create('ns0:design_situation')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Design Situation No.
        clientObject.no = no

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Design Situation to client model
        clientModel.service.set_design_situation(clientObject)