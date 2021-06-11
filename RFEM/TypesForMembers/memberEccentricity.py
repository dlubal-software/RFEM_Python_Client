from RFEM.initModel import *
from RFEM.enums import SetType

class MemberEccentricity():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Member Eccentricity
        clientObject = clientModel.factory.create('ns0:member_eccentricity')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Eccentricity No.
        clientObject.no = no

        # Add Member Eccentricity to client model
        clientModel.service.set_member_eccentricity(clientObject)