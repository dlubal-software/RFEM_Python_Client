from RFEM.initModel import *
from RFEM.enums import SetType

class LineSet():
    def __init__(self,
                 no: int = 1,
                 lines_no: str = '33 36 39 42 45',
                 line_set_type = SetType.SET_TYPE_CONTINUOUS,
                 comment: str = ''):

        # Client model | Line Set
        clientObject = clientModel.factory.create('ns0:line_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Set No.
        clientObject.no = no

        # Lines number
        clientObject.lines = lines_no

        # Line Set Type
        clientObject.set_type = line_set_type.name

        # Comment
        clientObject.comment = comment

        # Add Line Set to client model
        clientModel.service.set_line_set(clientObject)

    def ContinuousLines(self,
                 no: int = 1,
                 lines_no: str = '33 36 39 42 45',
                 line_set_type = SetType.SET_TYPE_CONTINUOUS,
                 comment: str = ''):

        # Client model | Line Set
        clientObject = clientModel.factory.create('ns0:line_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Set No.
        clientObject.no = no

        # Lines number
        clientObject.lines = lines_no

        # Line Set Type
        clientObject.set_type = line_set_type.name

        # Comment
        clientObject.comment = comment

        # Add Line Set to client model
        clientModel.service.set_line_set(clientObject)

    def GroupOfLines(self,
                 no: int = 1,
                 lines_no: str = '33 36 39 42 45',
                 line_set_type = SetType.SET_TYPE_CONTINUOUS,
                 comment: str = ''):

        # Client model | Line Set
        clientObject = clientModel.factory.create('ns0:line_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Set No.
        clientObject.no = no

        # Lines number
        clientObject.lines = lines_no

        # Line Set Type
        clientObject.set_type = line_set_type.name

        # Comment
        clientObject.comment = comment

        # Add Line Set to client model
        clientModel.service.set_line_set(clientObject)
