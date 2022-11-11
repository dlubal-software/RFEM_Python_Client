from RFEM.initModel import Model, clearAttributes
from RFEM.enums import AnalysisType

class LoadCombination():
    def __init__(self,
                 no: int = 1,
                 analysis_type = AnalysisType.ANALYSIS_TYPE_STATIC,
                 design_situation: int = 1,
                 user_defined_name = [False],
                 static_analysis_settings: int = 1,
                 consider_imperfection: bool = False,
                 consider_initial_state: bool = False,
                 structure_modification: bool = False,
                 to_solve: bool = True,
                 combination_items = [[1.5, 1, 0, False]],
                 comment: str = '',
                 params: dict = {}):

        # Client model | Load Combination
        clientObject = Model.clientModel.factory.create('ns0:load_combination')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Load Combination No.
        clientObject.no = no

        # Analysis Type
        clientObject.analysis_type = analysis_type.name

        # Design Situation Assignment
        clientObject.design_situation = design_situation

        # Combination Name
        clientObject.user_defined_name_enabled = user_defined_name[0]
        if user_defined_name[0]:
            clientObject.name = user_defined_name[1]

        # Analysis Settings Assignment
        clientObject.static_analysis_settings = static_analysis_settings

        # Consider Imperfection Options
        clientObject.consider_imperfection = consider_imperfection

        # Consider Initial State
        clientObject.consider_initial_state = consider_initial_state

        # Structure Modification Enable
        clientObject.structure_modification_enabled = structure_modification

        # Decide to Solve
        clientObject.to_solve = to_solve

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Items
        clientObject.items = Model.clientModel.factory.create('ns0:load_combination.items')

        for i,j in enumerate(combination_items):
            mlvlp = Model.clientModel.factory.create('ns0:load_combination_items')
            mlvlp.no = i+1
            mlvlp.factor = combination_items[i][0]
            mlvlp.load_case = combination_items[i][1]
            mlvlp.action = combination_items[i][2]
            mlvlp.is_leading = combination_items[i][3]
            mlvlp.gamma=0
            mlvlp.psi=0
            mlvlp.xi=0
            mlvlp.k_fi=0
            mlvlp.c_esl=0
            mlvlp.k_def=0
            mlvlp.psi_0=0
            mlvlp.psi_1=0
            mlvlp.psi_2=0
            mlvlp.fi=0
            mlvlp.gamma_0=0
            mlvlp.alfa=0
            mlvlp.k_f=0
            mlvlp.phi=0
            mlvlp.rho=0
            mlvlp.omega_0=0
            mlvlp.gamma_l_1=0
            mlvlp.k_creep=0
            mlvlp.shift=0
            mlvlp.amplitude_function_type = "CONSTANT"


            clientObject.items.load_combination_items.append(mlvlp)

        # Add Load Combination to client model
        Model.clientModel.service.set_load_combination(clientObject)
