import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import *
from RFEM.initModel import Model, client
from RFEM.Calculate.meshSettings import MeshSettings
from RFEM.Calculate.optimizationSettings import OptimizationSettings
from UnitTests.test_solids import test_solids_and_solid_sets

if Model.clientModel is None:
    Model()

# These tests needs to be executed last
def test_mesh_settings():

    common = MeshSettings.ComonMeshConfig
    common['general_target_length_of_fe'] = 0.4321
    common['members_number_of_divisions_for_special_types'] = 12
    common['surfaces_shape_of_finite_elements'] = SurfacesShapeOfFiniteElements.E_SHAPE_OF_FINITE_ELEMENTS_FOR_SURFACES__TRIANGLES_ONLY.name
    surf = MeshSettings.SurfacesMeshQualityConfig
    surf['QualityCriteriaConfig']['quality_criterion_check_aspect_ratio_warning'] = 22
    solid = dict(MeshSettings.SolidsMeshQualityConfig)
    solid['QualityCriteriaConfig']['quality_criterion_parallel_deviations_warning'] = 1.7
    wind = dict(MeshSettings.WindSimulationMeshConfig)

    mesh = MeshSettings(common, surf, solid, wind)

    control_mesh = mesh.get_mesh_settings()
    assert control_mesh['general_target_length_of_fe'] == 0.4321
    assert control_mesh['members_number_of_divisions_for_special_types'] == 12
    assert control_mesh['surfaces_shape_of_finite_elements'] == SurfacesShapeOfFiniteElements.E_SHAPE_OF_FINITE_ELEMENTS_FOR_SURFACES__TRIANGLES_ONLY.name
    assert control_mesh['SurfacesMeshQualityConfig']['QualityCriteriaConfig']['quality_criterion_check_aspect_ratio_warning'] == 22
    assert control_mesh['SolidsMeshQualityConfig']['QualityCriteriaConfig']['quality_criterion_parallel_deviations_warning'] == 1.7

    control_mesh['general_maximum_distance_between_node_and_line'] = 0.003
    mesh.set_mesh_settings(control_mesh)
    control_mesh = mesh.get_mesh_settings()
    assert control_mesh['general_maximum_distance_between_node_and_line'] == 0.003

    test_solids_and_solid_sets()

    info = MeshSettings()
    count = info.get_model_info()
    assert count['property_node_count'] == 28

def test_optimization_settings():

    OptimizationSettings(True, 11, OptimizeOnType.E_OPTIMIZE_ON_TYPE_MIN_COST,
                         Optimizer.E_OPTIMIZER_TYPE_PERCENTS_OF_RANDOM_MUTATIONS,
                         0.3)
    opt_sett = OptimizationSettings.get_optimization_settings()
    assert opt_sett.general_optimization_active
    assert opt_sett.general_keep_best_number_model_mutations == 11
    assert opt_sett.general_optimize_on == OptimizeOnType.E_OPTIMIZE_ON_TYPE_MIN_COST.name
    assert opt_sett.general_optimizer == Optimizer.E_OPTIMIZER_TYPE_PERCENTS_OF_RANDOM_MUTATIONS.name
    assert opt_sett.general_number_random_mutations == 0.3
