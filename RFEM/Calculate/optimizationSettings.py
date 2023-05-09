import enum
from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import OptimizerType, OptimizationTargetValueType

class OptimizationSettings():
    def __init__(self,
                 no: int = 1,
                 number_of_mutations_to_keep: int = 20,
                 target_value_type: enum = OptimizationTargetValueType.MIN_TOTAL_WEIGHT,
                 optimizer_type: enum = OptimizerType.ALL_MUTATIONS,
                 percent_of_mutations: float = 0.1,
                 optimization_values_table = None,
                 total_number_of_mutations: int = 40,
                 active: bool = True,
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        """
        Args:
            no: int = 1,
            number_of_mutations_to_keep: int = 20,
            target_value_type: enum = OptimizationTargetValueType.MIN_TOTAL_WEIGHT,
            optimizer_type: enum = OptimizerType.ALL_MUTATIONS,
            percent_of_mutations: float = 0.1,
            optimization_values_table = None,
            total_number_of_mutations: int = 40,
            active: bool = True,
            name: str = None,
            comment: str = '',
            params: dict = None,
            model = Model):
        """

        # Client model | Optimization Settings
        clientObject = model.clientModel.factory.create('ns0:optimization_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Optimization Settings No.
        clientObject.no = no

        clientObject.active = active
        clientObject.number_of_mutations_to_keep = number_of_mutations_to_keep
        clientObject.target_value_type = target_value_type.name
        clientObject.optimizer_type = optimizer_type.name

        clientObject.percent_of_mutations = percent_of_mutations
        clientObject.optimization_values_table = optimization_values_table
        clientObject.total_number_of_mutations = total_number_of_mutations

        # Optimization Settings Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Set Optimization settings to client model
        model.clientModel.service.set_optimization_settings(clientObject)

    @staticmethod
    def GetOptimizationSettings(no = 1, model = Model):
        return model.clientModel.service.get_optimization_settings(no)
