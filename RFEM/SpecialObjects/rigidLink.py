from RFEM.initModel import *

class RigidLink():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Rigid Link
        clientObject = Model.clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add rigid link to client model
        Model.clientModel.service.set_rigid_link(clientObject)

    def LineToLine(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line To Line Rigid Link
        clientObject = Model.clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add rigid link to client model
        Model.clientModel.service.set_rigid_link(clientObject)

    def LineToSurface(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line To Surface Rigid Link
        clientObject = Model.clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add rigid link to client model
        Model.clientModel.service.set_rigid_link(clientObject)

    def Diapragm(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Diapragm Rigid Link
        clientObject = Model.clientModel.factory.create('ns0:rigid_link')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Rigid Link No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add rigid link to client model
        Model.clientModel.service.set_rigid_link(clientObject)
