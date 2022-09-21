import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn, WeldComponentType
from RFEM.initModel import Model, SetAddonStatus
from RFEM.TypesForAluminumDesign. aluminumMemberTransverseWelds import AluminumMemberTransverseWeld, transverseWeldComponent


if Model.clientModel is None:
    Model()

def test_typesForLines():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.aluminum_design_active)

    AluminumMemberTransverseWeld(2, 'Weld_1', '', '', [transverseWeldComponent])

    Model.clientModel.service.finish_modification()

    aw = Model.clientModel.service.get_aluminum_member_transverse_weld(2)
    assert aw.name == 'Weld_1'
    assert aw.components[0][0].row.weld_type == WeldComponentType.WELD_COMPONENT_TYPE_BUTT.name
    assert aw.components[0][0].row.position == 0.3
