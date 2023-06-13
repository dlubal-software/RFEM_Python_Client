from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import MemberShearPanelDefinitionType, MemberShearPanelFasteningArrangement

class MemberShearPanel():

    def __init__(self) -> None:
        pass

    @staticmethod
    def TrapezodialSheeting(no: int = 1,
                            name: str = '',
                            girder_length_definition: list = [True],
                            sheeting_name: str = 'FI (+) 35/207 - 0.63 (b: 1) | DIN 18807 | Fischer Profil',
                            fastening_arrangement = MemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_RIB,
                            panel_length: float = 2.0,
                            beam_spacing: float = 1.0,
                            coefficient_k1: float = None,
                            coefficient_k2: float = None,
                            comment: str = '',
                            params: dict = None,
                            model = Model):

        """
        Args:
            no (int): Member Shear Panel Tag
            name (str): User Defined Member Shear Panel Name
                if name == '':
                    user_defined_name_enabled = False (Automatic Name Assignment)
                else:
                    user_defined_name_enabled = True
                    name = User Defined Name
            girder_length_definition (list): Girder Length Definition List
                girder_length_definition[0] (bool): Activate/Deactivate Automatically Girder Length
                girder_length_definition[1] (float): Girder Length Value
            sheeting_name (str): Sheeting Name According to Library
            fastening_arrangement (enum): Fastening Arrangement Enumeration
            panel_length (float): Panel Length
            beam_spacing (float): Beam Spacing
            coefficient_k1 (float, optional): Coefficient K1
            coefficient_k2 (float, optional): Coefficient K2
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Member Shear Panel
        clientObject = model.clientModel.factory.create('ns0:member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Definition Type
        clientObject.definition_type = MemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING.name

        # Member Shear Panel User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Shear Panel Girder Length Definition
        if girder_length_definition[0]:
            clientObject.define_girder_length_automatically = True
        else:
            clientObject.define_girder_length_automatically = False
            clientObject.girder_length = girder_length_definition[1]

        # Member Shear Panel Sheeting Name
        clientObject.sheeting_name = sheeting_name

        # Member Shear Panel Fastening Arrangement
        clientObject.fastening_arrangement = fastening_arrangement.name

        # Member Shear Panel Panel Length
        clientObject.panel_length = panel_length

        # Member Shear Panel Beam Spacing
        clientObject.beam_spacing = beam_spacing

        # Member Shear Panel Coefficient K1
        clientObject.coefficient_k1 = coefficient_k1

        # Member Shear Panel Coefficient K2
        clientObject.coefficient_k2 = coefficient_k2

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Shear Panel to client model
        model.clientModel.service.set_member_shear_panel(clientObject)

    @staticmethod
    def Bracing(no: int = 1,
                name: str = '',
                girder_length_definition: list = [True],
                material_name: str = 'S235',
                diagonal_section: str = 'CHC 60.3x4.0',
                posts_section: str = 'CHC 76.1x4.0',
                modulus_of_elasticity: float = None,
                panel_length: float = 2.0,
                beam_spacing: float = 1.0,
                posts_spacing: float = 2.0,
                number_of_bracings: int = 2,
                diagonals_section_area: float = None,
                posts_section_area: float = None,
                comment: str = '',
                params: dict = None,
                model = Model):

        """
        Args:
            no (int): Member Shear Panel Tag
            name (str): User Defined Member Shear Panel Name
                if name == '':
                    user_defined_name_enabled = False (Automatic Name Assignment)
                else:
                    user_defined_name_enabled = True
                    name = User Defined Name
            girder_length_definition (list): Girder Length Definition List
                girder_length_definition[0] (bool): Activate/Deactivate Automatically Girder Length
                girder_length_definition[1] (float): Girder Length Value
            material_name (str): Material Name
            diagonal_section (str): Diagonal Section
            posts_section (str): Posts Section
            modulus_of_elasticity (float, optional): Modulus of Elasticity
            panel_length (float): Panel Length
            beam_spacing (float): Beam Spacing
            posts_spacing (float): Posts Spacing
            number_of_bracings (int): Number of Bracings
            diagonals_section_area (float, optional): Diagonals Section Area
            posts_section_area (float, optional): Posts Section Area
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Member Shear Panel
        clientObject = model.clientModel.factory.create('ns0:member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Definition Type
        clientObject.definition_type = MemberShearPanelDefinitionType.DEFINITION_TYPE_BRACING.name

        # Member Shear Panel User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Shear Panel Girder Length Definition
        if girder_length_definition[0]:
            clientObject.define_girder_length_automatically = True
        else:
            clientObject.define_girder_length_automatically = False
            clientObject.girder_length = girder_length_definition[1]

        # Member Shear Panel Material Name
        clientObject.material_name = material_name

        # Member Shear Panel Diagonal Section
        clientObject.diagonals_section_name = diagonal_section

        # Member Shear Panel Posts Section
        clientObject.posts_section_name = posts_section

        # Member Shear Panel Modulus of Elasticity
        clientObject.modulus_of_elasticity = modulus_of_elasticity

        # Member Shear Panel Panel Length
        clientObject.panel_length = panel_length

        # Member Shear Panel Beam Spacing
        clientObject.beam_spacing = beam_spacing

        # Member Shear Panel Posts Spacing
        clientObject.post_spacing = posts_spacing

        # Member Shear Panel Number of Bracing
        clientObject.number_of_bracings = number_of_bracings

        # Member Shear Panel Diagonals Section Area
        clientObject.diagonals_section_area = diagonals_section_area

        # Member Shear Panel Posts Section Area
        clientObject.posts_section_area = posts_section_area

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Shear Panel to client model
        model.clientModel.service.set_member_shear_panel(clientObject)

    @staticmethod
    def DefineSProv(no: int = 1,
                    name: str = '',
                    girder_length_definition: list = [True],
                    shear_panel_stiffness: float = 1000.0,
                    comment: str = '',
                    params: dict = None,
                    model = Model):

        """
        Args:
            no (int): Member Shear Panel Tag
            name (str): User Defined Member Shear Panel Name
                if name == '':
                    user_defined_name_enabled = False (Automatic Name Assignment)
                else:
                    user_defined_name_enabled = True
                    name = User Defined Name
            girder_length_definition (list): Girder Length Definition List
                girder_length_definition[0] (bool): Activate/Deactivate Automatically Girder Length
                girder_length_definition[1] (float): Girder Length Value
            shear_panel_stiffness (float): Shear Panel Stiffness
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Member Shear Panel
        clientObject = model.clientModel.factory.create('ns0:member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Definition Type
        clientObject.definition_type = MemberShearPanelDefinitionType.DEFINITION_TYPE_DEFINE_S_PROV.name

        # Member Shear Panel User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Shear Panel Stiffness
        clientObject.stiffness = shear_panel_stiffness

        # Member Shear Panel Girder Length Definition
        if girder_length_definition[0]:
            clientObject.define_girder_length_automatically = True
        else:
            clientObject.define_girder_length_automatically = False
            clientObject.girder_length = girder_length_definition[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Shear Panel to client model
        model.clientModel.service.set_member_shear_panel(clientObject)

    @staticmethod
    def TrapeziodalSheetingAndBracing(
                    no: int = 1,
                    name: str = '',
                    sheeting_name: str = 'FI (+) 35/207 - 0.63 (b: 1) | DIN 18807 | Fischer Profil',
                    material_name: str = 'S235',
                    diagonals_section: str = 'CHC 60.3x3.2',
                    posts_section: str = 'CHC 76.1x4.0',
                    fastening_arrangement = MemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_RIB,
                    modulus_of_elasticity: float = None,
                    panel_length: float = 1.0,
                    girder_length_definition: list = [True],
                    beam_spacing: float = 2.0,
                    coefficient_k1: float = None,
                    coefficient_k2: float = None,
                    post_spacing: float = 3.0,
                    number_of_bracing: int = 2,
                    diagonals_section_area: float = None,
                    posts_section_area: float = None,
                    comment: str = '',
                    params: dict = None,
                    model = Model):

        """
        Args:
            no (int): Member Shear Panel Tag
            name (str): User Defined Member Shear Panel Name
                if name == '':
                    user_defined_name_enabled = False (Automatic Name Assignment)
                else:
                    user_defined_name_enabled = True
                    name = User Defined Name
            sheeting_name (str): Sheeting Name According to Library
            material_name (str): Material Name
            diagonals_section (str): Diagonals Section
            posts_section (str): Posts Section
            fastening_arrangement (enum): Fastening Arrangement Enumeration
            modulus_of_elasticity (float, optional): Modulus of Elasticity
            panel_length (float): Panel Length
            girder_length_definition (list): Girder Length Definition List
                girder_length_definition[0] (bool): Activate/Deactivate Automatically Girder Length
                girder_length_definition[1] (float): Girder Length Value
            beam_spacing (float): Beam Spacing
            coefficient_k1 (float, optional): Coefficient K1
            coefficient_k2 (float, optional): Coefficient K2
            post_spacing (float): Posts Spacing
            number_of_bracing (int): Number of Bracings
            diagonals_section_area (float, optional): Diagonals Section Area
            posts_section_area (float, optional): Posts Section Area
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Member Shear Panel
        clientObject = model.clientModel.factory.create('ns0:member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Definition Type
        clientObject.definition_type = MemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING_AND_BRACING.name

        # Member Shear Panel User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Shear Panel Sheeting Name
        clientObject.sheeting_name = sheeting_name

        # Member Shear Panel Material Name
        clientObject.material_name = material_name

        # Member Shear Panel Diagonals Section
        clientObject.diagonals_section_name = diagonals_section

        # Member Shear Panel Posts Section
        clientObject.posts_section_name = posts_section

        # Member Shear Panel Fastening Arrangement
        clientObject.fastening_arrangement = fastening_arrangement.name

        # Member Shear Panel Modulus of Elasticity
        clientObject.modulus_of_elasticity= modulus_of_elasticity

        # Member Shear Panel Panel Length
        clientObject.panel_length = panel_length

        # Member Shear Panel Beam Spacing
        clientObject.beam_spacing = beam_spacing

        # Member Shear Panel Girder Length Definition
        if girder_length_definition[0]:
            clientObject.define_girder_length_automatically = True
        else:
            clientObject.define_girder_length_automatically = False
            clientObject.girder_length = girder_length_definition[1]

        # Member Shear Panel Coefficients
        clientObject.coefficient_k1 = coefficient_k1
        clientObject.coefficient_k2 = coefficient_k2

        # Member Shear Panel Posts Spacings
        clientObject.post_spacing = post_spacing

        # Member Shear Panel Number of Bracing
        clientObject.number_of_bracings = number_of_bracing

        # Member Shear Panel Diagonals Section Area
        clientObject.diagonals_section_area = diagonals_section_area

        # Member Shear Panel Posts Section Area
        clientObject.posts_section_area = posts_section_area

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Shear Panel to client model
        model.clientModel.service.set_member_shear_panel(clientObject)
