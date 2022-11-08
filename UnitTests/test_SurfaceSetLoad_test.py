import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Loads.surfacesetload import SurfaceSetLoad
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.BasicObjects.surfaceSet import SurfaceSet
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model
from RFEM.enums import *

if Model.clientModel is None:
    Model()

def test_surface_set_load():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Thickness
    Thickness(1, '1', 1, 0.01)

    # Create Nodes
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 0.0, 2.0, 0.0)
    Node(3, 2.0, 2.0, 0.0)
    Node(4, 2.0, 0.0, 0.0)
    Node(5, 0.0, 4.0, 0.0)
    Node(6, 2.0, 4.0, 0.0)

    Node(7, 5, 0, 0)
    Node(8, 7, 0, 0)
    Node(9, 5, 0, 2)
    Node(10, 7, 0, 2)
    Node(11, 5, 0, -2)
    Node(12, 7, 0, -2)

    # Create Lines
    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line(5, '2 5')
    Line(6, '5 6')
    Line(7, '6 3')

    Line(8, '9 7')
    Line(9, '7 8')
    Line(10, '8 10')
    Line(11, '10 9')
    Line(12, '8 12')
    Line(13, '12 11')
    Line(14, '11 7')

    # Create Surfaces
    Surface(1, '1 2 3 4', 1)
    Surface(2, '2 5 6 7', 1)

    Surface(3, '8 9 10 11', 1)
    Surface(4, '12 13 14 9', 1)

    # Create Surface Set
    # Added types and functions just to cover SurfaceSet completely
    SurfaceSet(1, '1 2', SetType.SET_TYPE_GROUP)
    SurfaceSet(2, '3 4', SetType.SET_TYPE_GROUP)
    SurfaceSet.ContinuousSurfaces(3, '3 4')
    SurfaceSet.GroupOfSurfaces(4, '1 2')

    # Create Nodal Supports
    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)
    NodalSupport(5, '5', NodalSupportType.FIXED)
    NodalSupport(6, '6', NodalSupportType.FIXED)
    NodalSupport(7, '7', NodalSupportType.FIXED)
    NodalSupport(8, '8', NodalSupportType.FIXED)
    NodalSupport(9, '9', NodalSupportType.FIXED)
    NodalSupport(10, '10', NodalSupportType.FIXED)
    NodalSupport(11, '11', NodalSupportType.FIXED)
    NodalSupport(12, '12', NodalSupportType.FIXED)

    # Create Static Analysis Settings
    StaticAnalysisSettings(1, '1. Order', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Create Load Case
    LoadCase(1, 'DEAD', [True, 0.0, 0.0, 1.0])

    ## Default Surface Load ##
    SurfaceSetLoad(1, 1, '1', 5000)

    ## Force Type Surface Load with UNIFORM Load Distribution ##
    SurfaceSetLoad.Force(2, 1, '1', SurfaceSetLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[5000])

    ## Force Type Surface Load with LINEAR Load Distribution ##
    SurfaceSetLoad.Force(3, 1, '1', SurfaceSetLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_LINEAR, load_parameter=[5000, 6000, 7000, 2, 3, 4])

    ## Force Type Surface Load with LINEAR_X or LINEAR_Y or LINEAR_Z Load Distribution ##
    SurfaceSetLoad.Force(4, 1, '1', SurfaceSetLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, load_parameter=[5000, 6000, 2, 6])

    ## Force sType Surface Load with RADIAL Load Distribution ##
    SurfaceSetLoad.Force(5, 1, '1', SurfaceSetLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_RADIAL,(2000, 4000, 1, 6, SurfaceSetLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS, [0,0,0], [0,0,1]))

    ## Force Type Surface Set Load with varying in Z
    SurfaceSetLoad.Force(32, 1, '2', SurfaceSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z, load_parameter=[[1, 1, 1000], [2, 1, 2000]])

    ## Temperature Type Surface Load with UNIFORM Load Distribution ##
    SurfaceSetLoad.Temperature(6, 1, '1', SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[18, 2])

    ## Temperature Type Surface Load with LINEAR Load Distribution ##
    SurfaceSetLoad.Temperature(7, 1, '1', SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_LINEAR, load_parameter=[18, 2, 20, 4, 22, 6, 2, 3, 4])

    ## Temperature Type Surface Load with LINEAR_X or LINEAR_Y or LINEAR_Z Load Distribution ##
    SurfaceSetLoad.Temperature(8, 1, '1', SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, load_parameter=[18, 2, 20, 4, 2, 3])

    ## Axial Strain Type Surface Load with UNIFORM Load Distribution ##
    SurfaceSetLoad.AxialStrain(9, 1, '1', SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[0.5, 1])

    ## Axial Strain Type Surface Load with LINEAR Load Distribution ##
    SurfaceSetLoad.AxialStrain(10, 1, '1', SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_LINEAR, load_parameter=[0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 2, 3, 4])

    ## Axial Strain Type Surface Load with LINEAR_IN_X Load Distribution ##
    SurfaceSetLoad.AxialStrain(11, 1, '1', SurfaceSetLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, load_parameter=[0.005, 0.006, 0.007, 0.008, 2, 3])

    ## Precamber Type Surface Load ##
    SurfaceSetLoad.Precamber(12, 1, '1', 50)

    ## Rotary Motion Surface Load ##
    SurfaceSetLoad.RotaryMotion(13, 1, '1', load_parameter=[1, 2, SurfaceSetLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS, [1,2,3], [4,5,6]])

    ## Mass Type Surface Load ##
    SurfaceSetLoad.Mass(14, 1, '1', True, [500, 600, 700])
    SurfaceSetLoad.Mass(15, 1, '1', False, [0.5])

    Model.clientModel.service.finish_modification()

    assert Model.clientModel.service.get_surface_set_load(1, 1).uniform_magnitude == 5000

    ssl = Model.clientModel.service.get_surface_set_load(3, 1)
    assert ssl.load_distribution == 'LOAD_DISTRIBUTION_LINEAR'
    assert ssl.magnitude_2 == 6000
    assert ssl.magnitude_3 == 7000
    assert ssl.node_2 == 3

    ssl = Model.clientModel.service.get_surface_set_load(4, 1)
    assert ssl.load_distribution == 'LOAD_DISTRIBUTION_LINEAR_IN_X'
    assert ssl.magnitude_2 == 6000
    assert ssl.node_1 == 2

    ssl = Model.clientModel.service.get_surface_set_load(5, 1)
    assert ssl.load_distribution == 'LOAD_DISTRIBUTION_RADIAL'
    assert ssl.axis_definition_type == 'AXIS_DEFINITION_TWO_POINTS'
    assert ssl.axis_definition_p2_z == 1
    assert ssl.axis_definition_p1_x == 0
    assert ssl.magnitude_2 == 4000
    assert ssl.node_1 == 1

    ssl = Model.clientModel.service.get_surface_set_load(7, 1)
    assert ssl.magnitude_t_c_3 == 22
    assert ssl.node_2 == 3

    ssl = Model.clientModel.service.get_surface_set_load(10, 1)
    assert ssl.magnitude_axial_strain_2y == 0.008
    assert ssl.node_1 == 2

    ssl = Model.clientModel.service.get_surface_set_load(12, 1)
    assert ssl.load_type == 'LOAD_TYPE_PRECAMBER'
    assert ssl.uniform_magnitude == 50

    ssl = Model.clientModel.service.get_surface_set_load(13, 1)
    assert ssl.angular_velocity == 2
    assert ssl.angular_acceleration == 1
    assert ssl.axis_definition_p1_z == 3
    assert ssl.axis_definition_p2_x == 4

    ssl = Model.clientModel.service.get_surface_set_load(14, 1)
    assert ssl.magnitude_mass_y == 600
    assert ssl.magnitude_mass_z == 700
