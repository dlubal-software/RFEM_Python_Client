import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.Loads.solidLoad import SolidLoad
from RFEM.Loads.solidSetLoad import SolidSetLoad
from RFEM.enums import NodalSupportType, StaticAnalysisType, LoadDirectionType, SolidLoadType, SolidLoadDistribution
from RFEM.enums import SolidLoadDirection, SolidSetLoadType, SolidSetLoadDistribution, SolidSetLoadDirection
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.solid import Solid
from RFEM.BasicObjects.solidSet import SolidSet
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad

if Model.clientModel is None:
    Model()

def test_solid_loads():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    # Solid 1
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10.0, 0.0, 0.0)
    Node(3, 10.0, 10.0, 0.0)
    Node(4, 0.0, 10.0, 0.0)

    Node(5, 0.0, 0.0, -5.0)
    Node(6, 10.0, 0.0, -5.0)
    Node(7, 10.0, 10.0, -5.0)
    Node(8, 0.0, 10.0, -5.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '5 6')
    Line(6, '6 7')
    Line(7, '7 8')
    Line(8, '8 5')

    Line(9, '1 5')
    Line(10, '2 6')
    Line(11, '3 7')
    Line(12, '4 8')

    Thickness(1, 'My Test Thickness', 1, 0.05)

    Surface(1, '1-4', 1)
    Surface(2, '5-8', 1)
    Surface(3, '1 9 5 10', 1)
    Surface(4, '2 10 6 11', 1)
    Surface(5, '3 11 7 12', 1)
    Surface(6, '4 12 8 9', 1)

    Solid(1, '1-6', 1)

    NodalSupport(1, '1 2 3 4 9 12 10 11 17 18 ', NodalSupportType.HINGED)

    StaticAnalysisSettings(1, 'Geometric linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1 , 'Test load case', [True, 0.0, 0.0, 1.0])

    NodalLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_X, 12.8)

    SolidLoad(1, 1, '1', SolidLoadType.LOAD_TYPE_FORCE, SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 1289.0, 'My Comment')
    SolidLoad.Force(2, 1, '1', SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 8569.21, 'My 2nd Comment')
    SolidLoad.Force(3, 1, '1', SolidLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 78548.21, 'My 2nd Comment')
    SolidLoad.Temperature(4, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,[78.4])
    SolidLoad.Temperature(5, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, [105.4, 507.8, 4, 3])
    SolidLoad.Temperature(6, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Y, [237, -8.9, 5, 7])
    SolidLoad.Temperature(7, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Z, [-2587.98, -8.9, 5, 2])

    SolidLoad.Strain(8, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, [0.01, 0.02, 0.03])
    SolidLoad.Strain(9, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 5, 6])
    SolidLoad.Strain(10, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Y, [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 5, 8])
    SolidLoad.Strain(11, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Z, [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 5, 1])

    SolidLoad.Motion(12, 1, '1',[ 5, 2, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])

    # Solid 2
    Node(9, 0.0, 20.0, 0.0)
    Node(10, 10.0, 20.0, 0.0)
    Node(11, 10.0, 30.0, 0.0)
    Node(12, 0.0, 30.0, 0.0)

    Node(13, 0.0, 20.0, -5.0)
    Node(14, 10.0, 20.0, -5.0)
    Node(15, 10.0, 30.0, -5.0)
    Node(16, 0.0, 30.0, -5.0)

    Line(13, '9 10')
    Line(14, '10 11')
    Line(15, '11 12')
    Line(16, '12 9')

    Line(17, '13 14')
    Line(18, '14 15')
    Line(19, '15 16')
    Line(20, '16 13')

    Line(21, '9 13')
    Line(22, '10 14')
    Line(23, '11 15')
    Line(24, '12 16')

    Surface(7, '13-16', 1)
    Surface(8, '17-20', 1)
    Surface(9, '13 22 17 21', 1)
    Surface(10, '15 23 19 24', 1)
    Surface(11, '16 21 20 24', 1)
    Surface(12, '14 22 18 23', 1)

    Solid(2, '7-12', 1)

    # Solid 3
    Node(17, 20.0, 20.0, 0.0)
    Node(18, 20.0, 30.0, 0.0)
    Node(19, 20.0, 20.0, -5.0)
    Node(20, 20.0, 30.0, -5.0)

    Line(25, '10 17')
    Line(26, '17 18')
    Line(27, '18 11')
    Line(28, '14 19')
    Line(29, '19 20')
    Line(30, '20 15')
    Line(31, '17 19')
    Line(32, '18 20')

    Surface(13, '25 26 27 14', 1)
    Surface(14, '28 29 30 18', 1)
    Surface(15, '25 31 28 22', 1)
    Surface(16, '27 32 30 23', 1)
    Surface(17, '26 31 29 32', 1)

    Solid(3, '13-17,12', 1)

    # Solid Set
    SolidSet.ContinuousSolids(1, '2 3')

    SolidSetLoad(1, 1, '1', SolidSetLoadType.LOAD_TYPE_FORCE, SolidSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, SolidSetLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 58.9*1000, 'My Comment')
    SolidSetLoad.Force(2, 1, '1', SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 8974.123, 'My 2nd Comment')
    SolidSetLoad.Temperature(3, 1, '1', SolidSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, [25489], 'My 3rd Comment')
    SolidSetLoad.Temperature(4, 1, '1', SolidSetLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, [1.5, 8.9, 16, 15], 'My 3rd Comment')
    SolidSetLoad.Strain(5, 1, '1', SolidSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, [0.1, 0.2, 0.3], 'My Comment')
    SolidSetLoad.Strain(6, 1, '1', SolidLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Y, [0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 13, 16])
    SolidSetLoad.Motion(7, 1, '1', [1.5, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])

    #Calculate_all() # Don't use in unit tests. See template for more info.

    sl = Model.clientModel.service.get_solid_load(1, 1)
    assert sl.load_type == 'LOAD_TYPE_FORCE'

    sl = Model.clientModel.service.get_solid_load(2, 1)
    assert sl.load_type == 'LOAD_TYPE_FORCE'

    sl = Model.clientModel.service.get_solid_load(3, 1)
    assert sl.load_distribution == 'LOAD_DISTRIBUTION_UNIFORM'

    sl = Model.clientModel.service.get_solid_load(4, 1)
    assert sl.load_type == 'LOAD_TYPE_TEMPERATURE'

    Model.clientModel.service.finish_modification()
