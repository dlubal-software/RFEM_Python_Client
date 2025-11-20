import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model, SetAddonStatus
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.crossSection import CrossSection
from RFEM.BasicObjects.material import Material
from RFEM.TypesforConcreteDesign.ConcreteDurability import ConcreteDurability
from RFEM.TypesforConcreteDesign.ConcreteEffectiveLength import ConcreteEffectiveLength
from RFEM.TypesforConcreteDesign.ConcreteReinforcementDirections import ConcreteReinforcementDirection
from RFEM.TypesforConcreteDesign.ConcreteSurfaceReinforcements import ConcreteSurfaceReinforcements

if Model.clientModel is None:
    Model()

def test_concrete_design():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.concrete_design_active)

    Material(1, 'C30/37')
    Material(2, 'B550S(A)')
    CrossSection()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member(1, 1, 2, 0, 1, 1)

    # Concrete Durabilities
    ConcreteDurability(1, "XC 1", '1', '', '', [True, False, False, False], [], [False, False, False], [], [DurabilityStructuralClassType.STANDARD, False, False, False, False], [False], [False], [DurabilityAllowanceDeviationType.STANDARD, False])

    ConcreteDurability(2, "XC 2", '1', '', '', [False, True, True, True], [DurabilityCorrosionCarbonation.CORROSION_INDUCED_BY_CARBONATION_TYPE_DRY_OR_PERMANENTLY_WET, DurabilityCorrosionChlorides.CORROSION_INDUCED_BY_CHLORIDES_TYPE_MODERATE_HUMIDITY, DurabilityCorrosionSeaWater.CORROSION_INDUCED_BY_CHLORIDES_FROM_SEA_WATER_TYPE_AIRBORNE_SALT], [False, False, False], [], [DurabilityStructuralClassType.STANDARD, False, False, False, False], [False], [False], [DurabilityAllowanceDeviationType.STANDARD, False])

    ConcreteDurability(3, "XC 3", '1', '', '', [True, False, False, False], [], [True, True, True], [DurabilityFreezeThawAttack.FREEZE_THAW_ATTACK_TYPE_MODERATE_SATURATION_NO_DEICING, DurabilityChemicalAttack.CHEMICAL_ATTACK_TYPE_SLIGHTLY_AGGRESSIVE, DurabilityCorrosionWear.CONCRETE_CORROSION_INDUCED_BY_WEAR_TYPE_MODERATE], [DurabilityStructuralClassType.STANDARD, False, False, False, False], [False], [False], [DurabilityAllowanceDeviationType.STANDARD, False])

    ConcreteDurability(4, "XC 4", '1', '', '', [True, False, False, False], [], [False, False, False], [], [DurabilityStructuralClassType.STANDARD, True, True, True, True], [False], [False], [DurabilityAllowanceDeviationType.STANDARD, False])

    ConcreteDurability(5, "XC 5", '1', '', '', [True, False, False, False], [], [False, False, False], [], [DurabilityStructuralClassType.DEFINED, DurabilityStructuralClass.S4], [False], [False], [DurabilityAllowanceDeviationType.STANDARD, False])

    ConcreteDurability(6, "XC 6", '1', '', '', [True, False, False, False], [], [False, False, False], [], [DurabilityStructuralClassType.STANDARD, False, False, False, False], [True, DurabilityStainlessSteelType.STANDARD], [False], [DurabilityAllowanceDeviationType.STANDARD, False])

    ConcreteDurability(7, "XC 7", '1', '', '', [True, False, False, False], [], [False, False, False], [], [DurabilityStructuralClassType.STANDARD, False, False, False, False], [True, DurabilityStainlessSteelType.DEFINED, 0.012], [False], [DurabilityAllowanceDeviationType.STANDARD, False])

    ConcreteDurability(8, "XC 8", '1', '', '', [True, False, False, False], [], [False, False, False], [], [DurabilityStructuralClassType.STANDARD, False, False, False, False], [True, DurabilityStainlessSteelType.DEFINED, 0.012], [True, DurabilityAdditionalProtectionType.STANDARD], [DurabilityAllowanceDeviationType.STANDARD, False])

    ConcreteDurability(9, "XC 9", '1', '', '', [True, False, False, False], [], [False, False, False], [], [DurabilityStructuralClassType.STANDARD, False, False, False, False], [True, DurabilityStainlessSteelType.DEFINED, 0.012], [True, DurabilityAdditionalProtectionType.DEFINED, 0.02], [DurabilityAllowanceDeviationType.STANDARD, False])

    ConcreteDurability(10, "XC 10", '1', '', '', [True, False, False, False], [], [False, False, False], [], [DurabilityStructuralClassType.STANDARD, False, False, False, False], [True, DurabilityStainlessSteelType.DEFINED, 0.012], [True, DurabilityAdditionalProtectionType.DEFINED, 0.02], [DurabilityAllowanceDeviationType.STANDARD, True, DurabilityConcreteCast.AGAINST_PREPARED_GROUND])

    ConcreteDurability(11, "XC 11", '1', '', '', [True, False, False, False], [], [False, False, False], [], [DurabilityStructuralClassType.STANDARD, False, False, False, False], [True, DurabilityStainlessSteelType.DEFINED, 0.012], [True, DurabilityAdditionalProtectionType.DEFINED, 0.02], [DurabilityAllowanceDeviationType.DEFINED, 0.008])

    # Concrete Effective Lengths
    ConcreteEffectiveLength()

    # Concrete Reinforcement Direction
    ConcreteReinforcementDirection(1, 'RD 1', "", ReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_FIRST_REINFORCEMENT_IN_X)
    ConcreteReinforcementDirection(2, 'RD 2', "", ReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_FIRST_REINFORCEMENT_IN_Y)
    ConcreteReinforcementDirection(3, 'RD 3', "", ReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_ROTATED, [30, 60])

    # Concrete Surface Reinforcements
    ConcreteSurfaceReinforcements()
    ConcreteSurfaceReinforcements(2, "RD 2", "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_ON_SURFACE, SurfaceReinforcementDefinitionType.DEFINITION_TYPE_SHEAR_REINFORCEMENT_STIRRUPS, [0.01, 0.15])
    ConcreteSurfaceReinforcements(3, "RD 3", "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_ON_SURFACE, SurfaceReinforcementDefinitionType.DEFINITION_TYPE_REINFORCING_MESH, [SurfaceReinforcementMeshProductRange.MESHSTANDARD_GERMANY_1997_01_01, SurfaceReinforcementMeshShape.MESHSHAPE_Q_MESH, "Q131A"])
    ConcreteSurfaceReinforcements(4, "RD 4", "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_ON_SURFACE, reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_PARALLEL_TO_TWO_POINTS, reinforcement_direction_parameters=[1, 2, 3, 4, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV])
    ConcreteSurfaceReinforcements(5, "RD 5", "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_ON_SURFACE, reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters=[SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[SurfaceReinforcementLocationRectangleType.RECTANGLE_TYPE_CORNER_POINTS, 1, 2, 3, 4, 35], reinforcement_acting_region=["-inf", "+inf"])
    ConcreteSurfaceReinforcements(6, 'RD 6', "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_FREE_RECTANGULAR, SurfaceReinforcementDefinitionType.DEFINITION_TYPE_SHEAR_REINFORCEMENT_STIRRUPS, [0.01, 0.15], reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters = [SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[SurfaceReinforcementLocationRectangleType.RECTANGLE_TYPE_CORNER_POINTS, 1, 2, 3, 4, 35], reinforcement_acting_region=["-inf", "+inf"])
    ConcreteSurfaceReinforcements(7, 'RD 7', "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_FREE_RECTANGULAR, SurfaceReinforcementDefinitionType.DEFINITION_TYPE_SHEAR_REINFORCEMENT_STIRRUPS, [0.01, 0.15], reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters = [SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[SurfaceReinforcementLocationRectangleType.RECTANGLE_TYPE_CENTER_AND_SIDES, 2, 3, 2, 2, 35], reinforcement_acting_region=["-inf", "+inf"])
    ConcreteSurfaceReinforcements(8, 'RD 8', "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_FREE_CIRCULAR, SurfaceReinforcementDefinitionType.DEFINITION_TYPE_SHEAR_REINFORCEMENT_STIRRUPS, [0.01, 0.15], reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters = [SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[1, 2, 3], reinforcement_acting_region=["-inf", "+inf"])
    ConcreteSurfaceReinforcements(9, 'RD 9', "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_FREE_POLYGON, SurfaceReinforcementDefinitionType.DEFINITION_TYPE_SHEAR_REINFORCEMENT_STIRRUPS, [0.01, 0.15], reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters = [SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[[1, 1, ""], [2, 2, ""], [3, 2, ""]], reinforcement_acting_region=["-inf", "+inf"])

    Model.clientModel.service.finish_modification()

    cd = Model.clientModel.service.get_concrete_durability(1)
    assert cd.no == 1
    assert cd.user_defined_name_enabled == True
    assert cd.name == "XC 1"
    assert cd.members == ""
    assert cd.member_sets == ""
    assert cd.surfaces == ""
    assert cd.no_risk_of_corrosion_or_attack_enabled == True
    assert cd.no_risk_of_corrosion_or_attack == "VERY_DRY"
    assert cd.freeze_thaw_attack_enabled == False
    assert cd.chemical_attack_enabled == False
    assert cd.concrete_corrosion_induced_by_wear_enabled == False
    assert cd.structural_class_type == "STANDARD"
    assert cd.increase_design_working_life_from_50_to_100_years_enabled == False
    assert cd.position_of_reinforcement_not_affected_by_construction_process_enabled == False
    assert cd.special_quality_control_of_production_enabled == False
    assert cd.air_entrainment_of_more_than_4_percent_enabled == False
    assert cd.stainless_steel_enabled == False
    assert cd.additional_protection_enabled == False
    assert cd.allowance_of_deviation_type == "STANDARD"
    assert cd.concrete_cast_enabled == False

    cdu = Model.clientModel.service.get_concrete_effective_lengths(1)
    assert cdu.no == 1
    assert cdu.user_defined_name_enabled == True
    assert cdu.name == "EL 1"
    assert cdu.comment == None
    assert cdu.members == ""
    assert cdu.member_sets == ""
    assert cdu.is_generated == False
    assert cdu.intermediate_nodes == False
    assert cdu.different_properties == True
    assert cdu.factors_definition_absolute == False
    assert cdu.import_from_stability_analysis_enabled == False
    assert cdu.structure_type_about_axis_y == "STRUCTURE_TYPE_UNBRACED"
    assert cdu.structure_type_about_axis_z == "STRUCTURE_TYPE_UNBRACED"
    assert cdu.flexural_buckling_about_y == True
    assert cdu.flexural_buckling_about_z == True

    crd = Model.clientModel.service.get_reinforcement_direction(1)
    assert crd.no == 1
    assert crd.user_defined_name_enabled == True
    assert crd.name == "RD 1"
    assert crd.surfaces == ""
    assert crd.reinforcement_direction_type == "REINFORCEMENT_DIRECTION_TYPE_FIRST_REINFORCEMENT_IN_X"

    csr1 = Model.clientModel.service.get_surface_reinforcement(1)
    assert csr1.no == 1
    assert csr1.location_type == "LOCATION_TYPE_ON_SURFACE"
    assert csr1.user_defined_name_enabled == True
    assert csr1.name == "RD 1"
    assert csr1.surfaces == ""
    assert csr1.material == 2
    assert csr1.definition_type == "DEFINITION_TYPE_REBARS_ONE_DIRECTION"
    assert csr1.rebar_diameter == 0.01
    assert csr1.rebar_spacing == 0.15
    assert csr1.alignment_top_enabled == True
    assert csr1.alignment_bottom_enabled == True
    assert csr1.additional_offset_to_concrete_cover_top == 0.0
    assert csr1.additional_offset_to_concrete_cover_bottom == 0.0
    assert csr1.reinforcement_direction_type == "REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION"
    assert csr1.design_reinforcement_direction == "DESIGN_REINFORCEMENT_DIRECTION_A_S_1"
    assert csr1.reinforcement_area_as1 == 0.0010471975511965978
    assert csr1.reinforcement_area_as1_top == 0.0005235987755982989
    assert csr1.reinforcement_area_as1_bottom == 0.0005235987755982989


    csr2 = Model.clientModel.service.get_surface_reinforcement(2)
    assert csr2.no == 2
    assert csr2.location_type == "LOCATION_TYPE_ON_SURFACE"
    assert csr2.user_defined_name_enabled == True
    assert csr2.name == "RD 2"
    assert csr2.surfaces == ""
    assert csr2.material == 2
    assert csr2.definition_type == "DEFINITION_TYPE_SHEAR_REINFORCEMENT_STIRRUPS"
    assert csr2.stirrup_diameter == 0.01
    assert csr2.stirrup_spacing == 0.15
    assert csr2.stirrup_reinforcement_area_asw == 0.0034906585039886596
