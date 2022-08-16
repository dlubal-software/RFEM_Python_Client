from RFEM.initModel import Model, clearAtributes, GetAddonStatus, SetAddonStatus
from RFEM.enums import DirectionalComponentCombinationRule, PeriodicResponseCombinationRule, CqsDampingRule, AddOn

class SpectralAnalysisSettings():

    def __init__(self,
                 no: int = 1,
                 name: str = 'SRSS | SRSS',
                 periodic_combination = PeriodicResponseCombinationRule.SRSS,
                 directional_combination = DirectionalComponentCombinationRule.SRSS,
                 equivalent_linear_combination : bool = False,
                 save_mode_results : bool = False,
                 signed_dominant_mode_results : bool = False,
                 directional_component_scale_value : float = 0.3,
                 damping_for_cqc_rule = CqsDampingRule.CONSTANT_FOR_EACH_MODE,
                 constant_d_for_each_mode: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Sprectral Analysis Settings Tag
            name (str): Sprectral Analysis Settings Name
            periodic_combination (enum): Periodic Combination Rule Enumeration
            directional_combination (enum): Directional Component Combination Rule Enumeration
            equivalent_linear_combination (bool): Equivalent Linear Combination Boolean
            save_mode_results (bool): Save Mode Results Boolean
            signed_dominant_mode_results (bool): Signed Dominant Mode Results Boolean
            directional_component_scale_value (float): Directional Component Scale Value
            damping_for_cqc_rule (enum): Cqs Damping Rule Enumeration
            constant_d_for_each_mode (float): Constant d for Each Mode
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Check if Spectral Add-on is active.
        if not GetAddonStatus(Model.clientModel, AddOn.spectral_active):
            SetAddonStatus(Model.clientModel, AddOn.spectral_active)

        # Client model | Surface
        clientObject = model.clientModel.factory.create('ns0:spectral_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        clientObject.name = name
        clientObject.user_defined_name_enabled = True

        # Periodic Combination
        clientObject.combination_rule_for_periodic_responses = periodic_combination.name

        # Directional Component
        clientObject.combination_rule_for_directional_components = directional_combination.name

        # Equivalent Linear Combination
        clientObject.use_equivalent_linear_combination = equivalent_linear_combination

        # Save Results of All Selected Modes
        clientObject.save_results_of_all_selected_modes = save_mode_results

        # CURRENTLY DEACTIVATED IN RFEM
        # Signed Results Using Dominant Mode
        clientObject.signed_results_using_dominant_mode = signed_dominant_mode_results
        '''
        if signed_dominant_mode_results:
            if directional_combination != DirectionalComponentCombinationRule.SCALED_SUM:
                raise Exception("WARNING: Signed results using dominant mode is only available with Scaled Sum Directional Combination.")
        '''

        # Further Options
        if directional_combination == DirectionalComponentCombinationRule.SCALED_SUM:
            clientObject.combination_rule_for_directional_components_value = directional_component_scale_value

        if periodic_combination == PeriodicResponseCombinationRule.CQC:
            clientObject.damping_for_cqc_rule = damping_for_cqc_rule.name
            clientObject.constant_d_for_each_mode = constant_d_for_each_mode

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]
        # Add Static Analysis Settings to client model
        model.clientModel.service.set_spectral_analysis_settings(clientObject)
