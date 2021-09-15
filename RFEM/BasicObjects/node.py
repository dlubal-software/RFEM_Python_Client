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
                 coordinate_system = [True, coordinate_X, coordinate_Y, coordinate_Z],
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
        
         # Node Type
        clientObject.type = NodeType.STANDARD.name
        
        # Coordinates
        clientObject.coordinate_1 = coordinate_X
        clientObject.coordinate_2 = coordinate_Y
        clientObject.coordinate_3 = coordinate_Z
            
        if parameters[0] == True:
            clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_CARTESIAN
            clientObject.coordinate_1 = parameters[1]
            clientObject.coordinate_2 = parameters[2]
            clientObject.coordinate_3 = parameters[3]
            
         if parameters[0] == False:           
            CoordinateSystemType = input('Please enter ''P'' for Polar Coordinate System OR ''X'' for X-Cylindrical Coordinate System OR ''Y'' for Y-Cylindrical Coordinate System OR ''Z'' for Z-Cylindrical Coordinate System')
            if CoordinateSystemType.lower() == 'X' or CoordinateSystemType.lower() == 'x':
                parameters[0] == 'X-Cylindrical'  #is that correct?
                clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_X_CYLINDRICAL
                #clientObject.coordinate_1 = parameters[1]
                #clientObject.coordinate_2 = parameters[2]
                #clientObject.coordinate_3 = parameters[3]
                
                elif CoordinateSystemType.lower() == 'Y' or CoordinateSystemType.lower() == 'y': 
                    parameters[0] == 'Y-Cylindrical'  #is that correct?
                    clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_Y_CYLINDRICAL
                    #clientObject.coordinate_1 = parameters[1]
                    #clientObject.coordinate_2 = parameters[2]
                    #clientObject.coordinate_3 = parameters[3]
                    
               elif CoordinateSystemType.lower() == 'Z' or CoordinateSystemType.lower() == 'z': 
                    parameters[0] == 'Z-Cylindrical'   #is that correct?
                    clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_Z_CYLINDRICAL
                    #clientObject.coordinate_1 = parameters[1]
                    #clientObject.coordinate_2 = parameters[2]
                    #clientObject.coordinate_3 = parameters[3]
            
               elif CoordinateSystemType.lower() == 'Y' or CoordinateSystemType.lower() == 'y': 
                    parameters[0] == 'Polar'   #is that correct?
                    clientObject.coordinate_system_type = NodeCoordinateSystemType.COORDINATE_SYSTEM_POLAR
                    #clientObject.coordinate_1 = parameters[1]
                    #clientObject.coordinate_2 = parameters[2]
                    #clientObject.coordinate_3 = parameters[3]

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def BetweenTwoNodes(self,
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
