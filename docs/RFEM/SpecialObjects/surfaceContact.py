from RFEM.initModel import Model, clearAttributes

class SurfaceContact():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Surfaces Contact
        clientObject = Model.clientModel.factory.create('ns0:surfaces_contact')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surfaces Contact No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surfaces Contact to client model
        Model.clientModel.service.set_surfaces_contact(clientObject)
