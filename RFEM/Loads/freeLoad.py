from RFEM.initModel import *
from RFEM.enums import *
from enum import Enum

class FreeLoad():

    def ConcentratedLoad(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 load_direction = FreeConcentratedLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z,
                 load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                 load_type = FreeConcentratedLoadLoadType.LOAD_TYPE_FORCE,
                 load_parameter = [1000, 0, 0],
                 surfaces_no = '1',
                 comment: str = '',
                 params: dict = {}):
                 
        '''
        for load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV:
            load_parameter = [magnitude, X, Y]

        for load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_YZ_OR_VW:
            load_parameter = [magnitude, Y, Z]

        for load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_XZ_OR_UW:
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

    def LineLoad(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 load_direction = FreeLineLoadLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_distribution = FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                 load_parameter = [],
                 surfaces_no = '1',
                 comment: str = '',
                 params: dict = {}):
                 
        '''
        for load_distribution = FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            load_parameter = [magnitude_uniform, load_location_first_x, load_location_first_y, load_location_second_x, load_location_second_y]

        for load_distribution = FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
            load_parameter = [magnitude_first, magnitude_second, load_location_first_x, load_location_first_y, load_location_second_x, load_location_second_y]
        '''

        # Client model | Free Concentrated Load
        clientObject = clientModel.factory.create('ns0:free_line_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no
        
        # Load Case No.
        clientObject.load_case = load_case_no
        
        # Assigned Surfaces No.
        clientObject.surfaces = ConvertToDlString(surfaces_no)
        
        # Load Distribution
        clientObject.load_distribution = load_distribution.name
        
        # Load Projection
        clientObject.load_projection = load_projection.name
        
        # Load Direction
        clientObject.load_direction = load_direction.name
        
        # Load Parameter
        if load_distribution.name == 'LOAD_DISTRIBUTION_UNIFORM':
            if len(load_parameter) != 5:
                raise Exception('WARNING: The load parameter needs to be of length 5. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_uniform = load_parameter[0]
            clientObject.load_location_first_x = load_parameter[1]
            clientObject.load_location_first_y = load_parameter[2]
            clientObject.load_location_second_x = load_parameter[3]
            clientObject.load_location_second_y = load_parameter[4]
        elif load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR':
            if len(load_parameter) != 6:
                raise Exception('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_first = load_parameter[0]
            clientObject.magnitude_second = load_parameter[1]
            clientObject.load_location_first_x = load_parameter[2]
            clientObject.load_location_first_y = load_parameter[3]
            clientObject.load_location_second_x = load_parameter[4]
            clientObject.load_location_second_y = load_parameter[5]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Free Concentrated Load to client model          
        clientModel.service.set_free_line_load(load_case_no, clientObject)
