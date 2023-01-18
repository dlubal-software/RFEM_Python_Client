import sys
import os
import pytest
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn, PositionOnSection
from RFEM.initModel import Model, SetAddonStatus
from RFEM.TypesForTimberDesign.timberMemberShearPanel import TimberMemberShearPanel

if Model.clientModel is None:
    Model()

# Used method/type: ns0:timber_member_shear_panel is not implemented in Web Services yet.
@pytest.mark.skip()
def test_timberMemberShearPanel():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.timber_design_active, True)

    TimberMemberShearPanel()
    TimberMemberShearPanel(2, position_on_section=PositionOnSection.POSITION_DEFINE, position_on_section_value=0.01)

    Model.clientModel.service.finish_modification()

    TMSP1 = Model.clientModel.service.get_timber_member_shear_panel(1)
    TMSP2 = Model.clientModel.service.get_timber_member_shear_panel(2)

    assert TMSP1.no == 1
    assert TMSP1.position_on_section == PositionOnSection.POSITION_ON_UPPER_FLANGE.name
    assert TMSP1.stiffness == 1000

    assert TMSP2.position_on_section == PositionOnSection.POSITION_DEFINE.name
    assert TMSP2.position_on_section_value == 0.01
