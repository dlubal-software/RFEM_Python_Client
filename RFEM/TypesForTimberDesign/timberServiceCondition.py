from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import TimberServiceConditionsMoistureType, TimberServiceConditionsTemperatureType
from RFEM.enums import TimberServiceConditionsTreatmentType
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations

class TimberServiceConditions():
    def __init__(self,
                no: int = 1,
                name: str = '',
                members: str = '',
                member_sets: str = '',
                surfaces: str = '',
                surface_sets: str = '',
                standard: int = 6336,
                moisture_service_condition = TimberServiceConditionsMoistureType.TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_DRY,
                temperature = TimberServiceConditionsTemperatureType.TEMPERATURE_TYPE_TEMPERATURE_ZONE_1,
                treatment_csa = TimberServiceConditionsTreatmentType.TREATMENT_TYPE_NONE,
                treatment_nds: bool = True,
                treatment_gb: bool = False,
                service_conditions = [False, False, False, False, False],
                comment: str = '',
                params: dict = None,
                model = Model):
        """
        Args:
            no (int): Timber Service Conditions Tag
            name (str): User Defined Timber Service Condition Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            surfaces (str): Assigned Surfaces
            surface_sets (str): Assigned Surface Sets
            standard (int): Code Number
            moisture_service_condition (enum): Timber Moisture Service Condition Enumeration
            temperature (enum): Timber Service Conditions Temperature Enumeration
            treatment_csa (enum): Timber Service Conditions Treatment Enumeration
            treatment_nds (bool): Member Pressure Treated
            treatment_gb (bool): Timber Is Point Impregnated
            service_conditions (list): Service Conditions
                service_conditions = [outdoor_environment, long_term_high_temperature_of_surface, permanent_load_design_situation,
                                      timber_structures, short_term_construction_or_maintenance]
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

         # Client Model | Types For Timber Design Service Condition
        clientObject = Model.clientModel.factory.create('ns0:timber_service_conditions')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Service Class
        clientObject.no = no

        # Assigned Members
        clientObject.member = ConvertToDlString(members)

        # Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Assigned Surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Assigned Surface Sets
        clientObject.surface_sets = ConvertToDlString(surface_sets)

        if standard in [6336, 6579, 6514, 6516]:
            LoadCasesAndCombinations(params = {"current_standard_for_combination_wizard": standard,
                                                "activate_combination_wizard_and_classification": True,
                                                "activate_combination_wizard": True,
                                                "result_combinations_active": True,
                                                "result_combinations_parentheses_active": False,
                                                "result_combinations_consider_sub_results": False,
                                                "combination_name_according_to_action_category": False})

            # Service Condition if Standard CSA - Moisture Service Conditions and Treatment
            if standard == 6336:
                clientObject.moisture_service_condition = moisture_service_condition
                clientObject.treatment = treatment_csa

            # Service Condition if Standard NDS(USA) - Service Moisture Conditions, Treatment and Temperature
            elif standard == 6579:
                clientObject.moisture_service_condition = moisture_service_condition
                clientObject.temperature = temperature
                clientObject.member_pressure_treated = treatment_nds

            # Treatment if Standard GB
            else:
                clientObject.moisture_service_condition = moisture_service_condition
                clientObject.outdoor_environment = service_conditions[0]
                clientObject.long_term_high_temperature_of_surface = service_conditions[1]
                clientObject.permanent_load_design_situation = service_conditions[2]
                clientObject.timber_structures = service_conditions[3]
                clientObject.short_term_construction_or_maintenance = service_conditions[4]
                clientObject.timber_is_point_impregnated = treatment_gb

        # User Defined Name
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

        # Add Service Class to client model
        model.clientModel.service.set_timber_service_conditions(clientObject)
