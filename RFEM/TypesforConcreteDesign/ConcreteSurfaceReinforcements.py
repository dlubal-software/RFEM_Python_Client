from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import SurfaceReinforcementLocationType, SurfaceReinforcementType, SurfaceReinforcementDirectionType, SurfaceReinforcementDesignDirection
from math import pi

class ConcreteSurfaceReinforcements():
    def __init__(self,
                no: int = 1,
                name: str = "RD 1",
                surfaces: str = "1",
                material: str = "2",
                location_type = SurfaceReinforcementLocationType.LOCATION_TYPE_ON_SURFACE,
                reinforcement_type = SurfaceReinforcementType.REINFORCEMENT_TYPE_REBARS,
                reinforcement_type_parameters: list = [0.01, 0.15, False],
                cover_offset: list = [True, True, 0, 0],
                reinforcement_direction = SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION,
                reinforcement_direction_parameters: list = [SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1],
                reinforcement_location: list = None,
                reinforcement_acting_region: list = None,
                comment: str = '',
                params: dict = None,
                model = Model):
        """
        Args:
            no (int): Concrete Surface Reinforcement Tag
            name (str): User Defined Name
            surfaces (str): Assigned Surfaces
            material (str): Reinforcement Material
            location_type (enum): Surface Reinforcement Location Type Enumeration
            reinforcement_type (enum): Surface Reinforcement Type Enumeration
            reinforcement_type_parameters (list): Reinforcement Type Parameters List
                for reinforcement_type = SurfaceReinforcementType.REINFORCEMENT_TYPE_REBARS:
                    reinforcement_type_parameters = [rebar_diameter, rebar_spacing, additional_transverse_reinforcement_enabled]
                    if additional_transverse_reinforcement_enabled == True:
                        reinforcement_type_parameters = [rebar_diameter, rebar_spacing, additional_transverse_reinforcement_enabled, additional_rebar_diameter, additional_rebar_spacing]
                for reinforcement_type = SurfaceReinforcementType.REINFORCEMENT_TYPE_STIRRUPS:
                    reinforcement_type_parameters = [stirrup_diameter, stirrup_spacing]
                for reinforcement_type = SurfaceReinforcementType.REINFORCEMENT_TYPE_MESH:
                    reinforcement_type_parameters = [mesh_product_range, mesh_shape, mesh_name]
            cover_offset (list): Cover Offset Parameters List
                cover_offset = [alignment_top_enabled, alignment_bottom_enabled, additional_offset_to_concrete_cover_top, additional_offset_to_concrete_cover_bottom]
            reinforcement_direction (enum): Surface Reinforcement Direction Type Enumeration
            reinforcement_direction_parameters (list): Reinforcement Direction Parameters
            reinforcement_location (list): Reinforcement Location Parameters
            reinforcement_acting_region (list): Reinforcement Acting Region Parameters
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Concrete Durabilities
        clientObject = model.clientModel.factory.create('ns0:surface_reinforcement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Concrete Durability No.
        clientObject.no = no

        # User Defined Name
        clientObject.user_defined_name_enabled = True
        clientObject.name = name

        # Assigned Surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Material
        clientObject.material = material

        # Location Type
        clientObject.location_type = location_type.name

        # Reinforcement Type
        clientObject.reinforcement_type = reinforcement_type.name
        if reinforcement_type.name == "REINFORCEMENT_TYPE_REBARS":
            clientObject.rebar_diameter = reinforcement_type_parameters[0]
            clientObject.rebar_spacing = reinforcement_type_parameters[1]

            clientObject.additional_transverse_reinforcement_enabled = reinforcement_type_parameters[2]
            if not isinstance(reinforcement_type_parameters[2], bool):
                raise Exception("WARNING: Last parameter should be type bool for cover_offset. Kindly check list inputs completeness and correctness.")

            if reinforcement_type_parameters[2]:
                clientObject.additional_rebar_diameter = reinforcement_type_parameters[3]
                clientObject.additional_rebar_spacing = reinforcement_type_parameters[4]
        elif reinforcement_type.name == "REINFORCEMENT_TYPE_STIRRUPS":
            clientObject.stirrup_diameter = reinforcement_type_parameters[0]
            clientObject.stirrup_spacing = reinforcement_type_parameters[1]
        elif reinforcement_type.name == "REINFORCEMENT_TYPE_MESH":
            clientObject.mesh_product_range = reinforcement_type_parameters[0]
            clientObject.mesh_shape = reinforcement_type_parameters[1]
            clientObject.mesh_name = reinforcement_type_parameters[2]

        # Concrete Cover Assignment
        if not isinstance(cover_offset[0], bool) and not isinstance(cover_offset[1], bool):
            raise Exception("WARNING: First two parameters should be type bool for cover_offset. Kindly check list inputs completeness and correctness.")
        clientObject.alignment_top_enabled = cover_offset[0]
        clientObject.alignment_bottom_enabled = cover_offset[1]

        if cover_offset[0]:
            clientObject.additional_offset_to_concrete_cover_top = cover_offset[2]
        if cover_offset[1]:
            clientObject.additional_offset_to_concrete_cover_bottom = cover_offset[3]

        # Reinforcement Direction
        if location_type.name == "LOCATION_TYPE_ON_SURFACE":
            clientObject.reinforcement_direction_type = reinforcement_direction.name
            if reinforcement_direction.name == "REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION":
                clientObject.design_reinforcement_direction = reinforcement_direction_parameters[0].name
            elif reinforcement_direction.name == "REINFORCEMENT_DIRECTION_TYPE_PARALLEL_TO_TWO_POINTS":
                clientObject.first_direction_point_1 = reinforcement_direction_parameters[0]
                clientObject.first_direction_point_2 = reinforcement_direction_parameters[1]
                clientObject.second_direction_point_1 = reinforcement_direction_parameters[2]
                clientObject.second_direction_point_2 = reinforcement_direction_parameters[3]
                clientObject.projection_coordinate_system = reinforcement_direction_parameters[4]
                clientObject.projection_plane = reinforcement_direction_parameters[5].name
        else:
            clientObject.reinforcement_direction_type = reinforcement_direction.name
            if reinforcement_direction.name == "REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION":
                clientObject.design_reinforcement_direction = reinforcement_direction_parameters[0].name
                clientObject.projection_coordinate_system = reinforcement_direction_parameters[1]
                clientObject.projection_plane = reinforcement_direction_parameters[2].name
            elif reinforcement_direction.name == "REINFORCEMENT_DIRECTION_TYPE_PARALLEL_TO_TWO_POINTS":
                clientObject.first_direction_point_1 = reinforcement_direction_parameters[0]
                clientObject.first_direction_point_2 = reinforcement_direction_parameters[1]
                clientObject.second_direction_point_1 = reinforcement_direction_parameters[2]
                clientObject.second_direction_point_2 = reinforcement_direction_parameters[3]
                clientObject.projection_coordinate_system = reinforcement_direction_parameters[4]
                clientObject.projection_plane = reinforcement_direction_parameters[5].name

        # Reinforcement Location
        if location_type.name == "LOCATION_TYPE_FREE_RECTANGULAR":
            clientObject.location_rectangle_type = reinforcement_location[0].name
            if reinforcement_location[0].name == "RECTANGLE_TYPE_CORNER_POINTS":
                clientObject.location_first_x = reinforcement_location[1]
                clientObject.location_first_y = reinforcement_location[2]
                clientObject.location_second_x = reinforcement_location[3]
                clientObject.location_second_y = reinforcement_location[4]
                clientObject.location_rotation = reinforcement_location[5]* pi/180
            elif reinforcement_location[0].name == "RECTANGLE_TYPE_CENTER_AND_SIDES":
                clientObject.location_center_x = reinforcement_location[1]
                clientObject.location_center_y = reinforcement_location[2]
                clientObject.location_center_side_a = reinforcement_location[3]
                clientObject.location_center_side_b = reinforcement_location[4]
                clientObject.location_rotation = reinforcement_location[5] * pi/180
        elif location_type.name == "LOCATION_TYPE_FREE_CIRCULAR":
            clientObject.location_center_x = reinforcement_location[0]
            clientObject.location_center_y = reinforcement_location[1]
            clientObject.location_radius = reinforcement_location[2]
        elif location_type.name == "LOCATION_TYPE_FREE_POLYGON":
            clientObject.polygon_points = model.clientModel.factory.create('ns0:surface_reinforcement.polygon_points')
            for i in range(len(reinforcement_location)):
                mlvlp = model.clientModel.factory.create('ns0:surface_reinforcement_polygon_points')
                mlvlp.no = i+1
                mlvlp.first_coordinate = reinforcement_location[i][0]
                mlvlp.second_coordinate = reinforcement_location[i][1]
                mlvlp.comment = reinforcement_location[i][2]
                clientObject.polygon_points.surface_reinforcement_polygon_points.append(mlvlp)

        # Reinforcement Acting Region
        if location_type.name != "LOCATION_TYPE_ON_SURFACE":
            clientObject.acting_region_from = reinforcement_acting_region[0]
            clientObject.acting_region_to = reinforcement_acting_region[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Global Parameter to client model
        model.clientModel.service.set_surface_reinforcement(clientObject)
