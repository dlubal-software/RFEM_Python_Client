from RFEM.initModel import Model, clearAtributes
from enum import Enum

class Modification_Type(Enum):
    MULTIPLY_FACTOR, DIVISION_FACTOR = range(2)
class MemberHingeSide(Enum):
    Start, End = range(2)

class StructureModification():
    material_item = {'no': 1, 'material_name': 1, 'modification_type': 'MULTIPLY_FACTOR', 'E_and_G': 1.0, 'comment': ''}
    section_item = {'no': 1, 'section_name': 'IPN 300', 'A': 1.0, 'A_y':1.0, 'A_z': 1.0, 'J': 1.0, 'I_y': 1.0, 'I_z': 1.0}
    member_item = {}
    surface_item = {}
    member_hinge_item = {'no': 1, 'member_side': 'Start', 'C_u_x': 0, 'C_u_y': 0, 'C_u_z': 0, 'C_phi_x': 0, 'C_phi_y': 0, 'C_phi_z': 0}
    line_hinge_item = {'no': 1, 'C_u_x': 1, 'C_u_y': 1, 'C_u_z': 1, 'C_phi_x': 0, 'C_phi_y': 0, 'C_phi_z': 0}

    def __init__(self,
                 no: int = 1,
                 modify_stiffnesses_materials: bool = False,
                 modify_stiffnesses_sections: bool = False,
                 modify_stiffnesses_members: bool = False,
                 modify_stiffnesses_surfaces: bool = False,
                 modify_stiffnesses_member_hinges: bool = False,
                 modify_stiffnesses_nodal_supports: bool = False,
                 modify_stiffness_timber_members_due_moisture_class: bool = False,
                 nonlinearities_disabled_material_nonlinearity_models: bool = False,
                 nonlinearities_disabled_solid_types_contact_or_surfaces_contact: bool = False,
                 modify_stiffnesses_materials_list: list = None,
                 modify_stiffnesses_sections_list: list = None,
                 modify_stiffnesses_members_list: list = None,
                 modify_stiffnesses_surfaces_list: list = None,
                 modify_stiffnesses_member_hinges_list: list = None,
                 modify_stiffnesses_nodal_supports_list: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Structural Modification

        Args:
            no (int, mandatory): _description_. Defaults to 1.
            modify_stiffnesses_materials (bool, optional): Material
            modify_stiffnesses_sections (bool, optional): _description_. Defaults to False.
            modify_stiffnesses_members (bool, optional): _description_. Defaults to False.
            modify_stiffnesses_surfaces (bool, optional): _description_. Defaults to False.
            modify_stiffnesses_member_hinges (bool, optional): _description_. Defaults to False.
            modify_stiffnesses_nodal_supports (bool, optional): _description_. Defaults to False.
            modify_stiffness_timber_members_due_moisture_class (bool, optional): _description_. Defaults to False.
            nonlinearities_disabled_material_nonlinearity_models (bool, optional): _description_. Defaults to False.
            nonlinearities_disabled_solid_types_contact_or_surfaces_contact (bool, optional): _description_. Defaults to False.
            modify_stiffnesses_materials_list (list, optional): _description_. Defaults to None.
            modify_stiffnesses_sections_list (list, optional): _description_. Defaults to None.
            modify_stiffnesses_members_list (list, optional): _description_. Defaults to None.
            modify_stiffnesses_surfaces_list (list, optional): _description_. Defaults to None.
            modify_stiffnesses_member_hinges_list (list, optional): _description_. Defaults to None.
            modify_stiffnesses_nodal_supports_list (list, optional): _description_. Defaults to None.
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (class, optional): Model instance
        """

        # Client model | Structure Modification
        clientObject = model.clientModel.factory.create('ns0:structure_modification')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Structure Modification No.
        clientObject.no = no

        # Modify Stiffneesses
        clientObject.modify_stiffnesses_materials = modify_stiffnesses_materials
        clientObject.modify_stiffnesses_sections = modify_stiffnesses_sections
        clientObject.modify_stiffnesses_members = modify_stiffnesses_members
        clientObject.modify_stiffnesses_surface = modify_stiffnesses_surfaces
        clientObject.modify_stiffnesses_member_hinges = modify_stiffnesses_member_hinges
        clientObject.modify_stiffnesses_nodal_supports = modify_stiffnesses_nodal_supports
        clientObject.modify_stiffness_timber_members_due_moisture_class = modify_stiffness_timber_members_due_moisture_class
        clientObject.nonlinearities_disabled_material_nonlinearity_models = nonlinearities_disabled_material_nonlinearity_models
        clientObject.nonlinearities_disabled_solid_types_contact_or_surfaces_contact = nonlinearities_disabled_solid_types_contact_or_surfaces_contact

        # Modify Stiffneesses Tables
        clientObject.modify_stiffnesses_material_table = modify_stiffnesses_materials_list
        clientObject.modify_stiffnesses_sections_table = modify_stiffnesses_sections_list
        clientObject.modify_stiffnesses_members_table = modify_stiffnesses_members_list
        clientObject.modify_stiffnesses_surfaces_table = modify_stiffnesses_surfaces_list
        clientObject.modify_stiffnesses_member_hinges_table = modify_stiffnesses_member_hinges_list
        clientObject.modify_stiffnesses_nodal_supports_table = modify_stiffnesses_nodal_supports_list

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Structure Modification to client model
        model.clientModel.service.set_structure_modification(clientObject)
