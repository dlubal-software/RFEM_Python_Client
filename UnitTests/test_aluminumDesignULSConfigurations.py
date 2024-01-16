import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn, NodalSupportType
from RFEM.initModel import Model, SetAddonStatus
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.AluminumDesign.aluminumULSConfiguration import AluminumDesignULSConfigurations

if Model.clientModel is None:
    Model()

def test_AluminumDesignUltimateConfigurations():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, addOn=AddOn.aluminum_design_active, status=True)

    Material(1, 'EN AW-3004 H24 | EN 1999-1-1:2007')

    Section(1, 'IPE 200')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5, 0.0, 0.0)

    Member(1, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)

    AluminumDesignULSConfigurations(1, name="myConfig")

    Model.clientModel.service.finish_modification()

    config = Model.clientModel.service.get_aluminum_design_uls_configuration(1)

    assert config.name == "myConfig"
    assert config.assigned_to_all_members == True
