from RFEM.initModel import *
from RFEM.enums import SetType

class LineWeldedJoint():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Line Welded Joint
        clientObject = clientModel.factory.create('ns0:line_welded_joint')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Welded Joint No.
        clientObject.no = no

        # Add Line welded joint to client model
        clientModel.service.set_line_welded_joint(clientObject)