import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import AddOn, DesignSupportOrientationYType, DesignSupportOrientationZType
from RFEM.initModel import Model, SetAddonStatus
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.crossSection import CrossSection
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.TypesForMembers.designSupport import DesignSupport

if Model.clientModel is None:
    Model()

def test_DesignSituation():

    Model.clientModel.service.delete_all()

    SetAddonStatus(Model.clientModel, AddOn.steel_design_active)
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    CrossSection(1, 'IPE 200')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10, 0.0, 0.0)
    Node(3, 0.0, 0.0, -10.0)
    Node(4, 10, 0.0, -10.0)

    Member(1, 1, 3)
    Member(2, 3, 4)
    Member(3, 2, 4)

    MemberSet(1, '1 2')
    MemberSet(2, '2 3')

    DesignSupport(1, '1', None, '1 3', [True, True, DesignSupportOrientationZType.DESIGN_SUPPORT_ORIENTATION_ZAXIS_POSITIVE, 0.3], \
        [True, False, DesignSupportOrientationYType.DESIGN_SUPPORT_ORIENTATION_YAXIS_NEGATIVE, 0.124, 1.014], 'General1')

    DesignSupport(2, None, '1', '4', False, [True, False, DesignSupportOrientationYType.DESIGN_SUPPORT_ORIENTATION_YAXIS_POSITIVE, 0.246, 0.437], 'General2')

    Model.clientModel.service.finish_modification()

    ds1 = Model.clientModel.service.get_design_support(1)
    ds2 = Model.clientModel.service.get_design_support(2)

    assert ds1.support_width_z == 0.3
    assert ds1.name == 'General1'
    assert ds2.activate_in_z == False
    assert ds2.assigned_to_nodes == '4'

def test_DesignSituation_Concrete():

    Model.clientModel.service.delete_all()

    SetAddonStatus(Model.clientModel, AddOn.concrete_design_active)
    Model.clientModel.service.begin_modification()

    Material(1, 'C8/10')

    CrossSection(1, 'R_M1 0.5/1')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10, 0.0, 0.0)
    Node(3, 0.0, 0.0, -10.0)
    Node(4, 10, 0.0, -10.0)

    Member(1, 1, 3)
    Member(2, 3, 4)
    Member(3, 2, 4)

    MemberSet(1, '1 2')
    MemberSet(2, '2 3')

    DesignSupport.Concrete(1, '3', None, '4', [True, True, True, True, 1.0, 0.1, 0.2], True,'Concre1')
    DesignSupport.Concrete(2, None, '2', '2', [True, True, True, False, False, 0.213], False, 'Concre2')

    Model.clientModel.service.finish_modification()

    ds1 = Model.clientModel.service.get_design_support(1)
    ds2 = Model.clientModel.service.get_design_support(2)

    assert ds1.support_width_z == 0.1
    assert ds1.name == 'Concre1'
    assert ds2.activate_in_y == False
    assert ds2.assigned_to_nodes == '2'

def test_DesignSituation_Steel():

    Model.clientModel.service.delete_all()

    SetAddonStatus(Model.clientModel, AddOn.steel_design_active)
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    CrossSection(1, 'IPE 200')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10, 0.0, 0.0)
    Node(3, 0.0, 0.0, -10.0)
    Node(4, 10, 0.0, -10.0)

    Member(1, 1, 3)
    Member(2, 3, 4)
    Member(3, 2, 4)

    MemberSet(1, '1 2')
    MemberSet(2, '2 3')

    DesignSupport.Steel(1, '3', None, '2', [True, True, DesignSupportOrientationZType.DESIGN_SUPPORT_ORIENTATION_ZAXIS_NEGATIVE, False, 0.25], True, 'Steel1')

    DesignSupport.Steel(2, None, '1', '4', [True, False, DesignSupportOrientationZType.DESIGN_SUPPORT_ORIENTATION_ZAXIS_POSITIVE, 0.014, 0.246, 0.437], False, 'Steel2')

    Model.clientModel.service.finish_modification()

    ds1 = Model.clientModel.service.get_design_support(1)
    ds2 = Model.clientModel.service.get_design_support(2)

    assert ds1.support_width_z == 0.25
    assert ds1.name == 'Steel1'
    assert ds2.activate_in_z == True
    assert ds2.assigned_to_nodes == '4'

def test_DesignSituation_Timber():

    Model.clientModel.service.delete_all()

    SetAddonStatus(Model.clientModel, AddOn.timber_design_active)
    Model.clientModel.service.begin_modification()

    Material(1, 'GL32c')

    CrossSection(1, 'Batten 50/100')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10, 0.0, 0.0)
    Node(3, 0.0, 0.0, -10.0)
    Node(4, 10, 0.0, -10.0)

    Member(1, 1, 3)
    Member(2, 3, 4)
    Member(3, 2, 4)

    MemberSet(1, '1 2')
    MemberSet(2, '2 3')

    DesignSupport.Timber(1, '3', None, '2', [True, True, True, False, DesignSupportOrientationZType.DESIGN_SUPPORT_ORIENTATION_ZAXIS_BOTH, True, 1.0, 0.32, 0.42], \
                                            [True, True, True, True, DesignSupportOrientationYType.DESIGN_SUPPORT_ORIENTATION_YAXIS_NEGATIVE, False, 1.45, 0.26], 'Timber1')

    DesignSupport.Timber(2, None, '1', '4', [True, False, True, True, DesignSupportOrientationZType.DESIGN_SUPPORT_ORIENTATION_ZAXIS_NEGATIVE], False, 'Timber2')

    Model.clientModel.service.finish_modification()

    ds1 = Model.clientModel.service.get_design_support(1)
    ds2 = Model.clientModel.service.get_design_support(2)

    assert ds1.support_width_z == 0.32
    assert ds1.name == 'Timber1'
    assert ds2.activate_in_y == False
    assert ds2.assigned_to_nodes == '4'
