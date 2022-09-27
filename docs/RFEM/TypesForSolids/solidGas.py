from RFEM.initModel import Model, clearAttributes

class SolidGas():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Solid Gas
        clientObject = Model.clientModel.factory.create('ns0:solid_gas')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid Gas No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Gas to client model
        Model.clientModel.service.set_solid_gas(clientObject)
