import sys
import os
import pytest
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, SetAddonStatus, CheckIfMethodOrTypeExists
from RFEM.enums import AddOn, AluminumMemberRotationalRestraintType, AluminumMemberRotationalRestraintContinuousBeamEffect
from RFEM.enums import AluminumMemberRotationalRestraintPositionofSheeting, AddOn, AluminumMemberRotationalRestraintRotationalStiffness
from RFEM.TypesForAluminumDesign.aluminumMemberRotationalRestraints import AluminumMemberRotationalRestraint
import pytest

if Model.clientModel is None:
    Model()

# Used method: ns0:aluminum_member_rotational_restraint is not implemented in Web Services yet.
@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'ns0:aluminum_member_rotational_restraint', True), reason="Type ns0:aluminum_member_rotational_restraint not in RFEM GM yet")
def test_aluminumMemberRotationalRestraints():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.aluminum_design_active)

    AluminumMemberRotationalRestraint(1, '', AluminumMemberRotationalRestraintType.TYPE_CONTINUOUS, "", "", ["EN AW-3004 H14", "Arval (-) 35/207 - 0.63 (b: 1) | DIN 18807 | Arval",
            AluminumMemberRotationalRestraintPositionofSheeting.SHEETING_POSITION_NEGATIVE, AluminumMemberRotationalRestraintContinuousBeamEffect.CONTINUOUS_BEAM_EFFECT_END_PANEL, True],
            [205000000000.0, 0.00063, 7.5e-08, 0.207, 0.106, 5200.0, 3.0])

    AluminumMemberRotationalRestraint(2, 'test_restraint', AluminumMemberRotationalRestraintType.TYPE_DISCRETE, "", "",
            ["EN AW-3004 H14", "IPE A 80 | EN 10365:2017 | ArcelorMittal (2018)", AluminumMemberRotationalRestraintRotationalStiffness.ROTATIONAL_STIFFNESS_INFINITELY, AluminumMemberRotationalRestraintContinuousBeamEffect.CONTINUOUS_BEAM_EFFECT_END_PANEL, True],
            [205000000000.0, 6.44e-07, 1, 3])

    Model.clientModel.service.finish_modification()

    aluminumMemberRestraint1 = Model.clientModel.service.get_aluminum_member_rotational_restraint(1)
    aluminumMemberRestraint2 = Model.clientModel.service.get_aluminum_member_rotational_restraint(2)

    assert aluminumMemberRestraint1.no == 1
    assert aluminumMemberRestraint1.material_name == "EN AW-3004 H14"

    assert aluminumMemberRestraint2.type == "TYPE_DISCRETE"
    assert aluminumMemberRestraint2.continuous_beam_effect == "CONTINUOUS_BEAM_EFFECT_END_PANEL"
