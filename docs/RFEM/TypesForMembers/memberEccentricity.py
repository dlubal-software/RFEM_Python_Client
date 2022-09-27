from RFEM.initModel import Model, clearAttributes

class MemberEccentricity():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member Eccentricity
        clientObject = Model.clientModel.factory.create('ns0:member_eccentricity')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Eccentricity No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Eccentricity to client model
        Model.clientModel.service.set_member_eccentricity(clientObject)
