from RFEM.initModel import *

class Node():
    def __init__(self,
                 no: int = 1,
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Coordinates
        clientObject.coordinate_1 = coordinate_X
        clientObject.coordinate_2 = coordinate_Y
        clientObject.coordinate_3 = coordinate_Z

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def Standard(self,
                 no: int = 1,
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Coordinates
        clientObject.coordinate_1 = coordinate_X
        clientObject.coordinate_2 = coordinate_Y
        clientObject.coordinate_3 = coordinate_Z

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def BetweenTwoNodes(self,
                 no: int = 1,
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Coordinates
        clientObject.coordinate_1 = coordinate_X
        clientObject.coordinate_2 = coordinate_Y
        clientObject.coordinate_3 = coordinate_Z

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def BetweenTwoPoints(self,
                 no: int = 1,
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Coordinates
        clientObject.coordinate_1 = coordinate_X
        clientObject.coordinate_2 = coordinate_Y
        clientObject.coordinate_3 = coordinate_Z

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def OnLine(self,
                 no: int = 1,
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Coordinates
        clientObject.coordinate_1 = coordinate_X
        clientObject.coordinate_2 = coordinate_Y
        clientObject.coordinate_3 = coordinate_Z

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)

    def OnMember(self,
                 no: int = 1,
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Node
        clientObject = clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Coordinates
        clientObject.coordinate_1 = coordinate_X
        clientObject.coordinate_2 = coordinate_Y
        clientObject.coordinate_3 = coordinate_Z

        # Comment
        clientObject.comment = comment

        for key in params:
            clientObject[key] = params[key]

        # Add Node to client model
        clientModel.service.set_node(clientObject)
