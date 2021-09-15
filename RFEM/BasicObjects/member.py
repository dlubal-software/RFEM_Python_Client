from RFEM.enums import MemberType
from RFEM.initModel import *

class Member():
    def __init__(self,
                 no: int = 1,
                 member_type = MemberType.TYPE_BEAM,
                 start_node_no: int = 1,
                 end_node_no: int = 2,
                 rotation_angle: float = 0.0,
                 start_section_no: int = 1,
                 end_section_no: int = 1,
                 start_member_hinge_no: int = 0,
                 end_member_hinge_no: int = 0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member
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
    
    def Beam(self,
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_angle: float = 0.0,
            start_section_no: int = 1,
            end_section_no: int = 1,
            start_member_hinge_no: int = 0,
            end_member_hinge_no: int = 0,
            comment: str = '',
            params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_BEAM.name

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

    def Rigid(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_RIGID.name

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

    def Rib(self,
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_angle: float = 0.0,
            start_section_no: int = 1,
            end_section_no: int = 1,
            start_member_hinge_no: int = 0,
            end_member_hinge_no: int = 0,
            comment: str = '',
            params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_RIB.name

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

    def Truss(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_TRUSS.name

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

    def TrussOnlyN(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_TRUSS_ONLY_N.name

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

    def Tension(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_TENSION.name

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

    def Compression(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COMPRESSION.name

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

    def Buckling(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_BUCKLING.name

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

    def Cable(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_CABLE.name

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

    def ResultBeam(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_BEAM.name

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

    def DefinableStifness(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_DEFINABLE_STIFFNESS.name

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

    def CouplingRigid_Rigid(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COUPLING_RIGID_RIGID.name

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

    def CouplingRigid_Hinge(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COUPLING_RIGID_HINGE.name

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

    def CouplingHinge_Rigid(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COUPLING_HINGE_RIGID.name

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

    def CouplingHinge_Hinge(self,
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COUPLING_HINGE_HINGE.name

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
