from RFEM.initModel import Model, clearAttributes

class ImperfectionCase():
    def __init__(self,
                 no: int = 1,
                 assigned_to_load_cases: str = '1',
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
        clearAttributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Assign to Load Cases
        clientObject.assigned_to_load_cases = assigned_to_load_cases

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Imperfection Case to client model
        Model.clientModel.service.set_imperfection_case(clientObject)
