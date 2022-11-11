from RFEM.initModel import Model, clearAttributes

class MemberNonlinearity():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member Nonlinearity
        clientObject = Model.clientModel.factory.create('ns0:member_nonlinearity')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Nonlinearity No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Nonlinearity to client model
        Model.clientModel.service.set_member_nonlinearity(clientObject)
