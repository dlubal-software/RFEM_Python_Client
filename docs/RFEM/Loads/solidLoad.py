from RFEM.initModel import Model, clearAttributes, ConvertToDlString
from RFEM.enums import SolidLoadType, SolidLoadDistribution, SolidLoadDirection

class SolidLoad():

    def __init__(self,
                 no: int =1,
                 load_case_no: int = 1,
                 solids_no: str= '1',
                 load_type = SolidLoadType.LOAD_TYPE_FORCE,
                 load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
                 magnitude: float = 0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Solid Load
        clientObject = Model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Load to client model
        Model.clientModel.service.set_solid_load(load_case_no, clientObject)

    def Force(self,
              no: int =1,
              load_case_no: int = 1,
              solids_no: str= '1',
              load_direction = SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
              magnitude: float = 0,
              comment: str = '',
              params: dict = {}):

        # Client model | Solid Load
        clientObject = Model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Load to client model
        Model.clientModel.service.set_solid_load(load_case_no, clientObject)

    def Temperature(self,
                    no: int = 1,
                    load_case_no: int = 1,
                    solids_no: str= '1',
                    load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                    load_parameter = None,
                    comment: str = '',
                    params: dict = {}):
        '''
        load_parameter:
            LOAD_DISTRIBUTION_UNIFORM: load_parameter = magnitude
            LOAD_DISTRIBUTION_LINEAR_IN_X: load_parameter = [magnitude_1, magnitude_2, node_1, node_2]
            LOAD_DISTRIBUTION_LINEAR_IN_Y: load_parameter = [magnitude_1, magnitude_2, node_1, node_2]
            LOAD_DISTRIBUTION_LINEAR_IN_Z: load_parameter = [magnitude_1, magnitude_2, node_1, node_2]
        params:
            {''}
        '''
        # Client model | Solid Load
        clientObject = Model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Load to client model
        Model.clientModel.service.set_solid_load(load_case_no, clientObject)

    def Strain(self,
               no: int = 1,
               load_case_no: int = 1,
               solids_no: str= '1',
               load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
               load_parameter = None,
               comment: str = '',
               params: dict = {}):
        '''
        load_parameter:
            LOAD_DISTRIBUTION_UNIFORM: load_parameter = [strain_uniform_magnitude_x, strain_uniform_magnitude_y, strain_uniform_magnitude_z]
            LOAD_DISTRIBUTION_LINEAR_IN_X: load_parameter = [strain_magnitude_x1, strain_magnitude_y1, strain_magnitude_z1, strain_magnitude_x2, strain_magnitude_y2, strain_magnitude_z2, node_1, node_2]
            LOAD_DISTRIBUTION_LINEAR_IN_Y: load_parameter = [strain_magnitude_x1, strain_magnitude_y1, strain_magnitude_z1, strain_magnitude_x2, strain_magnitude_y2, strain_magnitude_z2, node_1, node_2]
            LOAD_DISTRIBUTION_LINEAR_IN_Z: load_parameter = [strain_magnitude_x1, strain_magnitude_y1, strain_magnitude_z1, strain_magnitude_x2, strain_magnitude_y2, strain_magnitude_z2, node_1, node_2]
        params:
            {''}
        '''
        # Client model | Solid Load
        clientObject = Model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Load to client model
        Model.clientModel.service.set_solid_load(load_case_no, clientObject)

    def Motion(self,
               no: int = 1,
               load_case_no: int = 1,
               solids_no: str= '1',
               load_parameter = None,
               comment: str = '',
               params: dict = {}):
        '''
        load_parameter:
            load_parameter = [angular_velocity, angular_acceleration, axis_definition_p1_x, axis_definition_p1_y, axis_definition_p1_z, axis_definition_p2_x, axis_definition_p2_y, axis_definition_p2_z]
        params:
            {''}
        '''
        # Client model | Solid Load
        clientObject = Model.clientModel.factory.create('ns0:solid_load')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Load to client model
        Model.clientModel.service.set_solid_load(load_case_no, clientObject)

    #def Buoyancy():
    #    print('The function Buoyancy() is not implemented yet.')

    #def Gas():
    #    print('The function Gas() is not implemented yet.')
