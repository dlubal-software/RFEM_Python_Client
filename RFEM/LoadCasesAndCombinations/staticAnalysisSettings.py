from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis
from RFEM.enums import StaticAnalysisSettingsMethodOfEquationSystem
from RFEM.enums import StaticAnalysisSettingsPlateBendingTheory, StaticAnalysisType

class StaticAnalysisSettings():

    def __init__(self,
                 no: int = 1,
                 name: str = None,
                 analysis_type=StaticAnalysisType.GEOMETRICALLY_LINEAR,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Static Analysis Setting Tag
            name (str): Static Analysis Setting Name
            analysis_type (enum): Analysis Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Surface
        clientObject = model.clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Analysis Type
        clientObject.analysis_type = analysis_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Static Analysis Settings to client model
        model.clientModel.service.set_static_analysis_settings(clientObject)

    @staticmethod
    def GeometricallyLinear(
                  no: int = 1,
                  name: str = None,
                  load_modification = [False, 1, False],
                  bourdon_effect: bool = False,
                  nonsymmetric_direct_solver: bool = False,
                  method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                  plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                  mass_conversion = [False, 0, 0, 0],
                  comment: str = '',
                  params: dict = None,
                  model = Model):

        """
        Args:
            no (int): Static Analysis Setting Tag
            name (str, optional): Static Analysis Setting Name
            load_modification (list, optional): Load Modification Parameters
                load_modification = [loading_by_multiplier_factor, multiplier_factor, dividing_results]
            bourdon_effect (bool, optional): Bourdon Effect Boolean
            nonsymmetric_direct_solver (bool, optional): Nonsymmetric Direct Solver Boolean
            method_of_equation_system (enum): Static Analysis Settings Method of Equation System Enumeration
            plate_bending_theory (enum): Static Analysis Settings Plate Bending Theory Enumeration
            mass_conversion (list, optional): Mass Conversion Parameters
                mass_conversion = [mass_conversion_enabled, mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model
        clientObject = model.clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Static Analysis Type
        clientObject.analysis_type = StaticAnalysisType.GEOMETRICALLY_LINEAR.name

        # Bourdon Effect Displacement
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect

        # Conversion of Mass into Load
        clientObject.mass_conversion_enabled = mass_conversion[0]
        if mass_conversion[0]:
            clientObject.mass_conversion_factor_in_direction_x = mass_conversion[1]
            clientObject.mass_conversion_factor_in_direction_y = mass_conversion[2]
            clientObject.mass_conversion_factor_in_direction_z = mass_conversion[3]

        # Method for Equation System
        clientObject.method_of_equation_system = method_of_equation_system.name

        if load_modification[0]:
            clientObject.modify_loading_by_multiplier_factor = True
            clientObject.loading_multiplier_factor = load_modification[1]
            clientObject.divide_results_by_loading_factor = load_modification[2]

        # Nonsymetric Direct Solver if Demanded by Nonlinear Model
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver

        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Static Analysis Settings to client model
        model.clientModel.service.set_static_analysis_settings(clientObject)

    @staticmethod
    def LargeDeformation(
                  no: int = 1,
                  name: str = None,
                  iterative_method = StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis.NEWTON_RAPHSON,
                  standard_precision_and_tolerance_settings = [False, 1.0, 1.0, 1.0],
                  control_nonlinear_analysis = [100, 1],
                  load_modification = [False, 1, False],
                  instabil_structure_calculation : bool = True,
                  bourdon_effect: bool = True,
                  nonsymmetric_direct_solver: bool = True,
                  method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                  plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                  mass_conversion = [False, 0, 0, 1],
                  comment: str = '',
                  params: dict = {'save_results_of_all_load_increments': False},
                  model = Model):

        """
        Args:
            no (int): Static Analysis Setting Tag
            name (str, optional):  Static Analysis Setting Name
            iterative_method (enum): Static Analysis Settings Iterative Method for Non-linear Analysis Enumeration
            standard_precision_and_tolerance_settings (list, optional): Standard Precision and Tolerance Settings List
                standard_precision_and_tolerance_settings = [standard_precision_and_tolerance_settings_enabled, precision_of_convergence_criteria_for_nonlinear_calculation, tolerance_for_detection_of_instability, robustness_of_iterative_calculation]
            control_nonlinear_analysis (list): Nonlinear Analysis Control Parameters
                control_nonlinear_analysis = [max_number_of_iterations, number_of_load_increments]
                for iterative_method == "NEWTON_RAPHSON" or iterative_method.name == "NEWTON_RAPHSON_COMBINED_WITH_PICARD" or iterative_method.name == "PICARD" or iterative_method.name == "NEWTON_RAPHSON_WITH_POSTCRITICAL_ANALYSIS":
                    control_nonlinear_analysis = [max_number_of_iterations = int, number_of_load_increments = int]
                for iterative_method == "DYNAMIC_RELAXATION":
                    control_nonlinear_analysis = [max_number_of_iterations = None, number_of_load_increments = None]
            load_modification (list, optional): Load Modification Parameters
                load_modification = [loading_by_multiplier_factor, multiplier_factor, dividing_results]
            instabil_structure_calculation (bool, optional): Instabil Structure Calculation Boolean
            bourdon_effect (bool, optional): Bourdon Effect Boolean
            nonsymmetric_direct_solver (bool, optional): Nonsymmetric Direct Solver Boolean
            method_of_equation_system (enum): Static Analysis Settings Method of Equation System Enumeration
            plate_bending_theory (enum): Static Analysis Settings Plate Bending Theory Enumeration
            mass_conversion (list, optional): Mass Conversion Parameters
                mass_conversion = [mass_conversion_enabled, mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model
        clientObject = model.clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Static Analysis Type
        clientObject.analysis_type = StaticAnalysisType.LARGE_DEFORMATIONS.name

        # Consider Favorable Effect due to Tension in Members
        clientObject.consider_favorable_effect_due_to_tension_in_members = True

        # Bourdon Effect Displacement
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect

        # Iterative Method
        clientObject.iterative_method_for_nonlinear_analysis = iterative_method.name

        # Controls for Nonlinear Analysis
        if iterative_method == StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis.DYNAMIC_RELAXATION:
            clientObject.max_number_of_iterations = None
            clientObject.number_of_load_increments = None
        else:
            clientObject.max_number_of_iterations = control_nonlinear_analysis[0]
            clientObject.number_of_load_increments = control_nonlinear_analysis[1]

        # Conversion of Mass into Load
        clientObject.mass_conversion_enabled = mass_conversion[0]
        if mass_conversion[0]:
            clientObject.mass_conversion_factor_in_direction_x = mass_conversion[1]
            clientObject.mass_conversion_factor_in_direction_y = mass_conversion[2]
            clientObject.mass_conversion_factor_in_direction_z = mass_conversion[3]

        # Method for Equation System
        clientObject.method_of_equation_system = method_of_equation_system.name

        # Modify Loading by Multiplier Factor
        if load_modification[0]:
            clientObject.modify_loading_by_multiplier_factor = True
            clientObject.loading_multiplier_factor = load_modification[1]
            clientObject.divide_results_by_loading_factor = load_modification[2]

        # Nonsymetric Direct Solver if Demanded by Nonlinear Model
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver

        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name

        # Modify Standard precision and Tolerance Settings...
        if standard_precision_and_tolerance_settings[0]:
            clientObject.standard_precision_and_tolerance_settings_enabled = True
            clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = standard_precision_and_tolerance_settings[1]
            clientObject.instability_detection_tolerance = standard_precision_and_tolerance_settings[2]
            clientObject.iterative_calculation_robustness = standard_precision_and_tolerance_settings[3]

        # Try to Calculate Unstable Structure
        clientObject.try_to_calculate_instabil_structure = instabil_structure_calculation

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Static Analysis Settings to client model
        model.clientModel.service.set_static_analysis_settings(clientObject)

    @staticmethod
    def SecondOrderPDelta(
                  no: int = 1,
                  name: str = None,
                  iterative_method = StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis.NEWTON_RAPHSON,
                  standard_precision_and_tolerance_settings = [False, 1.0, 1.0, 1.0],
                  control_nonlinear_analysis = [100, 1],
                  load_modification = [False, 0, False],
                  favorable_effect_due_to_tension_in_members : bool = False,
                  bourdon_effect: bool = True,
                  nonsymmetric_direct_solver: bool = True,
                  internal_forces_to_deformed_structure = [True, True, True, True],
                  method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                  plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                  mass_conversion = [False, 0, 0, 1],
                  comment: str = '',
                  params: dict = None,
                  model = Model):
        """
        Args:
            no (int): Static Analysis Setting Tag
            name (str, optional):  Static Analysis Setting Name
            iterative_method (enum): Static Analysis Settings Iterative Method for Non-linear Analysis Enumeration
            standard_precision_and_tolerance_settings (list, optional): Standard Precision and Tolerance Settings List
                standard_precision_and_tolerance_settings = [standard_precision_and_tolerance_settings_enabled, precision_of_convergence_criteria_for_nonlinear_calculation, tolerance_for_detection_of_instability, robustness_of_iterative_calculation]
            control_nonlinear_analysis (list): Nonlinear Analysis Control Parameters
                control_nonlinear_analysis = [max_number_of_iterations, number_of_load_increments]
            load_modification (list): Modify Loading by Multiplier Factor
                load_modification = [modify_loading_by_multiplier_factor, loading_multiplier_factor, divide_results_by_loading_factor]
            favorable_effect_due_to_tension_in_members (bool, optional): Favorable Effect due to Tension In Members Boolean
            bourdon_effect (bool, optional): Bourdon Effect Boolean
            nonsymmetric_direct_solver (bool, optional): Nonsymmetric Direct Solver Boolean
            internal_forces_to_deformed_structure (list, optional): Internal Forces to Deformed Structure List
                internal_forces_to_deformed_structure = [refer_internal_forces_to_deformed_structure, internal_forces_to_deformed_structure_for_moments, internal_forces_to_deformed_structure_for_normal_forces, internal_forces_to_deformed_structure_for_shear_forces]
            method_of_equation_system (enum): Static Analysis Settings Method of Equation System Enumeration
            plate_bending_theory (enum): Static Analysis Settings Plate Bending Theory Enumeration
            mass_conversion (list, optional): Mass Conversion Parameters
                mass_conversion = [mass_conversion_enabled, mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model
        clientObject = model.clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Static Analysis Type
        clientObject.analysis_type = StaticAnalysisType.SECOND_ORDER_P_DELTA.name

        # Consider Favorable Effect due to Tension in Members
        clientObject.consider_favorable_effect_due_to_tension_in_members = favorable_effect_due_to_tension_in_members

        # Bourdon Effect Displacement
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect

        # Iterative Method
        clientObject.iterative_method_for_nonlinear_analysis = iterative_method.name

        # Conversion of Mass Into Load
        clientObject.mass_conversion_enabled = mass_conversion[0]
        if mass_conversion[0]:
            clientObject.mass_conversion_factor_in_direction_x = mass_conversion[1]
            clientObject.mass_conversion_factor_in_direction_y = mass_conversion[2]
            clientObject.mass_conversion_factor_in_direction_z = mass_conversion[3]

        clientObject.max_number_of_iterations = control_nonlinear_analysis[0]
        clientObject.number_of_load_increments = control_nonlinear_analysis[1]

        # Method for Equation System
        clientObject.method_of_equation_system = method_of_equation_system.name

        # Modify Loading by Multiplier Factor
        if load_modification[0]:
            clientObject.modify_loading_by_multiplier_factor = True
            clientObject.loading_multiplier_factor = load_modification[1]
            clientObject.divide_results_by_loading_factor = load_modification[2]

        # Non-symetric Direct Solver id Demanded by Nonlinear Model
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver

        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name

        # Iterative Method Settings
        if internal_forces_to_deformed_structure[0]:
            clientObject.refer_internal_forces_to_deformed_structure = True
            clientObject.refer_internal_forces_to_deformed_structure_for_moments = internal_forces_to_deformed_structure[1]
            clientObject.refer_internal_forces_to_deformed_structure_for_normal_forces = internal_forces_to_deformed_structure[2]
            clientObject.refer_internal_forces_to_deformed_structure_for_shear_forces = internal_forces_to_deformed_structure[3]

        # Modify Standard Precision and Tolerance Settings...
        if standard_precision_and_tolerance_settings[0]:
            clientObject.standard_precision_and_tolerance_settings_enabled = True
            clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = standard_precision_and_tolerance_settings[1]
            clientObject.instability_detection_tolerance = standard_precision_and_tolerance_settings[2]
            clientObject.iterative_calculation_robustness = standard_precision_and_tolerance_settings[3]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Static Analysis Settings to client model
        model.clientModel.service.set_static_analysis_settings(clientObject)
