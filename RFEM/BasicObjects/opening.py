from RFEM.initModel import *

class Opening():
    def __init__(self,
                 no: int,
                 lines_no: str,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Opening
        clientObject = Model.clientModel.factory.create('ns0:opening')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Opening No.
        clientObject.no = no

        # Boundary Lines No.
        clientObject.boundary_lines = ConvertToDlString(lines_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Opening to client model
        Model.clientModel.service.set_opening(clientObject)
