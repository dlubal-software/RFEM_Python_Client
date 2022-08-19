from http import client
from RFEM.initModel import Model, clearAtributes
from RFEM.enums import *

class MemberEccentricity():
    def __init__(self,
                 no: int = 1,
                 name: list = [False],
                 eccentricity_type = MemberEccentricitySpecificationType.TYPE_RELATIVE,
                 eccentricity_parameters: list = [MemberEccentricityHorizontalSectionAlignment.ALIGN_MIDDLE, MemberEccentricityVerticalSectionAlignment.ALIGN_MIDDLE],
                 transverse_offset_type = MemberEccentricityTransverseOffsetType.TRANSVERSE_OFFSET_TYPE_NONE,
                 transverse_offset_parameters: list = None,
                 axial_offset_active: bool = False,
                 hinge_location_at_node: bool = False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Eccentricity Tag
            name (list): User Defined Name
            eccentricity_type (enum): Member Eccentricity Specification Type Enumeration
            eccentricity_parameters (list): Eccentricity Parameters List
                for eccentricity_type == MemberEccentricitySpecificationType.TYPE_RELATIVE:
                    eccentricity_parameters = [horizontal_section_alignment, vertical_section_alignment]
                for eccentricity_type == MemberEccentricitySpecificationType.TYPE_ABSOLUTE:
                    eccentricity_parameters = [coordinate_system, offset_x, offset_y, offset_z]
                for eccentricity_type == MemberEccentricitySpecificationType.TYPE_RELATIVE_AND_ABSOLUTE:
                    eccentricity_parameters = [coordinate_system, offset_x, offset_y, offset_z, horizontal_section_alignment, vertical_section_alignment]
            transverse_offset_type (enum): Member Eccentricity Transverse Offset Type Enumeration
            transverse_offset_parameters (list): Transverse Offset Parameters List
                for transverse_offset_type == MemberEccentricityTransverseOffsetType.TRANSVERSE_OFFSET_TYPE_NONE:
                    transverse_offset_parameters = None
                for transverse_offset_type == MemberEccentricityTransverseOffsetType.TRANSVERSE_OFFSET_TYPE_FROM_SURFACE_THICKNESS:
                    transverse_offset_parameters = [transverse_offset_reference_surface, transverse_offset_vertical_alignment]
                for transverse_offset_type == MemberEccentricityTransverseOffsetType.TRANSVERSE_OFFSET_TYPE_FROM_MEMBER_SECTION:
                    transverse_offset_parameters = [transverse_offset_reference_member, transverse_offset_member_reference_node, transverse_offset_horizontal_alignment, transverse_offset_vertical_alignment]
            axial_offset_active (bool): Enable/Disable Axial Offset
            hinge_location_at_node (bool): Enable/Disable Hinge Location at Node
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member Eccentricity
        clientObject = model.clientModel.factory.create('ns0:member_eccentricity')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Eccentricity No.
        clientObject.no = no

        # User Defined Name
        if name[0]:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name[1]
        else:
            clientObject.user_defined_name_enabled = False


        # Eccentricity Specification Type
        clientObject.specification_type = eccentricity_type.name

        if eccentricity_type.name == "TYPE_RELATIVE":
            clientObject.horizontal_section_alignment = eccentricity_parameters[0].name
            clientObject.vertical_section_alignment = eccentricity_parameters[1].name

        elif eccentricity_type.name == "TYPE_ABSOLUTE":
            clientObject.coordinate_system = eccentricity_parameters[0]
            clientObject.offset_x = eccentricity_parameters[1]
            clientObject.offset_y = eccentricity_parameters[2]
            clientObject.offset_z = eccentricity_parameters[3]

        elif eccentricity_parameters.name == "TYPE_RELATIVE_AND_ABSOLUTE":
            clientObject.coordinate_system = eccentricity_parameters[0]
            clientObject.offset_x = eccentricity_parameters[1]
            clientObject.offset_y = eccentricity_parameters[2]
            clientObject.offset_z = eccentricity_parameters[3]
            clientObject.horizontal_section_alignment = eccentricity_parameters[4].name
            clientObject.vertical_section_alignment = eccentricity_parameters[5].name

        else:
            print("WARNING: Invalid eccentricity type.")

        # Transverse Offset Reference Type
        clientObject.transverse_offset_reference_type = transverse_offset_type.name

        if transverse_offset_type.name == "TRANSVERSE_OFFSET_TYPE_NONE":
            pass

        elif transverse_offset_type.name == "TRANSVERSE_OFFSET_TYPE_FROM_SURFACE_THICKNESS":
            clientObject.transverse_offset_reference_surface = transverse_offset_parameters[0]
            clientObject.transverse_offset_vertical_alignment = transverse_offset_parameters[1].name

        elif transverse_offset_type.name == "TRANSVERSE_OFFSET_TYPE_FROM_MEMBER_SECTION":
            clientObject.transverse_offset_reference_member = transverse_offset_parameters[0]
            clientObject.transverse_offset_member_reference_node = transverse_offset_parameters[1]
            clientObject.transverse_offset_horizontal_alignment = transverse_offset_parameters[2].name
            clientObject.transverse_offset_vertical_alignment = transverse_offset_parameters[3].name
        else:
            print("WARNING: Invalid transverse offset type.")

        # Axial Offset Option
        clientObject.axial_offset_active = axial_offset_active

        # Hinge Location at Node Option
        clientObject.hinge_location_at_node = hinge_location_at_node

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Member Eccentricity to client model
        model.clientModel.service.set_member_eccentricity(clientObject)
