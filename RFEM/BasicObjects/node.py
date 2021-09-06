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

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def OnLine(self,
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

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def OnMember(self,
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

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)
