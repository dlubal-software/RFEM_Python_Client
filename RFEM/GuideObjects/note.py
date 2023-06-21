from RFEM.enums import NoteType, NoteOffsetType
from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes

class Note():

    def __init__(self,
                 no: int = 1,
                 text: str = None,
                 type = NoteType.NOTE_TYPE_POINT,
                 parameter: list = None,
                 offset_para: list = None,
                 rotation: float = 0.0,
                 display_style: int = 0,
                 name: str = None,
                 show_comment: bool = False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Note Tag
            text (str): Note Text
            type (enum): Note Type Enumeration
            parameter (int or list): Note Type Parameter
                for type == NoteType.NOTE_TYPE_POINT:
                    parameter = [point_coordinate_x, point_coordinate_y, point_coordinate_z]
                for type == NoteType.NOTE_TYPE_NODE:
                    parameter = node number
                for type == NoteType.NOTE_TYPE_LINE:
                    parameter = [line number, note_member_reference_type enumeration, member_distance_is_defined_as_relative(bool), member_distance_relative/absolute] (if relative is true than value must be between 0.0 and 1.0)
                for type == NoteType.NOTE_TYPE_MEMBER:
                    parameter = [member number, note_member_reference_type enumeration, member_distance_is_defined_as_relative(bool), member_distance_relative/absolute] (if relative is true than value must be between 0.0 and 1.0)
                for type == NoteType.NOTE_TYPE_SURFACE:
                    parameter = [surface number, note_surface_reference_type enumeration, surface_first_coordinate, surface_second_coordinate]
            offset_para (list): Offset Parameter
                for offset_para[0] == NoteOffsetType.OFFSET_TYPE_XYZ:
                    offset_para = [offset_coordinate_x, offset_coordinate_y, offset_coordinate_z]
                for offset_para[0] == NoteOffsetType.OFFSET_TYPE_XY:
                    offset_para = [offset_coordinate_x, offset_coordinate_y]
                for offset_para[0] == NoteOffsetType.OFFSET_TYPE_XZ:
                    offset_para = [offset_coordinate_x, offset_coordinate_z]
                for offset_para[0] == NoteOffsetType.OFFSET_TYPE_YZ:
                    offset_para = [offset_coordinate_y, offset_coordinate_z]
            rotation (float): Note Display Rotation
            display_style (int): Note Display Style Tag (Value must be from 0 to 4)
            name (str): User Defined Name
            show_comment (bool): Enable/disable Show Comment
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:note')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Note No.
        clientObject.no = no

        # Text
        clientObject.text = text

        # Note type
        clientObject.type = type.name

        # For Note Type Point
        if type == NoteType.NOTE_TYPE_POINT:
            clientObject.point_coordinate_x = parameter[0]
            clientObject.point_coordinate_y = parameter[1]
            clientObject.point_coordinate_z = parameter[2]

        # For Note Type Node
        elif type == NoteType.NOTE_TYPE_NODE:
            clientObject.node = parameter

        # For Note Type Line
        elif type == NoteType.NOTE_TYPE_LINE:
            clientObject.line = parameter[0]
            clientObject.member_reference_type = parameter[1].name
            clientObject.member_distance_is_defined_as_relative = parameter[2]

            if parameter[2]:
                clientObject.member_distance_relative = parameter[3]
            else:
                clientObject.member_distance_absolute = parameter[3]

        # For Note Type Member
        elif type == NoteType.NOTE_TYPE_MEMBER:
            clientObject.member = parameter[0]
            clientObject.member_reference_type = parameter[1].name
            clientObject.member_distance_is_defined_as_relative = parameter[2]

            if parameter[2]:
                clientObject.member_distance_relative = parameter[3]
            else:
                clientObject.member_distance_absolute = parameter[3]

        # For Note Type Surface
        elif type == NoteType.NOTE_TYPE_SURFACE:
            clientObject.surface = parameter[0]
            clientObject.surface_reference_type = parameter[1].name
            clientObject.surface_first_coordinate = parameter[2]
            clientObject.surface_second_coordinate = parameter[3]

        # offset of Note

        if offset_para:
            clientObject.offset = True
            clientObject.offset_type = offset_para[0].name

            if offset_para[0] == NoteOffsetType.OFFSET_TYPE_XYZ:
                clientObject.offset_coordinate_x = offset_para[1]
                clientObject.offset_coordinate_y = offset_para[2]
                clientObject.offset_coordinate_z = offset_para[3]

            elif offset_para[0] == NoteOffsetType.OFFSET_TYPE_XY:
                clientObject.offset_coordinate_x = offset_para[1]
                clientObject.offset_coordinate_y = offset_para[2]

            elif offset_para[0] == NoteOffsetType.OFFSET_TYPE_XZ:
                clientObject.offset_coordinate_x = offset_para[1]
                clientObject.offset_coordinate_z = offset_para[2]

            elif offset_para[0] == NoteOffsetType.OFFSET_TYPE_YZ:
                clientObject.offset_coordinate_y = offset_para[1]
                clientObject.offset_coordinate_z = offset_para[2]

        clientObject.rotation = rotation

        clientObject.show_comment = show_comment
        clientObject.display_properties_index = display_style

        # Note User Defined Name
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

        # Add Note to client model
        model.clientModel.service.set_note(clientObject)
