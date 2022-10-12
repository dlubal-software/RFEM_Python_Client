import pytest
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model, CheckIfMethodOrTypeExists
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.lineSet import LineSet
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.BasicObjects.opening import Opening
from RFEM.BasicObjects.solid import Solid
from RFEM.BasicObjects.solidSet import SolidSet
from RFEM.BasicObjects.surfaceSet import SurfaceSet
from RFEM.BasicObjects.thickness import Thickness

from RFEM.Tools.GetObjectNumbersByType import GetObjectNumbersByType

if Model.clientModel is None:
    Model()

@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel, 'set_model_settings_and_options', True), reason="set_model_settings_and_options not in RFEM GM yet")


def test_GetObjectNumbersByType():


    """
    Create Nodes, Lines and Line_Set

    Run function to test the output

    """

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 0, 5, 0)


    Line(1, '1 2')
    Line(2, '2 3')
    LineSet(1, '1 2')



    Model.clientModel.service.finish_modification()


    ObjectDictionary = GetObjectNumbersByType.GetObjectNumbers(ObjectTypes.E_OBJECT_TYPE_LINE)

    assert ObjectDictionary == [1, 2]

    ObjectDictionary = GetObjectNumbersByType.GetObjectNumbers(ObjectTypes.E_OBJECT_TYPE_NODE)

    assert ObjectDictionary == [1, 2, 3]

    ObjectDictionary = GetObjectNumbersByType.GetObjectNumbers(ObjectTypes.E_OBJECT_TYPE_LINE_SET)

    assert ObjectDictionary == [1]