import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn, TimberServiceClassServiceClass
from RFEM.initModel import Model, SetAddonStatus
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForTimberDesign.timberServiceClass import TimberServiceClass

if Model.clientModel is None:
    Model()

def test_timberServiceClass():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.timber_design_active, True)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 10, 0, 0)
    Material(1, 'KLH (20 mm) | KLH')
    Section(1, 'R_M1 0.2/0.5', 1)
    Member(1, 1, 2, 0, 1, 1)
    Member(2, 2, 3, 0, 1, 1)

    TimberServiceClass(members='1 2', service_class=TimberServiceClassServiceClass.TIMBER_SERVICE_CLASS_TYPE_2)

    Model.clientModel.service.finish_modification()

    tsc = Model.clientModel.service.get_timber_service_class(1)

    assert tsc.members == '1 2'
    assert tsc.service_class == TimberServiceClassServiceClass.TIMBER_SERVICE_CLASS_TYPE_2.name
