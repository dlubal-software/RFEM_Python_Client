from os import close
from RFEM.initModel import *
from RFEM.enums import *

class LineLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 lines_no: str = '1',
                 load_direction = LoadDirectionType.LOAD_DIRECTION_LOCAL_Z,
                 magnitude: float = 0,
                 comment: str = '',
                 params: dict = {}):
        '''
        Assigns line load without any further options.
        Load type is Foce by default.
        Load distribution is Uniform by default.
        '''

        # Client model | Line Load
        clientObject = clientModel.factory.create('ns0:line_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Line No. (e.g. '5 6 7 12')
        clientObject.lines = ConvertToDlString(lines_no)

        # Line Load Type
        load_type = LineLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Line Load Distribution
        load_distribution = LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM
        clientObject.load_distribution = load_distribution.name

        # Line Load Direction
        clientObject.load_direction = load_direction.name

        # Load Magnitude
        clientObject.magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]
        
        # Add Load Line Load to client model
        clientModel.service.set_line_load(load_case_no, clientObject)


    def Force(self,
                no: int = 1,
                load_case_no: int = 1,
                lines_no: str = '1',
                load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                load_direction= LineLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                load_parameter = None,
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
        params:
            {''}
        '''

        # Client model | Line Load
        clientObject = clientModel.factory.create('ns0:line_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Line Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Lines No. (e.g. '5 6 7 12')
        clientObject.lines = ConvertToDlString(lines_no)

        # Line Load Type
        load_type = LineLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Line Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Load Magnitude and Parameters
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
                print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:line_load').varying_load_parameters

            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:line_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                #mlvlp.magnitude_t_c = 0.0      Gibt diese Parameter im localhost nicht
                #mlvlp.magnitude_delta_t = 0.0  Gibt diese Parameter im localhost nicht
                #mlvlp.magnitude_t_t = 0.0      Gibt diese Parameter im localhost nicht
                #mlvlp.magnitude_t_b = 0.0      Gibt diese Parameter im localhost nicht

                clientObject.varying_load_parameters.line_load_varying_load_parameters.append(mlvlp)

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
                print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:line_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:line_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                #mlvlp.magnitude_t_c = 0.0      Gibt diese Parameter im localhost nicht
                #mlvlp.magnitude_delta_t = 0.0  Gibt diese Parameter im localhost nicht
                #mlvlp.magnitude_t_t = 0.0      Gibt diese Parameter im localhost nicht
                #mlvlp.magnitude_t_b = 0.0      Gibt diese Parameter im localhost nicht

                clientObject.varying_load_parameters.line_load_varying_load_parameters.append(mlvlp)
        
        # Line Load Direction
        clientObject.load_direction = load_direction.name

        # Reference to List of Lines
        clientObject.reference_to_list_of_lines = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Line Load to client model
        clientModel.service.set_line_load(load_case_no, clientObject)

    def Moment(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 lines_no: str = '1',
                 load_distribution = LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = LineLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = None,
                 list_reference: bool = False,
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

        # Client model | Line Load
        clientObject = clientModel.factory.create('ns0:line_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Line Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Lines No. (e.g. '5 6 7 12')
        clientObject.lines = ConvertToDlString(lines_no)

        # Line Load Type
        load_type = LineLoadType.LOAD_TYPE_MOMENT
        clientObject.load_type = load_type.name

        # Line Load Distribution
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
                print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:line_load').varying_load_parameters

            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:line_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                #mlvlp.magnitude_t_c = 0.0
                #mlvlp.magnitude_delta_t = 0.0
                #mlvlp.magnitude_t_t = 0.0
                #mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.line_load_varying_load_parameters.append(mlvlp)

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
                print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:line_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:line_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                #mlvlp.magnitude_t_c = 0.0
                #mlvlp.magnitude_delta_t = 0.0
                #mlvlp.magnitude_t_t = 0.0
                #mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.line_load_varying_load_parameters.append(mlvlp)

        # Line Load Direction
        clientObject.load_direction = load_direction.name

        #Reference to List of Lines
        clientObject.reference_to_list_of_lines = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Line Load to client model
        clientModel.service.set_line_load(load_case_no, clientObject)

    def Mass(self,
                no: int = 1,
                load_case_no: int = 1,
                lines_no: str = '1',
                mass_components = None,
                individual_mass_components: bool=True,
                comment: str = '',
                params: dict = {}):

        # Client model | Line Load
        clientObject = clientModel.factory.create('ns0:line_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Lines No. (e.g. '5 6 7 12')
        clientObject.lines = ConvertToDlString(lines_no)

        # Line Load Type
        load_type = LineLoadType.E_TYPE_MASS
        clientObject.load_type = load_type.name

        # Line Load Distribution
        load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM
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