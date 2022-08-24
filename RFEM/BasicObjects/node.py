from RFEM.enums import NodeType
from RFEM.enums import NodeCoordinateSystemType
from RFEM.enums import NodeReferenceType, ObjectTypes
from RFEM.initModel import Model, clearAtributes, ConvertStrToListOfInt
from math import pi

class Node():
    def __init__(self,
                 no: int = 1,
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Node Tag
            coordinate_X (float): X-Coordinate
            coordinate_Y (float): Y-Coordinate
            coordinate_Z (float): Z-Coordinate
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Coordinates
        clientObject.coordinate_1 = coordinate_X
        clientObject.coordinate_2 = coordinate_Y
        clientObject.coordinate_3 = coordinate_Z

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Node to client model
        model.clientModel.service.set_node(clientObject)

    @staticmethod
    def Standard(
                 no: int = 1,
                 coordinate_system: list = None,
                 coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_CARTESIAN,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Node Tag
            coordinate_system (list): Coordinate System
              for coordinate_system_type == NodeCoordinateSystemType.COORDINATE_SYSTEM_CARTESIAN;
                coordinate_system = [X, Y, Z]
              for coordinate_system_type == NodeCoordinateSystemType.COORDINATE_SYSTEM_X_CYLINDRICAL;
                coordinate_system = [X, R, θ]
              for coordinate_system_type == NodeCoordinateSystemType.COORDINATE_SYSTEM_Y_CYLINDRICAL;
                coordinate_system = [R, Ύ, θ]
              for coordinate_system_type == NodeCoordinateSystemType.COORDINATE_SYSTEM_Z_CYLINDRICAL;
                coordinate_system = [R, θ, Z]
              for coordinate_system_type == NodeCoordinateSystemType.COORDINATE_SYSTEM_POLAR:
                coordinate_system = [R, θ, φ]
            coordinate_system_type (enum): Coordinate System Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Node Type
        clientObject.type = NodeType.TYPE_STANDARD.name

        # Coordinates

        clientObject.coordinate_system_type = coordinate_system_type.name

        if len(coordinate_system) != 3:
            raise Exception('WARNING: The coordinate system needs to be of length 3.')

        if not all(isinstance(x, (int, float)) for x in coordinate_system):
            raise Exception ('WARNING: Coordinate system should be type "int" or "float".')


        if clientObject.coordinate_system_type == "COORDINATE_SYSTEM_CARTESIAN":
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1]
            clientObject.coordinate_3 = coordinate_system[2]

        elif clientObject.coordinate_system_type == "COORDINATE_SYSTEM_X_CYLINDRICAL":
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1]
            clientObject.coordinate_3 = coordinate_system[2] * (pi/180)

        elif clientObject.coordinate_system_type == "COORDINATE_SYSTEM_Y_CYLINDRICAL":
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1]
            clientObject.coordinate_3 = coordinate_system[2] * (pi/180)

        elif clientObject.coordinate_system_type == "COORDINATE_SYSTEM_Z_CYLINDRICAL":
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1] * (pi/180)
            clientObject.coordinate_3 = coordinate_system[2]

        elif clientObject.coordinate_system_type == "COORDINATE_SYSTEM_POLAR":
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1] * (pi/180)
            clientObject.coordinate_3 = coordinate_system[2] * (pi/180)

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Node to client model
        model.clientModel.service.set_node(clientObject)


    @staticmethod
    def BetweenTwoNodes(
                 no: int = 1,
                 start_node_no: int = 1,
                 end_node_no: int = 2,
                 node_reference = NodeReferenceType.REFERENCE_TYPE_L,
                 length_between_i_and_j: int = 1,
                 parameters = [True, 50],
                 offset_y: int = 0,
                 offset_z: int = 0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Node Tag
            start_node_no (int): Start Node
            end_node_no (int): End Node
            node_reference (enum): Node Reference Enumeration
            length_between_i_and_j (float): Length between 2 Nodes
            parameters (list):
              if distance_from_start_relative:
                parameters = [True, %]
              if distance_from_start_absolute:
                parameters = [False, magnitude]
            offset_y (float): Offset in Y-Direction
            offset_z (float): Offset in Z-Direction
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Node Type
        clientObject.type = NodeType.TYPE_BETWEEN_TWO_NODES.name

        # Start Node No.
        clientObject.between_two_nodes_start_node = start_node_no

        # End Node No.
        clientObject.between_two_nodes_end_node = end_node_no

         # Length between i and j

        clientObject.reference_type = node_reference.name

        clientObject.reference_object_projected_length = length_between_i_and_j

        # Distance between node k and start point

        if parameters[0]: #if parameters[0]==True
            clientObject.distance_from_start_relative = parameters[1]
        else:
            clientObject.distance_from_start_absolute = parameters[1]

        # Offset_local_y
        clientObject.offset_in_local_direction_y = offset_y

        # Offset_local_z
        clientObject.offset_in_local_direction_z = offset_z

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Node to client model
        model.clientModel.service.set_node(clientObject)

    @staticmethod
    def BetweenTwoPoints(
                 no: int = 1,
                 start_point_x: float = 0.0,
                 start_point_y: float = 0.0,
                 start_point_z: float = 0.0,
                 end_point_x: float = 1.0,
                 end_point_y: float = 1.0,
                 end_point_z: float = 1.0,
                 node_reference = NodeReferenceType.REFERENCE_TYPE_L,
                 parameters = [True, 0.5],
                 offset_y: float = 0.0,
                 offset_z: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Node Tag
            start_point_x (float): Start Point in X-Coordinate
            start_point_y (float): Start Point in Y-Coordinate
            start_point_z (float): Start Point in Z-Coordinate
            end_point_x (float): End Point in X-Coordinate
            end_point_y (float): End Point in Y-Coordinate
            end_point_z (float): End Point in Z-Coordinate
            node_reference (enum): Node Reference Enumeration
            parameters (list):
              if distance_from_start_relative:
                parameters = [True, %]
              if distance_from_start_absolute:
                parameters = [False, magnitude]
            offset_y (float): Offset in Y-Direction
            offset_z (float): Offset in Z-Direction
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Node Type
        clientObject.type = NodeType.TYPE_BETWEEN_TWO_POINTS.name

        # Coordinates start point
        clientObject.between_two_points_start_point_coordinate_1= start_point_x
        clientObject.between_two_points_start_point_coordinate_2= start_point_y
        clientObject.between_two_points_start_point_coordinate_3= start_point_z

        # Coordinates end point

        clientObject.between_two_points_end_point_coordinate_1= end_point_x
        clientObject.between_two_points_end_point_coordinate_2= end_point_y
        clientObject.between_two_points_end_point_coordinate_3= end_point_z

        # Length between i and j

        clientObject.reference_type = node_reference.name

        # Distance between node k and start point

        if parameters[0]:
            clientObject.distance_from_start_relative = parameters[1]
        else:
            clientObject.distance_from_start_absolute = parameters[1]

        # offset local coordinates
        clientObject.offset_in_local_direction_y= offset_y
        clientObject.offset_in_local_direction_z= offset_z

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Node to client model
        model.clientModel.service.set_node(clientObject)

    @staticmethod
    def OnLine(
                 no: int = 1,
                 line_number: int = 1,
                 node_reference = NodeReferenceType.REFERENCE_TYPE_L,
                 length_between_i_and_j: int = 1,
                 parameters = [True, 0.5],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Node Tag
            line_number (int): Line Tag
            node_reference (enum): Node Reference Enumeration
            length_between_i_and_j (float): Length between 2 Nodes
            parameters (list):
              if distance_from_start_relative:
                parameters = [True, %]
              if distance_from_start_absolute:
                parameters = [False, magnitude]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Reference Line
        clientObject.on_line_reference_line = line_number

        # Node Type
        clientObject.type = NodeType.TYPE_ON_LINE.name

        # Length between i and j

        clientObject.reference_type = node_reference.name

        clientObject.reference_object_projected_length = length_between_i_and_j

        # Distance between node k and start point

        if parameters[0]:
            clientObject.distance_from_start_relative = parameters[1]
        else:
            clientObject.distance_from_start_absolute = parameters[1]

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Node to client model
        model.clientModel.service.set_node(clientObject)

    @staticmethod
    def OnMember(
                 no: int = 1,
                 member_number: int = 1,
                 node_reference = NodeReferenceType.REFERENCE_TYPE_L,
                 length_between_i_and_j: int = 1,
                 parameters = [True, 0.5],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Node Tag
            member_number (int): Member Tag
            node_reference (enum): Node Reference Enumeration
            length_between_i_and_j (int): Length between 2 Nodes
            parameters (list):
              if distance_from_start_relative:
                parameters = [True, %]
              if distance_from_start_absolute:
                parameters = [False, magnitude]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Member Reference No.
        clientObject.on_member_reference_member = member_number

        # Node Type
        clientObject.type = NodeType.TYPE_ON_MEMBER.name

        # Length between i and j

        clientObject.reference_type = node_reference.name

        clientObject.reference_object_projected_length = length_between_i_and_j

        # Distance between node k and start point

        if parameters[0]:
            clientObject.distance_from_start_relative = parameters[1]
        else:
            clientObject.distance_from_start_absolute = parameters[1]

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Node to client model
        model.clientModel.service.set_node(clientObject)

    @staticmethod
    def DeleteNode(nodes_no: str = '1 2', model = Model):

        '''
        Args:
            nodes_no (str): Numbers of Nodes to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete from client model
        for node in ConvertStrToListOfInt(nodes_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_NODE.name, node)