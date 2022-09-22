from RFEM.initModel import Model, clearAttributes

class EnlargedColumnHead():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Enlarged Column Head
        clientObject = Model.clientModel.factory.create('ns0:enlarged_column_head')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Enlarged Column Head No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Enlarged Column Head to client model
        Model.clientModel.service.set_enlarged_column_head(clientObject)
