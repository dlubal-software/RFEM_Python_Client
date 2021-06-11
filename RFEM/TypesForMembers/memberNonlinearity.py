from RFEM.initModel import *
from RFEM.enums import SetType

class MemberNonlinearity():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Member Nonlinearity
        clientObject = clientModel.factory.create('ns0:member_nonlinearity')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Nonlinearity No.
        clientObject.no = no

        # Add Member Nonlinearity to client model
        clientModel.service.set_member_nonlinearity(clientObject)