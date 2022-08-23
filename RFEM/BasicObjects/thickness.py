from RFEM.enums import ThicknessDirection, ThicknessType, LayerType
from RFEM.enums import ThicknessOrthotropyType, AddOn, ObjectTypes
from RFEM.enums import ThicknessShapeOrthotropySelfWeightDefinitionType
from RFEM.enums import ThicknessStiffnessMatrixSelfWeightDefinitionType
from RFEM.initModel import Model, GetAddonStatus, clearAtributes, SetAddonStatus, ConvertStrToListOfInt
from math import pi

class Thickness():
    def __init__(self,
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Thickness Tag
            name (str): Thickness Name
            material_no (int): Tag of Material assigned to Thickness
            uniform_thickness_d (float): Magnitude of Thickness
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Thickness
        clientObject = model.clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name is not None:
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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Thickness to client model
        model.clientModel.service.set_thickness(clientObject)

    @staticmethod
    def Uniform(
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = [0.2],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Thickness Tag
            name (str): Thickness Name
            material_no (int): Tag of Material assigned to Thickness
            properties (list): Magnitude of Thickness [Thickness]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Thickness
        clientObject = model.clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name is not None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_UNIFORM.name

        # Material No.
        clientObject.material = material_no

        # Thickness Parameters
        if properties is None:
            raise Exception('WARNING: The properties parameter cannot be empty.')
        clientObject.uniform_thickness = properties[0]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Thickness to client model
        model.clientModel.service.set_thickness(clientObject)

    @staticmethod
    def Variable_3Nodes(
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Thickness Tag
            name (str): Thickness Name
            material_no (int): Tag of Material assigned to Thickness
            properties (list): Properties for 3 Nodes Variable Thickness Definition
                properties = [thickness_d1, node_no_1, thickness_d2, node_no_2, thickness_d3, node_no_3]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Thickness
        clientObject = model.clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name is not None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_VARIABLE_THREE_NODES.name

        # Material No.
        clientObject.material = material_no

        # Thickness Properties
        if properties is None:
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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Thickness to client model
        model.clientModel.service.set_thickness(clientObject)

    @staticmethod
    def Variable_2NodesAndDirection(
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = [0.18, 1, 0.18, 2, ThicknessDirection.THICKNESS_DIRECTION_IN_X],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Thickness Tag
            name (str): Thickness Name
            material_no (int): Tag of Material assigned to Thickness
            properties (list): Properties for 2 Nodes and Direction Variable Thickness Definition
                properties = [thickness_d1, node_no_1, thickness_d2, node_no_2, direction]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited

        '''

        # Client model | Thickness
        clientObject = model.clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name is not None:
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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Thickness to client model
        model.clientModel.service.set_thickness(clientObject)

    @staticmethod
    def Variable_4SurfaceCorners(
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Thickness Tag
            name (str): Thickness Name
            material_no (int): Tag of Material assigned to Thickness
            properties (list): Properties for 4 Surface Corners Variable Definition
                properties = [thickness_d1, node_no_1, thickness_d2, node_no_2, thickness_d3, node_no_3, thickness_d4, node_no_4]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited

        '''

        # Client model | Thickness
        clientObject = model.clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name is not None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_VARIABLE_FOUR_SURFACE_CORNERS.name

        # Material No.
        clientObject.material = material_no

        # Thickness Properties
        if properties is None:
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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Thickness to client model
        model.clientModel.service.set_thickness(clientObject)

    @staticmethod
    def Variable_Circle(
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 properties = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Thickness Tag
            name (str): Thickness Name
            material_no (int): Tag of Material assigned to Thickness
            properties (list): Properties for Circular Thickness Definition
                properties = [thickness_circle_center_dC, thickness_circle_line_dR]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Thickness
        clientObject = model.clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name is not None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_VARIABLE_CIRCLE.name

        # Material No.
        clientObject.material = material_no

        # Thickness Properties
        if properties is None:
            raise Exception('WARNING: The properties parameter cannot be empty')
        elif len(properties) != 2:
            raise Exception('WARNING: The properties parameter needs to be of length 2. Kindly check list inputs for completeness and correctness.')
        clientObject.thickness_circle_center = properties[0]
        clientObject.thickness_circle_line = properties[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Thickness to client model
        model.clientModel.service.set_thickness(clientObject)

    @staticmethod
    def Layers(
                 no: int = 1,
                 name: str = None,
                 layers = [[0, 1, 0.012], [0, 1, 0.01]],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        NOTE: Available only for Special Solution Add-on Multilayer Surfaces.

        Args:
            no (int): Thickness Tag
            name (str): Thickness Name
            layers (list of lists): Layers Table as an Array
                layers = [[thickness_type, material, thickness], ...]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Check if Multilayer Surfaces Add-on is ON.
        if not GetAddonStatus(model.clientModel, AddOn.multilayer_surfaces_design_active):
            SetAddonStatus(model.clientModel, AddOn.multilayer_surfaces_design_active, True)

        # Client model | Thickness
        clientObject = model.clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_LAYERS.name



        # Layers
        clientObject.layers_reference_table = model.clientModel.factory.create('ns0:thickness.layers_reference_table')

        for i,j in enumerate(layers):
            tlrt = model.clientModel.factory.create('ns0:thickness_layers_reference_table_row')
            tlrt.no = i+1
            tlrt.row.layer_no = i+1
            tlrt.row.layer_type = LayerType.E_LAYER_TYPE_LAYER.name
            tlrt.row.thickness_type = layers[i][0]
            tlrt.row.material = layers[i][1]
            tlrt.row.thickness = layers[i][2]
            tlrt.row.connection_with_other_topological_elements = False
            if Model.clientModel.service.get_material(layers[i][1])['material_model'] == "MODEL_ORTHOTROPIC_2D":
                tlrt.row.angle = layers[i][3] * (pi/180)
                if len(layers[i]) == 5:
                    tlrt.row.comment = layers[i][4]
            else:
                if len(layers[i]) == 4:
                    tlrt.row.comment = layers[i][3]

            clientObject.layers_reference_table.thickness_layers_reference_table.append(tlrt)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Thickness to client model
        model.clientModel.service.set_thickness(clientObject)

    @staticmethod
    def ShapeOrthotropy(
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 orthotropy_type = ThicknessOrthotropyType.EFFECTIVE_THICKNESS,
                 rotation_beta: float = 0.0,
                 consideration_of_self_weight = [ThicknessShapeOrthotropySelfWeightDefinitionType.SELF_WEIGHT_COMPUTED_FROM_PARAMETERS, 0.18],
                 parameters = [0.18, 0.18],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Thickness Tag
            name (str): Thickness Name
            material_no (int): Tag of Material assigned to Thickness
            orthotropy_type (enum): Thickness Orthotropy Type
            rotation_beta (float): Rotation
            consideration_of_self_weight (list): Consideration of Self-Weight Parameters
                for consideration_of_self_weight == 'parameter defined'
                    consideration_of_self_weight = [ThicknessShapeOrthotropySelfWeightDefinitionType.SELF_WEIGHT_COMPUTED_FROM_PARAMETERS, fictitious_thickness]
                for consideration_of_self_weight == 'user-defined fictitious thickness'
                    consideration_of_self_weight = [ThicknessShapeOrthotropySelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, fictitious_thickness]
                for consideration_of_self_weight == 'user-defined'
                    consideration_of_self_weight = [ThicknessShapeOrthotropySelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_WEIGHT, self_weight]
            parameters (list): Parameters List of chosen Orthotropy Type
                for orthotropy_type == ThicknessOrthotropyType.EFFECTIVE_THICKNESS:
                    parameters = [effective_thickness_x, effective_thickness_y]
                for orthotropy_type == ThicknessOrthotropyType.COUPLING:
                    parameters = [coupling_thickness, coupling_spacing, coupling_width]
                for orthotropy_type == ThicknessOrthotropyType.UNIDIRECTIONAL_RIBBED_PLATE:
                    parameters = [slab_thickness, rib_height, rib_spacing, rib_width]
                for orthotropy_type == ThicknessOrthotropyType.BIDIRECTIONAL_RIBBED_PLATE:
                    parameters = [slab_thickness, rib_height_x, rib_height_y, rib_spacing_x, rib_spacing_y, rib_width_x, rib_width_y]
                for orthotropy_type == ThicknessOrthotropyType.TRAPEZOIDAL_SHEET:
                    parameters = [sheet_thickness, total_profile_height, rib_spacing, top_flange_width, bottom_flange_width]
                for orthotropy_type == ThicknessOrthotropyType.HOLLOW_CORE_SLAB:
                    parameters = [slab_thickness, void_spacing, void_diameter]
                for orthotropy_type == ThicknessOrthotropyType.GRILLAGE:
                    parameters = [slab_thickness, rib_spacing_x, rib_spacing_y, rib_width_x, rib_width_y]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Thickness
        clientObject = model.clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name is not None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_SHAPE_ORTHOTROPY.name

        # Material No.
        clientObject.material = material_no

        # Orthotropy Type
        clientObject.orthotropy_type = 'ORTHOTROPIC_THICKNESS_TYPE_' + orthotropy_type.name

        # Rotation Beta
        clientObject.orthotropy_rotation_beta = rotation_beta * (pi/180)

        # Consideration of Self-Weight
        if len(consideration_of_self_weight) != 2:
            raise Exception('WARNING: The consideration of self-weight parameter needs to be of length 2. Kindly check list inputs for completeness and correctness.')
        clientObject.shape_orthotropy_self_weight_definition_type = consideration_of_self_weight[0].name
        if consideration_of_self_weight[0].name == 'SELF_WEIGHT_COMPUTED_FROM_PARAMETERS' or consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS':
            clientObject.orthotropy_fictitious_thickness = consideration_of_self_weight[1]
        elif consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINED_VIA_WEIGHT':
            clientObject.shape_orthotropy_self_weight = consideration_of_self_weight[1]

        # Shape Orthotropy Parameters
        if orthotropy_type.name == 'EFFECTIVE_THICKNESS':
            if len(parameters) != 2:
                raise Exception('WARNING: The parameters needs to be of length 2. Kindly check list inputs for completeness and correctness.')
            clientObject.shape_orthotropy_effective_thickness_x = parameters[0]
            clientObject.shape_orthotropy_effective_thickness_y = parameters[1]
        elif orthotropy_type.name == 'COUPLING':
            if len(parameters) != 3:
                raise Exception('WARNING: The parameters needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            clientObject.coupling_thickness = parameters[0]
            clientObject.coupling_spacing = parameters[1]
            clientObject.coupling_width = parameters[2]
        elif orthotropy_type.name == 'UNIDIRECTIONAL_RIBBED_PLATE':
            if len(parameters) != 4:
                raise Exception('WARNING: The parameters needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            clientObject.slab_thickness = parameters[0]
            clientObject.rib_height = parameters[1]
            clientObject.rib_spacing = parameters[2]
            clientObject.rib_width = parameters[3]
        elif orthotropy_type.name == 'BIDIRECTIONAL_RIBBED_PLATE':
            if len(parameters) != 7:
                raise Exception('WARNING: The parameters needs to be of length 7. Kindly check list inputs for completeness and correctness.')
            clientObject.slab_thickness = parameters[0]
            clientObject.rib_height_x = parameters[1]
            clientObject.rib_height_y = parameters[2]
            clientObject.rib_spacing_x = parameters[3]
            clientObject.rib_spacing_y = parameters[4]
            clientObject.rib_width_x = parameters[5]
            clientObject.rib_width_y = parameters[6]
        elif orthotropy_type.name == 'TRAPEZOIDAL_SHEET':
            if len(parameters) != 5:
                raise Exception('WARNING: The parameters needs to be of length 5. Kindly check list inputs for completeness and correctness.')
            clientObject.sheet_thickness = parameters[0]
            clientObject.total_profile_height = parameters[1]
            clientObject.rib_spacing = parameters[2]
            clientObject.top_flange_width = parameters[3]
            clientObject.bottom_flange_width = parameters[4]
        elif orthotropy_type.name == 'HOLLOW_CORE_SLAB':
            if len(parameters) != 3:
                raise Exception('WARNING: The parameters needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            clientObject.slab_thickness = parameters[0]
            clientObject.void_spacing = parameters[1]
            clientObject.void_diameter = parameters[2]
        elif orthotropy_type.name == 'GRILLAGE':
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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Thickness to client model
        model.clientModel.service.set_thickness(clientObject)

    @staticmethod
    def StiffnessMatrix(
                 no: int = 1,
                 name: str = None,
                 material_no: int = 1,
                 rotation_beta: float = 0.0,
                 consideration_of_self_weight = [ThicknessStiffnessMatrixSelfWeightDefinitionType.SELF_WEIGHT_DEFINITION_TYPE_DEFINED_VIA_FICTITIOUS_THICKNESS_AND_BULK_DENSITY, 0.2, 0.0],
                 coefficient_of_thermal_expansion: float = 0,
                 stiffness_matrix = [[0, 0, 0, 0, 0, 0],[0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Thickness Tag
            name (str): Thickness Name
            material_no (int): Tag of Material assigned to Thickness
            rotation_beta (float): Rotation
            consideration_of_self_weight (list): Self-Weight Consideration Parameters
                for consideration_of_self_weight == 'fictitious thickness and bulk density'
                    consideration_of_self_weight = [ThicknessStiffnessMatrixSelfWeightDefinitionType.SELF_WEIGHT_DEFINITION_TYPE_DEFINED_VIA_FICTITIOUS_THICKNESS_AND_BULK_DENSITY, fictitious_thickness, stiffness_matrix_bulk_density]
                for consideration_of_self_weight == 'fictitious thickness and area density'
                    consideration_of_self_weight = [ThicknessStiffnessMatrixSelfWeightDefinitionType.SELF_WEIGHT_DEFINITION_TYPE_DEFINED_VIA_FICTITIOUS_THICKNESS_AND_AREA_DENSITY, stiffness_matrix_bulk_density, stiffness_matrix_area_density]
                for consideration_of_self_weight == 'bulk density and area density'
                    consideration_of_self_weight = [ThicknessStiffnessMatrixSelfWeightDefinitionType.SELF_WEIGHT_DEFINITION_TYPE_DEFINED_VIA_BULK_DENSITY_AND_AREA_DENSITY, fictitious_thickness, stiffness_matrix_area_density]
            coefficient_of_thermal_expansion (float): Coefficient of Thermal Expansion
            stiffness_matrix (list): Nested List of Stiffness Matrix Entries (See Below)
                Element entry overview : [[Bending/Torsional Stiffness Elements (Nm)],
                                            [Shear Stiffness Elements (N/m)],
                                            [Membrane Stiffness Elements (N/m)],
                                            [Eccentric Stiffness Elements (Nm/m)]]
                Detailed element entry : [[D11, D12, D13, D22, D23, D33],
                                            [D44, D45, D55],
                                            [D66, D67, D68, D77, D78, D88],
                                            [D16, D17, D18, D27, D28, D38]]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Thickness
        clientObject = model.clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        if name is not None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Thickness Type
        clientObject.type = ThicknessType.TYPE_STIFFNESS_MATRIX.name

        # Material No.
        clientObject.material = material_no

        # Rotation Beta
        clientObject.orthotropy_rotation_beta = rotation_beta * (pi/180)

        # Consideration of Self-Weight
        clientObject.stiffness_matrix_self_weight_definition_type = consideration_of_self_weight[0].name
        if consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINITION_TYPE_DEFINED_VIA_FICTITIOUS_THICKNESS_AND_BULK_DENSITY':
            clientObject.orthotropy_fictitious_thickness = consideration_of_self_weight[1]
            clientObject.stiffness_matrix_bulk_density = consideration_of_self_weight[2]
        elif consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINITION_TYPE_DEFINED_VIA_FICTITIOUS_THICKNESS_AND_AREA_DENSITY':
            clientObject.orthotropy_fictitious_thickness = consideration_of_self_weight[1]
            clientObject.stiffness_matrix_area_density = consideration_of_self_weight[2]
        elif consideration_of_self_weight[0].name == 'SELF_WEIGHT_DEFINITION_TYPE_DEFINED_VIA_BULK_DENSITY_AND_AREA_DENSITY':
            clientObject.stiffness_matrix_bulk_density = consideration_of_self_weight[1]
            clientObject.stiffness_matrix_area_density = consideration_of_self_weight[2]

        # Coefficient of Thermal Expansion
        clientObject.stiffness_matrix_coefficient_of_thermal_expansion = coefficient_of_thermal_expansion

        # Stiffness Matrix - Bending/Torsional Stiffness Elements
        array_count = []
        for item_length in stiffness_matrix:
            array_count.append(len(item_length))
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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Thickness to client model
        model.clientModel.service.set_thickness(clientObject)

    @staticmethod
    def DeleteThickness(thickness_no: str = '1 2', model = Model):

        '''
        Args:
            thickness_no (str): Numbers of Thickness to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete from client model
        for thickness in ConvertStrToListOfInt(thickness_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_THICKNESS.name, thickness)