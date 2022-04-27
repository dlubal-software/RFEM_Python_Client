from RFEM.initModel import Model, clearAtributes

class ResultSection():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Result Section
        clientObject = model.clientModel.factory.create('ns0:result_section')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Result Section No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Result Section to client model
        model.clientModel.service.set_result_section(clientObject)
