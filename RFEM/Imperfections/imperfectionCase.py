from RFEM.initModel import Model, clearAtributes

class ImperfectionCase():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Imperfection Case
        clientObject = Model.clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Imperfection Case to client model
        Model.clientModel.service.set_imperfection_case(clientObject)
