from RFEM.initModel import Model, clearAttributes
from RFEM.enums import StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis
from RFEM.enums import StaticAnalysisSettingsMethodOfEquationSystem
from RFEM.enums import StaticAnalysisSettingsPlateBendingTheory, StaticAnalysisType

class StaticAnalysisSettings():
    def __init__(self,
                 no: int = 1,
                 name: str = None,
                 analysis_type=StaticAnalysisType.GEOMETRICALLY_LINEAR,
                 comment: str = '',
                 params: dict = {}):
        """
        Args:
            no (int): Static Analysis Setting Tag
            name (str): Static Analysis Setting Name
            analysis_type (enum): Analysis Type Enumeration
            comment (str): Comments
            params (dict): Parameters
        """
        # Client model | Surface
        clientObject = Model.clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        clientObject.user_defined_name_enabled = True
        clientObject.name = name

        # Analysis Type
        clientObject.analysis_type = analysis_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        Model.clientModel.service.set_static_analysis_settings(clientObject)

    def GeometricallyLinear(self,
                  no: int = 1,
                  name: str = None,
                  load_modification = [False, 1, False],
                  bourdon_effect: bool = False,
                  nonsymmetric_direct_solver: bool = False,
                  method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                  plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                  mass_conversion = [False, 0, 0, 0],
                  comment: str = '',
                  params: dict = {}):

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
            comment (str, optional):
            params (dict, optional):
        """

        # Client model
        clientObject = Model.clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name is not None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Static Analysis Type
        clientObject.analysis_type = StaticAnalysisType.GEOMETRICALLY_LINEAR.name

        # Bourdon Effect Displacement
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect

        # Nonsymetric Direct Solver
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver

        # Equation System
        clientObject.method_of_equation_system = method_of_equation_system.name

        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name
        # Load Modification
        if len(load_modification) != 3:
            raise Exception('WARNING: The load modification parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')

        # if type(load_modification[0]) != bool :
        #     raise Exception ('WARNING: Load multiplier factor parameter at index 0 to be of type "int"')
        # if type(load_modification[1]) != int :
        #     raise Exception ('WARNING: Multiplier factor parameter at index 1 to be of type "int"')
        # if type(load_modification[2]) != bool :
        #     raise Exception ('WARNING: Dividing results parameter at index 2 to be of type "bool"')

        if load_modification[0]:
            clientObject.modify_loading_by_multiplier_factor = True
            clientObject.loading_multiplier_factor = load_modification[1]
            clientObject.divide_results_by_loading_factor = load_modification[2]

        # mass_conversion_enabled = mass_conversion[0]
        # mass_conversion_factor_in_direction_x = mass_conversion[1]
        # mass_conversion_factor_in_direction_y = mass_conversion[2]
        # mass_conversion_factor_in_direction_z = mass_conversion[3]

        #     mass_conversion_factor_in_direction_x =  float
        #     mass_conversion_acceleration_in_direction_y = float
        #     mass_conversion_acceleration_in_direction_z = float

        # Mass Conversion
        if len(mass_conversion) != 4:
            raise Exception('WARNING: The mass conversion parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
        # if type(mass_conversion[0]) != bool :
        #     raise Exception ('WARNING: Enabling the mass conversion at index 0 has to be of type "bool"')
        # if type(mass_conversion[1]) != float or type(mass_conversion[1]) != int:
        #     raise Exception ('WARNING: Mass conversion factor in direction x at index 1 has to be of type "float" or "int"')
        # if type(mass_conversion[2]) != float or type(mass_conversion[2]) != int:
        #     raise Exception ('WARNING: Mass conversion factor in direction y at index 2 has to be of type "float" or "int"')
        # if type(mass_conversion[3]) != float or type(mass_conversion[3]) != int :
        #     raise Exception ('WARNING: Mass conversion factor in direction z at index 3 has to be of type "float" or "int"')

        clientObject.mass_conversion_enabled = mass_conversion[0]
        if mass_conversion[0]:
            clientObject.mass_conversion_factor_in_direction_x = mass_conversion[1]
            clientObject.mass_conversion_factor_in_direction_y = mass_conversion[2]
            clientObject.mass_conversion_factor_in_direction_z = mass_conversion[3]
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        Model.clientModel.service.set_static_analysis_settings(clientObject)

    def LargeDeformation(self,
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
                  params: dict = {}):

        """
        Args:
            no (int): Static Analysis Setting Tag
            name (str, optional):  Static Analysis Setting Name
            iterative_method (enum): Static Analysis Settings Iterative Method for Non-linear Analysis Enumeration
            standard_precision_and_tolerance_settings (list, optional): [standard_precision_and_tolerance_settings_enabled, precision_of_convergence_criteria_for_nonlinear_calculation, tolerance_for_detection_of_instability, robustness_of_iterative_calculation]
            control_nonlinear_analysis (list): [max_number_of_iterations, number_of_load_increments]
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
            params (dict, optional): Parameters
        """

        # Client model
        clientObject = Model.clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name is not None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Static Analysis Type
        clientObject.analysis_type = StaticAnalysisType.LARGE_DEFORMATIONS.name

        # Iterative Method
        clientObject.iterative_method_for_nonlinear_analysis = iterative_method.name
        # not used anywhere
        #if iterative_method.name == "NEWTON_RAPHSON" or iterative_method.name == "NEWTON_RAPHSON_COMBINED_WITH_PICARD" or iterative_method.name == "PICARD" or iterative_method.name == "NEWTON_RAPHSON_WITH_POSTCRITICAL_ANALYSIS":
        #    max_number_of_iterations = int
        #    number_of_load_increments = int
        #elif iterative_method.name == "DYNAMIC_RELAXATION":
        #    max_number_of_iterations = None
        #    number_of_load_increments = None

        # Standard Precision and Tolerance
        # if standard_precision_and_tolerance_settings_enabled != False:
        #     clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = float
        #     clientObject.instability_detection_tolerance = float
        #     clientObject.iterative_calculation_robustness = float
        if len(standard_precision_and_tolerance_settings) != 4:
            raise Exception('WARNING: The standard precision and tolerance settings parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')

        if not isinstance(standard_precision_and_tolerance_settings[0], bool):
            raise Exception ('WARNING: Enabling the standard precision and tolerance settings at index 0 to be of type "bool"')
        # if type(standard_precision_and_tolerance_settings[1]) != float or type(standard_precision_and_tolerance_settings[1]) != int:
        #     raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculation factor at index 1 to be of type "float" or "int"')
        # if type(standard_precision_and_tolerance_settings[2]) != float or type(standard_precision_and_tolerance_settings[2]) != int:
        #     raise Exception ('WARNING: Tolerance for detection of instability factor at index 2 to be of type "float" or "int"')
        # if type(standard_precision_and_tolerance_settings[3]) != float or type(standard_precision_and_tolerance_settings[3]) != int:
        #     raise Exception ('WARNING: Robustness of iterative calculation factor at index 3 to be of type "float" or "int"')

        # while not float(standard_precision_and_tolerance_settings[1]) or not int(standard_precision_and_tolerance_settings[1]) in range(0.01,100):
        #     raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculations at index 1 is out of range. Input has to be in the range [0.01 ... 100].')

        # while not float(standard_precision_and_tolerance_settings[2]) or not int(standard_precision_and_tolerance_settings[2]) in range(0.01,100):
        #     raise Exception ('WARNING: Tolerance for detection of instability at index 2 is out of range. Input has to be in the range [0.01 ... 100].')

        # while not float(standard_precision_and_tolerance_settings[3]) or not int(standard_precision_and_tolerance_settings[3]) in range(1.00,100):
        #     raise Exception ('WARNING: Robustness of iterative calculation at index 3 is out of range. Input has to be in the range [1.00 ... 100].')
        if standard_precision_and_tolerance_settings[0]:
            clientObject.standard_precision_and_tolerance_settings_enabled = True
            clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = standard_precision_and_tolerance_settings[1]
            clientObject.instability_detection_tolerance = standard_precision_and_tolerance_settings[2]
            clientObject.iterative_calculation_robustness = standard_precision_and_tolerance_settings[3]

        # Control nonlinear Analysis
        if len(control_nonlinear_analysis) != 2:
            raise Exception('WARNING: The nonlinear analysis control parameter needs to be of length 2. Kindly check list inputs for completeness and correctness.')

        if not isinstance(control_nonlinear_analysis[0],int):
            raise Exception ('WARNING: Enabling the standard precision and tolerance settings at index 0 has to be of type "int"')
        if not isinstance(control_nonlinear_analysis[1], int):
            raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculation factor at index 1 has to be of type "int"')

        clientObject.max_number_of_iterations = control_nonlinear_analysis[0]
        clientObject.number_of_load_increments = control_nonlinear_analysis[1]
        ## Load Modification
        if len(load_modification) != 3:
            raise Exception('WARNING: The load modification parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')

        # if type(load_modification[0]) != bool :
        #     raise Exception ('WARNING: Load multiplier factor parameter at index 0 to be of type "int"')
        # if type(load_modification[1]) != int :
        #     raise Exception ('WARNING: Multiplier factor parameter at index 1 to be of type "int"')
        # if type(load_modification[2]) != bool :
        #     raise Exception ('WARNING: Dividing results parameter at index 2 to be of type "bool"')

        if load_modification[0]:
            clientObject.modify_loading_by_multiplier_factor = True
            clientObject.loading_multiplier_factor = load_modification[1]
            clientObject.divide_results_by_loading_factor = load_modification[2]

        # Instabil Structure
        clientObject.try_to_calculate_instabil_structure = instabil_structure_calculation

        # Bourdon Effect Displacement
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect

        # Nonsymetric Direct Solver
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver

        # Equation System
        clientObject.method_of_equation_system = method_of_equation_system.name

        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name

        # Mass Conversion
        if len(mass_conversion) != 4:
            raise Exception('WARNING: The mass conversion parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
        # if type(mass_conversion[0]) != bool :
        #     raise Exception ('WARNING: Enabling the mass conversion at index 0 has to be of type "bool"')
        # if type(mass_conversion[1]) != float or type(mass_conversion[1]) != int:
        #     raise Exception ('WARNING: Mass conversion factor in direction x at index 1 has to be of type "float" or "int"')
        # if type(mass_conversion[2]) != float or type(mass_conversion[2]) != int:
        #     raise Exception ('WARNING: Mass conversion factor in direction y at index 2 has to be of type "float" or "int"')
        # if type(mass_conversion[3]) != float or type(mass_conversion[3]) != int :
        #     raise Exception ('WARNING: Mass conversion factor in direction z at index 3 has to be of type "float" or "int"')

        clientObject.mass_conversion_enabled = mass_conversion[0]
        if mass_conversion[0]:
            clientObject.mass_conversion_factor_in_direction_x = mass_conversion[1]
            clientObject.mass_conversion_factor_in_direction_y = mass_conversion[2]
            clientObject.mass_conversion_factor_in_direction_z = mass_conversion[3]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        Model.clientModel.service.set_static_analysis_settings(clientObject)

    def SecondOrderPDelta(self,
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
                  params: dict = {}):
        """
        Args:
            no (int): Static Analysis Setting Tag
            name (str, optional):  Static Analysis Setting Name
            iterative_method (enum): Static Analysis Settings Iterative Method for Non-linear Analysis Enumeration
            standard_precision_and_tolerance_settings (list, optional): [Standard Precision and Tolerance Settings List
                standard_precision_and_tolerance_settings = [standard_precision_and_tolerance_settings_enabled, precision_of_convergence_criteria_for_nonlinear_calculation, tolerance_for_detection_of_instability, robustness_of_iterative_calculation]
            control_nonlinear_analysis (list): Nonlinear Analysis Control Parameters
                control_nonlinear_analysis = [max_number_of_iterations, number_of_load_increments]
            favorable_effect_due_to_tension_in_members (bool, optional): Favorable Effect due to Tension In Members Boolean
            bourdon_effect (bool, optional): Bourdon Effect Boolean
            nonsymmetric_direct_solver (bool, optional): Nonsymmetric Direct Solver Boolean
            internal_forces_to_deformed_structure (list, optional): Internal Forces to Deformed Structure List
                internal_forces_to_deformed_structure = [refer_internal_forces_to_deformed_structure, internal_forces_to_deformed_structure_for_moments, internal_forces_to_deformed_structure_for_normal_forces, internal_forces_to_deformed_structure_for_shear_forces]
            method_of_equation_system (enum): Static Analysis Settings Method of Equation System Enumeration
            plate_bending_theory (enum): Static Analysis Settings Plate Bending Theory Enumeration
            mass_conversion (list, optional): Mass Conversion Parameters
                mass_conversion = [mass_conversion_enabled, mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
            comment (str, optional):
            params (dict, optional):
        """

        # Client model
        clientObject = Model.clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name is not None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Static Analysis Type
        clientObject.analysis_type = StaticAnalysisType.SECOND_ORDER_P_DELTA.name

        # Iterative Method
        clientObject.iterative_method_for_nonlinear_analysis = iterative_method.name

        # Standard Precision and Tolerance
        # if standard_precision_and_tolerance_settings_enabled != False:
        #     clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = float
        #     clientObject.instability_detection_tolerance = float
        #     clientObject.iterative_calculation_robustness = float
        if len(standard_precision_and_tolerance_settings) != 4:
            raise Exception('WARNING: The standard precision and tolerance settings parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')

        if not isinstance(standard_precision_and_tolerance_settings[0], bool):
            raise Exception ('WARNING: Enabling the standard precision and tolerance settings at index 0 to be of type "bool"')
        # if type(standard_precision_and_tolerance_settings[1]) != float or type(standard_precision_and_tolerance_settings[1]) != int:
        #     raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculation factor at index 1 to be of type "float" or "int"')
        # if type(standard_precision_and_tolerance_settings[2]) != float or type(standard_precision_and_tolerance_settings[2]) != int:
        #     raise Exception ('WARNING: Tolerance for detection of instability factor at index 2 to be of type "float" or "int"')
        # if type(standard_precision_and_tolerance_settings[3]) != float or type(standard_precision_and_tolerance_settings[3]) != int:
        #     raise Exception ('WARNING: Robustness of iterative calculation factor at index 3 to be of type "float" or "int"')

        # while not float(standard_precision_and_tolerance_settings[1]) or not int(standard_precision_and_tolerance_settings[1]) in range(0.01,100):
        #     raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculations at index 1 is out of range. Input has to be in the range [0.01 ... 100].')

        # while not float(standard_precision_and_tolerance_settings[2]) or not int(standard_precision_and_tolerance_settings[2]) in range(0.01,100):
        #     raise Exception ('WARNING: Tolerance for detection of instability at index 2 is out of range. Input has to be in the range [0.01 ... 100].')

        # while not float(standard_precision_and_tolerance_settings[3]) or not int(standard_precision_and_tolerance_settings[3]) in range(1.00,100):
        #     raise Exception ('WARNING: Robustness of iterative calculation at index 3 is out of range. Input has to be in the range [1.00 ... 100].')
        if standard_precision_and_tolerance_settings[0]:
            clientObject.standard_precision_and_tolerance_settings_enabled = True
            clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = standard_precision_and_tolerance_settings[1]
            clientObject.instability_detection_tolerance = standard_precision_and_tolerance_settings[2]
            clientObject.iterative_calculation_robustness = standard_precision_and_tolerance_settings[3]

       # Control nonlinear Analysis
        if len(control_nonlinear_analysis) != 2:
            raise Exception('WARNING: The nonlinear analysis control parameter needs to be of length 2. Kindly check list inputs for completeness and correctness.')

        if not isinstance(control_nonlinear_analysis[0], int):
            raise Exception ('WARNING: Enabling the standard precision and tolerance settings at index 0 has to be of type "int"')
        if not isinstance(control_nonlinear_analysis[1], int):
            raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculation factor at index 1 has to be of type "int"')

        clientObject.max_number_of_iterations = control_nonlinear_analysis[0]
        clientObject.number_of_load_increments = control_nonlinear_analysis[1]

         ## Load Modification
        if len(load_modification) != 3:
            raise Exception('WARNING: The load modification parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')

        # if type(load_modification[0]) != bool :
        #     raise Exception ('WARNING: Load multiplier factor parameter at index 0 to be of type "int"')
        # if type(load_modification[1]) != int :
        #     raise Exception ('WARNING: Multiplier factor parameter at index 1 to be of type "int"')
        # if type(load_modification[2]) != bool :
        #     raise Exception ('WARNING: Dividing results parameter at index 2 to be of type "bool"')

        if load_modification[0]:
            clientObject.modify_loading_by_multiplier_factor = True
            clientObject.loading_multiplier_factor = load_modification[1]
            clientObject.divide_results_by_loading_factor = load_modification[2]
        # Effect due to Tension in Members
        clientObject.consider_favorable_effect_due_to_tension_in_members = favorable_effect_due_to_tension_in_members
        # Bourdon Effect Displacement
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect
        # Nonsymetric Direct Solver
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver
        if len(internal_forces_to_deformed_structure) != 4:
            raise Exception('WARNING: The internal forces to deformed structure parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
        # if type(mass_conversion[0]) != bool :
        #     raise Exception ('WARNING: Refering internal forces to deformed structure at index 0 to be of type "bool"')
        # if type(mass_conversion[1]) != bool :
        #     raise Exception ('WARNING: Internal forces to deformed structure for moments at index 1 to be of type "bool"')
        # if type(mass_conversion[2]) != bool :
        #     raise Exception ('WARNING: Internal forces to deformed structure for normal forces at index 2 to be of type "bool"')
        # if type(mass_conversion[3]) != bool :
        #     raise Exception ('WARNING: Internal forces to deformed structure for shear forces at index 3 to be of type "bool"')
         # Internal Forces to Deformed Structure
        if internal_forces_to_deformed_structure[0]:
            clientObject.refer_internal_forces_to_deformed_structure = internal_forces_to_deformed_structure[0]
            clientObject.refer_internal_forces_to_deformed_structure_for_moments = internal_forces_to_deformed_structure[1]
            clientObject.refer_internal_forces_to_deformed_structure_for_normal_forces = internal_forces_to_deformed_structure[2]
            clientObject.refer_internal_forces_to_deformed_structure_for_shear_forces = internal_forces_to_deformed_structure[3]

        # Equation System
        clientObject.method_of_equation_system = method_of_equation_system.name

        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name

       # Mass Conversion
        if len(mass_conversion) != 4:
            raise Exception('WARNING: The mass conversion parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
        # if type(mass_conversion[0]) != bool :
        #     raise Exception ('WARNING: Enabling the mass conversion at index 0 has to be of type "bool"')
        # if type(mass_conversion[1]) != float or type(mass_conversion[1]) != int:
        #     raise Exception ('WARNING: Mass conversion factor in direction x at index 1 has to be of type "float" or "int"')
        # if type(mass_conversion[2]) != float or type(mass_conversion[2]) != int:
        #     raise Exception ('WARNING: Mass conversion factor in direction y at index 2 has to be of type "float" or "int"')
        # if type(mass_conversion[3]) != float or type(mass_conversion[3]) != int :
        #     raise Exception ('WARNING: Mass conversion factor in direction z at index 3 has to be of type "float" or "int"')

        clientObject.mass_conversion_enabled = mass_conversion[0]
        if mass_conversion[0]:
            clientObject.mass_conversion_factor_in_direction_x = mass_conversion[1]
            clientObject.mass_conversion_factor_in_direction_y = mass_conversion[2]
            clientObject.mass_conversion_factor_in_direction_z = mass_conversion[3]
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        Model.clientModel.service.set_static_analysis_settings(clientObject)
