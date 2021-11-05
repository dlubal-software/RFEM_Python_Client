import sys
sys.path.append(".")

# Import the relevant Libraries
from os import name
from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.solid import *
from RFEM.Tools.centreOfGravityAndObjectInfo import *

def test_centre_of_gravity():

    clientModel.service.begin_modification('new')

    x1, y1, z1, = 0, 0, 0
    x2, y2, z2 = 4, 10, -6
    Node(1, x1, y1, z1), Node(2, x2, y2, z2)
    Material(1, 'S235')
    Section()
    Member(1, start_node_no= 1, end_node_no= 2)

    clientModel.service.finish_modification()

    CoG_X = (x2 - x1) / 2
    CoG_Y = (y2 - y1) / 2
    CoG_Z = (z2 - z1) / 2
    L = round(sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2),3)

    assert CoG_X == ObjectInformation.CentreOfGravity(ObjectInformation, coord= 'X')
    assert CoG_Y == ObjectInformation.CentreOfGravity(ObjectInformation, coord= 'Y')
    assert CoG_Z == ObjectInformation.CentreOfGravity(ObjectInformation, coord= 'Z')

def test_member_information():
    
    clientModel.service.begin_modification('new')

    x1, y1, z1, = 0, 0, 0
    x2, y2, z2 = 4, 10, -6
    Node(1, x1, y1, z1), Node(2, x2, y2, z2)
    Material(1, 'S235')
    Section()
    Member(1, start_node_no= 1, end_node_no= 2)

    clientModel.service.finish_modification()

    L = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    A = 53.80 / (100 * 100)
    V = L * A
    M = (V * 7850) / 1000

    assert round(L,3) == ObjectInformation.MemberInformation(ObjectInformation, information= SelectedObjectInformation.LENGTH)
    assert round(V,3) == ObjectInformation.MemberInformation(ObjectInformation, information= SelectedObjectInformation.VOLUME)
    assert round(M,3) == ObjectInformation.MemberInformation(ObjectInformation, information= SelectedObjectInformation.MASS)

def test_surface_information():

    clientModel.service.begin_modification('new')

    x1, y1, z1 = 0 , 0, 0
    x2, y2, z2 = 10, 0, 0
    x3, y3, z3 = 10, 15, 0
    x4, y4, z4 = 0, 15, 0

    Node(1, x1, y1, z1), Node(2, x2, y2, z2), Node(3, x3, y3, z3), Node(4, x4, y4, z4)
    Line(1, '1 2'), Line(2, '2 3'), Line(3, '3 4'), Line(4, '4 1')
    Material(2, name='C30/37')
    Thickness(material_no= 2)
    Surface()

    clientModel.service.finish_modification()

    A = (x2 - x1) * (y4 - y1)
    V = A * 0.2
    M = (V * 2500) / 1000

    assert round(A,3) == ObjectInformation.SurfaceInformation(ObjectInformation, information= SelectedObjectInformation.AREA)
    assert round(V,3) == ObjectInformation.SurfaceInformation(ObjectInformation, information= SelectedObjectInformation.VOLUME)
    assert round(M,3) == ObjectInformation.SurfaceInformation(ObjectInformation, information= SelectedObjectInformation.MASS)