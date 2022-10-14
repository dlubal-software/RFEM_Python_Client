from RFEM.initModel import Model, clearAttributes

class MemberDefinableStiffness():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member Definable Stffness
        clientObject = Model.clientModel.factory.create('ns0:member_definable_stiffness')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Definable Stffness No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Definable Stffness to client model
        Model.clientModel.service.set_member_definable_stiffness(clientObject)
