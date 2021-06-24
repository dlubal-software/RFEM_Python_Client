from RFEM.initModel import *
from RFEM.enums import SurfaceLoadDirection, SurfaceLoadDistribution, SurfaceLoadType
from enum import Enum

class SurfaceLoad():
    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 surface_no: str = '1',
                 load_magnitude_p: float = 1.0,
                 load_direction = SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
                 load_distribution = SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Surface Load
        clientObject = clientModel.factory.create('ns0:surface_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Load No.
        clientObject.no = no

        # Load Type
        clientObject.load_type = "LOAD_TYPE_FORCE" #SurfaceLoadType.LOAD_TYPE_FORCE

        # Load Case No.
        clientObject.load_case = load_case_no

        # Surfaces No. (e.g. '5 6 7 12')
        clientObject.surfaces = ConvertToDlString(surface_no)

        # Load Direction
        clientObject.load_direction = load_direction.name

        # Load Magnitude P
        clientObject.uniform_magnitude = load_magnitude_p

        # Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface Load to client model
        clientModel.service.set_surface_load(load_case_no, clientObject)
