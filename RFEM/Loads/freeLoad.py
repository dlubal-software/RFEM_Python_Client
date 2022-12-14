from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import FreeConcentratedLoadLoadType, FreeConcentratedLoadLoadDirection, FreeLoadLoadProjection
from RFEM.enums import FreeLineLoadLoadDistribution, FreeLineLoadLoadDirection, FreeRectangularLoadLoadDistribution
from RFEM.enums import FreeRectangularLoadLoadDirection, FreeRectangularLoadLoadLocationRectangle, FreeCircularLoadLoadDistribution
from RFEM.enums import  FreeCircularLoadLoadDirection, FreePolygonLoadLoadDistribution, FreePolygonLoadLoadDirection
from math import pi

class FreeLoad():

    @staticmethod
    def ConcentratedLoad(
                 no: int = 1,
                 load_case_no: int = 1,
                 surfaces_no: str = '1',
                 load_type = FreeConcentratedLoadLoadType.LOAD_TYPE_FORCE,
                 load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                 load_direction = FreeConcentratedLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z,
                 load_parameter: list = [1000, 0, 0],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surfaces_no (str): Assigned Surface(s)
            load_type (enum): Free Concentrated Load Load Type Enumeration
            load_projection (enum): Free Load Load Projection Enumeration
            load_direction (enum): Free Concentrated Load Load Direction Enumeration
            load_parameter (list): Load Parameter List
                for load_projection == FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV:
                    load_parameter = [magnitude, X, Y]
                for load_projection == FreeLoadLoadProjection.LOAD_PROJECTION_YZ_OR_VW:
                    load_parameter = [magnitude, Y, Z]
                for load_projection == FreeLoadLoadProjection.LOAD_PROJECTION_XZ_OR_UW:
                    load_parameter = [magnitude, X, Z]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Free Concentrated Load
        clientObject = model.clientModel.factory.create('ns0:free_concentrated_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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
            raise ValueError('WARNING: The load parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
        clientObject.magnitude = load_parameter[0]
        clientObject.load_location_x = load_parameter[1]
        clientObject.load_location_y = load_parameter[2]

        # Load Type
        clientObject.load_type = load_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Free Concentrated Load to client model
        model.clientModel.service.set_free_concentrated_load(load_case_no, clientObject)

    @staticmethod
    def LineLoad(
                 no: int = 1,
                 load_case_no: int = 1,
                 surfaces_no: str = '1',
                 load_distribution = FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                 load_direction = FreeLineLoadLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surfaces_no (str): Assigned Surface(s)
            load_distribution (enum): Free Line Load Load Distribution Enumeration
            load_projection (enum): Free Load Load Projection Enumeration
            load_direction (enum): Free Line Load Load Direction Enumeration
            load_parameter (list): Load Parameter List
                for load_distribution == FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [magnitude_uniform, load_location_first_x, load_location_first_y, load_location_second_x, load_location_second_y]
                for load_distribution == FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
                    load_parameter = [magnitude_first, magnitude_second, load_location_first_x, load_location_first_y, load_location_second_x, load_location_second_y]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Free Concentrated Load
        clientObject = model.clientModel.factory.create('ns0:free_line_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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
                raise ValueError('WARNING: The load parameter needs to be of length 5. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_uniform = load_parameter[0]
            clientObject.load_location_first_x = load_parameter[1]
            clientObject.load_location_first_y = load_parameter[2]
            clientObject.load_location_second_x = load_parameter[3]
            clientObject.load_location_second_y = load_parameter[4]
        elif load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR':
            if len(load_parameter) != 6:
                raise ValueError('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_first = load_parameter[0]
            clientObject.magnitude_second = load_parameter[1]
            clientObject.load_location_first_x = load_parameter[2]
            clientObject.load_location_first_y = load_parameter[3]
            clientObject.load_location_second_x = load_parameter[4]
            clientObject.load_location_second_y = load_parameter[5]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Free Concentrated Load to client model
        model.clientModel.service.set_free_line_load(load_case_no, clientObject)

    @staticmethod
    def RectangularLoad(
                 no: int = 1,
                 load_case_no: int = 1,
                 surfaces_no: str = '1',
                 load_distribution = FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                 load_direction = FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                 load_magnitude_parameter: list = None,
                 load_location = FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CORNER_POINTS,
                 load_location_parameter: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surfaces_no (str): Assigned Surface(s)
            load_distribution (enum): Free Rectangular Load Load Distribution Enumeration
            load_projection (enum): Free Load Load Projection Enumeration
            load_direction (enum): Free Rectangular Load Load Direction Enumeration
            load_magnitude_parameter (list): Load Magnitude Parameter
                for load_distribution == FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_magnitude_parameter = [magnitude_uniform]
                for load_distribution == FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_FIRST or FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_SECOND:
                    load_magnitude_parameter = [magnitude_linear_first, magnitude_linear_second]
            load_location (enum): Free Rectangular Load Load Rectangle Enumeration
            load_location_parameter (list): Load Location Parameters
                for load_location == FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CORNER_POINTS:
                    for load_distribution == FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM or FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_FIRST or FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_SECOND:
                        load_location_parameter = [load_location_first_x, load_location_first_y, load_location_second_x, load_location_second_y, axis_start_angle]
                    for load_distribution == FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z:
                        load_location_parameter = [load_location_first_x, load_location_first_y, load_location_second_x, load_location_second_y, [[distance, factor], ...]
                    for load_distribution == FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_ALONG_PERIMETER:
                        load_location_parameter = [load_location_first_x, load_location_first_y, load_location_second_x, load_location_second_y, [axis_definition_p1_x, axis_definition_p1_y, axis_definition_p1_z], [axis_definition_p2_x, axis_definition_p2_y, axis_definition_p2_z], axis_start_angle,[[alpha, factor], ...]
                    for load_distribution == FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z_AND_ALONG_PERIMETER:
                        load_location_parameter = [load_location_first_x, load_location_first_y, load_location_second_x, load_location_second_y, [[distance, factor], ...], [axis_definition_p1_x, axis_definition_p1_y, axis_definition_p1_z], [axis_definition_p2_x, axis_definition_p2_y, axis_definition_p2_z], axis_start_angle,[[alpha, factor], ...]
                for load_location == FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES:
                    for load_distribution == FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM or FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_FIRST or FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_SECOND:
                        load_location_parameter = [load_location_center_x, load_location_center_y, load_location_center_side_a, load_location_center_side_b, axis_start_angle]
                    for load_distribution == FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z:
                        load_location_parameter = [load_location_center_x, load_location_center_y, load_location_center_side_a, load_location_center_side_b, [[distance, factor], ...]
                    for load_distribution == FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_ALONG_PERIMETER:
                        load_location_parameter = [load_location_center_x, load_location_center_y, load_location_center_side_a, load_location_center_side_b, [axis_definition_p1_x, axis_definition_p1_y, axis_definition_p1_z], [axis_definition_p2_x, axis_definition_p2_y, axis_definition_p2_z], axis_start_angle,[[alpha, factor], ...]
                    for load_distribution == FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z_AND_ALONG_PERIMETER:
                        load_location_parameter = [load_location_center_x, load_location_center_y, load_location_center_side_a, load_location_center_side_b, [[distance, factor], ...], [axis_definition_p1_x, axis_definition_p1_y, axis_definition_p1_z], [axis_definition_p2_x, axis_definition_p2_y, axis_definition_p2_z], axis_start_angle,[[alpha, factor], ...]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Free Concentrated Load
        clientObject = model.clientModel.factory.create('ns0:free_rectangular_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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

        # Load Magnitude Parameter
        if load_distribution.name == 'LOAD_DISTRIBUTION_UNIFORM' or load_distribution.name == 'LOAD_DISTRIBUTION_VARYING_IN_Z' or load_distribution.name == 'LOAD_DISTRIBUTION_VARYING_ALONG_PERIMETER' or load_distribution.name == 'LOAD_DISTRIBUTION_VARYING_IN_Z_AND_ALONG_PERIMETER':
            if len(load_magnitude_parameter) != 1:
                raise ValueError('WARNING: The load parameter for the selected distribution needs to be of length 1. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_uniform = load_magnitude_parameter[0]

        elif load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR_FIRST' or load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR_SECOND':
            if len(load_magnitude_parameter) != 2:
                raise ValueError('WARNING: The load parameter for the selected distribution needs to be of length 2. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_linear_first = load_magnitude_parameter[0]
            clientObject.magnitude_linear_second = load_magnitude_parameter[1]

        # Load Location Parameter
        clientObject.load_location_rectangle = load_location.name

        if load_location.name == 'LOAD_LOCATION_RECTANGLE_CORNER_POINTS':

            if load_distribution.name == 'LOAD_DISTRIBUTION_UNIFORM' or load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR_FIRST' or load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR_SECOND':
                if len(load_location_parameter) != 5:
                    raise ValueError('WARNING: The load location parameter for the designated location and distribution type needs to be of length 5. Kindly check list inputs for completeness and correctness.')
                clientObject.load_location_first_x = load_location_parameter[0]
                clientObject.load_location_first_y = load_location_parameter[1]
                clientObject.load_location_second_x = load_location_parameter[2]
                clientObject.load_location_second_y = load_location_parameter[3]
                clientObject.axis_start_angle = load_location_parameter[4] * (pi/180)

            elif load_distribution.name == 'LOAD_DISTRIBUTION_VARYING_IN_Z':
                if len(load_location_parameter) != 5:
                    raise ValueError('WARNING: The load location parameter for the designated location and distribution type needs to be of length 5. Kindly check list inputs for completeness and correctness.')
                clientObject.load_location_first_x = load_location_parameter[0]
                clientObject.load_location_first_y = load_location_parameter[1]
                clientObject.load_location_second_x = load_location_parameter[2]
                clientObject.load_location_second_y = load_location_parameter[3]

                clientObject.load_varying_in_z_parameters = model.clientModel.factory.create('ns0:free_rectangular_load.load_varying_in_z_parameters')
                varying_in_z = load_location_parameter[4]
                for i,j in enumerate(varying_in_z):
                    frllvp = model.clientModel.factory.create('ns0:free_rectangular_load_load_varying_in_z_parameters_row')
                    frllvp.no = i+1
                    frllvp.row.distance = varying_in_z[i][0]
                    frllvp.row.factor = varying_in_z[i][1]
                    clientObject.load_varying_in_z_parameters.free_rectangular_load_load_varying_in_z_parameters.append(frllvp)

            elif load_distribution.name == 'LOAD_DISTRIBUTION_VARYING_ALONG_PERIMETER':
                if len(load_location_parameter) != 8:
                    raise ValueError('WARNING: The load location parameter for the designated location and distribution type needs to be of length 9. Kindly check list inputs for completeness and correctness.')
                clientObject.load_location_first_x = load_location_parameter[0]
                clientObject.load_location_first_y = load_location_parameter[1]
                clientObject.load_location_second_x = load_location_parameter[2]
                clientObject.load_location_second_y = load_location_parameter[3]
                clientObject.axis_definition_p1_x = load_location_parameter[4][0]
                clientObject.axis_definition_p1_y = load_location_parameter[4][1]
                clientObject.axis_definition_p1_z = load_location_parameter[4][2]
                clientObject.axis_definition_p2_x = load_location_parameter[5][0]
                clientObject.axis_definition_p2_y = load_location_parameter[5][1]
                clientObject.axis_definition_p2_z = load_location_parameter[5][2]
                clientObject.axis_start_angle = load_location_parameter[6]

                clientObject.load_varying_along_perimeter_parameters = model.clientModel.factory.create('ns0:free_rectangular_load.load_varying_along_perimeter_parameters')
                varying_along_perimeter = load_location_parameter[7]
                for i,j in enumerate(varying_along_perimeter):
                    frllvapp = model.clientModel.factory.create('ns0:free_rectangular_load_load_varying_along_perimeter_parameters_row')
                    frllvapp.no = i+1
                    frllvapp.row.alpha = varying_along_perimeter[i][0] * (pi/180)
                    frllvapp.row.factor = varying_along_perimeter[i][1]
                    clientObject.load_varying_along_perimeter_parameters.free_rectangular_load_load_varying_along_perimeter_parameters.append(frllvapp)

            elif load_distribution.name == 'LOAD_DISTRIBUTION_VARYING_IN_Z_AND_ALONG_PERIMETER':
                if len(load_location_parameter) != 9:
                    raise ValueError('WARNING: The load location parameter for the designated location and distribution type needs to be of length 9. Kindly check list inputs for completeness and correctness.')
                clientObject.load_location_first_x = load_location_parameter[0]
                clientObject.load_location_first_y = load_location_parameter[1]
                clientObject.load_location_second_x = load_location_parameter[2]
                clientObject.load_location_second_y = load_location_parameter[3]

                clientObject.load_varying_in_z_parameters = model.clientModel.factory.create('ns0:free_rectangular_load.load_varying_in_z_parameters')
                varying_in_z = load_location_parameter[4]
                for i,j in enumerate(varying_in_z):
                    frllvp = model.clientModel.factory.create('ns0:free_rectangular_load_load_varying_in_z_parameters_row')
                    frllvp.no = i+1
                    frllvp.row.distance = varying_in_z[i][0]
                    frllvp.row.factor = varying_in_z[i][1]
                    clientObject.load_varying_in_z_parameters.free_rectangular_load_load_varying_in_z_parameters.append(frllvp)

                clientObject.axis_definition_p1_x = load_location_parameter[5][0]
                clientObject.axis_definition_p1_y = load_location_parameter[5][1]
                clientObject.axis_definition_p1_z = load_location_parameter[5][2]
                clientObject.axis_definition_p2_x = load_location_parameter[6][0]
                clientObject.axis_definition_p2_y = load_location_parameter[6][1]
                clientObject.axis_definition_p2_z = load_location_parameter[6][2]
                clientObject.axis_start_angle = load_location_parameter[7]

                clientObject.load_varying_along_perimeter_parameters = model.clientModel.factory.create('ns0:free_rectangular_load.load_varying_along_perimeter_parameters')
                varying_along_perimeter = load_location_parameter[8]
                for i,j in enumerate(varying_along_perimeter):
                    frllvapp = model.clientModel.factory.create('ns0:free_rectangular_load_load_varying_along_perimeter_parameters_row')
                    frllvapp.no = i+1
                    frllvapp.row.alpha = varying_along_perimeter[i][0] * (pi/180)
                    frllvapp.row.factor = varying_along_perimeter[i][1]
                    clientObject.load_varying_along_perimeter_parameters.free_rectangular_load_load_varying_along_perimeter_parameters.append(frllvapp)

        elif load_location.name == 'LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES':

            if load_distribution.name == 'LOAD_DISTRIBUTION_UNIFORM' or load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR_FIRST' or load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR_SECOND':
                if len(load_location_parameter) != 5:
                    raise ValueError('WARNING: The load location parameter for the designated location and distribution type needs to be of length 5. Kindly check list inputs for completeness and correctness.')
                clientObject.load_location_center_x = load_location_parameter[0]
                clientObject.load_location_center_y = load_location_parameter[1]
                clientObject.load_location_center_side_a = load_location_parameter[2]
                clientObject.load_location_center_side_b = load_location_parameter[3]
                clientObject.axis_start_angle = load_location_parameter[4] * (pi/180)

            elif load_distribution.name == 'LOAD_DISTRIBUTION_VARYING_IN_Z':
                if len(load_location_parameter) != 5:
                    raise ValueError('WARNING: The load location parameter for the designated location and distribution type needs to be of length 5. Kindly check list inputs for completeness and correctness.')
                clientObject.load_location_center_x = load_location_parameter[0]
                clientObject.load_location_center_y = load_location_parameter[1]
                clientObject.load_location_center_side_a = load_location_parameter[2]
                clientObject.load_location_center_side_b = load_location_parameter[3]

                clientObject.load_varying_in_z_parameters = model.clientModel.factory.create('ns0:free_rectangular_load.load_varying_in_z_parameters')
                varying_in_z = load_location_parameter[4]
                for i,j in enumerate(varying_in_z):
                    frllvp = model.clientModel.factory.create('ns0:free_rectangular_load_load_varying_in_z_parameters_row')
                    frllvp.no = i+1
                    frllvp.row.distance = varying_in_z[i][0]
                    frllvp.row.factor = varying_in_z[i][1]
                    clientObject.load_varying_in_z_parameters.free_rectangular_load_load_varying_in_z_parameters.append(frllvp)

            elif load_distribution.name == 'LOAD_DISTRIBUTION_VARYING_ALONG_PERIMETER':
                if len(load_location_parameter) != 8:
                    raise ValueError('WARNING: The load location parameter for the designated location and distribution type needs to be of length 9. Kindly check list inputs for completeness and correctness.')
                clientObject.load_location_center_x = load_location_parameter[0]
                clientObject.load_location_center_y = load_location_parameter[1]
                clientObject.load_location_center_side_a = load_location_parameter[2]
                clientObject.load_location_center_side_b = load_location_parameter[3]
                clientObject.axis_definition_p1_x = load_location_parameter[4][0]
                clientObject.axis_definition_p1_y = load_location_parameter[4][1]
                clientObject.axis_definition_p1_z = load_location_parameter[4][2]
                clientObject.axis_definition_p2_x = load_location_parameter[5][0]
                clientObject.axis_definition_p2_y = load_location_parameter[5][1]
                clientObject.axis_definition_p2_z = load_location_parameter[5][2]
                clientObject.axis_start_angle = load_location_parameter[6]

                clientObject.load_varying_along_perimeter_parameters = model.clientModel.factory.create('ns0:free_rectangular_load.load_varying_along_perimeter_parameters')
                varying_along_perimeter = load_location_parameter[7]
                for i,j in enumerate(varying_along_perimeter):
                    frllvapp = model.clientModel.factory.create('ns0:free_rectangular_load_load_varying_along_perimeter_parameters_row')
                    frllvapp.no = i+1
                    frllvapp.row.alpha = varying_along_perimeter[i][0] * (pi/180)
                    frllvapp.row.factor = varying_along_perimeter[i][1]
                    clientObject.load_varying_along_perimeter_parameters.free_rectangular_load_load_varying_along_perimeter_parameters.append(frllvapp)

            elif load_distribution.name == 'LOAD_DISTRIBUTION_VARYING_IN_Z_AND_ALONG_PERIMETER':
                if len(load_location_parameter) != 9:
                    raise ValueError('WARNING: The load location parameter for the designated location and distribution type needs to be of length 9. Kindly check list inputs for completeness and correctness.')
                clientObject.load_location_center_x = load_location_parameter[0]
                clientObject.load_location_center_y = load_location_parameter[1]
                clientObject.load_location_center_side_a = load_location_parameter[2]
                clientObject.load_location_center_side_b = load_location_parameter[3]

                clientObject.load_varying_in_z_parameters = model.clientModel.factory.create('ns0:free_rectangular_load.load_varying_in_z_parameters')
                varying_in_z = load_location_parameter[4]
                for i,j in enumerate(varying_in_z):
                    frllvp = model.clientModel.factory.create('ns0:free_rectangular_load_load_varying_in_z_parameters_row')
                    frllvp.no = i+1
                    frllvp.row.distance = varying_in_z[i][0]
                    frllvp.row.factor = varying_in_z[i][1]
                    clientObject.load_varying_in_z_parameters.free_rectangular_load_load_varying_in_z_parameters.append(frllvp)

                clientObject.axis_definition_p1_x = load_location_parameter[5][0]
                clientObject.axis_definition_p1_y = load_location_parameter[5][1]
                clientObject.axis_definition_p1_z = load_location_parameter[5][2]
                clientObject.axis_definition_p2_x = load_location_parameter[6][0]
                clientObject.axis_definition_p2_y = load_location_parameter[6][1]
                clientObject.axis_definition_p2_z = load_location_parameter[6][2]
                clientObject.axis_start_angle = load_location_parameter[7]

                clientObject.load_varying_along_perimeter_parameters = model.clientModel.factory.create('ns0:free_rectangular_load.load_varying_along_perimeter_parameters')
                varying_along_perimeter = load_location_parameter[8]
                for i,j in enumerate(varying_along_perimeter):
                    frllvapp = model.clientModel.factory.create('ns0:free_rectangular_load_load_varying_along_perimeter_parameters_row')
                    frllvapp.no = i+1
                    frllvapp.row.alpha = varying_along_perimeter[i][0] * (pi/180)
                    frllvapp.row.factor = varying_along_perimeter[i][1]
                    clientObject.load_varying_along_perimeter_parameters.free_rectangular_load_load_varying_along_perimeter_parameters.append(frllvapp)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Free Concentrated Load to client model
        model.clientModel.service.set_free_rectangular_load(load_case_no, clientObject)

    @staticmethod
    def CircularLoad(
                 no: int = 1,
                 load_case_no: int = 1,
                 surfaces_no: str = '1',
                 load_distribution = FreeCircularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                 load_direction = FreeCircularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                 load_parameter: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surfaces_no (str): Assigned Surface(s)
            load_distribution (enum): Free Circular Load Load Distribution Enumeration
            load_projection (enum): Free Load Load Projection Enumeration
            load_direction (enum): Free Circular Load Load Direction Enumeration
            load_parameter (list): Load Parameter
                for load_distribution == FreeCircularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [magnitude_uniform, load_location_x, load_location_y, load_location_radius]
                for load_distribution == FreeCircularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
                    load_parameter = [magnitude_center, magnitude_radius, load_location_x, load_location_y, load_location_radius]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Free Concentrated Load
        clientObject = model.clientModel.factory.create('ns0:free_circular_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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
            if len(load_parameter) != 4:
                raise ValueError('WARNING: The load parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_uniform = load_parameter[0]
            clientObject.load_location_x = load_parameter[1]
            clientObject.load_location_y = load_parameter[2]
            clientObject.load_location_radius = load_parameter[3]

        elif load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR':
            if len(load_parameter) != 5:
                raise ValueError('WARNING: The load parameter needs to be of length 5. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_center = load_parameter[0]
            clientObject.magnitude_radius = load_parameter[1]
            clientObject.load_location_x = load_parameter[2]
            clientObject.load_location_y = load_parameter[3]
            clientObject.load_location_radius = load_parameter[4]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Free Concentrated Load to client model
        model.clientModel.service.set_free_circular_load(load_case_no, clientObject)

    @staticmethod
    def PolygonLoad(
                 no: int = 1,
                 load_case_no: int = 1,
                 surfaces_no: str = '1',
                 load_distribution = FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_projection = FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                 load_direction = FreePolygonLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                 load_location: list = None,
                 load_parameter: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surfaces_no (str): Assigned Surface(s)
            load_distribution (enum): Free Polygon Load Load Distribution Enumeration
            load_projection (enum): Free Load Load Projection Enumeration
            load_direction (enum): Free Polygon Load Load Direction Enumeration
            load_location (list of list): Load Location Parameter
            load_parameter (list): Load Parameter
                for load_distribution == FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_location = [[first_coordinate, second_coordinate], ...]
                    load_parameter = [magnitude_uniform]
                for load_distribution == FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
                    load_location = [[first_coordinate, second_coordinate], ...]
                    load_parameter = [magnitude_linear_1, magnitude_linear_2, magnitude_linear_3, magnitude_linear_location_1, magnitude_linear_location_2, magnitude_linear_location_3]
                for load_distribution == FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_FIRST:
                    load_location = [[first_coordinate, second_coordinate], ...]
                    load_parameter = [magnitude_linear_1, magnitude_linear_2, magnitude_linear_location_1, magnitude_linear_location_2]
                for load_distribution == FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_SECOND:
                    load_location = [[first_coordinate, second_coordinate], ...]
                    load_parameter = [magnitude_linear_1, magnitude_linear_2, magnitude_linear_location_1, magnitude_linear_location_2]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Free Concentrated Load
        clientObject = model.clientModel.factory.create('ns0:free_polygon_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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

        # Load Location
        clientObject.load_location = model.clientModel.factory.create('ns0:free_polygon_load.load_location')
        for i,j in enumerate(load_location):
            fplld = model.clientModel.factory.create('ns0:free_polygon_load_load_location_row')
            fplld.no = i+1
            fplld.row.first_coordinate = load_location[i][0]
            fplld.row.second_coordinate = load_location[i][1]
            clientObject.load_location.free_polygon_load_load_location.append(fplld)

        # Load Parameter
        if load_distribution.name == 'LOAD_DISTRIBUTION_UNIFORM':
            if len(load_parameter) != 1:
                raise ValueError('WARNING: The load parameter needs to be of length 1. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_uniform = load_parameter[0]

        elif load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR':
            if len(load_parameter) != 6:
                raise ValueError('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_linear_1 = load_parameter[0]
            clientObject.magnitude_linear_2 = load_parameter[1]
            clientObject.magnitude_linear_3 = load_parameter[2]
            clientObject.magnitude_linear_location_1 = load_parameter[3]
            clientObject.magnitude_linear_location_2 = load_parameter[4]
            clientObject.magnitude_linear_location_3 = load_parameter[5]

        elif load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR_FIRST' or load_distribution.name == 'LOAD_DISTRIBUTION_LINEAR_SECOND':
            if len(load_parameter) != 4:
                raise ValueError('WARNING: The load parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_linear_1 = load_parameter[0]
            clientObject.magnitude_linear_2 = load_parameter[1]
            clientObject.magnitude_linear_location_1 = load_parameter[2]
            clientObject.magnitude_linear_location_2 = load_parameter[3]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Free Concentrated Load to client model
        model.clientModel.service.set_free_polygon_load(load_case_no, clientObject)
