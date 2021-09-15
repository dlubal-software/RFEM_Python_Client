from RFEM.initModel import *
from RFEM.enums import *
from enum import Enum

class FreeConcentratedLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 load_direction = FreeConcentratedLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z,
                 load_projection = FreeConcentratedLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                 load_type = FreeConcentratedLoadLoadType.LOAD_TYPE_FORCE,
                 load_parameter = [1000, 0, 0],
                 surfaces_no = '1',
                 comment: str = '',
                 params: dict = {}):
                 
        '''
        if load_projection = FreeConcentratedLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV:
            load_parameter = [magnitude, X, Y]

        if load_projection = FreeConcentratedLoadLoadProjection.LOAD_PROJECTION_YZ_OR_VW:
            load_parameter = [magnitude, Y, Z]

        if load_projection = FreeConcentratedLoadLoadProjection.LOAD_PROJECTION_XZ_OR_UW:
            load_parameter = [magnitude, X, Z]
        '''

        # Client model | Free Concentrated Load
        clientObject = clientModel.factory.create('ns0:free_concentrated_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no
        
        # Load Case No.
        clientObject.load_case = load_case_no
        
        # Assigned Surfaces No.
        clientObject.surfaces = ConvertToDlString(surfaces_no)
        
        # Load Projection
        clientObject.load_projection = load_projection.name
        
        # Load Direction
        clientObject.load_direction = load_direction.name
        
        # Load Parameter
        if len(load_parameter) != 3:
            raise Exception('WARNING: The load parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
        clientObject.magnitude = load_parameter[0]
        clientObject.load_location_x = load_parameter[1]
        clientObject.load_location_y = load_parameter[2]

        # Load Type
        clientObject.load_type = load_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Free Concentrated Load to client model          
        clientModel.service.set_free_concentrated_load(load_case_no, clientObject)
