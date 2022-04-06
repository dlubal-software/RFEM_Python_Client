from RFEM.initModel import Model, clearAtributes

class MemberSupport():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Member Support
        clientObject = model.clientModel.factory.create('ns0:member_support')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Support No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Member Support to client model
        model.clientModel.service.set_member_support(clientObject)
