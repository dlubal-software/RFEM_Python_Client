from RFEM.enums import MemberType
from RFEM.initModel import *

class MemberByLine():
    def __init__(self,
                 no: int = 1,
                 member_type = MemberType.TYPE_BEAM,
                 line_no: int = 1,
                 rotation_angle: float = 0.0,
                 start_section_no: int = 1,
                 end_section_no: int = 1,
                 start_member_hinge_no: int = 0,
                 end_member_hinge_no: int = 0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name
        
        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)
            

    def Beam(self,
            no: int = 1,
            member_type = MemberType.TYPE_BEAM,
            line_no: int = 1,
            rotation_angle: float = 0.0,
            start_section_no: int = 1,
            end_section_no: int = 1,
            start_member_hinge_no: int = 0,
            end_member_hinge_no: int = 0,
            comment: str = '',
            params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def Rigid(self,
                no: int = 1,
                member_type = MemberType.TYPE_RIGID,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def Rib(self,
            no: int = 1,
            member_type = MemberType.TYPE_RIB,
            line_no: int = 1,
            rotation_angle: float = 0.0,
            start_section_no: int = 1,
            end_section_no: int = 1,
            start_member_hinge_no: int = 0,
            end_member_hinge_no: int = 0,
            comment: str = '',
            params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def Truss(self,
                no: int = 1,
                member_type = MemberType.TYPE_TRUSS,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def TrussOnlyN(self,
                no: int = 1,
                member_type = MemberType.TYPE_TRUSS_ONLY_N,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def Tension(self,
                no: int = 1,
                member_type = MemberType.TYPE_TENSION,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def Compression(self,
                no: int = 1,
                member_type = MemberType.TYPE_COMPRESSION,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def Buckling(self,
                no: int = 1,
                member_type = MemberType.TYPE_BUCKLING,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def Cable(self,
                no: int = 1,
                member_type = MemberType.TYPE_CABLE,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def ResultBeam(self,
                no: int = 1,
                member_type = MemberType.TYPE_BEAM,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def DefinableStifness(self,
                no: int = 1,
                member_type = MemberType.TYPE_DEFINABLE_STIFFNESS,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def CouplingRigid_Rigid(self,
                no: int = 1,
                member_type = MemberType.TYPE_COUPLING_RIGID_RIGID,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def CouplingRigid_Hinge(self,
                no: int = 1,
                member_type = MemberType.TYPE_COUPLING_RIGID_HINGE,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def CouplingHinge_Rigid(self,
                no: int = 1,
                member_type = MemberType.TYPE_COUPLING_HINGE_RIGID,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)

    def CouplingHinge_Hinge(self,
                no: int = 1,
                member_type = MemberType.TYPE_COUPLING_HINGE_HINGE,
                line_no: int = 1,
                rotation_angle: float = 0.0,
                start_section_no: int = 1,
                end_section_no: int = 1,
                start_member_hinge_no: int = 0,
                end_member_hinge_no: int = 0,
                comment: str = '',
                params: dict = {}):

        # Client model | Member
        clientObject = Model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = member_type.name

        # Line No.
        clientObject.line = line_no

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
        Model.clientModel.service.set_member(clientObject)
