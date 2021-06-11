from RFEM.initModel import *
from RFEM.enums import SetType

class LineHinge():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Line Hinge
        clientObject = clientModel.factory.create('ns0:line_hinge')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Hinge No.
        clientObject.no = no

        # Add Line Hinge to client model
        clientModel.service.set_line_hinge(clientObject)