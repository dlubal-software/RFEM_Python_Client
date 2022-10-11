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
    Create Nodes, Lines, Members and Sections

    Run function to test the output

    """

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 0, 5, 0)
    Node(4, 5, 5, 0)

    Node(5, 1, 1, 0)
    Node(6, 4, 1, 0)
    Node(7, 4, 4, 0)
    Node(8, 1, 4, 0)

    Node(9, 0, 0, 1)
    Node(10, 5, 0, 1)
    Node(11, 0, 5, 1)
    Node(12, 5, 5, 1)

    Node(13, 0, 0, 2)
    Node(14, 5, 0, 2)
    Node(15, 0, 5, 2)
    Node(16, 5, 5, 2)


    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '3 4')
    Line(4, '1 3')
    LineSet(1, '1 2')

    Line(5, '5 6')
    Line(6, '6 7')
    Line(7, '7 8')
    Line(8, '8 5')
    LineSet(2, '5 6 7 8' )

    Line(9, '9 10')
    Line(10, '9 11')
    Line(11, '11 12')
    Line(12, '12 10')
    LineSet(3, '9 10 11 12')

    Line(13, '13 14')
    Line(14, '13 15')
    Line(15, '15 16')
    Line(16, '16 14')
    LineSet(4, '13 14 15 16')

    Line(17, '9 13')
    Line(18, '10 14')
    Line(19, '11 15')
    Line(20, '12 16')



    Material(1, 'S235')

    Section(1, 'IPE 300', 1)


    Member(1, 1, 2, 0, 1, 1,)
    Member(2, 2, 4, 0, 1, 1,)
    MemberSet(1, '1 2')


    Surface(1, '1 2 3 4', 1)

    Surface(2, '9 10 11 12', 1)
    Surface(3, '13 14 15 16', 1)
    Surface(4, '11 15 19 20', 1)
    Surface(5, '12 16 18 20', 1)
    Surface(6, '9 13 17 18', 1)
    Surface(7, '10 14 17 19', 1)
    SurfaceSet(1, '2 3 4 5 6 7')

    Opening(1, '5 6 7 8')

    Solid(1, '2 3 4 5 6 7')
    SolidSet(1, '1')

    Thickness(1, '', 1)

    Model.clientModel.service.finish_modification()


    ObjectDictionary = GetObjectNumbersByType.GetBasicObjects()


    assert ObjectDictionary["Line"] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

    assert ObjectDictionary['Line_Set'] == [1, 2, 3, 4]

    assert ObjectDictionary["Material"] == [1]

    assert ObjectDictionary["Member"] == [1, 2]

    assert ObjectDictionary["Member_Set"] == [1]

    assert ObjectDictionary["Node"] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    assert ObjectDictionary["Opening"] == [1]

    assert ObjectDictionary["Section"] == [1]

    assert ObjectDictionary["Solid"] == [1]

    assert ObjectDictionary["Solid_Set"] == [1]

    assert ObjectDictionary["Surface"] == [1, 2, 3, 4, 5, 6, 7]

    assert ObjectDictionary["Surface_Set"] == [1]

    assert ObjectDictionary["Thickness"] == [1]


