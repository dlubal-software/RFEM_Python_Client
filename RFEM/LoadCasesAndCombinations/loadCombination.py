from RFEM.initModel import Model, clearAtributes
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
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Combination Tag
            analysis_type (enum): Analysis Type Enumeration
            design_situation (int): Design Situation
            user_defined_name (list): User defined Combination Name
            static_analysis_settings (int): Static Analysis Settings Number
            consider_imperfection (bool): Consider Imperfection Options
            consider_initial_state (bool): Consider Initial State
            structure_modification (bool): Enable/Disable Structure Modification
            to_solve (bool): Decide to solve
            combination_items (list of list): Combination Items
                for Combination Items;
                    combination_items = [[factor, load_case, action, is_leading],...]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Load Combination
        clientObject = model.clientModel.factory.create('ns0:load_combination')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Items
        clientObject.items = model.clientModel.factory.create('ns0:load_combination.items')

        for i,j in enumerate(combination_items):
            mlvlp = model.clientModel.factory.create('ns0:load_combination_items_row')
            mlvlp.no = i+1
            mlvlp.row.factor = combination_items[i][0]
            mlvlp.row.load_case = combination_items[i][1]
            mlvlp.row.action = combination_items[i][2]
            mlvlp.row.is_leading = combination_items[i][3]
            mlvlp.row.gamma=0
            mlvlp.row.psi=0
            mlvlp.row.xi=0
            mlvlp.row.k_fi=0
            mlvlp.row.c_esl=0
            mlvlp.row.k_def=0
            mlvlp.row.psi_0=0
            mlvlp.row.psi_1=0
            mlvlp.row.psi_2=0
            mlvlp.row.fi=0
            mlvlp.row.gamma_0=0
            mlvlp.row.alfa=0
            mlvlp.row.k_f=0
            mlvlp.row.phi=0
            mlvlp.row.rho=0
            mlvlp.row.omega_0=0
            mlvlp.row.gamma_l_1=0
            mlvlp.row.k_creep=0
            mlvlp.row.shift=0
            mlvlp.row.amplitude_function_type = "CONSTANT"


            clientObject.items.load_combination_items.append(mlvlp)

        # Add Load Combination to client model
        model.clientModel.service.set_load_combination(clientObject)
