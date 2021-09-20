from RFEM.enums import ThicknessDirection, ThicknessType
from RFEM.enums import ThicknessOrthotropyType
from RFEM.enums import ThicknessSelfWeightDefinitionType
from RFEM.initModel import *
from math import *

class Thickness():
    def __init__(self,
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        '''
        Assigns thickness without any further options.
        Thickness types is Uniform by default.
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_UNIFORM.name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Uniform(self,
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        properties = [uniform_thickness]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_UNIFORM.name

        # Material No.
        clientObject.material = material_no

        # Thickness Parameters
        if properties == None:
            raise Exception('WARNING: The properties parameter cannot be empty.')
        clientObject.uniform_thickness = properties[0]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_3Nodes(self,
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        properties = [thickness_d1, node_no_1, thickness_d2, node_no_2, thickness_d3, node_no_3]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_VARIABLE_THREE_NODES.name

        # Material No.
        clientObject.material = material_no

        # Thickness Properties
        if properties == None:
            raise Exception('WARNING: The properties parameter cannot be empty')
        elif len(properties) != 6:
            raise Exception('WARNING: The properties parameter needs to be of length 6. Kindly check list inputs for completeness and correctness.')
        clientObject.thickness_1 = properties[0]
        clientObject.node_1 = properties[1]
        clientObject.thickness_2 = properties[2]
        clientObject.node_2 = properties[3]
        clientObject.thickness_3 = properties[4]
        clientObject.node_3 = properties[5]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_2NodesAndDirection(self,
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = [0.18, 1, 0.18, 2, ThicknessDirection.THICKNESS_DIRECTION_IN_X],
                 comment: str = '',
                 params: dict = {}):

        '''
        properties = [thickness_d1, node_no_1, thickness_d2, node_no_2, direction]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_VARIABLE_TWO_NODES_AND_DIRECTION.name

        # Material No.
        clientObject.material = material_no

        # Thickness Properties
        if len(properties) != 5:
            raise Exception('WARNING: The properties parameter needs to be of length 5. Kindly check list inputs for completeness and correctness.')
        clientObject.thickness_1 = properties[0]
        clientObject.node_1 = properties[1]
        clientObject.thickness_2 = properties[2]
        clientObject.node_2 = properties[3]
        clientObject.direction = properties[4].name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_4SurfaceCorners(self,
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        properties = [thickness_d1, node_no_1, thickness_d2, node_no_2, thickness_d3, node_no_3, thickness_d4, node_no_4]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_VARIABLE_FOUR_SURFACE_CORNERS.name

        # Material No.
        clientObject.material = material_no

        # Thickness Properties
        if properties == None:
            raise Exception('WARNING: The properties parameter cannot be empty')
        elif len(properties) != 8:
            raise Exception('WARNING: The properties parameter needs to be of length 8. Kindly check list inputs for completeness and correctness.')
        clientObject.thickness_1 = properties[0]
        clientObject.node_1 = properties[1]
        clientObject.thickness_2 = properties[2]
        clientObject.node_2 = properties[3]
        clientObject.thickness_3 = properties[4]
        clientObject.node_3 = properties[5]
        clientObject.thickness_4 = properties[6]
        clientObject.node_4 = properties[7]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_Circle(self,
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        properties = [thickness_circle_center_dC, thickness_circle_line_dR]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_VARIABLE_CIRCLE.name

        # Material No.
        clientObject.material = material_no

        # Thickness Properties
        if properties == None:
            raise Exception('WARNING: The properties parameter cannot be empty')
        elif len(properties) != 2:
            raise Exception('WARNING: The properties parameter needs to be of length 2. Kindly check list inputs for completeness and correctness.')
        clientObject.thickness_circle_center = properties[0]
        clientObject.thickness_circle_line = properties[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Layers(self,
                 no: int = 1,
                 name: str = None,
                 layers = [[0, 1, 200, 0.0, '']],
                 comment: str = '',
                 params: dict = {}):

        '''
        layers = [[thickness_type, material, thickness, rotation, comment], ...]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_LAYERS.name

        # Layers
        clientObject.layers_reference_table = clientModel.factory.create('ns0:thickness.layers_reference_table')

        for i in range(len(layers)):
            tlrt = clientModel.factory.create('ns0:thickness_layers_reference_table')
            tlrt.no = no
            tlrt.layer_no = i+1
            tlrt.layer_type = None
            tlrt.thickness_type = layers[i][0]
            tlrt.material = layers[i][1]
            tlrt.thickness = layers[i][2]
            tlrt.angle = layers[i][3] * (pi/180)
            tlrt.connection_with_other_topological_elements = False
            tlrt.comment = layers[i][4]
            tlrt.specific_weight = 0
            tlrt.weight = 0

            clientObject.layers_reference_table.thickness_layers_reference_table.append(tlrt)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def ShapeOrthotropy(self,
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 orthotropy_type = ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_EFFECTIVE_THICKNESS,
                 rotation_beta: float = 0,
                 consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_COMPUTED_FROM_PARAMETERS, 0.18],
                 parameters = [0.18, 0.18],
                 comment: str = '',
                 params: dict = {}):

        '''
        for consideration of self-weight = determined from parameters:
            consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_COMPUTED_FROM_PARAMETERS, fictitious_thickness]
            
        for consideration of self-weight = user-defined fictitious thickness:
            consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, fictitious_thickness]

        for consideration of self-weight = user-defined self-weight:
            consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_WEIGHT, self_weight]
            
        for orthotropy_type = ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_EFFECTIVE_THICKNESS:
            parameters = [effective_thickness_x, effective_thickness_y]

        for orthotropy_type = ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_COUPLING:
            parameters = [coupling_thickness, coupling_spacing, coupling_width]
        
        for orthotropy_type = ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_UNIDIRECTIONAL_RIBBED_PLATE:
            parameters = [slab_thickness, rib_height, rib_spacing, rib_width]

        for orthotropy_type = ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_BIDIRECTIONAL_RIBBED_PLATE:
            parameters = [slab_thickness, rib_height_x, rib_height_y, rib_spacing_x, rib_spacing_y, rib_width_x, rib_width_y]
        
        for orthotropy_type = ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_TRAPEZOIDAL_SHEET:
            parameters = [sheet_thickness, total_profile_height, rib_spacing, top_flange_width, bottom_flange_width]

        for orthotropy_type = ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_HOLLOW_CORE_SLAB:
            parameters = [slab_thickness, void_spacing, void_diameter]
        
        for orthotropy_type = ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_GRILLAGE:
            parameters = [slab_thickness, rib_spacing_x, rib_spacing_y, rib_width_x, rib_width_y]

        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_SHAPE_ORTHOTROPY.name

        # Material No.
        clientObject.material = material_no

        # Orthotropy Type
        clientObject.orthotropy_type = orthotropy_type.name

        # Rotation Beta
        clientObject.rotation_beta = rotation_beta * (pi/180)

        # Consideration of Self-Weight
        if len(consideration_of_self_weight) != 2:
            raise Exception('WARNING: The consideration of self-weight parameter needs to be of length 2. Kindly check list inputs for completeness and correctness.')
        clientObject.self_weight_definition_type = consideration_of_self_weight[0].name
        if consideration_of_self_weight[0].name == 'SELF_WEIGHT_COMPUTED_FROM_PARAMETERS' or consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS':
            clientObject.fictitious_thickness = consideration_of_self_weight[1]
        elif consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINED_VIA_WEIGHT':
            clientObject.self_weight = consideration_of_self_weight[1]

        # Shape Orthotropy Parameters
        if orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_EFFECTIVE_THICKNESS':
            if len(parameters) != 2:
                raise Exception('WARNING: The parameters needs to be of length 2. Kindly check list inputs for completeness and correctness.')
            clientObject.effective_thickness_x = parameters[0]
            clientObject.effective_thickness_y = parameters[1]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_COUPLING':
            if len(parameters) != 3:
                raise Exception('WARNING: The parameters needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            clientObject.coupling_thickness = parameters[0]
            clientObject.coupling_spacing = parameters[1]
            clientObject.coupling_width = parameters[2]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_UNIDIRECTIONAL_RIBBED_PLATE':
            if len(parameters) != 4:
                raise Exception('WARNING: The parameters needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            clientObject.slab_thickness = parameters[0]
            clientObject.rib_height = parameters[1]
            clientObject.rib_spacing = parameters[2]
            clientObject.rib_width = parameters[3]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_BIDIRECTIONAL_RIBBED_PLATE':
            if len(parameters) != 7:
                raise Exception('WARNING: The parameters needs to be of length 7. Kindly check list inputs for completeness and correctness.')
            clientObject.slab_thickness = parameters[0]
            clientObject.rib_height_x = parameters[1]
            clientObject.rib_height_y = parameters[2]
            clientObject.rib_spacing_x = parameters[3]
            clientObject.rib_spacing_y = parameters[4]
            clientObject.rib_width_x = parameters[5]
            clientObject.rib_width_y = parameters[6]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_TRAPEZOIDAL_SHEET':
            if len(parameters) != 5:
                raise Exception('WARNING: The parameters needs to be of length 5. Kindly check list inputs for completeness and correctness.')
            clientObject.sheet_thickness = parameters[0]
            clientObject.total_profile_height = parameters[1]
            clientObject.rib_spacing = parameters[2]
            clientObject.top_flange_width = parameters[3]
            clientObject.bottom_flange_width = parameters[4]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_HOLLOW_CORE_SLAB':
            if len(parameters) != 3:
                raise Exception('WARNING: The parameters needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            clientObject.slab_thickness = parameters[0]
            clientObject.void_spacing = parameters[1]
            clientObject.void_diameter = parameters[2]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_GRILLAGE':
            if len(parameters) != 5:
                raise Exception('WARNING: The parameters needs to be of length 5. Kindly check list inputs for completeness and correctness.')
            clientObject.slab_thickness = parameters[0]
            clientObject.rib_spacing_x = parameters[1]
            clientObject.rib_spacing_y = parameters[2]
            clientObject.rib_width_x = parameters[3]
            clientObject.rib_width_y = parameters[4]
        
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def StiffnessMatrix(self,
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 rotation_beta: float = 0,
                 consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, 0.18],
                 stiffness_matrix = [[0, 0, 0, 0, 0, 0],[0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]],
                 comment: str = '',
                 params: dict = {}):

        '''          
        for consideration of self-weight = via fictitious thickness:
            SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS: consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, fictitious_thickness]

        for consideration of self-weight = via weight:
            consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_WEIGHT, self_weight]
        
        stiffness_matrix:
            Element entry overview = [[Bending/Torsional Stiffness Elements (Nm)],
                                      [Shear Stiffness Elements (N/m)],
                                      [Membrane Stiffness Elements (N/m)],
                                      [Eccentric Stiffness Elements (Nm/m)]]
            Detailed element entry = [[D11, D12, D13, D22, D23, D33],
                                      [D44, D45, D55],
                                      [D66, D67, D68, D77, D78, D88],
                                      [D16, D17, D18, D27, D28, D38]]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_STIFFNESS_MATRIX.name

        # Material No.
        clientObject.material = material_no

        # Rotation Beta
        clientObject.rotation_beta = rotation_beta * (pi/180)

        # Consideration of Self-Weight
        clientObject.self_weight_definition_type = consideration_of_self_weight[0].name
        if consideration_of_self_weight[0].name == 'SELF_WEIGHT_COMPUTED_FROM_PARAMETERS' or consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS':
            clientObject.fictitious_thickness = consideration_of_self_weight[1]
        elif consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINED_VIA_WEIGHT':
            clientObject.self_weight = consideration_of_self_weight[1]

        # Stiffness Matrix - Bending/Torsional Stiffness Elements
        array_count = []
        [array_count.append(len(item_length)) for item_length in stiffness_matrix]
        if array_count != [6, 3, 6, 6]:
            raise Exception('WARNING: Kindly check Stiffness Matrix inputs for completeness and correctness.')
        clientObject.D11, clientObject.D12, clientObject.D13 = stiffness_matrix[0][0], stiffness_matrix[0][1], stiffness_matrix[0][2]
        clientObject.D22, clientObject.D23, clientObject.D33 = stiffness_matrix[0][3], stiffness_matrix[0][4], stiffness_matrix[0][5]
        
        # Stiffness Matrix - Shear Stiffness Elements
        clientObject.D44, clientObject.D45, clientObject.D55 = stiffness_matrix[1][0], stiffness_matrix[1][1], stiffness_matrix[1][2]
        
        # Stiffness Matrix - Membrane Stiffness Elements
        clientObject.D66, clientObject.D67, clientObject.D68 = stiffness_matrix[2][0], stiffness_matrix[2][1], stiffness_matrix[2][2]
        clientObject.D77, clientObject.D78, clientObject.D88 = stiffness_matrix[2][3], stiffness_matrix[2][4], stiffness_matrix[2][5]

        # Stiffness Matrix - Eccentric Stiffness Elements
        clientObject.D16, clientObject.D17, clientObject.D18 = stiffness_matrix[3][0], stiffness_matrix[3][1], stiffness_matrix[3][2]
        clientObject.D27, clientObject.D28, clientObject.D38 = stiffness_matrix[3][3], stiffness_matrix[3][4], stiffness_matrix[3][5]
        
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)
