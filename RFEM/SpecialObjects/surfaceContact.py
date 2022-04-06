from RFEM.initModel import Model, clearAtributes

class SurfaceContact():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Surfaces Contact
        clientObject = model.clientModel.factory.create('ns0:surfaces_contact')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surfaces Contact No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surfaces Contact to client model
        model.clientModel.service.set_surfaces_contact(clientObject)
