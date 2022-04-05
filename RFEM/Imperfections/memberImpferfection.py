from RFEM.initModel import Model, clearAtributes, ConvertToDlString

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
                   members: str ='1',
                   sway: float =300.0, # Das muss in clientObject eingefügt werden.
                   direction: , # Da muss eine Aufzählung definiert werden.
                   comment: str = '',
                   params: dict = {}):
        '''
        Args:
            no (int): Member Imperfection Tag
            imperfection_case_no (int): number of imperfection case for this member imperfection
            members (str) : List of member numbers
            sway (float):
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''
        # Hier geht es weiter!
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

    def InitalBow(self,
                   ):
        pass

    def InitalBowAndCriterion(self,
                   ):
        pass
