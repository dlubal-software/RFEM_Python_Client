from RFEM.enums import ImperfectionType
from RFEM.initModel import Model, clearAtributes, ConvertToDlString

class ImperfectionCase():

    def __init__(self,
                 no: int = 1,
                 assigned_to_load_combinations: str ='',
                 assigned_to_load_cases: str = '',
                 comment: str = '',
                 params: dict = {}):
        '''
        Args:
            no (int): Imperfection Case Tag
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Imperfection Case
        clientObject = Model.clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Assign to Load Combinations
        if len(assigned_to_load_combinations) > 0:
            clientObject.assigned_to_load_combinations = ConvertToDlString(assigned_to_load_combinations)

        # Assign to Load Cases
        if len(assigned_to_load_cases) > 0:
            clientObject.assigned_to_load_cases = ConvertToDlString(assigned_to_load_cases)

        if len(assigned_to_load_cases) + len(assigned_to_load_combinations) == 0:
            print('Warning: An imperfection case should be assigned to a load case or load combination.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Imperfection Case to client model
        Model.clientModel.service.set_imperfection_case(clientObject)

    def Local(self,
              no: int = 1,
              assigned_to_load_combinations: str ='',
              assigned_to_load_cases: str = '',
              comment: str = '',
              params: dict = {}):
        '''
        Args:
            no (int): Imperfection Case Tag
            assigned_to_load_combinations (str, optional): Assigned Load Combinations
            assigned_to_load_cases (str, optional): Assigned Load Cases
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # assigned_to_load_combinations XY is first in parameter list because imperfections are
        # usually assigned to load combinations.

        # Client model | Imperfection Case
        clientObject = Model.clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Der Typ local muss übergeben werden. Der wird jetzt nur gesetzt, weil er default ist.
        clientObject.type = ImperfectionType.IMPERFECTION_TYPE_LOCAL_IMPERFECTIONS.name

        # Assign to Load Combinations
        if len(assigned_to_load_combinations) > 0:
            clientObject.assigned_to_load_combinations = ConvertToDlString(assigned_to_load_combinations)

        # Assign to Load Cases
        if len(assigned_to_load_cases) > 0:
            clientObject.assigned_to_load_cases = ConvertToDlString(assigned_to_load_cases)

        if len(assigned_to_load_cases) + len(assigned_to_load_combinations) == 0:
            print('Warning: An imperfection case should be assigned to a load case or load combination.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Imperfection Case to client model
        Model.clientModel.service.set_imperfection_case(clientObject)
