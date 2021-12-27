from RFEM.initModel import *

class LineWeldedJoint():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line Welded Joint
        clientObject = Model.clientModel.factory.create('ns0:line_welded_joint')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Welded Joint No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line welded joint to client model
        Model.clientModel.service.set_line_welded_joint(clientObject)
