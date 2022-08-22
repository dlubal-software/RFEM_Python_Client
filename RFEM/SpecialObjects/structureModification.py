from RFEM.initModel import Model, clearAtributes

class StructureModification():
    material_item = {'no': 1, 'material_name': 1, 'modification_type': 'DIVISION_FACTOR', 'E_and_G': 1.5, 'comment': 'comment'}
    section_item = {'no': 1, 'section_name': 'IPN 300', 'A': 1.0, 'A_y':1.0, 'A_z': 1.0, 'J': 1.0, 'I_y': 1.0, 'I_z': 1.0}
    member_item = {'no': 2, 'member_modification': 1, 'members':'11', 'comment': ''}
    surface_item = {'no': 1, 'surface_modification': 1, 'surfaces':'2', 'comment': ''}
    member_hinge_item = {'no': 1, 'member_side': 'Start', 'C_u_x': 1, 'C_u_y': 0, 'C_u_z': 0, 'C_phi_x': 0, 'C_phi_y': 0, 'C_phi_z': 0}
    line_hinge_item = {'no': 1, 'C_u_x': 1, 'C_u_y': 0, 'C_u_z': 0, 'C_phi_x': 0, 'C_phi_y': 0, 'C_phi_z': 0}
    nodal_support_item = {'C_u_X': 1, 'C_u_Y': 0, 'C_u_Z': 0, 'C_phi_X': 0, 'C_phi_Y': 0, 'C_phi_Z': 0}
    line_support_item = {'C_u_X': 1, 'C_u_Y': 0, 'C_u_Z': 0, 'C_phi_X': 0, 'C_phi_Y': 0, 'C_phi_Z': 0}
    member_support_item = {'C_u_x': 1, 'C_u_y': 0, 'C_u_z': 0, 'C_s_x': 0, 'C_s_y': 0, 'C_s_z': 0, 'C_phi_x': 0}
    surface_support_item = {'C_u_X': 1, 'C_u_Y': 0, 'C_u_Z': 0, 'C_v_xz': 0, 'C_v_yz': 0}
    modify_stiffness = {'modify_stiffnesses_gamma_m': False,
                        'modify_stiffnesses_materials': False,
                        'modify_stiffnesses_sections': False,
                        'modify_stiffnesses_members': False,
                        'modify_stiffnesses_surfaces': False,
                        'modify_stiffnesses_member_hinges': False,
                        'modify_stiffnesses_line_hinges': False,
                        'modify_stiffnesses_nodal_supports': False,
                        'modify_stiffnesses_line_supports': False,
                        'modify_stiffnesses_member_supports': False,
                        'modify_stiffnesses_surface_supports': False,
                        'modify_stiffness_member_reinforcement': False,
                        'modify_stiffness_surface_reinforcement': False,
                        'modify_stiffness_timber_members_due_moisture_class': False,
                        'nonlinearities_disabled_material_nonlinearity_models': False,
                        'nonlinearities_disabled_material_temperature_nonlinearities': False,
                        'nonlinearities_disabled_line_hinges': False,
                        'nonlinearities_disabled_member_types': False,
                        'nonlinearities_disabled_member_nonlinearities': False,
                        'nonlinearities_disabled_solid_types_contact_or_surfaces_contact': False,
                        'nonlinearities_disabled_member_hinges': False,
                        'nonlinearities_disabled_nodal_supports': False,
                        'nonlinearities_disabled_line_supports': False,
                        'nonlinearities_disabled_member_supports': False,
                        'nonlinearities_disabled_surface_supports': False,
                        'deactivate_members_enabled': False}

    def __init__(self,
                 no: int = 1,
                 modify_stiffnesses: dict = modify_stiffness,
                 modify_stiffnesses_materials_list: list = None,
                 modify_stiffnesses_sections_list: list = None,
                 modify_stiffnesses_members_list: list = None,
                 modify_stiffnesses_surfaces_list: list = None,
                 modify_stiffnesses_member_hinges_list: list = None,
                 modify_stiffnesses_line_hinges_list: list = None,
                 modify_stiffnesses_nodal_supports_list: list = None,
                 modify_stiffnesses_line_supports_list: list = None,
                 modify_stiffnesses_member_supports_list: list = None,
                 modify_stiffnesses_surface_supports_list: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Structural Modification
        Modify only objects allready existing and used/assigned in the model.

        Args:
            no (int, optional): Structure Modification Tag
            modify_stiffnesses (dict, optional): Modify Stiffnesses
            modify_stiffnesses_materials_list (list, optional): Modify Stiffnesses Materials List
            modify_stiffnesses_sections_list (list, optional): Modify Stiffnesses Sections List
            modify_stiffnesses_members_list (list, optional): Modify Stiffnesses Members List
            modify_stiffnesses_surfaces_list (list, optional): Modify Stiffnesses Surfaces List
            modify_stiffnesses_member_hinges_list (list, optional): Modify Stiffnesses Member Hinges List
            modify_stiffnesses_line_hinges_list (list, optional): Modify Stiffnesses Line Hinges List
            modify_stiffnesses_nodal_supports_list (list, optional): Modify Stiffnesses Nodal Supports List
            modify_stiffnesses_line_supports_list (list, optional): Modify Stiffnesses Line Support List
            modify_stiffnesses_member_supports_list (list, optional): Modify Stiffnesses Member Suppoorts List
            modify_stiffnesses_surface_supports_list (list, optional): Modify Stiffnesses Surface Supports List
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Structure Modification
        clientObject = None
        try:
            clientObject = model.clientModel.service.get_structure_modification(no)
        except:
            clientObject = model.clientModel.factory.create('ns0:structure_modification')

            # Clears object atributes | Sets all atributes to None
            clearAtributes(clientObject)

            # Structure Modification No.
            clientObject.no = no

            # Modify Stiffneesses
            clientObject.modify_stiffnesses_gamma_m = modify_stiffnesses['modify_stiffnesses_gamma_m']
            clientObject.modify_stiffnesses_materials = modify_stiffnesses['modify_stiffnesses_materials']
            clientObject.modify_stiffnesses_sections = modify_stiffnesses['modify_stiffnesses_sections']
            clientObject.modify_stiffnesses_members = modify_stiffnesses['modify_stiffnesses_members']
            clientObject.modify_stiffnesses_surfaces = modify_stiffnesses['modify_stiffnesses_surfaces']
            clientObject.modify_stiffnesses_member_hinges = modify_stiffnesses['modify_stiffnesses_member_hinges']
            clientObject.modify_stiffnesses_line_hinges = modify_stiffnesses['modify_stiffnesses_line_hinges']
            clientObject.modify_stiffnesses_nodal_supports = modify_stiffnesses['modify_stiffnesses_nodal_supports']
            clientObject.modify_stiffnesses_line_supports = modify_stiffnesses['modify_stiffnesses_line_supports']
            clientObject.modify_stiffnesses_member_supports = modify_stiffnesses['modify_stiffnesses_member_supports']
            clientObject.modify_stiffnesses_surface_supports = modify_stiffnesses['modify_stiffnesses_surface_supports']
            clientObject.modify_stiffness_member_reinforcement = modify_stiffnesses['modify_stiffness_member_reinforcement']
            clientObject.modify_stiffness_surface_reinforcement = modify_stiffnesses['modify_stiffness_surface_reinforcement']
            clientObject.modify_stiffness_timber_members_due_moisture_class = modify_stiffnesses['modify_stiffness_timber_members_due_moisture_class']
            clientObject.nonlinearities_disabled_material_nonlinearity_models = modify_stiffnesses['nonlinearities_disabled_material_nonlinearity_models']
            clientObject.nonlinearities_disabled_material_temperature_nonlinearities = modify_stiffnesses['nonlinearities_disabled_material_temperature_nonlinearities']
            clientObject.nonlinearities_disabled_line_hinges = modify_stiffnesses['nonlinearities_disabled_line_hinges']
            clientObject.nonlinearities_disabled_member_types = modify_stiffnesses['nonlinearities_disabled_member_types']
            clientObject.nonlinearities_disabled_member_nonlinearities = modify_stiffnesses['nonlinearities_disabled_member_nonlinearities']
            clientObject.nonlinearities_disabled_solid_types_contact_or_surfaces_contact = modify_stiffnesses['nonlinearities_disabled_solid_types_contact_or_surfaces_contact']
            clientObject.nonlinearities_disabled_member_hinges = modify_stiffnesses['nonlinearities_disabled_member_hinges']
            clientObject.nonlinearities_disabled_nodal_supports = modify_stiffnesses['nonlinearities_disabled_nodal_supports']
            clientObject.nonlinearities_disabled_line_supports = modify_stiffnesses['nonlinearities_disabled_line_supports']
            clientObject.nonlinearities_disabled_member_supports = modify_stiffnesses['nonlinearities_disabled_member_supports']
            clientObject.nonlinearities_disabled_surface_supports = modify_stiffnesses['nonlinearities_disabled_surface_supports']
            clientObject.deactivate_members_enabled = modify_stiffnesses['deactivate_members_enabled']

            model.clientModel.service.set_structure_modification(clientObject)
            clientObject = model.clientModel.service.get_structure_modification(no)

        # Modify Stiffneesses Tables
        if modify_stiffnesses['modify_stiffnesses_materials']:
            for i in modify_stiffnesses_materials_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_material_table[0][idx].row.modification_type = i['modification_type']
                clientObject.modify_stiffnesses_material_table[0][idx].row.E_and_G = i['E_and_G']
                clientObject.modify_stiffnesses_material_table[0][idx].row.comment = i['comment']
        if modify_stiffnesses['modify_stiffnesses_sections']:
            for i in modify_stiffnesses_sections_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_sections_table[0][idx].row.A = i['A']
                clientObject.modify_stiffnesses_sections_table[0][idx].row.A_y = i['A_y']
                clientObject.modify_stiffnesses_sections_table[0][idx].row.A_z = i['A_z']
                clientObject.modify_stiffnesses_sections_table[0][idx].row.J = i['J']
                clientObject.modify_stiffnesses_sections_table[0][idx].row.I_Y = i['I_y']
                clientObject.modify_stiffnesses_sections_table[0][idx].row.I_z = i['I_z']
        if modify_stiffnesses['modify_stiffnesses_members']:
            for i in modify_stiffnesses_members_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_members_table[0][idx].row.member_modification = i['member_modification']
                clientObject.modify_stiffnesses_members_table[0][idx].row.members = i['members']
                clientObject.modify_stiffnesses_members_table[0][idx].row.comment = i['comment']
        if modify_stiffnesses['modify_stiffnesses_surfaces']:
            for i in modify_stiffnesses_surfaces_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_surfaces_table[0][idx].row.surface_modification = i['surface_modification']
                clientObject.modify_stiffnesses_surfaces_table[0][idx].row.surfaces = i['surfaces']
                clientObject.modify_stiffnesses_surfaces_table[0][idx].row.comment = i['comment']
        if modify_stiffnesses['modify_stiffnesses_member_hinges']:
            for i in modify_stiffnesses_member_hinges_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_member_hinges_table[0][idx].row.member_side = i['member_side']
                clientObject.modify_stiffnesses_member_hinges_table[0][idx].row.C_u_x = i['C_u_x']
                clientObject.modify_stiffnesses_member_hinges_table[0][idx].row.C_u_y = i['C_u_y']
                clientObject.modify_stiffnesses_member_hinges_table[0][idx].row.C_u_z = i['C_u_z']
                clientObject.modify_stiffnesses_member_hinges_table[0][idx].row.C_phi_x = i['C_phi_x']
                clientObject.modify_stiffnesses_member_hinges_table[0][idx].row.C_phi_y = i['C_phi_y']
                clientObject.modify_stiffnesses_member_hinges_table[0][idx].row.C_phi_z = i['C_phi_z']
        if modify_stiffnesses['modify_stiffnesses_line_hinges']:
            for i in modify_stiffnesses_line_hinges_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_line_hinges_table[0][idx].row.C_u_x = i['C_u_x']
                clientObject.modify_stiffnesses_line_hinges_table[0][idx].row.C_u_y = i['C_u_y']
                clientObject.modify_stiffnesses_line_hinges_table[0][idx].row.C_u_z = i['C_u_z']
                clientObject.modify_stiffnesses_line_hinges_table[0][idx].row.C_phi_x = i['C_phi_x']
                clientObject.modify_stiffnesses_line_hinges_table[0][idx].row.C_phi_y = i['C_phi_y']
                clientObject.modify_stiffnesses_line_hinges_table[0][idx].row.C_phi_z = i['C_phi_z']
        if modify_stiffnesses['modify_stiffnesses_nodal_supports']:
            for i in modify_stiffnesses_nodal_supports_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_nodal_supports_table[0][idx].row.C_u_x = i['C_u_x']
                clientObject.modify_stiffnesses_nodal_supports_table[0][idx].row.C_u_y = i['C_u_y']
                clientObject.modify_stiffnesses_nodal_supports_table[0][idx].row.C_u_z = i['C_u_z']
                clientObject.modify_stiffnesses_nodal_supports_table[0][idx].row.C_phi_x = i['C_phi_x']
                clientObject.modify_stiffnesses_nodal_supports_table[0][idx].row.C_phi_y = i['C_phi_y']
                clientObject.modify_stiffnesses_nodal_supports_table[0][idx].row.C_phi_z = i['C_phi_z']
        if modify_stiffnesses['modify_stiffnesses_line_supports']:
            for i in modify_stiffnesses_line_supports_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_line_supports_table[0][idx].row.C_u_X = i['C_u_X']
                clientObject.modify_stiffnesses_line_supports_table[0][idx].row.C_u_Y = i['C_u_Y']
                clientObject.modify_stiffnesses_line_supports_table[0][idx].row.C_u_Z = i['C_u_Z']
                clientObject.modify_stiffnesses_line_supports_table[0][idx].row.C_phi_X = i['C_phi_X']
                clientObject.modify_stiffnesses_line_supports_table[0][idx].row.C_phi_Y = i['C_phi_Y']
                clientObject.modify_stiffnesses_line_supports_table[0][idx].row.C_phi_Z = i['C_phi_Z']
        if modify_stiffnesses['modify_stiffnesses_member_supports']:
            for i in modify_stiffnesses_member_supports_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_member_supports_table[0][idx].row.C_u_x = i['C_u_x']
                clientObject.modify_stiffnesses_member_supports_table[0][idx].row.C_u_y = i['C_u_y']
                clientObject.modify_stiffnesses_member_supports_table[0][idx].row.C_u_z = i['C_u_z']
                clientObject.modify_stiffnesses_member_supports_table[0][idx].row.C_s_x = i['C_s_x']
                clientObject.modify_stiffnesses_member_supports_table[0][idx].row.C_s_y = i['C_s_y']
                clientObject.modify_stiffnesses_member_supports_table[0][idx].row.C_s_z = i['C_s_z']
                clientObject.modify_stiffnesses_member_supports_table[0][idx].row.C_phi_x = i['C_phi_x']
        if modify_stiffnesses['modify_stiffnesses_surface_supports']:
            for i in modify_stiffnesses_surface_supports_list:
                idx = i['no']-1
                clientObject.modify_stiffnesses_surface_supports_table[0][idx].row.C_u_X = i['C_u_X']
                clientObject.modify_stiffnesses_surface_supports_table[0][idx].row.C_u_Y = i['C_u_Y']
                clientObject.modify_stiffnesses_surface_supports_table[0][idx].row.C_u_Z = i['C_u_Z']
                clientObject.modify_stiffnesses_surface_supports_table[0][idx].row.C_v_xz = i['C_v_xz']
                clientObject.modify_stiffnesses_surface_supports_table[0][idx].row.C_v_yz = i['C_v_yz']

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Structure Modification to client model
        model.clientModel.service.set_structure_modification(clientObject)
