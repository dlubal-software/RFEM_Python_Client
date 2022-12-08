from RFEM.initModel import Model, clearAttributes, GetAddonStatus
from RFEM.enums import DefinitionType, AddOn

class CombinationWizard():

    def __init__(self,
                no: int = 1,
                name: str = 'Load Wizard 1',
                static_analysis_settings: int = 1,
                comment: str = '',
                params: dict = None,
                model = Model
                ):

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
    def StaticAnalysisSettings(
                static_analysis_setting: int = 1,
                model = Model):

            clientObject = model.clientModel.factory.create('ns0:combination_wizard')

            clientObject.static_analysis_setting = static_analysis_setting


    #Setting imperfection case
    @staticmethod
    def ImperfectionCase(
                consider_imperfection_case: bool = False,
                model = Model):

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clearAttributes(clientObject)
        clientObject.consider_imperfection_case = consider_imperfection_case
        model.clientModel.service.set_combination_wizard(clientObject)

    #Setting stability analysis
    def StabilityAnalyis(
                stability_analysis: bool = True,
                stability_analysis_setting: int = 1,
                model = Model):

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clientObject.stability_analysis = stability_analysis
        clientObject.stability_analysis_setting = stability_analysis_setting

    #Setting imperfections
    def Imperfection(
                consider_imperfection_case: bool = True,
                generate_same_CO_without_IC: bool = True,
                model = Model):

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clientObject.consider_imperfection_case = consider_imperfection_case
        clientObject.generate_same_CO_without_IC = generate_same_CO_without_IC

    #Setting options II
    def OptionsII(
                user_defined_action_combinations: bool = False,
                favorable_permanent_actions: bool = False,
                reduce_number_of_generated_combinations: bool = False,
                auxiliary_combinations: bool = False,
                model = Model):

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')

        clientObject.user_defined_action_combinations = user_defined_action_combinations
        clientObject.favorable_permanent_actions = favorable_permanent_actions
        clientObject.reduce_number_of_generated_combinations = reduce_number_of_generated_combinations
        clientObject.auxiliary_combinations = auxiliary_combinations


    #setting result combinations
    def ResultCombination(
                generate_subcombinations_of_type_superposition: bool = False,
                model = Model):

        clientObject = model.clientModel.factory.create('ns0:combination_wizard')
        clientObject.generate_subcombinatons_of_type_superposition = generate_subcombinations_of_type_superposition


    #setting initial state
    def SetInitialState(
                consider_initial_state: bool = False,
                initial_state_case: int = 1,
                initial_state_definition_type: str = '',
                model = Model):

            clientObject = model.clientModel.factory.create('ns0:combination_wizard')
            clientObject.consider_initial_state = consider_initial_state
            clientObject.initial_state_case = initial_state_case
            clientObject.initial_state_definition_type = initial_state_definition_type

    #setting structure modifiication
    def StructureModification(
                structure_modification_enabled: bool = False,
                structure_modification: int = 1,
                model = Model):

            clientObject = model.clientModel.factory.create('ns0:combination_wizard')
            clientObject.structure_modification_enabled = structure_modification_enabled
            clientObject.structure_modificaton = structure_modification
