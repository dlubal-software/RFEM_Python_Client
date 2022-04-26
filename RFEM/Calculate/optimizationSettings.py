from RFEM.initModel import Model
from RFEM.enums import *

class OptimizationSettings():
    def __init__(self,
        general_optimization_active = True,
        general_keep_best_number_model_mutations = 10,
        general_optimize_on = OptimizeOnType.E_OPTIMIZE_ON_TYPE_MIN_WHOLE_WEIGHT,
        general_optimizer = Optimizer.E_OPTIMIZER_TYPE_ALL_MUTATIONS,
        general_number_random_mutations = 0.2,
        model = Model):
        """
        The object is automaticaly created therefore we can assume,
        that it will not be created but only updated/changed.

        Args:
            general_optimization_active (bool): Set Optimization Active
            general_keep_best_number_model_mutations (int): Keep best number of model mutations
            general_optimize_on (enum): Optimize on
            general_optimizer (enum): Optimizer
            general_number_random_mutations (float): Number of random mutations
        """

        opt_settings = model.clientModel.service.get_optimization_settings()
        opt_settings.general_optimization_active = general_optimization_active
        opt_settings.general_keep_best_number_model_mutations = general_keep_best_number_model_mutations
        opt_settings.general_optimize_on = general_optimize_on.name
        opt_settings.general_optimizer = general_optimizer.name
        opt_settings.general_number_random_mutations = general_number_random_mutations

        # Set Optimization settings to client model
        model.clientModel.service.set_optimization_settings(opt_settings)

    @staticmethod
    def get(model = Model):
        return model.clientModel.service.get_optimization_settings()

    @staticmethod
    def set(opt_settings, model = Model):
        model.clientModel.service.set_optimization_settings(opt_settings)