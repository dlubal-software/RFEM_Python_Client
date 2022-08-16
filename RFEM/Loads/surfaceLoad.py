from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import SurfaceLoadType, SurfaceLoadDirection, SurfaceLoadDistribution, SurfaceLoadAxisDefinitionType

class SurfaceLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 surface_no: str = '1',
                 magnitude: float = 1.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surface_no (str): Assigend Surfaces
            magnitude (float): Load Magnitude
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Surface Load
        clientObject = model.clientModel.factory.create('ns0:surface_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Load No.
        clientObject.no = no

        # Load Type
        clientObject.load_type = SurfaceLoadType.LOAD_TYPE_FORCE.name
        # Load Case No.
        clientObject.load_case = load_case_no

        # Surfaces No. (e.g. '5 6 7 12')
        clientObject.surfaces = ConvertToDlString(surface_no)

        # Load Direction
        clientObject.load_direction = SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE.name

        # Load Magnitude
        clientObject.uniform_magnitude = magnitude

        # Load Distribution
        clientObject.load_distribution = SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Load to client model
        model.clientModel.service.set_surface_load(load_case_no, clientObject)

    @staticmethod
    def Force(
                 no: int = 1,
                 load_case_no: int = 1,
                 surface_no: str = '1',
                 load_direction = SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
                 load_distribution = SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_parameter: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surface_no (str): Assigned Surfaces
            load_direction (enum): Surface Load Direction Enumeration
            load_distribution (enum): Surface Load Distribution Enumeration
            load_parameter (list): Load Parameter List
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [magnitude]
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
                    load_parameter = [magnitude_1, magnitude_2, magnitude_3, node_1, node_2, node_3]
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_X:
                                        /SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_Y:
                                        /SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_Z:
                    load_parameter = [magnitude_1, magnitude_2, node_1, node_2]
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_RADIAL:
                    if SurfaceLoadAxisDefinitionType == AXIS_DEFINITION_TWO_POINTS:
                        load_parameter = [magnitude_1, magnitude_2, node_1, node_2, SurfaceLoadAxisDefinitionType, axis_definition_p1, axis_definition_p2]
                    if SurfaceLoadAxisDefinitionType == AXIS_DEFINITION_POINT_AND_AXIS:
                        load_parameter = [magnitude_1, magnitude_2, node_1, node_2, SurfaceLoadAxisDefinitionType, SurfaceLoadAxisDefinitionAxis, axis_definition_p1]
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z:
                    load_parameter = [[distance_1, delta_distance_1, magnitude_1], [distance_2, delta_distance_2, magnitude_2]...]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Surface Load
        clientObject = model.clientModel.factory.create('ns0:surface_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Load No.
        clientObject.no = no

        # Load Type
        clientObject.load_type = SurfaceLoadType.LOAD_TYPE_FORCE.name
        # Load Case No.
        clientObject.load_case = load_case_no

        # Surfaces No. (e.g. '5 6 7 12')
        clientObject.surfaces = ConvertToDlString(surface_no)

        # Load Direction
        clientObject.load_direction = load_direction.name

        # Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Load Magnitude
        if load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.uniform_magnitude = load_parameter[0]

        elif load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

            clientObject.node_1 = load_parameter[3]
            clientObject.node_2 = load_parameter[4]
            clientObject.node_3 = load_parameter[5]

        elif load_distribution in (SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Y, \
            SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Z):

            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.node_1 = load_parameter[2]
            clientObject.node_2 = load_parameter[3]

        elif load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_RADIAL:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.node_1 = load_parameter[2]
            clientObject.node_2 = load_parameter[3]

            clientObject.axis_definition_type = load_parameter[4].name
            if load_parameter[4] == SurfaceLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS:
                clientObject.axis_definition_p1_x = load_parameter[5][0]
                clientObject.axis_definition_p1_y = load_parameter[5][1]
                clientObject.axis_definition_p1_z = load_parameter[5][2]
                clientObject.axis_definition_p2_x = load_parameter[6][0]
                clientObject.axis_definition_p2_y = load_parameter[6][1]
                clientObject.axis_definition_p2_z = load_parameter[6][2]

            else:
                clientObject.axis_definition_axis = load_parameter[5].name
                clientObject.axis_definition_p1_x = load_parameter[6][0]
                clientObject.axis_definition_p1_y = load_parameter[6][1]
                clientObject.axis_definition_p1_z = load_parameter[6][2]

        elif load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z:

            clientObject.varying_load_parameters = model.clientModel.factory.create('ns0:surface_load.varying_load_parameters')
            for i,j in enumerate(load_parameter):
                mlvlp = model.clientModel.factory.create('ns0:surface_load_varying_load_parameters_row')
                mlvlp.no = i+1
                mlvlp.row.distance = load_parameter[i][0]
                mlvlp.row.delta_distance = load_parameter[i][1]
                mlvlp.row.magnitude = load_parameter[i][2]
                mlvlp.row.note = None
                clientObject.varying_load_parameters.surface_load_varying_load_parameters.append(mlvlp)
                clientObject.varying_load_parameters_sorted = True

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Load to client model
        model.clientModel.service.set_surface_load(load_case_no, clientObject)

    @staticmethod
    def Temperature(
                 no: int = 1,
                 load_case_no: int = 1,
                 surface_no: str = '1',
                 load_distribution = SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_parameter: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surface_no (str): Assigned Surfaces
            load_distribution (enum): Surface Load Distribution Enumeration
            load_parameter (list): Load Parameter List
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [t_c, delta_t]
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
                    load_parameter = [t_c_1, delta_t_1, t_c_2, delta_t_2, t_c_3, delta_t_3, node_1, node_2, node_3]
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_X:
                                        /SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_Y:
                                        /SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_Z:
                    load_parameter = [t_c_1, delta_t_1, t_c_2, delta_t_2, node_1, node_2]
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_RADIAL:
                    if SurfaceLoadAxisDefinitionType == AXIS_DEFINITION_TWO_POINTS:
                        load_parameter = [t_c_1, delta_t_1, t_c_2, delta_t_2, node_1, node_2, SurfaceLoadAxisDefinitionType, axis_definition_p1, axis_definition_p2]
                    if SurfaceLoadAxisDefinitionType == AXIS_DEFINITION_POINT_AND_AXIS:
                        load_parameter = [t_c_1, delta_t_1, t_c_2, delta_t_2, node_1, node_2, SurfaceLoadAxisDefinitionType, SurfaceLoadAxisDefinitionAxis, axis_definition_p1]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Surface Load
        clientObject = model.clientModel.factory.create('ns0:surface_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Load No.
        clientObject.no = no

        # Load Type
        clientObject.load_type = SurfaceLoadType.LOAD_TYPE_TEMPERATURE.name
        # Load Case No.
        clientObject.load_case = load_case_no

        # Surfaces No. (e.g. '5 6 7 12')
        clientObject.surfaces = ConvertToDlString(surface_no)

        # Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Load Magnitude
        if load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.uniform_magnitude_t_c = load_parameter[0]
            clientObject.uniform_magnitude_delta_t = load_parameter[1]

        elif load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
            clientObject.magnitude_t_c_1 = load_parameter[0]
            clientObject.magnitude_delta_t_1 = load_parameter[1]
            clientObject.magnitude_t_c_2 = load_parameter[2]
            clientObject.magnitude_delta_t_2 = load_parameter[3]
            clientObject.magnitude_t_c_3 = load_parameter[4]
            clientObject.magnitude_delta_t_3 = load_parameter[5]

            clientObject.node_1 = load_parameter[6]
            clientObject.node_2 = load_parameter[7]
            clientObject.node_3 = load_parameter[8]

        elif load_distribution in (SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Y,\
            SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Z):
            clientObject.magnitude_t_c_1 = load_parameter[0]
            clientObject.magnitude_delta_t_1 = load_parameter[1]
            clientObject.magnitude_t_c_2 = load_parameter[2]
            clientObject.magnitude_delta_t_2 = load_parameter[3]

            clientObject.node_1 = load_parameter[4]
            clientObject.node_2 = load_parameter[5]

        elif load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_RADIAL:
            clientObject.magnitude_t_c_1 = load_parameter[0]
            clientObject.magnitude_delta_t_1 = load_parameter[1]

            clientObject.magnitude_t_c_2 = load_parameter[2]
            clientObject.magnitude_delta_t_2 = load_parameter[3]

            clientObject.node_1 = load_parameter[4]
            clientObject.node_2 = load_parameter[5]

            clientObject.axis_definition_type = load_parameter[6].name
            if load_parameter[6] == SurfaceLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS:
                clientObject.axis_definition_p1_x = load_parameter[7]
                clientObject.axis_definition_p1_y = load_parameter[8]
                clientObject.axis_definition_p1_z = load_parameter[9]

            else:
                clientObject.axis_definition_axis = load_parameter[7]
                clientObject.axis_definition_p1 = load_parameter[8]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Load to client model
        model.clientModel.service.set_surface_load(load_case_no, clientObject)

    @staticmethod
    def AxialStrain(
                 no: int = 1,
                 load_case_no: int = 1,
                 surface_no: str = '1',
                 load_distribution = SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_parameter: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surface_no (str): Assigned Surfaces
            load_distribution (enum): Surface Load Distribution Enumeration
            load_parameter (list): Load Parameter List
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [axial_strain_x, axial_strain_y]
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
                    load_parameter = [magnitude_axial_strain_1x, magnitude_axial_strain_1y, magnitude_axial_strain_2x, magnitude_axial_strain_2y, magnitude_axial_strain_3x, magnitude_axial_strain_3y, node_1, node_2, node_3]
                for load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_X:
                                        /SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_Y:
                                        /SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_Z:
                    load_parameter = [magnitude_axial_strain_1x, magnitude_axial_strain_1y, magnitude_axial_strain_2x, magnitude_axial_strain_2y, node_1, node_2]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Surface Load
        clientObject = model.clientModel.factory.create('ns0:surface_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Load No.
        clientObject.no = no

        # Load Type
        clientObject.load_type = SurfaceLoadType.LOAD_TYPE_AXIAL_STRAIN.name
        # Load Case No.
        clientObject.load_case = load_case_no

        # Surfaces No. (e.g. '5 6 7 12')
        clientObject.surfaces = ConvertToDlString(surface_no)

        # Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Load Magnitude
        if load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude_axial_strain_x = load_parameter[0]
            clientObject.magnitude_axial_strain_y = load_parameter[1]

        elif load_distribution == SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR:
            clientObject.magnitude_axial_strain_1x = load_parameter[0]
            clientObject.magnitude_axial_strain_1y = load_parameter[1]
            clientObject.magnitude_axial_strain_2x = load_parameter[2]
            clientObject.magnitude_axial_strain_2y = load_parameter[3]
            clientObject.magnitude_axial_strain_3x = load_parameter[4]
            clientObject.magnitude_axial_strain_3y = load_parameter[5]

            clientObject.node_1 = load_parameter[6]
            clientObject.node_2 = load_parameter[7]
            clientObject.node_3 = load_parameter[8]

        elif load_distribution in (SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Y,\
            SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Z):
            clientObject.magnitude_axial_strain_1x = load_parameter[0]
            clientObject.magnitude_axial_strain_1y = load_parameter[1]
            clientObject.magnitude_axial_strain_2x = load_parameter[2]
            clientObject.magnitude_axial_strain_2y = load_parameter[3]

            clientObject.node_1 = load_parameter[4]
            clientObject.node_2 = load_parameter[5]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Load to client model
        model.clientModel.service.set_surface_load(load_case_no, clientObject)

    @staticmethod
    def Precamber(
                 no: int = 1,
                 load_case_no: int = 1,
                 surface_no: str = '1',
                 uniform_magnitude : float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surface_no (str): Assigned Surfaces
            uniform_magnitude (float): Magnitude
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Surface Load
        clientObject = model.clientModel.factory.create('ns0:surface_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Load No.
        clientObject.no = no

        # Load Type
        clientObject.load_type = SurfaceLoadType.LOAD_TYPE_PRECAMBER.name
        # Load Case No.
        clientObject.load_case = load_case_no

        # Surfaces No. (e.g. '5 6 7 12')
        clientObject.surfaces = ConvertToDlString(surface_no)

        # Load Distribution
        clientObject.load_distribution = SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        #Load Direction
        clientObject.load_direction = SurfaceLoadDirection.LOAD_DIRECTION_LOCAL_Z.name

        # Load Magnitude
        clientObject.uniform_magnitude = uniform_magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Load to client model
        model.clientModel.service.set_surface_load(load_case_no, clientObject)

    @staticmethod
    def RotaryMotion(
                 no: int = 1,
                 load_case_no: int = 1,
                 surface_no: str = '1',
                 load_parameter: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surface_no (str): Assigned Surfaces
            load_parameter (list): Load Parameter List
                for axis_definition_type = SurfaceLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS:
                    load_parameter = [angular_velocity, angular_acceleration, SurfaceLoadAxisDefinitionType, [x1, y1, z1], [x2, y2, z2]]
                for axis_definition_type = SurfaceLoadAxisDefinitionType.AXIS_DEFINITION_POINT_AND_AXIS:
                    load_parameter = [angular_velocity, angular_acceleration, SurfaceLoadAxisDefinitionType, SurfaceLoadAxisDefinitionAxis, SurfaceLoadAxisDirectionType; [x1, y1, z1]]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Surface Load
        clientObject = model.clientModel.factory.create('ns0:surface_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Load No.
        clientObject.no = no

        # Load Type
        clientObject.load_type = SurfaceLoadType.LOAD_TYPE_ROTARY_MOTION.name
        # Load Case No.
        clientObject.load_case = load_case_no

        # Surfaces No. (e.g. '5 6 7 12')
        clientObject.surfaces = ConvertToDlString(surface_no)

        # Load Magnitude
        clientObject.angular_velocity = load_parameter[0]
        clientObject.angular_acceleration = load_parameter[1]
        clientObject.axis_definition_type = load_parameter[2].name

        if load_parameter[2] == SurfaceLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS:
            clientObject.axis_definition_p1_x = load_parameter[3][0]
            clientObject.axis_definition_p1_y = load_parameter[3][1]
            clientObject.axis_definition_p1_z = load_parameter[3][2]

            clientObject.axis_definition_p2_x = load_parameter[4][0]
            clientObject.axis_definition_p2_y = load_parameter[4][1]
            clientObject.axis_definition_p2_z = load_parameter[4][2]

        else:
            clientObject.axis_definition_axis = load_parameter[3].name
            clientObject.axis_definition_axis_orientation = load_parameter[4].name
            clientObject.axis_definition_p1_x = load_parameter[5][0]
            clientObject.axis_definition_p1_y = load_parameter[5][1]
            clientObject.axis_definition_p1_z = load_parameter[5][2]
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Load to client model
        model.clientModel.service.set_surface_load(load_case_no, clientObject)

    @staticmethod
    def Mass(
                 no: int = 1,
                 load_case_no: int = 1,
                 surface_no: str = '1',
                 individual_mass_components : bool = False,
                 mass_parameter: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            surface_no (str): Assigned Surfaces
            individual_mass_components (bool): Enable/Disable Individual Mass Components Option
            mass_parameter (list): Mass Parameter List
                if individual_mass_components == True:
                    mass_parameter = [mass_global]
                elif individual_mass_components == False:
                    mass_parameter = [mass_x, mass_y, mass_z]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Surface Load
        clientObject = model.clientModel.factory.create('ns0:surface_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Load No.
        clientObject.no = no

        # Load Type
        clientObject.load_type = SurfaceLoadType.LOAD_TYPE_MASS.name
        # Load Case No.
        clientObject.load_case = load_case_no

        # Surfaces No. (e.g. '5 6 7 12')
        clientObject.surfaces = ConvertToDlString(surface_no)

        # Load Distribution
        clientObject.load_distribution = SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        #Load Direction
        clientObject.load_direction = SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE.name

        #Individual Mass Components
        clientObject.individual_mass_components = individual_mass_components

        # Load Magnitude
        if individual_mass_components:
            clientObject.magnitude_mass_x = mass_parameter[0]
            clientObject.magnitude_mass_y = mass_parameter[1]
            clientObject.magnitude_mass_z = mass_parameter[2]
        else:
            clientObject.magnitude_mass_global = mass_parameter[0]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Load to client model
        model.clientModel.service.set_surface_load(load_case_no, clientObject)
