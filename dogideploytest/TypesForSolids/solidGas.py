from RFEM.initModel import Model, clearAtributes

class SolidGas():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Solid Gas
        clientObject = model.clientModel.factory.create('ns0:solid_gas')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Gas No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Solid Gas to client model
        model.clientModel.service.set_solid_gas(clientObject)
