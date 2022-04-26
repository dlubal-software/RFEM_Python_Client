from RFEM.initModel import Model, clearAtributes, ConvertToDlString

class Opening():
    def __init__(self,
                 no: int = 1,
                 lines_no: str = '1 2 3 4',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Opening Tag
            lines_no (str): Tags of Lines defining Opening
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        '''

        # Client model | Opening
        clientObject = model.clientModel.factory.create('ns0:opening')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Opening No.
        clientObject.no = no

        # Boundary Lines No.
        clientObject.boundary_lines = ConvertToDlString(lines_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Opening to client model
        model.clientModel.service.set_opening(clientObject)
