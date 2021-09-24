from RFEM.enums import NodeType
from RFEM.enums import NodeCoordinateSystemType
from RFEM.enums import NodeReferenceType
from RFEM.initModel import *

class Node():
    def __init__(self,
                 no: int = 1,
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

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
        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def Standard(self,
                 no: int = 1,
                 coordinate_system = [], 
                 coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_CARTESIAN,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Node Type
        clientObject.type = NodeType.STANDARD.name
        
        # Coordinates

        clientObject.coordinate_system_type= coordinate_system_type.name


        if len(coordinate_system) != 3:
            raise Exception('WARNING: The coordinate system needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            
        if type(coordinate_system[0]) != int or type(coordinate_system[0]) != float :
            raise Exception ('WARNING: Coordinate system at index 0 to be of type "int" or ''float''')
        
        if type(coordinate_system[1]) != int or type(coordinate_system[1]) != float :
            raise Exception ('WARNING: Coordinate system at index 1 to be of type "int" or ''float''')

        if type(coordinate_system[2]) != int or type(coordinate_system[2]) != float :
            raise Exception ('WARNING: Coordinate system at index 2 to be of type "int" or ''float''')
    
        if coordinate_system_type.name == "COORDINATE_SYSTEM_CARTESIAN":
            clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_CARTESIAN
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1]
            clientObject.coordinate_3 = coordinate_system[2]
            

        elif coordinate_system_type.name == "COORDINATE_SYSTEM_X_CYLINDRICAL":   
            clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_X_CYLINDRICAL
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1]
            clientObject.coordinate_3 = coordinate_system[2] * (pi/180) 

        elif coordinate_system_type.name == "COORDINATE_SYSTEM_Y_CYLINDRICAL":
            clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_Y_CYLINDRICAL
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1]
            clientObject.coordinate_3 = coordinate_system[2] * (pi/180)
        
        elif coordinate_system_type.name == "COORDINATE_SYSTEM_Z_CYLINDRICAL":
            clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_Z_CYLINDRICAL
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1] * (pi/180)
            clientObject.coordinate_3 = coordinate_system[2]
            
        
        elif coordinate_system_type.name == "COORDINATE_SYSTEM_POLAR":
            clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_POLAR
            clientObject.coordinate_1 = coordinate_system[0]
            clientObject.coordinate_2 = coordinate_system[1] * (pi/180)
            clientObject.coordinate_3 = coordinate_system[2] * (pi/180)

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)
        

    def BetweenTwoNodes(self,
                 no: int = 1,
                 start_node_no: int = 1,
                 end_node_no: int = 2,
                 node_reference = NodeReferenceType.REFERENCE_TYPE_L,
                 length_between_i_and_j: int = 1,
                 parameters = [True, 50],
                 offset_x: int = 0,
                 offset_y: int = 0,
                 offset_z: int = 0,
                 comment: str = '',
                 params: dict = {}):

        '''
        if distance_from_start_relative:
            parameters = [True, %]
        
        if distance_from_start_absolute:
            parameters[False, magnitude]
        '''

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

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
         
        if parameters[0] == True:
            clientObject.distance_from_start_relative = parameters[1]
        
        elif parameters[0] == False:
         clientObject.distance_from_start_absolute = parameters[1]

        # Offset_local_y
        clientObject.offset_in_local_direction_y = offset_y

        # Offset_local_z
        clientObject.offset_in_local_direction_z = offset_z

        # Comment
        clientObject.comment = comment


        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)


    def BetweenTwoPoints(self,
                 no: int = 1,
                 start_point_x: float = 0.0,
                 start_point_y: float = 0.0,
                 start_point_z: float = 0.0,
                 end_point_x: float = 1.0,
                 end_point_y:float = 1.0,
                 end_point_z: float = 1.0,
                 node_reference = NodeReferenceType.REFERENCE_TYPE_L,
                 parameters = [True, 0.5],
                 offset_y: float = 0.0,
                 offset_z: float = 0.0, 
                 comment: str = '',
                 params: dict = {}):
        
        '''
       ############
       
       
       
        '''

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

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

        if parameters[0] == True:
            clientObject.distance_from_start_relative = parameters[1]
        elif parameters[0] == False:
         clientObject.distance_from_start_absolute = parameters[1]

        # offset local coordinates
        clientObject.offset_in_local_direction_y= offset_y
        clientObject.offset_in_local_direction_z= offset_z

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def OnLine(self,
                 no: int = 1,
                 line_number: int = 1,
                 node_reference = NodeReferenceType.REFERENCE_TYPE_L,
                 length_between_i_and_j: int = 1,
                 parameters = [True, 0.5],
                 comment: str = '',
                 params: dict = {}):
        
         
        '''
       [docstring]
       
        '''

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.on_line_reference_line = line_number

        # Node Type
        clientObject.type = NodeType.TYPE_ON_LINE.name

        # Length between i and j

        clientObject.reference_type = node_reference.name

        clientObject.reference_object_projected_length = length_between_i_and_j
       
       
        # Distance between node k and start point

        if parameters[0] == True:
            clientObject.distance_from_start_relative = parameters[1]
        elif parameters[0] == False:
         clientObject.distance_from_start_absolute = parameters[1] 

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def OnMember(self,
                 no: int = 1,
                 member_number: int = 1,
                 node_reference = NodeReferenceType.REFERENCE_TYPE_L,
                 length_between_i_and_j: int = 1,
                 parameters = [True, 0.5],
                 comment: str = '',
                 params: dict = {}):
        
               
        '''
       [docstring]
       
        '''


        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

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

        if parameters[0] == True:
            clientObject.distance_from_start_relative = parameters[1]
        elif parameters[0] == False:
         clientObject.distance_from_start_absolute = parameters[1]

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)
