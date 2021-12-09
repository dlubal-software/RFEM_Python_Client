from RFEM.initModel import *

class LineHinge():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line Hinge
        clientObject = Model.clientModel.factory.create('ns0:line_hinge')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Hinge No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line Hinge to client model
        Model.clientModel.service.set_line_hinge(clientObject)