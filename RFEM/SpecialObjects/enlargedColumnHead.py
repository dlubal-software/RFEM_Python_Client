from RFEM.initModel import *
from RFEM.enums import SetType

class EnlargedColumnHead():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Enlarged Column Head
        clientObject = clientModel.factory.create('ns0:enlarged_column_head')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Enlarged Column Head No.
        clientObject.no = no

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Enlarged Column Head to client model
        clientModel.service.set_enlarged_column_head(clientObject)