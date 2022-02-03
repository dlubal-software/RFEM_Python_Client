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
        Args:
            no (int): Surface Tag
            boundary_lines_no (str): Tags of Lines defining Surface
            thickness (int): Tag of Thickness assigned to Surface
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Surface
        clientObject = Model.clientModel.factory.create('ns0:surface')

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
        Model.clientModel.service.set_surface(clientObject)

    def Standard(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = {}):

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
            boundary_lines_no (str): Tags of Lines defining Standard Surface
            thickness (int): Tag of Thickness assigned to Standard Surface
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Surface
        clientObject = Model.clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_STANDARD.name

        # Reptitive code between various functions migrated to a private method
        self.type = SurfaceType.TYPE_STANDARD.name
        self.boundary_lines_no = boundary_lines_no
        self.geometry_type = geometry_type
        self.geometry_type_parameters = geometry_type_parameters
        self.thickness = thickness
        self.comment = comment
        self.params = params
        self.clientObject = clientObject
        self.__CreateGeometryAndSetToModel(self)

    def WithoutThickness(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 comment: str = '',
                 params: dict = {}):

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
            boundary_lines_no (str): Tags of Lines defining Without Thickness Surface
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Surface
        clientObject = Model.clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_WITHOUT_THICKNESS.name

        # Reptitive code between various functions migrated to a private method
        self.type = SurfaceType.TYPE_WITHOUT_THICKNESS.name
        self.boundary_lines_no = boundary_lines_no
        self.geometry_type = geometry_type
        self.geometry_type_parameters = geometry_type_parameters
        self.comment = comment
        self.params = params
        self.clientObject = clientObject
        self.__CreateGeometryAndSetToModel(self)

    def Rigid(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 comment: str = '',
                 params: dict = {}):

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
            boundary_lines_no (str): Tags of Lines defining Rigid Surface
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Surface
        clientObject = Model.clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_RIGID.name

        # Reptitive code between various functions migrated to a private method
        self.type = SurfaceType.TYPE_RIGID.name
        self.boundary_lines_no = boundary_lines_no
        self.geometry_type = geometry_type
        self.geometry_type_parameters = geometry_type_parameters
        self.comment = comment
        self.params = params
        self.clientObject = clientObject
        self.__CreateGeometryAndSetToModel(self)

    def Membrane(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = {}):

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
            boundary_lines_no (str): Tags of Lines defining Membrane Surface
            thickness (int): Tag of Thickness assigned to Membrane Surface
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Surface
        clientObject = Model.clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_MEMBRANE.name

        # Reptitive code between various functions migrated to a private method
        self.type = SurfaceType.TYPE_MEMBRANE.name
        self.boundary_lines_no = boundary_lines_no
        self.geometry_type = geometry_type
        self.geometry_type_parameters = geometry_type_parameters
        self.thickness = thickness
        self.comment = comment
        self.params = params
        self.clientObject = clientObject
        self.__CreateGeometryAndSetToModel(self)

    def WithoutMemberaneTension(self,
                 no: int = 1,
                 geometry_type = SurfaceGeometry.GEOMETRY_PLANE,
                 geometry_type_parameters = None,
                 boundary_lines_no: str = '1 2 3 4',
                 thickness: int = 1,
                 comment: str = '',
                 params: dict = {}):

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
            boundary_lines_no (str): Tags of Lines defining Without Membrane Tension Surface
            thickness (int): Tag of Thickness assigned to Without Membrane Tension Surface
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Surface
        clientObject = Model.clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Surface Type
        clientObject.type = SurfaceType.TYPE_WITHOUT_MEMBRANE_TENSION.name

        # Reptitive code between various functions migrated to a private method
        self.type = SurfaceType.TYPE_WITHOUT_MEMBRANE_TENSION.name
        self.boundary_lines_no = boundary_lines_no
        self.geometry_type = geometry_type
        self.geometry_type_parameters = geometry_type_parameters
        self.thickness = thickness
        self.comment = comment
        self.params = params
        self.clientObject = clientObject
        self.__CreateGeometryAndSetToModel(self)

    def LoadDistribution(self,
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
                 params: dict = {}):

        '''
        Args:
            no (int): Surface Tag
            boundary_lines_no (str): Tags of Lines defining Load Distribution Surface
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
            params (dict, optional): Parameters
        '''

        # Client model | Surface
        clientObject = Model.clientModel.factory.create('ns0:surface')

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
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        Model.clientModel.service.set_surface(clientObject)

    def __CreateGeometryAndSetToModel(self):

        # Geometry Type
        boundary_lines_list = self.boundary_lines_no.split(sep= ' ')

        if self.geometry_type.name == 'GEOMETRY_NURBS':
            if len(self.geometry_type_parameters) != 4:
                raise Exception('WARNING: The geometry type parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            for line in boundary_lines_list:
                if Model.clientModel.service.get_line(int(line))['type'] != 'TYPE_NURBS':
                    raise Exception('WARNING: For a NURBS Surface, the boundary lines need to be NURBS Curves')
            self.clientObject.nurbs_control_point_count_in_direction_u = self.geometry_type_parameters[0]
            self.clientObject.nurbs_control_point_count_in_direction_v = self.geometry_type_parameters[1]
            self.clientObject.nurbs_order_in_direction_u = self.geometry_type_parameters[2]
            self.clientObject.nurbs_order_in_direction_v = self.geometry_type_parameters[3]

        elif self.geometry_type.name == 'GEOMETRY_PLANE':
            self.geometry_type_parameters = None

        elif self.geometry_type.name == 'GEOMETRY_QUADRANGLE':
            if len(self.geometry_type_parameters) != 4:
                raise Exception('WARNING: The geometry type parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            self.clientObject.quadrangle_corner_node_1 = self.geometry_type_parameters[0]
            self.clientObject.quadrangle_corner_node_2 = self.geometry_type_parameters[1]
            self.clientObject.quadrangle_corner_node_3 = self.geometry_type_parameters[2]
            self.clientObject.quadrangle_corner_node_4 = self.geometry_type_parameters[3]

        self.clientObject.geometry = self.geometry_type.name

        # Lines No. (e.g. "5 7 8 12")
        self.clientObject.boundary_lines = ConvertToDlString(self.boundary_lines_no)

        # Thickness
        if self.type == 'TYPE_STANDARD'or self.type == 'TYPE_MEMBRANE' or self.type == 'TYPE_WITHOUT_MEMBRANE_TENSION':
            self.clientObject.thickness = self.thickness

        # Comment
        self.clientObject.comment = self.comment

        # Adding optional parameters via dictionary
        for key in self.params:
            self.clientObject[key] = self.params[key]

        # Add Surface to client model
        Model.clientModel.service.set_surface(self.clientObject)
