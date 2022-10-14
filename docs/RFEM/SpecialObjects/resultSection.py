from RFEM.initModel import Model, clearAttributes

class ResultSection():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Result Section
        clientObject = Model.clientModel.factory.create('ns0:result_section')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Result Section No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Result Section to client model
        Model.clientModel.service.set_result_section(clientObject)
