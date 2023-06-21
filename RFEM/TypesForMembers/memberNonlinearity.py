from RFEM.enums import MemberNonlinearityType
from RFEM.initModel import Model, clearAttributes, ConvertToDlString, deleteEmptyAttributes

class MemberNonlinearity():
    def __init__(self,
                 no: int = 1,
                 members: str = "",
                 nonlinearity_type = MemberNonlinearityType.TYPE_FAILURE_IF_TENSION,
                 parameters = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Member Nonlinearity Tag
            members (str): Assigned Members
            nonlinearity_type (enum): Member Nonlinearity Type Enumeration Item
            parameters (list): Nonlinearity Parameters
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member Nonlinearity
        clientObject = model.clientModel.factory.create('ns0:member_nonlinearity')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Nonlinearity No.
        clientObject.no = no

        # Assigned Members
        clientObject.assigned_to = ConvertToDlString(members)

        # Nonlinearity Type and Parameters
        clientObject.type = nonlinearity_type.name

        if nonlinearity_type.name == "TYPE_FAILURE_IF_TENSION_WITH_SLIPPAGE" or nonlinearity_type.name == "TYPE_FAILURE_IF_COMPRESSION_WITH_SLIPPAGE" or nonlinearity_type.name == "TYPE_SLIPPAGE":
            clientObject.slippage = parameters[0]

        elif nonlinearity_type.name == "TYPE_TEARING_IF_TENSION" or nonlinearity_type.name == "TYPE_YIELDING_IF_TENSION":
            clientObject.tension_force = parameters[0]

        elif nonlinearity_type.name == "TYPE_TEARING_IF_COMPRESSION" or nonlinearity_type.name == "TYPE_YIELDING_IF_COMPRESSION":
            clientObject.compression_force = parameters[0]

        elif nonlinearity_type.name == "TYPE_TEARING" or nonlinearity_type.name == "TYPE_YIELDING":
            clientObject.compression_force = parameters[0]
            clientObject.tension_force = parameters[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Nonlinearity to client model
        model.clientModel.service.set_member_nonlinearity(clientObject)
