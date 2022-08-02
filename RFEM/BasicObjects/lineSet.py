from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import SetType

class LineSet():
    def __init__(self,
                 no: int = 1,
                 lines_no: str = '33 36 39 42 45',
                 line_set_type = SetType.SET_TYPE_CONTINUOUS,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Line Set Tag
            lines_no (str): Numbers of Lines Contained Within Line Set
            line_set_type (enum): Line Set Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Line Set
        clientObject = model.clientModel.factory.create('ns0:line_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Set No.
        clientObject.no = no

        # Lines number
        clientObject.lines = ConvertToDlString(lines_no)

        # Line Set Type
        clientObject.set_type = line_set_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line Set to client model
        model.clientModel.service.set_line_set(clientObject)

    @staticmethod
    def ContinuousLines(
                 no: int = 1,
                 lines_no: str = '33 36 39 42 45',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Line Set Tag
            lines_no (str): Numbers of Lines Contained Within Continuous Line Set
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Line Set
        clientObject = model.clientModel.factory.create('ns0:line_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Set No.
        clientObject.no = no

        # Lines number
        clientObject.lines = ConvertToDlString(lines_no)

        # Line Set Type
        clientObject.set_type = SetType.SET_TYPE_CONTINUOUS.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line Set to client model
        model.clientModel.service.set_line_set(clientObject)

    @staticmethod
    def GroupOfLines(
                 no: int = 1,
                 lines_no: str = '33 36 39 42 45',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Line Set Tag
            lines_no (str): Numbers of Lines Contained Within Group of Lines Line Set
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Line Set
        clientObject = model.clientModel.factory.create('ns0:line_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Set No.
        clientObject.no = no

        # Lines number
        clientObject.lines = ConvertToDlString(lines_no)

        # Line Set Type
        clientObject.set_type = SetType.SET_TYPE_GROUP.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line Set to client model
        model.clientModel.service.set_line_set(clientObject)
