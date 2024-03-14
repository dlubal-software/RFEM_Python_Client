from RFEM.initModel import clearAttributes, deleteEmptyAttributes, Model, ConvertStrToListOfInt
from RFEM.enums import ObjectTypes, MaterialType, MaterialModel, MaterialDefinitionType
from RFEM.enums import MaterialStiffnessModificationType, PoissonRatioEditableGroupType

class Material():
    def __init__(self,
                 no: int = 1,
                 name: str = 'S235',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Material Tag
            name (str): Name of Desired Material (As Named in RFEM Database)
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Material
        clientObject = model.clientModel.factory.create('ns0:material')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Material No.
        clientObject.no = no

        # Material Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add material to client model
        model.clientModel.service.set_material(clientObject)

    @staticmethod
    def UserDefinedMaterial(no: int = 1,
                            name: str = 'S235',
                            material_type = MaterialType.TYPE_CONCRETE,
                            material_model = MaterialModel.MODEL_ISOTROPIC_LINEAR_ELASTIC,
                            elasticity_modulus: float = None,
                            elasticity_modulus_x: float = None,
                            elasticity_modulus_y: float = None,
                            elasticity_modulus_z: float = None,
                            shear_modulus: float = None,
                            shear_modulus_yz: float = None,
                            shear_modulus_xz: float = None,
                            shear_modulus_xy: float = None,
                            poisson_ratio: float = None,
                            poisson_ratio_yz: float = None,
                            poisson_ratio_xz: float = None,
                            poisson_ratio_xy: float = None,
                            poisson_ratio_zy: float = None,
                            poisson_ratio_zx: float = None,
                            poisson_ratio_yx: float = None,
                            poisson_ratio_editable_group_type = PoissonRatioEditableGroupType.POISSON_RATIOS_GROUP_MAJOR_3D,
                            mass_density: float = None,
                            thermal_expansion_coefficient: float = None,
                            thermal_expansion_coefficient_x: float = None,
                            thermal_expansion_coefficient_y: float = None,
                            thermal_expansion_coefficient_z: float = None,
                            definition_type = MaterialDefinitionType.E_G_NU,
                            stiffness_modification_type = MaterialStiffnessModificationType.STIFFNESS_MODIFICATION_TYPE_DIVISION,
                            division_multiplication_factor: float = 1,
                            comment: str = '',
                            params: dict = None,
                            model = Model):

        '''
        Args:
            no (int): Material Tag
            name (str): User Defined Material Name
            material_type (enum): Material Type Enumeration
            material_model (enum): Material Model Enumeration
            elasticity_modulus (float): Elasticity Modulus
            elasticity_modulus_x (float): X-Direction Elasticity Modulus
            elasticity_modulus_y (float): Y-Direction Elasticity Modulus
            elasticity_modulus_z (float): Z-Direction Elasticity Modulus
            shear_modulus (float): Shear Modulus
            shear_modulus_yz (float): YZ-Direction Shear Modulus
            shear_modulus_xz (float): XZ-Direction Shear Modulus
            shear_modulus_xy (float): XY-Direction Shear Modulus
            poisson_ratio (float): Poisson Ratio
            poisson_ratio_yz (float): YZ-Direction Poisson Ratio
            poisson_ratio_xz (float): XZ-Direction Poisson Ratio
            poisson_ratio_xy (float): XY-Direction Poisson Ratio
            poisson_ratio_zy (float): ZY-Direction Poisson Ratio
            poisson_ratio_zx (float): ZX-Direction Poisson Ratio
            poisson_ratio_yx (float): YX-Direction Poisson Ratio
            poisson_ratio_editable_group_type (enum): Poisson Ratio Editable Group Type Enumeration
            mass_density (float): Mass Density
            thermal_expansion_coefficient (float): Thermal Expansion Coefficient
            thermal_expansion_coefficient_x (float): X-Direction Thermal Expansion Coefficient
            thermal_expansion_coefficient_y (float): Y-Direction Thermal Expansion Coefficient
            thermal_expansion_coefficient_z (float): Z-Direction Thermal Expansion Coefficient
            definition_type (enum): Material Definition Type Enumeration
            stiffness_modification_type (enum): Material Stiffness Modification Type Enumeration
            division_multiplication_factor (float): Division Multiplication Factor
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Material
        clientObject = model.clientModel.factory.create('ns0:material')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Material No.
        clientObject.no = no

        clientObject.user_defined = True

        # Material Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Material Type
        clientObject.material_type = material_type.name

        # Material Model
        clientObject.material_model = material_model.name

        # Basic Material Properties
        clientObject.temperature = model.clientModel.factory.create('ns0:material.temperature')

        mbp = model.clientModel.factory.create('ns0:material_temperature_row')
        mbp.no = 1
        mbp.row = model.clientModel.factory.create('ns0:material_temperature')
        clearAttributes(mbp.row)
        mbp.row.poisson_ratio_editable_group_type = poisson_ratio_editable_group_type.name
        mbp.row.elasticity_modulus_global = elasticity_modulus
        mbp.row.elasticity_modulus_y = elasticity_modulus_y
        mbp.row.elasticity_modulus_x = elasticity_modulus_x
        mbp.row.elasticity_modulus_z = elasticity_modulus_z
        mbp.row.shear_modulus_global = shear_modulus
        mbp.row.shear_modulus_yz = shear_modulus_yz
        mbp.row.shear_modulus_xz = shear_modulus_xz
        mbp.row.shear_modulus_xy = shear_modulus_xy
        mbp.row.poisson_ratio_global = poisson_ratio
        mbp.row.poisson_ratio_yz = poisson_ratio_yz
        mbp.row.poisson_ratio_xz = poisson_ratio_xz
        mbp.row.poisson_ratio_xy = poisson_ratio_xy
        mbp.row.poisson_ratio_zy = poisson_ratio_zy
        mbp.row.poisson_ratio_zx = poisson_ratio_zx
        mbp.row.poisson_ratio_yx = poisson_ratio_yx
        mbp.row.mass_density = mass_density
        mbp.row.thermal_expansion_coefficient_global = thermal_expansion_coefficient
        mbp.row.thermal_expansion_coefficient_x = thermal_expansion_coefficient_x
        mbp.row.thermal_expansion_coefficient_y = thermal_expansion_coefficient_y
        mbp.row.thermal_expansion_coefficient_z = thermal_expansion_coefficient_z
        mbp.row.division_multiplication_factor = division_multiplication_factor

        clientObject.temperature.material_temperature.append(mbp)

        # Definition Type
        clientObject.definition_type = definition_type.name

        # Stiffness Modification
        if stiffness_modification_type:
            clientObject.stiffness_modification = True
            clientObject.stiffness_modification_type = stiffness_modification_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add material to client model
        model.clientModel.service.set_material(clientObject)

    @staticmethod
    def DeleteMaterial(materials_no: str = '1 2', model = Model):

        '''
        Args:
            materials_no (str): Numbers of Materials to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete from client model
        for material in ConvertStrToListOfInt(materials_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_MATERIAL.name, material)

    @staticmethod
    def GetMaterial(object_index: int = 1, model = Model):

        '''
        Args:
            obejct_index (int): Material Index
            model (RFEM Class, optional): Model to be edited
        '''

        # Get Material from client model
        return model.clientModel.service.get_material(object_index)
