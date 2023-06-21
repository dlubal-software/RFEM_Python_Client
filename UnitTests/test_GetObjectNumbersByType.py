import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import ObjectTypes
from RFEM.initModel import Model
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.lineSet import LineSet
from RFEM.Tools.GetObjectNumbersByType import GetObjectNumbersByType

if Model.clientModel is None:
    Model()

def test_GetObjectNumbersByType():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 0, 5, 0)

    Line(1, '1 2')
    Line(2, '2 3')
    LineSet(1, '1 2')

    Model.clientModel.service.finish_modification()

    ObjectDictionary = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_LINE)
    assert ObjectDictionary == [1, 2]

    ObjectDictionary = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_NODE)
    assert ObjectDictionary == [1, 2, 3]

    ObjectDictionary = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_LINE_SET)
    assert ObjectDictionary == [1]
