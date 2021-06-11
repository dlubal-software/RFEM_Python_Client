from RFEM.initModel import *
from RFEM.enums import SetType

class SolidContact():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Solid Contact
        clientObject = clientModel.factory.create('ns0:solid_contacts')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Contact No.
        clientObject.no = no

        # Add Solid Contact to client model
        clientModel.service.set_solid_contacts(clientObject)