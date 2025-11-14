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
from RFEM.BasicObjects.crossSection import CrossSection
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TimberDesign.timberServiceLimitStateConfigurations import TimberDesignServiceLimitStateConfigurations

if Model.clientModel is None:
    Model()

def test_timberDesignServiceLimitStateConfigurations():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, addOn=AddOn.timber_design_active, status=True)

    Material(1, 'C24 | EN 338:2016-04')

    CrossSection(1, 'R_M1 0.18/0.36')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5, 0.0, 0.0)

    Member(1, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)

    TimberDesignServiceLimitStateConfigurations(1, name="myConfig")

    Model.clientModel.service.finish_modification()

    config = Model.clientModel.service.get_timber_design_sls_configuration(1)

    assert config.name == "myConfig"
    assert config.assigned_to_all_members == True

