from RFEM.initModel import Model, clearAtributes

class MemberStiffnessModification():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Member Stiffness Modification
        clientObject = model.clientModel.factory.create('ns0:smember_stiffness_modification')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Stiffness Modification No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Member Stiffness Modification to client model
        model.clientModel.service.set_member_stiffness_modification(clientObject)
