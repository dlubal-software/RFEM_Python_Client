import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model, SetAddonStatus
from RFEM.TypesForTimberDesign.timberEffectiveLengths import TimberEffectiveLengths

if Model.clientModel is None:
    Model()

def test_timberEffectiveLengths():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.timber_design_active, True)

    TimberEffectiveLengths()

    Model.clientModel.service.finish_modification()

    tel = Model.clientModel.service.get_timber_effective_lengths(1)
    assert tel.flexural_buckling_about_y == True
    assert tel.flexural_buckling_about_z == True
    assert tel.intermediate_nodes == False
    assert tel.different_properties == True
    assert tel.factors_definition_absolute == False
    assert tel.fire_design_different_buckling_factors == False
    assert tel.import_from_stability_analysis_enabled == False
    assert tel.determination_type == TimberEffectiveLengthsDeterminationType.DETERMINATION_EIGENVALUE_SOLVER.name
    assert tel.nodal_supports[0][0].row.support_type == TimberEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION.name
    assert tel.nodal_supports[0][0].row.support_in_z == True
    assert tel.nodal_supports[0][0].row.eccentricity_type == TimberEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE.name
