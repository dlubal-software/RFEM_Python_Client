from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import ResultSectionType, ResultSectionProjection, ResultSectionResultDirection

class ResultSection():
    def __init__(self,
                 no: int = 1,
                 type = ResultSectionType.TYPE_2_POINTS_AND_VECTOR,
                 show_section_in_direction = ResultSectionResultDirection.SHOW_RESULTS_IN_LOCAL_PLUS_Z,
                 show_values_on_isolines: bool = False,
                 parameters: list = None,
                 assigned_to_surfaces: str = '',
                 assigned_to_solids: str = '',
                 params: dict = None,
                 model = Model):
        """
        Result Section

        Args:
            no (int, mandatory): Number
            type (enum, mandatory): Categories Type
            show_section_in_direction (enum, mandatory): Show section in direction
            show_values_on_isolines (bool, mandatory): Show values on isolines
            parameters (list, mandatory): Variable parameters
                if type == ResultSectionType.TYPE_LINE:
                    [lines]
                    ['1 2']
                if type == ResultSectionType.TYPE_2_POINTS_AND_VECTOR:
                    [coordinate_system, first_point_coordinates, second_point_coordinates, projection, vector]
                    [1, [1,0,0], [0,2,0], ResultSectionProjection.PROJECTION_IN_VECTOR, [1,1,1]]
            assigned_to_surfaces (str, optional) = Assigned to surfaces
            assigned_to_solids (str, optional) Assigned to solids
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (class, optional): Model instance
        """

        # Client model | Result Section
        clientObject = model.clientModel.factory.create('ns0:result_section')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Result Section No.
        clientObject.no = no

        # Result Section Type
        clientObject.type = type.name

        # Result Section Show Section in Direction
        clientObject.show_results_in_direction = show_section_in_direction.name

        # Result Section Show Values on Isolines Option
        clientObject.show_values_on_isolines_enabled = show_values_on_isolines

        # Result Section Parameters
        if type == ResultSectionType.TYPE_LINE:
            clientObject.lines = ConvertToDlString(parameters[0])
        elif type == ResultSectionType.TYPE_2_POINTS_AND_VECTOR:
            clientObject.coordinate_system = parameters[0]
            clientObject.first_point_coordinate_1 = parameters[1][0]
            clientObject.first_point_coordinate_2 = parameters[1][1]
            clientObject.first_point_coordinate_3 = parameters[1][2]
            clientObject.second_point_coordinate_1 = parameters[2][0]
            clientObject.second_point_coordinate_2 = parameters[2][1]
            clientObject.second_point_coordinate_3 = parameters[2][2]
            clientObject.projection_in_direction = parameters[3].name
            if parameters[3] == ResultSectionProjection.PROJECTION_IN_VECTOR:
                clientObject.vector_coordinate_1 = parameters[4][0]
                clientObject.vector_coordinate_2 = parameters[4][1]
                clientObject.vector_coordinate_3 = parameters[4][2]

        # Assigned to all surfaces
        clientObject.assigned_to_surfaces = ConvertToDlString(assigned_to_surfaces)

        # Assigned to all solids
        clientObject.assigned_to_solids = ConvertToDlString(assigned_to_solids)

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Result Section to client model
        model.clientModel.service.set_result_section(clientObject)

    @staticmethod
    def TwoPointsAndVector(
                           no: int = 1,
                           coordinate_system: int = 1,
                           show_section_in_direction = ResultSectionResultDirection.SHOW_RESULTS_IN_LOCAL_PLUS_Z,
                           show_values_on_isolines: bool = False,
                           first_point_coordinates: list = None,
                           second_point_coordinates: list = None,
                           projection = ResultSectionProjection.PROJECTION_IN_GLOBAL_X,
                           vector: list = None,
                           assigned_to_surfaces: str = '',
                           assigned_to_solids: str = '',
                           comment: str = '',
                           params: dict = None,
                           model = Model):
        """
        Result Section defined by 2 points and vector

        Args:
            no (int, mandatory): Number
            coordinate_system (int, mandatory): Coordinate system number
            show_section_in_direction (enum, mandatory): Show section in direction
            show_values_on_isolines (bool, mandatory): Show values on isolines option
            first_point_coordinates (list, mandatory): First point coordinates
            second_point_coordinates (list, mandatory): Second point coordinates
            projection (enum, mandatory): Projection in direction
            vector (list, optional): Vector if projection is VECTOR
            assigned_to_surfaces (str, optional) = Assigned to surfaces
            assigned_to_solids (str, optional) Assigned to solids
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (class, optional): Model instance
        """

        # Client model | Result Section
        clientObject = model.clientModel.factory.create('ns0:result_section')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Result Section No.
        clientObject.no = no

        # Result Section Coordinate System
        clientObject.coordinate_system = coordinate_system

        # Result Section Show Section in Direction
        clientObject.show_results_in_direction = show_section_in_direction.name

        # Result Section Show Values on Isolines
        clientObject.show_values_on_isolines_enabled = show_values_on_isolines

        # Result Section First Point Coordinates
        clientObject.first_point_coordinate_1 = first_point_coordinates[0]
        clientObject.first_point_coordinate_2 = first_point_coordinates[1]
        clientObject.first_point_coordinate_3 = first_point_coordinates[2]

        # Result Section Second Point Coordinates
        clientObject.second_point_coordinate_1 = second_point_coordinates[0]
        clientObject.second_point_coordinate_2 = second_point_coordinates[1]
        clientObject.second_point_coordinate_3 = second_point_coordinates[2]

        # Result Section Projection
        clientObject.projection_in_direction = projection.name

        # Result Section Projection Vector
        if projection == ResultSectionProjection.PROJECTION_IN_VECTOR:
            clientObject.vector_coordinate_1 = vector[0]
            clientObject.vector_coordinate_2 = vector[1]
            clientObject.vector_coordinate_3 = vector[2]

        # Assigned to all surfaces
        clientObject.assigned_to_surfaces = ConvertToDlString(assigned_to_surfaces)

        # Assigned to all solids
        clientObject.assigned_to_solids = ConvertToDlString(assigned_to_solids)

        # Comment
        #clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Result Section to client model
        model.clientModel.service.set_result_section(clientObject)

    @staticmethod
    def Line(
             no: int = 1,
             show_section_in_direction = ResultSectionResultDirection.SHOW_RESULTS_IN_LOCAL_PLUS_Z,
             show_values_on_isolines: bool = False,
             lines: str = '1',
             assigned_to_surfaces: str = '',
             assigned_to_solids: str = '',
             comment: str = '',
             params: dict = None,
             model = Model):
        """
        Result Section defined by line

        Args:
            no (int, mandatory): Number
            type (enum, mandatory): _description_. Defaults to ResultSectionType.TYPE_2_POINTS_AND_VECTOR.
            show_section_in_direction (enum, mandatory): _description_. Defaults to ResultSectionResultDirection.SHOW_RESULTS_IN_LOCAL_PLUS_Z.
            show_values_on_isolines (bool, mandatory): _description_. Defaults to False.
            lines (int, mandatory): Lines
            assigned_to_surfaces (str, optional) = Assigned to surfaces
            assigned_to_solids (str, optional) Assigned to solids
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (class, optional): Model instance
        """

        # Client model | Result Section
        clientObject = model.clientModel.factory.create('ns0:result_section')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Result Section No.
        clientObject.no = no

        # Result Section Type
        clientObject.type = ResultSectionType.TYPE_LINE.name

        # Result Section Show Section in Direction
        clientObject.show_results_in_direction = show_section_in_direction.name

        # Result Section Show Values on Isolines Option
        clientObject.show_values_on_isolines_enabled = show_values_on_isolines

        # Result Section Lines
        clientObject.lines = ConvertToDlString(lines)

        # Assigned to all surfaces
        clientObject.assigned_to_surfaces = ConvertToDlString(assigned_to_surfaces)

        # Assigned to all solids
        clientObject.assigned_to_solids = ConvertToDlString(assigned_to_solids)

        # Comment
        #clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Result Section to client model
        model.clientModel.service.set_result_section(clientObject)
