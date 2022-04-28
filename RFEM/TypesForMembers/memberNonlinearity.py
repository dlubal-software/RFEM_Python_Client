from pytest import param
from RFEM.enums import MemberNonlinearityType
from RFEM.initModel import ConvertToDlString, Model, clearAtributes

class MemberNonlinearity():
    def __init__(self,
                 no: int = 1,
                 members: str = "",
                 nonlinearity_type = MemberNonlinearityType.TYPE_FAILURE_IF_TENSION,
                 parameters = None,
                 comment: str = '',
                 params: dict = None):

        # Client model | Member Nonlinearity
        clientObject = Model.clientModel.factory.create('ns0:member_nonlinearity')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Nonlinearity No.
        clientObject.no = no

        # Assigned Members
        clientObject.assigned_to = ConvertToDlString(members)

        # Nonlinearity Type and Parameters
        clientObject.type = nonlinearity_type.name

        if type.name == "TYPE_FAILURE_IF_TENSION_WITH_SLIPPAGE" or type.name == "TYPE_FAILURE_IF_COMPRESSION_WITH_SLIPPAGE" or type.name == "TYPE_SLIPPAGE":
            clientObject.slippage = parameters[0]

        elif type.name == "TYPE_TEARING_IF_TENSION" or type.name == "TYPE_YIELDING_IF_TENSION":
            clientObject.tension_force = parameters[0]

        elif type.name == "TYPE_TEARING_IF_COMPRESSION" or type.name == "TYPE_YIELDING_IF_COMPRESSION":
            clientObject.compression_force = parameters[0]

        elif type.name == "TYPE_TEARING" or type.name == "TYPE_YIELDING":
            clientObject.compression_force = parameters[0]
            clientObject.tension_force = parameters[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Member Nonlinearity to client model
        Model.clientModel.service.set_member_nonlinearity(clientObject)
