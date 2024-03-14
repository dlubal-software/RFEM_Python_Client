from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import CoordinateSystemType, CoordinateSystemRotationAnglesSequence

class CoordinateSystem():
    def __init__(self,
                 no: int = 1,
                 origin_coordinate_x: float = 0.0,
                 origin_coordinate_y: float = 0.0,
                 origin_coordinate_z: float = 0.0,
                 name: str = 'Coord1',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Coordinate System Tag
            origin_coordinate_x (float): X-Coordinate
            origin_coordinate_y (float): Y-Coordinate
            origin_coordinate_z (float): Z-Coordinate
            name (str, optional): User Defined Coordinate System Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Coordinate System
        clientObject = model.clientModel.factory.create('ns0:coordinate_system')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Coordinate System No.
        clientObject.no = no

        # Coordinate System Type
        clientObject.type = CoordinateSystemType.TYPE_OFFSET_XYZ.name

        # Coordinates
        clientObject.origin_coordinate_x = origin_coordinate_x
        clientObject.origin_coordinate_y = origin_coordinate_y
        clientObject.origin_coordinate_z = origin_coordinate_z

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Coordinate System to client model
        model.clientModel.service.set_coordinate_system(clientObject)

    @staticmethod
    def OffsetXYZ(no: int = 1,
                  origin_coordinate_x: float = 0.0,
                  origin_coordinate_y: float = 0.0,
                  origin_coordinate_z: float = 0.0,
                  name: str = '',
                  comment: str = '',
                  params: dict = None,
                  model = Model):

        '''
         Args:
            no (int): Coordinate System Tag
            origin_coordinate_x (float): X-Coordinate
            origin_coordinate_y (float): Y-Coordinate
            origin_coordinate_z (float): Z-Coordinate
            name (str, optional): User Defined Coordinate System Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Coordinate System
        clientObject = model.clientModel.factory.create('ns0:coordinate_system')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Coordinate System No.
        clientObject.no = no

        # Coordinate System Type
        clientObject.type = CoordinateSystemType.TYPE_OFFSET_XYZ.name

        # Coordinates
        clientObject.origin_coordinate_x = origin_coordinate_x
        clientObject.origin_coordinate_y = origin_coordinate_y
        clientObject.origin_coordinate_z = origin_coordinate_z

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Coordinate System to client model
        model.clientModel.service.set_coordinate_system(clientObject)

    @staticmethod
    def ThreePoints(no: int = 1,
                    origin_coordinate_x: float = 1.0,
                    origin_coordinate_y: float = 0.0,
                    origin_coordinate_z: float = 0.0,
                    u_axis_point_coordinate_x: float = 0.0,
                    u_axis_point_coordinate_y: float = 1.0,
                    u_axis_point_coordinate_z: float = 0.0,
                    uw_plane_point_coordinate_x: float = 0.0,
                    uw_plane_point_coordinate_y: float = 0.0,
                    uw_plane_point_coordinate_z: float = 1.0,
                    name: str = '',
                    comment: str = '',
                    params: dict = None,
                    model = Model):

        '''
         Args:
            no (int): Coordinate System Tag
            origin_coordinate_x (float): Origin Point X-Coordinate
            origin_coordinate_y (float): Origin Point Y-Coordinate
            origin_coordinate_z (float): Origin Point Z-Coordinate
            u_axis_point_coordinate_x (float): Point on +U-Axis - 1st point X-Coordinate
            u_axis_point_coordinate_y (float): Point on +U-Axis - 1st point Y-Coordinate
            u_axis_point_coordinate_z (float): Point on +U-Axis - 1st point Z-Coordinate
            uw_plane_point_coordinate_x (float): Point in +UW-Plane - 2nd Point X-Coordinate
            uw_plane_point_coordinate_y (float): Point in +UW-Plane - 2nd Point Y-Coordinate
            uw_plane_point_coordinate_z (float): Point in +UW-Plane - 2nd Point Z-Coordinate
            name (str, optional): User Defined Coordinate System Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Coordinate System
        clientObject = model.clientModel.factory.create('ns0:coordinate_system')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Coordinate System No.
        clientObject.no = no

        # Coordinate System Type
        clientObject.type = CoordinateSystemType.TYPE_3_POINTS.name

        # Coordinates
        clientObject.origin_coordinate_x = origin_coordinate_x
        clientObject.origin_coordinate_y = origin_coordinate_y
        clientObject.origin_coordinate_z = origin_coordinate_z

        clientObject.u_axis_point_coordinate_x = u_axis_point_coordinate_x
        clientObject.u_axis_point_coordinate_y = u_axis_point_coordinate_y
        clientObject.u_axis_point_coordinate_z = u_axis_point_coordinate_z

        clientObject.uw_plane_point_coordinate_x = uw_plane_point_coordinate_x
        clientObject.uw_plane_point_coordinate_y = uw_plane_point_coordinate_y
        clientObject.uw_plane_point_coordinate_z = uw_plane_point_coordinate_z

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Coordinate System to client model
        model.clientModel.service.set_coordinate_system(clientObject)

    @staticmethod
    def TwoPointsAndAngle(no: int = 1,
                          origin_coordinate_x: float = 1.0,
                          origin_coordinate_y: float = 0.0,
                          origin_coordinate_z: float = 0.0,
                          u_axis_point_coordinate_x: float = 0.0,
                          u_axis_point_coordinate_y: float = 0.0,
                          u_axis_point_coordinate_z: float = 0.0,
                          uw_plane_angle: float = 0.0,
                          name: str = '',
                          comment: str = '',
                          params: dict = None,
                          model = Model):

        '''
         Args:
            no (int): Coordinate System Tag
            origin_coordinate_x (float): Origin Point X-Coordinate
            origin_coordinate_y (float): Origin Point Y-Coordinate
            origin_coordinate_z (float): Origin Point Z-Coordinate
            u_axis_point_coordinate_x (float): Point on +U-Axis - 1st point X-Coordinate
            u_axis_point_coordinate_y (float): Point on +U-Axis - 1st point Y-Coordinate
            u_axis_point_coordinate_z (float): Point on +U-Axis - 1st point Z-Coordinate
            uw_plane_angle (float): Rotation About U-Axis
            name (str, optional): User Defined Coordinate System Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Coordinate System
        clientObject = model.clientModel.factory.create('ns0:coordinate_system')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Coordinate System No.
        clientObject.no = no

        # Coordinate System Type
        clientObject.type = CoordinateSystemType.TYPE_2_POINTS_AND_ANGLE.name

        # Coordinates
        clientObject.origin_coordinate_x = origin_coordinate_x
        clientObject.origin_coordinate_y = origin_coordinate_y
        clientObject.origin_coordinate_z = origin_coordinate_z

        clientObject.u_axis_point_coordinate_x = u_axis_point_coordinate_x
        clientObject.u_axis_point_coordinate_y = u_axis_point_coordinate_y
        clientObject.u_axis_point_coordinate_z = u_axis_point_coordinate_z

        clientObject.uw_plane_angle = uw_plane_angle

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Coordinate System to client model
        model.clientModel.service.set_coordinate_system(clientObject)

    @staticmethod
    def PointAndThreeAngles(no: int = 1,
                            origin_coordinate_x: float = 1.0,
                            origin_coordinate_y: float = 2.0,
                            origin_coordinate_z: float = 3.0,
                            rotation_angles_sequence: float = CoordinateSystemRotationAnglesSequence.SEQUENCE_XYZ,
                            rotation_angle_1: float = 0.0,
                            rotation_angle_2: float = 0.0,
                            rotation_angle_3: float = 0.0,
                            name: str = '',
                            comment: str = '',
                            params: dict = None,
                            model = Model):

        '''
         Args:
            no (int): Coordinate System Tag
            origin_coordinate_x (float): Origin Point X-Coordinate
            origin_coordinate_y (float): Origin Point Y-Coordinate
            origin_coordinate_z (float): Origin Point Z-Coordinate
            rotation_angles_sequence (enum): Coordinate System Rotation Angles Sequence Enumeration
            rotation_angle_1 (float): Rotation about X Axes
            rotation_angle_2 (float): Rotation about Y Axes
            rotation_angle_3 (float): Rotation about Z Axes
            name (str, optional): User Defined Coordinate System Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Coordinate System
        clientObject = model.clientModel.factory.create('ns0:coordinate_system')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Coordinate System No.
        clientObject.no = no

        # Coordinate System Type
        clientObject.type = CoordinateSystemType.TYPE_POINT_AND_3_ANGLES.name

        # Coordinates
        clientObject.origin_coordinate_x = origin_coordinate_x
        clientObject.origin_coordinate_y = origin_coordinate_y
        clientObject.origin_coordinate_z = origin_coordinate_z

        # Rotation Angles
        clientObject.rotation_angles_sequence = rotation_angles_sequence.name

        clientObject.rotation_angle_1 = rotation_angle_1
        clientObject.rotation_angle_2 = rotation_angle_2
        clientObject.rotation_angle_3 = rotation_angle_3

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Coordinate System to client model
        model.clientModel.service.set_coordinate_system(clientObject)

    @staticmethod
    def GetCoordinateSystem(object_index: int = 1, model = Model):

        '''
        Args:
            obejct_index (int): Coordinate System Index
            model (RFEM Class, optional): Model to be edited
        '''

        # Get Coordinate System from client model
        return model.clientModel.service.get_coordinate_system(object_index)
