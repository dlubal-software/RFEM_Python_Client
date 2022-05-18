from RFEM.initModel import Model, clearAtributes, ConvertToDlString

class MemberTransverseStiffeners():
    def __init__(self,
                 no: int= 1,
                 members: str= "",
                 member_sets: str= "",
                 components= None,
                 comment: str= '',
                 params: dict= None,
                 model= Model):
        """
        Args:
            no (int): Member Transverse Stiffener Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            components (list): [
            [stiffener_type, position, position_type, multiple, multiple_number, multiple_offset_definition_type, multiple_offset, material,
            consider_stiffener, thickness, width, height, non_rigid, rigid, width_b_u, height_h_u, thickness_t_u,
            thickness_s_u, width_b, thickness_t, column_section, height_h_m, section,
            cantilever_l_k, full_warping_restraint, user_defined_restraint, user_defined_restraint_value]
                               ]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        """

        # Client Model | Member Transverse Stiffeners
        clientObject= model.clientModel.factory.create('ns0:member_transverse_stiffener')

        # Clear Object Atributes | Set All Atributes to None
        clearAtributes(clientObject)

        # Member Transverse Stiffeners No.
        clientObject.no = no

        # Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Transverse Components
        clientObject.components = Model.clientModel.factory.create('ns0:member_transverse_stiffener.components')

        for i,j in enumerate(components):
            mlvlp = Model.clientModel.factory.create('ns0:member_transverse_stiffener_components_row')
            mlvlp.no = i+1
            mlvlp.row.stiffener_type = components[i][0].name
            mlvlp.row.position = components[i][1]
            mlvlp.row.position_type = components[i][2].name
            mlvlp.row.multiple = components[i][3]
            mlvlp.row.multiple_number = components[i][4]
            mlvlp.row.multiple_offset_definition_type = components[i][5].name
            mlvlp.row.multiple_offset = components[i][6]
            mlvlp.row.material = components[i][7]
            mlvlp.row.consider_stiffener = components[i][8]
            mlvlp.row.thickness = components[i][9]
            mlvlp.row.width = components[i][10]
            mlvlp.row.height = components[i][11]
            mlvlp.row.non_rigid = components[i][12]
            mlvlp.row.rigid = components[i][13]
            mlvlp.row.width_b_u = components[i][14]
            mlvlp.row.height_h_u = components[i][15]
            mlvlp.row.thickness_t_u = components[i][16]
            mlvlp.row.thickness_s_u = components[i][17]
            mlvlp.row.width_b = components[i][18]
            mlvlp.row.thickness_t = components[i][19]
            mlvlp.row.column_section = components[i][20]
            mlvlp.row.height_h_m = components[i][21]
            mlvlp.row.section = components[i][22]
            mlvlp.row.cantilever_l_k = components[i][23]
            mlvlp.row.full_warping_restraint = components[i][24]
            mlvlp.row.user_defined_restraint = components[i][25]
            mlvlp.row.user_defined_restraint_value = components[i][26]
            mlvlp.row.note = None

            clientObject.components.member_transverse_stiffener_components.append(mlvlp)

        # Comment
        clientObject.comment= comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key]= params[key]

        # Add Member Definable Stffness to client model
        model.clientModel.service.set_member_transverse_stiffener(clientObject)
