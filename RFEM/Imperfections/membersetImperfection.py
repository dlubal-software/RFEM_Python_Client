from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import MemberImperfectionType, MemberImperfectionDefinitionType
from RFEM.enums import ImperfectionDirection, MemberImperfectionActiveCriterion

class MemberSetImperfection():

    def __init__(self,
                 no: int = 1,
                 imperfection_case: int = 1,
                 member_sets: str ='1',
                 imperfection_type = MemberImperfectionType.IMPERFECTION_TYPE_INITIAL_SWAY,
                 definition_type = MemberImperfectionDefinitionType.DEFINITION_TYPE_ABSOLUTE,
                 imperfection_direction = ImperfectionDirection.IMPERFECTION_DIRECTION_LOCAL_Z,
                 parameters: list = [0.0022],
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Member Imperfection
        An imperfection case must be created before.

        Args:
            no (int): Member Set Imperfection Tag
            imperfection_case (int): Imperfection Case Number
            member_sets (str): Assigned to Member Sets
            imperfection_type (enum): Member Imperfection Type Enumeration
            definition_type (enum): Member Imperfection Definition Type Enumeration
            imperfection_direction (enum): Imperfection Direction Enumeration
            parameters (list): Parameters depending on Imperfection and Definition type
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Imperfection Case
        clientObject = model.clientModel.factory.create('ns0:member_set_imperfection')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Imperfection No.
        clientObject.no = no

        # Member Imperfection Type
        clientObject.imperfection_type = imperfection_type.name

        # Assigned to Members No.
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Imperfection Case
        clientObject.imperfection_case = imperfection_case

        # Definition Type
        clientObject.definition_type = definition_type.name


        # Imperfection Direction
        clientObject.imperfection_direction = imperfection_direction.name

        # Parameters
        if imperfection_type == MemberImperfectionType.IMPERFECTION_TYPE_INITIAL_SWAY:
            if definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_RELATIVE:
                clientObject.basic_value_relative = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_ABSOLUTE:
                clientObject.basic_value_absolute = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1993_1_1 or definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1992_1:
                clientObject.basic_value_relative = parameters[0]
                clientObject.height = parameters[1]
                clientObject.column_in_row = parameters[2]
                clientObject.reduction_factor_h = parameters[3]
                clientObject.reduction_factor_m = parameters[4]
                clientObject.initial_sway = parameters[5]
                clientObject.initial_sway_inverted = parameters[6]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1995_1_1:
                clientObject.basic_value_relative = parameters[0]
                clientObject.height = parameters[1]
                clientObject.reduction_factor_h = parameters[2]
                clientObject.initial_sway = parameters[3]
                clientObject.initial_sway_inverted = parameters[4]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_ANSI_CURRENT:
                clientObject.basic_value_coefficient = parameters[0]
                clientObject.standard_factor_enumeration = parameters[1].name
                clientObject.standard_factor_number = parameters[2]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_GB_50017_2017_GRAVITY_LOAD:
                clientObject.basic_value_coefficient = parameters[0]
                clientObject.standard_factor_enumeration = parameters[1].name
                clientObject.standard_factor_number = parameters[2]
                clientObject.case_object = parameters[3]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_CSA_CURRENT:
                clientObject.basic_value_coefficient = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_CSA_GRAVITY_LOAD:
                clientObject.basic_value_coefficient = parameters[0]
                clientObject.case_object = parameters[1]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_GB_50017_2017_CURRENT:
                clientObject.basic_value_relative = parameters[0]
                clientObject.height = parameters[1]
                clientObject.number_of_floors = parameters[2]
                clientObject.delta = parameters[3]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_GB_50017_2017_GRAVITY_LOAD:
                clientObject.basic_value_coefficient = parameters[0]
                clientObject.number_of_floors = parameters[1]
                clientObject.case_object = parameters[2]
            else:
                assert False, 'Wrong MemberImperfectionDefinitionType for IMPERFECTION_TYPE_INITIAL_SWAY'

        elif imperfection_type == MemberImperfectionType.IMPERFECTION_TYPE_INITIAL_BOW:
            if definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_RELATIVE:
                clientObject.basic_value_relative = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_ABSOLUTE:
                clientObject.basic_value_absolute = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1993_1_1:
                clientObject.section_design = parameters[0].name
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1995_1_1:
                clientObject.basic_value_relative = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1999_1_1:
                clientObject.section_design = parameters[0].name
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_ANSI_CURRENT:
                clientObject.basic_value_relative = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_ANSI_GRAVITY_LOAD:
                clientObject.basic_value_relative = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_CSA_CURRENT:
                clientObject.basic_value_relative = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_CSA_GRAVITY_LOAD:
                clientObject.basic_value_relative = parameters[0]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_GB_50017_2017:
                #clientObject. = parameters[0] # TODO: possibly missing parameter Buckling Curve = a - d
                pass
            else:
                assert False, 'Wrong MemberImperfectionDefinitionType for IMPERFECTION_TYPE_INITIAL_BOW'

        elif imperfection_type == MemberImperfectionType.IMPERFECTION_TYPE_INITIAL_BOW_AND_CRITERION:
            if definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_RELATIVE:
                clientObject.basic_value_relative = parameters[0]
                clientObject.active_criterion = parameters[1].name
                if clientObject.active_criterion == MemberImperfectionActiveCriterion.ACTIVITY_CRITERION_DEFINE:
                    clientObject.active_bow = parameters[2]
            elif definition_type == MemberImperfectionDefinitionType.DEFINITION_TYPE_ABSOLUTE:
                clientObject.basic_value_absolute = parameters[0]
                clientObject.active_criterion = parameters[1].name
                if clientObject.active_criterion == MemberImperfectionActiveCriterion.ACTIVITY_CRITERION_DEFINE:
                    clientObject.active_bow = parameters[2]
            else:
                assert False, 'Wrong MemberImperfectionDefinitionType for IMPERFECTION_TYPE_INITIAL_BOW_AND_CRITERION'
        else:
            assert False, 'Wrong MemberImperfectionDefinitionType'

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Imperfection to client model
        model.clientModel.service.set_member_set_imperfection(imperfection_case, clientObject)
