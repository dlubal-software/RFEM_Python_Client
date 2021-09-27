from RFEM.initModel import *

class Line():
    def __init__(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = ''):

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

        # Add Line to client model
        clientModel.service.set_line(clientObject)
