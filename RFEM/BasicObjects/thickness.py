from RFEM.enums import ThicknessType
from RFEM.enums import ThicknessOrthotropyType
from RFEM.enums import ThicknessSelfWeightDefinitionType
from RFEM.initModel import *
from math import *

class Thickness():
    def __init__(self,
                 no: int = 1,
                 user_defined_name_enabled: bool = False,
                 thickness_name: str = '',
                 thickness_type = ThicknessType.TYPE_UNIFORM,
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness User Defined Name
        clientObject.user_defined_name_enabled = user_defined_name_enabled

        # Thickness Name
        clientObject.name = thickness_name

        # Thickness Type
        clientObject.type = thickness_type.name

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
                 user_defined_name_enabled: bool = False,
                 thickness_name: str = '',
                 thickness_type = ThicknessType.TYPE_UNIFORM,
                 material_no: int = 1,
                 thickness_parameter = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        thickness_parameter = [uniform_thickness]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness User Defined Name
        clientObject.user_defined_name_enabled = user_defined_name_enabled
        
        # Thickness Name
        clientObject.name = thickness_name

        # Thickness Type
        clientObject.type = thickness_type.name

        # Material No.
        clientObject.material = material_no

        # Thickness Parameters
        clientObject.uniform_thickness = thickness_parameter[0]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_3Nodes(self,
                 no: int = 1,
                 user_defined_name_enabled: bool = False,
                 thickness_name: str = '',
                 thickness_type = ThicknessType.TYPE_VARIABLE_THREE_NODES,
                 material_no: int = 1,
                 thickness_parameter = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        thickness_parameter = [thickness_1, node_1, thickness_2, node_2, thickness_3, node_3]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness User Defined Name
        clientObject.user_defined_name_enabled = user_defined_name_enabled
        
        # Thickness Name
        clientObject.name = thickness_name

        # Thickness Type
        clientObject.type = thickness_type.name

        # Material No.
        clientObject.material = material_no

        # Thickness Parameters
        clientObject.thickness_1 = thickness_parameter[0]
        clientObject.node_1 = thickness_parameter[1]
        clientObject.thickness_2 = thickness_parameter[2]
        clientObject.node_2 = thickness_parameter[3]
        clientObject.thickness_3 = thickness_parameter[4]
        clientObject.node_3 = thickness_parameter[5]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_2NodesAndDirection(self,
                 no: int = 1,
                 user_defined_name_enabled: bool = False,
                 thickness_name: str = '',
                 thickness_type = ThicknessType.TYPE_VARIABLE_TWO_NODES_AND_DIRECTION,
                 material_no: int = 1,
                 thickness_parameter = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        thickness_parameter = [thickness_1, node_1, thickness_2, node_2, direction]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness User Defined Name
        clientObject.user_defined_name_enabled = user_defined_name_enabled
        
        # Thickness Name
        clientObject.name = thickness_name

        # Thickness Type
        clientObject.type = thickness_type.name

        # Material No.
        clientObject.material = material_no

        # Thickness Parameters
        clientObject.thickness_1 = thickness_parameter[0]
        clientObject.node_1 = thickness_parameter[1]
        clientObject.thickness_2 = thickness_parameter[2]
        clientObject.node_2 = thickness_parameter[3]
        clientObject.direction = thickness_parameter[4].name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_4SurfaceCorners(self,
                 no: int = 1,
                 user_defined_name_enabled: bool = False,
                 thickness_name: str = '',
                 thickness_type = ThicknessType.TYPE_VARIABLE_FOUR_SURFACE_CORNERS,
                 material_no: int = 1,
                 thickness_parameter = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        thickness_parameter = [thickness_1, node_1, thickness_2, node_2, thickness_3, node_3, thickness_4, node_4]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness User Defined Name
        clientObject.user_defined_name_enabled = user_defined_name_enabled
        
        # Thickness Name
        clientObject.name = thickness_name

        # Thickness Type
        clientObject.type = thickness_type.name

        # Material No.
        clientObject.material = material_no

        # Thickness Parameters
        clientObject.thickness_1 = thickness_parameter[0]
        clientObject.node_1 = thickness_parameter[1]
        clientObject.thickness_2 = thickness_parameter[2]
        clientObject.node_2 = thickness_parameter[3]
        clientObject.thickness_3 = thickness_parameter[4]
        clientObject.node_3 = thickness_parameter[5]
        clientObject.thickness_4 = thickness_parameter[6]
        clientObject.node_4 = thickness_parameter[7]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_Circle(self,
                 no: int = 1,
                 user_defined_name_enabled: bool = False,
                 thickness_name: str = '',
                 thickness_type = ThicknessType.TYPE_VARIABLE_CIRCLE,
                 material_no: int = 1,
                 thickness_parameter = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        thickness_parameter = [thickness_circle_center, thickness_circle_line]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness User Defined Name
        clientObject.user_defined_name_enabled = user_defined_name_enabled
        
        # Thickness Name
        clientObject.name = thickness_name

        # Thickness Type
        clientObject.type = thickness_type.name

        # Material No.
        clientObject.material = material_no

        # Thickness Parameters
        clientObject.thickness_circle_center = thickness_parameter[0]
        clientObject.thickness_circle_line = thickness_parameter[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Layers(self,
                 no: int = 1,
                 user_defined_name_enabled: bool = False,
                 thickness_name: str = '',
                 thickness_type = ThicknessType.TYPE_LAYERS,
                 reference_table = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        reference_table = [[thickness_type, material, thickness, angle, comment],
                           [...                                                 ]]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness User Defined Name
        clientObject.user_defined_name_enabled = user_defined_name_enabled
        
        # Thickness Name
        clientObject.name = thickness_name

        # Thickness Type
        clientObject.type = thickness_type.name

        # Layers
        clientObject.layers_reference_table = clientModel.factory.create('ns0:thickness').layers_reference_table

        for i in range(len(reference_table)):
            tlrt = clientModel.factory.create('ns0:thickness_layers_reference_table')
            tlrt.no = no
            tlrt.layer_no = i+1
            tlrt.layer_type = None
            tlrt.thickness_type = reference_table[i][0]
            tlrt.material = reference_table[i][1]
            tlrt.thickness = reference_table[i][2]
            tlrt.angle = reference_table[i][3] * (pi/180)
            tlrt.connection_with_other_topological_elements = False
            tlrt.comment = reference_table[i][4]
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
                 user_defined_name_enabled: bool = False,
                 thickness_name: str = '',
                 thickness_type = ThicknessType.TYPE_SHAPE_ORTHOTROPY,
                 material_no: int = 1,
                 orthotropy_type = ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_EFFECTIVE_THICKNESS,
                 rotation_beta: float = 90,
                 consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_COMPUTED_FROM_PARAMETERS, 0.18],
                 shape_orthotropy_parameter = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        consideration_of_self_weight:
            SELF_WEIGHT_COMPUTED_FROM_PARAMETERS: consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_COMPUTED_FROM_PARAMETERS, fictitious_thickness]
            SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS: consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, fictitious_thickness]
            SELF_WEIGHT_DEFINED_VIA_WEIGHT: consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_WEIGHT, self_weight]
            
        shape_orthotropy_parameter:
            ORTHOTROPIC_THICKNESS_TYPE_EFFECTIVE_THICKNESS: shape_orthotropy_parameter = [effective_thickness_x, effective_thickness_y]
            ORTHOTROPIC_THICKNESS_TYPE_COUPLING: shape_orthotropy_parameter = [coupling_thickness, coupling_spacing, coupling_width]
            ORTHOTROPIC_THICKNESS_TYPE_UNIDIRECTIONAL_RIBBED_PLATE: shape_orthotropy_parameter = [slab_thickness, rib_height, rib_spacing, rib_width]
            ORTHOTROPIC_THICKNESS_TYPE_BIDIRECTIONAL_RIBBED_PLATE: shape_orthotropy_parameter = [slab_thickness, rib_height_x, rib_height_y, rib_spacing_x, rib_spacing_y, rib_width_x, rib_width_y]
            ORTHOTROPIC_THICKNESS_TYPE_TRAPEZOIDAL_SHEET: shape_orthotropy_parameter = [sheet_thickness, total_profile_height, rib_spacin, top_flange_width, bottom_flange_width]
            ORTHOTROPIC_THICKNESS_TYPE_HOLLOW_CORE_SLAB: shape_orthotropy_parameter = [slab_thickness, void_spacing, void_diameter]
            ORTHOTROPIC_THICKNESS_TYPE_GRILLAGE: shape_orthotropy_parameter = [slab_thickness, rib_spacing_x, rib_spacing_y, rib_width_x, rib_width_y]]
        '''

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness User Defined Name
        clientObject.user_defined_name_enabled = user_defined_name_enabled
        
        # Thickness Name
        clientObject.name = thickness_name

        # Thickness Type
        clientObject.type = thickness_type.name

        # Material No.
        clientObject.material = material_no

        # Orthotropy Type
        clientObject.orthotropy_type = orthotropy_type.name

        # Rotation Beta
        clientObject.rotation_beta = rotation_beta * (pi/180)

        # Consideration of Self-Weight
        clientObject.self_weight_definition_type = consideration_of_self_weight[0].name
        if consideration_of_self_weight[0].name == 'SELF_WEIGHT_COMPUTED_FROM_PARAMETERS' or consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS':
            clientObject.fictitious_thickness = consideration_of_self_weight[1]
        elif consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINED_VIA_WEIGHT':
            clientObject.self_weight = consideration_of_self_weight[1]

        # Shape Orthotropy Parameters
        if orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_EFFECTIVE_THICKNESS':
            clientObject.effective_thickness_x = shape_orthotropy_parameter[0]
            clientObject.effective_thickness_y = shape_orthotropy_parameter[1]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_COUPLING':
            clientObject.coupling_thickness = shape_orthotropy_parameter[0]
            clientObject.coupling_spacing = shape_orthotropy_parameter[1]
            clientObject.coupling_width = shape_orthotropy_parameter[2]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_UNIDIRECTIONAL_RIBBED_PLATE':
            clientObject.slab_thickness = shape_orthotropy_parameter[0]
            clientObject.rib_height = shape_orthotropy_parameter[1]
            clientObject.rib_spacing = shape_orthotropy_parameter[2]
            clientObject.rib_width = shape_orthotropy_parameter[3]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_BIDIRECTIONAL_RIBBED_PLATE':
            clientObject.slab_thickness = shape_orthotropy_parameter[0]
            clientObject.rib_height_x = shape_orthotropy_parameter[1]
            clientObject.rib_height_y = shape_orthotropy_parameter[2]
            clientObject.rib_spacing_x = shape_orthotropy_parameter[3]
            clientObject.rib_spacing_y = shape_orthotropy_parameter[4]
            clientObject.rib_width_x = shape_orthotropy_parameter[5]
            clientObject.rib_width_y = shape_orthotropy_parameter[6]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_TRAPEZOIDAL_SHEET':
            clientObject.sheet_thickness = shape_orthotropy_parameter[0]
            clientObject.total_profile_height = shape_orthotropy_parameter[1]
            clientObject.rib_spacing = shape_orthotropy_parameter[2]
            clientObject.top_flange_width = shape_orthotropy_parameter[3]
            clientObject.bottom_flange_width = shape_orthotropy_parameter[4]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_HOLLOW_CORE_SLAB':
            clientObject.slab_thickness = shape_orthotropy_parameter[0]
            clientObject.void_spacing = shape_orthotropy_parameter[1]
            clientObject.void_diameter = shape_orthotropy_parameter[2]
        elif orthotropy_type.name == 'ORTHOTROPIC_THICKNESS_TYPE_GRILLAGE':
            clientObject.slab_thickness = shape_orthotropy_parameter[0]
            clientObject.rib_spacing_x = shape_orthotropy_parameter[1]
            clientObject.rib_spacing_y = shape_orthotropy_parameter[2]
            clientObject.rib_width_x = shape_orthotropy_parameter[3]
            clientObject.rib_width_y = shape_orthotropy_parameter[4]
        
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def StiffnessMatrix(self,
                 no: int = 1,
                 user_defined_name_enabled: bool = False,
                 thickness_name: str = '',
                 thickness_type = ThicknessType.TYPE_STIFFNESS_MATRIX,
                 material_no: int = 1,
                 rotation_beta: float = 90,
                 consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, 0.18],
                 stiffness_matrix = [[0, 0, 0, 0, 0, 0],[0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]],
                 comment: str = '',
                 params: dict = {}):

        '''
        consideration_of_self_weight:
            SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS: consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, fictitious_thickness]
            SELF_WEIGHT_DEFINED_VIA_WEIGHT: consideration_of_self_weight = [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_WEIGHT, self_weight]
        
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

        # Thickness User Defined Name
        clientObject.user_defined_name_enabled = user_defined_name_enabled
        
        # Thickness Name
        clientObject.name = thickness_name

        # Thickness Type
        clientObject.type = thickness_type.name

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
