from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString, ConvertStrToListOfInt
from RFEM.enums import ObjectTypes

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
            lines_no (str): Numbers of Lines defining Opening
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Opening
        clientObject = model.clientModel.factory.create('ns0:opening')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

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

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Opening to client model
        model.clientModel.service.set_opening(clientObject)

    @staticmethod
    def DeleteOpening(openings_no: str = '1 2', model = Model):

        '''
        Args:
            openings_no (str): Numbers of Openings to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete from client model
        for opening in ConvertStrToListOfInt(openings_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_OPENING.name, opening)
