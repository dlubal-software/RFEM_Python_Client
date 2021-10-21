import sys
sys.path.append(".")
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.section import Section
from RFEM.enums import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import Material
from RFEM.TypesforConcreteDesign.ConcreteDurability import ConcreteDurability
from RFEM.ConcreteDesign.ConcreteUltimateConfigurations import ConcreteUltimateConfiguration
from RFEM.ConcreteDesign.ConcreteServiceabilityConfigurations import ConcreteServiceabilityConfiguration
from RFEM.TypesforConcreteDesign.ConcreteEffectiveLength import ConcreteEffectiveLength


if __name__ == '__main__':

    clientModel.service.begin_modification()

    Material(1, 'C30/37')
    Section(1, 'R_M1 500/500', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member(1, MemberType.TYPE_BEAM, 1, 2, 0, 1, 1)

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
    ConcreteUltimateConfiguration(1, 'ULS', '1')

    # Concrete Serviceability Configuration
    ConcreteServiceabilityConfiguration(1, 'SLS', '1')

    # Concrete Effective Lengths 
    ConcreteEffectiveLength()

    print("Ready!")
    clientModel.service.finish_modification()