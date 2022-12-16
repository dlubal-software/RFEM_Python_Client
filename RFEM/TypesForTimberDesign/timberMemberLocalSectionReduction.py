from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import TimberMemberLocalSectionReductionType, MultipleOffsetDefinitionType, ZAxisReferenceType, OrientationType, DirectionType

class Components():
    def __init__(self,
                reduction_type: TimberMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_RECTANGLE_OPENING):
        '''
        Args:
            reduction_type (Enum): Timber Member Local Section Reduction Type Enum
        '''
        self.reduction_type = reduction_type.name
        if self.reduction_type == 'REDUCTION_COMPONENT_TYPE_RECTANGLE_OPENING':
            self.position = 1
            self.width = 0.5
            self.height = 0.5
            self.z_axis_reference_type = ZAxisReferenceType.E_POSITION_REFERENCE_CENTER.name
            self.distance = 0.01
            self.multiple = True
            self.multiple_number = 2
            self.multiple_offset_definition_type = MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE.name
            self.multiple_offset = 1
        elif self.reduction_type == 'REDUCTION_COMPONENT_TYPE_CIRCLE_OPENING':
            self.position = 1
            self.z_axis_reference_type = ZAxisReferenceType.E_POSITION_REFERENCE_TOP.name
            self.distance = 0.01
            self.diameter = 0.05
            self.multiple = True
            self.multiple_offset_definition_type = MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE.name
            self.multiple_number = 2
            self.multiple_offset = 2
        elif self.reduction_type == 'REDUCTION_COMPONENT_TYPE_START_NOTCH':
            self.length = 0.2
            self.orientation_type = OrientationType.E_ORIENTATION_DEPTH.name
            self.depth = 0.001
            self.width = None
            self.direction_type = DirectionType.E_DIRECTION_DEPTH_POSITIVE.name
            self.stability = True
            self.multiple = False
            self.fire_design = True
            self.fire_exposure_top = True
            self.fire_exposure_left = True
            self.fire_exposure_right = True
            self.fire_exposure_bottom = True
            self.support = True
        elif self.reduction_type == 'REDUCTION_COMPONENT_TYPE_INNER_NOTCH':
            self.position = 0.2
            self.length = 0.3
            self.orientation_type = OrientationType.E_ORIENTATION_DEPTH.name
            self.depth = 0.004
            self.direction_type = DirectionType.E_DIRECTION_DEPTH_POSITIVE.name
            self.stability = True
            self.multiple = True
            self.multiple_number = 2
            self.multiple_offset_definition_type = MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE.name
            self.multiple_offset = 2
            self.fire_design = True
            self.fire_exposure_top = True
            self.fire_exposure_left = True
            self.fire_exposure_right = True
            self.fire_exposure_bottom = True
        elif self.reduction_type == 'REDUCTION_COMPONENT_TYPE_END_NOTCH':
            self.length = 0.3
            self.orientation_type = OrientationType.E_ORIENTATION_DEPTH.name
            self.depth = 0.02
            self.direction_type = DirectionType.E_DIRECTION_DEPTH_POSITIVE.name
            self.stability = True
            self.support = True
            self.multiple = False
            self.fire_design = True
            self.fire_exposure_top = True
            self.fire_exposure_left = True
            self.fire_exposure_right = True
            self.fire_exposure_bottom = True
        else:
            assert True, 'Unsupported reduction_type'

class TimberMemberLocalSectionReduction():
    def __init__(self,
                 no: int = 1,
                 members: str = '1',
                 member_sets: str = '',
                 components: list = None,
                 user_defined_name: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Member Local Section Reduction Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            components (list): List of Component classes
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
            clearAttributes(smlsr.row)

            smlsr.no = i+1
            smlsr.row.reduction_type = components[i].reduction_type
            if smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_RECTANGLE_OPENING':
                smlsr.row.position = components[i].position
                smlsr.row.width = components[i].width
                smlsr.row.height = components[i].height
                smlsr.row.z_axis_reference_type = components[i].z_axis_reference_type
                smlsr.row.distance = components[i].distance
                smlsr.row.multiple = components[i].multiple
                if smlsr.row.multiple:
                    smlsr.row.multiple_number = components[i].multiple_number
                    smlsr.row.multiple_offset_definition_type = components[i].multiple_offset_definition_type
                    smlsr.row.multiple_offset = components[i].multiple_offset
            elif smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_CIRCLE_OPENING':
                smlsr.row.position = 1
                smlsr.row.z_axis_reference_type = components[i].z_axis_reference_type
                smlsr.row.distance = components[i].distance
                smlsr.row.diameter = components[i].diameter
                smlsr.row.multiple = components[i].multiple
                if smlsr.row.multiple:
                    smlsr.row.multiple_offset_definition_type = components[i].multiple_offset_definition_type
                    smlsr.row.multiple_number = components[i].multiple_number
                    smlsr.row.multiple_offset = components[i].multiple_offset
            elif smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_START_NOTCH':
                smlsr.row.length = components[i].length
                smlsr.row.orientation_type = components[i].orientation_type
                smlsr.row.depth = components[i].depth
                smlsr.row.direction_type = components[i].direction_type
                smlsr.row.stability = components[i].stability
                smlsr.row.multiple = components[i].multiple
                smlsr.row.fire_design = components[i].fire_design
                smlsr.row.support = components[i].support
                if smlsr.row.fire_design:
                    smlsr.row.fire_exposure_top = components[i].fire_exposure_top
                    smlsr.row.fire_exposure_left = components[i].fire_exposure_left
                    smlsr.row.fire_exposure_right = components[i].fire_exposure_right
                    smlsr.row.fire_exposure_bottom = components[i].fire_exposure_bottom
                if smlsr.row.multiple:
                    smlsr.row.multiple_number = components[i].multiple_number
                    smlsr.row.multiple_offset_definition_type = components[i].multiple_offset_definition_type
                    smlsr.row.multiple_offset = components[i].multiple_offset
            elif smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_INNER_NOTCH':
                smlsr.row.position = components[i].position
                smlsr.row.length = components[i].length
                smlsr.row.orientation_type = components[i].orientation_type
                smlsr.row.depth = components[i].depth
                smlsr.row.direction_type = components[i].direction_type
                smlsr.row.stability = components[i].stability
                smlsr.row.multiple = components[i].multiple
                smlsr.row.fire_design = components[i].fire_design
                if smlsr.row.fire_design:
                    smlsr.row.fire_exposure_top = components[i].fire_exposure_top
                    smlsr.row.fire_exposure_left = components[i].fire_exposure_left
                    smlsr.row.fire_exposure_right = components[i].fire_exposure_right
                    smlsr.row.fire_exposure_bottom = components[i].fire_exposure_bottom
                if smlsr.row.multiple:
                    smlsr.row.multiple_number = components[i].multiple_number
                    smlsr.row.multiple_offset_definition_type = components[i].multiple_offset_definition_type
                    smlsr.row.multiple_offset = components[i].multiple_offset
            elif smlsr.row.reduction_type == 'REDUCTION_COMPONENT_TYPE_END_NOTCH':
                smlsr.row.length = components[i].length
                smlsr.row.orientation_type = components[i].orientation_type
                smlsr.row.depth = components[i].depth
                smlsr.row.direction_type = components[i].direction_type
                smlsr.row.stability = components[i].stability
                smlsr.row.support = components[i].support
                smlsr.row.multiple = components[i].multiple
                smlsr.row.fire_design = components[i].fire_design
                if smlsr.row.fire_design:
                    smlsr.row.fire_exposure_top = components[i].fire_exposure_top
                    smlsr.row.fire_exposure_left = components[i].fire_exposure_left
                    smlsr.row.fire_exposure_right = components[i].fire_exposure_right
                    smlsr.row.fire_exposure_bottom = components[i].fire_exposure_bottom
            else:
                assert True, 'Unsupported reduction_type'

            clientObject.components.timber_member_local_section_reduction_components.append(smlsr)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Timber Member Local Section Reduction to Client Model
        model.clientModel.service.set_timber_member_local_section_reduction(clientObject)
