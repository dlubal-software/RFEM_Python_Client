import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member

if Model.clientModel is None:
    Model()

def test_node():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node.Standard(3, [5, 5, 0],NodeCoordinateSystemType.COORDINATE_SYSTEM_CARTESIAN)
    Node.BetweenTwoNodes(4,2,3,NodeReferenceType.REFERENCE_TYPE_L, 1, [True, 0.60])
    Node.BetweenTwoPoints(5,0,0,0,6,0,0,NodeReferenceType.REFERENCE_TYPE_L, [True, 0.7], 1, 1)

    Line(1,'1 2')
    Node.OnLine(6, 1, NodeReferenceType.REFERENCE_TYPE_L, 1, [True, 0.50])

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1, 1, 2, 0, 1, 1)
    Node.OnMember(7,1,NodeReferenceType.REFERENCE_TYPE_L)

    Model.clientModel.service.finish_modification()

    node = Model.clientModel.service.get_node(1)
    assert node.type == 'TYPE_STANDARD'
    node = Model.clientModel.service.get_node(3)
    assert node.type == 'TYPE_STANDARD'
    node = Model.clientModel.service.get_node(4)
    assert node.type == 'TYPE_BETWEEN_TWO_NODES'
    node = Model.clientModel.service.get_node(5)
    assert node.type == 'TYPE_BETWEEN_TWO_POINTS'
    node = Model.clientModel.service.get_node(7)
    assert node.type == 'TYPE_ON_MEMBER'

def test_node_delete():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 0, 0, -5)
    Node(3, 0, 0, -10)

    Node.DeleteNode('1 3')

    Model.clientModel.service.finish_modification()

    modelInfo = Model.clientModel.service.get_model_info()

    assert modelInfo.property_node_count == 1