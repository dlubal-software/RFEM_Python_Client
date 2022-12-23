from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import StabilityAnalysisSettingsAnalysisType
from RFEM.enums import StabilityAnalysisSettingsEigenvalueMethod
from RFEM.enums import StabilityAnalysisSettingsMatrixType

class StabilityAnalysisSettings():

    def __init__(self,
                 no: int = 1,
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        '''
        Args:
            no (int): Stability Analysis Setting Tag
            name (str): Stability Analysis Setting Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Stability Analysis Settings
        clientObject = model.clientModel.factory.create('ns0:stability_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Stability Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Stability Analysis Settings to client model
        model.clientModel.service.set_stability_analysis_settings(clientObject)

    @staticmethod
    def EigenvalueMethod(
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
                 params: dict = None,
                 model = Model):
        '''
        Args:
            no (int): Stability Analysis Setting Tag
            name (str, optional): Stability Analysis Setting Name
            number_of_lowest_eigenvalues (int): Number of Lowest Eigenvalues
            considered_favored_effect (bool): Considered Favored Effect
            critical_load_factor (int, optional): Critical Load Factor
                for find_eigenvectors_beyond_critical_load_factor == False:
                    critical_load_factor = None
                for find_eigenvectors_beyond_critical_load_factor == True:
                    critical_load_factor = int
            minimum_initial_strain (optional): Minimum Initial Strain
                for minimum initial strain application:
                    minimum_initial_strain != 0 or minimum_initial_strain
                for no minimum initial strain application:
                    minimum_initial_strain == 0 or minimum_initial_strain is None
            local_torsional_rotations (optional): Local Torsional Rotations
                for no local torsional rotations display:
                    local_torsional_rotations = None
                for local torsional rotations display:
                    local_torsional_rotations = double
            eigenvalue_method (enum): StabilityAnalysisSettings Eigenvalue Method Enumeration
            matrix_type (enum): StabilityAnalysisSettings Matrix Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Stability Analysis Settings
        clientObject = model.clientModel.factory.create('ns0:stability_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Stability Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Stability Analysis Type
        clientObject.analysis_type = StabilityAnalysisSettingsAnalysisType.EIGENVALUE_METHOD.name

        # Number of Lowest Eigenvalues
        clientObject.number_of_lowest_eigenvalues = number_of_lowest_eigenvalues

        # Considered Favored Effect
        clientObject.considered_favored_effect = considered_favored_effect

        # Finding Eigenvectors Beyond Critical Load Factor
        if critical_load_factor:
            clientObject.find_eigenvectors_beyond_critical_load_factor = True
            clientObject.critical_load_factor = critical_load_factor

        # Minimum Initial Strain
        if minimum_initial_strain in (None, 0):
            clientObject.activate_minimum_initial_prestress = False
        else:
            clientObject.activate_minimum_initial_prestress = True
            clientObject.minimum_initial_strain = minimum_initial_strain

        # Local Torsional Relations
        if local_torsional_rotations:
            clientObject.display_local_torsional_rotations = True

        # Eigenvalue Method
        clientObject.eigenvalue_method = eigenvalue_method.name

        # Matrix Type
        clientObject.matrix_type = matrix_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Stability Analysis Settings to client model
        model.clientModel.service.set_stability_analysis_settings(clientObject)

    @staticmethod
    def IncrementalyMethodWithEigenvalue(
                 no: int = 1,
                 name: str = None,
                 number_of_lowest_eigenvalues: int = 4,
                 considered_favored_effect: bool = True,
                 critical_load_factor = None,
                 minimum_initial_strain = 1e-05,
                 local_torsional_rotations = None,
                 incrementally_increasing_loading = [1.0, 0.1, 10, 100],
                 stopping_of_load_increasing = None,
                 save_results_of_all_increments: bool = False,
                 eigenvalue_method = StabilityAnalysisSettingsEigenvalueMethod.EIGENVALUE_METHOD_LANCZOS,
                 matrix_type = StabilityAnalysisSettingsMatrixType.MATRIX_TYPE_STANDARD,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        '''
        Args:
            no (int): Stability Analysis Setting Tag
            name (str, optional): Stability Analysis Setting Name
            number_of_lowest_eigenvalues (int): Number of Lowest Eigenvalues
            considered_favored_effect (bool): Considered Favored Effect
            critical_load_factor (int, optional): Critical Load Factor
                for find_eigenvectors_beyond_critical_load_factor == False:
                    critical_load_factor = None
                for find_eigenvectors_beyond_critical_load_factor == True:
                    critical_load_factor = int
            minimum_initial_strain (optional): Minimum Initial Strain
                for minimum initial strain application:
                    minimum_initial_strain != 0 or minimum_initial_strain
                for no minimum initial strain application:
                    minimum_initial_strain is None
            local_torsional_rotations (optional): Local Torsional Rotations
                for no local torsional rotations display:
                    local_torsional_rotations = None
                for local torsional rotations display:
                    local_torsional_rotations = double
            incrementally_increasing_loading (list): Incrementally Increasing Loading
                incrementally_increasing_loading = [initial_load_factor, load_factor_increment, refinement_of_the_last_load_increment, maximum_number_of_load_increments]
            stopping_of_load_increasing (list, optional): Stopping of Load Increasing
                for stopping of load increasing deactivated:
                    stopping_of_load_increasing = None
                for result u:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_DISPLACEMENT_U, limit_result_displacement, limit_node]
                for result uX:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_DISPLACEMENT_U_X, limit_result_displacement, limit_node]
                for result uY:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_DISPLACEMENT_U_Y, limit_result_displacement, limit_node]
                for result uZ:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_DISPLACEMENT_U_Z, limit_result_displacement, limit_node]
                for result phi:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_ROTATION_PHI, limit_result_rotation, limit_node]
                for result phiX:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_ROTATION_PHI_X, limit_result_rotation, limit_node]
                for result phiY:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_ROTATION_PHI_Y, limit_result_rotation, limit_node]
                for result phiZ:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_ROTATION_PHI_Z, limit_result_rotation, limit_node]
            save_results_of_all_increments (bool, optional): Save Results of All Increments
            eigenvalue_method (enum): StabilityAnalysisSettings Eigenvalue Method Enumeration
            matrix_type (enum): StabilityAnalysisSettings Matrix Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Stability Analysis Settings
        clientObject = model.clientModel.factory.create('ns0:stability_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Stability Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Stability Analysis Type
        clientObject.analysis_type = StabilityAnalysisSettingsAnalysisType.INCREMENTALY_METHOD_WITH_EIGENVALUE.name

        # Number of Lowest Eigenvalues
        clientObject.number_of_lowest_eigenvalues = number_of_lowest_eigenvalues

        # Considered Favored Effect
        clientObject.considered_favored_effect = considered_favored_effect

        # Finding Eigenvectors Beyond Critical Load Factor
        if critical_load_factor:
            clientObject.find_eigenvectors_beyond_critical_load_factor = True
            clientObject.critical_load_factor = critical_load_factor

        # Minimum Initial Strain
        if minimum_initial_strain in (None, 0):
            clientObject.activate_minimum_initial_prestress = False
        else:
            clientObject.activate_minimum_initial_prestress = True
            clientObject.minimum_initial_strain = minimum_initial_strain

        # Local Torsional Relations
        if local_torsional_rotations:
            clientObject.display_local_torsional_rotations = True

        # Increase Loading
        if len(incrementally_increasing_loading) != 4:
            raise ValueError('WARNING: The incrementally increasing loading parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
        clientObject.initial_load_factor = incrementally_increasing_loading[0]
        clientObject.load_factor_increment = incrementally_increasing_loading[1]
        clientObject.refinement_of_the_last_load_increment = incrementally_increasing_loading[2]
        clientObject.maximum_number_of_load_increments = incrementally_increasing_loading[3]

        # Stopping of Load-Increasing
        if stopping_of_load_increasing:
            if len(stopping_of_load_increasing) != 3:
                raise ValueError('WARNING: For active stopping of load-increasing, the stopping of load increasing parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            clientObject.activate_stopping_of_load_increasing = True
            clientObject.stopping_of_load_increasing_result = stopping_of_load_increasing[0].name
            if stopping_of_load_increasing[0].name == 'RESULT_TYPE_DISPLACEMENT_U' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_DISPLACEMENT_U_X' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_DISPLACEMENT_U_Y' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_DISPLACEMENT_U_Z':
                clientObject.stopping_of_load_increasing_limit_result_displacement = stopping_of_load_increasing[1]
            elif stopping_of_load_increasing[0].name == 'RESULT_TYPE_ROTATION_PHI' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_ROTATION_PHI_X' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_ROTATION_PHI_Y' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_ROTATION_PHI_Z':
                clientObject.stopping_of_load_increasing_limit_result_rotation = stopping_of_load_increasing[1]
            clientObject.stopping_of_load_increasing_limit_node = stopping_of_load_increasing[2]

        # Save Results of All Increments
        clientObject.save_results_of_all_increments = save_results_of_all_increments

        # Eigenvalue Method
        clientObject.eigenvalue_method = eigenvalue_method.name

        # Matrix Type
        clientObject.matrix_type = matrix_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Stability Analysis Settings to client model
        model.clientModel.service.set_stability_analysis_settings(clientObject)

    @staticmethod
    def IncrementalyMethodWithoutEigenvalue(
                 no: int = 1,
                 name: str = None,
                 minimum_initial_strain = 1e-05,
                 local_torsional_rotations = None,
                 incrementally_increasing_loading = [1.0, 0.1, 10, 100],
                 stopping_of_load_increasing = None,
                 save_results_of_all_increments: bool = False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        '''
        Args:
            no (int): Stability Analysis Setting Tag
            name (str, optional): Stability Analysis Setting Name
            minimum_initial_strain (optional): Minimum Initial Strain
                for minimum initial strain application:
                    minimum_initial_strain != 0 or minimum_initial_strain
                for no minimum initial strain application:
                    minimum_initial_strain == 0 or minimum_initial_strain is None
            local_torsional_rotations (optional): Local Torsional Rotations
                for no local torsional rotations display:
                    local_torsional_rotations = None
                for local torsional rotations display:
                    local_torsional_rotations = double
            incrementally_increasing_loading (list): Incrementally Increasing Loading
                incrementally_increasing_loading = [initial_load_factor, load_factor_increment, refinement_of_the_last_load_increment, maximum_number_of_load_increments]
            stopping_of_load_increasing (list, optional): Stopping of Load Increasing
                for stopping of load increasing deactivated:
                    stopping_of_load_increasing = None
                for result u:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_DISPLACEMENT_U, limit_result_displacement, limit_node]
                for result uX:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_DISPLACEMENT_U_X, limit_result_displacement, limit_node]
                for result uY:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_DISPLACEMENT_U_Y, limit_result_displacement, limit_node]
                for result uZ:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_DISPLACEMENT_U_Z, limit_result_displacement, limit_node]
                for result phi:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_ROTATION_PHI, limit_result_rotation, limit_node]
                for result phiX:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_ROTATION_PHI_X, limit_result_rotation, limit_node]
                for result phiY:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_ROTATION_PHI_Y, limit_result_rotation, limit_node]
                for result phiZ:
                    stopping_of_load_increasing = [StabilityAnalysisSettingsStoppingOfLoadIncreasingResult.RESULT_TYPE_ROTATION_PHI_Z, limit_result_rotation, limit_node]
            save_results_of_all_increments (bool, optional): Save Results of All Increments
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Stability Analysis Settings
        clientObject = model.clientModel.factory.create('ns0:stability_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Stability Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Stability Analysis Type
        clientObject.analysis_type = StabilityAnalysisSettingsAnalysisType.INCREMENTALY_METHOD_WITHOUT_EIGENVALUE.name

        # Minimum Initial Strain
        if minimum_initial_strain in (None, 0):
            clientObject.activate_minimum_initial_prestress = False
        else:
            clientObject.activate_minimum_initial_prestress = True
            clientObject.minimum_initial_strain = minimum_initial_strain

        # Local Torsional Relations
        if local_torsional_rotations:
            clientObject.display_local_torsional_rotations = True

        # Increase Loading
        if len(incrementally_increasing_loading) != 4:
            raise ValueError('WARNING: The incrementally increasing loading parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
        clientObject.initial_load_factor = incrementally_increasing_loading[0]
        clientObject.load_factor_increment = incrementally_increasing_loading[1]
        clientObject.refinement_of_the_last_load_increment = incrementally_increasing_loading[2]
        clientObject.maximum_number_of_load_increments = incrementally_increasing_loading[3]

        # Stopping of Load-Increasing
        if stopping_of_load_increasing:
            if len(stopping_of_load_increasing) != 3:
                raise ValueError('WARNING: For active stopping of load-increasing, the stopping of load increasing parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            clientObject.activate_stopping_of_load_increasing = True
            clientObject.stopping_of_load_increasing_result = stopping_of_load_increasing[0].name
            if stopping_of_load_increasing[0].name == 'RESULT_TYPE_DISPLACEMENT_U' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_DISPLACEMENT_U_X' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_DISPLACEMENT_U_Y' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_DISPLACEMENT_U_Z':
                clientObject.stopping_of_load_increasing_limit_result_displacement = stopping_of_load_increasing[1]
            elif stopping_of_load_increasing[0].name == 'RESULT_TYPE_ROTATION_PHI' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_ROTATION_PHI_X' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_ROTATION_PHI_Y' or stopping_of_load_increasing[0].name == 'RESULT_TYPE_ROTATION_PHI_Z':
                clientObject.stopping_of_load_increasing_limit_result_rotation = stopping_of_load_increasing[1]
            clientObject.stopping_of_load_increasing_limit_node = stopping_of_load_increasing[2]

        # Save Results of All Increments
        clientObject.save_results_of_all_increments = save_results_of_all_increments

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Stability Analysis Settings to client model
        model.clientModel.service.set_stability_analysis_settings(clientObject)
