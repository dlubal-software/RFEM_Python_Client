from RFEM.initModel import Model, clearAttributes

class MemberSupport():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member Support
        clientObject = Model.clientModel.factory.create('ns0:member_support')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Support No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Support to client model
        Model.clientModel.service.set_member_support(clientObject)
