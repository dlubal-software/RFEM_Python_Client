from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import LoadWizardType, InitialStateDefintionType

class CombinationWizard():
    def __init__(self,
                no: int = 1,
                name: str = '',
                static_analysis_settings: int = 1,
                stability_analysis_setting: int = 1,
                consider_imperfection_case: bool = True,
                generate_same_CO_without_IC: bool = True,
                initial_state_case: int = 1,
                initial_state_definition_type = InitialStateDefintionType.DEFINITION_TYPE_FINAL_STATE,
                structure_modification: int = 1,
                user_defined_action_combinations: bool = False,
                favorable_permanent_actions: bool = False,
                reduce_number_of_generated_combinations: bool = False,
                comment: str = '',
                params: dict = None,
                model = Model
                ):
        """
        Args:
            no (int): combination wizard tag
            name (str, optional): User-Defined name
            static_analysis_settings (int): Analysis Settings requiered to do combinations
            consider_imperfection_case (bool): enable/disable
            generate_same_CO_without_IC (bool): enable/disable
            initial_state_case (int): Initial state to be considered
            initial_state_definition_type (enum): Definition of initial state type enumeration
            structure_modification (int): structure modification to be considered
            user_defined_action_combinations (bool): enable/disable
            favorable_permanent_actions (bool): enable/diable
            reduce_number_of_generated_combinations (bool): enable/disable
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        #  Client Model | Combination Wizard
        clientObject = model.clientModel.factory.create('ns0:combination_wizard')

        # Clear all attributes
        clearAttributes(clientObject)

        # Set Combination Wizard no.
        clientObject.no = no

        # Combination Wizard name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # What to generate
        clientObject.generate_combinations = LoadWizardType.GENERATE_LOAD_COMBINATIONS.name

        # Statical Analysis Model
        clientObject.static_analysis_settings = static_analysis_settings

        # Setting stability analysisa
        if stability_analysis_setting:
            clientObject.has_stability_analysis = True
            clientObject.stability_analysis_settings = stability_analysis_setting

        # Setting imperfection case
        clientObject.consider_imperfection_case = consider_imperfection_case
        clientObject.generate_same_CO_without_IC = generate_same_CO_without_IC

        # Setting initial state
        if initial_state_case:
            clientObject.consider_initial_state = True
            clientObject.initial_state_case = initial_state_case
            clientObject.initial_state_definition_type = initial_state_definition_type.name

        # Setting structure modificication
        # WS for new structure modification not yet available
        if structure_modification:
            clientObject.structure_modification_enabled = True
            clientObject.structure_modification = structure_modification

        # Setting user defined action combinations
        if user_defined_action_combinations:
            clientObject.user_defined_action_combinations = user_defined_action_combinations

        # Setting favorable combinations
        if favorable_permanent_actions:
            clientObject.favorable_permanent_actions = favorable_permanent_actions

        # Reduce number of generated combinations
        if reduce_number_of_generated_combinations:
            clientObject.reduce_number_of_generated_combinations = reduce_number_of_generated_combinations

        # Comment
        if comment:
            clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Clearing unused attributes
        deleteEmptyAttributes(clientObject)

        # Setting the combination wizard
        model.clientModel.service.set_combination_wizard(clientObject)

    # Setting result combination
    @staticmethod
    def SetResultCombination(no: int = 1,
                name: str = '',
                stability_analysis_setting: int = 1,
                consider_imperfection_case: bool = False,
                generate_same_CO_without_IC: bool = True,
                user_defined_action_combinations: bool = False,
                favorable_permanent_actions: bool = False,
                generate_subcombinations_of_type_superposition: bool = False,
                comment: str = '',
                params: dict = None,
                model = Model
                ):
        """
        Args:
            no (int): combination wizard tag
            name (str, optional): User-Defined name
            stability_analysis_settings (int): stability settings requiered to do combinations
            consider_imperfection_case (bool): enable/disable
            generate_same_CO_without_IC (bool): enable/disable
            user_defined_action_combinations (bool): enable/disable
            favorable_permanent_actions (bool): enable/disable
            generate_subcombinations_of_type_superposition (bool): enable/disable
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client Model | Combination Wizard
        clientObject = model.clientModel.factory.create('ns0:combination_wizard')

        # Clear all attributes
        clearAttributes(clientObject)

        # Set Combination Wizard no.
        clientObject.no = no

        # Combination Wizard name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # What to generate
        clientObject.generate_combinations = LoadWizardType.GENERATE_RESULT_COMBINATIONS.name

        # Setting stability analysisa
        if stability_analysis_setting:
            clientObject.has_stability_analysis = True
            clientObject.stability_analysis_settings = stability_analysis_setting

        # Setting imperfection case
        clientObject.consider_imperfection_case = consider_imperfection_case

        # Setting additional setting for imperfection case
        clientObject.generate_same_CO_without_IC = generate_same_CO_without_IC

        # Setting user defined action combinations
        if user_defined_action_combinations:
            clientObject.user_defined_action_combinations = user_defined_action_combinations

        # Setting favorable combinations
        if favorable_permanent_actions:
            clientObject.favorable_permanent_actions = favorable_permanent_actions

        # Setting addition setting for sub - combinations
        clientObject.generate_subcombinations_of_type_superposition = generate_subcombinations_of_type_superposition

        # Comment
        if comment:
            clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Clearing unused attributes
        deleteEmptyAttributes(clientObject)

        # Setting the combination wizard
        model.clientModel.service.set_combination_wizard(clientObject)
