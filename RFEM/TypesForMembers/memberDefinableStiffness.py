from RFEM.initModel import *
from RFEM.enums import SetType

class MemberDefinableStiffness():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Member Definable Stffness
        clientObject = clientModel.factory.create('ns0:member_definable_stiffness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Definable Stffness No.
        clientObject.no = no

        # Add Member Definable Stffness to client model
        clientModel.service.set_member_definable_stiffness(clientObject)