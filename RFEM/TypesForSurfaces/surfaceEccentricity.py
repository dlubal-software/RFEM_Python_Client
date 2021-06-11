from RFEM.initModel import *
from RFEM.enums import SetType

class SurfaceEccentricity():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Surface Eccentricity
        clientObject = clientModel.factory.create('ns0:surface_eccentricity')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Eccentricity No.
        clientObject.no = no

        # Add Surface Eccentricity to client model
        clientModel.service.set_surface_eccentricity(clientObject)