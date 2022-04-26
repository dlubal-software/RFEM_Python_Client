import sys
import os
import pytest
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import SteelMemberShearPanelDefinitionType, SteelMemberShearPanelPositionOnSection, SteelMemberShearPanelFasteningArrangement
from RFEM.initModel import Model, SetAddonStatus, CheckIfMethodOrTypeExists, AddOn
from RFEM.TypesForSteelDesign.steelMemberShearPanel import SteelMemberShearPanel

if Model.clientModel is None:
    Model()

@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'ns0:steel_member_shear_panel', True), reason="Type ns0:steel_member_shear_panel not in RFEM GM yet")
def test_steelMemberShearPanel():

    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.steel_design_active, True)

    SteelMemberShearPanel()

    SteelMemberShearPanel(2, [True, "shearPanel"], SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING, "1", "",
                         categories=[SteelMemberShearPanelPositionOnSection.POSITION_DEFINE, "FI (+) 35/207 - 0.63 (b: 1) | DIN 18807 | Fischer Profil", SteelMemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_SECOND_RIB],
                         parameters=[2,4, 0.00043, 0.00056, 0.05])

    SteelMemberShearPanel(3, [False], SteelMemberShearPanelDefinitionType.DEFINITION_TYPE_BRACING, "", "",
                            [SteelMemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE, "CHS 48.3x4 | EN 10210-2 | Condesa", "CHS 33.7x2.3 | EN 10210-2 | Ferona"],
                            [2,4,1,1,0.055, 0.224])


    shearPanel_1 = Model.clientModel.service.get_steel_member_shear_panel(1)
    shearPanel_2 = Model.clientModel.service.get_steel_member_shear_panel(2)
    shearPanel_3 = Model.clientModel.service.get_steel_member_shear_panel(3)

    assert shearPanel_1.no == 1
    assert shearPanel_2.definition_type == "DEFINITION_TYPE_TRAPEZOIDAL_SHEETING"
    assert shearPanel_3.panel_length == 2.0


    Model.clientModel.service.finish_modification()
