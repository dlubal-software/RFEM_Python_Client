from RFEM.initModel import *

class Opening():
    def __init__(self,
                 no: int,
                 lines_no: str,
                 comment: str = ''):

        # Client model | Opening
        clientObject = clientModel.factory.create('ns0:opening')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Opening No.
        clientObject.no = no

        # Boundary Lines No.
        clientObject.boundary_lines = lines_no

        # Comment
        clientObject.comment = comment

        # Add Opening to client model
        clientModel.service.set_opening(clientObject)
