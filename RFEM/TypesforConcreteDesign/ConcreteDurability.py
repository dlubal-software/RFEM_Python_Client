from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import DurabilityStructuralClassType, DurabilityAllowanceDeviationType

class ConcreteDurability():
    def __init__(self,
                no: int = 1,
                name: str = "XC 1",
                members_no: str = "1",
                member_sets_no: str = "1",
                surfaces_no: str = "1",
                exposure_classes_reinforcement: list = [True, False, False, False],
                exposure_classes_reinforcement_types: list = None,
                exposure_classes_concrete: list = [False, False, False],
                exposure_classes_concrete_types: list = None,
                structural_class: list = [DurabilityStructuralClassType.STANDARD, False, False, False, False],
                stainless_steel_reduction: list = [False],
                additional_protection_reduction: list = [False],
                allowance_deviation: list = [DurabilityAllowanceDeviationType.STANDARD, False],
                comment: str = '',
                params: dict = None,
                model = Model):
        """
        Args:
            no (int): Concrete Durability Tag
            name (str): User Defined Name
            members_no (str): Assigned Members
            member_sets_no (str): Assigned Member Sets
            surfaces_no (str): Assigned Surfaces
            exposure_classes_reinforcement (list): Exposure Classes Reinforcement Parameters
            exposure_classes_reinforcement_types (list of enum): Exposure Classes Reinforcement Type List of Enumeration
            exposure_classes_concrete (list): Exposure Classes Concrete Parameters
            exposure_classes_concrete_types (list of enum): Exposure Classes Concrete Type List of Enumeration
            structural_class (list): Structural Class Parameters
            stainless_steel_reduction (list): Stainless Steel Reduction Parameters
            additional_protection_reduction (list): Additional Protection Reduction
            allowance_deviation (list): Allowance Deviation Parameters
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Concrete Durabilities
        clientObject = model.clientModel.factory.create('ns0:concrete_durability')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Concrete Durability No.
        clientObject.no = no

        # User Defined Name
        clientObject.user_defined_name_enabled = True
        clientObject.name = name

        # Assigned Members
        clientObject.members = ConvertToDlString(members_no)

        # Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets_no)

        # Assigned Surfaces
        clientObject.surfaces = ConvertToDlString(surfaces_no)

        # Exposure Classes for Reinforcement
        clientObject.no_risk_of_corrosion_or_attack_enabled = exposure_classes_reinforcement[0]
        clientObject.corrosion_induced_by_carbonation_enabled = exposure_classes_reinforcement[1]
        clientObject.corrosion_induced_by_chlorides_enabled = exposure_classes_reinforcement[2]
        clientObject.corrosion_induced_by_chlorides_from_sea_water_enabled = exposure_classes_reinforcement[3]

        if all(exposure_classes_reinforcement):
            raise Exception("WARNING: At least one reinforcement exposure class must be selected.")

        for i in exposure_classes_reinforcement:
            if not isinstance(i, bool):
                raise Exception('WARNING: The type of parameters should be bool. Kindly check list inputs for completeness and correctness.')

        if exposure_classes_reinforcement[0]:
            clientObject.no_risk_of_corrosion_or_attack = "VERY_DRY"
            for i in exposure_classes_reinforcement[1:]:
                if i:
                    raise Exception('WARNING: If No Risk of Corrosion is True, other parameters cannot be selected. Kindly check list inputs for completeness and correctness.')

        if exposure_classes_reinforcement[1] :
            clientObject.corrosion_induced_by_carbonation = exposure_classes_reinforcement_types[0].name
        if exposure_classes_reinforcement[2]:
            clientObject.corrosion_induced_by_chlorides = exposure_classes_reinforcement_types[1].name
        if exposure_classes_reinforcement[3]:
            clientObject.corrosion_induced_by_chlorides_from_sea_water = exposure_classes_reinforcement_types[2].name

        # Exposure Classes for Concrete
        for i in exposure_classes_concrete:
            if not isinstance(i, bool):
                raise Exception('WARNING: The type of parameters should be bool. Kindly check list inputs for completeness and correctness.')

        if exposure_classes_concrete[0]:
            clientObject.freeze_thaw_attack_enabled = True
            clientObject.freeze_thaw_attack = exposure_classes_concrete_types[0].name
        if exposure_classes_concrete[1]:
            clientObject.chemical_attack_enabled = True
            clientObject.chemical_attack = exposure_classes_concrete_types[1].name
        if exposure_classes_concrete[2]:
            clientObject.concrete_corrosion_induced_by_wear_enabled = True
            clientObject.concrete_corrosion_induced_by_wear = exposure_classes_concrete_types[2].name

        # Structural Class
        clientObject.structural_class_type = structural_class[0].name

        if structural_class[0].name == "STANDARD":
            for i in structural_class[1:]:
                if not isinstance(i, bool):
                    raise Exception('WARNING: The type of last three parameters should be bool. Kindly check list inputs for completeness and correctness.')

            clientObject.increase_design_working_life_from_50_to_100_years_enabled = structural_class[1]
            clientObject.position_of_reinforcement_not_affected_by_construction_process_enabled = structural_class[2]
            clientObject.special_quality_control_of_production_enabled = structural_class[3]
            clientObject.air_entrainment_of_more_than_4_percent_enabled = structural_class[4]
        elif structural_class[0].name == "DEFINED":
            clientObject.userdefined_structural_class = structural_class[1].name

        # Stainless Steel Concrete Cover Reduction
        clientObject.stainless_steel_enabled = stainless_steel_reduction[0]

        if not isinstance(stainless_steel_reduction[0], bool):
            raise Exception('WARNING: The type of the first parameter should be bool. Kindly check list inputs for completeness and correctness.')

        if stainless_steel_reduction[0]:
            clientObject.stainless_steel_type = stainless_steel_reduction[1].name

            if stainless_steel_reduction[1].name == "DEFINED":
                clientObject.stainless_steel_factor = stainless_steel_reduction[2]

        # Additional Protection Concrete Cover Reduction
        clientObject.additional_protection_enabled = additional_protection_reduction[0]

        if not isinstance(additional_protection_reduction[0], bool):
            raise Exception('WARNING: The type of the first parameter should be bool. Kindly check list inputs for completeness and correctness.')

        if additional_protection_reduction[0]:
            clientObject.additional_protection_type = additional_protection_reduction[1].name

            if additional_protection_reduction[1].name == "DEFINED":
                clientObject.additional_protection_factor = additional_protection_reduction[2]

        # Allowance for Deviation
        clientObject.allowance_of_deviation_type = allowance_deviation[0].name

        if allowance_deviation[0].name == "STANDARD":
            clientObject.concrete_cast_enabled = allowance_deviation[1]

            if not isinstance(allowance_deviation[1], bool):
                raise Exception('WARNING: The type of the second parameter should be bool. Kindly check list inputs for completeness and correctness.')

            if allowance_deviation[1]:
                clientObject.concrete_cast = allowance_deviation[2].name

        elif allowance_deviation[0].name == "DEFINED":
            clientObject.userdefined_allowance_of_deviation_factor = allowance_deviation[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Global Parameter to client model
        model.clientModel.service.set_concrete_durability(clientObject)
