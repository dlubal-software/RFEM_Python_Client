from RFEM.initModel import *
from RFEM.enums import StabilityAnalysisSettingsAnalysisType
from RFEM.enums import StabilityAnalysisSettingsEigenvalueMethod
from RFEM.enums import StabilityAnalysisSettingsMatrixType
from RFEM.enums import StabilityAnalysisSettingsStoppingOfLoadIncreasingResult

class StabilityAnalysisSettings():
    def __init__(self,
                 no: int = 1,
                 name: str = None,
                 comment: str = '',
                 params: dict = {}):
        '''
        Creates default stability analysis settings with no further options. 
        Stability analysis type is Eigenvalue by default.
        Eigenvalue method is Lanczos by default.
        Matrix type is Standard by default.
        '''

        # Client model | Stability Analysis Settings
        clientObject = clientModel.factory.create('ns0:stability_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Stability Analysis Settings No.
        clientObject.no = no

        # Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Stability Analysis Type
        clientObject.analysis_type = StabilityAnalysisSettingsAnalysisType.EIGENVALUE_METHOD.name

        # Number of Lowest Eigenvalues
        clientObject.number_of_lowest_eigenvalues = 4

        # Eigenvalue Method
        clientObject.eigenvalue_method = StabilityAnalysisSettingsEigenvalueMethod.EIGENVALUE_METHOD_LANCZOS.name

        # Matrix Type 
        clientObject.matrix_type = StabilityAnalysisSettingsMatrixType.MATRIX_TYPE_STANDARD.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Stability Analysis Settings to client model
        clientModel.service.set_stability_analysis_settings(clientObject)

    def EigenvalueMethod(self,
                 no: int = 1,
                 name: str = None,
                 number_of_lowest_eigenvalues: int = 4,
                 considered_favored_effect: bool = True,
                 critical_load_factor = None,
                 minimum_initial_strain = 1e-05,
                 local_torsional_rotations = None,
                 eigenvalue_method = StabilityAnalysisSettingsEigenvalueMethod.EIGENVALUE_METHOD_LANCZOS,
                 matrix_type = StabilityAnalysisSettingsMatrixType.MATRIX_TYPE_STANDARD,
                 comment: str = '',
                 params: dict = {}):
        '''
        Args:
            no (int): 
            name (str, optional): Stability Analysis Name
            number_of_lowest_eigenvalues (int): Number of Lowest Eigenvalues
            considered_favored_effect (bool): Considered Favored Effect
            critical_load_factor (int, optional):
                For find_eigenvectors_beyond_critical_load_factor == False:
                    critical_load_factor = None
                For find_eigenvectors_beyond_critical_load_factor == True:
                    critical_load_factor = int
            minimum_initial_strain (optional):
                For minimum initial strain application:
                    minimum_initial_strain != 0 or minimum_initial_strain != None
                For no minimum initial strain application:
                    minimum_initial_strain == 0 or minimum_initial_strain == None
            local_torsional_rotations (optional):
                For no local torsional rotations display:
                    local_torsional_rotations = None
                For local torsional rotations display:
                    local_torsional_rotations = double
            eigenvalue_method (enum): Eigenvalue Method Enumeration
            matrix_type (enum): Matrix Type Enumeration
            comment (str, optional):
            params (dict, optional):
        '''
        # Client model | Stability Analysis Settings
        clientObject = clientModel.factory.create('ns0:stability_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Stability Analysis Settings No.
        clientObject.no = no

        # Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Stability Analysis Type
        clientObject.analysis_type = StabilityAnalysisSettingsAnalysisType.EIGENVALUE_METHOD.name

        # Number of Lowest Eigenvalues
        clientObject.number_of_lowest_eigenvalues = number_of_lowest_eigenvalues

        # Considered Favored Effect
        clientObject.considered_favored_effect = considered_favored_effect

        # Finding Eigenvectors Beyond Critical Load Factor
        if critical_load_factor != None:
            clientObject.find_eigenvectors_beyond_critical_load_factor = True
            clientObject.critical_load_factor = critical_load_factor
        
        # Minimum Initial Strain
        if minimum_initial_strain != None:
            clientObject.activate_minimum_initial_prestress = True
            clientObject.minimum_initial_strain = minimum_initial_strain
        elif minimum_initial_strain == None or minimum_initial_strain == 0:
            clientObject.activate_minimum_initial_prestress = False
        
        # Local Torsional Relations
        if local_torsional_rotations != None:
            clientObject.display_local_torsional_rotations = True
            clientObject.local_torsional_rotations

        # Eigenvalue Method
        clientObject.eigenvalue_method = eigenvalue_method.name

        # Matrix Type
        clientObject.matrix_type = matrix_type.name
        
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Stability Analysis Settings to client model
        clientModel.service.set_stability_analysis_settings(clientObject)
