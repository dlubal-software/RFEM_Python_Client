from RFEM.initModel import *

class Line():
    def __init__(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line
        clientObject = clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = nodes_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        clientModel.service.set_line(clientObject)

    def Polyline(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line
        clientObject = clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = nodes_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        clientModel.service.set_line(clientObject)

    def Arc(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line
        clientObject = clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = nodes_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        clientModel.service.set_line(clientObject)

    def Circle(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line
        clientObject = clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = nodes_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        clientModel.service.set_line(clientObject)

    def EllipticalArc(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line
        clientObject = clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = nodes_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        clientModel.service.set_line(clientObject)

    def Ellipse(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line
        clientObject = clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = nodes_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        clientModel.service.set_line(clientObject)

    def Parabola(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line
        clientObject = clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = nodes_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        clientModel.service.set_line(clientObject)

    def Spline(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line
        clientObject = clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = nodes_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        clientModel.service.set_line(clientObject)

    def NURBS(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line
        clientObject = clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = nodes_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        clientModel.service.set_line(clientObject)
