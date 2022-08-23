from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import SurfaceResultsAdjustmentShape, SurfaceResultsAdjustmentType, SurfaceResultsAdjustmentProjection

class SurfaceResultsAdjustment():
    def __init__(self,
                 no: int = 1,
                 shape = SurfaceResultsAdjustmentShape.SHAPE_RECTANGLE,
                 dimensions: list = None,
                 center_position: list = None,
                 adjustment_type_in_direction_u = SurfaceResultsAdjustmentType.AVERAGING_OF_MY_MXY_VY_NY_NXY,
                 adjustment_type_in_direction_v = SurfaceResultsAdjustmentType.AVERAGING_OF_MX_MXY_VX_NX_NXY,
                 projection = SurfaceResultsAdjustmentProjection.PERPENDICULAR,
                 projection_vector: list = None,
                 surfaces: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Surface Results Adjustment

        Args:
            no (int): Surface Results Adjustment Tag
            shape (enum): Surface Results Adjustment Shape Enumeration
            dimensions (list): Dimensions and Angular Rotation List
            center_position (list, optional): Center Position List
            adjustment_type_in_direction_u (enum, optional): Surface Results Adjustment Type Enumeration
            adjustment_type_in_direction_v (enum, optional): Surface Results Adjustment Type Enumeration
            projection (enum, optional): Surface Results Adjustment Projection Enumeration
            projection_vector (list, optional): Projection vector List in case projection == VECTOR
            surfaces (str, optional): Assigned to surfaces
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Result Adjustment
        clientObject = model.clientModel.factory.create('ns0:surface_results_adjustment')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Result Adjustment No.
        clientObject.no = no

        # Surface Result Adjustment Shape
        clientObject.shape = shape.name

        # Surface Result Adjustment Dimensions
        if shape == SurfaceResultsAdjustmentShape.SHAPE_RECTANGLE:
            clientObject.dimension_1 = dimensions[0]
            clientObject.dimension_2 = dimensions[1]
            clientObject.angular_rotation = dimensions[2]
        elif shape == SurfaceResultsAdjustmentShape.SHAPE_CIRCLE:
            clientObject.dimension_1 = dimensions[0]
            clientObject.angular_rotaSurfaceResultsAdjustmentShapetion = dimensions[1]
        elif shape == SurfaceResultsAdjustmentShape.SHAPE_ELLIPSE:
            clientObject.dimension_1 = dimensions[0]
            clientObject.dimension_2 = dimensions[1]
            clientObject.angular_rotation = dimensions[2]

        # Surface Result Adjustment Center Position
        if center_position:
            clientObject.center_position_x = center_position[0]
            clientObject.center_position_y = center_position[1]
            clientObject.center_position_z = center_position[2]
        else:
            clientObject.center_position_x = 0
            clientObject.center_position_y = 0
            clientObject.center_position_z = 0

        # Surface Result Adjustment Type
        clientObject.adjustment_type_in_direction_u = adjustment_type_in_direction_u.name
        clientObject.adjustment_type_in_direction_v = adjustment_type_in_direction_v.name

        # Surface Result Adjustment Projection
        clientObject.projection_in_direction_type = projection.name

        # Surface Result Adjustment Vector
        if projection == SurfaceResultsAdjustmentProjection.VECTOR:
            clientObject.vector_of_projection_in_direction_coordinates_x = projection_vector[0]
            clientObject.vector_of_projection_in_direction_coordinates_y = projection_vector[1]
            clientObject.vector_of_projection_in_direction_coordinates_z = projection_vector[2]

        # assigned to surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Result Adjustmentto client model
        model.clientModel.service.set_surface_results_adjustment(clientObject)
