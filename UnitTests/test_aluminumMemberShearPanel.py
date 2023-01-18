import sys
import os
import pytest
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AluminumMemberShearPanelDefinitionType, AluminumMemberShearPanelPositionOnSection, AluminumMemberShearPanelFasteningArrangement
from RFEM.initModel import Model, SetAddonStatus, AddOn, CheckIfMethodOrTypeExists
from RFEM.TypesForAluminumDesign.aluminumMemberShearPanel import AluminumMemberShearPanel
import pytest

if Model.clientModel is None:
    Model()

# Used method: ns0:aluminum_member_shear_panel is not implemented in Web Services yet.
@pytest.mark.skip()
def test_steelMemberShearPanel():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.steel_design_active)

    AluminumMemberShearPanel()

    AluminumMemberShearPanel(2, "shearPanel", AluminumMemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING, "1", "",
                         categories=[AluminumMemberShearPanelPositionOnSection.POSITION_DEFINE, "FI (+) 35/207 - 0.63 (b: 1) | DIN 18807 | Fischer Profil", AluminumMemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_SECOND_RIB],
                         parameters=[2,4, 0.00043, 0.00056, 0.05])

    AluminumMemberShearPanel(3, 'bracing', AluminumMemberShearPanelDefinitionType.DEFINITION_TYPE_BRACING, "", "",
                            [AluminumMemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE, "CHS 48.3x4 | EN 10210-2 | Condesa", "CHS 33.7x2.3 | EN 10210-2 | Ferona"],
                            [2,4,1,1,0.055, 0.224])

    Model.clientModel.service.finish_modification()

    shearPanel_1 = Model.clientModel.service.get_aluminum_member_shear_panel(1)
    shearPanel_2 = Model.clientModel.service.get_aluminum_member_shear_panel(2)
    shearPanel_3 = Model.clientModel.service.get_aluminum_member_shear_panel(3)

    assert shearPanel_1.no == 1
    assert shearPanel_2.definition_type == "DEFINITION_TYPE_TRAPEZOIDAL_SHEETING"
    assert shearPanel_3.panel_length == 2.0
