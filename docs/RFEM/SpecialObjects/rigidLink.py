from RFEM.initModel import Model, clearAttributes
from RFEM.enums import *

class RigidLink():
    def __init__(self,
                 no: int = 1,
                 line_1: int = 1,
                 line_2: int = 2,
                 ignore_relative_position: bool = True,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Rigid Link
        clientObject = Model.clientModel.factory.create('ns0:rigid_link')

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
        for key in params:
            clientObject[key] = params[key]

        # Add rigid link to client model
        Model.clientModel.service.set_rigid_link(clientObject)

    def LineToLine(self,
                 no: int = 1,
                 line_1: int = 1,
                 line_2: int = 2,
                 ignore_relative_position: bool = True,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line To Line Rigid Link
        clientObject = Model.clientModel.factory.create('ns0:rigid_link')

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
        for key in params:
            clientObject[key] = params[key]

        # Add rigid link to client model
        Model.clientModel.service.set_rigid_link(clientObject)

    def LineToSurface(self,
                 no: int = 1,
                 line_1: int = 1,
                 surface: int = 1,
                 ignore_relative_position: bool = True,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line To Surface Rigid Link
        clientObject = Model.clientModel.factory.create('ns0:rigid_link')

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
        for key in params:
            clientObject[key] = params[key]

        # Add rigid link to client model
        Model.clientModel.service.set_rigid_link(clientObject)

    def Diapragm(self,
                 no: int = 1,
                 nodes: str = '3 4',
                 lines: str = '6 7',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Diapragm Rigid Link
        clientObject = Model.clientModel.factory.create('ns0:rigid_link')

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
        for key in params:
            clientObject[key] = params[key]

        # Add rigid link to client model
        Model.clientModel.service.set_rigid_link(clientObject)
