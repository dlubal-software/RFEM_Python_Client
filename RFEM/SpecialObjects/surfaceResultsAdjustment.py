from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import SurfaceResultsAdjustmentShape, SurfaceResultsAdjustmentType, SurfaceResultsAdjustmentProjection

def Child_items(mx = True,
               my = False,
               mxy = False,
               vx = False,
               vy = False,
               nx = False,
               ny = False,
               nxy = False,
               ):

    child_items = [
        {"no": 0, "row": f"main_quantity_property_id_surface_results_basic_internal_forces_mx={str(mx).lower()}"},
        {"no": 1, "row": f"main_quantity_property_id_surface_results_basic_internal_forces_my={str(my).lower()}"},
        {"no": 2, "row": f"main_quantity_property_id_surface_results_basic_internal_forces_mxy={str(mxy).lower()}"},
        {"no": 3, "row": f"main_quantity_property_id_surface_results_basic_internal_forces_vx={str(vx).lower()}"},
        {"no": 4, "row": f"main_quantity_property_id_surface_results_basic_internal_forces_vy={str(vy).lower()}"},
        {"no": 5, "row": f"main_quantity_property_id_surface_results_basic_internal_forces_nx={str(nx).lower()}"},
        {"no": 6, "row": f"main_quantity_property_id_surface_results_basic_internal_forces_ny={str(ny).lower()}"},
        {"no": 7, "row": f"main_quantity_property_id_surface_results_basic_internal_forces_nxy={str(nxy).lower()}"}
    ]

    return child_items

class SurfaceResultsAdjustment():
    def __init__(self,
                 no: int = 1,
                 shape = SurfaceResultsAdjustmentShape.SHAPE_RECTANGLE,
                 dimensions: list = None,
                 center_position: list = [0,0,0],
                 adjustment_type_in_direction_u = SurfaceResultsAdjustmentType.AVERAGING_OF_MY_MXY_VY_NY_NXY,
                 adjustment_type_in_direction_v = SurfaceResultsAdjustmentType.AVERAGING_OF_MX_MXY_VX_NX_NXY,
                 projection = SurfaceResultsAdjustmentProjection.PERPENDICULAR,
                 projection_vector: list = None,
                 surfaces: str = '',
                 name: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Surface Results Adjustment

        Args:
            no (int): Surface Results Adjustment Tag
            shape (enum): Surface Results Adjustment Shape Enumeration (Note: 'SHAPE_POLYGON' is allowed only for adjustment type: 'CONTACT_STRESS_AREA')
            dimensions (list/list of lists): Dimensions and Angular Rotation List for Shape
                for shape == SHAPE_RECTANGLE:
                    dimensions = [dimension_1, dimension_2, angular_rotation]
                for shape == SHAPE_CIRCLE:
                    dimensions = [dimension_1, angular_rotation]
                for shape == SHAPE_ELLIPSE:
                    dimensions = [dimension_1, dimension_2, angular_rotation]
                for shape == SHAPE_POLYGON:
                    dimensions = [[x1, y1, z1], [x2, y2, z2]...]
            center_position (list): Center Position List
            adjustment_type_in_direction_u (enum/list): Surface Results Adjustment Type in Direction U
            adjustment_type_in_direction_v (enum/list): Surface Results Adjustment Type in Direction V
                for adjustment type in u/v direction == AVERAGING_OF_MY_MXY_VY_NY_NXY/AVERAGING_OF_MX_MXY_VX_NX_NXY/NONE/CONTACT_STRESS_AREA:
                    adjustment_type_in_direction_u/v (enum) = Surface Results Adjustment Type Enumeration
                for adjustment type in u/v direction == USER_DEFINED/ZERO:
                    adjustment_type_in_direction_u/v (list) = [Surface Results Adjustment Type Enumeration, Child_items dictionary]
            projection (enum, optional): Surface Results Adjustment Projection Enumeration
            projection_vector (list, optional): Projection vector List in case projection
                for projection == VECTOR:
                    projection_vector (list): [coordinates_x, coordinates_y, coordinates_z]
                else:
                    projection_vector = None
            surfaces (str): Assigned to surfaces
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Result Adjustment
        clientObject = model.clientModel.factory.create('ns0:surface_results_adjustment')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Result Adjustment No.
        clientObject.no = no

        # Surface Result Adjustment Shape and Dimensions
        if shape == SurfaceResultsAdjustmentShape.SHAPE_RECTANGLE:
            clientObject.shape = shape.name
            clientObject.dimension_1 = dimensions[0]
            clientObject.dimension_2 = dimensions[1]
            clientObject.angular_rotation = dimensions[2]

        elif shape == SurfaceResultsAdjustmentShape.SHAPE_CIRCLE:
            clientObject.shape = shape.name
            clientObject.dimension_1 = dimensions[0]
            clientObject.angular_rotation = dimensions[1]

        elif shape == SurfaceResultsAdjustmentShape.SHAPE_ELLIPSE:
            clientObject.shape = shape.name
            clientObject.dimension_1 = dimensions[0]
            clientObject.dimension_2 = dimensions[1]
            clientObject.angular_rotation = dimensions[2]

        elif shape == SurfaceResultsAdjustmentShape.SHAPE_POLYGON:

            if (not isinstance(adjustment_type_in_direction_u, list) and adjustment_type_in_direction_u.name == 'CONTACT_STRESS_AREA') or \
                (not isinstance(adjustment_type_in_direction_v, list) and adjustment_type_in_direction_v.name == 'CONTACT_STRESS_AREA'):
                clientObject.shape = shape.name

            else:
                raise TypeError("WARNING! 'SHAPE_POLYGON' is allowed only for adjustment type: 'CONTACT_STRESS_AREA'")

            clientObject.polygon_points = model.clientModel.factory.create('ns0:array_of_surface_results_adjustment_polygon_points')

            # Polygon Points
            for i, j in enumerate(dimensions):
                srap = model.clientModel.factory.create('ns0:surface_results_adjustment_polygon_points_row')
                clearAttributes(srap)
                srap.no = i+1
                srap.row = model.clientModel.factory.create('ns0:surface_results_adjustment_polygon_points')
                srap.row.x = dimensions[i][0]
                srap.row.y = dimensions[i][1]
                srap.row.z = dimensions[i][2]

                clientObject.polygon_points.surface_results_adjustment_polygon_points.append(srap)

        # Surface Result Adjustment Center Position
        if shape.name != 'SHAPE_POLYGON':
            clientObject.center_position_x = center_position[0]
            clientObject.center_position_y = center_position[1]
            clientObject.center_position_z = center_position[2]

        # Surface Result Adjustment Type Direction U
        if isinstance(adjustment_type_in_direction_u, list):
            clientObject.adjustment_type_in_direction_u = adjustment_type_in_direction_u[0].name

            # Surface Result Adjustment Type USer Defined in Direction U
            if adjustment_type_in_direction_u[0] == SurfaceResultsAdjustmentType.USER_DEFINED:
                clientObject.results_to_adjust_in_direction_u = model.clientModel.factory.create('ns0:array_of_surface_results_adjustment_results_to_adjust_in_direction_u_and_child_items')

                child_items_array = []

                # Create Child Items
                for item in adjustment_type_in_direction_u[1]:
                    child_item = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_in_direction_u_and_child_items')
                    adjustment_row = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_in_direction_u_row')
                    adjustment_row.no = item["no"]
                    adjustment_row.row = item["row"]

                    child_item.surface_results_adjustment_results_to_adjust_in_direction_u = adjustment_row
                    delattr(child_item, 'child_items')

                    child_items_array.append(child_item)

                main_item = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_in_direction_u_and_child_items')
                main_item.surface_results_adjustment_results_to_adjust_in_direction_u = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_in_direction_u_row')
                main_item.surface_results_adjustment_results_to_adjust_in_direction_u.no = 0
                main_item.surface_results_adjustment_results_to_adjust_in_direction_u.row = "main_quantity_property_id_surface_results_basic_internal_forces=false"
                main_item.child_items = model.clientModel.factory.create('ns0:array_of_surface_results_adjustment_results_to_adjust_in_direction_u_and_child_items')
                main_item.child_items.item = child_items_array

                # Assign the Main Item to the Array
                clientObject.results_to_adjust_in_direction_u.item.append(main_item)

        else:
            clientObject.adjustment_type_in_direction_u = adjustment_type_in_direction_u.name

        # Surface Result Adjustment Type Direction U
        if isinstance(adjustment_type_in_direction_v, list):
            clientObject.adjustment_type_in_direction_v = adjustment_type_in_direction_v[0].name

            # Surface Result Adjustment Type USer Defined in Direction U
            if adjustment_type_in_direction_v[0] == SurfaceResultsAdjustmentType.USER_DEFINED:
                clientObject.results_to_adjust_in_direction_v = model.clientModel.factory.create('ns0:array_of_surface_results_adjustment_results_to_adjust_in_direction_v_and_child_items')

                child_items_array = []

                # Create Child Items
                for item in adjustment_type_in_direction_v[1]:
                    child_item = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_in_direction_v_and_child_items')
                    adjustment_row = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_in_direction_v_row')
                    adjustment_row.no = item["no"]
                    adjustment_row.row = item["row"]

                    child_item.surface_results_adjustment_results_to_adjust_in_direction_v = adjustment_row
                    delattr(child_item, 'child_items')

                    child_items_array.append(child_item)

                main_item = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_in_direction_v_and_child_items')
                main_item.surface_results_adjustment_results_to_adjust_in_direction_v = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_in_direction_v_row')
                main_item.surface_results_adjustment_results_to_adjust_in_direction_v.no = 0
                main_item.surface_results_adjustment_results_to_adjust_in_direction_v.row = "main_quantity_property_id_surface_results_basic_internal_forces=false"
                main_item.child_items = model.clientModel.factory.create('ns0:array_of_surface_results_adjustment_results_to_adjust_in_direction_v_and_child_items')
                main_item.child_items.item = child_items_array

                # Assign the Main Item to the Array
                clientObject.results_to_adjust_in_direction_v.item.append(main_item)

        else:
            clientObject.adjustment_type_in_direction_v = adjustment_type_in_direction_v.name

        # Surface Result Adjustment Type Zero
        u_dir_zero = isinstance(adjustment_type_in_direction_u, list) and adjustment_type_in_direction_u[0].name == 'ZERO'
        v_dir_zero = isinstance(adjustment_type_in_direction_v, list) and adjustment_type_in_direction_v[0].name == 'ZERO'

        child_items_zero = None
        if u_dir_zero and v_dir_zero:
            raise TypeError("WARNING: Surface result adjustment type in both directon can not be 'ZERO'.")

        elif u_dir_zero:
            child_items_zero = adjustment_type_in_direction_u[1]

        elif v_dir_zero:
            child_items_zero = adjustment_type_in_direction_v[1]

        if child_items_zero:
            clientObject.results_to_adjust_zero = model.clientModel.factory.create('ns0:array_of_surface_results_adjustment_results_to_adjust_zero_and_child_items')

            child_items_array = []

            # Create Child Items
            for item in child_items_zero:
                child_item = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_zero_and_child_items')
                adjustment_row = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_zero_row')
                adjustment_row.no = item["no"]
                adjustment_row.row = item["row"]

                child_item.surface_results_adjustment_results_to_adjust_zero = adjustment_row
                delattr(child_item, 'child_items')

                child_items_array.append(child_item)

            main_item = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_zero_and_child_items')
            main_item.surface_results_adjustment_results_to_adjust_zero = model.clientModel.factory.create('ns0:surface_results_adjustment_results_to_adjust_zero_row')
            main_item.surface_results_adjustment_results_to_adjust_zero.no = 0
            main_item.surface_results_adjustment_results_to_adjust_zero.row = "main_quantity_property_id_surface_results_basic_internal_forces=false"
            main_item.child_items = model.clientModel.factory.create('ns0:array_of_surface_results_adjustment_results_to_adjust_zero_and_child_items')
            main_item.child_items.item = child_items_array

            # Assign the Main Item to the Array
            clientObject.results_to_adjust_zero.item.append(main_item)

        # Surface Result Adjustment Projection
        clientObject.projection_in_direction_type = projection.name

        # Surface Result Adjustment Vector
        if projection == SurfaceResultsAdjustmentProjection.VECTOR:
            clientObject.vector_of_projection_in_direction_coordinates_x = projection_vector[0]
            clientObject.vector_of_projection_in_direction_coordinates_y = projection_vector[1]
            clientObject.vector_of_projection_in_direction_coordinates_z = projection_vector[2]

        # assigned to surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Surface Results Adjustment User defined name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface Results Adjustment client model
        model.clientModel.service.set_surface_results_adjustment(clientObject)
