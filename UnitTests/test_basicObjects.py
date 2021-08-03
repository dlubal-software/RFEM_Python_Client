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
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.solidSet import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.surfaceLoad import *
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')


def test_material():

    clientModel.service.begin_modification('new')
    Material(1, 'S235')
    clientModel.service.finish_modification()

    material = clientModel.service.get_material(1)
    print(material)
    assert material.name == 'S235'


def test_section():

    clientModel.service.begin_modification('new')
    Material(1, 'S235')
    Section(1, 'IPE 200')
    clientModel.service.finish_modification()

    section = clientModel.service.get_section(1)
    print(section)
    assert section.material == 1
    assert section.name == 'IPE 200'
    assert section.rotation_angle == 0.0


def test_nodes():

    clientModel.service.begin_modification('new')
    Node(1, 1.0, 2.0, 3.0)
    Node(2, 4.0, 5.0, 6.0)
    clientModel.service.finish_modification()

    nodeOne = clientModel.service.get_node(1)
    nodeTwo = clientModel.service.get_node(2)

    assert nodeOne.coordinate_1 == 1.0
    assert nodeOne.coordinate_2 == 2.0
    assert nodeOne.coordinate_3 == 3.0
    assert nodeOne.coordinate_system == 1
    assert nodeOne.comment == None
    assert nodeOne.is_generated == False

    assert nodeTwo.coordinate_1 == 4.0
    assert nodeTwo.coordinate_2 == 5.0
    assert nodeTwo.coordinate_3 == 6.0
    assert nodeTwo.coordinate_system == 1
    assert nodeTwo.comment == None
    assert nodeTwo.is_generated == False

