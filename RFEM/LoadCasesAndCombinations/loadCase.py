from RFEM.initModel import *
from RFEM.enums import AnalysisType

class LoadCase():
    def __init__(self,
                 no: int = 1,
                 name: str = 'Self-weight',
                 analysis_type = AnalysisType.ANALYSIS_TYPE_STATIC,
                 analysis_settings_no: int = 1,
                 action_category: int = 1,
                 active_self_weight: bool = False,
                 self_weight_factor_X: float = 0.0,
                 self_weight_factor_Y: float = 0.0,
                 self_weight_factor_Z: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Load Case
        clientObject = clientModel.factory.create('ns0:load_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Load Case No.
        clientObject.no = no

        # Load Case Name
        clientObject.name = name

        # Analysis Type
        clientObject.analysis_type = analysis_type.name

        # Analysis Settings No.
        if analysis_type == AnalysisType.ANALYSIS_TYPE_STATIC:
            clientObject.static_analysis_settings = analysis_settings_no
        else:
            printInitErr('Load Case', no, 'Static Analysis Settings')

        '''
        Todo!!!
        Action Category
        clientObject.action_category = action_category
        '''

        # Active Self-weight
        clientObject.self_weight_active = active_self_weight

        # Self-weight Factor in direction X
        clientObject.self_weight_factor_x = self_weight_factor_X

        # Self_weight Factor in direction Y
        clientObject.self_weight_factor_y = self_weight_factor_Y

        # Self_weight Factor in direction Z
        clientObject.self_weight_factor_z = self_weight_factor_Z

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Case to client model
        clientModel.service.set_load_case(clientObject)
