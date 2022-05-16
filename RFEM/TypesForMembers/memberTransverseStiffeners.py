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
            mlvlp = Model.clientModel.factory.create('ns0:member_transverse_stiffener_components')
            mlvlp.no = i+1
            mlvlp.stiffener_type = components[i][0].name
            mlvlp.position = components[i][1]
            mlvlp.position_type = components[i][2].name
            mlvlp.multiple = components[i][3]
            mlvlp.multiple_number = components[i][4]
            mlvlp.multiple_offset_definition_type = components[i][5].name
            mlvlp.multiple_offset = components[i][6]
            mlvlp.material = components[i][7]
            mlvlp.consider_stiffener = components[i][8]
            mlvlp.thickness = components[i][9]
            mlvlp.width = components[i][10]
            mlvlp.height = components[i][11]
            mlvlp.non_rigid = components[i][12]
            mlvlp.rigid = components[i][13]
            mlvlp.width_b_u = components[i][14]
            mlvlp.height_h_u = components[i][15]
            mlvlp.thickness_t_u = components[i][16]
            mlvlp.thickness_s_u = components[i][17]
            mlvlp.width_b = components[i][18]
            mlvlp.thickness_t = components[i][19]
            mlvlp.column_section = components[i][20]
            mlvlp.height_h_m = components[i][21]
            mlvlp.section = components[i][22]
            mlvlp.cantilever_l_k = components[i][23]
            mlvlp.full_warping_restraint = components[i][24]
            mlvlp.user_defined_restraint = components[i][25]
            mlvlp.user_defined_restraint_value = components[i][26]
            mlvlp.note = None

            clientObject.components.member_transverse_stiffener_components.append(mlvlp)

        # Comment
        clientObject.comment= comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key]= params[key]

        # Add Member Definable Stffness to client model
        model.clientModel.service.set_member_transverse_stiffener(clientObject)
