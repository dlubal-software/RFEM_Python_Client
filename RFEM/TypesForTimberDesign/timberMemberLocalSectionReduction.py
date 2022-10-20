from RFEM.initModel import Model, clearAttributes, ConvertToDlString
from RFEM.enums import TimberMemberLocalSectionReductionType, MultipleOffsetDefinitionType, FastenerDefinitionType

class TimberMemberLocalSectionReduction():

    def __init__(self,
                 no: int = 1,
                 members: str = '1',
                 member_sets: str = '',
                 components: list = [
                    [TimberMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_RECTANGLE_OPENING, 1.0, False,\
                     FastenerDefinitionType.DEFINITION_TYPE_ABSOLUTE, 0.5, 2,\
                     MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 1.0]
                                    ],
                 user_defined_name: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Member Local Section Reduction Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            components (list of lists): Components Table Definition
                components[i][0] (enum): Timber Member Local Section Reduction Type Enumeration
                components[i][1] (float): Position Value
                components[i][2] (bool): Enable/Disable Multiple Option
                components[i][3] (enum): Fastener Definition Type Enumeration
                for components[i][3] == FastenerDefinitionType.DEFINITION_TYPE_ABSOLUTE;
                    components[i][4] (float): Reduction Area
                for components[i][3] == FastenerDefinitionType.DEFINITION_TYPE_RELATIVE;
                    components[i][4] (float): Reduction Area Factor (value must be between 0.0 and 1.0)
                if components[i][2] == True
                    components[i][5] (int): Multiple Number
                    components[i][6] (enum): Multiple Offset Definition Type Enumeration
                    for components[i][6] == MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE;
                        components[i][7] (float): Multiple Offset Value
                    for components[i][6] == MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_RELATIVE;
                        components[i][7] (float): Multiple Offset Value (value must be between 0.0 and 1.0)
            user_defined_name (str): User Defined  Member Local Section Reduction Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Types For Timber Member Local Section Reduction
        clientObject = model.clientModel.factory.create('ns0:timber_member_local_section_reduction')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        #Local Section Reduction No.
        clientObject.no = no

        #Local Section Reduction Assigned Members
        clientObject.members = ConvertToDlString(members)

        #Local Section Reduction Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        #Local Section Reduction User defined Name
        if user_defined_name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = user_defined_name

        #Local Section Reduction Components
        clientObject.components = model.clientModel.factory.create('ns0:array_of_timber_member_local_section_reduction_components')

        for i,j in enumerate(components):
            smlsr = model.clientModel.factory.create('ns0:timber_member_local_section_reduction_components_row')
            smlsr.no = i+1
            smlsr.row.reduction_type = components[i][0].name

            if smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_RECTANGLE_OPENING':
                smlsr.row.position = components[i][1]
                #smlsr.row.definition_type = None # important
                smlsr.row.multiple = components[i][2]
                if smlsr.row.multiple:
                    smlsr.row.multiple_number = components[i][3]
                    smlsr.row.multiple_offset_definition_type = components[i][4].name
                    smlsr.row.multiple_offset = components[i][5]
                else:
                    smlsr.row.multiple_offset_definition_type = None # important
            elif smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_CIRCLE_OPENING':
                smlsr.row.position = components[i][1]
                smlsr.row.z_axis_reference_type = components[i][2].name
                smlsr.row.distance = components[i][3].name
                smlsr.row.diameter = components[i][4].name
                smlsr.row.multiple = components[i][5]
                if smlsr.row.multiple:
                    smlsr.row.multiple_offset_definition_type = components[i][6].name
                    smlsr.row.multiple_number = components[i][7]
                    smlsr.row.multiple_offset = components[i][8]
                else:
                    smlsr.row.multiple_offset_definition_type = None # important
            elif smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_START_NOTCH':
                #smlsr.row.definition_type = None # important
                smlsr.row.length = components[i][1]
                smlsr.row.orientation_type = components[i][2].name
                smlsr.row.depth = components[i][3]
                smlsr.row.direction_type = components[i][4].name
                smlsr.row.stability = components[i][5]
                smlsr.row.multiple = components[i][6]
                smlsr.row.fire_design = components[i][7]
                if smlsr.row.fire_design:
                    smlsr.row.fire_exposure_top = components[i][8]
                    smlsr.row.fire_exposure_left = components[i][9]
                    smlsr.row.fire_exposure_right = components[i][10]
                    smlsr.row.fire_exposure_bottom = components[i][11]
                    smlsr.row.support = components[i][12]
                if smlsr.row.multiple:
                    smlsr.row.multiple_number = components[i][13]
                    smlsr.row.multiple_offset_definition_type = components[i][14].name
                    smlsr.row.multiple_offset = components[i][15]
                else:
                    smlsr.row.multiple_offset_definition_type = None # important
            elif smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_INNER_NOTCH':
                #smlsr.row.definition_type = None # important
                smlsr.row.position = components[i][1]
                smlsr.row.length = components[i][2]
                smlsr.row.orientation_type = components[i][3].name
                smlsr.row.depth = components[i][4]
                smlsr.row.direction_type = components[i][5].name
                smlsr.row.stability = components[i][6]
                smlsr.row.support = components[i][7]
                smlsr.row.multiple = components[i][8]
                smlsr.row.fire_design = components[i][9]
                if smlsr.row.fire_design:
                    smlsr.row.fire_exposure_top = components[i][10]
                    smlsr.row.fire_exposure_left = components[i][11]
                    smlsr.row.fire_exposure_right = components[i][12]
                    smlsr.row.fire_exposure_bottom = components[i][13]
                if smlsr.row.multiple:
                    smlsr.row.multiple_number = components[i][14]
                    smlsr.row.multiple_offset_definition_type = components[i][15].name
                    smlsr.row.multiple_offset = components[i][16]
                else:
                    smlsr.row.multiple_offset_definition_type = None # important
            elif smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_END_NOTCH':
                #smlsr.row.definition_type = None # important
                smlsr.row.length = components[i][1]
                smlsr.row.orientation_type = components[i][2].name
                smlsr.row.depth = components[i][3]
                smlsr.row.direction_type = components[i][4].name
                smlsr.row.stability = components[i][5]
                smlsr.row.support = components[i][6]
                smlsr.row.multiple = components[i][7]
                smlsr.row.fire_design = components[i][8]
                if smlsr.row.fire_design:
                    smlsr.row.fire_exposure_top = components[i][9]
                    smlsr.row.fire_exposure_left = components[i][10]
                    smlsr.row.fire_exposure_right = components[i][11]
                    smlsr.row.fire_exposure_bottom = components[i][12]
                if smlsr.row.multiple:
                    smlsr.row.multiple_number = components[i][13]
                    smlsr.row.multiple_offset_definition_type = components[i][14].name
                    smlsr.row.multiple_offset = components[i][15]
                else:
                    smlsr.row.multiple_offset_definition_type = None # important
            else:
                assert True, 'Unsupported reduction_type'

            clientObject.components.timber_member_local_section_reduction_components.append(smlsr)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        #Add Timber Member Local Section Reduction to Client Model
        model.clientModel.service.set_timber_member_local_section_reduction(clientObject)
