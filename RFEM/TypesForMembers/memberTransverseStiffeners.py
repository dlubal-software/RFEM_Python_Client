from RFEM.initModel import Model, clearAtributes, ConvertToDlString, GetAddonStatus, SetAddonStatus
from RFEM.enums import MemberTransverseStiffenerType, MemberTransverseStiffenerPosition, MemberTransverseStiffenerOffsetType, MemberTransverseStiffenerDefinitionType, AddOn

class MemberTransverseStiffeners():

    # Member Transverse Component
    component = {'no' : 1,
                 'cantilever_l_c' : 0,
                 'stiffener_type' : MemberTransverseStiffenerType.STIFFENER_COMPONENT_TYPE_FLAT,
                 'position' : 1,
                 'position_type' : MemberTransverseStiffenerPosition.STIFFENER_COMPONENT_POSITION_DOUBLE_SIDED,
                 'multiple' : False,
                 'multiple_number' : 0,
                 'definition_type' : MemberTransverseStiffenerDefinitionType.DIMENSION_TYPE_OFFSET,
                 'multiple_offset_definition_type' : MemberTransverseStiffenerOffsetType.OFFSET_DEFINITION_TYPE_ABSOLUTE,
                 'multiple_offset' : 0,
                 'material' : 1,
                 'consider_stiffener' : True,
                 'thickness' : 0.005,
                 'width' : 0.02,
                 'height' : 0,
                 'non_rigid' : False,
                 'rigid' : False,
                 'width_b_u' : 0,
                 'height_h_u' : 0,
                 'thickness_t_u' : 0,
                 'thickness_s_u' : 0,
                 'width_b' : 0,
                 'thickness_t' : 0,
                 'column_section' : 0,
                 'section' : 0,
                 'full_warping_restraint' : False,
                 'user_defined_restraint' : False,
                 'user_defined_restraint_value' : 0,
                 'note' : 'comment'
            }

    def __init__(self,
                 no: int = 1,
                 members: str = "",
                 member_sets: str = "",
                 components: list = [component],
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Member Transverse Stiffener Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            components (list of components): List of components dictionary
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Check if Steel Design Add-on is ON.
        SetAddonStatus(model.clientModel, AddOn.steel_design_active)

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

        for i in components:
            mlvlp = Model.clientModel.factory.create('ns0:member_transverse_stiffener_components_row')
            mlvlp.no = i['no']
            mlvlp.row.stiffener_type = i['stiffener_type'].name
            mlvlp.row.position = i['position']
            mlvlp.row.position_type = i['position_type'].name
            mlvlp.row.multiple = i['multiple']
            mlvlp.row.multiple_number = i['multiple_number']
            mlvlp.row.multiple_offset_definition_type = i['multiple_offset_definition_type'].name
            mlvlp.row.multiple_offset = i['multiple_offset']
            mlvlp.row.material = i['material']
            mlvlp.row.consider_stiffener = i['consider_stiffener']
            mlvlp.row.thickness = i['thickness']
            mlvlp.row.width = i['width']
            mlvlp.row.height = i['height']
            mlvlp.row.non_rigid = i['non_rigid']
            mlvlp.row.rigid = i['rigid']
            mlvlp.row.width_b_u = i['width_b_u']
            mlvlp.row.height_h_u = i['height_h_u']
            mlvlp.row.thickness_t_u = i['thickness_t_u']
            mlvlp.row.thickness_s_u = i['thickness_s_u']
            mlvlp.row.width_b = i['width_b']
            mlvlp.row.thickness_t = i['thickness_t']
            mlvlp.row.column_section = i['column_section']
            mlvlp.row.section = i['section']
            mlvlp.row.full_warping_restraint = i['full_warping_restraint']
            mlvlp.row.user_defined_restraint = i['user_defined_restraint']
            mlvlp.row.user_defined_restraint_value = i['user_defined_restraint_value']
            mlvlp.row.note = i['note']
            mlvlp.row.cantilever_l_c = i['cantilever_l_c']
            mlvlp.row.definition_type = i['definition_type'].name

            clientObject.components.member_transverse_stiffener_components.append(mlvlp)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key]= params[key]

        # Add Member Definable Stffness to client model
        model.clientModel.service.set_member_transverse_stiffener(clientObject)
