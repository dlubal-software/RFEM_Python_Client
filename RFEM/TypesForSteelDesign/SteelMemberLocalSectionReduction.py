#SteelMemberLocalSectionReduction

from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import SteelMemberLocalSectionReductionType, MultipleOffsetDefinitionType, FastenerDefinitionType

class SteelMemberLocalSectionReduction():

    def __init__(self,
                 no: int = 1,
                 members: str = '1',
                 member_sets: str = '',
                 components: list = [
                    [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 0.0, False, 0, \
                     MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 0.0, FastenerDefinitionType.DEFINITION_TYPE_ABSOLUTE, 0.0]
                                    ],
                 user_defined_name: list = [False],
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Member Local Section Reduction Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            components (list of lists): Components Table Definition
                components[i][0] (enum): Steel Member Local Section Reduction Type Enumeration
                components[i][1] (float): Position Value
                components[i][2] (bool): Enable/Disable Multiple Option
                if components[i][2] == True
                    components[i][3] (int): Multiple Number
                    components[i][4] (enum): Multiple Offset Definition Type Enumeration
                    components[i][5] (float): Multiple Offset Value
                components[i][6] (enum): Fastener Definition Type Enumeration
                components[i][7] (float): Reduction Area
            user_defined_name (list): User Defined  Member Local Section Reduction Name
                for user_defined_name[0] == False:
                    pass
                for user_defined_name == True:
                    user_defined_name[1] = Defined Name
            comment (str): Comments
            params (dict): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Types For Steel Member Local Section Reduction
        clientObject = model.clientModel.factory.create('ns0:steel_member_local_section_reduction')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        #Local Section Reduction No.
        clientObject.no = no

        #Local Section Reduction Assigned Members
        clientObject.members = ConvertToDlString(members)

        #Local Section Reduction Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        #Local Section Reduction User defined Name
        if user_defined_name[0] == False:
            clientObject.user_defined_name_enabled = user_defined_name[0]
        else:
            clientObject.user_defined_name_enabled = user_defined_name[0]
            clientObject.name = user_defined_name[1]

        #Local Section Reduction Components
        clientObject.components = model.clientModel.factory.create('ns0:steel_member_local_section_reduction.components')

        for i,j in enumerate(components):
            smlsr = model.clientModel.factory.create('ns0:steel_member_local_section_reduction_components_row')
            smlsr.no = i
            smlsr.row.reduction_type = components[i][0].name
            smlsr.row.position = components[i][1]
            smlsr.row.multiple = components[i][2]
            if smlsr.row.multiple == True:
                smlsr.row.multiple_number = components[i][3]
                smlsr.row.multiple_offset_definition_type = components[i][4].name
                smlsr.row.multiple_offset = components[i][5]
            smlsr.row.fastener_definition_type = components[i][6].name
            smlsr.row.reduction_area = components[i][7]

            clientObject.components.steel_member_local_section_reduction_components.append(smlsr)
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        #Add Steel Member Local Section Reduction to Client Model
        model.clientModel.service.set_steel_member_local_section_reduction(clientObject)
