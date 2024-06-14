import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

# Import the relevant Libraries
from RFEM.enums import ObjectTypes
from RFEM.initModel import CheckIfMethodOrTypeExists, Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.Tools.centreOfGravityAndObjectInfo import ObjectsInfo
from math import sqrt
import pytest

if Model.clientModel is None:
    Model()

# pytestmark sets same parameters (in this case skipif) to all functions in the module or class
# TODO: US-8142
# pytestmark = pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'ns0:array_of_get_center_of_gravity_and_objects_info_elements_type', True),
#              reason="ns0:array_of_get_center_of_gravity_and_objects_info_elements_type not in RFEM GM yet")

def test_center_of_gravity():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    x1, y1, z1, = 0, 0, 0
    x2, y2, z2 = 4, 10, -6
    Node(1, x1, y1, z1)
    Node(2, x2, y2, z2)
    Material(1, 'S235')
    Section()
    Member(1, start_node_no= 1, end_node_no= 2)

    Model.clientModel.service.finish_modification()

    CoG_X = (x2 - x1) / 2
    CoG_Y = (y2 - y1) / 2
    CoG_Z = (z2 - z1) / 2

    cog = ObjectsInfo.CenterofGravity([[ObjectTypes.E_OBJECT_TYPE_MEMBER, 1]])

    assert cog['Center of gravity coordinate X'] == CoG_X
    assert cog['Center of gravity coordinate Y'] == CoG_Y
    assert cog['Center of gravity coordinate Z'] == CoG_Z

def test_member_information():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    x1, y1, z1, = 0, 0, 0
    x2, y2, z2 = 4, 10, -6
    Node(1, x1, y1, z1)
    Node(2, x2, y2, z2)
    Material(1, 'S235')
    Section()
    Member(1, start_node_no= 1, end_node_no= 2)

    Model.clientModel.service.finish_modification()

    L = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    A = 53.80 / (100 * 100)
    V = L * A
    M = (V * 7850) / 1000

    info = ObjectsInfo.MembersInfo([[ObjectTypes.E_OBJECT_TYPE_MEMBER, 1]])

    assert info['Length of members'] == round(L,3)
    assert info['Volume'] == round(V,3)
    assert info['Mass'] == round(M,3)

def test_surface_information():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    x1, y1, z1 = 0 , 0, 0
    x2, y2, z2 = 10, 0, 0
    x3, y3, z3 = 10, 15, 0
    x4, y4, z4 = 0, 15, 0

    Node(1, x1, y1, z1)
    Node(2, x2, y2, z2)
    Node(3, x3, y3, z3)
    Node(4, x4, y4, z4)
    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Material(2, name='C30/37')
    Thickness(material_no= 2)
    Surface()

    Model.clientModel.service.finish_modification()

    A = (x2 - x1) * (y4 - y1)
    V = A * 0.2
    M = (V * 2500) / 1000

    info = ObjectsInfo.SurfacesInfo([[ObjectTypes.E_OBJECT_TYPE_SURFACE, 1]])

    assert info['Area of surfaces'] == round(A,3)
    assert info['Volume'] == round(V,3)
    assert info['Mass'] == round(M,3)

def test_envelopsize_information():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    x1, y1, z1 = 0 , 0, 0
    x2, y2, z2 = 10, 0, 0
    x3, y3, z3 = 10, 15, 0
    x4, y4, z4 = 0, 15, 0

    Node(1, x1, y1, z1)
    Node(2, x2, y2, z2)
    Node(3, x3, y3, z3)
    Node(4, x4, y4, z4)
    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Material(2, name='C30/37')
    Thickness(material_no= 2)
    Surface()

    Model.clientModel.service.finish_modification()

    X = max(x1, x2, x3, x4) - min(x1, x2, x3, x4)
    Y = max(y1, y2, y3, y4) - min(y1, y2, y3, y4)
    Z = max(z1, z2, z3, z4) - min(z1, z2, z3, z4)

    info = ObjectsInfo.EnvelopeSize([[ObjectTypes.E_OBJECT_TYPE_SURFACE, 1]])

    assert info['Size in X'] == round(X,3)
    assert info['Size in Y'] == round(Y,3)
    assert info['Size in Z'] == round(Z,3)
