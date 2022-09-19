import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model, SetAddonStatus
from RFEM.TypesForAluminumDesign.aluminumEffectiveLengths import AluminumEffectiveLengths

if Model.clientModel is None:
    Model()

def test_aluminumEffectiveLengths():

    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.aluminum_design_active)

    AluminumEffectiveLengths(1, "", "", True, False, False, False, True, False, 'SEL1')

    AluminumEffectiveLengths(2, "", "", False, False, False, True, True, False, 'SEL2',
                             True, True, determination_of_mcr=SteelEffectiveLengthsDeterminationMcrEurope.DETERMINATION_EUROPE_USER_DEFINED)

    AluminumEffectiveLengths(3, "", "", True, False, False, False, True, True, 'SEL3')

    Model.clientModel.service.finish_modification()

    ef_1 = Model.clientModel.service.get_aluminum_effective_lengths(1)
    assert ef_1.flexural_buckling_about_y == True

    ef_2 = Model.clientModel.service.get_aluminum_effective_lengths(2)
    assert ef_2.principal_section_axes == True
    assert ef_2.nodal_supports[0][0].row['support_type'] == 'SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION'
    assert ef_2.determination_mcr_europe == SteelEffectiveLengthsDeterminationMcrEurope.DETERMINATION_EUROPE_USER_DEFINED.name

    ef_3 = Model.clientModel.service.get_aluminum_effective_lengths(3)
    assert ef_3.factors[0][0].row['flexural_buckling_u'] == 1
    assert ef_3.factors[0][0].row['flexural_buckling_y'] == 1
