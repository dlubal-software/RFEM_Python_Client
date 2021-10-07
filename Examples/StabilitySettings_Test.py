from os import name
import sys
sys.path.append(".")

# Import der Bibliotheken
from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.LoadCasesAndCombinations.stabilityAnalysisSettings import *

if __name__ == '__main__':
	
	clientModel.service.begin_modification('new')

	# Testing Functions with Default Parameters
	StabilityAnalysisSettings(no= 1)

	StabilityAnalysisSettings.EigenvalueMethod(StabilityAnalysisSettings, no= 2)

	StabilityAnalysisSettings.IncrementalyMethodWithEigenvalue(StabilityAnalysisSettings, no= 3)

	StabilityAnalysisSettings.IncrementalyMethodWithoutEigenvalue(StabilityAnalysisSettings, no= 4)

	# Testing Functions with User-Defiend Parameters

	StabilityAnalysisSettings(no= 5,
							  name= 'Default Test',
							  comment= 'Test Comment')

	StabilityAnalysisSettings.EigenvalueMethod(StabilityAnalysisSettings, no= 6,
											name= 'Eigenvalue Method Test',
											number_of_lowest_eigenvalues= 5,
											considered_favored_effect= False,
											critical_load_factor= 10,
											minimum_initial_strain= 0.000025,
											local_torsional_rotations= 0.2,
											eigenvalue_method= StabilityAnalysisSettingsEigenvalueMethod.EIGENVALUE_METHOD_ROOTS_OF_CHARACTERISTIC_POLYNOMIAL,
											matrix_type= StabilityAnalysisSettingsMatrixType.MATRIX_TYPE_UNIT,
											comment= 'Test Comment')

	StabilityAnalysisSettings.IncrementalyMethodWithEigenvalue(StabilityAnalysisSettings, no= 7,
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

	StabilityAnalysisSettings.IncrementalyMethodWithoutEigenvalue(StabilityAnalysisSettings, no= 8,
											name= 'Incrementaly Method with Eigenvalue Test',
											minimum_initial_strain= 0,
											local_torsional_rotations= 0.2,
											incrementally_increasing_loading= [1, 0.25, 5, 125],
											save_results_of_all_increments= False,
											comment= 'Test Comment')

	clientModel.service.finish_modification()