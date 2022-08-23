from RFEM.initModel import Model, ConvertToDlString, clearAtributes
from RFEM.enums import *

class LineSetLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 linesets_no: str = '1',
                 load_direction = LineSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 magnitude: float = 0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        '''
        Assigns lineset load without any further options.
        Load type is Force by default.
        Load distribution is Uniform by default.

        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            linesets_no (str): Assigned Lineset(s)
            load_direction (enum): LineSet Load Direction Enumeration
            magnitude (float): Magnitude of Line Load
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Lineset Load
        clientObject = model.clientModel.factory.create('ns0:line_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Lineset Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Line No. (e.g. '5 6 7 12')
        clientObject.line_sets = ConvertToDlString(linesets_no)

        # Lineset Load Type
        load_type = LineSetLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Lineset Load Distribution
        load_distribution = LineSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM
        clientObject.load_distribution = load_distribution.name

        # Lineset Load Direction
        clientObject.load_direction = load_direction.name

        # Load Magnitude
        clientObject.magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Load Lineset Load to client model
        model.clientModel.service.set_line_set_load(load_case_no, clientObject)

    @staticmethod
    def Force(
                no: int = 1,
                load_case_no: int = 1,
                linesets_no: str = '1',
                load_distribution = LineSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                load_direction= LineSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                load_parameter = None,
                list_reference: bool= False,
                comment: str = '',
                params: dict = None,
                model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            linesets_no (str): Assigned Lineset(s)
            load_distribution (enum): LineSet Load Distribution Enumeration
            load_direction (enum): LineSet Load Direction Enumeration
            load_parameter (float/list/list of lists): Load Parameter
                for load_distribution == LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = magnitude
                for load_distribution == LOAD_DISTRIBUTION_UNIFORM_TOTAL:
                    load_parameter = magnitude
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_1:
                    load_parameter = [relative_distance = False, magnitude, distance_a]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_N:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude, count_n, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_2x2:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, relative_distance_c = False, magnitude, distance_a, distance_b, distance_c]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_2:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
                    load_parameter = [[distance, delta_distance, magnitude], ...]
                for load_distribution == LOAD_DISTRIBUTION_TRAPEZOIDAL:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_PARABOLIC:
                    load_parameter = [magnitude_1, magnitude_2, magnitude_3]
                for load_distribution == LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, delta_distance, magnitude], ...]
            list_reference (bool) : List Reference Bool
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Lineset Load
        clientObject = model.clientModel.factory.create('ns0:line_set_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Lineset Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Linesets No. (e.g. '5 6 7 12')
        clientObject.line_sets = ConvertToDlString(linesets_no)

        # Linesets Load Type
        load_type = LineSetLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Lineset Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Load Magnitude and Parameters
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM" or load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM_TOTAL":
            clientObject.magnitude = load_parameter

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_1":
            if len(load_parameter) != 3:
                raise Exception('WARNING: The load parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool):
                raise Exception ('WARNING: Load parameter at index 0 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            if not load_parameter[0]:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
            else:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_relative = load_parameter[2]

        elif load_distribution.name ==  "LOAD_DISTRIBUTION_CONCENTRATED_N":
            if len(load_parameter) != 6:
                raise Exception('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool):
                raise Exception ('WARNING: Load parameter at index 0 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude = load_parameter[2]
            clientObject.count_n = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2x2":
            if len(load_parameter) != 7:
                raise Exception('WARNING: The load parameter needs to be of length 7. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool) or not isinstance(load_parameter[1], bool) or not isinstance(load_parameter[2], bool):
                raise Exception ('WARNING: Load parameter at index 0, 1 and 2 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.distance_c_is_defined_as_relative = load_parameter[2]
            clientObject.magnitude = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

            if not load_parameter[2]:
                clientObject.distance_c_absolute = load_parameter[6]
            else:
                clientObject.distance_c_relative = load_parameter[6]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2":
            if len(load_parameter) != 6:
                raise Exception('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool) or not isinstance(load_parameter[1], bool):
                raise Exception ('WARNING: Load parameter at index 0 and 1 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = Model.clientModel.factory.create('ns0:line_load.varying_load_parameters')

            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 3:
                    raise Exception('WARNING: The load parameter sub-lists need to be of length 3. Kindly check sub-list inputs for completeness and correctness.')
                mlvlp = Model.clientModel.factory.create('ns0:line_set_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.delta_distance = load_parameter[i][1]
                mlvlp.row.magnitude = load_parameter[i][2]
                mlvlp.row.note = None

                clientObject.varying_load_parameters.line_set_load_varying_load_parameters.append(mlvlp)

        elif load_distribution.name == "LOAD_DISTRIBUTION_TRAPEZOIDAL":
            if len(load_parameter) != 6:
                raise Exception('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool) or not isinstance(load_parameter[1], bool):
                raise Exception ('WARNING: Load parameter at index 0 and 1 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_TAPERED":
            if len(load_parameter) != 6:
                raise Exception('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool) or not isinstance(load_parameter[1], bool):
                raise Exception ('WARNING: Load parameter at index 0 and 1 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_PARABOLIC":
            if len(load_parameter) != 3:
                raise Exception('WARNING: The load parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = Model.clientModel.factory.create('ns0:line_set_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 3:
                    raise Exception('WARNING: The load parameter sub-lists need to be of length 3. Kindly check sub-list inputs for completeness and correctness.')
                mlvlp = Model.clientModel.factory.create('ns0:line_set_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.delta_distance = load_parameter[i][1]
                mlvlp.row.magnitude = load_parameter[i][2]
                mlvlp.row.note = None

                clientObject.varying_load_parameters.line_set_load_varying_load_parameters.append(mlvlp)

        # Line Load Direction
        clientObject.load_direction = load_direction.name

        # Reference to List of Lines
        clientObject.reference_to_list_of_line_sets = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Load Line Load to client model
        model.clientModel.service.set_line_set_load(load_case_no, clientObject)

    @staticmethod
    def Moment(
                no: int = 1,
                load_case_no: int = 1,
                linesets_no: str = '1',
                load_distribution = LineSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                load_direction= LineSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                load_parameter = None,
                list_reference: bool= False,
                comment: str = '',
                params: dict = None,
                model = Model):
        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            linesets_no (str): Assigned Lineset(s)
            load_distribution (enum): LineSet Load Distribution Enumeration
            load_direction (enum): LineSet Load Direction Enumeration
            load_parameter (float/list/list of lists): Load Parameter
                for load_distribution == LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = magnitude
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_1:
                    load_parameter = [relative_distance = False, magnitude, distance_a]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_N:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude, count_n, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_2x2:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, relative_distance_c = False, magnitude, distance_a, distance_b, distance_c]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_2:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
                    load_parameter = [[distance, delta_distance, magnitude], ...]
                for load_distribution == LOAD_DISTRIBUTION_TRAPEZOIDAL:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_TAPERED:
                    load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
                for load_distribution == LOAD_DISTRIBUTION_PARABOLIC:
                    load_parameter = [magnitude_1, magnitude_2, magnitude_3]
                for load_distribution == LOAD_DISTRIBUTION_VARYING:
                    load_parameter = [[distance, delta_distance, magnitude], ...]
            list_reference (bool) : List Reference Bool
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Lineset Load
        clientObject = model.clientModel.factory.create('ns0:line_set_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Lineset Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Linesets No. (e.g. '5 6 7 12')
        clientObject.line_sets = ConvertToDlString(linesets_no)

        # Linesets Load Type
        load_type = LineSetLoadType.LOAD_TYPE_MOMENT
        clientObject.load_type = load_type.name

        # Lineset Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Load Magnitude and Parameters
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM" or load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM_TOTAL":
            clientObject.magnitude = load_parameter

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_1":
            if len(load_parameter) != 3:
                raise Exception('WARNING: The load parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool):
                raise Exception ('WARNING: Load parameter at index 0 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            if not load_parameter[0]:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
            else:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_relative = load_parameter[2]

        elif load_distribution.name ==  "LOAD_DISTRIBUTION_CONCENTRATED_N":
            if len(load_parameter) != 6:
                raise Exception('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool):
                raise Exception ('WARNING: Load parameter at index 0 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude = load_parameter[2]
            clientObject.count_n = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2x2":
            if len(load_parameter) != 7:
                raise Exception('WARNING: The load parameter needs to be of length 7. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool) or not isinstance(load_parameter[1], bool) or not isinstance(load_parameter[2], bool):
                raise Exception ('WARNING: Load parameter at index 0, 1 and 2 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.distance_c_is_defined_as_relative = load_parameter[2]
            clientObject.magnitude = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

            if not load_parameter[2]:
                clientObject.distance_c_absolute = load_parameter[6]
            else:
                clientObject.distance_c_relative = load_parameter[6]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2":
            if len(load_parameter) != 6:
                raise Exception('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool) or not isinstance(load_parameter[1], bool):
                raise Exception ('WARNING: Load parameter at index 0 and 1 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = Model.clientModel.factory.create('ns0:line_load.varying_load_parameters')

            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 3:
                    raise Exception('WARNING: The load parameter sub-lists need to be of length 3. Kindly check sub-list inputs for completeness and correctness.')
                mlvlp = Model.clientModel.factory.create('ns0:line_set_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.delta_distance = load_parameter[i][1]
                mlvlp.row.magnitude = load_parameter[i][2]
                mlvlp.row.note = None

                clientObject.varying_load_parameters.line_set_load_varying_load_parameters.append(mlvlp)

        elif load_distribution.name == "LOAD_DISTRIBUTION_TRAPEZOIDAL":
            if len(load_parameter) != 6:
                raise Exception('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool) or not isinstance(load_parameter[1], bool):
                raise Exception ('WARNING: Load parameter at index 0 and 1 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_TAPERED":
            if len(load_parameter) != 6:
                raise Exception('WARNING: The load parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
            if not isinstance(load_parameter[0], bool) or not isinstance(load_parameter[1], bool):
                raise Exception ('WARNING: Load parameter at index 0 and 1 to be of type "bool"')
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if not load_parameter[0]:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if not load_parameter[1]:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_PARABOLIC":
            if len(load_parameter) != 3:
                raise Exception('WARNING: The load parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = Model.clientModel.factory.create('ns0:line_set_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                if len(load_parameter[i]) != 3:
                    raise Exception('WARNING: The load parameter sub-lists need to be of length 3. Kindly check sub-list inputs for completeness and correctness.')
                mlvlp = Model.clientModel.factory.create('ns0:line_set_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.delta_distance = load_parameter[i][1]
                mlvlp.row.magnitude = load_parameter[i][2]
                mlvlp.row.note = None

                clientObject.varying_load_parameters.line_set_load_varying_load_parameters.append(mlvlp)

        # Lineset Load Direction
        clientObject.load_direction = load_direction.name

        # Reference to List of Lines
        clientObject.reference_to_list_of_line_sets = list_reference

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Load Lineset Load to client model
        model.clientModel.service.set_line_set_load(load_case_no, clientObject)

    @staticmethod
    def Mass(
                no: int = 1,
                load_case_no: int = 1,
                linesets_no: str = '1',
                individual_mass_components: bool = True,
                mass_components: list = None,
                comment: str = '',
                params: dict = None,
                model = Model):
        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            linesets_no (str): Assigned Lineset(s)
            individual_mass_components (bool): Individual Mass Components
            mass_components (list): Mass Components
                if individual_mass_components == False:
                    mass_components = [mass_global]
                if individual_mass_components == True:
                    mass_components = [mass_x, mass_y, mass_z]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Line Load
        clientObject = model.clientModel.factory.create('ns0:line_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Linesets No. (e.g. '5 6 7 12')
        clientObject.line_sets = ConvertToDlString(linesets_no)

        # Lineset Load Type
        load_type = LineSetLoadType.E_TYPE_MASS
        clientObject.load_type = load_type.name

        # Lineset Load Distribution
        load_distribution= LineSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM
        clientObject.load_distribution= load_distribution.name

        # Individual Mass Components
        if not isinstance(individual_mass_components, bool):
            raise Exception('WARNING: Input to be of type "bool"')
        clientObject.individual_mass_components = individual_mass_components

        # Mass magnitude
        if not individual_mass_components:
            if len(mass_components) != 1:
                raise Exception('WARNING: The mass components parameter for global mass assignment needs to be of length 1. Kindly check list inputs for completeness and correctness.')
            clientObject.mass_global = mass_components[0]
        else:
            if len(mass_components) != 3:
                raise Exception('WARNING: The mass components parameter for individual mass component assignment needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            clientObject.mass_x = mass_components[0]
            clientObject.mass_y = mass_components[1]
            clientObject.mass_z = mass_components[2]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Load Line Load to client model
        model.clientModel.service.set_line_set_load(load_case_no, clientObject)
