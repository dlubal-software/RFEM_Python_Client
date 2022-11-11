import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

import pytest
from RFEM.enums import *
from RFEM.initModel import Model, CheckIfMethodOrTypeExists, SetAddonStatus
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
from RFEM.TypesforConcreteDesign.ConcreteDurability import ConcreteDurability
#from RFEM.ConcreteDesign.ConcreteUltimateConfigurations import ConcreteUltimateConfiguration
#from RFEM.ConcreteDesign.ConcreteServiceabilityConfigurations import ConcreteServiceabilityConfiguration
from RFEM.TypesforConcreteDesign.ConcreteEffectiveLength import ConcreteEffectiveLength
from RFEM.TypesforConcreteDesign.ConcreteReinforcementDirections import ConcreteReinforcementDirection
from RFEM.TypesforConcreteDesign.ConcreteSurfaceReinforcements import ConcreteSurfaceReinforcements

if Model.clientModel is None:
    Model()

# TODO: US-8087
@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'ns0:concrete_durability', True), reason="ns0:concrete_durability not in RFEM GM yet")
def test_concrete_design():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.concrete_design_active)

    Material(1, 'C30/37')
    Material(2, 'B550S(A)')
    Section()

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

    # Concrete Ultimate Configuration
    # ConcreteUltimateConfiguration(1, 'ULS', '1')

    # Concrete Serviceability Configuration
    #ConcreteServiceabilityConfiguration(1, 'SLS', '1')

    # Concrete Effective Lengths
    ConcreteEffectiveLength()

    # Concrete Reinforcement Direction
    ConcreteReinforcementDirection(1, 'RD 1', "", ReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_FIRST_REINFORCEMENT_IN_X)
    ConcreteReinforcementDirection(2, 'RD 2', "", ReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_FIRST_REINFORCEMENT_IN_Y)
    ConcreteReinforcementDirection(3, 'RD 3', "", ReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_ROTATED, [30, 60])

    # Concrete Surface Reinforcements
    ConcreteSurfaceReinforcements()
    ConcreteSurfaceReinforcements(2, "RD 2", "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_ON_SURFACE, SurfaceReinforcementType.REINFORCEMENT_TYPE_STIRRUPS, [0.01, 0.15])
    ConcreteSurfaceReinforcements(3, "RD 3", "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_ON_SURFACE, SurfaceReinforcementType.REINFORCEMENT_TYPE_MESH, [SurfaceReinforcementMeshProductRange.MESHSTANDARD_GERMANY_1997_01_01, SurfaceReinforcementMeshShape.MESHSHAPE_Q_MESH, "Q131A"])
    ConcreteSurfaceReinforcements(4, "RD 4", "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_ON_SURFACE, reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_PARALLEL_TO_TWO_POINTS, reinforcement_direction_parameters=[1, 2, 3, 4, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV])
    ConcreteSurfaceReinforcements(5, "RD 5", "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_ON_SURFACE, reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters=[SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[SurfaceReinforcementLocationRectangleType.RECTANGLE_TYPE_CORNER_POINTS, 1, 2, 3, 4, 35], reinforcement_acting_region=["-inf", "+inf"])
    ConcreteSurfaceReinforcements(6, 'RD 6', "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_FREE_RECTANGULAR, SurfaceReinforcementType.REINFORCEMENT_TYPE_STIRRUPS, [0.01, 0.15], reinforcement_direction =SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters = [SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[SurfaceReinforcementLocationRectangleType.RECTANGLE_TYPE_CORNER_POINTS, 1, 2, 3, 4, 35], reinforcement_acting_region=["-inf", "+inf"])
    ConcreteSurfaceReinforcements(7, 'RD 7', "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_FREE_RECTANGULAR, SurfaceReinforcementType.REINFORCEMENT_TYPE_STIRRUPS, [0.01, 0.15], reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters = [SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[SurfaceReinforcementLocationRectangleType.RECTANGLE_TYPE_CENTER_AND_SIDES, 2, 3, 2, 2, 35], reinforcement_acting_region=["-inf", "+inf"])
    ConcreteSurfaceReinforcements(8, 'RD 8', "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_FREE_CIRCULAR, SurfaceReinforcementType.REINFORCEMENT_TYPE_STIRRUPS, [0.01, 0.15], reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters = [SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[1, 2, 3], reinforcement_acting_region=["-inf", "+inf"])
    ConcreteSurfaceReinforcements(9, 'RD 9', "", "2", SurfaceReinforcementLocationType.LOCATION_TYPE_FREE_POLYGON, SurfaceReinforcementType.REINFORCEMENT_TYPE_STIRRUPS, [0.01, 0.15], reinforcement_direction=SurfaceReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_IN_DESIGN_REINFORCEMENT_DIRECTION, reinforcement_direction_parameters = [SurfaceReinforcementDesignDirection.DESIGN_REINFORCEMENT_DIRECTION_A_S_1, "1", SurfaceReinforcementProjectionPlane.PROJECTION_PLANE_XY_OR_UV], reinforcement_location=[[1, 1, ""], [2, 2, ""], [3, 2, ""]], reinforcement_acting_region=["-inf", "+inf"])

    Model.clientModel.service.finish_modification()
