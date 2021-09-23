from RFEM.initModel import *
from RFEM.enums import AnalysisType

class LoadCase():
    def __init__(self,
                 no: int = 1,
                 name: str = 'Self-weight',
                 to_solve: bool = True,
                 analysis_type = AnalysisType.ANALYSIS_TYPE_STATIC,
                 analysis_settings_no: int = 1,
                 action_category: str = 'Permanent | G',
                 self_weight = [True, 0.0, 0.0, 10.0],
                 comment: str = 'Comment',
                 params: dict = {}):
        '''
        for self-weight considerations:
            self_weight = [True, self_weight_factor_x, self_weight_factor_y, self_weight_factor_z]
        
        for no self-weight considerations:
            self_weight = [False]
        '''

        # Client model | Load Case
        clientObject = clientModel.factory.create('ns0:load_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Load Case No.
        clientObject.no = no

        # Load Case Name
        clientObject.name = name

        # To Solve
        clientObject.to_solve = to_solve

        # Analysis Type
        clientObject.analysis_type = analysis_type.name

        # Analysis Settings No.
        if analysis_type == AnalysisType.ANALYSIS_TYPE_STATIC:
            clientObject.static_analysis_settings = analysis_settings_no

        # Action Category
        clientObject.action_category = action_category

        # Self-weight Considerations
        clientObject.self_weight_active = self_weight[0]
        if type(self_weight[0]) != bool:
            raise Exception('WARNING: Entry at index 0 of Self-Weight parameter to be of type bool')
        if self_weight[0] == True:
            if len(self_weight) != 4:
                raise Exception('WARNING: Self-weight is activated and therefore requires a list definition of length 4. Kindly check list inputs for completeness and correctness.')
            clientObject.self_weight_factor_x = self_weight[1]
            clientObject.self_weight_factor_y = self_weight[2]
            clientObject.self_weight_factor_z = self_weight[3]
        elif self_weight[0] == False:
            if len(self_weight) != 1:
                raise Exception('WARNING: Self-weight is deactivated and therefore requires a list definition of length 1. Kindly check list inputs for completeness and correctness.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Case to client model
        clientModel.service.set_load_case(clientObject)

#   ACTION CATEGORIES ACCESSED USING WIZDLER. EXACT STRING NEEDS TO BE PASSED AS ACTION CATEGORY IN THE CODE
#   G
#   Permanent/Imposed | Gq
#   Prestress | P
#   Imposed loads - category A: domestic, residential areas | QI A
#   Imposed loads - category B: office areas | QI B
#   Imposed loads - category C: congregation areas | QI C
#   Imposed loads - category D: shopping areas | QI D
#   Imposed loads - category E: storage areas | QI E
#   Imposed loads - category F: traffic area - vehicle weight &lt;= 30 kN | QI F
#   Imposed loads - category G: traffic area - vehicle weight &lt;= 160 kN | QI G
#   Imposed loads - category H: roofs | QI H
#   Snow / Ice loads - Finland, Island, ... | Qs
#   Snow / Ice loads - H &gt; 1000 m | Qs
#   Snow / Ice loads - H &lt;= 1000 m | Qs
#   Wind | Qw
#   Temperature (non-fire) | QT
#   Accidental actions | A
#   Seismic actions | AE


