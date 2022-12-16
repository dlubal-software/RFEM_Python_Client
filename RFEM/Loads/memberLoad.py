from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import LoadDirectionType, MemberLoadType, MemberLoadDistribution, MemberLoadDirection, MemberLoadDirectionOrientation
from RFEM.enums import MemberLoadEccentricityHorizontalAlignment, MemberLoadEccentricityVerticalAlignment, MemberLoadEccentricitySectionMiddle
from RFEM.enums import MemberLoadAxisDefinitionType, MemberLoadAxisDefinitionAxisOrientation, MemberLoadAxisDefinition

class MemberLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_direction = LoadDirectionType.LOAD_DIRECTION_LOCAL_Z,
                 magnitude: float = 2000,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Members
            load_direction (enum): Load Directin Enumeration
            magnitude (float): Load Magnitude
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        clientObject.magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def Force(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_distribution= MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction= MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter: list = None,
                 force_eccentricity: bool= False,
                 list_reference: bool= False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_distribution (enum): Member Load Distribution Enumeration
            load_direction (enum): Member Load Direction Enumeration
            load_parameter (list/list of lists): Load Parameter List
                for load_distribution == LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [magnitude]
                for load_distribution == LOAD_DISTRIBUTION_UNIFORM_TOTAL:
                    load_parameter = [magnitude]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_1:
                    load_parameter = [relative_distance = False, magnitude, distance_a]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_N:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude, count_n, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_2x2:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, relative_distance_c = False, magnitude, distance_a, distance_b, distance_c]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_2:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
                    load_parameter = [[distance, magnitude], ...]
                for load_distribution == LOAD_DISTRIBUTION_TRAPEZOIDAL:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_PARABOLIC:
                    load_parameter = [magnitude_1, magnitude_2, magnitude_3]
                for load_distribution == LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, magnitude], ...]
                for load_distribution == LOAD_DISTRIBUTION_VARYING_IN_Z:
                    load_parameter = [[distance, magnitude], ...]
            force_eccentricity (bool): Enable/Disable Force Eccentricity Option
            list_reference (bool): Enable/Disable List Reference Option
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
                for force_eccentricity == True:
                    params = {'eccentricity_horizontal_alignment': MemberLoadEccentricityHorizontalAlignment.ALIGN_NONE,
                        'eccentricity_vertical_alignment': MemberLoadEccentricityVerticalAlignment.ALIGN_NONE,
                        'eccentricity_section_middle': MemberLoadEccentricitySectionMiddle.LOAD_ECCENTRICITY_SECTION_MIDDLE_CENTER_OF_GRAVITY,
                        'is_eccentricity_at_end_different_from_start': False,
                        'eccentricity_y_at_end': 0.0,
                        'eccentricity_y_at_start': 0.0,
                        'eccentricity_z_at_end': 0.0,
                        'eccentricity_z_at_start': 0.0}
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution= load_distribution.name

        #Load Magnitude and Parameters
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM" or load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM_TOTAL":
            clientObject.magnitude = load_parameter[0]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_1":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            if load_parameter[0] == False:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
            else:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_relative = load_parameter[2]

        elif load_distribution.name ==  "LOAD_DISTRIBUTION_CONCENTRATED_N":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude = load_parameter[2]
            clientObject.count_n = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2x2":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.distance_c_is_defined_as_relative = load_parameter[2]
            clientObject.magnitude = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

            if load_parameter[2] == False:
                clientObject.distance_c_absolute = load_parameter[6]
            else:
                clientObject.distance_c_relative = load_parameter[6]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_VARYING":
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')

            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 2:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        elif load_distribution.name == "LOAD_DISTRIBUTION_TRAPEZOIDAL":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_TAPERED":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_PARABOLIC":
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 2:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING_IN_Z":
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 2:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Reference to List of Members
        clientObject.reference_to_list_of_members = list_reference

        #Force Eccentiricity
        clientObject.has_force_eccentricity = force_eccentricity

        if force_eccentricity == True:

            params_ecc = {'eccentricity_horizontal_alignment': MemberLoadEccentricityHorizontalAlignment.ALIGN_NONE,
                           'eccentricity_vertical_alignment': MemberLoadEccentricityVerticalAlignment.ALIGN_NONE,
                           'eccentricity_section_middle': MemberLoadEccentricitySectionMiddle.LOAD_ECCENTRICITY_SECTION_MIDDLE_CENTER_OF_GRAVITY,
                           'is_eccentricity_at_end_different_from_start': False,
                           'eccentricity_y_at_end': 0.0,
                           'eccentricity_y_at_start': 0.0,
                           'eccentricity_z_at_end': 0.0,
                           'eccentricity_z_at_start': 0.0}

            params_ecc.update(params)

            if params_ecc['is_eccentricity_at_end_different_from_start'] == False:

                clientObject.eccentricity_horizontal_alignment= params_ecc['eccentricity_horizontal_alignment'].name
                clientObject.eccentricity_vertical_alignment= params_ecc['eccentricity_vertical_alignment'].name
                clientObject.eccentricity_section_middle = params_ecc['eccentricity_section_middle'].name
                clientObject.eccentricity_y_at_end= params_ecc['eccentricity_y_at_start']
                clientObject.eccentricity_y_at_start= params_ecc['eccentricity_y_at_start']
                clientObject.eccentricity_z_at_end= params_ecc['eccentricity_z_at_start']
                clientObject.eccentricity_z_at_start= params_ecc['eccentricity_z_at_start']

            elif params_ecc['is_eccentricity_at_end_different_from_start'] == True:

                clientObject.eccentricity_horizontal_alignment= params_ecc['eccentricity_horizontal_alignment']
                clientObject.eccentricity_vertical_alignment= params_ecc['eccentricity_vertical_alignment']
                clientObject.eccentricity_section_middle = params_ecc['eccentricity_section_middle']
                clientObject.eccentricity_y_at_end= params_ecc['eccentricity_y_at_end']
                clientObject.eccentricity_y_at_start= params_ecc['eccentricity_y_at_start']
                clientObject.eccentricity_z_at_end= params_ecc['eccentricity_z_at_end']
                clientObject.eccentricity_z_at_start= params_ecc['eccentricity_z_at_start']

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if 'eccentricity_horizontal_alignment' or 'eccentricity_vertical_alignment' or 'eccentricity_section_middle' or 'is_eccentricity_at_end_different_from_start' or 'eccentricity_y_at_end' or 'eccentricity_y_at_start' or 'eccentricity_z_at_end' or 'eccentricity_z_at_start':
            pass
        else:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def Moment(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_distribution= MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction= MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter: list = None,
                 list_reference: bool= False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_distribution (enum): Load Distribution Enumeration
            load_direction (enum): Load Direction Enumeration
            load_parameter (list/list of lists): Load Parameter List
                for load_distribution == LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [magnitude]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_1:
                    load_parameter = [relative_distance = False, magnitude, distance_a]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_N:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude, count_n, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_2x2:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, relative_distance_c = False, magnitude, distance_a, distance_b, distance_c]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_2:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
                    load_parameter = [[distance, magnitude], ...]
                for load_distribution == LOAD_DISTRIBUTION_TRAPEZOIDAL:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_PARABOLIC:
                    load_parameter = [magnitude_1, magnitude_2, magnitude_3]
                for load_distribution == LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, magnitude], ...]
            list_reference (bool): Enable/Disable List Reference Option
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_MOMENT
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution= load_distribution.name

        #Load Magnitude and Parameters
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM":
            clientObject.magnitude = load_parameter[0]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_1":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            if load_parameter[0] == False:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
            else:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_relative = load_parameter[2]

        elif load_distribution.name ==  "LOAD_DISTRIBUTION_CONCENTRATED_N":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude = load_parameter[2]
            clientObject.count_n = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2x2":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.distance_c_is_defined_as_relative = load_parameter[2]
            clientObject.magnitude = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

            if load_parameter[2] == False:
                clientObject.distance_c_absolute = load_parameter[6]
            else:
                clientObject.distance_c_relative = load_parameter[6]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_VARYING":
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')

            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 2:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        elif load_distribution.name == "LOAD_DISTRIBUTION_TRAPEZOIDAL":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_TAPERED":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_PARABOLIC":
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 2:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Reference to List of Members
        clientObject.reference_to_list_of_members = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def Mass(
                no: int = 1,
                load_case_no: int = 1,
                members_no: str = '1',
                individual_mass_components: bool=False,
                mass_components: list = None,
                comment: str = '',
                params: dict = None,
                model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str):Assigned Member(s)
            individual_mass_components (bool): Enable/Disable Individual Mass Components Option
            mass_components (list): Mass Components List
                if individual_mass_components == False:
                    mass_components = [M]
                else:
                    mass_components = [Mx, My, Mz, Ix, Iy, Iz]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        clientObject.load_type = MemberLoadType.E_TYPE_MASS.name

        # Member Load Distribution
        clientObject.load_distribution= MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Individual Mass Components
        clientObject.individual_mass_components = individual_mass_components

        # Mass magnitude
        if individual_mass_components == False:
            clientObject.mass_global = mass_components[0]
        else:
            clientObject.mass_x = mass_components[0]
            clientObject.mass_y = mass_components[1]
            clientObject.mass_z = mass_components[2]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def Temperature(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter: list = None,
                 list_reference: bool= False,
                 load_over_total_length: bool= False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_distribution (enum): Member Load Distribution Enumeration
            load_direction (enum): Member Load Direction Enumeration
            load_parameter (list/list of lists): Load Parameter List
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [tt, tb]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
                    for load_over_total_length == False:
                        load_parameter = [tt1, tt2, tb1, tb2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                    for load_over_total_length == True:
                        load_parameter = [tt1, tt2, tb1, tb2]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [tt1, tt2, tb1, tb2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
                    load_parameter = [tb1, tb2, tb3, tt1, tt2, tt3]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, magnitude], ...]
            list_reference (bool): List Reference Boolean
            load_over_total_length (bool): Enable/Disable Load Over Total Length Option
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_TEMPERATURE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude_t_b = load_parameter[0]
            clientObject.magnitude_t_t = load_parameter[1]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_t_b_1 = load_parameter[0]
            clientObject.magnitude_t_b_2 = load_parameter[1]
            clientObject.magnitude_t_t_1 = load_parameter[2]
            clientObject.magnitude_t_t_2 = load_parameter[3]

            if load_over_total_length == False:

                if load_parameter[4] == True:
                    clientObject.distance_a_is_defined_as_relative = True
                    clientObject.distance_a_relative = load_parameter[6]
                else:
                    clientObject.distance_a_is_defined_as_relative = False
                    clientObject.distance_a_absolute = load_parameter[6]

                if load_parameter[5] == True:
                    clientObject.distance_b_is_defined_as_relative = True
                    clientObject.distance_b_relative = load_parameter[7]
                else:
                    clientObject.distance_b_is_defined_as_relative = False
                    clientObject.distance_b_absolute = load_parameter[7]
            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:

            clientObject.magnitude_t_b_1 = load_parameter[0]
            clientObject.magnitude_t_b_2 = load_parameter[1]
            clientObject.magnitude_t_t_1 = load_parameter[2]
            clientObject.magnitude_t_t_2 = load_parameter[3]

            if load_parameter[4] == True:
                clientObject.distance_a_is_defined_as_relative = True
                clientObject.distance_a_relative = load_parameter[6]
            else:
                clientObject.distance_a_is_defined_as_relative = False
                clientObject.distance_a_absolute = load_parameter[6]

            if load_parameter[5] == True:
                clientObject.distance_b_is_defined_as_relative = True
                clientObject.distance_b_relative = load_parameter[7]
            else:
                clientObject.distance_b_is_defined_as_relative = False
                clientObject.distance_b_absolute = load_parameter[7]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:

            clientObject.magnitude_t_b_1 = load_parameter[0]
            clientObject.magnitude_t_b_2 = load_parameter[1]
            clientObject.magnitude_t_b_3 = load_parameter[2]
            clientObject.magnitude_t_t_1 = load_parameter[3]
            clientObject.magnitude_t_t_2 = load_parameter[4]
            clientObject.magnitude_t_t_3 = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 3:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = load_parameter[i][1]
                mlvlp.row.magnitude_delta_t = load_parameter[i][2]
                mlvlp.row.magnitude_t_t = load_parameter[i][1]
                mlvlp.row.magnitude_t_b = load_parameter[i][2]

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        # Reference to list of members
        clientObject.reference_to_list_of_members = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def TemperatureChange(
                           no: int = 1,
                           load_case_no: int = 1,
                           members_no: str = '1',
                           load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                           load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                           load_parameter: list = None,
                           list_reference: bool= False,
                           load_over_total_length: bool= False,
                           comment: str = '',
                           params: dict = None,
                           model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_distribution (enum): Member Load Distribution
            load_direction (enum): Member Load Direction Enumeration
            load_parameter (list/list of lists): Load Parameter List
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [tc, delta_t]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
                    for load_over_total_length == False:
                        load_parameter = [delta_t_1, delta_t_2, t_c_1, t_c_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                    for load_over_total_length == True:
                        load_parameter = [delta_t_1, delta_t_2, t_c_1, t_c_2]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [delta_t_1, delta_t_2, t_c_1, t_c_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
                    load_parameter = [delta_t_1, delta_t_2, delta_t_3, t_c_1, t_c_2, t_c_3]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, magnitude], ...]
            list_reference (bool): Enable/Disable List Reference Option
            load_over_total_length (bool): Enable/Disable Load Over Total Length Option
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_TEMPERATURE_CHANGE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude_delta_t = load_parameter[0]
            clientObject.magnitude_t_c = load_parameter[1]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_delta_t_1 = load_parameter[0]
            clientObject.magnitude_delta_t_2 = load_parameter[1]
            clientObject.magnitude_t_c_1 = load_parameter[2]
            clientObject.magnitude_t_c_2 = load_parameter[3]

            if load_over_total_length == False:

                if load_parameter[4] == True:
                    clientObject.distance_a_is_defined_as_relative = True
                    clientObject.distance_a_relative = load_parameter[6]
                else:
                    clientObject.distance_a_is_defined_as_relative = False
                    clientObject.distance_a_absolute = load_parameter[6]

                if load_parameter[5] == True:
                    clientObject.distance_b_is_defined_as_relative = True
                    clientObject.distance_b_relative = load_parameter[7]
                else:
                    clientObject.distance_b_is_defined_as_relative = False
                    clientObject.distance_b_absolute = load_parameter[7]
            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:

            clientObject.magnitude_delta_t_1 = load_parameter[0]
            clientObject.magnitude_delta_t_2 = load_parameter[1]
            clientObject.magnitude_t_c_1 = load_parameter[2]
            clientObject.magnitude_t_c_2 = load_parameter[3]

            if load_parameter[4] == True:
                clientObject.distance_a_is_defined_as_relative = True
                clientObject.distance_a_relative = load_parameter[6]
            else:
                clientObject.distance_a_is_defined_as_relative = False
                clientObject.distance_a_absolute = load_parameter[6]

            if load_parameter[5] == True:
                clientObject.distance_b_is_defined_as_relative = True
                clientObject.distance_b_relative = load_parameter[7]
            else:
                clientObject.distance_b_is_defined_as_relative = False
                clientObject.distance_b_absolute = load_parameter[7]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:

            clientObject.magnitude_delta_t_1 = load_parameter[0]
            clientObject.magnitude_delta_t_2 = load_parameter[1]
            clientObject.magnitude_delta_t_3 = load_parameter[2]
            clientObject.magnitude_t_c_1 = load_parameter[3]
            clientObject.magnitude_t_c_2 = load_parameter[4]
            clientObject.magnitude_t_c_3 = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 3:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = load_parameter[i][1]
                mlvlp.row.magnitude_delta_t = load_parameter[i][2]
                mlvlp.row.magnitude_t_t = load_parameter[i][1]
                mlvlp.row.magnitude_t_b = load_parameter[i][2]

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        # Reference to list of members
        clientObject.reference_to_list_of_members = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def AxialStrain(
                    no: int = 1,
                    load_case_no: int = 1,
                    members_no: str = '1',
                    load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                    load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_X,
                    load_parameter: list = None,
                    list_reference: bool= False,
                    load_over_total_length: bool= False,
                    comment: str = '',
                    params: dict = None,
                    model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_distribution (enum): Member Load Distribution Enumeration
            load_direction (enum): Member Load Direction Enumeration
            load_parameter (list/list of lists): Load Parameter List
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [epsilon]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
                    load_parameter = [epsilon1, epsilon2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [epsilon1, epsilon2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [epsilon1, epsilon2, epsilon3]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, magnitude], ...]
            list_reference (bool): Enable/Disable List Reference Option
            load_over_total_length (bool): Enable/Disable Load Over Total Length Option
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_AXIAL_STRAIN
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude = load_parameter[0]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_over_total_length == False:

                if load_parameter[2] == True:
                    clientObject.distance_a_is_defined_as_relative = True
                    clientObject.distance_a_relative = load_parameter[4]
                else:
                    clientObject.distance_a_is_defined_as_relative = False
                    clientObject.distance_a_absolute = load_parameter[4]

                if load_parameter[3] == True:
                    clientObject.distance_b_is_defined_as_relative = True
                    clientObject.distance_b_relative = load_parameter[5]
                else:
                    clientObject.distance_b_is_defined_as_relative = False
                    clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:

            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_parameter[2] == True:
                clientObject.distance_a_is_defined_as_relative = True
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_is_defined_as_relative = False
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3] == True:
                clientObject.distance_b_is_defined_as_relative = True
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_is_defined_as_relative = False
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:

            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 3:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        # Reference to list of members
        clientObject.reference_to_list_of_members = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def AxialDisplacement(
                    no: int = 1,
                    load_case_no: int = 1,
                    members_no: str = '1',
                    load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_X,
                    magnitude : float = 0.0,
                    comment: str = '',
                    params: dict = None,
                    model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_direction (enum): Member Load Direction Enumeration
            magnitude (float): Load Magnitude
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_AXIAL_DISPLACEMENT
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        clientObject.magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def Precamber(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter: list = None,
                 list_reference: bool= False,
                 load_over_total_length: bool= False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_distribution (enum): Member Load Distribution Enumeration
            load_direction (enum): Member Load Direction Enumeration
            load_parameter (list/list of lists): Load Parameter List
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [magnitude]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
                    load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
                    load_parameter = [magnitude_1, magnitude_2, magnitude_3]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, magnitude], ...]
            list_reference (bool): Enable/Disable List Reference Option
            load_over_total_length (bool): Enable/Disable Load Over Total Length Option
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_PRECAMBER
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude = load_parameter[0]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_over_total_length == False:

                if load_parameter[2] == True:
                    clientObject.distance_a_is_defined_as_relative = True
                    clientObject.distance_a_relative = load_parameter[4]
                else:
                    clientObject.distance_a_is_defined_as_relative = False
                    clientObject.distance_a_absolute = load_parameter[4]

                if load_parameter[3] == True:
                    clientObject.distance_b_is_defined_as_relative = True
                    clientObject.distance_b_relative = load_parameter[5]
                else:
                    clientObject.distance_b_is_defined_as_relative = False
                    clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:

            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_parameter[2] == True:
                clientObject.distance_a_is_defined_as_relative = True
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_is_defined_as_relative = False
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3] == True:
                clientObject.distance_b_is_defined_as_relative = True
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_is_defined_as_relative = False
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:

            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 2:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        # Reference to list of members
        clientObject.reference_to_list_of_members = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def InitialPrestress(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_X,
                 magnitude : float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_direction (enum): Member Load Direction Enumeration
            magnitude (float): Load Magnitude
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_INITIAL_PRESTRESS
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        clientObject.magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def Displacement(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter: list = None,
                 list_reference: bool= False,
                 load_over_total_length: bool= False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_distribution (enum): Member Load Distribution Enumeration
            load_direction (enum): Member Load Direction Enumeration
            load_parameter (list/list of lists): Load Parameter List
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [magnitude]
                for load_distrubition == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
                    load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_a]
                for load_distrubition == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
                    load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_a, distance_b]
                for load_distrubition == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
                    load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_c_is_defined_as_relative = False, distance_a, distance_b, distance_c]
                for load_distrubition == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
                    load_parameter = [magnitude_1, magnitude_2, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_a, distance_b]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
                    load_parameter = [[distance, magnitude], ...]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
                    load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
                    load_parameter = [magnitude_1, magnitude_2, magnitude_3]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, magnitude], ...]
            list_reference (bool): Enable/Disable List Reference Option
            load_over_total_length (bool): Enable/Disable Load Over Total Length Option
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_DISPLACEMENT
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude = load_parameter[0]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[2]
            else:
                clientObject.distance_a_absolute = load_parameter[2]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            clientObject.distance_b_is_defined_as_relative = load_parameter[2]

            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[3]
            else:
                clientObject.distance_a_absolute = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_b_relative = load_parameter[4]
            else:
                clientObject.distance_b_absolute = load_parameter[4]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            clientObject.distance_b_is_defined_as_relative = load_parameter[2]
            clientObject.distance_c_is_defined_as_relative = load_parameter[3]

            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[2]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

            if load_parameter[3]:
                clientObject.distance_c_relative = load_parameter[6]
            else:
                clientObject.distance_c_absolute = load_parameter[6]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.distance_a_is_defined_as_relative = load_parameter[2]
            clientObject.distance_b_is_defined_as_relative = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 3:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_over_total_length == False:

                clientObject.distance_a_is_defined_as_relative = load_parameter[2]
                clientObject.distance_b_is_defined_as_relative = load_parameter[3]

                if load_parameter[2]:
                    clientObject.distance_a_relative = load_parameter[4]
                else:
                    clientObject.distance_a_absolute = load_parameter[4]

                if load_parameter[3]:
                    clientObject.distance_b_relative = load_parameter[5]
                else:
                    clientObject.distance_b_absolute = load_parameter[5]

            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.distance_a_is_defined_as_relative = load_parameter[2]
            clientObject.distance_b_is_defined_as_relative = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING:
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 2:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        # Reference to list of members
        clientObject.reference_to_list_of_members = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def Rotation(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter: list = None,
                 list_reference: bool= False,
                 load_over_total_length: bool= False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_distribution (enum): Member Load Distribution Enumeration
            load_direction (enum): Member Load Direction Enumeration
            load_parameter (list/list of lists): Load Parameter List
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [magnitude]
                for load_distrubition == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
                    load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_a]
                for load_distrubition == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
                    load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_a, distance_b]
                for load_distrubition == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
                    load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_c_is_defined_as_relative = False, distance_a, distance_b, distance_c]
                for load_distrubition == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
                    load_parameter = [magnitude_1, magnitude_2, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_a, distance_b]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
                    load_parameter = [[distance, magnitude], ...]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
                    load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
                    load_parameter = [magnitude_1, magnitude_2, magnitude_3]
                for load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, magnitude], ...]
            list_reference (bool): Enable/Disable List Reference Option
            load_over_total_length (bool): Enable/Disable Load Over Total Length Option
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_ROTATION
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude = load_parameter[0]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[2]
            else:
                clientObject.distance_a_absolute = load_parameter[2]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            clientObject.distance_b_is_defined_as_relative = load_parameter[2]

            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[3]
            else:
                clientObject.distance_a_absolute = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_b_relative = load_parameter[4]
            else:
                clientObject.distance_b_absolute = load_parameter[4]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            clientObject.distance_b_is_defined_as_relative = load_parameter[2]
            clientObject.distance_c_is_defined_as_relative = load_parameter[3]

            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[2]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

            if load_parameter[3]:
                clientObject.distance_c_relative = load_parameter[6]
            else:
                clientObject.distance_c_absolute = load_parameter[6]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.distance_a_is_defined_as_relative = load_parameter[2]
            clientObject.distance_b_is_defined_as_relative = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 2:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_over_total_length == False:

                clientObject.distance_a_is_defined_as_relative = load_parameter[2]
                clientObject.distance_b_is_defined_as_relative = load_parameter[3]

                if load_parameter[2]:
                    clientObject.distance_a_relative = load_parameter[4]
                else:
                    clientObject.distance_a_absolute = load_parameter[4]

                if load_parameter[3]:
                    clientObject.distance_b_relative = load_parameter[5]
                else:
                    clientObject.distance_b_absolute = load_parameter[5]

            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.distance_a_is_defined_as_relative = load_parameter[2]
            clientObject.distance_b_is_defined_as_relative = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING:
            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:member_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 2:
                    raise ValueError("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))
                mlvlp = model.clientModel.factory.create('ns0:member_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.magnitude = load_parameter[i][1]
                mlvlp.row.note = None
                mlvlp.row.magnitude_t_c = 0.0
                mlvlp.row.magnitude_delta_t = 0.0
                mlvlp.row.magnitude_t_t = 0.0
                mlvlp.row.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        # Reference to list of members
        clientObject.reference_to_list_of_members = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def PipeContentFull(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_direction_orientation = MemberLoadDirectionOrientation.LOAD_DIRECTION_FORWARD,
                 specific_weight : float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_direction_orientation (enum): Member Load Direction Enumeration
            specific_weight (float): Specific Weight
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_PIPE_CONTENT_FULL
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE.name

        #Member Load Orientation
        clientObject.load_direction_orientation = load_direction_orientation.name

        #Load Magnitude
        clientObject.magnitude = specific_weight

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def PipeContentPartial(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_direction_orientation = MemberLoadDirectionOrientation.LOAD_DIRECTION_FORWARD,
                 specific_weight : float = 0.0,
                 filling_height : float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            load_direction_orientation (enum): Member Load Direction Enumeration
            specific_weight (float): Specific Weight
            filling_height (float): Filling Height
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_PIPE_CONTENT_PARTIAL
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE.name

        #Member Load Orientation
        clientObject.load_direction_orientation = load_direction_orientation.name

        #Load Magnitude
        clientObject.magnitude = specific_weight

        #Filling Height
        clientObject.filling_height = filling_height

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def PipeInternalPressure(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 pressure : float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            pressure (float): Pressure
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_PIPE_INTERNAL_PRESSURE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_X.name

        #Load Magnitude
        clientObject.magnitude = pressure

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)

    @staticmethod
    def RotaryMotion(
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 angular_acceleration : float = 1.0,
                 angular_velocity : float = 2.0,
                 axis_definition_type = MemberLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS,
                 axis_orientation = MemberLoadAxisDefinitionAxisOrientation.AXIS_POSITIVE,
                 axis_definition = MemberLoadAxisDefinition.AXIS_X,
                 axis_definition_p1: list = [1,0,1],
                 axis_definition_p2: list = [0,1,0],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            members_no (str): Assigned Member(s)
            angular_acceleration (float): Angular Acceleration
            angular_velocity (float): Angular Velocity
            axis_definition_type (enum): Member Load Axis Definition Type Enumeration
            axis_orientation (enum): Member Load Axis Orientation Enumeration
            axis_definition (enum): Member Load Axis Definition Enumeration
            axis_definition_p1 (list): P1 List [X, Y, Z]
            axis_definition_p2 (list): P2 List [X, Y, Z]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Load
        clientObject = model.clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_ROTARY_MOTION
        clientObject.load_type = load_type.name

        #Angular Acceleration
        clientObject.angular_acceleration = angular_acceleration

        #Angular Velocity
        clientObject.angular_velocity = angular_velocity

        #Axis Definition Type
        clientObject.axis_definition_type = axis_definition_type.name

        #Axis definition
        if axis_definition_type == MemberLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS.name:
            clientObject.axis_definition_p1_x = axis_definition_p1[0]
            clientObject.axis_definition_p1_y = axis_definition_p1[1]
            clientObject.axis_definition_p1_z = axis_definition_p1[2]

            clientObject.axis_definition_p2_x = axis_definition_p2[0]
            clientObject.axis_definition_p2_y = axis_definition_p2[1]
            clientObject.axis_definition_p2_z = axis_definition_p2[2]

        elif axis_definition_type == MemberLoadAxisDefinitionType.AXIS_DEFINITION_POINT_AND_AXIS.name:
            clientObject.axis_definition_p1_x = axis_definition_p1[0]
            clientObject.axis_definition_p1_y = axis_definition_p1[1]
            clientObject.axis_definition_p1_z = axis_definition_p1[2]

            clientObject.axis_definition_axis = axis_definition.name
            clientObject.axis_definition_axis_orientation = axis_orientation.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Load Member Load to client model
        model.clientModel.service.set_member_load(load_case_no, clientObject)