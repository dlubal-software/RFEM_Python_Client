import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, SetAddonStatus
from RFEM.enums import AddOn
from RFEM.TypesForMembers.memberRotationalRestraint import MemberRotationalRestraint

if Model.clientModel is None:
    Model()

def test_memberRotationalRestraint():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.aluminum_design_active)
    SetAddonStatus(Model.clientModel, AddOn.timber_design_active)
    SetAddonStatus(Model.clientModel, AddOn.steel_design_active)

    MemberRotationalRestraint.Continuous()

    MemberRotationalRestraint.Discrete(2, purlin_spacing=4)

    MemberRotationalRestraint.Manually(3, rotational_spring_stiffness=4000)

    Model.clientModel.service.finish_modification()

    rotationalRestraint1 = Model.clientModel.service.get_member_rotational_restraint(1)
    assert rotationalRestraint1.no == 1

    rotationalRestraint2 = Model.clientModel.service.get_member_rotational_restraint(2)
    assert rotationalRestraint2.purlin_spacing == 4

    rotationalRestraint3 = Model.clientModel.service.get_member_rotational_restraint(3)
    assert rotationalRestraint3.total_rotational_spring_stiffness == 4000
