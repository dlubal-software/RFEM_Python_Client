from RFEM.initModel import Model, clearAttributes

class SolidContact():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Solid Contact
        clientObject = Model.clientModel.factory.create('ns0:solid_contacts')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid Contact No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Contact to client model
        Model.clientModel.service.set_solid_contacts(clientObject)
