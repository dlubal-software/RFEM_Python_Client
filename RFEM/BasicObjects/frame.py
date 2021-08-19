from RFEM.enums import MemberType
from RFEM.initModel import *

class Frame():
    def __init__(self,
                 no: int = 1,
                 start_node_no: int = 1,
                 end_node_no: int = 2,
                 rotation_angle: float = 0.0,
                 start_section_no: int = 1,
                 end_section_no: int = 1,
                 start_node_no: int = 2,
                 end_node_no: int = 3,
                 rotation_angle: float = 0.0,
                 start_section_no: int = 2,
                 end_section_no: int = 2,
                 start_node_no: int = 3,
                 end_node_no: int = 4,
                 rotation_angle: float = 0.0,
                 start_section_no: int = 3,
                 end_section_no: int = 3,
                 comment: str = '',
                 params: dict = {}):
 
 # Client model | Frame
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Member Rotation Angle beta
        clientObject.rotation_angle = rotation_angle

        # Start Section No.
        clientObject.section_start = start_section_no

        # End Section No.
        clientObject.section_end = end_section_no

        # Start Member Hinge No.
        clientObject.member_hinge_start = start_member_hinge_no

        # End Member Hinge No.
        clientObject.member_hinge_end = end_member_hinge_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member to client model
        clientModel.service.set_member(clientObject)
