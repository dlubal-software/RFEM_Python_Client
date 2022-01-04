from RFEM.initModel import *
from RFEM.enums import *

class ImposedLineDeformation():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 line_no: str = '',
                 load_parameter = None,
                 comment: str = '',
                 params: dict = {}):

        '''
        load_parameter:
            load_parameter = [imposed_displacement_line_start_x, 
                              imposed_displacement_line_start_y, 
                              imposed_displacement_line_start_z, 
                              imposed_rotation_line_start, 
                              imposed_displacement_line_end_x, 
                              imposed_displacement_line_end_y, 
                              imposed_displacement_line_end_z, 
                              imposed_rotation_line_end]
        '''

        # Client model | Imposed Line Deformation
        clientObject = Model.clientModel.factory.create('ns0:imposed_line_deformation')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Line No.
        clientObject.lines = ConvertToDlString(line_no)

        # Load Parameter
        clientObject.imposed_displacement_line_start_x = load_parameter[0]
        clientObject.imposed_displacement_line_start_y = load_parameter[1]
        clientObject.imposed_displacement_line_start_z = load_parameter[2]
        clientObject.imposed_rotation_line_start = load_parameter[3]
        clientObject.imposed_displacement_line_end_x = load_parameter[4]
        clientObject.imposed_displacement_line_end_y = load_parameter[5]
        clientObject.imposed_displacement_line_end_z = load_parameter[6]
        clientObject.imposed_rotation_line_end = load_parameter[7]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Nodal Support to client model
        Model.clientModel.service.set_imposed_line_deformation(load_case_no, clientObject)
