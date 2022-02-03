from RFEM.initModel import Model, clearAtributes, ConvertToDlString

class Opening():
    def __init__(self,
                 no: int = 1,
                 lines_no: str = '1 2 3 4',
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Opening Tag
            lines_no (str): Tags of Lines defining Opening
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Opening
        clientObject = Model.clientModel.factory.create('ns0:opening')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Opening No.
        clientObject.no = no

        # Boundary Lines No.
        clientObject.boundary_lines = ConvertToDlString(lines_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Opening to client model
        Model.clientModel.service.set_opening(clientObject)
