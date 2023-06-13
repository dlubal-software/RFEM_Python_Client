import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, SetAddonStatus
from RFEM.enums import AddOn
from RFEM.TypesForMembers.memberShearPanel import MemberShearPanel

if Model.clientModel is None:
    Model()

def test_memberShearPanel():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.aluminum_design_active)
    SetAddonStatus(Model.clientModel, AddOn.timber_design_active)
    SetAddonStatus(Model.clientModel, AddOn.steel_design_active)

    MemberShearPanel.TrapeziodalSheetingAndBracing()

    MemberShearPanel.TrapezodialSheeting()

    MemberShearPanel.Bracing(3, panel_length=4)

    MemberShearPanel.DefineSProv(4, shear_panel_stiffness=2000)

    Model.clientModel.service.finish_modification()

    shearPanel1 = Model.clientModel.service.get_member_shear_panel(1)
    assert shearPanel1.no == 1

    shearPanel3 = Model.clientModel.service.get_member_shear_panel(3)
    assert shearPanel3.panel_length == 4

    shearPanel4 = Model.clientModel.service.get_member_shear_panel(4)
    assert shearPanel4.stiffness == 2000
