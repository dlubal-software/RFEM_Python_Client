import sys
import pytest
sys.path.append(".")
from RFEM.enums import *
from RFEM.initModel import *
from RFEM.LoadCasesAndCombinations.stabilityAnalysisSettings import StabilityAnalysisSettings

@pytest.mark.skip("all tests still WIP")
def test_stability_analysis_settings_init():

	clientModel.service.reset()
	clientModel.service.begin_modification()

	StabilityAnalysisSettings()

	clientModel.service.finish_modification()

	stability_analysis_settings = clientModel.service.get_stability_analysis_settings(1)

	assert stability_analysis_settings.analysis_type == 'EIGENVALUE_METHOD'
	assert stability_analysis_settings.activate_minimum_initial_prestress == True
	assert stability_analysis_settings.eigenvalue_method == 'EIGENVALUE_METHOD_LANCZOS'
	assert stability_analysis_settings.calculate_without_loading_for_instability == False
	assert stability_analysis_settings.considered_favored_effect == True
	assert stability_analysis_settings.display_local_torsional_rotations == False
	assert stability_analysis_settings.find_eigenvectors_beyond_critical_load_factor == False
	assert stability_analysis_settings.matrix_type == 'MATRIX_TYPE_STANDARD'
	assert stability_analysis_settings.minimum_initial_strain == 1e-05
	assert stability_analysis_settings.number_of_lowest_eigenvalues == 4

@pytest.mark.skip("all tests still WIP")
def test_stability_analysis_settings_eigenvalue_method():

	clientModel.service.reset()
	clientModel.service.begin_modification()

	StabilityAnalysisSettings.EigenvalueMethod(StabilityAnalysisSettings, no= 1,
											name= 'Eigenvalue Method Test',
											number_of_lowest_eigenvalues= 5,
											considered_favored_effect= False,
											critical_load_factor= 10,
											minimum_initial_strain= 0.000025,
											local_torsional_rotations= 0.2,
											eigenvalue_method= StabilityAnalysisSettingsEigenvalueMethod.EIGENVALUE_METHOD_ROOTS_OF_CHARACTERISTIC_POLYNOMIAL,
											matrix_type= StabilityAnalysisSettingsMatrixType.MATRIX_TYPE_UNIT,
											comment= 'Test Comment')

	clientModel.service.finish_modification()

	stability_analysis_settings = clientModel.service.get_stability_analysis_settings(1)

	assert stability_analysis_settings.analysis_type == 'EIGENVALUE_METHOD'
	assert stability_analysis_settings.activate_minimum_initial_prestress == True
	assert stability_analysis_settings.eigenvalue_method == 'EIGENVALUE_METHOD_ROOTS_OF_CHARACTERISTIC_POLYNOMIAL'
	assert stability_analysis_settings.calculate_without_loading_for_instability == False
	assert stability_analysis_settings.considered_favored_effect == False
	assert stability_analysis_settings.display_local_torsional_rotations == True
	assert stability_analysis_settings.find_eigenvectors_beyond_critical_load_factor == True
	assert stability_analysis_settings.critical_load_factor == 10
	assert stability_analysis_settings.matrix_type == 'MATRIX_TYPE_UNIT'
	assert stability_analysis_settings.minimum_initial_strain == 2.5e-05
	assert stability_analysis_settings.number_of_lowest_eigenvalues == 5

@pytest.mark.skip("all tests still WIP")
def test_stability_analysis_settings_incrementaly_method_with_eigenvalue():

	clientModel.service.reset()
	clientModel.service.begin_modification()

	StabilityAnalysisSettings.IncrementalyMethodWithEigenvalue(StabilityAnalysisSettings, no= 1,
											name= 'Incrementaly Method with Eigenvalue Test',
											number_of_lowest_eigenvalues= 5,
											considered_favored_effect= True,
											critical_load_factor= 11,
											minimum_initial_strain= None,
											local_torsional_rotations= None,
											incrementally_increasing_loading= [2, 0.2, 12, 200],
											stopping_of_load_increasing= [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_DISPLACEMENT_U, 0.1, 0],
											save_results_of_all_increments= True,
											eigenvalue_method= StabilityAnalysisSettingsEigenvalueMethod.EIGENVALUE_METHOD_LANCZOS,
											matrix_type= StabilityAnalysisSettingsMatrixType.MATRIX_TYPE_STANDARD,
											comment= 'Test Comment')

	clientModel.service.finish_modification()

	stability_analysis_settings = clientModel.service.get_stability_analysis_settings(1)

	assert stability_analysis_settings.analysis_type == 'INCREMENTALY_METHOD_WITH_EIGENVALUE'
	assert stability_analysis_settings.activate_minimum_initial_prestress == False
	assert stability_analysis_settings.activate_stopping_of_load_increasing == True
	assert stability_analysis_settings.eigenvalue_method == 'EIGENVALUE_METHOD_LANCZOS'
	assert stability_analysis_settings.calculate_without_loading_for_instability == False
	assert stability_analysis_settings.considered_favored_effect == True
	assert stability_analysis_settings.display_local_torsional_rotations == False
	assert stability_analysis_settings.find_eigenvectors_beyond_critical_load_factor == True
	assert stability_analysis_settings.critical_load_factor == 11
	assert stability_analysis_settings.initial_load_factor == 2
	assert stability_analysis_settings.load_factor_increment == 0.2
	assert stability_analysis_settings.matrix_type == 'MATRIX_TYPE_STANDARD'
	assert stability_analysis_settings.maximum_number_of_load_increments == 200
	assert stability_analysis_settings.number_of_lowest_eigenvalues == 5
	assert stability_analysis_settings.refinement_of_the_last_load_increment == 12
	assert stability_analysis_settings.save_results_of_all_increments == True
	assert stability_analysis_settings.stopping_of_load_increasing_limit_node == 0
	assert stability_analysis_settings.stopping_of_load_increasing_limit_result_displacement == 0.1
	assert stability_analysis_settings.stopping_of_load_increasing_result == 'RESULT_TYPE_DISPLACEMENT_U'

@pytest.mark.skip("all tests still WIP")
def test_stability_analysis_settings_incrementaly_method_without_eigenvalue():

	clientModel.service.reset()
	clientModel.service.begin_modification()

	StabilityAnalysisSettings.IncrementalyMethodWithoutEigenvalue(StabilityAnalysisSettings, no= 1,
											name= 'Incrementaly Method with Eigenvalue Test',
											minimum_initial_strain= 0,
											local_torsional_rotations= 0.2,
											incrementally_increasing_loading= [1, 0.25, 5, 125],
											save_results_of_all_increments= False,
											comment= 'Test Comment')

	clientModel.service.finish_modification()

	stability_analysis_settings = clientModel.service.get_stability_analysis_settings(1)

	assert stability_analysis_settings.analysis_type == 'INCREMENTALY_METHOD_WITHOUT_EIGENVALUE'
	assert stability_analysis_settings.activate_minimum_initial_prestress == False
	assert stability_analysis_settings.activate_stopping_of_load_increasing == False
	assert stability_analysis_settings.display_local_torsional_rotations == True
	assert stability_analysis_settings.local_torsional_rotations == 0.2
	assert stability_analysis_settings.initial_load_factor == 1
	assert stability_analysis_settings.load_factor_increment == 0.25
	assert stability_analysis_settings.maximum_number_of_load_increments == 125
	assert stability_analysis_settings.refinement_of_the_last_load_increment == 5
	assert stability_analysis_settings.save_results_of_all_increments == False