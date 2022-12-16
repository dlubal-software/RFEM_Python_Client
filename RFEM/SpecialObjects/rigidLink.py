from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import RigidLinkType

class RigidLink():
    def __init__(self,
                 no: int = 1,
                 line_1: int = 1,
                 line_2: int = 2,
                 ignore_relative_position: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Rigid Link

        Args:
            no (int): Rigid Link Tag
            line_1 (int): Assigned Line Number
            line_2 (int): Assigned Line Number
            ignore_relative_position (bool): Enable/Disable Ignore Relative Position
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """


        # Client model | Rigid Link
        clientObject = model.clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Type
        #clientObject.type = RigidLinkType.TYPE_LINE_TO_LINE.name

        # Rigid Link No.
        clientObject.no = no

        # Attached lines
        clientObject.line1 = line_1
        clientObject.line2 = line_2

        # Ignore relative possition
        clientObject.ignore_relative_position = ignore_relative_position

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add rigid link to client model
        model.clientModel.service.set_rigid_link(clientObject)

    @staticmethod
    def LineToLine(
                 no: int = 1,
                 line_1: int = 1,
                 line_2: int = 2,
                 ignore_relative_position: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Rigid Link Line to Line

        Args:
            no (int): Rigid Link Tag
            line_1 (int): Assigned Line Number
            line_2 (int): Assigned Line Number
            ignore_relative_position (bool): Enable/Disable Ignore Relative Position
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Line To Line Rigid Link
        clientObject = model.clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Type
        clientObject.type = RigidLinkType.TYPE_LINE_TO_LINE.name

        # Rigid Link No.
        clientObject.no = no

        # Attached lines
        clientObject.line1 = line_1
        clientObject.line2 = line_2

        # Ignore relative possition
        clientObject.ignore_relative_position = ignore_relative_position

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add rigid link to client model
        model.clientModel.service.set_rigid_link(clientObject)

    @staticmethod
    def LineToSurface(
                 no: int = 1,
                 line_1: int = 1,
                 surface: int = 1,
                 ignore_relative_position: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Rigid Link Line to Surface

        Args:
            no (int): Rigid Link Tag
            line_1 (int): Assigned Line Number
            surface (int): Assigned Surface Number
            ignore_relative_position (bool): Enable/Disable Ignore Relative Position
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Line To Surface Rigid Link
        clientObject = model.clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Type
        clientObject.type = RigidLinkType.TYPE_LINE_TO_SURFACE.name

        # Attached lines
        clientObject.line1 = line_1

        clientObject.surface = surface

        # Ignore relative possition
        clientObject.ignore_relative_position = ignore_relative_position

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add rigid link to client model
        model.clientModel.service.set_rigid_link(clientObject)

    @staticmethod
    def Diapragm(
                 no: int = 1,
                 nodes: str = '3 4',
                 lines: str = '6 7',
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Rigid Link Tag
            nodes (str): Assigned Nodes Number
            lines (str): Assigned Lines Number
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Diapragm Rigid Link
        clientObject = model.clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Type
        clientObject.type = RigidLinkType.TYPE_DIAPHRAGM.name

        # Attached nodes
        clientObject.nodes = nodes

        # Attached lines
        clientObject.lines = lines

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add rigid link to client model
        model.clientModel.service.set_rigid_link(clientObject)
