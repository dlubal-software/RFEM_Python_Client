from RFEM.enums import SurfaceGeometry, SurfaceLoadDistributionDirection, SurfaceType, ObjectTypes
from RFEM.initModel import Model, clearAtributes, ConvertToDlString, ConvertStrToListOfInt
import math

def CreateGeometryAndSetToModel(no, surface_type, boundary_lines_no, geometry_type, geometry_type_parameters, thickness = None, comment = None, params = None, model = Model):
    '''
        Args:
            no (int): Surface Tag
            surface_type (enum): Surface Type Enumeration
            boundary_lines_no (str): Numbers of Lines defining Standard Surface
            geometry_type (enum): Geometry Type Enumeration
            geometry_type_parameters (list): Geometry Type Parameters
                for geometry_type == SurfaceGeometry.GEOMETRY_NURBS:
                    geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
                for geometry_type == SurfaceGeometry.GEOMETRY_PLANE:
                    geometry_type_parameters = None
                for geometry_type == SurfaceGeometry.GEOMETRY_QUADRANGLE:
                    geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
                for geometry_type == SurfaceGeometry.GEOMETRY_ROTATED:
                    geometry_type_parameters = [rotated_angle_of_rotation, [rotated_point_p_x, rotated_point_p_y, rotated_point_p_z], [rotated_point_r_x, rotated_point_r_y, rotated_point_r_z], rotated_boundary_line]
            thickness (int): Tag of Thickness assigned to Standard Surface
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
    # Client model | Surface
    clientObject = model.clientModel.factory.create('ns0:surface')

    # Clears object atributes | Sets all atributes to None
    clearAtributes(clientObject)

    # Surface No.
    clientObject.no = no

    # Surface Type
    clientObject.type = surface_type.name

    # Geometry Type
    boundary_lines_list = boundary_lines_no.split(sep= ' ')
    if geometry_type.name == 'GEOMETRY_NURBS':
        if len(geometry_type_parameters) != 4:
            raise Exception('WARNING: The geometry type parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
        for line in boundary_lines_list:
            if model.clientModel.service.get_line(int(line))['type'] != 'TYPE_NURBS':
                raise Exception('WARNING: For a NURBS Surface, the boundary lines need to be NURBS Curves')
        clientObject.nurbs_control_point_count_in_direction_u = geometry_type_parameters[0]
        clientObject.nurbs_control_point_count_in_direction_v = geometry_type_parameters[1]
        clientObject.nurbs_order_in_direction_u = geometry_type_parameters[2]
        clientObject.nurbs_order_in_direction_v = geometry_type_parameters[3]
    elif geometry_type.name == 'GEOMETRY_PLANE':
        geometry_type_parameters = None
    elif geometry_type.name == 'GEOMETRY_ROTATED':
        clientObject.rotated_angle_of_rotation = geometry_type_parameters[0] * (math.pi/180)
        clientObject.rotated_point_p_x = geometry_type_parameters[1][0]
        clientObject.rotated_point_p_y = geometry_type_parameters[1][1]
        clientObject.rotated_point_p_z = geometry_type_parameters[1][2]
        clientObject.rotated_point_r_x = geometry_type_parameters[2][0]
        clientObject.rotated_point_r_y = geometry_type_parameters[2][1]
        clientObject.rotated_point_r_z = geometry_type_parameters[2][2]
        clientObject.rotated_boundary_line = geometry_type_parameters[3]
    elif geometry_type.name == 'GEOMETRY_QUADRANGLE':
        if len(geometry_type_parameters) != 4:
            raise Exception('WARNING: The geometry type parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
        clientObject.quadrangle_corner_node_1 = geometry_type_parameters[0]
        clientObject.quadrangle_corner_node_2 = geometry_type_parameters[1]
        clientObject.quadrangle_corner_node_3 = geometry_type_parameters[2]
        clientObject.quadrangle_corner_node_4 = geometry_type_parameters[3]
    clientObject.geometry = geometry_type.name

    # Lines No. (e.g. "5 7 8 12")
    clientObject.boundary_lines = ConvertToDlString(boundary_lines_no)

    # Thickness
    if type == 'TYPE_STANDARD'or type == 'TYPE_MEMBRANE' or type == 'TYPE_WITHOUT_MEMBRANE_TENSION':
        clientObject.thickness = thickness

    # Comment
    clientObject.comment = comment

    # Adding optional parameters via dictionary
    if params:
        for key in params:
            clientObject[key] = params[key]

    # Add Surface to client model
    model.clientModel.service.set_surface(clientObject)

class Surface():
    def __init__(self,
                 no: int = 1,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surface Tag
            boundary_lines_no (str): Numbers of Lines defining Surface
            thickness (int): Tag of Thickness assigned to Surface
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Surface
        clientObject = model.clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Lines No. (e.g. "5 7 8 12")
        clientObject.boundary_lines = ConvertToDlString(boundary_lines_no)

        # Thickness
        clientObject.thickness = thickness

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface to client model
        model.clientModel.service.set_surface(clientObject)

    @staticmethod
    def Standard(
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surface Tag
            geometry_type (enum): Surface Geometry Type Enumeration
            geometry_type_parameters (list): Geometry Type Parameters
                for geometry_type == SurfaceGeometry.GEOMETRY_NURBS:
                    geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
                for geometry_type == SurfaceGeometry.GEOMETRY_PLANE:
                    geometry_type_parameters = None
                for geometry_type == SurfaceGeometry.GEOMETRY_QUADRANGLE:
                    geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
            boundary_lines_no (str): Numbers of Lines defining Standard Surface
            thickness (int): Tag of Thickness assigned to Standard Surface
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        CreateGeometryAndSetToModel(no, SurfaceType.TYPE_STANDARD, boundary_lines_no, geometry_type, geometry_type_parameters, thickness, comment, params, model)

    @staticmethod
    def WithoutThickness(
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surface Tag
            geometry_type (enum): Surface Geometry Type Enumeration
            geometry_type_parameters (list): Geometry Type Parameters
                for geometry_type == SurfaceGeometry.GEOMETRY_NURBS:
                    geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
                for geometry_type == SurfaceGeometry.GEOMETRY_PLANE:
                    geometry_type_parameters = None
                for geometry_type == SurfaceGeometry.GEOMETRY_QUADRANGLE:
                    geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
            boundary_lines_no (str): Numbers of Lines defining Without Thickness Surface
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        CreateGeometryAndSetToModel(no, SurfaceType.TYPE_WITHOUT_THICKNESS, boundary_lines_no, geometry_type, geometry_type_parameters, comment=comment, params=params, model=model)

    @staticmethod
    def Rigid(
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surface Tag
            geometry_type (enum): Surface Geometry Type Enumeration
            geometry_type_parameters (list): Geometry Type Parameters
                for geometry_type == SurfaceGeometry.GEOMETRY_NURBS:
                    geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
                for geometry_type == SurfaceGeometry.GEOMETRY_PLANE:
                    geometry_type_parameters = None
                for geometry_type == SurfaceGeometry.GEOMETRY_QUADRANGLE:
                    geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
            boundary_lines_no (str): Numbers of Lines defining Rigid Surface
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        CreateGeometryAndSetToModel(no, SurfaceType.TYPE_RIGID, boundary_lines_no, geometry_type, geometry_type_parameters, comment=comment, params=params, model=model)

    @staticmethod
    def Membrane(
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surface Tag
            geometry_type (enum): Surface Geometry Type Enumeration
            geometry_type_parameters (list): Geometry Type Parameters
                for geometry_type == SurfaceGeometry.GEOMETRY_NURBS:
                    geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
                for geometry_type == SurfaceGeometry.GEOMETRY_PLANE:
                    geometry_type_parameters = None
                for geometry_type == SurfaceGeometry.GEOMETRY_QUADRANGLE:
                    geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
            boundary_lines_no (str): Numbers of Lines defining Membrane Surface
            thickness (int): Tag of Thickness assigned to Membrane Surface
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        CreateGeometryAndSetToModel(no, SurfaceType.TYPE_MEMBRANE, boundary_lines_no, geometry_type, geometry_type_parameters, thickness, comment, params, model)

    @staticmethod
    def WithoutMemberaneTension(
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surface Tag
            geometry_type (enum): Surface Geometry Type Enumeration
            geometry_type_parameters (list): Geometry Type Parameters
                for geometry_type == SurfaceGeometry.GEOMETRY_NURBS:
                    geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
                for geometry_type == SurfaceGeometry.GEOMETRY_PLANE:
                    geometry_type_parameters = None
                for geometry_type == SurfaceGeometry.GEOMETRY_QUADRANGLE:
                    geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
            boundary_lines_no (str): Numbers of Lines defining Without Membrane Tension Surface
            thickness (int): Tag of Thickness assigned to Without Membrane Tension Surface
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        CreateGeometryAndSetToModel(no, SurfaceType.TYPE_WITHOUT_MEMBRANE_TENSION, boundary_lines_no, geometry_type, geometry_type_parameters, thickness, comment, params, model)

    @staticmethod
    def LoadDistribution(
                 no: int = 1,
                 boundary_lines_no: str = '1 2 3 4',
                 load_transfer_direction = SurfaceLoadDistributionDirection.LOAD_TRANSFER_DIRECTION_IN_X,
                 surface_weight_enabled: bool = False,
                 surface_weight: float = None,
                 excluded_members = None,
                 excluded_parallel_to_members = None,
                 excluded_lines = None,
                 excluded_parallel_to_lines = None,
                 loaded_members = None,
                 loaded_lines = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surface Tag
            boundary_lines_no (str): Numbers of Lines defining Load Distribution Surface
            load_transfer_direction (enum): Surface Load Transfer Direction Enumeration
            surface_weight_enabled (bool): Activate/De-Activate Surface Weight
            surface_weight (float): Magnitude of Surface Weight
            excluded_members (str): Tag of Members to be excluded from Load Distribution
            excluded_parallel_to_members (str): Tag of Members to which parallel Members are excluded from Load Distribution
            excluded_lines (str): Tag of Lines to be excluded from Load Distribution
            excluded_parallel_to_lines (str): Tag of Lines to which parallel Lines are excluded from Load Distribution
            loaded_members (str): Tag of Loaded Members
            loaded_lines (str): Tag of Loaded Lines
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Surface
        clientObject = model.clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_LOAD_TRANSFER.name

        # Geometry Type
        clientObject.geometry = SurfaceGeometry.GEOMETRY_PLANE.name

        # Lines No. (e.g. "5 7 8 12")
        clientObject.boundary_lines = ConvertToDlString(boundary_lines_no)

        # Surface Load Distribution Direction
        clientObject.load_transfer_direction = load_transfer_direction.name

        # Surface Weight
        clientObject.is_surface_weight_enabled = surface_weight_enabled
        clientObject.surface_weight = surface_weight

        # Loading Parameters
        if excluded_members is not None:
            clientObject.excluded_members = ConvertToDlString(excluded_members)
        if excluded_parallel_to_members is not None:
            clientObject.excluded_parallel_to_members = ConvertToDlString(excluded_parallel_to_members)
        if excluded_lines is not None:
            clientObject.excluded_lines = ConvertToDlString(excluded_lines)
        if excluded_parallel_to_lines is not None:
            clientObject.excluded_parallel_to_lines = ConvertToDlString(excluded_parallel_to_lines)
        if loaded_members is not None:
            clientObject.loaded_members = ConvertToDlString(loaded_members)
        if loaded_lines is not None:
            clientObject.loaded_lines = ConvertToDlString(loaded_lines)
        if loaded_lines is None and loaded_members is None:
            raise Exception('WARNING: Loaded lines and/or members need to be specified.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface to client model
        model.clientModel.service.set_surface(clientObject)

    @staticmethod
    def DeleteSurface(surfaces_no: str = '1 2', model = Model):

        '''
        Args:
            surfaces_no (str): Numbers of Surfaces to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete surfaces from client model
        for surface in ConvertStrToListOfInt(surfaces_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_SURFACE.name, surface)
