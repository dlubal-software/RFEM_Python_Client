from RFEM.initModel import *
from RFEM.enums import BracingType

class Bracing():
 def __init__(self,
                 no: int = 1,
                 member_type = BracingType.TYPE_HORIZONTAL,
                 start_node_no: int = 1,
                 end_node_no: int = 2,
                 rotation_angle: float = 0.0,
                 start_section_no: int = 1,
                 end_section_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Bracing
        clientObject = clientModel.factory.create('ns0:bracing')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Bracing No.
        clientObject.no = no

        # Bracing Type
        clientObject.type = bracing_type.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Bracing Rotation Angle beta
        clientObject.rotation_angle = rotation_angle

        # Start Section No.
        clientObject.section_start = start_section_no

        # End Section No.
        clientObject.section_end = end_section_no

        # Start Bracing Hinge No.
        clientObject.bracing_hinge_start = start_bracing_hinge_no

        # End Bracing Hinge No.
        clientObject.bracing_hinge_end = end_bracing_hinge_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member to client model
        clientModel.service.set_bracing(clientObject)

      def Horizontal(self,
            no: int = 1,
            bracing_type = BracingType.TYPE_HORIZONTAL,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_angle: float = 0.0,
            start_section_no: int = 1,
            end_section_no: int = 1,
            start_bracing_hinge_no: int = 0,
            end_bracing_hinge_no: int = 0,
            comment: str = '',
            params: dict = {}):

        # Client model | Bracing
        clientObject = clientModel.factory.create('ns0:bracing')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Bracing No.
        clientObject.no = no

        # Bracing Type
        clientObject.type = bracing_type.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Bracing Rotation Angle beta
        clientObject.rotation_angle = rotation_angle

        # Start Section No.
        clientObject.section_start = start_section_no

        # End Section No.
        clientObject.section_end = end_section_no

        # Start Bracing Hinge No.
        clientObject.bracing_hinge_start = start_bracing_hinge_no

        # End Bracing Hinge No.
        clientObject.bracing_hinge_end = end_bracing_hinge_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Bracing to client model
        clientModel.service.set_bracing(clientObject)

        def Vertical(self,
            no: int = 1,
            bracing_type = BracingType.TYPE_VERTICAL,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_angle: float = 0.0,
            start_section_no: int = 1,
            end_section_no: int = 1,
            start_bracing_hinge_no: int = 0,
            end_bracing_hinge_no: int = 0,
            comment: str = '',
            params: dict = {}):

        # Client model | Bracing
        clientObject = clientModel.factory.create('ns0:bracing')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Bracing No.
        clientObject.no = no

        # Bracing Type
        clientObject.type = bracing_type.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Bracing Rotation Angle beta
        clientObject.rotation_angle = rotation_angle

        # Start Section No.
        clientObject.section_start = start_section_no

        # End Section No.
        clientObject.section_end = end_section_no

        # Start Bracing Hinge No.
        clientObject.bracing_hinge_start = start_bracing_hinge_no

        # End Bracing Hinge No.
        clientObject.bracing_hinge_end = end_bracing_hinge_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Bracing to client model
        clientModel.service.set_bracing(clientObject)

