from RFEM.initModel import Model, clearAttributes, GetAddonStatus
from RFEM.enums import DefinitionType, AddOn

class CombinationWizard():
    def __init__(self,
                no: int = 1,
                name: str = 'Load Wizard 1',
                generate_combinations: str = 'GENERATE_LOAD_COMBINATIONS',
                static_analysis_settings: int = 1,
                comment: str = '',
                params: dict = None,
                model = Model
                ):

        """
        Args:
            no (int): combination wizard tag
            name (str, optional): User-Defined name
            generate_combinatios: Which combinations should be created by wizard:
                                  GENERATE_LOAD_COMBINATIONS/GENERATE_RESULT_COMBINATIONS
            static_analysis_settings (int): Analysis Settings requiered to do combinations
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        #Client Model | Combination Wizard
        clientObject = model.clientModel.factory.create('ns0:combination_wizard')

        #Clear all attributes
        clearAttributes(clientObject)

        #Set Combination Wizard no.
        clientObject.no = no

        #Combination Wizard name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        #What to generate

        clientObject.generate_combinations = generate_combinations

        if generate_combinations == 'GENERATE_LOAD_COMBINATIONS':

            #Statical Analysis Model
            clientObject.static_analysis_settings = static_analysis_settings

        #Comment
        if comment:
            clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        model.clientModel.service.set_combination_wizard(clientObject)


    #Setting static analysis settings
    @staticmethod
    def StaticAnalysisSettings(
                no: int = 1,
                static_analysis_setting: int = 1,
                model = Model):

        """
        Args:
            no (int): combination wizard to be edited
            static_analysis_settings (int): Analysis Settings requiered to do combinations
            model (RFEM Class, optional): Model to be edited
        """

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clearAttributes(clientObject)
        clientObject.no = no
        clientObject.static_analysis_settings = static_analysis_setting
        model.clientModel.service.set_combination_wizard(clientObject)



    #Setting stability analysis
    @staticmethod
    def StabilityAnalyis(
                no: int = 1,
                has_stability_analysis: bool = True,
                stability_analysis_setting: int = 1,
                model = Model):

        """
        Args:
            no (int): combination wizard to be edited
            has_stabililty_analysis (bool): Enable/Disable Stability Analysis
            model (RFEM Class, optional): Model to be edited
        """

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clearAttributes(clientObject)
        clientObject.no = no
        clientObject.has_stability_analysis = has_stability_analysis
        clientObject.stability_analysis_settings = stability_analysis_setting
        model.clientModel.service.set_combination_wizard(clientObject)



    #Setting imperfections
    @staticmethod
    def Imperfection(
                no: int = 1,
                consider_imperfection_case: bool = True,
                generate_same_CO_without_IC: bool = True,
                model = Model):

        """
        Args:
            no (int): combination wizard to be edited
            consider_imperfection_case (bool): Enable/Disable imperfection case
            generate_same_CO_without_IC (bool): Enable/Disable
            model (RFEM Class, optional): Model to be edited
        """

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clearAttributes(clientObject)
        clientObject.no = no
        clientObject.consider_imperfection_case = consider_imperfection_case
        clientObject.generate_same_CO_without_IC = generate_same_CO_without_IC
        model.clientModel.service.set_combination_wizard(clientObject)

    #Setting options II
    @staticmethod
    def OptionsII(
                no: int = 1,
                user_defined_action_combinations: bool = False,
                favorable_permanent_actions: bool = False,
                reduce_number_of_generated_combinations: bool = False,
                model = Model):

        """
        Args:
            no (int): combination wizard to be edited
            user_defined_action_combinations (bool): Enable/Disable
            favorable_permanent_actions (bool): Enable/Disable
            reduce_number_of_generated_combinations (bool): Enable/Disable
            model (RFEM Class, optional): Model to be edited
        """

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clearAttributes(clientObject)
        clientObject.no = no
        clientObject.user_defined_action_combinations = user_defined_action_combinations
        clientObject.favorable_permanent_actions = favorable_permanent_actions
        clientObject.reduce_number_of_generated_combinations = reduce_number_of_generated_combinations
        model.clientModel.service.set_combination_wizard(clientObject)


    #setting result combinations
    @staticmethod
    def ResultCombination(
                no: int = 1,
                generate_subcombinations_of_type_superposition: bool = False,
                model = Model):

        """
        Args:
            no (int): combination wizard to be edited
            generate_subcombinations_of_type_superposition (bool): Enable/Disable
            model (RFEM Class, optional): Model to be edited
        """

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clearAttributes(clientObject)
        clientObject.no = no
        clientObject.generate_subcombinations_of_type_superposition = generate_subcombinations_of_type_superposition
        model.clientModel.service.set_combination_wizard(clientObject)


    #Initial state
    #WS for setting initial state is missing
    @staticmethod
    def SetInitialState(
                no: int = 1,
                consider_initial_state: bool = False,
                initial_state_case: int = 1,
                initial_state_definition_type: str = 'DEFINITION_TYPE_FINAL_STATE',
                model = Model):

        """
        Args:
            no (int): combination wizard to be edited
            consider_initial_state (bool): Enable/Disable
            initial_state_case (int): No. of inital state
            initial_state_definition_type (str): Type of the initial state
            model (RFEM Class, optional): Model to be edited
        """

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clearAttributes(clientObject)
        clientObject.no = no
        clientObject.consider_initial_state = consider_initial_state
        clientObject.initial_state_case = initial_state_case
        clientObject.initial_state_definition_type = initial_state_definition_type

        model.clientModel.service.set_combination_wizard(clientObject)

    #setting structure modification
    #WS for new structure modification not yet available
    @staticmethod
    def StructureModification(
                no: int = 1,
                structure_modification_enabled: bool = False,
                structure_modification: int = 1,
                model = Model):

        """
        Args:
            no (int): combination wizard to be edited
            structure_modification_enabled (bool): Enable/Disable
            structure_modification (int): No. of strucutre modification
            model (RFEM Class, optional): Model to be edited
        """

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clearAttributes(clientObject)
        clientObject.no = no
        clientObject.structure_modification_enabled = structure_modification_enabled
        clientObject.structure_modification = structure_modification
        model.clientModel.service.set_combination_wizard(clientObject)
