from RFEM.initModel import Model, ConvertToDlString, clearAtributes
from RFEM.enums import *

class LinesetLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 linesets_no: str = '1',
                 load_direction = LoadDirectionType.LOAD_DIRECTION_LOCAL_Z,
                 magnitude: float = 0,
                 comment: str = '',
                 params: dict = {}):
        '''
        Assigns lineset load without any further options.
        Load type is Force by default.
        Load distribution is Uniform by default.
        '''

        # Client model | Lineset Load
        clientObject = Model.clientModel.factory.create('ns0:line_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Lineset Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Line No. (e.g. '5 6 7 12')
        clientObject.line_sets = ConvertToDlString(linesets_no)

        # Lineset Load Type
        load_type = LinesetLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Lineset Load Distribution
        load_distribution = LinesetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM
        clientObject.load_distribution = load_distribution.name

        # Lineset Load Direction
        clientObject.load_direction = load_direction.name

        # Load Magnitude
        clientObject.magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Lineset Load to client model
        Model.clientModel.service.set_line_set_load(load_case_no, clientObject)

        pass