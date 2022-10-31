import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model, SetAddonStatus
from RFEM.TypesForSteelDesign.steelEffectiveLengths import SteelEffectiveLengths

if Model.clientModel is None:
    Model()

def test_steelEffectiveLengths():

    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.steel_design_active, True)

    SteelEffectiveLengths(1, "", "", True, False, False, False, True, False, 'SEL1',
        [
            [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z, True, 0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, 0, 0, 0, 0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, \
            SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, ""],

            [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z, True, 0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, 0, 0, 0, 0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, \
            SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, ""],
        ],

        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
                        )

    SteelEffectiveLengths(2, "", "", False, False, False, True, True, False, 'SEL2',
        [
            [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_ALL, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, 0, 0, 0, 0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, \
            SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_YES, ""],

            [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_RESTRAINT_ABOUT_X, False, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, 0, 0, 0, 0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_NO, \
            SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, ""],

            [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_INDIVIDUALLY, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, 0,0,0,0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, \
            SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_YES, ""]

        ],

        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 543], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ],

        intermediate_nodes=True, different_properties=True, determination_of_mcr=SteelEffectiveLengthsDeterminationMcrEurope.DETERMINATION_EUROPE_USER_DEFINED,
                        )

    SteelEffectiveLengths(3, "", "", True, False, False, False, True, True, 'SEL3',
        [
            [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, 0, 0, 0, 0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, \
            SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, ""],

            [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, 0, 0, 0, 0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, \
            SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, ""]

        ],

        [
            [3, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
                        )

    ef_1 = Model.clientModel.service.get_steel_effective_lengths(1)
    assert ef_1.flexural_buckling_about_y == True

    ef_2 = Model.clientModel.service.get_steel_effective_lengths(2)
    assert ef_2.principal_section_axes == True
    assert ef_2.nodal_supports[0][0].row['support_type'] == 'SUPPORT_TYPE_FIXED_ALL'

    ef_3 = Model.clientModel.service.get_steel_effective_lengths(3)
    assert ef_3.factors[0][0].row['flexural_buckling_u'] == 3
    assert ef_3.factors[0][0].row['flexural_buckling_y'] == 4

    Model.clientModel.service.finish_modification()
