from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.dataTypes import inf
from RFEM.enums import LineSupportType

def setLineSupportConditions(clientObject,
                              C_u_X: float,
                              C_u_Y: float,
                              C_u_Z: float,
                              C_phi_X: float,
                              C_phi_Y: float,
                              C_phi_Z: float):
    '''
    Sets Line Support Conditions

    Args:
        clientObject: Client Model Object | Line Support
        C_u_X,Y,Z (float): Translational Support Conditions in Respected Direction
        C_phi_X,Y,Z (float): Rotational Support Conditions about Respected Axis

    Returns:
        clientObject: Initialized Client Model Object | Line Support
    '''

    clientObject.spring_x = C_u_X
    clientObject.spring_y = C_u_Y
    clientObject.spring_z = C_u_Z

    clientObject.rotational_restraint_x = C_phi_X
    clientObject.rotational_restraint_y = C_phi_Y
    clientObject.rotational_restraint_z = C_phi_Z

    return clientObject

class LineSupport():
    def __init__(self,
                 no: int = 1,
                 lines_no: str = '1 2',
                 support_type = LineSupportType.HINGED,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Line Support Tag
            lines_no (str): Assigned Lines
            support_type (enum): Line Support Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Line Support
        clientObject = model.clientModel.factory.create('ns0:line_support')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Support No.
        clientObject.no = no

        # Nodes No. (e.g. "5 6 7 12")
        clientObject.lines = ConvertToDlString(lines_no)

        # Nodal Support Conditions
        if   support_type == LineSupportType.FIXED:
            # FIXED       'xxx xxx'
            clientObject = setLineSupportConditions(clientObject, inf, inf, inf, inf, inf, inf)

        elif support_type == LineSupportType.HINGED:
            # HINGED      'xxx ---'
            clientObject = setLineSupportConditions(clientObject, inf, inf, inf, 0.0, 0.0, 0.0)

        elif support_type == LineSupportType.SLIDING_IN_X_AND_Y:
            # SLIDING_IN_X_AND_Y      '--x --x'
            clientObject = setLineSupportConditions(clientObject, 0.0, 0.0, inf, 0.0, 0.0, inf)

        elif support_type == LineSupportType.SLIDING_IN_X:
            # SLIDING_IN_X '-xx --x'
            clientObject = setLineSupportConditions(clientObject, 0.0, inf, inf, 0.0, 0.0, inf)

        elif support_type == LineSupportType.SLIDING_IN_Y:
            # SLIDING_IN_Y 'x-x --x'
            clientObject = setLineSupportConditions(clientObject, inf, 0.0, inf, 0.0, 0.0, inf)

        elif support_type == LineSupportType.SLIDING_IN_Z:
            # SLIDING_IN_Z 'xx- --x'
            clientObject = setLineSupportConditions(clientObject, inf, inf, 0.0, 0.0, 0.0, inf)

        elif support_type == LineSupportType.FREE:
            # FREE '--- ---'
            clientObject = setLineSupportConditions(clientObject, 10000, 0, 0, 0, 0, 0)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line Support to client model
        model.clientModel.service.set_line_support(clientObject)
