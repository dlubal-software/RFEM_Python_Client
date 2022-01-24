from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.dataTypes import inf
from RFEM.enums import NodalSupportType

def setNodalSupportConditions(clientObject,
                              C_u_X: float,
                              C_u_Y: float,
                              C_u_Z: float,
                              C_phi_X: float,
                              C_phi_Y: float,
                              C_phi_Z: float):
    '''
    Sets nodal support conditions

    Params:
        clientObject: Client model object | Nodal support
        C_u_X,Y,Z: Translational support conditions in respected direction
        C_phi_X,Y,Z: Rotational support conditions about respected axis
        comment: Comment

    Returns:
        clientObject: Initialized client model object | Nodal Support
    '''

    clientObject.spring_x = C_u_X
    clientObject.spring_y = C_u_Y
    clientObject.spring_z = C_u_Z

    clientObject.rotational_restraint_x = C_phi_X
    clientObject.rotational_restraint_y = C_phi_Y
    clientObject.rotational_restraint_z = C_phi_Z

    return clientObject

class NodalSupport():
    def __init__(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 support_type = NodalSupportType.HINGED,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Nodal Support
        clientObject = Model.clientModel.factory.create('ns0:nodal_support')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Nodal Support No.
        clientObject.no = no

        # Nodes No. (e.g. "5 6 7 12")
        clientObject.nodes = ConvertToDlString(nodes_no)

        # Nodal Support Conditions
        if   support_type == NodalSupportType.FIXED:
            # FIXED       'xxx xxx'
            clientObject = setNodalSupportConditions(clientObject, inf, inf, inf, inf, inf, inf)

        elif support_type == NodalSupportType.HINGED:
            # HINGED      'xxx --x'
            clientObject = setNodalSupportConditions(clientObject, inf, inf, inf, 0.0, 0.0, inf)

        elif support_type == NodalSupportType.ROLLER:
            # ROLLER      '--x --x'
            clientObject = setNodalSupportConditions(clientObject, 0.0, 0.0, inf, 0.0, 0.0, inf)

        elif support_type == NodalSupportType.ROLLER_IN_X:
            # ROLLER_IN_X '-xx --x'
            clientObject = setNodalSupportConditions(clientObject, 0.0, inf, inf, 0.0, 0.0, inf)

        elif support_type == NodalSupportType.ROLLER_IN_Y:
            # ROLLER_IN_Y 'x-x --x'
            clientObject = setNodalSupportConditions(clientObject, inf, 0.0, inf, 0.0, 0.0, inf)

        elif support_type == NodalSupportType.ROLLER_IN_Z:
            # ROLLER_IN_Z 'xx- --x'
            clientObject = setNodalSupportConditions(clientObject, inf, inf, 0.0, 0.0, 0.0, inf)

        elif support_type == NodalSupportType.FREE:
            # FREE '--- ---'
            clientObject = setNodalSupportConditions(clientObject, 0, 0, 0, 0, 0, 0)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Nodal Support to client model
        Model.clientModel.service.set_nodal_support(clientObject)
