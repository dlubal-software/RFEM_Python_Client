import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Loads.lineLoad import LineLoad
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Loads.surfaceLoad import SurfaceLoad
from RFEM.Loads.freeLoad import FreeLoad

if Model.clientModel is None:
    Model()

### Nodal Load Unit Tests ###
def test_nodal_load_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    NodalLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 5000)

    Model.clientModel.service.finish_modification()

    nodal_load = Model.clientModel.service.get_nodal_load(1, 1)

    assert nodal_load.no == 1
    assert nodal_load.force_magnitude == 5000

def test_nodal_load_force():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    NodalLoad.Force(0, 1, 1, '1', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 5000)
    Model.clientModel.service.finish_modification()

    nodal_load = Model.clientModel.service.get_nodal_load(1, 1)

    assert nodal_load.no == 1
    assert nodal_load.force_magnitude == 5000

def test_nodal_load_moment():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    NodalLoad.Moment(0, 1, 1, '1', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 5000)

    Model.clientModel.service.finish_modification()

    nodal_load = Model.clientModel.service.get_nodal_load(1, 1)

    assert nodal_load.no == 1
    assert nodal_load.moment_magnitude == 5000

def test_nodal_load_components():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    NodalLoad.Components(0, 1, 1, '1', [5000, 0, 0, 0, 6000, 0])

    Model.clientModel.service.finish_modification()

    nodal_load = Model.clientModel.service.get_nodal_load(1, 1)

    assert nodal_load.components_moment_y == 6000
    assert nodal_load.components_force_x  == 5000

def test_nodal_load_mass():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 2, 0, 0)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    NodalLoad.Mass(0, 1, 1, '1', False,[5000])

    Model.clientModel.service.finish_modification()

    nodal_load = Model.clientModel.service.get_nodal_load(1, 1)

    assert nodal_load.no == 1
    assert nodal_load.mass_global == 5000

### Member Load Unit Tests ###

def test_member_load_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 4000)

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 4000

def test_member_load_force():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.Force(0, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [6000])

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 6000

def test_member_load_moment():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.Moment(0, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [3000])

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 3000

def test_member_load_mass():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.Mass(0, 1, 1, '1', False, mass_components=[5000])
    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.mass_global == 5000

def test_member_load_temperature():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.Temperature(0, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.497, 0.596])

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.magnitude_t_b  == 0.497
    assert member_load.magnitude_t_t  == 0.596

def test_member_load_temperature_change():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.TemperatureChange(0, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, 0.6])

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.magnitude_delta_t   == 0.5
    assert member_load.magnitude_t_c   == 0.6

def test_member_load_axial_strain():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.AxialStrain(0, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, [0.5])

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.magnitude == 0.5
    assert member_load.load_type == "LOAD_TYPE_AXIAL_STRAIN"

def test_member_load_axial_displacement():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.AxialDisplacement(0, 1, 1, '1', MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, 50)

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 50

def test_member_load_precamber():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.Precamber(0, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [5])

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 5

def test_member_load_initial_prestress():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.InitialPrestress(0, 1, 1, '1', MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, 50)

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 50

def test_member_load_displacement():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.Displacement(0, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [60])

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 60

def test_member_load_rotation():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.Rotation(0, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.6])

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 0.6

def test_member_load_pipecontentfull():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'CHS 100x4', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.PipeContentFull(0, 1, 1, '1', MemberLoadDirectionOrientation.LOAD_DIRECTION_FORWARD, 50)

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 50

def test_member_load_pipecontentpartial():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'CHS 100x4', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.PipeContentPartial(0, 1, 1, '1', MemberLoadDirectionOrientation.LOAD_DIRECTION_FORWARD, 50, 50)

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 50

def test_member_load_pipeinternalpressure():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Material(1, 'S235')
    Section(1, 'CHS 100x4', 1)
    Member(1,  1, 2, 0, 1, 1)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    MemberLoad.PipeInternalPressure(0, 1, 1, '1', 50)

    Model.clientModel.service.finish_modification()

    member_load = Model.clientModel.service.get_member_load(1, 1)

    assert member_load.no == 1
    assert member_load.magnitude == 50

### Surface Load Unit Tests ###

def test_surface_load_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    SurfaceLoad(1, 1, '1', 5000)

    Model.clientModel.service.finish_modification()

    surface_load = Model.clientModel.service.get_surface_load(1, 1)

    assert surface_load.no == 1
    assert surface_load.uniform_magnitude == 5000

def test_surface_load_force():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    SurfaceLoad.Force(0, 1, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[5000])

    Model.clientModel.service.finish_modification()

    surface_load = Model.clientModel.service.get_surface_load(1, 1)

    assert surface_load.no == 1
    assert surface_load.uniform_magnitude == 5000

def test_surface_load_temperature():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    SurfaceLoad.Temperature(0, 1, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[18, 2])

    Model.clientModel.service.finish_modification()

    surface_load = Model.clientModel.service.get_surface_load(1, 1)

    assert surface_load.no == 1
    assert surface_load.uniform_magnitude_delta_t == 2

def test_surface_load_axial_strain():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    SurfaceLoad.AxialStrain(0, 1, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[0.5, 1])

    Model.clientModel.service.finish_modification()

    surface_load = Model.clientModel.service.get_surface_load(1, 1)

    assert surface_load.no == 1
    assert surface_load.magnitude_axial_strain_x == 0.5

def test_surface_load_precamber():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    SurfaceLoad.Precamber(0, 1, 1, '1', 50)

    Model.clientModel.service.finish_modification()

    surface_load = Model.clientModel.service.get_surface_load(1, 1)

    assert surface_load.no == 1
    assert surface_load.uniform_magnitude == 50

def test_surface_load_mass():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    SurfaceLoad.Mass(0, 1, 1, '1', individual_mass_components=True, mass_parameter=[500, 600, 700])

    Model.clientModel.service.finish_modification()

    surface_load = Model.clientModel.service.get_surface_load(1, 1)

    assert surface_load.no == 1

### Line Load Unit Tests ##

def test_line_load_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    LineLoad(1, 1, '1', magnitude=500)

    Model.clientModel.service.finish_modification()

    line_load = Model.clientModel.service.get_line_load(1, 1)

    assert line_load.no == 1
    assert line_load.magnitude == 500

def test_line_load_force():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    LineLoad.Force(LineLoad, 1, 1, '1',
                     load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                     load_parameter=[1000])

    Model.clientModel.service.finish_modification()

    line_load = Model.clientModel.service.get_line_load(1, 1)

    assert line_load.no == 1
    assert line_load.magnitude == 1000

def test_line_load_moment():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    LineLoad.Moment(LineLoad, 1, 1, '1',
                     load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                     load_parameter=[2000])

    Model.clientModel.service.finish_modification()

    line_load = Model.clientModel.service.get_line_load(1, 1)

    assert line_load.no == 1
    assert line_load.magnitude == 2000

def test_line_load_mass():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    LineLoad.Mass(LineLoad, 1, 1, '1',
                     individual_mass_components= False,
                     mass_components= [10])

    Model.clientModel.service.finish_modification()

    line_load = Model.clientModel.service.get_line_load(1, 1)

    assert line_load.no == 1
    assert line_load.mass_global == 10

### Free Load Unit Tests ###

def test_free_concentrated_load():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10.0, 0.0, 0.0)
    Node(3, 10.0, 10.0, 0.0)
    Node(4, 0.0, 10.0, 0.0)
    Node(5, 0.0, 0.0, 10.0)
    Node(6, 0.0, 10.0, 10.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Thickness(1, '1', 1, 0.05)
    Surface(1, '1-4', 1)

    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', NodalSupportType.HINGED)
    NodalSupport(3, '3', NodalSupportType.HINGED)
    NodalSupport(4, '4', NodalSupportType.HINGED)

    StaticAnalysisSettings(1, 'LINEAR', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    FreeLoad.ConcentratedLoad(FreeLoad, 1, 1, load_parameter= [5000, 4, 2])

    Model.clientModel.service.finish_modification()

    free_load = Model.clientModel.service.get_free_concentrated_load(1, 1)

    assert free_load.load_location_x == 4
    assert free_load.magnitude == 5000

def test_free_line_load():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10.0, 0.0, 0.0)
    Node(3, 10.0, 10.0, 0.0)
    Node(4, 0.0, 10.0, 0.0)
    Node(5, 0.0, 0.0, 10.0)
    Node(6, 0.0, 10.0, 10.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Thickness(1, '1', 1, 0.05)
    Surface(1, '1-4', 1)

    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', NodalSupportType.HINGED)
    NodalSupport(3, '3', NodalSupportType.HINGED)
    NodalSupport(4, '4', NodalSupportType.HINGED)

    StaticAnalysisSettings(1, 'LINEAR', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    FreeLoad.LineLoad(FreeLoad, 1, 1, '1',
                        FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                        FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                        FreeLineLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                        [5000, 2, 2, 4, 4])

    Model.clientModel.service.finish_modification()

    free_load = Model.clientModel.service.get_free_line_load(1, 1)

    assert free_load.load_location_first_x == 2
    assert free_load.magnitude_uniform == 5000

def test_free_rectangular_load():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10.0, 0.0, 0.0)
    Node(3, 10.0, 10.0, 0.0)
    Node(4, 0.0, 10.0, 0.0)
    Node(5, 0.0, 0.0, 10.0)
    Node(6, 0.0, 10.0, 10.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Thickness(1, '1', 1, 0.05)
    Surface(1, '1-4', 1)

    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', NodalSupportType.HINGED)
    NodalSupport(3, '3', NodalSupportType.HINGED)
    NodalSupport(4, '4', NodalSupportType.HINGED)

    StaticAnalysisSettings(1, 'LINEAR', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    FreeLoad.RectangularLoad(FreeLoad, 1, 1, '1',
                             FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                             FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                             FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                             [5000],
                             FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CORNER_POINTS,
                             [1, 8, 3, 10, 0])

    Model.clientModel.service.finish_modification()

    free_load = Model.clientModel.service.get_free_rectangular_load(1, 1)

    assert free_load.load_location_center_x == 2
    assert free_load.magnitude_uniform == 5000

def test_free_circular_load():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10.0, 0.0, 0.0)
    Node(3, 10.0, 10.0, 0.0)
    Node(4, 0.0, 10.0, 0.0)
    Node(5, 0.0, 0.0, 10.0)
    Node(6, 0.0, 10.0, 10.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Thickness(1, '1', 1, 0.05)
    Surface(1, '1-4', 1)

    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', NodalSupportType.HINGED)
    NodalSupport(3, '3', NodalSupportType.HINGED)
    NodalSupport(4, '4', NodalSupportType.HINGED)

    StaticAnalysisSettings(1, 'LINEAR', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    FreeLoad.CircularLoad(FreeLoad, 1, 1, '1',
                             FreeCircularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                             FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                             FreeCircularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                             [10000, 7.5, 5, 2])

    Model.clientModel.service.finish_modification()

    free_load = Model.clientModel.service.get_free_circular_load(1, 1)

    assert free_load.load_location_x == 7.5
    assert free_load.magnitude_uniform == 10000

def test_free_polygon_load():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10.0, 0.0, 0.0)
    Node(3, 10.0, 10.0, 0.0)
    Node(4, 0.0, 10.0, 0.0)
    Node(5, 0.0, 0.0, 10.0)
    Node(6, 0.0, 10.0, 10.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Thickness(1, '1', 1, 0.05)
    Surface(1, '1-4', 1)

    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', NodalSupportType.HINGED)
    NodalSupport(3, '3', NodalSupportType.HINGED)
    NodalSupport(4, '4', NodalSupportType.HINGED)

    StaticAnalysisSettings(1, 'LINEAR', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'DEAD')

    FreeLoad.PolygonLoad(FreeLoad, 1, 1, '1',
                         FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                         FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                         FreePolygonLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                         [[1, 0], [0, 2], [2, 2]],
                         [5000])

    Model.clientModel.service.finish_modification()

    free_load = Model.clientModel.service.get_free_polygon_load(1, 1)

    assert free_load.no == 1
    assert free_load.magnitude_uniform == 5000
