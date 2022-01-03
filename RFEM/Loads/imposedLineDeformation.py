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


        pass
