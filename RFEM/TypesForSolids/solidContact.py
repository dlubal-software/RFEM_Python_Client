from RFEM.initModel import Model, clearAtributes

class SolidContact():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Solid Contact
        clientObject = model.clientModel.factory.create('ns0:solid_contacts')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Contact No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Solid Contact to client model
        model.clientModel.service.set_solid_contacts(clientObject)
