import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.TypesForNodes.nodalSupport import NodalSupport, NodalSupportType
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model
from RFEM.Tools.PlausibilityCheck import PlausibilityCheck

if Model.clientModel is None:
    Model()

def test_plausibility_check():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Sections
    Section(1, 'HEA 240', 1)

    # Create Nodes
    Node(1, 0, 0, 0)
    Node(2, 6, 0, 0)

    # Create Members
    Member(1, 1, 2, 0, 1, 1)

    # Create Nodal Supports
    NodalSupport(1, '1', NodalSupportType.FIXED)

    Model.clientModel.service.finish_modification()

    check = PlausibilityCheck()
    assert check.message == 'Success'
    assert check.errormessage == ''
    assert check.IsModelOK()
    assert check.GetErrorMessage() == ''
