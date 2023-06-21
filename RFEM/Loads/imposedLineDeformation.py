from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString

class ImposedLineDeformation():

    LineDeformationParams = {'imposed_displacement_line_start_x' : 0.0,
                            'imposed_displacement_line_start_y' : 0.0,
                            'imposed_displacement_line_start_z': 0.003,
                            'imposed_rotation_line_start' : 0.0,
                            'imposed_displacement_line_end_x': 0.0,
                            'imposed_displacement_line_end_y': 0.0,
                            'imposed_displacement_line_end_z': 0.0002,
                            'imposed_rotation_line_end': 0.0}

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 line_no: str = '1',
                 comment: str = '',
                 params: dict = LineDeformationParams,
                 model = Model):

        '''
        Args:
            no (int): Load Tag
            load_case_no (int): Assigned Load Case
            line_no (str): Assigned line(s)
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Imposed Line Deformation
        clientObject = model.clientModel.factory.create('ns0:imposed_line_deformation')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Line No.
        clientObject.lines = ConvertToDlString(line_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Nodal Support to client model
        model.clientModel.service.set_imposed_line_deformation(load_case_no, clientObject)
