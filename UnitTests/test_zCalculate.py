import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import SurfacesShapeOfFiniteElements, OptimizerType, OptimizationTargetValueType, AddOn,NodalSupportType, LoadDirectionType, ActionCategoryType, ObjectTypes
from RFEM.initModel import Model, client, SetAddonStatus,Calculate_all, CalculateSelectedCases
from RFEM.Calculate.meshSettings import GetMeshSettings, MeshSettings, GetModelInfo
from RFEM.Calculate.optimizationSettings import OptimizationSettings
from UnitTests.test_solids import test_solids_and_solid_sets
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.Loads.nodalLoad import NodalLoad

if Model.clientModel is None:
    Model()

def createmodel():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Section(1, 'IPE 200')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5.0, 0.0, 0.0)

    Member(1, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)

    LoadCasesAndCombinations(params = {"current_standard_for_combination_wizard": 6208})
    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
    LoadCase.StaticAnalysis(1, 'SW', True, 1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_G, [True, 0, 0, 1])
    LoadCase.StaticAnalysis(2, 'SDL', True,  1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_IMPOSED_GQ, [False])

    NodalLoad(1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 150*1000)
    Model.clientModel.service.finish_modification()

def test_calculate_specific():

    createmodel()
    messages = CalculateSelectedCases([1])

    assert not messages
    assert  Model.clientModel.service.has_results(ObjectTypes.E_OBJECT_TYPE_LOAD_CASE.name, 1)
    assert not Model.clientModel.service.has_results(ObjectTypes.E_OBJECT_TYPE_LOAD_CASE.name, 2)

def test_calculate_all():

    createmodel()
    messages = Calculate_all()

    assert not messages
    assert Model.clientModel.service.has_results(ObjectTypes.E_OBJECT_TYPE_LOAD_CASE.name, 1)
    assert Model.clientModel.service.has_results(ObjectTypes.E_OBJECT_TYPE_LOAD_CASE.name, 2)

# CAUTION:
# These tests needs to be executed last because they change global settings.
# At the end of the script the model is closed.
def test_mesh_settings():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    SetAddonStatus(Model.clientModel, AddOn.wind_simulation_active, False)

    common = MeshSettings.ComonMeshConfig
    common['general_target_length_of_fe'] = 0.4321
    common['members_number_of_divisions_for_special_types'] = 12
    common['surfaces_shape_of_finite_elements'] = SurfacesShapeOfFiniteElements.E_SHAPE_OF_FINITE_ELEMENTS_FOR_SURFACES__TRIANGLES_ONLY.name
    surf = MeshSettings.SurfacesMeshQualityConfig
    surf['QualityCriteriaConfigForSurfaces']['quality_criterion_check_aspect_ratio_warning'] = 22
    solid = dict(MeshSettings.SolidsMeshQualityConfig)
    solid['QualityCriteriaConfigForSolids']['quality_criterion_parallel_deviations_warning'] = 1.7
    wind = dict(MeshSettings.WindSimulationMeshConfig)

    MeshSettings(common, surf, solid, wind)

    control_mesh = GetMeshSettings()
    assert control_mesh['general_target_length_of_fe'] == 0.4321
    assert control_mesh['members_number_of_divisions_for_special_types'] == 12
    assert control_mesh['surfaces_shape_of_finite_elements'] == SurfacesShapeOfFiniteElements.E_SHAPE_OF_FINITE_ELEMENTS_FOR_SURFACES__TRIANGLES_ONLY.name
    assert control_mesh['SurfacesMeshQualityConfig']['QualityCriteriaConfigForSurfaces']['quality_criterion_check_aspect_ratio_warning'] == 22
    assert control_mesh['SolidsMeshQualityConfig']['QualityCriteriaConfigForSolids']['quality_criterion_parallel_deviations_warning'] == 1.7

    control_mesh['general_maximum_distance_between_node_and_line'] = 0.003
    MeshSettings.set_mesh_settings(control_mesh)
    control_mesh = GetMeshSettings()
    assert control_mesh['general_maximum_distance_between_node_and_line'] == 0.003

    Model.clientModel.service.finish_modification()

    test_solids_and_solid_sets()

    count = GetModelInfo()
    assert count['property_node_count'] == 28

def test_optimization_settings():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.cost_estimation_active)
    OptimizationSettings()

    Model.clientModel.service.finish_modification()

    opt_sett = OptimizationSettings.GetOptimizationSettings(1)

    assert opt_sett.active
    assert opt_sett.number_of_mutations_to_keep == 20
    assert opt_sett.target_value_type == OptimizationTargetValueType.MIN_TOTAL_WEIGHT.name

    # Testing model is closed at the end of the testing session to enable easier and cleaned restart of the unit tests.
    client.service.close_model(0, False)
