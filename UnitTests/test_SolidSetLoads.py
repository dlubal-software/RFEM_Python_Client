import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.Loads.solidSetLoad import SolidSetLoad
from RFEM.enums import SolidLoadDirection, SolidSetLoadType, SolidSetLoadDistribution, SolidSetLoadDirection, StaticAnalysisType, SolidLoadDistribution
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.solid import Solid
from RFEM.BasicObjects.solidSet import SolidSet
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase

if Model.clientModel is None:
    Model()

def test_solid_set_loads():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5.0, 0.0, 0.0)
    Node(3, 5.0, 6.0, 0.0)
    Node(4, 0.0, 6.0, 0.0)

    Node(5, 0.0, 0.0, 3.0)
    Node(6, 5.0, 0.0, 3.0)
    Node(7, 5.0, 6.0, 3.0)
    Node(8, 0.0, 6.0, 3.0)

    Node(9, 0.0, 0.0, 6.0)
    Node(10, 5.0, 0.0, 6.0)
    Node(11, 5.0, 6.0, 6.0)
    Node(12, 0.0, 6.0, 6.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '5 6')
    Line(6, '6 7')
    Line(7, '7 8')
    Line(8, '8 5')

    Line(9, '9 10')
    Line(10, '10 11')
    Line(11, '11 12')
    Line(12, '12 9')

    Line(13, '1 5')
    Line(15, '2 6')
    Line(16, '3 7')
    Line(17, '4 8')

    Line(18, '5 9')
    Line(19, '6 10')
    Line(20, '7 11')
    Line(21, '8 12')

    Thickness(1, 'My Thickness', 1, 0.05)

    Surface(1, '1-4', 1, 'My Test 1')
    Surface(2, '5-8', 1, 'My Test 2')
    Surface(3, '9-12', 1, 'My Test 3')

    Surface(4, '1 15 5 13', 1, 'My Test 4')
    Surface(5, '2 16 6 15', 1, 'My Test 5')
    Surface(6, '3 17 7 16', 1, 'My Test 6')
    Surface(7, '4 13 8 17', 1, 'My Test 7')

    Surface(8, '5 19 9 18', 1)
    Surface(9, '6 19 10 20', 1)
    Surface(10, '7 20 11 21', 1)
    Surface(11, '8 18 12 21', 1)

    Solid(1, '1 2 4 5 6 7')
    Solid(2, '2 3 8 9 10 11')

    SolidSet(1, '1 2')

    StaticAnalysisSettings(1, 'LINEAR', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'Test 1')

    SolidSetLoad(1, 1, '1', SolidSetLoadType.LOAD_TYPE_FORCE, SolidSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, SolidSetLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 58.9*1000, 'My Comment')
    SolidSetLoad.Force(2, 1, '1', SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 8974.123, 'My 2nd Comment')
    SolidSetLoad.Temperature(3, 1, '1', SolidSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, [25489], 'My 3rd Comment')
    SolidSetLoad.Temperature(4, 1, '1', SolidSetLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, [1.5, 8.9, 11, 12], 'My 3rd Comment')
    SolidSetLoad.Strain(5, 1, '1', SolidSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, [0.1, 0.2, 0.3], 'My Comment')
    SolidSetLoad.Strain(6, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, [0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 9, 10])
    SolidSetLoad.Motion(7, 1, '1', [1.5, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])

    Model.clientModel.service.finish_modification()

    ssl = Model.clientModel.service.get_solid_set_load(1, 1)
    assert ssl.load_type == 'LOAD_TYPE_FORCE'

    ssl = Model.clientModel.service.get_solid_set_load(2, 1)
    assert ssl.load_direction == 'LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE'

    ssl = Model.clientModel.service.get_solid_set_load(3, 1)
    assert ssl.load_distribution == 'LOAD_DISTRIBUTION_UNIFORM'

    ssl = Model.clientModel.service.get_solid_set_load(5, 1)
    assert ssl.comment == 'My Comment'

    ssl = Model.clientModel.service.get_solid_set_load(7, 1)
    assert ssl.angular_acceleration == 0.2
