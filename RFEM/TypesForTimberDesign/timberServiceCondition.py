from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import TimberServiceConditionsMoistureServiceCondition, TimberServiceConditionsTemperature
from RFEM.enums import TimberServiceConditionsTreatment
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations

class TimberServiceCondition():
    def __init__(self,
                no: int = 1,
                name: str = '',
                members: str = '',
                member_sets: str = '',
                surfaces: str = '',
                surface_sets: str = '',
                standard = LoadCasesAndCombinations(params = {"current_standard_for_combination_wizard": 6336}),
                moisture_service_condition = TimberServiceConditionsMoistureServiceCondition.TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_DRY,
                temperature = TimberServiceConditionsTemperature.TEMPERATURE_TYPE_TEMPERATURE_ZONE_1,
                treatment = [False, True, TimberServiceConditionsTreatment.TREATMENT_TYPE_NONE],
                service_conditions = [False, False, False, False, False],
                comment: str = '',
                params: dict = None):
        """
        Args:
            no (int): Timber Member Shear Panel Tag
            name (str): User Defined Member Shear Panel Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            surfaces (str): Assigned Surfaces
            surface_sets (str): Assigned Surface Sets
            service_class (enum): Timber Service Condition
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        """

         # Client Model | Types For Timber Design Service Condition
        clientObject = Model.clientModel.factory.create('ns0:timber_service_condition')

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

        # Service Condition if Standard CSA - Moisture Service Conditions and Treatment
        if standard:
            clientObject.moisture_service_condition = moisture_service_condition
            clientObject.treatment = treatment[2]

        # Service Condition if Standard NDS(USA) - Service Moisture Conditions, Treatment and Temperature
        if standard == LoadCasesAndCombinations(params = {"current_standard_for_combination_wizard": 6579}):
            clientObject.moisture_service_condition = moisture_service_condition
            clientObject.temperature = temperature
            clientObject.member_pressure_treated = treatment[1]

        # Treatment if Standard GB
        if standard == LoadCasesAndCombinations(params = {"current_standard_for_combination_wizard": 6514}) \
        or standard == LoadCasesAndCombinations(params = {"current_standard_for_combination_wizard": 6516}):
            clientObject.moisture_service_condition = moisture_service_condition
            clientObject.outdoor_environment = service_conditions[0]
            clientObject.long_term_high_temperature_of_surface = service_conditions[1]
            clientObject.permanent_load_design_situation = service_conditions[2]
            clientObject.timber_structures = service_conditions[3]
            clientObject.short_term_construction_or_maintenance = service_conditions[4]
            clientObject.timber_is_point_impregnated = treatment[0]

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
        Model.clientModel.service.set_timber_service_condition(clientObject)
