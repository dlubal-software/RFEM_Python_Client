from os import sep
from RFEM.enums import SurfaceGeometry, SurfaceLoadDistributionDirection, SurfaceType
from RFEM.initModel import *

class Surface():
    def __init__(self,
                 no: int = 1,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = {}):

        '''
        Assigns surface without any further options.
        Surface is a Standard planar surface by default.
        '''

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:surface')

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
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_surface(clientObject)

    def Standard(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = {}):

        '''
        for geometry_type = SurfaceGeometry.GEOMETRY_NURBS:
            geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
        
        for geometry_type = SurfaceGeometry.GEOMETRY_PLANE:
            geometry_type_parameters = None
        
        for geometry_type = SurfaceGeometry.GEOMETRY_QUADRANGLE:
            geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
        '''

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_STANDARD.name

        # Geometry Type
        boundary_lines_list = boundary_lines_no.split(sep= ' ')

        if geometry_type.name == 'GEOMETRY_NURBS':
            if len(geometry_type_parameters) != 4:
                raise Exception('WARNING: The geometry type parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            for line in boundary_lines_list:
                if clientModel.service.get_line(int(line))['type'] != 'TYPE_NURBS':
                    raise Exception('WARNING: For a NURBS Surface, the boundary lines need to be NURBS Curves')
            clientObject.nurbs_control_point_count_in_direction_u = geometry_type_parameters[0]
            clientObject.nurbs_control_point_count_in_direction_v = geometry_type_parameters[1]
            clientObject.nurbs_order_in_direction_u = geometry_type_parameters[2]
            clientObject.nurbs_order_in_direction_v = geometry_type_parameters[3]
        
        elif geometry_type.name == 'GEOMETRY_PLANE':
            geometry_type_parameters = None
        
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
        clientObject.thickness = thickness

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_surface(clientObject)

    def WithoutThickness(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 comment: str = '',
                 params: dict = {}):

        '''
        for geometry_type = SurfaceGeometry.GEOMETRY_NURBS:
            geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
        
        for geometry_type = SurfaceGeometry.GEOMETRY_PLANE:
            geometry_type_parameters = None
        
        for geometry_type = SurfaceGeometry.GEOMETRY_QUADRANGLE:
            geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
        '''

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_WITHOUT_THICKNESS.name

        # Geometry Type
        boundary_lines_list = boundary_lines_no.split(sep= ' ')

        if geometry_type.name == 'GEOMETRY_NURBS':
            if len(geometry_type_parameters) != 4:
                raise Exception('WARNING: The geometry type parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            for line in boundary_lines_list:
                if clientModel.service.get_line(int(line))['type'] != 'TYPE_NURBS':
                    raise Exception('WARNING: For a NURBS Surface, the boundary lines need to be NURBS Curves')
            clientObject.nurbs_control_point_count_in_direction_u = geometry_type_parameters[0]
            clientObject.nurbs_control_point_count_in_direction_v = geometry_type_parameters[1]
            clientObject.nurbs_order_in_direction_u = geometry_type_parameters[2]
            clientObject.nurbs_order_in_direction_v = geometry_type_parameters[3]
        
        elif geometry_type.name == 'GEOMETRY_PLANE':
            geometry_type_parameters = None
        
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

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_surface(clientObject)

    def Rigid(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 comment: str = '',
                 params: dict = {}):

        '''
        for geometry_type = SurfaceGeometry.GEOMETRY_NURBS:
            geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
        
        for geometry_type = SurfaceGeometry.GEOMETRY_PLANE:
            geometry_type_parameters = None
        
        for geometry_type = SurfaceGeometry.GEOMETRY_QUADRANGLE:
            geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
        '''

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_RIGID.name

        # Geometry Type
        boundary_lines_list = boundary_lines_no.split(sep= ' ')

        if geometry_type.name == 'GEOMETRY_NURBS':
            if len(geometry_type_parameters) != 4:
                raise Exception('WARNING: The geometry type parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            for line in boundary_lines_list:
                if clientModel.service.get_line(int(line))['type'] != 'TYPE_NURBS':
                    raise Exception('WARNING: For a NURBS Surface, the boundary lines need to be NURBS Curves')
            clientObject.nurbs_control_point_count_in_direction_u = geometry_type_parameters[0]
            clientObject.nurbs_control_point_count_in_direction_v = geometry_type_parameters[1]
            clientObject.nurbs_order_in_direction_u = geometry_type_parameters[2]
            clientObject.nurbs_order_in_direction_v = geometry_type_parameters[3]
        
        elif geometry_type.name == 'GEOMETRY_PLANE':
            geometry_type_parameters = None
        
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

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_surface(clientObject)

    def Membrane(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = {}):

        '''
        for geometry_type = SurfaceGeometry.GEOMETRY_NURBS:
            geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
        
        for geometry_type = SurfaceGeometry.GEOMETRY_PLANE:
            geometry_type_parameters = None
        
        for geometry_type = SurfaceGeometry.GEOMETRY_QUADRANGLE:
            geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
        '''

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_MEMBRANE.name

        # Geometry Type
        boundary_lines_list = boundary_lines_no.split(sep= ' ')

        if geometry_type.name == 'GEOMETRY_NURBS':
            if len(geometry_type_parameters) != 4:
                raise Exception('WARNING: The geometry type parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            for line in boundary_lines_list:
                if clientModel.service.get_line(int(line))['type'] != 'TYPE_NURBS':
                    raise Exception('WARNING: For a NURBS Surface, the boundary lines need to be NURBS Curves')
            clientObject.nurbs_control_point_count_in_direction_u = geometry_type_parameters[0]
            clientObject.nurbs_control_point_count_in_direction_v = geometry_type_parameters[1]
            clientObject.nurbs_order_in_direction_u = geometry_type_parameters[2]
            clientObject.nurbs_order_in_direction_v = geometry_type_parameters[3]
        
        elif geometry_type.name == 'GEOMETRY_PLANE':
            geometry_type_parameters = None
        
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
        clientObject.thickness = thickness

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_surface(clientObject)

    def WithoutMemberaneTension(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = {}):

        '''
        for geometry_type = SurfaceGeometry.GEOMETRY_NURBS:
            geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
        
        for geometry_type = SurfaceGeometry.GEOMETRY_PLANE:
            geometry_type_parameters = None
        
        for geometry_type = SurfaceGeometry.GEOMETRY_QUADRANGLE:
            geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
        '''

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_WITHOUT_MEMBRANE_TENSION.name

        # Geometry Type
        boundary_lines_list = boundary_lines_no.split(sep= ' ')

        if geometry_type.name == 'GEOMETRY_NURBS':
            if len(geometry_type_parameters) != 4:
                raise Exception('WARNING: The geometry type parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            for line in boundary_lines_list:
                if clientModel.service.get_line(int(line))['type'] != 'TYPE_NURBS':
                    raise Exception('WARNING: For a NURBS Surface, the boundary lines need to be NURBS Curves')
            clientObject.nurbs_control_point_count_in_direction_u = geometry_type_parameters[0]
            clientObject.nurbs_control_point_count_in_direction_v = geometry_type_parameters[1]
            clientObject.nurbs_order_in_direction_u = geometry_type_parameters[2]
            clientObject.nurbs_order_in_direction_v = geometry_type_parameters[3]
        
        elif geometry_type.name == 'GEOMETRY_PLANE':
            geometry_type_parameters = None
        
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
        clientObject.thickness = thickness

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_surface(clientObject)

    def LoadDistribution(self,
                 no: int = 1,
                 boundary_lines_no: str = '1 2 3 4',
                 load_distribution_direction = SurfaceLoadDistributionDirection.LOAD_DISTRIBUTION_DIRECTION_IN_X,
                 surface_weight_enabled: bool = False,
                 surface_weight: float = None,
                 excluded_members = None,
                 excluded_parallel_to_members = None,
                 excluded_lines = None,
                 excluded_parallel_to_lines = None,
                 loaded_members = None,
                 loaded_lines = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        for geometry_type = SurfaceGeometry.GEOMETRY_NURBS:
            geometry_type_parameters = [nurbs_control_point_count_in_direction_u, nurbs_control_point_count_in_direction_v, nurbs_order_in_direction_u, nurbs_order_in_direction_v]
        
        for geometry_type = SurfaceGeometry.GEOMETRY_PLANE:
            geometry_type_parameters = None
        
        for geometry_type = SurfaceGeometry.GEOMETRY_QUADRANGLE:
            geometry_type_parameters = [quadrangle_corner_node_1, quadrangle_corner_node_2, quadrangle_corner_node_3, quadrangle_corner_node_4]
        '''

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_LOAD_DISTRIBUTION.name

        # Geometry Type
        clientObject.geometry = SurfaceGeometry.GEOMETRY_PLANE.name

        # Lines No. (e.g. "5 7 8 12")
        clientObject.boundary_lines = ConvertToDlString(boundary_lines_no)

        # Surface Load Distribution Direction
        clientObject.load_distribution_direction = load_distribution_direction.name

        # Surface Weight
        clientObject.is_surface_weight_enabled = surface_weight_enabled
        clientObject.surface_weight = surface_weight

        # Loading Parameters
        if excluded_members != None:
            clientObject.excluded_members = ConvertToDlString(excluded_members)
        if excluded_parallel_to_members != None:
            clientObject.excluded_parallel_to_members = ConvertToDlString(excluded_parallel_to_members)
        if excluded_lines != None:
            clientObject.excluded_lines = ConvertToDlString(excluded_lines)
        if excluded_parallel_to_lines != None:
            clientObject.excluded_parallel_to_lines = ConvertToDlString(excluded_parallel_to_lines)
        if loaded_members != None:
            clientObject.loaded_members = ConvertToDlString(loaded_members)
        if loaded_lines != None:
            clientObject.loaded_lines = ConvertToDlString(loaded_lines)
        if loaded_lines == None and loaded_members == None:
            raise Exception('WARNING: Loaded lines and/or members need to be specified.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_surface(clientObject)