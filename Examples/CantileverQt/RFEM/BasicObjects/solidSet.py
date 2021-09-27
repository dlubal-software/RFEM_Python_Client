from RFEM.initModel import *
from RFEM.enums import SetType

class SolidSet():
    def __init__(self,
                 no: int = 1,
                 solids_no: str = '1 2',
                 solid_set_type = SetType.SET_TYPE_GROUP,
                 comment: str = ''):

        # Client model | Solid Set
        clientObject = clientModel.factory.create('ns0:solid_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Set No.
        clientObject.no = no

        # Solids number
        clientObject.solides = solids_no

        # Solid Set Type
        clientObject.set_type = solid_set_type.name

        # Comment
        clientObject.comment = comment

        # Add Solid Set to client model
        clientModel.service.set_solid_set(clientObject)
