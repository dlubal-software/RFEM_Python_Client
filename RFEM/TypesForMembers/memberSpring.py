from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes,ConvertToDlString
from RFEM.enums import MemberSpringType, PartialActivityAlongType, MemberSpringSelfWeightDefinition

class MemberSpring():

    def __init__(self,
                 no: int = 1,
                 member: str = "",
                 definition_type = MemberSpringType.PARTIAL_ACTIVITY,
                 parameters: list = [[PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 0.0], [PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 0.0]],
                 axial_stiffness: float = 0.0,
                 self_weight: list = [MemberSpringSelfWeightDefinition.MASS_PER_LENGTH, 1],
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Member Spring Tag
            members (str): Assigned Members
            definition_type (enum): Member Spring Type Enumeration
            parameters (list of lists): List of Parameters for Spring Nonlinearity
                for definition_type == 'PARTIAL_ACTIVITY':
                    parameters = [negative zone, positive zone]
                    for negative/positive zone[0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                        negative/positive zone = [negative/positive zone type (enum), slippage (float)]
                    for negative/positive zone[0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED:
                        negative/positive zone = [negative/positive zone type (enum), slippage (float), displacement (float)]  (Note: Displacement must be greater than slippage)
                    for negative/positive zone[0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE/PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                        negative/positive zone = [negative/positive zone type (enum), slippage (float), force (float)]
                for definition_type == 'DIAGRAM':
                    parameters = [[symmetric(bool), LineReleaseDiagram Enumeration(start), LineReleaseDiagram Enumeration(end)], [[displacement, force],...]]
            axial_stiffness (float): Axial Stiffness
            self_weight (list): Self Weight Parameters List
                for self_weight[0] == 'MASS':
                    self_weight = [MemberSpringSelfWeightDefinition.MASS, mass (float)]
                for self_weight[0] == 'MASS_PER_LENGTH':
                    self_weight = [MemberSpringSelfWeightDefinition.MASS_PER_LENGTH, mass_per_length (float)]
                for self_weight[0] == 'SPECIFIC_WEIGHT':
                    self_weight = [MemberSpringSelfWeightDefinition.SPECIFIC_WEIGHT, specific_weight (float), section_area (float)]
            name (str, option): User Defined Design Support Name
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Member Hinge
        clientObject = model.clientModel.factory.create('ns0:member_spring')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Spring No.
        clientObject.no = no

        # Assigned Member
        clientObject.assigned_to = ConvertToDlString(member)

        # Member Spring Type
        clientObject.definition_type = definition_type.name

        # Spring Nonlinearity
        if definition_type.name == 'PARTIAL_ACTIVITY':

            # Negative Zone
            clientObject.partial_activity_along_x_negative_type = parameters[0][0].name

            if parameters[0][0].name == "PARTIAL_ACTIVITY_TYPE_COMPLETE":
                clientObject.partial_activity_along_x_negative_slippage = parameters[0][1]

            elif parameters[0][0].name == "PARTIAL_ACTIVITY_TYPE_FIXED":
                clientObject.partial_activity_along_x_negative_slippage = parameters[0][1]
                clientObject.partial_activity_along_x_negative_displacement = parameters[0][2]

            elif parameters[0][0].name == ("PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE" or "PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE"):
                clientObject.partial_activity_along_x_negative_slippage = parameters[0][1]
                clientObject.partial_activity_along_x_negative_force = parameters[0][2]

            # Positive Zone
            clientObject.partial_activity_along_x_positive_type = parameters[1][0].name

            if parameters[1][0].name == "PARTIAL_ACTIVITY_TYPE_COMPLETE":
                clientObject.partial_activity_along_x_positive_slippage = parameters[1][1]

            elif parameters[1][0].name == "PARTIAL_ACTIVITY_TYPE_FIXED":
                clientObject.partial_activity_along_x_positive_slippage = parameters[1][1]
                clientObject.partial_activity_along_x_positive_displacement = parameters[1][1]

            elif parameters[1][0].name == ("PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE" or "PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE"):
                clientObject.partial_activity_along_x_positive_slippage = parameters[1][1]
                clientObject.partial_activity_along_x_positive_force = parameters[1][2]

        elif definition_type.name == 'DIAGRAM':

            clientObject.diagram_along_x_symmetric = parameters[0][0]
            clientObject.diagram_along_x_is_sorted = True

            if parameters[0][0]:
                clientObject.diagram_along_x_start = parameters[0][1].name
                clientObject.diagram_along_x_end = parameters[0][1].name

            else:
                clientObject.diagram_along_x_start = parameters[0][1].name
                clientObject.diagram_along_x_end = parameters[0][2].name

            clientObject.diagram_along_x_table = model.clientModel.factory.create('ns0:member_spring.diagram_along_x_table')

            for i,j in enumerate(parameters[1]):
                msdx = model.clientModel.factory.create('ns0:member_spring_diagram_along_x_table_row')
                msdx.no = i+1
                msdx.row = model.clientModel.factory.create('ns0:member_spring_diagram_along_x_table')
                clearAttributes(msdx.row)
                msdx.row.displacement = parameters[1][i][0]
                msdx.row.force = parameters[1][i][1]

                clientObject.diagram_along_x_table.member_spring_diagram_along_x_table.append(msdx)

        # Axial Stiffness
        clientObject.axial_stiffness = axial_stiffness

        # Self Weight
        clientObject.self_weight_definition = self_weight[0].name

        if self_weight[0].name == 'MASS':
            clientObject.mass = self_weight[1]

        elif self_weight[0].name == 'MASS_PER_LENGTH':
            clientObject.mass_per_length = self_weight[1]

        elif self_weight[0].name == 'SPECIFIC_WEIGHT':
            clientObject.specific_weight = self_weight[1]
            clientObject.section_area = self_weight[2]

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

        # Add Member Spring to client model
        model.clientModel.service.set_member_spring(clientObject)

