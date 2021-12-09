from RFEM.initModel import *

class LineSupport():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line Support
        clientObject = Model.clientModel.factory.create('ns0:line_support')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Support No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line Support to client model
        Model.clientModel.service.set_line_support(clientObject)