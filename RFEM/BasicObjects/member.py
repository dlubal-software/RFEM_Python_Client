from RFEM.enums import MemberType, MemberRotationSpecificationType, MemberSectionDistributionType, MemberTypeRibAlignment, MemberResultBeamIntegration, ObjectTypes
from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertStrToListOfInt, ConvertToDlString

class Member():
    def __init__(self,
                 no: int = 1,
                 start_node_no: int = 1,
                 end_node_no: int = 2,
                 rotation_angle: float = 0.0,
                 start_section_no: int = 1,
                 end_section_no: int = 1,
                 start_member_hinge_no: int = 0,
                 end_member_hinge_no: int = 0,
                 line: int = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_angle (float): Member Rotation Angle
            start_section_no (int): Tag of Start Section
            end_section_no (int): Tag of End Section
            start_member_hinge_no (int): Tag of Start Member Hinge
            end_member_hinge_no (int): Tag of End Member Hinge
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_BEAM.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def Beam(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            section_distribution_type = MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM,
            rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
            rotation_parameters = [0],
            start_section_no: int = 1,
            end_section_no: int = 1,
            distribution_parameters: list = None,
            line = None,
            comment: str = '',
            params: dict = {'member_hinge_start':0, 'member_hinge_end': 0,
                            'member_eccentricity_start': 0, 'member_eccentricity_end': 0,
                            'support':0, 'member_nonlinearity': 0,
                            'end_modifications_member_start_extension': 0,
                            'end_modifications_member_start_slope_y': 0,
                            'end_modifications_member_start_slope_z': 0,
                            'end_modifications_member_end_extension': 0,
                            'end_modifications_member_end_slope_y': 0,
                            'end_modifications_member_end_slope_z': 0,
                            'member_result_intermediate_point' : 0,
                            'is_deactivated_for_calculation' : False},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            section_distribution_type (enum): Section Distribution Type Enumeration
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_LINEAR:
                    distribution_parameters = [section_alignment]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_BOTH_SIDES:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_end_is_defined_as_relative,
                                               section_distance_from_start_relative/absolute, section_distance_from_end_relative/absolute,
                                               section_alignment, section_internal]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_START_OF_MEMBER:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_END_OF_MEMBER:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_SADDLE:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment, section_internal]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_BOTH_SIDES:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_end_is_defined_as_relative,
                                               section_distance_from_start_relative/absolute, section_distance_from_end_relative/absolute,
                                               section_alignment, section_internal]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_START_OF_MEMBER:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_END_OF_MEMBER:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment]
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters; 1 or 2 params
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            start_section_no (int): Tag of Start Section
            end_section_no (int): End of End Section
            distribution_parameters (list): Distribution Parameters
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'member_hinge_start':, 'member_hinge_end': , 'member_eccentricity_start': ,
                          'member_eccentricity_end': 0, 'support':0, 'member_nonlinearity': 0,
                          'end_modifications_member_start_extension': , 'end_modifications_member_start_slope_y': ,
                          'end_modifications_member_start_slope_z': , 'end_modifications_member_end_extension': ,
                          'end_modifications_member_end_slope_y': , 'end_modifications_member_end_slope_z': ,
                          'member_result_intermediate_point' : , 'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_BEAM.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Section Distribution
        clientObject.section_distribution_type = section_distribution_type.name

        if section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_LINEAR:
            clientObject.section_alignment = distribution_parameters[0].name
        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_BOTH_SIDES:
            try:
                isinstance(distribution_parameters[0], bool)
                isinstance(distribution_parameters[1], bool)
            except:
                raise TypeError("WARNING: First two parameters should be type bool for SECTION_DISTRIBUTION_TYPE_TAPERED_AT_BOTH_SIDES. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_start_is_defined_as_relative = distribution_parameters[0]
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[1]
            if distribution_parameters[0]:
                clientObject.section_distance_from_start_relative = distribution_parameters[2]
            else:
                clientObject.section_distance_from_start_absolute = distribution_parameters[2]
            if distribution_parameters[1]:
                clientObject.section_distance_from_end_relative = distribution_parameters[3]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[3]
            clientObject.section_alignment = distribution_parameters[4].name
            clientObject.section_internal = distribution_parameters[5]

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_START_OF_MEMBER:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_TAPERED_AT_START_OF_MEMBER. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_start_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_start_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_start_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_END_OF_MEMBER:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_TAPERED_AT_END_OF_MEMBER. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_end_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_SADDLE:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_SADDLE. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_end_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name
            clientObject.section_internal = distribution_parameters[3]

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_BOTH_SIDES:
            try:
                isinstance(distribution_parameters[0], bool)
                isinstance(distribution_parameters[1], bool)
            except:
                raise TypeError("WARNING: First two parameters should be type bool for SECTION_DISTRIBUTION_TYPE_OFFSET_AT_BOTH_SIDES. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_start_is_defined_as_relative = distribution_parameters[0]
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[1]
            if distribution_parameters[0]:
                clientObject.section_distance_from_start_relative = distribution_parameters[2]
            else:
                clientObject.section_distance_from_start_absolute = distribution_parameters[2]
            if distribution_parameters[1]:
                clientObject.section_distance_from_end_relative = distribution_parameters[3]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[3]
            clientObject.section_alignment = distribution_parameters[4].name
            clientObject.section_internal = distribution_parameters[5]

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_START_OF_MEMBER:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_OFFSET_AT_START_OF_MEMBER. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_start_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_start_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_start_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_END_OF_MEMBER:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_OFFSET_AT_END_OF_MEMBER. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_end_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Start Section No.
        clientObject.section_start = start_section_no

        # End Section No.
        clientObject.section_end = end_section_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def Rigid(
                no: int = 1,
                start_node_no: int = 1,
                end_node_no: int = 2,
                rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
                rotation_parameters = [0],
                line = None,
                comment: str = '',
                params: dict = {'member_hinge_start':0, 'member_hinge_end': 0,
                                'member_eccentricity_start': 0, 'member_eccentricity_end': 0,
                                'support':0, 'member_nonlinearity': 0,
                                'member_result_intermediate_point' : 0,
                                'is_deactivated_for_calculation' : False},
                model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'member_hinge_start':, 'member_hinge_end': , 'member_eccentricity_start': ,
                          'member_eccentricity_end': , 'support':, 'member_nonlinearity': ,
                          'member_result_intermediate_point' : , 'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_RIGID.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    # Rib Member should be corrected.
    @staticmethod
    def Rib(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            section_distribution_type = MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM,
            start_section_no: int = 1,
            end_section_no: int = 1,
            rib_surfaces_no =  [],
            rib_alignment = MemberTypeRibAlignment.ALIGNMENT_ON_Z_SIDE_POSITIVE,
            line = None,
            comment: str = '',
            params: dict = {'member_hinge_start':0, 'member_hinge_end': 0,
                            'support':0,
                            'end_modifications_member_start_extension': 0,
                            'end_modifications_member_start_slope_y': 0,
                            'end_modifications_member_start_slope_z': 0,
                            'end_modifications_member_end_extension': 0,
                            'end_modifications_member_end_slope_y': 0,
                            'end_modifications_member_end_slope_z': 0,
                            'member_result_intermediate_point' : 0,
                            'is_deactivated_for_calculation' : False},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            section_distribution_type (enum): Section Distribution Type Enuemration
            start_section_no (int): Tag of Start Section
            end_section_no (int): Tag of End Section
            rib_surfaces_no (list): Surfaces Tags Assigned to Rib
            rib_alignment (enum): Rib Alignment Enumeration
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'member_hinge_start':, 'member_hinge_end': , 'support':,
                          'end_modifications_member_start_extension': , 'end_modifications_member_start_slope_y': ,
                          'end_modifications_member_start_slope_z': , 'end_modifications_member_end_extension': ,
                          'end_modifications_member_end_slope_y': , 'end_modifications_member_end_slope_z': ,
                          'member_result_intermediate_point' : , 'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited

        for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_LINEAR:
            distribution_parameters[section_alignment] BJÖRN: Where is this parameter used?
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_RIB.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Section Distribution
        clientObject.section_distribution_type = section_distribution_type.name
        if section_distribution_type.name == "SECTION_DISTRIBUTION_TYPE_UNIFORM" or section_distribution_type.name == "SECTION_DISTRIBUTION_TYPE_LINEAR":
            pass
        else:
            raise TypeError("WARNING: Only Uniform and Linear section distributions are available for Rib member. Kindly check inputs and correctness.")

        # Start Section No.
        clientObject.section_start = start_section_no

        # End Section No.
        clientObject.section_end = end_section_no

        # Rib Surfaces
        clientObject.member_rib_first_surface = rib_surfaces_no[0]
        clientObject.member_rib_second_surface = rib_surfaces_no[1]

        # Rib Alignment
        clientObject.member_type_rib_alignment = rib_alignment.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def Truss(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
            rotation_parameters = [0],
            section_no: int = 1,
            line = None,
            comment: str = '',
            params: dict = {'member_eccentricity_start': 0, 'member_eccentricity_end': 0,
                            'member_nonlinearity': 0,
                            'end_modifications_member_start_extension': 0,
                            'end_modifications_member_start_slope_y': 0,
                            'end_modifications_member_start_slope_z': 0,
                            'end_modifications_member_end_extension': 0,
                            'end_modifications_member_end_slope_y': 0,
                            'end_modifications_member_end_slope_z': 0,
                            'is_deactivated_for_calculation' : False},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            section_no (int): Section Tag
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'member_eccentricity_start': , 'member_eccentricity_end': , 'member_nonlinearity': ,
                          'end_modifications_member_start_extension': , 'end_modifications_member_start_slope_y': ,
                          'end_modifications_member_start_slope_z': , 'end_modifications_member_end_extension': ,
                          'end_modifications_member_end_slope_y': , 'end_modifications_member_end_slope_z': ,
                          'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_TRUSS.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Start Section No.
        clientObject.section_start = section_no

        # End Section No.
        clientObject.section_end = section_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def TrussOnlyN(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
            rotation_parameters = [0],
            section_no: int = 1,
            line = None,
            comment: str = '',
            params: dict = {'member_eccentricity_start': 0, 'member_eccentricity_end': 0,
                            'member_nonlinearity': 0,
                            'end_modifications_member_start_extension': 0,
                            'end_modifications_member_start_slope_y': 0,
                            'end_modifications_member_start_slope_z': 0,
                            'end_modifications_member_end_extension': 0,
                            'end_modifications_member_end_slope_y': 0,
                            'end_modifications_member_end_slope_z': 0,
                            'is_deactivated_for_calculation' : False},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            section_no (int): Section Tag
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'member_eccentricity_start': , 'member_eccentricity_end': , 'member_nonlinearity': ,
                          'end_modifications_member_start_extension': , 'end_modifications_member_start_slope_y': ,
                          'end_modifications_member_start_slope_z': , 'end_modifications_member_end_extension': ,
                          'end_modifications_member_end_slope_y': , 'end_modifications_member_end_slope_z': ,
                          'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_TRUSS_ONLY_N.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Start Section No.
        clientObject.section_start = section_no

        # End Section No.
        clientObject.section_end = section_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def Tension(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
            rotation_parameters = [0],
            section_no: int = 1,
            line = None,
            comment: str = '',
            params: dict = {'member_eccentricity_start': 0, 'member_eccentricity_end': 0,
                            'member_nonlinearity': 0,
                            'end_modifications_member_start_extension': 0,
                            'end_modifications_member_start_slope_y': 0,
                            'end_modifications_member_start_slope_z': 0,
                            'end_modifications_member_end_extension': 0,
                            'end_modifications_member_end_slope_y': 0,
                            'end_modifications_member_end_slope_z': 0,
                            'is_deactivated_for_calculation' : False},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            section_no (int): Section Tag
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'member_eccentricity_start': , 'member_eccentricity_end': , 'member_nonlinearity': ,
                          'end_modifications_member_start_extension': , 'end_modifications_member_start_slope_y': ,
                          'end_modifications_member_start_slope_z': , 'end_modifications_member_end_extension': ,
                          'end_modifications_member_end_slope_y': , 'end_modifications_member_end_slope_z': ,
                          'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_TENSION.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Start Section No.
        clientObject.section_start = section_no

        # End Section No.
        clientObject.section_end = section_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def Compression(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
            rotation_parameters = [0],
            section_no: int = 1,
            line = None,
            comment: str = '',
            params: dict = {'member_eccentricity_start': 0, 'member_eccentricity_end': 0,
                            'member_nonlinearity': 0,
                            'end_modifications_member_start_extension': 0,
                            'end_modifications_member_start_slope_y': 0,
                            'end_modifications_member_start_slope_z': 0,
                            'end_modifications_member_end_extension': 0,
                            'end_modifications_member_end_slope_y': 0,
                            'end_modifications_member_end_slope_z': 0,
                            'is_deactivated_for_calculation' : False},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            section_no (int): Section Tag
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'member_eccentricity_start': , 'member_eccentricity_end': , 'member_nonlinearity': ,
                          'end_modifications_member_start_extension': , 'end_modifications_member_start_slope_y': ,
                          'end_modifications_member_start_slope_z': , 'end_modifications_member_end_extension': ,
                          'end_modifications_member_end_slope_y': , 'end_modifications_member_end_slope_z': ,
                          'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COMPRESSION.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Start Section No.
        clientObject.section_start = section_no

        # End Section No.
        clientObject.section_end = section_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def Buckling(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
            rotation_parameters = [0],
            section_no: int = 1,
            line = None,
            comment: str = '',
            params: dict = {'member_eccentricity_start': 0, 'member_eccentricity_end': 0,
                            'member_nonlinearity': 0,
                            'end_modifications_member_start_extension': 0,
                            'end_modifications_member_start_slope_y': 0,
                            'end_modifications_member_start_slope_z': 0,
                            'end_modifications_member_end_extension': 0,
                            'end_modifications_member_end_slope_y': 0,
                            'end_modifications_member_end_slope_z': 0,
                            'is_deactivated_for_calculation' : False},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            section_no (int): Section Tag
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'member_eccentricity_start': , 'member_eccentricity_end': , 'member_nonlinearity': ,
                          'end_modifications_member_start_extension': , 'end_modifications_member_start_slope_y': ,
                          'end_modifications_member_start_slope_z': , 'end_modifications_member_end_extension': ,
                          'end_modifications_member_end_slope_y': , 'end_modifications_member_end_slope_z': ,
                          'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_BUCKLING.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Start Section No.
        clientObject.section_start = section_no

        # End Section No.
        clientObject.section_end = section_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def Cable(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
            rotation_parameters = [0],
            section_no: int = 1,
            line = None,
            comment: str = '',
            params: dict = {'end_modifications_member_start_extension': 0,
                            'end_modifications_member_start_slope_y': 0,
                            'end_modifications_member_start_slope_z': 0,
                            'end_modifications_member_end_extension': 0,
                            'end_modifications_member_end_slope_y': 0,
                            'end_modifications_member_end_slope_z': 0,
                            'is_deactivated_for_calculation' : False},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            section_no (int): Section Tag
            line (int, optional): Assigned Line
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'end_modifications_member_start_extension': , 'end_modifications_member_start_slope_y': ,
                          'end_modifications_member_start_slope_z': , 'end_modifications_member_end_extension': ,
                          'end_modifications_member_end_slope_y': , 'end_modifications_member_end_slope_z': ,
                          'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_CABLE.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Start Section No.
        clientObject.section_start = section_no

        # End Section No.
        clientObject.section_end = section_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def ResultBeam(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            section_distribution_type = MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM,
            rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
            result_beam_integrate_stresses_and_forces = MemberResultBeamIntegration.INTEGRATE_WITHIN_CUBOID_QUADRATIC,
            rotation_parameters = [0],
            start_section_no: int = 1,
            end_section_no: int = 1,
            distribution_parameters: list = None,
            integration_parameters: list = None,
            include_objects: list = [True, True, True],
            exclude_objects: list = [None, None, None],
            comment: str = '',
            params: dict = { 'end_modifications_member_start_extension': 0,
                            'end_modifications_member_start_slope_y': 0,
                            'end_modifications_member_start_slope_z': 0,
                            'end_modifications_member_end_extension': 0,
                            'end_modifications_member_end_slope_y': 0,
                            'end_modifications_member_end_slope_z': 0,
                            'member_result_intermediate_point' : 0},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int,): Tag of End Node
            section_distribution_type (enum): Section Distribution Type Enumeration
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            result_beam_integrate_stresses_and_forces (enum): Member Result Beam Integration Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            start_section_no (int): Tag of Start Section
            end_section_no (int): Tag of End Section
            distribution_parameters (list): Distribution Parameters
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_LINEAR:
                    distribution_parameters = [section_alignment]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_BOTH_SIDES:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_end_is_defined_as_relative,
                                               section_distance_from_start_relative/absolute, section_distance_from_end_relative/absolute,
                                               section_alignment, section_internal]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_START_OF_MEMBER:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_END_OF_MEMBER:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_SADDLE:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment, section_internal]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_BOTH_SIDES:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_end_is_defined_as_relative,
                                               section_distance_from_start_relative/absolute, section_distance_from_end_relative/absolute,
                                               section_alignment, section_internal]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_START_OF_MEMBER:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment]
                for section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_END_OF_MEMBER:
                    distribution_parameters = [section_distance_from_start_is_defined_as_relative, section_distance_from_start_relative/absolute, section_alignment]
            integration_parameters (list): Integration Parameters
                for result_beam_integrate_stresses_and_forces.name == "INTEGRATE_WITHIN_CUBOID_QUADRATIC":
                    integration_parameters = [result_beam_y_z]
                for result_beam_integrate_stresses_and_forces.name == "INTEGRATE_WITHIN_CUBOID_GENERAL":
                    integration_parameters = [result_beam_y_plus, result_beam_z_plus, result_beam_y_minus, result_beam_z_minus]
                for result_beam_integrate_stresses_and_forces.name == "INTEGRATE_WITHIN_CYLINDER":
                    integration_parameters = [result_beam_radius]
            include_objects (list): Include Objects List
                include_objects[0] (bool/str)= Assign Include Surfaces (e.g '1 2 3') (Note: 'True' for all surfaces else string input)
                include_objects[1] (bool/str)= Assign Include Solids (e.g '1 2 3') (Note: 'True' for all solids else string input)
                include_objects[2] (bool/str)= Assign Include Members (e.g '1 2 3') (Note: 'True' for all members else string input)
            exclude_objects (list): Exclude Objects List
                exclude_objects[0] (str)= Assign Exclude Surfaces (e.g '1 2 3')
                exclude_objects[1] (str)= Assign Exclude Solids (e.g '1 2 3')
                exclude_objects[2] (str)= Assign Exclude Members (e.g '1 2 3')
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'end_modifications_member_start_extension': , 'end_modifications_member_start_slope_y': ,
                          'end_modifications_member_start_slope_z': , 'end_modifications_member_end_extension': ,
                          'end_modifications_member_end_slope_y': , 'end_modifications_member_end_slope_z': ,
                          'member_result_intermediate_point' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_RESULT_BEAM.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Section Distribution
        clientObject.section_distribution_type = section_distribution_type.name

        # Result Beam Integration
        clientObject.result_beam_integrate_stresses_and_forces = result_beam_integrate_stresses_and_forces.name
        if result_beam_integrate_stresses_and_forces.name == "INTEGRATE_WITHIN_CUBOID_QUADRATIC":
            clientObject.result_beam_y_z = integration_parameters[0]
        elif result_beam_integrate_stresses_and_forces.name == "INTEGRATE_WITHIN_CUBOID_GENERAL":
            clientObject.result_beam_y_plus = integration_parameters[0]
            clientObject.result_beam_z_plus = integration_parameters[1]
            clientObject.result_beam_y_minus = integration_parameters[2]
            clientObject.result_beam_z_minus = integration_parameters[3]
        elif result_beam_integrate_stresses_and_forces.name == "INTEGRATE_WITHIN_CYLINDER":
            clientObject.result_beam_radius = integration_parameters[0]

        # Include Exclude Objects
        if include_objects[0] == True:
            clientObject.result_beam_include_all_surfaces = True
        elif isinstance(include_objects[0], str):
            clientObject.result_beam_include_all_surfaces = False
            clientObject.result_beam_include_surfaces = ConvertToDlString(include_objects[0])

        if include_objects[1] == True:
            clientObject.result_beam_include_all_solids = True
        elif isinstance(include_objects[1], str):
            clientObject.result_beam_include_all_solids = False
            clientObject.result_beam_include_solids = ConvertToDlString(include_objects[1])

        if include_objects[2] == True:
            clientObject.result_beam_include_all_members = True
        elif isinstance(include_objects[2], str):
            clientObject.result_beam_include_all_members = False
            clientObject.result_beam_include_members = ConvertToDlString(include_objects[2])

        if isinstance(exclude_objects[0], str):
            clientObject.result_beam_exclude_surfaces = ConvertToDlString(exclude_objects[0])
        if isinstance(exclude_objects[1], str):
            clientObject.result_beam_exclude_solids = ConvertToDlString(exclude_objects[1])
        if isinstance(exclude_objects[2], str):
            clientObject.result_beam_exclude_members = ConvertToDlString(exclude_objects[2])

        # Section Distribution
        if section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_LINEAR:
            clientObject.section_alignment = distribution_parameters[0].name
        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_BOTH_SIDES:
            try:
                isinstance(distribution_parameters[0], bool)
                isinstance(distribution_parameters[1], bool)
            except:
                raise TypeError("WARNING: First two parameters should be type bool for SECTION_DISTRIBUTION_TYPE_TAPERED_AT_BOTH_SIDES. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_start_is_defined_as_relative = distribution_parameters[0]
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[1]
            if distribution_parameters[0]:
                clientObject.section_distance_from_start_relative = distribution_parameters[2]
            else:
                clientObject.section_distance_from_start_absolute = distribution_parameters[2]
            if distribution_parameters[1]:
                clientObject.section_distance_from_end_relative = distribution_parameters[3]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[3]
            clientObject.section_alignment = distribution_parameters[4].name
            clientObject.section_internal = distribution_parameters[5]

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_START_OF_MEMBER:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_TAPERED_AT_START_OF_MEMBER. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_start_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_start_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_start_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_TAPERED_AT_END_OF_MEMBER:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_TAPERED_AT_END_OF_MEMBER. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_end_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_SADDLE:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_SADDLE. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_end_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name
            clientObject.section_internal = distribution_parameters[3]

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_BOTH_SIDES:
            try:
                isinstance(distribution_parameters[0], bool)
                isinstance(distribution_parameters[1], bool)
            except:
                raise TypeError("WARNING: First two parameters should be type bool for SECTION_DISTRIBUTION_TYPE_OFFSET_AT_BOTH_SIDES. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_start_is_defined_as_relative = distribution_parameters[0]
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[1]
            if distribution_parameters[0]:
                clientObject.section_distance_from_start_relative = distribution_parameters[2]
            else:
                clientObject.section_distance_from_start_absolute = distribution_parameters[2]
            if distribution_parameters[1]:
                clientObject.section_distance_from_end_relative = distribution_parameters[3]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[3]
            clientObject.section_alignment = distribution_parameters[4].name
            clientObject.section_internal = distribution_parameters[5]

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_START_OF_MEMBER:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_OFFSET_AT_START_OF_MEMBER. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_start_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_start_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_start_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name

        elif section_distribution_type == MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_OFFSET_AT_END_OF_MEMBER:
            try:
                isinstance(distribution_parameters[0], bool)
            except:
                raise TypeError("WARNING: First parameter should be type bool for SECTION_DISTRIBUTION_TYPE_OFFSET_AT_END_OF_MEMBER. Kindly check list inputs completeness and correctness.")
            clientObject.section_distance_from_end_is_defined_as_relative = distribution_parameters[0]
            if distribution_parameters[0]:
                clientObject.section_distance_from_end_relative = distribution_parameters[1]
            else:
                clientObject.section_distance_from_end_absolute = distribution_parameters[1]
            clientObject.section_alignment = distribution_parameters[2].name

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Start Section No.
        clientObject.section_start = start_section_no

        # End Section No.
        clientObject.section_end = end_section_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def DefinableStiffness(
            no: int = 1,
            start_node_no: int = 1,
            end_node_no: int = 2,
            rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
            rotation_parameters = [0],
            definable_stiffness : int = 1,
            comment: str = '',
            params: dict = {'member_hinge_start':0, 'member_hinge_end': 0,
                            'member_eccentricity_start': 0, 'member_eccentricity_end': 0,
                            'member_nonlinearity': 0,
                            'member_result_intermediate_point' : 0,
                            'is_deactivated_for_calculation' : False},
            model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            definable_stiffness (int): Definable Stiffness Tag
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'member_hinge_start':, 'member_hinge_end': , 'member_eccentricity_start': ,
                          'member_eccentricity_end': , 'member_nonlinearity': ,
                          'member_result_intermediate_point' : , 'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_DEFINABLE_STIFFNESS.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Section Distribution
        clientObject.section_distribution_type = "SECTION_DISTRIBUTION_TYPE_UNIFORM"

        # Member Type Definable Stiffness
        clientObject.member_type_definable_stiffness = definable_stiffness

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def CouplingRigidRigid(
                        no: int = 1,
                        start_node_no: int = 1,
                        end_node_no: int = 2,
                        rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
                        rotation_parameters = [0],
                        comment: str = '',
                        params: dict = {'is_deactivated_for_calculation' : False},
                        model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COUPLING_RIGID_RIGID.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def CouplingRigidHinge(
                        no: int = 1,
                        start_node_no: int = 1,
                        end_node_no: int = 2,
                        rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
                        rotation_parameters = [0],
                        comment: str = '',
                        params: dict = {'is_deactivated_for_calculation' : False},
                        model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COUPLING_RIGID_HINGE.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def CouplingHingeRigid(
                        no: int = 1,
                        start_node_no: int = 1,
                        end_node_no: int = 2,
                        rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
                        rotation_parameters = [0],
                        comment: str = '',
                        params: dict = {'is_deactivated_for_calculation' : False},
                        model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COUPLING_HINGE_RIGID.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def CouplingHingeHinge(
                        no: int = 1,
                        start_node_no: int = 1,
                        end_node_no: int = 2,
                        rotation_specification_type = MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE,
                        rotation_parameters = [0],
                        comment: str = '',
                        params: dict = {'is_deactivated_for_calculation' : False},
                        model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            rotation_specification_type (enum): Rotation Specification Type Enumeration
            rotation_parameters (list): Rotation Parameters
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
                    rotation_parameters = [rotation_angle]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
                    rotation_parameters = [rotation_help_node, rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
                    rotation_parameters = [rotation_plane_type]
                for rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
                    rotation_parameters = [rotation_surface, rotation_surface_plane_type]
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                params = {'is_deactivated_for_calculation' : }
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_COUPLING_HINGE_HINGE.name

        # Start Node No.
        clientObject.node_start = start_node_no

        # End Node No.
        clientObject.node_end = end_node_no

        # Member Rotation
        clientObject.rotation_specification_type = rotation_specification_type.name
        if rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE:
            clientObject.rotation_angle = rotation_parameters[0]
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_HELP_NODE:
            clientObject.rotation_help_node = rotation_parameters[0]
            clientObject.rotation_plane_type = rotation_parameters[1].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_INSIDE_NODE:
            clientObject.rotation_plane_type = rotation_parameters[0].name
        elif rotation_specification_type == MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_SURFACE:
            clientObject.rotation_surface = rotation_parameters[0]
            clientObject.rotation_surface_plane_type = rotation_parameters[1].name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def Spring(no: int = 1,
               start_node_no: int = 1,
               end_node_no: int = 2,
               line: int = None,
               spring_type: int = None,
               comment: str = '',
               params: dict = None,
               model = Model):
        """
        Args:
            no (int): Member Tag
            start_node_no (int): Tag of Start Node
            end_node_no (int): Tag of End Node
            line (int, optional): Assigned Line
            spring_type (int, optional): Assign Member Spring Type
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member
        clientObject = model.clientModel.factory.create('ns0:member')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member No.
        clientObject.no = no

        # Member Type
        clientObject.type = MemberType.TYPE_SPRING.name

        # Assigned Line number or Node numbers
        if line is None:
            clientObject.node_start = start_node_no
            clientObject.node_end = end_node_no
        else:
            clientObject.line = line

        # Spring Type
        clientObject.member_type_spring = spring_type

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member to client model
        model.clientModel.service.set_member(clientObject)

    @staticmethod
    def DeleteMember(members_no: str = '1 2', model = Model):

        '''
        Args:
            members_no (str): Numbers of Members to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete from client model
        for member in ConvertStrToListOfInt(members_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_MEMBER.name, member)

    @staticmethod
    def GetMember(object_index: int = 1, model = Model):

        '''
        Args:
            obejct_index (int): Member Index
            model (RFEM Class, optional): Model to be edited
        '''

        # Get Member from client model
        return model.clientModel.service.get_member(object_index)
