from RFEM.initModel import *
from RFEM.enums import SetType

class SurfaceContact():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Surfaces Contact
        clientObject = clientModel.factory.create('ns0:surfaces_contact')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surfaces Contact No.
        clientObject.no = no

        # Add Surfaces Contact to client model
        clientModel.service.set_surfaces_contact(clientObject)