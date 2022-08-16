from http import client
from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import *

class SteelMemberShearPanel():
    def __init__(self,
                no: int = 1,
                user_defined_name: list = [False],
                definition_type = SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING,
                members: str = "",
                member_sets: str = "",
                categories = [SteelMemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE, "FI (+) 35/207 - 0.63 (b: 1) | DIN 18807 | Fischer Profil", SteelMemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_RIB],
                parameters = [1, 2, 0.000247, 0.01043],
                comment: str = '',
                params: dict = None):
        """
        Args:
            no (int): Steel Member Shear Panel Tag
            user_defined_name (list): User Defined Member Shear Panel Name
                for user_defined_name[0] == False:
                    pass
                for user_defined_name == True:
                    user_defined_name[1] = Defined Name
            definition_type (enum): Steel Member Shear Panel Definition Type Enumeration
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            categories (list): Positional Categories LIst
                for definition_type == SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING:
                    categories[0] = Section Position Enumeration Type
                    categories[1] = Sheeting Name
                    categories[2] = Fastening Arrangment Enumeration Type
                for definition_type == SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_BRACING:
                    categories[0] = Section Position Enumeration Type
                    categories[1] = Diagonal Section Name
                    categories[2] = Post Section Name
                for definition_type == SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING_AND_BRACING:
                    categories[0] = Section Position Enumeration Type
                    categories[1] = Sheeting Name
                    categories[2] = Digonal Section Name
                    categories[3] = Post Section Name
                    categories[4] = Fastening Arrangment Enumeration Type
                for definition_type == SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_DEFINE_S_PROV:
                    categories[0] = Section Position Enumeration Type
            parameters (list): Positional Parameters List
                for definition_type == SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING:
                    parameters[0] = Panel Length
                    parameters[1] = Beam Spacing
                    parameters[2] = K1 Coefficient
                    parameters[3] = K2 Coefficient
                    if categories[0] == "POSITION_DEFINE":
                        parameters[4] = Position on Section Value
                for definition_type == SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_BRACING:
                    parameters[0] = Panel Length
                    parameters[1] = Beam Spacing
                    parameters[2] = Post Spacing
                    parameters[3] = Number of Bracings
                    parameters[4] = Diagonals Section Area
                    parameters[5] = Post Section Area
                    if categories[0] == "POSITION_DEFINE":
                        parameters[6] = Position on Section Value
                for definition_type == SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING_AND_BRACING:
                    parameters[0] = Panel Length
                    parameters[1] = Beam Spacing
                    parameters[2] = K1 Coefficient
                    parameters[3] = K2 Coefficient
                    parameters[4] = Post Spacing
                    parameters[5] = Number of Bracing
                    parameters[6] = Diagonals Section Area
                    parameters[7] = Post Section Area
                    if categories[0] == "POSITION_DEFINE":
                        parameters[8] = Position on Section Value
                for definition_type == SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_DEFINE_S_PROV:
                    parameters[0] = Stifness
                    if categories[0] == "POSITION_DEFINE":
                        parameters[1] = Position on Section Value
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        """

         # Client Model | Types For Steel Design Member Shear Panel
        clientObject = Model.clientModel.factory.create('ns0:steel_member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Member Shear Panel Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Shear Panel User Defined Name
        if user_defined_name[0]:
            clientObject.user_defined_name_enabled = user_defined_name[0]
            clientObject.name = user_defined_name[1]
        else:
            clientObject.user_defined_name_enabled = user_defined_name[0]

        # Member Shear Panel Definition Type
        clientObject.definition_type = definition_type.name

        # Member Shear Panel Categories
        if definition_type.name == "DEFINITION_TYPE_TRAPEZOIDAL_SHEETING":
            clientObject.position_on_section = categories[0].name
            clientObject.sheeting_name = categories[1]
            clientObject.fastening_arrangement = categories[2].name

        elif definition_type.name == "DEFINITION_TYPE_BRACING":
            clientObject.position_on_section = categories[0].name
            clientObject.diagonals_section_name = categories[1]
            clientObject.posts_section_name = categories[2]

        elif definition_type.name == "DEFINITION_TYPE_TRAPEZOIDAL_SHEETING_AND_BRACING":
            clientObject.position_on_section = categories[0].name
            clientObject.sheeting_name = categories[1]
            clientObject.diagonals_section_name = categories[2]
            clientObject.posts_section_name = categories[3]
            clientObject.fastening_arrangement = categories[4].name

        elif definition_type.name == "DEFINITION_TYPE_DEFINE_S_PROV":
            clientObject.position_on_section = categories[0].name

        # Member Shear Panel Parameters
        if definition_type.name == "DEFINITION_TYPE_TRAPEZOIDAL_SHEETING":
            clientObject.panel_length = parameters[0]
            clientObject.beam_spacing = parameters[1]
            clientObject.coefficient_k1 = parameters[2]
            clientObject.coefficient_k2 = parameters[3]

            if categories[0].name == "POSITION_DEFINE":
                clientObject.position_on_section_value = parameters[4]

        elif definition_type.name == "DEFINITION_TYPE_BRACING":
            clientObject.panel_length = parameters[0]
            clientObject.beam_spacing = parameters[1]
            clientObject.post_spacing = parameters[2]
            clientObject.number_of_bracings = parameters[3]
            clientObject.diagonals_section_area = parameters[4]
            clientObject.posts_section_area = parameters[5]

            if categories[0].name == "POSITION_DEFINE":
                clientObject.position_on_section_value = parameters[6]

        elif definition_type.name == "DEFINITION_TYPE_TRAPEZOIDAL_SHEETING_AND_BRACING":
            clientObject.panel_length = parameters[0]
            clientObject.beam_spacing = parameters[1]
            clientObject.coefficient_k1 = parameters[2]
            clientObject.coefficient_k2 = parameters[3]
            clientObject.post_spacing = parameters[4]
            clientObject.number_of_bracings = parameters[5]
            clientObject.diagonals_section_area = parameters[6]
            clientObject.posts_section_area = parameters[7]

            if categories[0].name == "POSITION_DEFINE":
                clientObject.position_on_section_value = parameters[8]

        elif definition_type.name == "DEFINITION_TYPE_DEFINE_S_PROV":
            clientObject.stiffness = parameters[0]

            if categories[0].name == "POSITION_DEFINE":
                clientObject.position_on_section_value = parameters[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Steel Effective Lengths to client model
        Model.clientModel.service.set_steel_member_shear_panel(clientObject)

