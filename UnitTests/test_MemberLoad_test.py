'''
DUE TO THE IMPORTANCE OF THE MEMBER LOAD LIBRARY, EACH MEMBER FORCE AND DISTRIBUTION COMBINATION WAS DOCUMENTED BELOW.
THIS PROVIDES USERS WITH A REFERENCE FOR IMPLEMENTATION.
PERTAINING TO THE UNIT TESTS: A SELECTION OF KEY PARAMETERS WERE SELECTED FOR THE ASSERTIONS.
'''
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model
from RFEM.enums import *

if Model.clientModel is None:
    Model()

def test_member_loads():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Thickness
    Section(1, 'IPE 300')
    Section(2, 'CHS 100x4')

    # Create Nodes
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4.0, 0.0, 0.0)

    Node(3, 0, 5, 0)
    Node(4, 4, 5, 0)

    Member(1, 1, 2, 0, 1, 1)
    Member(2, 3, 4, 0, 2, 2)

    # Create Nodal Supports
    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    # Create Static Analysis Settings
    StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Create Load Case
    LoadCase(1, 'DEAD', [True, 0.0, 0.0, 1.0])

    ## Initial Member Load ##
    MemberLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 5000)

    ## Force Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Force(2, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Force Type Member Load with LOAD_DISTRIBUTION_UNIFORM with Eccentricity ##
    MemberLoad.Force(3, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000], force_eccentricity=True, params={'eccentricity_y_at_start' : 0.01, 'eccentricity_z_at_start': 0.02})

    ## Force Type Member Load with LOAD_DISTRIBUTION_UNIFORM_TOTAL ##
    MemberLoad.Force(4, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TOTAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberLoad.Force(5, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, 5000, 1.2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberLoad.Force(6, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 2, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberLoad.Force(7, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, False, 5000, 1, 2, 3])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x ##
    MemberLoad.Force(8, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 6000, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberLoad.Force(9, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 4000], [2, 5000]])

    ## Force Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Force(10, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Force(11, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Force(12, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[4000, 8000, 12000])

    ## Force Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Force(13, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 4000], [2, 5000]])

    ## Force Type Member Load with LOAD_DISTRIBUTION_VARYING_IN_Z ##
    MemberLoad.Force(14, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 4000], [2, 5000]])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Moment(15, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberLoad.Moment(16, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, 5000, 1.2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberLoad.Moment(17, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 2, 1, 2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberLoad.Moment(18, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, False, 5000, 1, 2, 3])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x ##
    MemberLoad.Moment(19, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 6000, 1, 2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberLoad.Moment(20, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 4000], [2, 5000]])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Moment(21, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Moment(22, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Moment(23, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[4000, 8000, 12000])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Moment(24, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 4000], [2, 5000]])

    ## Mass Type Member Load ##
    MemberLoad.Mass(25, 1, mass_components=[1000])

    ## Temperature Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Temperature(26, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[18, 2])

    ## Temperature Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Temperature(27, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## Temperature Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Temperature(28, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## Temperature Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Temperature(29, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3, 4, 5, 6])

    ## Temperature Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Temperature(30, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 285, 289], [2, 293, 297]])

    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.TemperatureChange(31, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[18, 2])

    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.TemperatureChange(32, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.TemperatureChange(33, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.TemperatureChange(34, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3, 4, 5, 6])

    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.TemperatureChange(35, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 285, 289], [2, 293, 297]])

    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.AxialStrain(36, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[0.005])

    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.AxialStrain(37, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[12, 16, False, False, 1, 2])

    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.AxialStrain(38, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[12, 16, False, False, 1, 2])

    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.AxialStrain(39, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[1, 2, 3])

    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.AxialStrain(40, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[[1, 285, 289], [2, 293, 297]])

    ## AxialDisplacement Type Member Load ##
    MemberLoad.AxialDisplacement(41, 1, '1', MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, 0.05)

    ## Precamber Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Precamber(42, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[0.005])

    ## Precamber Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Precamber(43, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Precamber Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Precamber(44, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Precamber Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Precamber(45, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3])

    ## Precamber Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Precamber(46, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 285], [2, 293]])

    ## InitialPrestress Type Member Load ##
    MemberLoad.InitialPrestress(47, 1, '1', MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, 50)

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Displacement(48, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberLoad.Displacement(49, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, 1])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberLoad.Displacement(50, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, 1, 2])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberLoad.Displacement(51, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, False, 1, 2, 3])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2 ##
    MemberLoad.Displacement(52, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, 0.6, False, False, 1, 2])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberLoad.Displacement(53, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[0.001, 1, 1], [0.002, 2, 1]])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Displacement(54, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Displacement(55, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Displacement(56, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Displacement(57, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 285], [2, 293]])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Rotation(58, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberLoad.Rotation(59, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, 1])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberLoad.Rotation(60, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, 1, 2])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberLoad.Rotation(61, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, False, 1, 2, 3])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2 ##
    MemberLoad.Rotation(62, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, 0.6, False, False, 1, 2])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberLoad.Rotation(63, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[1, 285], [2, 293]])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Rotation(64, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Rotation(65, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Rotation(66, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Rotation(67, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 285], [2, 293]])

    ## PipeContentFull Type Member Load ##
    MemberLoad.PipeContentFull(68, 1, '2', MemberLoadDirectionOrientation.LOAD_DIRECTION_FORWARD, 50)

    MemberLoad.RotaryMotion(69, 1, '2', 2, 3, MemberLoadAxisDefinitionType.AXIS_DEFINITION_POINT_AND_AXIS, axis_definition_p1=[1,1,0])

    Model.clientModel.service.finish_modification()

    ml = Model.clientModel.service.get_member_load(3, 1)
    assert ml.load_direction == 'LOAD_DIRECTION_LOCAL_Z'
    assert ml.magnitude == 5000
    assert ml.has_force_eccentricity == True
    assert ml.eccentricity_y_at_start == 0.01
    assert ml.eccentricity_z_at_start == 0.02

    ml = Model.clientModel.service.get_member_load(19, 1)
    assert ml.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_2'
    assert ml.load_direction == 'LOAD_DIRECTION_LOCAL_Z'
    assert ml.magnitude_2 == 6000
    assert ml.distance_a_absolute == 1

    ml = Model.clientModel.service.get_member_load(25, 1)
    assert ml.load_type == 'E_TYPE_MASS'
    assert ml.load_distribution == 'LOAD_DISTRIBUTION_UNIFORM'
    assert ml.mass_global == 1000

    ml = Model.clientModel.service.get_member_load(30, 1)
    assert ml.load_type == 'LOAD_TYPE_TEMPERATURE'
    assert ml.load_distribution == 'LOAD_DISTRIBUTION_VARYING'
    assert ml.varying_load_parameters['member_load_varying_load_parameters'][1].row['distance'] == 2
    assert ml.varying_load_parameters['member_load_varying_load_parameters'][0].row['magnitude'] == 285

    ml = Model.clientModel.service.get_member_load(33, 1)
    assert ml.load_type == 'LOAD_TYPE_TEMPERATURE_CHANGE'
    assert ml.load_distribution == 'LOAD_DISTRIBUTION_TAPERED'
    assert ml.magnitude_t_c_1 == 18
    assert ml.magnitude_delta_t_2 == 16
    assert ml.distance_b_absolute == 2

    ml = Model.clientModel.service.get_member_load(40, 1)
    assert ml.load_type == 'LOAD_TYPE_AXIAL_STRAIN'
    assert ml.load_distribution == 'LOAD_DISTRIBUTION_VARYING'
    assert ml.varying_load_parameters['member_load_varying_load_parameters'][1].row['distance'] == 2
    assert ml.varying_load_parameters['member_load_varying_load_parameters'][0].row['magnitude'] == 285

    ml = Model.clientModel.service.get_member_load(41, 1)
    assert ml.load_type == 'LOAD_TYPE_AXIAL_DISPLACEMENT'
    assert ml.magnitude == 0.05

    ml = Model.clientModel.service.get_member_load(43, 1)
    assert ml.load_type == 'LOAD_TYPE_PRECAMBER'
    assert ml.load_distribution == 'LOAD_DISTRIBUTION_TRAPEZOIDAL'
    assert ml.magnitude_2 == 16

    ml = Model.clientModel.service.get_member_load(47, 1)
    assert ml.load_type == 'LOAD_TYPE_INITIAL_PRESTRESS'
    assert ml.load_distribution == 'LOAD_DISTRIBUTION_UNIFORM'
    assert ml.magnitude == 50

    ml = Model.clientModel.service.get_member_load(52, 1)
    assert ml.load_type == 'LOAD_TYPE_DISPLACEMENT'
    assert ml.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_2'
    assert ml.magnitude_2 == 0.6
    assert ml.distance_a_absolute == 1

    ml = Model.clientModel.service.get_member_load(64, 1)
    assert ml.load_type == 'LOAD_TYPE_ROTATION'
    assert ml.load_distribution == 'LOAD_DISTRIBUTION_TRAPEZOIDAL'
    assert ml.magnitude_1 == 12
    assert ml.distance_b_absolute == 2

    ml = Model.clientModel.service.get_member_load(68, 1)
    assert ml.load_type == 'LOAD_TYPE_PIPE_CONTENT_FULL'
    assert ml.magnitude == 50

    ml = Model.clientModel.service.get_member_load(69, 1)
    assert ml.load_type == 'LOAD_TYPE_ROTARY_MOTION'
    assert ml.angular_velocity == 3
    assert ml.axis_definition_type == 'AXIS_DEFINITION_POINT_AND_AXIS'
