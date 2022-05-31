import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import AddOn, StabilityAnalysisSettingsEigenvalueMethod, StabilityAnalysisSettingsMatrixType, StabilityAnalysisSettingsStoppingOfLoadIncreasingResult
from RFEM.initModel import Model, SetAddonStatus
from RFEM.LoadCasesAndCombinations.stabilityAnalysisSettings import StabilityAnalysisSettings

if Model.clientModel is None:
    Model()

def test_stability_analysis_settings_init():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, True)
    StabilityAnalysisSettings()
    Model.clientModel.service.finish_modification()

    stability_analysis_settings = Model.clientModel.service.get_stability_analysis_settings(1)

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

    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, False)

def test_stability_analysis_settings_eigenvalue_method():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, True)

    StabilityAnalysisSettings.EigenvalueMethod(no= 1,
                                            name= 'Eigenvalue Method Test',
                                            number_of_lowest_eigenvalues= 5,
                                            considered_favored_effect= False,
                                            critical_load_factor= 10,
                                            minimum_initial_strain= 0.000025,
                                            local_torsional_rotations= 0.2,
                                            eigenvalue_method= StabilityAnalysisSettingsEigenvalueMethod.EIGENVALUE_METHOD_ROOTS_OF_CHARACTERISTIC_POLYNOMIAL,
                                            matrix_type= StabilityAnalysisSettingsMatrixType.MATRIX_TYPE_UNIT,
                                            comment= 'Test Comment')

    Model.clientModel.service.finish_modification()

    stability_analysis_settings = Model.clientModel.service.get_stability_analysis_settings(1)

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

    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, False)

def test_stability_analysis_settings_incrementaly_method_with_eigenvalue():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, True)

    StabilityAnalysisSettings.IncrementalyMethodWithEigenvalue(no= 1,
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

    Model.clientModel.service.finish_modification()

    stability_analysis_settings = Model.clientModel.service.get_stability_analysis_settings(1)

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

    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, False)

def test_stability_analysis_settings_incrementaly_method_without_eigenvalue():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, True)

    StabilityAnalysisSettings.IncrementalyMethodWithoutEigenvalue(no= 1,
                                            name= 'Incrementaly Method with Eigenvalue Test',
                                            minimum_initial_strain= 0,
                                            local_torsional_rotations= 0.2,
                                            incrementally_increasing_loading= [1, 0.25, 5, 125],
                                            save_results_of_all_increments= False,
                                            comment= 'Test Comment')

    Model.clientModel.service.finish_modification()

    stability_analysis_settings = Model.clientModel.service.get_stability_analysis_settings(1)

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

    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, False)
