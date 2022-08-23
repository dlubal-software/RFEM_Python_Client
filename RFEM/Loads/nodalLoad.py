from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import LoadDirectionType, NodalLoadType, NodalLoadSpecificDirectionType

class NodalLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 nodes_no: str= '1',
                 load_direction= LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,
                 magnitude: float = 0.0,
                 comment: str= '',
                 params: dict= None,
                 model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            nodes_no (str): Assigned Nodes
            load_direction (enum): Load Direction Enumeration
            magnitude (float): Force Magnitude
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Nodal Force
        clientObject = model.clientModel.factory.create('ns0:nodal_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Nodal Force No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Nodes No. (e.g. '5 6 7 12')
        clientObject.nodes = ConvertToDlString(nodes_no)

        # Force Direction
        clientObject.load_direction = load_direction.name

        # Load Type
        load_type = NodalLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Magnitude
        clientObject.force_magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Nodal Force to client model
        model.clientModel.service.set_nodal_load(load_case_no, clientObject)

    @staticmethod
    def Force(
              no: int= 1,
              load_case_no: int = 1,
              nodes_no: str= '1',
              load_direction= LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,
              magnitude: float= 0.0,
              force_eccentricity: bool = False,
              specific_direction: bool = False,
              shifted_display: bool = False,
              comment: str= '',
              params: dict = None,
              model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            nodes_no (str): Assigned Nodes
            load_direction (enum): Load Direction Enumeration
            magnitude (float): Force Magnitude
            force_eccentricity (bool): Enable/Disable Force Eccentricity Option
            specific_direction (bool): Enable/Disable Specific Direction Option
            shifted_display (bool): Enable/Disable Shifted Display Option
            comment (str, optional): Comments
            params (dict, optional):
                For specific_direction type DIRECTION_TYPE_ROTATED_VIA_3_ANGLES;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES, NodalLoadAxesSequence, angle_1, angle_2, angle_3, angle_x, angle_y, angle_z]}
                For specific_direction type DIRECTION_TYPE_DIRECTED_TO_NODE;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_DIRECTED_TO_NODE, nodes_no]}
                For specific_direction type DIRECTION_TYPE_PARALLEL_TO_TWO_NODES;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_TWO_NODES, nodes_no]}
                For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE, line_no]}
                For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER, member_no]}
                For force_eccentricity;
                    params={'force_eccentricity' : [ex, ey, ez]}
                For shifted_display;
                    params={'shifted_display' : [offset_x, offset_y, offset_y, distance]}
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Nodal Force
        clientObject = model.clientModel.factory.create('ns0:nodal_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Nodal Force No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Nodes No. (e.g. '5 6 7 12')
        clientObject.nodes = ConvertToDlString(nodes_no)

        # Force Direction
        clientObject.load_direction = load_direction.name

        # Load Type
        load_type = NodalLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        ## Force Magnitude
        clientObject.force_magnitude = magnitude

        #Option Check
        if force_eccentricity and shifted_display:
            raise Exception("Only one of force_eccentiricity and shifted_display could be TRUE")

        # Specific Direction
        if specific_direction:

            if 'specific_direction' not in list(params.keys()):
                raise Exception("Required key is missing")

            params_s = params['specific_direction']

            clientObject.has_specific_direction = specific_direction
            clientObject.specific_direction_type = params_s[0].name

            if params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES:
                clientObject.axes_sequence = params_s[1].name
                clientObject.rotated_about_angle_1 = params_s[2]
                clientObject.rotated_about_angle_2 = params_s[3]
                clientObject.rotated_about_angle_3 = params_s[4]
                clientObject.rotated_about_angle_x = params_s[5]
                clientObject.rotated_about_angle_y = params_s[6]
                clientObject.rotated_about_angle_z = params_s[7]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_DIRECTED_TO_NODE:
                clientObject.directed_to_node_direction_node = params_s[1]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_TWO_NODES:
                clientObject.parallel_to_two_nodes_first_node = params_s[1]
                clientObject.parallel_to_two_nodes_second_node = params_s[2]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE:
                clientObject.parallel_to_line = params_s[1]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER:
                clientObject.parallel_to_member = params_s[1]

        #Force Eccentiricity
        if force_eccentricity:

            if 'force_eccentricity' not in list(params.keys()):
                raise Exception("Required key is missing")

            params_e = params['force_eccentricity']

            clientObject.has_force_eccentricity = True

            clientObject.force_eccentricity_x = params_e[0]
            clientObject.force_eccentricity_y = params_e[1]
            clientObject.force_eccentricity_z = params_e[2]

        #Shifted Display
        if shifted_display:

            if 'shifted_display' not in list(params.keys()):
                raise Exception("Required key is missing")

            params_d = params['shifted_display']

            clientObject.has_shifted_display = shifted_display

            clientObject.offset_x = params_d[0]
            clientObject.offset_y = params_d[1]
            clientObject.offset_z = params_d[2]
            clientObject.size_or_distance = params_d[3]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if 'specific_direction' or 'force_eccentricity' or 'force_eccentricity' in params.keys():
            pass
        else:
            for key in params:
                clientObject[key] = params[key]

        # Add Nodal Force to client model
        model.clientModel.service.set_nodal_load(load_case_no, clientObject)

    @staticmethod
    def Moment(
              no: int= 1,
              load_case_no: int= 1,
              nodes_no: str= '1',
              load_direction= LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,
              moment_magnitude: float= 0.0,
              specific_direction: bool= False,
              shifted_display: bool= False,
              comment: str = '',
              params: dict = None,
              model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            nodes_no (str): Assigned Nodes
            load_direction (enum): Load Direction Enumeration
            moment_magnitude (float): Moment Magnitude
            specific_direction (bool): Enable/Disable Specific Direction Option
            shifted_display (bool): Enable/Disable Shifted Display Option
            comment (str, optional): Comments
            params (dict, optional):
                For specific_direction type DIRECTION_TYPE_ROTATED_VIA_3_ANGLES;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES, NodalLoadAxesSequence, angle_1, angle_2, angle_3, angle_x, angle_y, angle_z]}
                For specific_direction type DIRECTION_TYPE_DIRECTED_TO_NODE;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_DIRECTED_TO_NODE, nodes_no]}
                For specific_direction type DIRECTION_TYPE_PARALLEL_TO_TWO_NODES;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_TWO_NODES, nodes_no]}
                For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE, line_no]}
                For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER, member_no]}
                For shifted_display;
                    params={'shifted_display' : [offset_x, offset_y, offset_y, distance]}
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Nodal Force
        clientObject = model.clientModel.factory.create('ns0:nodal_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Nodal Force No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Nodes No. (e.g. '5 6 7 12')
        clientObject.nodes = ConvertToDlString(nodes_no)

        # Force Direction
        clientObject.load_direction = load_direction.name

        # Load Type
        load_type = NodalLoadType.LOAD_TYPE_MOMENT
        clientObject.load_type = load_type.name

        ## Force Magnitude
        clientObject.moment_magnitude = moment_magnitude

        # Specific Direction
        if specific_direction:

            if 'specific_direction' not in list(params.keys()):
                raise Exception("Required key is missing")

            params_s = params['specific_direction']

            clientObject.has_specific_direction = specific_direction
            clientObject.specific_direction_type = params_s[0].name

            if params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES:
                clientObject.axes_sequence = params_s[1].name
                clientObject.rotated_about_angle_1 = params_s[2]
                clientObject.rotated_about_angle_2 = params_s[3]
                clientObject.rotated_about_angle_3 = params_s[4]
                clientObject.rotated_about_angle_x = params_s[5]
                clientObject.rotated_about_angle_y = params_s[6]
                clientObject.rotated_about_angle_z = params_s[7]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_DIRECTED_TO_NODE:
                clientObject.directed_to_node_direction_node = params_s[1]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_TWO_NODES:
                clientObject.parallel_to_two_nodes_first_node = params_s[1]
                clientObject.parallel_to_two_nodes_second_node = params_s[2]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE:
                clientObject.parallel_to_line = params_s[1]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER:
                clientObject.parallel_to_member = params_s[1]

        #Shifted Display
        if shifted_display:

            if 'shifted_display' not in list(params.keys()):
                raise Exception("Required key is missing")

            params_d = params['shifted_display']

            clientObject.has_shifted_display = shifted_display

            clientObject.offset_x = params_d[0]
            clientObject.offset_y = params_d[1]
            clientObject.offset_z = params_d[2]
            clientObject.size_or_distance = params_d[3]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if 'specific_direction' or 'force_eccentricity' in params.keys():
            pass
        else:
            for key in params:
                clientObject[key] = params[key]

        # Add Nodal Force to client model
        model.clientModel.service.set_nodal_load(load_case_no, clientObject)

    @staticmethod
    def Components(
              no: int= 1,
              load_case_no: int= 1,
              nodes_no: str= '1',
              components: list = None,
              specific_direction: bool= False,
              force_eccentricity: bool= False,
              shifted_display: bool= False,
              comment: str= '',
              params: dict= None,
              model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            nodes_no (str): Assigned Nodes
            components (list): Component Magnitude List
            specific_direction (bool): Enable/Disable Specific Direction Option
            force_eccentricity(bool): Enable/Disable Force Direction Option
            shifted_display(bool): Enable/Disable Shifted Display Option
            comment (str, optional): Comments
            params (dict, optional):
                For specific_direction type DIRECTION_TYPE_ROTATED_VIA_3_ANGLES;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES, NodalLoadAxesSequence, angle_1, angle_2, angle_3, angle_x, angle_y, angle_z]}
                For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE, line_no]}
                For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER;
                    params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER, member_no]}
                For force_eccentricity;
                    params={'force_eccentricity' : [ex, ey, ez]}

                For shifted_display;
                    params={'shifted_display' : [offset_x, offset_y, offset_y, distance]}
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Nodal Force
        clientObject = model.clientModel.factory.create('ns0:nodal_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Nodal Force No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Nodes No. (e.g. '5 6 7 12')
        clientObject.nodes = ConvertToDlString(nodes_no)

        # Load Type
        load_type = NodalLoadType.LOAD_TYPE_COMPONENTS
        clientObject.load_type = load_type.name

        #Load Magnitudes
        if len(components) == 6:
            clientObject.components_force_x = components[0]
            clientObject.components_force_y = components[1]
            clientObject.components_force_z = components[2]

            clientObject.components_moment_x = components[3]
            clientObject.components_moment_y = components[4]
            clientObject.components_moment_z = components[5]
        else:
            raise Exception("WARNING: The components must contain 6 elements. Kindly check list inputs for completeness and correctness.")

        #Option Check
        if force_eccentricity and shifted_display:
            raise Exception("WARNING: Only one of force_eccentiricity and shifted_display could be TRUE")

        # Specific Direction
        if specific_direction:

            if 'specific_direction' not in list(params.keys()):
                raise Exception("Required key is missing")

            params_s = params['specific_direction']

            clientObject.has_specific_direction = specific_direction
            clientObject.specific_direction_type = params_s[0].name

            if params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES:
                clientObject.axes_sequence = params_s[1].name
                clientObject.rotated_about_angle_1 = params_s[2]
                clientObject.rotated_about_angle_2 = params_s[3]
                clientObject.rotated_about_angle_3 = params_s[4]
                clientObject.rotated_about_angle_x = params_s[5]
                clientObject.rotated_about_angle_y = params_s[6]
                clientObject.rotated_about_angle_z = params_s[7]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE:
                clientObject.parallel_to_line = params_s[1]

            elif params_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER:
                clientObject.parallel_to_member = params_s[1]

        #Force Eccentiricity
        if force_eccentricity:

            if 'force_eccentricity' not in list(params.keys()):
                raise Exception("Required key is missing")

            params_e = params['force_eccentricity']

            clientObject.has_force_eccentricity = force_eccentricity

            clientObject.force_eccentricity_x = params_e[0]
            clientObject.force_eccentricity_y = params_e[1]
            clientObject.force_eccentricity_z = params_e[2]

        #Shifted Display
        if shifted_display:

            if 'shifted_display' not in list(params.keys()):
                raise Exception("Required key is missing")

            params_d = params['shifted_display']

            clientObject.has_shifted_display = shifted_display

            clientObject.offset_x = params_d[0]
            clientObject.offset_y = params_d[1]
            clientObject.offset_z = params_d[2]
            clientObject.size_or_distance = params_d[3]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if 'specific_direction' or 'force_eccentricity' or 'force_eccentricity' in params.keys():
            pass
        else:
            for key in params:
                clientObject[key] = params[key]

        # Add Nodal Force to client model
        model.clientModel.service.set_nodal_load(load_case_no, clientObject)

    @staticmethod
    def Mass(
              no: int = 1,
              load_case_no: int = 1,
              nodes_no: str = '1',
              individual_mass_components : bool = False,
              mass: list = None,
              comment: str = '',
              params: dict = None,
              model = Model):
        """
        Args:
            no (int): Load Tag
            load_case_no (int): Load Case Number
            nodes_no (str): Assigned Nodes
            individual_mass_components (bool): Enable/Disable Mass Component Option
            mass (list):
                if individual_mass_components == False:
                    mass = [M]
                elif individual_mass_components == True:
                    mass = [Mx, My, Mz, Ix, Iy, Iz]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Nodal Force
        clientObject = model.clientModel.factory.create('ns0:nodal_load')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Nodal Force No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Nodes No. (e.g. '5 6 7 12')
        clientObject.nodes = ConvertToDlString(nodes_no)

        # Load Type
        load_type = NodalLoadType.LOAD_TYPE_MASS
        clientObject.load_type = load_type.name

        # Magnitude
        if individual_mass_components:

            clientObject.individual_mass_components = individual_mass_components
            clientObject.mass_x = mass[0]
            clientObject.mass_y = mass[1]
            clientObject.mass_z = mass[2]

            clientObject.mass_moment_of_inertia_x = mass[3]
            clientObject.mass_moment_of_inertia_y = mass[4]
            clientObject.mass_moment_of_inertia_z = mass[5]

        else:
            clientObject.individual_mass_components = individual_mass_components
            clientObject.mass_global = mass[0]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Nodal Force to client model
        model.clientModel.service.set_nodal_load(load_case_no, clientObject)
