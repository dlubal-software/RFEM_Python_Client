from os import close
from RFEM.initModel import *
from RFEM.enums import *

class MemberLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_direction = LoadDirectionType.LOAD_DIRECTION_LOCAL_Z,
                 magnitude: float = 0,
                 comment: str = '',
                 params: dict = {}):
        '''
        Assigns member load without any further options. 
        Load type is Force by default.
        Load distrubition is Uniform by default.
        '''

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_load(load_case_no, clientObject)


    def Force(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_distribution= MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction= MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = None,
                 force_eccentricity: bool= False,
                 list_reference: bool= False,
                 comment: str = '',
                 params: dict = {}):
        '''
        load_parameter:
            LOAD_DISTRIBUTION_UNIFORM: load_parameter = magnitude
            LOAD_DISTRIBUTION_UNIFORM_TOTAL: load_parameter = magnitude
            LOAD_DISTRIBUTION_CONCENTRATED_1: load_parameter = [relative_distance = False, magnitude, distance_a]
            LOAD_DISTRIBUTION_CONCENTRATED_N: load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude, count_n, distance_a, distance_b]
            LOAD_DISTRIBUTION_CONCENTRATED_2x2: load_parameter = [relative_distance_a = False, relative_distance_b = False, relative_distance_c = False, magnitude, distance_a, distance_b, distance_c]
            LOAD_DISTRIBUTION_CONCENTRATED_2: load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_CONCENTRATED_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
            LOAD_DISTRIBUTION_TRAPEZOIDAL: load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_TAPERED: load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_PARABOLIC: load_parameter = [magnitude_1, magnitude_2, magnitude_3]
            LOAD_DISTRIBUTION_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
            LOAD_DISTRIBUTION_VARYING_IN_Z: load_parameter = [[distance, delta_distance, magnitude], ...]

        params:
            {'eccentricity_horizontal_alignment': MemberLoadEccentricityHorizontalAlignment.ALIGN_NONE,
            'eccentricity_vertical_alignment': MemberLoadEccentricityVerticalAlignment.ALIGN_NONE,
            'eccentricity_section_middle': MemberLoadEccentricitySectionMiddle.LOAD_ECCENTRICITY_SECTION_MIDDLE_CENTER_OF_GRAVITY,
            'is_eccentricity_at_end_different_from_start': False,
            'eccentricity_y_at_end': 0.0,
            'eccentricity_y_at_start': 0.0,
            'eccentricity_z_at_end': 0.0,
            'eccentricity_z_at_start': 0.0}
        '''

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
            clientObject.magnitude = load_parameter
            
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
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_load').varying_load_parameters

            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

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
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING_IN_Z":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

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

        # Add Load Member Load to client model
        clientModel.service.set_member_load(load_case_no, clientObject)

    def Moment(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_distribution= MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction= MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = None,
                 list_reference: bool= False,
                 comment: str = '',
                 params: dict = {}):
        '''
        load_parameter:
            LOAD_DISTRIBUTION_UNIFORM: load_parameter = magnitude
            LOAD_DISTRIBUTION_CONCENTRATED_1: load_parameter = [relative_distance = False, magnitude, distance_a]
            LOAD_DISTRIBUTION_CONCENTRATED_N: load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude, count_n, distance_a, distance_b]
            LOAD_DISTRIBUTION_CONCENTRATED_2x2: load_parameter = [relative_distance_a = False, relative_distance_b = False, relative_distance_c = False, magnitude, distance_a, distance_b, distance_c]
            LOAD_DISTRIBUTION_CONCENTRATED_2: load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_CONCENTRATED_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
            LOAD_DISTRIBUTION_TRAPEZOIDAL: load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_TAPERED: load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_PARABOLIC: load_parameter = [magnitude_1, magnitude_2, magnitude_3]
            LOAD_DISTRIBUTION_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
        '''

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
            clientObject.magnitude = load_parameter
            
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
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_load').varying_load_parameters

            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

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
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Reference to List of Members
        clientObject.reference_to_list_of_members = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_load(load_case_no, clientObject)

    def Mass(self,
                no: int = 1,
                load_case_no: int = 1,
                members_no: str = '1',
                mass_components = None,
                individual_mass_components: bool=True,
                comment: str = '',
                params: dict = {}):

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        #clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.E_TYPE_MASS
        clientObject.load_type = load_type.name

        # Member Load Distribution
        load_distribution= MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM
        clientObject.load_distribution= load_distribution.name

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
        for key in params:
            clientObject[key] = params[key]

    def Temperature(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_direction = MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_parameters = None,
                 comment: str = '',
                 params: dict = {}):
        '''
        Assigns member load without any further options. 
        Load type is Force by default.
        Load distrubition is Uniform by default.
        '''

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
        clientObject.magnitude_t_b = load_parameters[0]
        clientObject.magnitude_t_t = load_parameters[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_load(load_case_no, clientObject)


        
        
        




            