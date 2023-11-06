from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.dataTypes import inf
from RFEM.enums import NodalSupportType, NodalSupportNonlinearity

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
        clearAttributes(clientObject)

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

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Nodal Support to client model
        model.clientModel.service.set_nodal_support(clientObject)

    @staticmethod
    def Nonlinearity(no: int = 1,
                     nodes: str = "1",
                     coordinate_system: int = 1,
                     spring_constant: list = [inf, inf, inf, 0.0, 0.0, inf],
                     spring_x_nonlinearity: list = [NodalSupportNonlinearity.NONLINEARITY_TYPE_NONE],
                     spring_y_nonlinearity: list = [NodalSupportNonlinearity.NONLINEARITY_TYPE_NONE],
                     spring_z_nonlinearity: list = [NodalSupportNonlinearity.NONLINEARITY_TYPE_NONE],
                     rotational_x_nonlinearity: list = [NodalSupportNonlinearity.NONLINEARITY_TYPE_NONE],
                     rotational_y_nonlinearity: list = [NodalSupportNonlinearity.NONLINEARITY_TYPE_NONE],
                     rotational_z_nonlinearity: list = [NodalSupportNonlinearity.NONLINEARITY_TYPE_NONE],
                     name: str = None,
                     comment: str = '',
                     params: dict = None,
                     model = Model):

        '''
        Args:
            no (int): Nodal Support Tag
            nodes (str): Assigned Nodes
            coordinate_system (int): Assigned Coordinate System
            spring_constant (list): Spring Constant List
                spring_constant = [spring_x, spring_y, spring_z, rotational_restraint_x, rotational_restraint_y, rotational_restraint_z]
            spring_x_nonlinearity (list/list of lists): Nonlinearity Parameters for Nodal Support along X direction
            spring_y_nonlinearity (list/list of lists): Nonlinearity Parameters for Nodal Support along Y direction
            spring_z_nonlinearity (list/list of lists): Nonlinearity Parameters for Nodal Support along Z direction
                for spring_x/y/z_nonlinearity[0] == NodalSupportNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
                    spring_x/y/z_nonlinearity = [Nodal Support nonlinearity Partial_Activity, negative zone, positive zone]
                    for negative/positive zone[0] == SupportPartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                        negative/positive zone = [negative/positive zone type, slippage]
                    for negative/positive zone[0] == SupportPartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED:
                        negative/positive zone = [negative/positive zone type, slippage, displacement]  (Note: Displacement must be greater than slippage)
                    for negative/positive zone[0] == SupportPartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE/PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                        negative/positive zone = [negative/positive zone type, slippage, force]
                for spring_x/y/z_nonlinearity[0] == NodalSupportNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
                    spring_x/y/z_nonlinearity = [nonlinearity_type_diagram, [symmetric(bool), diagram_type_enumeration(start), diagram_type_enumeration(end)], [[displacement, force],...]]
                for spring_x/y/z_nonlinearity[0] == NodalSupportNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1/NONLINEARITY_TYPE_FRICTION_DIRECTION_2/NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2:
                    spring_x/y/z_nonlinearity = [nonlinearity_type_friction, friction_coefficient]
                for spring_x/y/z_nonlinearity[0] == NodalSupportNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2:
                    spring_x/y/z_nonlinearity = [nonlinearity_type_friction, friction_coefficient_1, friction_coefficient_2]
            rotational_x_nonlinearity (list of lists): Nonlinearity Parameters for Nodal Support around X direction
            rotational_y_nonlinearity (list of lists): Nonlinearity Parameters for Nodal Support around Y direction
            rotational_z_nonlinearity (list of lists): Nonlinearity Parameters for Nodal Support around Z direction
                for rotational_x/y/z_nonlinearity[0] == NodalSupportNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
                    rotational_x/y/z_nonlinearity = [Nodal Support nonlinearity Partial_Activity, negative zone, positive zone]
                    for negative/positive zone[0] == SupportPartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                        negative/positive zone = [negative/positive zone type, slippage]
                    for negative/positive zone[0] == SupportPartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_FIXED:
                        negative/positive zone = [negative/positive zone type, slippage, rotation]
                    for negative/positive zone[0] == SupportPartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT/PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                        negative/positive zone = [negative/positive zone type, slippage, moment]
                for rotational_x/y/z_nonlinearity[0] == NodalSupportNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
                    rotational_x/y/z_nonlinearity = [nonlinearity_type_diagram, [symmetric(bool), diagram_type_enumeration(start), diagram_type_enumeration(end)], [[rotation, moment],...]]
                for rotational_x/y/z_nonlinearity[0] == NodalSupportNonlinearity.NONLINEARITY_TYPE_STIFFNESS_DIAGRAM:
                    rotational_x/y/z_nonlinearity = [nonlinearity_type_stiffness_diagram, [stiffness_diagram_around_depends_on, symmetric(bool), diagram_type_enumeration(start), diagram_type_enumeration(end)], [[force, spring],...]]
                    (note: for stiffness_diagram_around_depends_on == SupportStiffnessDiagramDependOn.STIFFNESS_DIAGRAM_DEPENDS_ON_P: symmetric must be True.)
            name (str, optional): User Defined Nodal Support Name
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Nodal Support
        clientObject = model.clientModel.factory.create('ns0:nodal_support')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Nodal Support No.
        clientObject.no = no

        # Assign Node Number
        clientObject.nodes = ConvertToDlString(nodes)

        # Coordinate System
        clientObject.coordinate_system = coordinate_system

        # Nodal Support Spring Constants
        clientObject.spring_x = spring_constant[0]
        clientObject.spring_y = spring_constant[1]
        clientObject.spring_z = spring_constant[2]

        clientObject.rotational_restraint_x = spring_constant[3]
        clientObject.rotational_restraint_y = spring_constant[4]
        clientObject.rotational_restraint_z = spring_constant[5]

        # Nodal Support Nonlinearity Type
        clientObject.spring_x_nonlinearity = spring_x_nonlinearity[0].name
        clientObject.spring_y_nonlinearity = spring_y_nonlinearity[0].name
        clientObject.spring_z_nonlinearity = spring_z_nonlinearity[0].name
        clientObject.rotational_restraint_x_nonlinearity = rotational_x_nonlinearity[0].name
        clientObject.rotational_restraint_y_nonlinearity = rotational_y_nonlinearity[0].name
        clientObject.rotational_restraint_z_nonlinearity = rotational_z_nonlinearity[0].name

        # Nodal Support Nonlinearity Parameters for Partial Activity
        # For spring_x_nonlinearity
        if spring_x_nonlinearity[0].name == "NONLINEARITY_TYPE_PARTIAL_ACTIVITY":

            # Negative Zone
            clientObject.partial_activity_along_x_negative_type = spring_x_nonlinearity[1][0].name

            if spring_x_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_along_x_negative_slippage = spring_x_nonlinearity[1][1]

            elif spring_x_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_along_x_negative_slippage = spring_x_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_displacement = spring_x_nonlinearity[1][2]

            elif spring_x_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE' or \
                spring_x_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE':
                clientObject.partial_activity_along_x_negative_slippage = spring_x_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_force = spring_x_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_x_positive_type = spring_x_nonlinearity[2][0].name

            if spring_x_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_along_x_positive_slippage = spring_x_nonlinearity[2][1]

            elif spring_x_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_along_x_positive_slippage = spring_x_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_displacement = spring_x_nonlinearity[2][2]

            elif spring_x_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE' or \
                spring_x_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE':
                clientObject.partial_activity_along_x_positive_slippage = spring_x_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_force = spring_x_nonlinearity[2][2]

        # For spring_y_nonlinearity
        if spring_y_nonlinearity[0].name == "NONLINEARITY_TYPE_PARTIAL_ACTIVITY":

            # Negative Zone
            clientObject.partial_activity_along_y_negative_type = spring_y_nonlinearity[1][0].name

            if spring_y_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_along_y_negative_slippage = spring_y_nonlinearity[1][1]

            elif spring_y_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_along_y_negative_slippage = spring_y_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_displacement = spring_y_nonlinearity[1][2]

            elif spring_y_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE' or \
                spring_y_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE':
                clientObject.partial_activity_along_y_negative_slippage = spring_y_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_force = spring_y_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_y_positive_type = spring_y_nonlinearity[2][0].name

            if spring_y_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_along_y_positive_slippage = spring_y_nonlinearity[2][1]

            elif spring_y_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_along_y_positive_slippage = spring_y_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_displacement = spring_y_nonlinearity[2][2]

            elif spring_y_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE' or \
                spring_y_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE':
                clientObject.partial_activity_along_y_positive_slippage = spring_y_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_force = spring_y_nonlinearity[2][2]

        # For spring_z_nonlinearity
        if spring_z_nonlinearity[0].name == "NONLINEARITY_TYPE_PARTIAL_ACTIVITY":

            # Negative Zone
            clientObject.partial_activity_along_z_negative_type  = spring_z_nonlinearity[1][0].name

            if spring_z_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_along_z_negative_slippage = spring_z_nonlinearity[1][1]

            elif spring_z_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_along_z_negative_slippage = spring_z_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_displacement = spring_z_nonlinearity[1][2]

            elif spring_z_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE' or \
                spring_z_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE':
                clientObject.partial_activity_along_z_negative_slippage = spring_z_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_force = spring_z_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_z_positive_type = spring_z_nonlinearity[2][0].name

            if spring_z_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_along_z_positive_slippage = spring_z_nonlinearity[2][1]

            elif spring_z_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_along_z_positive_slippage = spring_z_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_displacement = spring_z_nonlinearity[2][2]

            elif spring_z_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE' or \
                spring_z_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE':
                clientObject.partial_activity_along_z_positive_slippage = spring_z_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_force = spring_z_nonlinearity[2][2]

        # For rotational_x_nonlinearity
        if rotational_x_nonlinearity[0].name == "NONLINEARITY_TYPE_PARTIAL_ACTIVITY":

            # Negative Zone
            clientObject.partial_activity_around_x_negative_type  = rotational_x_nonlinearity[1][0].name

            if rotational_x_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_around_x_negative_slippage = rotational_x_nonlinearity[1][1]

            elif rotational_x_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_around_x_negative_slippage = rotational_x_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_rotation = rotational_x_nonlinearity[1][2]

            elif rotational_x_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT' or \
                rotational_x_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT':
                clientObject.partial_activity_around_x_negative_slippage = rotational_x_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_moment = rotational_x_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_x_positive_type  = rotational_x_nonlinearity[2][0].name

            if rotational_x_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_around_x_positive_slippage = rotational_x_nonlinearity[2][1]

            elif rotational_x_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_around_x_positive_slippage = rotational_x_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_rotation = rotational_x_nonlinearity[2][2]

            elif rotational_x_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT' or \
                rotational_x_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT':
                clientObject.partial_activity_around_x_positive_slippage = rotational_x_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_moment = rotational_x_nonlinearity[2][2]

        # For rotational_y_nonlinearity
        if rotational_y_nonlinearity[0].name == "NONLINEARITY_TYPE_PARTIAL_ACTIVITY":

            # Negative Zone
            clientObject.partial_activity_around_y_negative_type  = rotational_y_nonlinearity[1][0].name

            if rotational_y_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_around_y_negative_slippage = rotational_y_nonlinearity[1][1]

            elif rotational_y_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_around_y_negative_slippage = rotational_y_nonlinearity[1][1]
                clientObject.partial_activity_around_y_negative_rotation = rotational_y_nonlinearity[1][2]

            elif rotational_y_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT' or \
                rotational_y_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT':
                clientObject.partial_activity_around_y_negative_slippage = rotational_y_nonlinearity[1][1]
                clientObject.partial_activity_around_y_negative_moment = rotational_y_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_y_positive_type  = rotational_y_nonlinearity[2][0].name

            if rotational_y_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_around_y_positive_slippage = rotational_y_nonlinearity[2][1]

            elif rotational_y_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_around_y_positive_slippage = rotational_y_nonlinearity[2][1]
                clientObject.partial_activity_around_y_positive_rotation = rotational_y_nonlinearity[2][2]

            elif rotational_y_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT' or \
                rotational_y_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT':
                clientObject.partial_activity_around_y_positive_slippage = rotational_y_nonlinearity[2][1]
                clientObject.partial_activity_around_y_positive_moment = rotational_y_nonlinearity[2][2]

        # For rotational_z_nonlinearity
        if rotational_z_nonlinearity[0].name == "NONLINEARITY_TYPE_PARTIAL_ACTIVITY":

            # Negative Zone
            clientObject.partial_activity_around_z_negative_type  = rotational_z_nonlinearity[1][0].name

            if rotational_z_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_around_z_negative_slippage = rotational_z_nonlinearity[1][1]

            elif rotational_z_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_around_z_negative_slippage = rotational_z_nonlinearity[1][1]
                clientObject.partial_activity_around_z_negative_rotation = rotational_z_nonlinearity[1][2]

            elif rotational_z_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT' or \
                rotational_z_nonlinearity[1][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT':
                clientObject.partial_activity_around_z_negative_slippage = rotational_z_nonlinearity[1][1]
                clientObject.partial_activity_around_z_negative_moment = rotational_z_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_z_positive_type  = rotational_z_nonlinearity[2][0].name

            if rotational_z_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_COMPLETE':
                clientObject.partial_activity_around_z_positive_slippage = rotational_z_nonlinearity[2][1]

            elif rotational_z_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FIXED':
                clientObject.partial_activity_around_z_positive_slippage = rotational_z_nonlinearity[2][1]
                clientObject.partial_activity_around_z_positive_rotation = rotational_z_nonlinearity[2][2]

            elif rotational_z_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT' or \
                rotational_z_nonlinearity[2][0].name == 'PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT':
                clientObject.partial_activity_around_z_positive_slippage = rotational_z_nonlinearity[2][1]
                clientObject.partial_activity_around_z_positive_moment = rotational_z_nonlinearity[2][2]

        # Nodal Support Nonlinearity Parameters for Diagram
        # For spring_x_nonlinearity
        if spring_x_nonlinearity[0].name == "NONLINEARITY_TYPE_DIAGRAM":
            clientObject.diagram_along_x_symmetric = spring_x_nonlinearity[1][0]

            if spring_x_nonlinearity[1][0]:
                clientObject.diagram_along_x_end = spring_x_nonlinearity[1][1].name
                clientObject.diagram_along_x_start = spring_x_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_x_start = spring_x_nonlinearity[1][1].name
                clientObject.diagram_along_x_end = spring_x_nonlinearity[1][2].name

            clientObject.diagram_along_x_table = Model.clientModel.factory.create('ns0:nodal_support.diagram_along_x_table')

            for i, j in enumerate(spring_x_nonlinearity[2]):
                nsux = Model.clientModel.factory.create('ns0:nodal_support_diagram_along_x_table_row')
                nsux.no = i+1
                nsux.row = model.clientModel.factory.create('ns0:nodal_support_diagram_along_x_table')
                clearAttributes(nsux.row)
                nsux.row.displacement = spring_x_nonlinearity[2][i][0]
                nsux.row.force = spring_x_nonlinearity[2][i][1]

                clientObject.diagram_along_x_table.nodal_support_diagram_along_x_table.append(nsux)

            clientObject.diagram_along_x_is_sorted = True

        # For spring_y_nonlinearity
        if spring_y_nonlinearity[0].name == "NONLINEARITY_TYPE_DIAGRAM":
            clientObject.diagram_along_y_symmetric = spring_y_nonlinearity[1][0]

            if spring_y_nonlinearity[1][0]:
                clientObject.diagram_along_y_end = spring_y_nonlinearity[1][1].name
                clientObject.diagram_along_y_start = spring_y_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_y_end = spring_y_nonlinearity[1][2].name
                clientObject.diagram_along_y_start = spring_y_nonlinearity[1][1].name

            clientObject.diagram_along_y_table = Model.clientModel.factory.create('ns0:nodal_support.diagram_along_y_table')

            for i, j in enumerate(spring_y_nonlinearity[2]):
                nsuy = Model.clientModel.factory.create('ns0:nodal_support_diagram_along_y_table_row')
                nsuy.no = i+1
                nsuy.row = model.clientModel.factory.create('ns0:nodal_support_diagram_along_y_table')
                clearAttributes(nsuy.row)
                nsuy.row.displacement = spring_y_nonlinearity[2][i][0]
                nsuy.row.force = spring_y_nonlinearity[2][i][1]

                clientObject.diagram_along_y_table.nodal_support_diagram_along_y_table.append(nsuy)

            clientObject.diagram_along_y_is_sorted = True

        # For spring_z_nonlinearity
        if spring_z_nonlinearity[0].name == "NONLINEARITY_TYPE_DIAGRAM":
            clientObject.diagram_along_z_symmetric = spring_z_nonlinearity[1][0]

            if spring_z_nonlinearity[1][0]:
                clientObject.diagram_along_z_end = spring_z_nonlinearity[1][1].name
                clientObject.diagram_along_z_start = spring_z_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_z_start = spring_z_nonlinearity[1][1].name
                clientObject.diagram_along_z_end = spring_z_nonlinearity[1][2].name

            clientObject.diagram_along_z_table = Model.clientModel.factory.create('ns0:nodal_support.diagram_along_z_table')

            for i, j in enumerate(spring_z_nonlinearity[2]):
                nsuz = Model.clientModel.factory.create('ns0:nodal_support_diagram_along_z_table_row')
                nsuz.no = i+1
                nsuz.row = model.clientModel.factory.create('ns0:nodal_support_diagram_along_z_table')
                clearAttributes(nsuz.row)
                nsuz.row.displacement = spring_z_nonlinearity[2][i][0]
                nsuz.row.force = spring_z_nonlinearity[2][i][1]

                clientObject.diagram_along_z_table.nodal_support_diagram_along_z_table.append(nsuz)

            clientObject.diagram_along_z_is_sorted = True

        # For rotational_x_nonlinearity
        if rotational_x_nonlinearity[0].name == "NONLINEARITY_TYPE_DIAGRAM":
            clientObject.diagram_around_x_symmetric = rotational_x_nonlinearity[1][0]

            if rotational_x_nonlinearity[1][0]:
                clientObject.diagram_around_x_end = rotational_x_nonlinearity[1][1].name
                clientObject.diagram_around_x_start = rotational_x_nonlinearity[1][1].name

            else:
                clientObject.diagram_around_x_start = rotational_x_nonlinearity[1][1].name
                clientObject.diagram_around_x_end = rotational_x_nonlinearity[1][2].name

            clientObject.diagram_around_x_table = Model.clientModel.factory.create('ns0:nodal_support.diagram_around_x_table')

            for i, j in enumerate(rotational_x_nonlinearity[2]):
                nsrx = Model.clientModel.factory.create('ns0:nodal_support_diagram_around_x_table_row')
                nsrx.no = i+1
                nsrx.row = model.clientModel.factory.create('ns0:nodal_support_diagram_around_x_table')
                clearAttributes(nsrx.row)
                nsrx.row.rotation = rotational_x_nonlinearity[2][i][0]
                nsrx.row.moment = rotational_x_nonlinearity[2][i][1]

                clientObject.diagram_around_x_table.nodal_support_diagram_around_x_table.append(nsrx)

            clientObject.diagram_around_x_is_sorted = True

        # For rotational_y_nonlinearity
        if rotational_y_nonlinearity[0].name == "NONLINEARITY_TYPE_DIAGRAM":
            clientObject.diagram_around_y_symmetric = rotational_y_nonlinearity[1][0]

            if rotational_y_nonlinearity[1][0]:
                clientObject.diagram_around_y_end = rotational_y_nonlinearity[1][1].name
                clientObject.diagram_around_y_start = rotational_y_nonlinearity[1][1].name

            else:
                clientObject.diagram_around_y_start = rotational_y_nonlinearity[1][1].name
                clientObject.diagram_around_y_end = rotational_y_nonlinearity[1][2].name

            clientObject.diagram_around_y_table = Model.clientModel.factory.create('ns0:nodal_support.diagram_around_y_table')

            for i, j in enumerate(rotational_y_nonlinearity[2]):
                nsry = Model.clientModel.factory.create('ns0:nodal_support_diagram_around_y_table_row')
                nsry.no = i+1
                nsry.row = model.clientModel.factory.create('ns0:nodal_support_diagram_around_y_table')
                clearAttributes(nsry.row)
                nsry.row.rotation = rotational_y_nonlinearity[2][i][0]
                nsry.row.moment = rotational_y_nonlinearity[2][i][1]

                clientObject.diagram_around_y_table.nodal_support_diagram_around_y_table.append(nsry)

            clientObject.diagram_around_y_is_sorted = True

        # For rotational_z_nonlinearity
        if rotational_z_nonlinearity[0].name == "NONLINEARITY_TYPE_DIAGRAM":
            clientObject.diagram_around_z_symmetric = rotational_z_nonlinearity[1][0]

            if rotational_z_nonlinearity[1][0]:
                clientObject.diagram_around_z_end = rotational_z_nonlinearity[1][1].name
                clientObject.diagram_around_z_start = rotational_z_nonlinearity[1][1].name

            else:
                clientObject.diagram_around_z_start = rotational_z_nonlinearity[1][1].name
                clientObject.diagram_around_z_end = rotational_z_nonlinearity[1][2].name

            clientObject.diagram_around_z_table = Model.clientModel.factory.create('ns0:nodal_support.diagram_around_z_table')

            for i, j in enumerate(rotational_z_nonlinearity[2]):
                nsrz = Model.clientModel.factory.create('ns0:nodal_support_diagram_around_z_table_row')
                nsrz.no = i+1
                nsrz.row = model.clientModel.factory.create('ns0:nodal_support_diagram_around_z_table')
                clearAttributes(nsrz.row)
                nsrz.row.rotation = rotational_z_nonlinearity[2][i][0]
                nsrz.row.moment = rotational_z_nonlinearity[2][i][1]

                clientObject.diagram_around_z_table.nodal_support_diagram_around_z_table.append(nsrz)

            clientObject.diagram_around_z_is_sorted = True

        # Nodal Support Nonlinearity Parameters for Frictions
        # For spring_x_nonlinearity
        if spring_x_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_1" or \
            spring_x_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_2" or \
            spring_x_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2":
            clientObject.friction_coefficient_x = spring_x_nonlinearity[1]

        elif spring_x_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2":
            clientObject.friction_coefficient_xy = spring_x_nonlinearity[1]
            clientObject.friction_coefficient_xz = spring_x_nonlinearity[2]

        # For spring_y_nonlinearity
        if spring_y_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_1" or \
            spring_y_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_2" or \
            spring_y_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2":
            clientObject.friction_coefficient_y = spring_y_nonlinearity[1]

        elif spring_y_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2":
            clientObject.friction_coefficient_yx = spring_y_nonlinearity[1]
            clientObject.friction_coefficient_yz = spring_y_nonlinearity[2]

        # For spring_z_nonlinearity
        if spring_z_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_1" or \
            spring_z_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_2" or \
            spring_z_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2":
            clientObject.friction_coefficient_z = spring_z_nonlinearity[1]

        elif spring_z_nonlinearity[0].name == "NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2":
            clientObject.friction_coefficient_zx = spring_z_nonlinearity[1]
            clientObject.friction_coefficient_zy = spring_z_nonlinearity[2]

        # Nodal Support Nonlinearity Parameters for Stifness Diagram
        # For rotational_x_nonlinearity
        if rotational_x_nonlinearity[0].name == "NONLINEARITY_TYPE_STIFFNESS_DIAGRAM":

            clientObject.stiffness_diagram_around_x_depends_on = rotational_x_nonlinearity[1][0].name
            clientObject.stiffness_diagram_around_x_symmetric = rotational_x_nonlinearity[1][1]
            if rotational_x_nonlinearity[1][0].name == 'STIFFNESS_DIAGRAM_DEPENDS_ON_P':
                clientObject.stiffness_diagram_around_x_symmetric = True

            if rotational_x_nonlinearity[1][1]:
                clientObject.stiffness_diagram_around_x_end = rotational_x_nonlinearity[1][2].name
                clientObject.stiffness_diagram_around_x_start = rotational_x_nonlinearity[1][2].name

            else:
                clientObject.stiffness_diagram_around_x_start = rotational_x_nonlinearity[1][2].name
                clientObject.stiffness_diagram_around_x_end = rotational_x_nonlinearity[1][3].name

            clientObject.stiffness_diagram_around_x_table = Model.clientModel.factory.create('ns0:nodal_support.stiffness_diagram_around_x_table')

            for i, j in enumerate(rotational_x_nonlinearity[2]):
                nssrx = Model.clientModel.factory.create('ns0:nodal_support_stiffness_diagram_around_x_table_row')
                nssrx.no = i+1
                nssrx.row = model.clientModel.factory.create('ns0:nodal_support_stiffness_diagram_around_x_table')
                clearAttributes(nssrx.row)
                nssrx.row.force = rotational_x_nonlinearity[2][i][0]
                nssrx.row.spring = rotational_x_nonlinearity[2][i][1]

                clientObject.stiffness_diagram_around_x_table.nodal_support_stiffness_diagram_around_x_table.append(nssrx)

            clientObject.stiffness_diagram_around_x_is_sorted = True

        # For rotational_y_nonlinearity
        if rotational_y_nonlinearity[0].name == "NONLINEARITY_TYPE_STIFFNESS_DIAGRAM":

            clientObject.stiffness_diagram_around_y_depends_on = rotational_y_nonlinearity[1][0].name
            clientObject.stiffness_diagram_around_y_symmetric = rotational_y_nonlinearity[1][1]
            if rotational_y_nonlinearity[1][0].name == 'STIFFNESS_DIAGRAM_DEPENDS_ON_P':
                clientObject.stiffness_diagram_around_y_symmetric = True

            if rotational_y_nonlinearity[1][1]:
                clientObject.stiffness_diagram_around_y_end = rotational_y_nonlinearity[1][2].name
                clientObject.stiffness_diagram_around_y_start = rotational_y_nonlinearity[1][2].name

            else:
                clientObject.stiffness_diagram_around_y_start = rotational_y_nonlinearity[1][2].name
                clientObject.stiffness_diagram_around_y_end = rotational_y_nonlinearity[1][3].name

            clientObject.stiffness_diagram_around_y_table = Model.clientModel.factory.create('ns0:nodal_support.stiffness_diagram_around_y_table')

            for i, j in enumerate(rotational_y_nonlinearity[2]):
                nssry = Model.clientModel.factory.create('ns0:nodal_support_stiffness_diagram_around_y_table_row')
                nssry.no = i+1
                nssry.row = model.clientModel.factory.create('ns0:nodal_support_stiffness_diagram_around_y_table')
                clearAttributes(nssry.row)
                nssry.row.force = rotational_y_nonlinearity[2][i][0]
                nssry.row.spring = rotational_y_nonlinearity[2][i][1]

                clientObject.stiffness_diagram_around_y_table.nodal_support_stiffness_diagram_around_y_table.append(nssry)

            clientObject.stiffness_diagram_around_y_is_sorted = True

        # For rotational_z_nonlinearity
        if rotational_z_nonlinearity[0].name == "NONLINEARITY_TYPE_STIFFNESS_DIAGRAM":

            clientObject.stiffness_diagram_around_z_depends_on = rotational_z_nonlinearity[1][0].name
            clientObject.stiffness_diagram_around_z_symmetric = rotational_z_nonlinearity[1][1]
            if rotational_z_nonlinearity[1][0].name == 'STIFFNESS_DIAGRAM_DEPENDS_ON_P':
                clientObject.stiffness_diagram_around_z_symmetric = True

            if rotational_z_nonlinearity[1][1]:
                clientObject.stiffness_diagram_around_z_end = rotational_z_nonlinearity[1][2].name
                clientObject.stiffness_diagram_around_z_start = rotational_z_nonlinearity[1][2].name

            else:
                clientObject.stiffness_diagram_around_z_start = rotational_z_nonlinearity[1][2].name
                clientObject.stiffness_diagram_around_z_end = rotational_z_nonlinearity[1][3].name

            clientObject.stiffness_diagram_around_z_table = Model.clientModel.factory.create('ns0:nodal_support.stiffness_diagram_around_z_table')

            for i, j in enumerate(rotational_z_nonlinearity[2]):
                nssrz = Model.clientModel.factory.create('ns0:nodal_support_stiffness_diagram_around_z_table_row')
                nssrz.no = i+1
                nssrz.row = model.clientModel.factory.create('ns0:nodal_support_stiffness_diagram_around_z_table')
                clearAttributes(nssrz.row)
                nssrz.row.force = rotational_z_nonlinearity[2][i][0]
                nssrz.row.spring = rotational_z_nonlinearity[2][i][1]

                clientObject.stiffness_diagram_around_z_table.nodal_support_stiffness_diagram_around_z_table.append(nssrz)

            clientObject.stiffness_diagram_around_z_is_sorted = True

        # User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Nodal Support to client model
        model.clientModel.service.set_nodal_support(clientObject)
