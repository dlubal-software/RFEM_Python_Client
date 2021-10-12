from RFEM.initModel import *
from RFEM.enums import AnalysisType

class LoadCombination():
    def __init__(self,
                 no: int = 1,
                 load_combination_name: str = 'CO1',
                 comment: str = 'Comment',
                 params: dict = {}):
                 

        # Client model | Load Combination
        clientObject = clientModel.factory.create('ns0:load_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Load Case No.
        clientObject.no = no

        # Load Case Name
        clientObject.name = load_combination_name

        # Analysis Type
        clientObject.analysis_type = AnalysisType.ANALYSIS_TYPE_STATIC.name
        clientObject.static_analysis_settings = 1

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Combination to client model
        clientModel.service.set_load_combination(clientObject)


    def StaticAnalysis(self,
                 no: int = 1,
                 name: str = 'CO1',
                 to_solve: bool = True,
                 analysis_settings_no: int = 1,
                 design_situation = int = 1,
                 comment: str = 'Comment',
                 params: dict = {}):

        """
         Args:
            no (int): Load Combination Tag
            load_combination_name (str): Load Combination Name
            to_solve (bool): Enable/Disbale Load Combination Solver Status
            analysis_settings_no (int): Analysis Settings Number
            design_situation (int): Design Situation Number
            comment (str, optional): Comments 
            params (dict, optional): Parameters
        """

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
        clientObject.analysis_type = AnalysisType.ANALYSIS_TYPE_STATIC.name

        # Analysis Type Settings Number
        clientObject.static_analysis_settings = analysis_settings_no
        
        # Design Situation
        clientObject.design_situation = design_situation

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Combination to client model
        clientModel.service.set_load_combination(clientObject)
