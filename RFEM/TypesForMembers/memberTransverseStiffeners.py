from RFEM.initModel import Model, clearAtributes, ConvertToDlString

class MemberTransverseStiffeners():
    def __init__(self,
                 no: int= 1,
                 members: str= "",
                 member_sets: str= "",
                 components= [],
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
            comment (str, optional): Comment
            params (dict, optional): Paramaters
        """

        # Client Model | Member Transverse Stiffeners
        clientObject= model.clientModel.factory.create('ns0:member_transverse_stiffener')

        # Clear Object Atributes | Set All Atributes to None
        clearAtributes(clientObject)

        # Member Transverse Stiffeners No.
        clientObject.no= no

        # Assigned Members
        clientObject.members= ConvertToDlString(members)

        # Assigned Member Sets
        clientObject.member_sets= ConvertToDlString(member_sets)

        # Member Transverse Components
        clientObject.components = Model.clientModel.factory.create('ns0:member_transverse_stiffener.components')

        for i,j in enumerate(components):
            mlvlp = Model.clientModel.factory.create('ns0:member_transverse_stiffener_components')
            mlvlp.no = i+1
            mlvlp.stiffener_type= components[0].name
            mlvlp.position= components[1]
            mlvlp.position_type= components[2].name
            mlvlp.multiple= components[3]
            mlvlp.multiple_number= components[4]
            mlvlp.multiple_offset_definition_type= components[5].name
            mlvlp.multiple_offset= components[6]
            mlvlp.material= components[7]
            mlvlp.consider_stiffener= components[8]
            mlvlp.thickness= components[9]
            mlvlp.width= components[10]
            mlvlp.height= components[11]
            mlvlp.non_rigid= components[12]
            mlvlp.rigid= components[13]
            mlvlp.width_b_u= components[14]
            mlvlp.height_h_u= components[15]
            mlvlp.thickness_t_u= components[16]
            mlvlp.thickness_s_u= components[17]
            mlvlp.width_b= components[18]
            mlvlp.thickness_t= components[19]
            mlvlp.column_section= components[20]
            mlvlp.height_h_m= components[21]
            mlvlp.section= components[22]
            mlvlp.cantilever_l_k= components[23]
            mlvlp.full_warping_restraint= components[24]
            mlvlp.user_defined_restraint= components[25]
            mlvlp.user_defined_restraint_value= components[26]
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