import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn
from RFEM.initModel import Model, SetAddonStatus
from RFEM.TypesForTimberDesign.timberMemberRotationalRestraint import TimberMemberRotationalRestraint

if Model.clientModel is None:
    Model()

def test_timberMemberRotationalRestraints():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.timber_design_active, True)

    TimberMemberRotationalRestraint()
    TimberMemberRotationalRestraint(2, 'TMRR2', spring_stiffness=30000)

    Model.clientModel.service.finish_modification()

    TMRR1 = Model.clientModel.service.get_timber_member_rotational_restraint(1)
    TMRR2 = Model.clientModel.service.get_timber_member_rotational_restraint(2)

    assert TMRR1.no == 1
    assert TMRR1.total_rotational_spring_stiffness == 20000

    assert TMRR2.type == 'TYPE_MANUALLY'
    assert TMRR2.name == 'TMRR2'
    assert TMRR2.total_rotational_spring_stiffness == 30000
