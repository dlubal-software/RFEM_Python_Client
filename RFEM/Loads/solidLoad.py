from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import SolidLoadType, SolidLoadDistribution, SolidLoadDirection

class SolidLoad():

    def __init__(self,
                 no: int =1,
                 load_case_no: int = 1,
                 solids_no: str= '1',
                 load_type = SolidLoadType.LOAD_TYPE_FORCE,
                 load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
                 magnitude: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            solids_no (str): Assigned Solids
            load_type (enum): Solid Load Type Enumeration
            load_distribution (enum): Solid Load Distribution Enumeration
            load_direction (enum): Solid Load Direction Enumeration
            magnitude (float): Uniform Magnitude
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Solid Load
        clientObject = model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)

        # Load Type
        clientObject.load_type = load_type.name

        # Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Load Direction
        clientObject.load_direction = load_direction.name

        # Load Magnitude
        clientObject.uniform_magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Solid Load to client model
        model.clientModel.service.set_solid_load(load_case_no, clientObject)

    @staticmethod
    def Force(
              no: int =1,
              load_case_no: int = 1,
              solids_no: str= '1',
              load_direction = SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
              magnitude: float = 0.0,
              comment: str = '',
              params: dict = None,
              model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            solids_no (str): Assigned Solids
            load_direction (enum): Solid Load Direction Enumeration
            magnitude (float): Uniform Magnitude
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Solid Load
        clientObject = model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)

        # Load Type
        clientObject.load_type = SolidLoadType.LOAD_TYPE_FORCE.name

        # Load Distribution
        clientObject.load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Load Direction
        clientObject.load_direction = load_direction.name

        # Load Magnitude
        clientObject.uniform_magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Solid Load to client model
        model.clientModel.service.set_solid_load(load_case_no, clientObject)

    @staticmethod
    def Temperature(
                    no: int = 1,
                    load_case_no: int = 1,
                    solids_no: str= '1',
                    load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                    load_parameter: list  = None,
                    comment: str = '',
                    params: dict = None,
                    model = Model):
        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            solids_no (str): Assigned Solids
            load_distribution (enum): Solid Load Distribution Enumeration
            load_parameter (float/list): Load Parameter List
                for load_distribution == SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = magnitude
                for load_distribution == SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X:
                    load_parameter = [magnitude_1, magnitude_2, node_1, node_2]
                for load_distribution == SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Y:
                    load_parameter = [magnitude_1, magnitude_2, node_1, node_2]
                for load_distribution == SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Z:
                    load_parameter = [magnitude_1, magnitude_2, node_1, node_2]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Solid Load
        clientObject = model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)

        # Load Type
        clientObject.load_type = SolidLoadType.LOAD_TYPE_TEMPERATURE.name

        # Load Distribution
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM":
            clientObject.uniform_magnitude = load_parameter
        else:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.node_1 = load_parameter[2]
            clientObject.node_2 = load_parameter[3]

        clientObject.load_distribution = load_distribution.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Solid Load to client model
        model.clientModel.service.set_solid_load(load_case_no, clientObject)

    @staticmethod
    def Strain(
               no: int = 1,
               load_case_no: int = 1,
               solids_no: str= '1',
               load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
               load_parameter: list = None,
               comment: str = '',
               params: dict = None,
               model = Model):
        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            solids_no (str): Assigned Solids
            load_distribution (enum): Solid Load Distribution Enumeration
            load_parameter (list): Load Parameter List
                for load_distribution == SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                    load_parameter = [strain_uniform_magnitude_x, strain_uniform_magnitude_y, strain_uniform_magnitude_z]
                for load_distribution == SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X:
                    load_parameter = [strain_magnitude_x1, strain_magnitude_y1, strain_magnitude_z1, strain_magnitude_x2, strain_magnitude_y2, strain_magnitude_z2, node_1, node_2]
                for load_distribution == SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Y:
                    load_parameter = [strain_magnitude_x1, strain_magnitude_y1, strain_magnitude_z1, strain_magnitude_x2, strain_magnitude_y2, strain_magnitude_z2, node_1, node_2]
                for load_distribution == SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Z:
                    load_parameter = [strain_magnitude_x1, strain_magnitude_y1, strain_magnitude_z1, strain_magnitude_x2, strain_magnitude_y2, strain_magnitude_z2, node_1, node_2]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Solid Load
        clientObject = model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)

        # Load Type
        clientObject.load_type = SolidLoadType.LOAD_TYPE_STRAIN.name

        # Load Distribution
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM":
            clientObject.strain_uniform_magnitude_x = load_parameter[0]
            clientObject.strain_uniform_magnitude_y = load_parameter[1]
            clientObject.strain_uniform_magnitude_z = load_parameter[2]
        else:
            clientObject.strain_magnitude_x1 = load_parameter[0]
            clientObject.strain_magnitude_y1 = load_parameter[1]
            clientObject.strain_magnitude_z1 = load_parameter[2]
            clientObject.strain_magnitude_x2 = load_parameter[3]
            clientObject.strain_magnitude_y2 = load_parameter[4]
            clientObject.strain_magnitude_z2 = load_parameter[6]
            clientObject.node_1 = load_parameter[6]
            clientObject.node_2 = load_parameter[7]

        clientObject.load_distribution = load_distribution.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Solid Load to client model
        model.clientModel.service.set_solid_load(load_case_no, clientObject)

    @staticmethod
    def Motion(
               no: int = 1,
               load_case_no: int = 1,
               solids_no: str= '1',
               load_parameter: list = None,
               comment: str = '',
               params: dict = None,
               model = Model):
        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            solids_no (str): Assigned Solids
            load_parameter: Load Parameter List
                load_parameter = [angular_velocity, angular_acceleration, axis_definition_p1_x, axis_definition_p1_y, axis_definition_p1_z, axis_definition_p2_x, axis_definition_p2_y, axis_definition_p2_z]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Solid Load
        clientObject = model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Assigned Solid No.
        clientObject.solids = ConvertToDlString(solids_no)

        # Load Type
        clientObject.load_type = SolidLoadType.LOAD_TYPE_ROTARY_MOTION.name

        # Velocity
        clientObject.angular_velocity = load_parameter[0]

        # Acceleration
        clientObject.angular_acceleration = load_parameter[1]

        # Axis Definition
        clientObject.axis_definition_p1_x = load_parameter[2]
        clientObject.axis_definition_p1_y = load_parameter[3]
        clientObject.axis_definition_p1_z = load_parameter[4]
        clientObject.axis_definition_p2_x = load_parameter[5]
        clientObject.axis_definition_p2_y = load_parameter[6]
        clientObject.axis_definition_p2_z = load_parameter[7]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Solid Load to client model
        model.clientModel.service.set_solid_load(load_case_no, clientObject)

    #def Buoyancy():
    #    print('The function Buoyancy() is not implemented yet.')

    #def Gas():
    #    print('The function Gas() is not implemented yet.')
