from RFEM.initModel import Model, clearAtributes

class MemberResultIntermediatePoint():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Member Result Intermediate Point
        clientObject = model.clientModel.factory.create('ns0:member_result_intermediate_point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Result Intermediate Point No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Member Result Intermediate Point to client model
        model.clientModel.service.set_member_result_intermediate_point(clientObject)
