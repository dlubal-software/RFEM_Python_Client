# TODO maybe rename this file to "complexTypes.py" as it is reffered to in WSDL
class BaseComplexType:
    """
    Base class for special objects, each of this object needs to be represented as dict, so it can be used in RFEM API.
    Therefore we need to implement toDict method, so this base class is here to avoid code duplication with the class inheritance.
    Each new object should inherit from this class.
    """
    def toDict(self):
        return self.__dict__

class DxfFileModelObject(BaseComplexType):
    def __init__(self,
        no = None, # int
        origin_coordinates = None, # xsd:vector_3d
        origin_coordinate_x = None, # double
        origin_coordinate_y = None, # double
        origin_coordinate_z = None, # double
        rotation_angles_sequence = None, # xsd:Dxf_file_model_object_rotation_angles_sequence
        rotation_angle_1 = None, # double
        rotation_angle_2 = None, # double
        rotation_angle_3 = None, # double
        user_defined_name_enabled = None, # boolean
        name = None, # string
        file_path = None, # string
        file_name = None, # string
        coordinate_system = None, # int
        insert_point = None, # xsd:Dxf_file_model_object_insert_point
        scale_is_nonuniform = None, # boolean
        scale_is_defined_as_relative = None, # boolean
        scale_relative = None, # double
        scale_absolute = None, # double
        scale_relative_x = None, # double
        scale_relative_y = None, # double
        scale_relative_z = None, # double
        scale_absolute_x = None, # double
        scale_absolute_y = None, # double
        scale_absolute_z = None, # double
        comment = None, # string
        is_generated = None, # boolean
        generating_object_info = None, # string
        id_for_export_import = None, # string
        metadata_for_export_import = None # string
    ):
        self.no = no
        self.origin_coordinates = origin_coordinates
        self.origin_coordinate_x = origin_coordinate_x
        self.origin_coordinate_y = origin_coordinate_y
        self.origin_coordinate_z = origin_coordinate_z
        self.rotation_angles_sequence = rotation_angles_sequence
        self.rotation_angle_1 = rotation_angle_1
        self.rotation_angle_2 = rotation_angle_2
        self.rotation_angle_3 = rotation_angle_3
        self.user_defined_name_enabled = user_defined_name_enabled
        self.name = name
        self.file_path = file_path
        self.file_name = file_name
        self.coordinate_system = coordinate_system
        self.insert_point = insert_point
        self.scale_is_nonuniform = scale_is_nonuniform
        self.scale_is_defined_as_relative = scale_is_defined_as_relative
        self.scale_relative = scale_relative
        self.scale_absolute = scale_absolute
        self.scale_relative_x = scale_relative_x
        self.scale_relative_y = scale_relative_y
        self.scale_relative_z = scale_relative_z
        self.scale_absolute_x = scale_absolute_x
        self.scale_absolute_y = scale_absolute_y
        self.scale_absolute_z = scale_absolute_z
        self.comment = comment
        self.is_generated = is_generated
        self.generating_object_info = generating_object_info
        self.id_for_export_import = id_for_export_import
        self.metadata_for_export_import = metadata_for_export_import

class BuildingStory(BaseComplexType):
    def __init__(self,
        no = None, # int
        type = None, # xsd:building_story_type
        user_defined_name_enabled = None, # boolean
        name = None, # string
        story_no = None, # int
        elevation = None, # double
        bottom_elevation = None, # double
        height = None, # double
        modified_height = None, # double
        thickness = None, # double
        info = None, # xsd:array_of_building_story_info_and_child_items
        comment = None, # string
        total_info = None, # xsd:array_of_building_story_total_info_and_child_items
        modify_geometry_type = None, # xsd:building_story_modify_geometry_type
        thickness_type = None, # xsd:building_story_thickness_type
        slab_stiffness_type = None, # xsd:building_story_slab_stiffness_type
        create_result_sections = None, # boolean
        floor_stiffness_type = None, # xsd:building_story_floor_stiffness_type
        vertical_result_line_active = None, # boolean
        vertical_result_line_position_x = None, # double
        vertical_result_line_position_y = None, # double
        vertical_result_line_relative = None, # boolean
        vertical_result_line_relative_position_x = None, # double
        vertical_result_line_relative_position_y = None, # double
        mass = None, # double
        center_of_gravity_x = None, # double
        center_of_gravity_y = None, # double
        id_for_export_import = None, # string
        metadata_for_export_import = None # string
    ):
        self.no = no
        self.type = type
        self.user_defined_name_enabled = user_defined_name_enabled
        self.name = name
        self.story_no = story_no
        self.elevation = elevation
        self.bottom_elevation = bottom_elevation
        self.height = height
        self.modified_height = modified_height
        self.thickness = thickness
        self.info = info
        self.comment = comment
        self.total_info = total_info
        self.modify_geometry_type = modify_geometry_type
        self.thickness_type = thickness_type
        self.slab_stiffness_type = slab_stiffness_type
        self.create_result_sections = create_result_sections
        self.floor_stiffness_type = floor_stiffness_type
        self.vertical_result_line_active = vertical_result_line_active
        self.vertical_result_line_position_x = vertical_result_line_position_x
        self.vertical_result_line_position_y = vertical_result_line_position_y
        self.vertical_result_line_relative = vertical_result_line_relative
        self.vertical_result_line_relative_position_x = vertical_result_line_relative_position_x
        self.vertical_result_line_relative_position_y = vertical_result_line_relative_position_y
        self.mass = mass
        self.center_of_gravity_x = center_of_gravity_x
        self.center_of_gravity_y = center_of_gravity_y
        self.id_for_export_import = id_for_export_import
        self.metadata_for_export_import = metadata_for_export_import
