from RFEM.initModel import *

class Frame():
    def __init__(self,
                 no: int = 1,
                 start_node_no: int = 1,
                 end_node_no: int = 2,
                 start_section_no: int = 1,
                 end_section_no: int = 1,
                 start_node_no: int = 2,
                 end_node_no: int = 3,
                 start_section_no: int = 2,
                 end_section_no: int = 2,
                 start_node_no: int = 3,
                 end_node_no: int = 4,
                 start_section_no: int = 3,
                 end_section_no: int = 3,
                 comment: str = '',
                 params: dict = {}):
 
 # Client model | Frame
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Frame No.
        clientObject.no = no

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Start Section No.
        clientObject.section_start = start_section_no

        # End Section No.
        clientObject.section_end = end_section_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member to client model
        clientModel.service.set_member(clientObject)
        
        # Nodes n
        i = 1
        while i <= n:
            j = (i-1) * 5
            Node(j+1, 0.0           , -(i-1) * d)
            Node(j+2, 0.0           , -(i-1) * d, -h)
            Node(j+3, l/2, -(i-1) * d, -h)
            Node(j+4, l  , -(i-1) * d, -h)
            Node(j+5, l  , -(i-1) * d)
            i += 1
            
            
         # Nodal supports n
        i = 1
        nodes_no = ""
        while i <= ns:
            j = (i-1) * 5
            nodes_no += str(j+1) + " "
            nodes_no += str(j+5) + " "
            NodalSupport(i, '???' , NodalSupportType.FIXED)
            i += 1
    
    
