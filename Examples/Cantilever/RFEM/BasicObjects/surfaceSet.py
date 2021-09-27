from RFEM.initModel import *
from RFEM.enums import SetType

class SurfaceSet():
    def __init__(self,
                 no: int = 1,
                 surfaces_no: str = '2 4 7',
                 surface_set_type = SetType.SET_TYPE_GROUP,
                 comment: str = ''):

        # Client model | Surface Set
        clientObject = clientModel.factory.create('ns0:surface_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Set No.
        clientObject.no = no

        # Surfaces number
        clientObject.surfaces = surfaces_no

        # Surface Set Type
        clientObject.set_type = surface_set_type.name

        # Comment
        clientObject.comment = comment

        # Add Surface Set to client model
        clientModel.service.set_surface_set(clientObject)
