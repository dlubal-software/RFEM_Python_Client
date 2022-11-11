from RFEM.initModel import Model, clearAttributes
from RFEM.enums import AnalysisType

DIN_Action_Category = {'1A': 'Permanent | G', '1B': 'Permanent - small fluctuations | G*', '1C': 'Permanent/Imposed | Gq', '2': 'Prestress | P',
                        '3A': 'Imposed loads - category A: domestic, residential areas | QI A', '3B': 'Imposed loads - category B: office areas | QI B',
                        '3C': 'Imposed loads - category C: congregation areas | QI C', '3D': 'Imposed loads - category D: shopping areas | QI D',
                        '3E': 'Imposed loads - category E: storage areas | QI E', '3F': 'Imposed loads - category F: traffic area - vehicle weight <= 30 kN | QI F',
                        '3G': 'Imposed loads - category G: traffic area - vehicle weight <= 160 kN | QI G', '3H': 'Imposed loads - category H: roofs | QI H',
                        '4A': 'Snow / Ice loads - H <= 1000 m | Qs', '4B': 'Snow / Ice loads - H > 1000 m | Qs', '5': 'Wind | Qw', '6': 'Temperature (non-fire) | QT',
                        '7': 'Foundation subsidence | Qf', '8': 'Other actions | Qo', '9': 'Accidental actions | A', '10': 'Seismic actions | AE', 'None': 'None | None'}

class LoadCase():

    def __init__(self,
                 no: int = 1,
                 name: str = 'Self-weight',
                 self_weight: list = [True, 0.0, 0.0, 1.0],
                 comment: str = 'Comment',
                 params: dict = {}):
        '''
        Args:
            no (int): Load Case Tag
            name (str): Load Case Name
            self_weight (list): Self-Weight Parameters
                self_weight = [self_weight_active, self_weight_factor_x, self_weight_factor_y, self_weight_factor_z]
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Load Case
        clientObject = Model.clientModel.factory.create('ns0:load_case')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Load Case No.
        clientObject.no = no

        # Load Case Name
        clientObject.name = name

        # To Solve
        clientObject.to_solve = True

        # Analysis Type
        clientObject.analysis_type = AnalysisType.ANALYSIS_TYPE_STATIC.name
        clientObject.static_analysis_settings = 1

        # Action Category
        clientObject.action_category = 'Permanent | G'

        # Self-weight Considerations
        clientObject.self_weight_active = self_weight[0]
        if not isinstance(self_weight[0], bool):
            raise Exception('WARNING: Entry at index 0 of Self-Weight parameter to be of type bool')
        if self_weight[0]:
            if len(self_weight) != 4:
                raise Exception('WARNING: Self-weight is activated and therefore requires a list definition of length 4. Kindly check list inputs for completeness and correctness.')
            clientObject.self_weight_factor_x = self_weight[1]
            clientObject.self_weight_factor_y = self_weight[2]
            clientObject.self_weight_factor_z = self_weight[3]
        else:
            if len(self_weight) != 1:
                raise Exception('WARNING: Self-weight is deactivated and therefore requires a list definition of length 1. Kindly check list inputs for completeness and correctness.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Case to client model
        Model.clientModel.service.set_load_case(clientObject)

    def StaticAnalysis(self,
                 no: int = 1,
                 name: str = 'Self-weight',
                 to_solve: bool = True,
                 analysis_settings_no: int = 1,
                 action_category= DIN_Action_Category['1A'],
                 self_weight = [True, 0.0, 0.0, 10.0],
                 comment: str = 'Comment',
                 params: dict = {}):
        '''
        Args:
            no (int): Load Case Tag
            name (str): Load Case Name
            to_solve (bool): Enable/Disbale Load Case Solver Status
            analysis_type (enum): Analysis Type Enumeration
            analysis_settings_no (int): Analysis Settings Number
            action_category (dict): Action Category Key
                    1A      =   Permanent | G
                    1B      =   Permanent - small fluctuations | G*
                    1C      =   Permanent/Imposed | Gq
                    2       =   Prestress | P
                    3A      =   Imposed loads - category A: domestic, residential areas | QI A
                    3B      =   Imposed loads - category B: office areas | QI B
                    3C      =   Imposed loads - category C: congregation areas | QI C
                    3D      =   Imposed loads - category D: shopping areas | QI D
                    3E      =   Imposed loads - category E: storage areas | QI E
                    3F      =   Imposed loads - category F: traffic area - vehicle weight <= 30 kN | QI F
                    3G      =   Imposed loads - category G: traffic area - vehicle weight <= 160 kN | QI G
                    3H      =   Imposed loads - category H: roofs | QI H
                    4A      =   Snow / Ice loads - H <= 1000 m | Qs
                    4B      =   Snow / Ice loads - H > 1000 m | Qs
                    5       =   Wind | Qw
                    6       =   Temperature (non-fire) | QT
                    7       =   Foundation subsidence | Qf
                    8       =   Other actions | Qo
                    9       =   Accidental actions | A
                    10      =   Seismic actions | AE
                    None    =   None | None
            self_weight (list): Self-weight Considerations
                for self-weight considerations;
                    self_weight = [True, self_weight_factor_x, self_weight_factor_y, self_weight_factor_z]
                for no self-weight considerations;
                    self_weight = [False]
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Load Case
        clientObject = Model.clientModel.factory.create('ns0:load_case')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Load Case No.
        clientObject.no = no

        # Load Case Name
        clientObject.name = name

        # To Solve
        clientObject.to_solve = to_solve

        # Analysis Type
        clientObject.analysis_type = AnalysisType.ANALYSIS_TYPE_STATIC.name
        clientObject.static_analysis_settings = analysis_settings_no

        # Action Category
        clientObject.action_category = action_category

        # Self-weight Considerations
        clientObject.self_weight_active = self_weight[0]
        if not isinstance(self_weight[0], bool):
            raise Exception('WARNING: Entry at index 0 of Self-Weight parameter to be of type bool')
        if self_weight[0]:
            if len(self_weight) != 4:
                raise Exception('WARNING: Self-weight is activated and therefore requires a list definition of length 4. Kindly check list inputs for completeness and correctness.')
            clientObject.self_weight_factor_x = self_weight[1]
            clientObject.self_weight_factor_y = self_weight[2]
            clientObject.self_weight_factor_z = self_weight[3]
        else:
            if len(self_weight) != 1:
                raise Exception('WARNING: Self-weight is deactivated and therefore requires a list definition of length 1. Kindly check list inputs for completeness and correctness.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Case to client model
        Model.clientModel.service.set_load_case(clientObject)
