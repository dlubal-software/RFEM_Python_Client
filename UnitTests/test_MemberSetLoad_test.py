import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Loads.membersetload import MemberSetLoad
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model
from RFEM.enums import *

if Model.clientModel is None:
    Model()

def test_member_set_load():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Section
    Section(1, 'IPE 300')
    Section(2, 'CHS 100x4')

    # Create Nodes
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 2, 0.0, 0.0)
    Node(3, 4, 0, 0)

    Node(4, 0, 5, 0)
    Node(5, 2, 5, 0)
    Node(6, 4, 5, 0)

    # Create Member
    Member(1, 1, 2, 0, 1)
    Member(2, 2, 3, 0, 1)
    Member(3, 4, 6, 0, 2)
    Member(4, 6, 5, 0, 2)

    # Create Member Set
    MemberSet(1, '1 2', SetType.SET_TYPE_CONTINUOUS)
    MemberSet(2, '3 4', SetType.SET_TYPE_CONTINUOUS)

    # Create Nodal Supports
    NodalSupport(1, '1 3 4 6', NodalSupportType.FIXED)

    # Create Static Analysis Settings
    StaticAnalysisSettings(1, '1. Order', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Create Load Case
    LoadCase(1, 'DEAD', [True, 0.0, 0.0, 1.0])

    ## Initial Member Set Load ##
    MemberSetLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 5000)

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberSetLoad.Force(2, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM with Eccentricity ##
    MemberSetLoad.Force(3, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000], force_eccentricity=True, params={'eccentricity_y_at_start' : 0.01, 'eccentricity_z_at_start': 0.02})

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM_TOTAL ##
    MemberSetLoad.Force(4, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TOTAL, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberSetLoad.Force(5, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, 5000, 1.2])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberSetLoad.Force(6, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 2, 1, 2])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberSetLoad.Force(7, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, False, 5000, 1, 2, 3])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_2x ##
    MemberSetLoad.Force(8, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 6000, 1, 2])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberSetLoad.Force(9, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberSetLoad.Force(10, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberSetLoad.Force(11, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberSetLoad.Force(12, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[4000, 8000, 12000])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_VARYING ##
    MemberSetLoad.Force(13, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])

    ## Force Type Member Set Load with LOAD_DISTRIBUTION_VARYING_IN_Z ##
    MemberSetLoad.Force(14, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberSetLoad.Moment(15, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberSetLoad.Moment(16, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, 5000, 1.2])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberSetLoad.Moment(17, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 2, 1, 2])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberSetLoad.Moment(18, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, False, 5000, 1, 2, 3])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_2x ##
    MemberSetLoad.Moment(19, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 6000, 1, 2])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberSetLoad.Moment(20, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberSetLoad.Moment(21, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberSetLoad.Moment(22, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberSetLoad.Moment(23, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[4000, 8000, 12000])

    ## Moment Type Member Set Load with LOAD_DISTRIBUTION_VARYING ##
    MemberSetLoad.Moment(24, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])

    ## Mass Type Member Set Load ##
    MemberSetLoad.Mass(25, 1, mass_components=[1000])

    ## Temperature Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberSetLoad.Temperature(26, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[18, 2])

    ## Temperature Type Member Set Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberSetLoad.Temperature(27, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## Temperature Type Member Set Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberSetLoad.Temperature(28, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## Temperature Type Member Set Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberSetLoad.Temperature(29, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3, 4, 5, 6])

    ## Temperature Type Member Set Load with LOAD_DISTRIBUTION_VARYING ##
    MemberSetLoad.Temperature(30, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285, 289], [2, 1, 293, 297]])

    ## TemperatureChange Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberSetLoad.TemperatureChange(31, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[18, 2])

    ## TemperatureChange Type Member Set Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberSetLoad.TemperatureChange(32, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## TemperatureChange Type Member Set Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberSetLoad.TemperatureChange(33, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## TemperatureChange Type Member Set Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberSetLoad.TemperatureChange(34, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3, 4, 5, 6])

    ## TemperatureChange Type Member Set Load with LOAD_DISTRIBUTION_VARYING ##
    MemberSetLoad.TemperatureChange(35, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285, 289], [2, 1, 293, 297]])

    ## AxialStrain Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberSetLoad.AxialStrain(36, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[0.005])

    ## AxialStrain Type Member Set Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberSetLoad.AxialStrain(37, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[12, 16, False, False, 1, 2])

    ## AxialStrain Type Member Set Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberSetLoad.AxialStrain(38, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[12, 16, False, False, 1, 2])

    ## AxialStrain Type Member Set Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberSetLoad.AxialStrain(39, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[1, 2, 3])

    ## AxialStrain Type Member Set Load with LOAD_DISTRIBUTION_VARYING ##
    MemberSetLoad.AxialStrain(40, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[[1, 1, 285, 289], [2, 1, 293, 297]])

    ## AxialDisplacement Type Member Set Load ##
    MemberSetLoad.AxialDisplacement(41, 1, '1', MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X, 0.05)

    ## Precamber Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberSetLoad.Precamber(42, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[0.005])

    ## Precamber Type Member Set Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberSetLoad.Precamber(43, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Precamber Type Member Set Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberSetLoad.Precamber(44, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Precamber Type Member Set Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberSetLoad.Precamber(45, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3])

    ## Precamber Type Member Set Load with LOAD_DISTRIBUTION_VARYING ##
    MemberSetLoad.Precamber(46, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285], [2, 1, 293]])

    ## InitialPrestress Type Member Set Load ##
    MemberSetLoad.InitialPrestress(47, 1, '1', MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X, 50)

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberSetLoad.Displacement(48, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5])

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberSetLoad.Displacement(49, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, 1])

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberSetLoad.Displacement(50, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, 1, 2])

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberSetLoad.Displacement(51, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, False, 1, 2, 3])

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_2 ##
    MemberSetLoad.Displacement(52, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, 0.6, False, False, 1, 2])

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberSetLoad.Displacement(53, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[0.001, 1, 1], [0.002, 2, 1]])

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberSetLoad.Displacement(54, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberSetLoad.Displacement(55, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberSetLoad.Displacement(56, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3])

    ## Displacement Type Member Set Load with LOAD_DISTRIBUTION_VARYING ##
    MemberSetLoad.Displacement(57, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285], [2, 1, 293]])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberSetLoad.Rotation(58, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberSetLoad.Rotation(59, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, 1])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberSetLoad.Rotation(60, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, 1, 2])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberSetLoad.Rotation(61, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, False, 1, 2, 3])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_2 ##
    MemberSetLoad.Rotation(62, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, 0.6, False, False, 1, 2])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberSetLoad.Rotation(63, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[1, 1, 285], [2, 1, 293]])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberSetLoad.Rotation(64, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberSetLoad.Rotation(65, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberSetLoad.Rotation(66, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3])

    ## Rotation Type Member Set Load with LOAD_DISTRIBUTION_VARYING ##
    MemberSetLoad.Rotation(67, 1, '1', MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285], [2, 1, 293]])

    ## Pipe Content Full Type Member Set Load ##
    MemberSetLoad.PipeContentFull(68, 1, '2', specific_weight=5000)

    ## Pipe Content Partial Type Member Set Load ##
    MemberSetLoad.PipeContentPartial(69, 1, '2', specific_weight=2000, filling_height=0.1)

    ## Pipe Internal Pressure Type Member Set Load ##
    MemberSetLoad.PipeInternalPressure(70, 1, '2', 2000)

    ## Pipe Rotary Motion Type Member Set Load ##
    MemberSetLoad.RotaryMotion(71, 1, '2', 3.5, 5,
                               MemberSetLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS,
                               MemberLoadAxisDefinitionAxisOrientation.AXIS_NEGATIVE,
                               MemberSetLoadAxisDefinition.AXIS_Y, [10,11,12], [0,5,6])

    #Calculate_all() # Don't use in unit tests. See template for more info.

    Model.clientModel.service.finish_modification()
