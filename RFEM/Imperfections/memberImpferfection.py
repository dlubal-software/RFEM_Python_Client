from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import *

class MemberImperfection():
    '''
    Creates a member imperfection.
    An imperfection case must be created before.
    '''

    def __init__(self,
                 no: int = 1,
                 imperfection_case_no: int = 1,
                 members: str ='1',
                 comment: str = '',
                 params: dict = {}):
        '''
        Args:
            no (int): Member Imperfection Tag
            imperfection_case_no (int): number of imperfection case for this member imperfection
            members (str) : List of member numbers
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Imperfection Case
        clientObject = Model.clientModel.factory.create('ns0:member_imperfection')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Imperfection No.
        clientObject.no = no

        clientObject.members = ConvertToDlString(members)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Imperfection to client model
        Model.clientModel.service.set_member_imperfection(imperfection_case_no, clientObject)


    def InitialSwayRelative(self,
                            no: int = 1,
                            imperfection_case_no: int = 1,
                            members: str = '1',
                            sway: float = 300.0,
                            imperfection_direction = ImperfectionDirection.IMPERFECTION_DIRECTION_LOCAL_Y,
                            comment: str = '',
                            params: dict = {}):
        '''
        Args:
            no (int): Member Imperfection Tag
            imperfection_case_no (int): number of imperfection case for this member imperfection
            members (str) : List of member numbers
            sway (float):
            imperfection_direction
            comment (str, optional): Comments
            params (dict, optional): Additional parameters
        '''
        # Client model | Imperfection Case
        clientObject = Model.clientModel.factory.create('ns0:member_imperfection')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Imperfection No.
        clientObject.no = no

        clientObject.members = ConvertToDlString(members)

        # Sway

        clientObject.basic_value_relative = sway

        # Imperfection Direction

        clientObject.imperfection_direction = imperfection_direction.name

        clientObject.imperfection_type = 'IMPERFECTION_TYPE_INITIAL_SWAY'
        clientObject.definition_type = 'DEFINITION_TYPE_RELATIVE'

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Imperfection to client model
        Model.clientModel.service.set_member_imperfection(imperfection_case_no, clientObject)

    def InitialBowRelative(self,
                          no: int = 1,
                          imperfection_case_no: int = 1,
                          members: str = '1',
                          bow: float = 250.0,
                          imperfection_direction = ImperfectionDirection.IMPERFECTION_DIRECTION_LOCAL_Y,
                          comment: str = '',
                          params: dict = {}):
        '''
        Args:
            no (int): Member Imperfection Tag
            imperfection_case_no (int): number of imperfection case for this member imperfection
            members (str) : List of member numbers
            bow (float):
            imperfection_direction
            comment (str, optional): Comments
            params (dict, optional): Additional parameters
        '''
        # Client model | Imperfection Case
        clientObject = Model.clientModel.factory.create('ns0:member_imperfection')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Imperfection No.
        clientObject.no = no

        clientObject.members = ConvertToDlString(members)

        # Bow

        clientObject.basic_value_relative = bow

        # Imperfection Direction

        clientObject.imperfection_direction = imperfection_direction.name

        clientObject.imperfection_type = 'IMPERFECTION_TYPE_INITIAL_BOW'
        clientObject.definition_type = 'DEFINITION_TYPE_RELATIVE'

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Imperfection to client model
        Model.clientModel.service.set_member_imperfection(imperfection_case_no, clientObject)

    def InitialBowRelativeAndCriterion(self,
                                       no: int = 1,
                                       imperfection_case_no: int = 1,
                                       members: str = '1',
                                       active_criterion = ImperfectionActivationCriterion.ACTIVITY_CRITERION_ALWAYS,
                                       bow = [250.0],
                                       imperfection_direction = ImperfectionDirection.IMPERFECTION_DIRECTION_LOCAL_Y,
                                       comment: str = '',
                                       params: dict = {}):
        '''
        Args:
            no (int): Member Imperfection Tag
            imperfection_case_no (int): number of imperfection case for this member imperfection
            members (str) : List of member numbers
            bow (float):
            active_criterion ():
            imperfection_direction
            comment (str, optional): Comments
            params (dict, optional): Additional parameters
        '''
        # Client model | Imperfection Case
        clientObject = Model.clientModel.factory.create('ns0:member_imperfection')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Imperfection No.
        clientObject.no = no

        clientObject.members = ConvertToDlString(members)

        # Criterion
        clientObject.active_criterion = active_criterion.name

        if active_criterion == ImperfectionActivationCriterion.ACTIVITY_CRITERION_DEFINE:
            clientObject.active_bow = bow[1]

        # Bow
        clientObject.basic_value_relative = bow[0]

        # Imperfection Direction

        clientObject.imperfection_direction = imperfection_direction.name

        clientObject.imperfection_type = 'IMPERFECTION_TYPE_INITIAL_BOW_AND_CRITERION'
        clientObject.definition_type = 'DEFINITION_TYPE_RELATIVE'

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Imperfection to client model
        Model.clientModel.service.set_member_imperfection(imperfection_case_no, clientObject)
