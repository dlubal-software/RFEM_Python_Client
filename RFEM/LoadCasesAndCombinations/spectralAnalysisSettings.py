from RFEM.initModel import Model, clearAtributes
from RFEM.enums import DirectionalComponentCombinationRule, PeriodicResponseCombinationRule, CqsDampingRule

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
                 params: dict = {}):

        # Client model | Surface
        clientObject = Model.clientModel.factory.create('ns0:spectral_analysis_settings')

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

        # Signed Results Using Dominant Mode
        clientObject.signed_results_using_dominant_mode = signed_dominant_mode_results

        if signed_dominant_mode_results :
            if directional_combination == DirectionalComponentCombinationRule.SCALED_SUM:
                pass
            else:
                raise "WARNING: Signed results using dominant mode is only available with Scaled Sum Directional Combination!"

        # Further Options
        if directional_combination == DirectionalComponentCombinationRule.SCALED_SUM:
            clientObject.combination_rule_for_directional_components_value = directional_component_scale_value

        if periodic_combination == PeriodicResponseCombinationRule.CQC:
            clientObject.damping_for_cqc_rule = damping_for_cqc_rule.name
            clientObject.constant_d_for_each_mode = constant_d_for_each_mode

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]
        # Add Static Analysis Settings to client model
        Model.clientModel.service.set_spectral_analysis_settings(clientObject)
