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
    Sets Nodal Support Conditions

    Args:
        clientObject: Client Model Object | Nodal Support
        C_u_X,Y,Z (float): Translational Support Conditions in Respected Direction
        C_phi_X,Y,Z (float): Rotational Support Conditions about Respected Axis

    Returns:
        clientObject: Initialized Client Model Object | Nodal Support
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
                 support = NodalSupportType.HINGED,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Nodal Support

        Args:
            no (int): Nodal Support Tag
            nodes_no (str): Assigned to Nodes
            support (enum or list): Support Definition List
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited

        Raises:
            ValueError: 'Support parameter can be enum or list with 6 items.'
        """

        # Client model | Nodal Support
        clientObject = model.clientModel.factory.create('ns0:nodal_support')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Nodal Support No.
        clientObject.no = no

        # Nodes No. (e.g. "5 6 7 12")
        clientObject.nodes = ConvertToDlString(nodes_no)

        # Nodal Support Conditions
        if   support == NodalSupportType.FIXED:
            # FIXED       'xxx xxx'
            clientObject = setNodalSupportConditions(clientObject, inf, inf, inf, inf, inf, inf)

        elif support == NodalSupportType.HINGED:
            # HINGED      'xxx --x'
            clientObject = setNodalSupportConditions(clientObject, inf, inf, inf, 0.0, 0.0, inf)

        elif support == NodalSupportType.ROLLER:
            # ROLLER      '--x --x'
            clientObject = setNodalSupportConditions(clientObject, 0.0, 0.0, inf, 0.0, 0.0, inf)

        elif support == NodalSupportType.ROLLER_IN_X:
            # ROLLER_IN_X '-xx --x'
            clientObject = setNodalSupportConditions(clientObject, 0.0, inf, inf, 0.0, 0.0, inf)

        elif support == NodalSupportType.ROLLER_IN_Y:
            # ROLLER_IN_Y 'x-x --x'
            clientObject = setNodalSupportConditions(clientObject, inf, 0.0, inf, 0.0, 0.0, inf)

        elif support == NodalSupportType.ROLLER_IN_Z:
            # ROLLER_IN_Z 'xx- --x'
            clientObject = setNodalSupportConditions(clientObject, inf, inf, 0.0, 0.0, 0.0, inf)

        elif support == NodalSupportType.FREE:
            # FREE '--- ---'
            clientObject = setNodalSupportConditions(clientObject, 0, 0, 0, 0, 0, 0)

        elif isinstance(support, list) and len(support) == 6:
            clientObject = setNodalSupportConditions(clientObject, support[0], support[1], support[2], support[3], support[4], support[5])

        else:
            raise ValueError('Support parameter can be enum or list with 6 items.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Nodal Support to client model
        model.clientModel.service.set_nodal_support(clientObject)
