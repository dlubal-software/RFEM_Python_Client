class BaseObject:
    def toDict(self):
        return self.__dict__

class DxfFileModelObject(BaseObject):
    def __init__(
        self,
        no = None,
        origin_coordinate_x = None,
        origin_coordinate_y = None,
        origin_coordinate_z = None,
        rotation_angles_sequence = {'value': None}, # TODO maybe it is different object
        rotation_angle_1 = None,
        rotation_angle_2 = None,
        rotation_angle_3 = None,
        user_defined_name_enabled = None,
        name = None,
        filename = None,
        coordinate_system = None,
        insert_point = {'value' : None},
        scale_is_nonuniform = None,
        scale_is_defined_as_relative = None,
        scale_relative = None,
        scale_absolute = None,
        scale_relative_x = None,
        scale_relative_y = None,
        scale_relative_z = None,
        scale_absolute_x = None,
        scale_absolute_y = None,
        scale_absolute_z = None
    ):
        self.no = no
        self.origin_coordinate_x = origin_coordinate_x
        self.origin_coordinate_y = origin_coordinate_y
        self.origin_coordinate_z = origin_coordinate_z
        self.rotation_angles_sequence = rotation_angles_sequence
        self.rotation_angle_1 = rotation_angle_1
        self.rotation_angle_2 = rotation_angle_2
        self.rotation_angle_3 = rotation_angle_3
        self.user_defined_name_enabled = user_defined_name_enabled
        self.name = name
        self.filename = filename
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
