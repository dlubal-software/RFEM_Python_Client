from RFEM.initModel import *
from RFEM.enums import *
from enum import Enum

class NodalLoad():
    
    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 nodes_no: str = '1',
                 load_direction = LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,
                 magnitude: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        '''
        Assigns nodal lode with no further options. Load type is 'force' by default.
        
        '''


        # Client model | Nodal Force
        clientObject = clientModel.factory.create('ns0:nodal_load')

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
        for key in params:
            clientObject[key] = params[key]

        # Add Nodal Force to client model
        clientModel.service.set_nodal_load(load_case_no, clientObject)

    def Force(self,
              no: int = 1,
              load_case_no: int = 1,
              nodes_no: str = '1',
              load_direction = LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,
              magnitude: float = 0.0,
              force_eccentricity : bool = False,
              specific_direction : bool = False,
              shifted_display : bool = False,
              load_parameter = {},
              comment: str = '',
              params: dict = {}):

        '''
        Assigns force type nodal lode. Further options are available. 

        For specific_direction type DIRECTION_TYPE_ROTATED_VIA_3_ANGLES;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES, NodalLoadAxesSequence, angle_1, angle_2, angle_3, angle_x, angle_y, angle_z]}

        For specific_direction type DIRECTION_TYPE_DIRECTED_TO_NODE;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_DIRECTED_TO_NODE, nodes_no]}

        For specific_direction type DIRECTION_TYPE_PARALLEL_TO_TWO_NODES;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_TWO_NODES, nodes_no]}

        For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE, line_no]}

        For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER, member_no]}


        For force_eccentricity;
        load_parameter={'force_eccentricity' : [ex, ey, ez]}


        For shifted_display;
        load_parameter={'shifted_display' : [offset_x, offset_y, offset_y, distance]}
        '''

        # Client model | Nodal Force
        clientObject = clientModel.factory.create('ns0:nodal_load')

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
        if force_eccentricity == True and shifted_display==True:
            raise Exception("Only one of force_eccentiricity and shifted_display could be TRUE")

        # Specific Direction
        if specific_direction == True:

            if 'specific_direction' not in list(load_parameter.keys()):
                raise Exception("Required key is missing")

            load_parameter_s = load_parameter['specific_direction']

            clientObject.has_specific_direction = specific_direction
            clientObject.specific_direction_type = load_parameter_s[0].name

            if load_parameter_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES:
                clientObject.axes_sequence = load_parameter_s[1].name
                clientObject.rotated_about_angle_1 = load_parameter_s[2]
                clientObject.rotated_about_angle_2 = load_parameter_s[3]
                clientObject.rotated_about_angle_3 = load_parameter_s[4]
                clientObject.rotated_about_angle_x = load_parameter_s[5]
                clientObject.rotated_about_angle_y = load_parameter_s[6]
                clientObject.rotated_about_angle_z = load_parameter_s[7]

            elif load_parameter_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_DIRECTED_TO_NODE:
                clientObject.directed_to_node_direction_node = load_parameter_s[1]

            elif load_parameter_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_TWO_NODES:
                clientObject.parallel_to_two_nodes_first_node = load_parameter_s[1]
                clientObject.parallel_to_two_nodes_second_node = load_parameter_s[2]

            elif load_parameter_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE:
                clientObject.parallel_to_line = load_parameter_s[1]

            elif load_parameter_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER:
                clientObject.parallel_to_member = load_parameter_s[1]


        #Force Eccentiricity
        if force_eccentricity == True:

            if 'force_eccentricity' not in list(load_parameter.keys()):
                raise Exception("Required key is missing")

            load_parameter_e = load_parameter['force_eccentricity']
            
            clientObject.has_force_eccentricity = force_eccentricity

            clientObject.force_eccentricity_x = load_parameter_e[0]
            clientObject.force_eccentricity_y = load_parameter_e[1]
            clientObject.force_eccentricity_z = load_parameter_e[2]

        #Shifted Display
        if shifted_display == True:

            if 'shifted_display' not in list(load_parameter.keys()):
                raise Exception("Required key is missing")

            load_parameter_d = load_parameter['shifted_display']

            clientObject.has_shifted_display = shifted_display

            clientObject.offset_x = load_parameter_d[0]
            clientObject.offset_y = load_parameter_d[1]
            clientObject.offset_z = load_parameter_d[2]
            clientObject.size_or_distance = load_parameter_d[3]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Nodal Force to client model
        clientModel.service.set_nodal_load(load_case_no, clientObject)


    def Moment(self,
              no: int = 1,
              load_case_no: int = 1,
              nodes_no: str = '1',
              load_direction = LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,
              moment_magnitude: float = 0.0,
              specific_direction : bool = False,
              shifted_display : bool = False,
              load_parameter = {},
              comment: str = '',
              params: dict = {}):

        
        '''
        Assigns moment type nodal lode. Further options are available. 

        For specific_direction type DIRECTION_TYPE_ROTATED_VIA_3_ANGLES;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES, NodalLoadAxesSequence, angle_1, angle_2, angle_3, angle_x, angle_y, angle_z]}

        For specific_direction type DIRECTION_TYPE_DIRECTED_TO_NODE;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_DIRECTED_TO_NODE, nodes_no]}

        For specific_direction type DIRECTION_TYPE_PARALLEL_TO_TWO_NODES;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_TWO_NODES, nodes_no]}

        For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE, line_no]}

        For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER, member_no]}



        For shifted_display;
        load_parameter={'shifted_display' : [offset_x, offset_y, offset_y, distance]}
        '''

        # Client model | Nodal Force
        clientObject = clientModel.factory.create('ns0:nodal_load')

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
        if specific_direction == True:

            if 'specific_direction' not in list(load_parameter.keys()):
                raise Exception("Required key is missing")

            load_parameter_s = load_parameter['specific_direction']

            clientObject.has_specific_direction = specific_direction
            clientObject.specific_direction_type = load_parameter_s[0].name

            if load_parameter_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES:
                clientObject.axes_sequence = load_parameter_s[1].name
                clientObject.rotated_about_angle_1 = load_parameter_s[2]
                clientObject.rotated_about_angle_2 = load_parameter_s[3]
                clientObject.rotated_about_angle_3 = load_parameter_s[4]
                clientObject.rotated_about_angle_x = load_parameter_s[5]
                clientObject.rotated_about_angle_y = load_parameter_s[6]
                clientObject.rotated_about_angle_z = load_parameter_s[7]

            elif load_parameter[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_DIRECTED_TO_NODE:
                clientObject.directed_to_node_direction_node = load_parameter_s[1]

            elif load_parameter[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_TWO_NODES:
                clientObject.parallel_to_two_nodes_first_node = load_parameter_s[1]
                clientObject.parallel_to_two_nodes_second_node = load_parameter_s[2]

            elif load_parameter[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE:
                clientObject.parallel_to_line = load_parameter_s[1]

            elif load_parameter[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER:
                clientObject.parallel_to_member = load_parameter_s[1]

        #Shifted Display
        if shifted_display == True:

            if 'shifted_display' not in list(load_parameter.keys()):
                raise Exception("Required key is missing")

            load_parameter_d = load_parameter['shifted_display']

            clientObject.has_shifted_display = shifted_display

            clientObject.offset_x = load_parameter_d[0]
            clientObject.offset_y = load_parameter_d[1]
            clientObject.offset_z = load_parameter_d[2]
            clientObject.size_or_distance = load_parameter_d[3]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Nodal Force to client model
        clientModel.service.set_nodal_load(load_case_no, clientObject)


    def Components(self,
              no: int = 1,
              load_case_no: int = 1,
              nodes_no: str = '1',
              components_force_x : float = 0,
              components_force_y : float = 0,
              components_force_z : float = 0,
              components_moment_x : float = 0,
              components_moment_y : float = 0,
              components_moment_z : float = 0,
              specific_direction : bool = False,
              force_eccentricity : bool = False,
              shifted_display : bool = False,
              load_parameter = {},
              comment: str = '',
              params: dict = {}):

        '''
        Assigns component type nodal lode. Further options are available. 



        For specific_direction type DIRECTION_TYPE_ROTATED_VIA_3_ANGLES;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES, NodalLoadAxesSequence, angle_1, angle_2, angle_3, angle_x, angle_y, angle_z]}


        For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE, line_no]}

        For specific_direction type DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER;
        load_parameter={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER, member_no]}


        For force_eccentricity;
        load_parameter={'force_eccentricity' : [ex, ey, ez]}
        

        For shifted_display;
        load_parameter={'shifted_display' : [offset_x, offset_y, offset_y, distance]}


        '''

        # Client model | Nodal Force
        clientObject = clientModel.factory.create('ns0:nodal_load')

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
        clientObject.components_force_x = components_force_x
        clientObject.components_force_y = components_force_y
        clientObject.components_force_z = components_force_z

        clientObject.components_moment_x = components_moment_x
        clientObject.components_moment_y = components_moment_y
        clientObject.components_moment_z = components_moment_z

        #Option Check
        if force_eccentricity == True and shifted_display==True:
            raise Exception("Only one of force_eccentiricity and shifted_display could be TRUE")


        # Specific Direction
        if specific_direction == True:

            
            if 'specific_direction' not in list(load_parameter.keys()):
                raise Exception("Required key is missing")
                

            load_parameter_s = load_parameter['specific_direction']

            clientObject.has_specific_direction = specific_direction
            clientObject.specific_direction_type = load_parameter_s[0].name

            if load_parameter_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES:
                clientObject.axes_sequence = load_parameter_s[1].name
                clientObject.rotated_about_angle_1 = load_parameter_s[2]
                clientObject.rotated_about_angle_2 = load_parameter_s[3]
                clientObject.rotated_about_angle_3 = load_parameter_s[4]
                clientObject.rotated_about_angle_x = load_parameter_s[5]
                clientObject.rotated_about_angle_y = load_parameter_s[6]
                clientObject.rotated_about_angle_z = load_parameter_s[7]

            elif load_parameter_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE:
                clientObject.parallel_to_line = load_parameter_s[1]

            elif load_parameter_s[0] == NodalLoadSpecificDirectionType.DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER:
                clientObject.parallel_to_member = load_parameter_s[1]


        #Force Eccentiricity
        if force_eccentricity == True:

                        
            if 'force_eccentricity' not in list(load_parameter.keys()):
                raise Exception("Required key is missing")
                
            load_parameter_e = load_parameter['force_eccentricity']
            
            clientObject.has_force_eccentricity = force_eccentricity

            clientObject.force_eccentricity_x = load_parameter_e[0]
            clientObject.force_eccentricity_y = load_parameter_e[1]
            clientObject.force_eccentricity_z = load_parameter_e[2]

        #Shifted Display
        if shifted_display == True:
                
            if 'shifted_display' not in list(load_parameter.keys()):
                raise Exception("Required key is missing")
                
            load_parameter_d = load_parameter['shifted_display']

            clientObject.has_shifted_display = shifted_display

            clientObject.offset_x = load_parameter_d[0]
            clientObject.offset_y = load_parameter_d[1]
            clientObject.offset_z = load_parameter_d[2]
            clientObject.size_or_distance = load_parameter_d[3]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Nodal Force to client model
        clientModel.service.set_nodal_load(load_case_no, clientObject)

    def Mass(self,
              no: int = 1,
              load_case_no: int = 1,
              nodes_no: str = '1',
              mass_advanced_options : bool = False,
              mass : float = 0,
              load_parameter = None,
              comment: str = '',
              params: dict = {}):

        '''
        Assigns mass type nodal force. Advanced options are available.

        load_parameter = [Mx, My, Mz, Ix, Iy, Iz]
        
        '''

        # Client model | Nodal Force
        clientObject = clientModel.factory.create('ns0:nodal_load')

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
        if mass_advanced_options == True:
            clientObject.mass_advanced_options = mass_advanced_options

            clientObject.mass_x = load_parameter[0]
            clientObject.mass_y = load_parameter[1]
            clientObject.mass_z = load_parameter[2]

            clientObject.mass_moment_of_inertia_x = load_parameter[3]
            clientObject.mass_moment_of_inertia_y = load_parameter[4]
            clientObject.mass_moment_of_inertia_z = load_parameter[5]
            
        elif mass_advanced_options == False:
            clientObject.mass_advanced_options = mass_advanced_options

            clientObject.mass_global = mass

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Nodal Force to client model
        clientModel.service.set_nodal_load(load_case_no, clientObject)