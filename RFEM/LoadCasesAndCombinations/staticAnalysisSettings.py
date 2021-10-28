from RFEM.initModel import *
from RFEM.enums import StaticAnalysisType
from RFEM.enums import StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis
from RFEM.enums import StaticAnalysisSettingsMethodOfEquationSystem
from RFEM.enums import StaticAnalysisSettingsPlateBendingTheory

class StaticAnalysisSettings():
    def __init__(self,
                 no: int = 1,
                 name: str = None,
                 analysis_type = StaticAnalysisType.GEOMETRICALLY_LINEAR,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        clientObject.user_defined_name_enabled = True
        clientObject.name = name

        # Analysis Type
        clientObject.analysis_type = StaticAnalysisType.GEOMETRICALLY_LINEAR.name
        
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        clientModel.service.set_static_analysis_settings(clientObject)
        
    def GeometricallyLinear(self,
                 no: int = 1,
                 name: str = None,
                 load_modification = [False, None, None],
                 bourdon_effect: bool = True,
                 nonsymmetric_direct_solver: bool = True,
                 method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                 plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                 mass_conversion = [False, None, None, None],
                 comment: str = '',
                 params: dict = {}):   
        
        '''
        Args:
            no (int): 
            name (str, optional): Static Analysis Name
            load_modification (list, optional): [load_multiplier_factor, multiplier_factor, dividing_results]
            bourdon_effect (bool, optional): 
            nonsymmetric_direct_solver (bool, optional): 
            method_of_equation_system (enum): Static Analysis Settings Method of Equation System Enumeration
            plate_bending_theory (enum): Static Analysis Settings Plate Bending Theory Enumeration
            mass_conversion (list, optional): [mass_conversion_enabled, mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
                  For mass_conversion_enabled == False:
                      mass_conversion_factors = [None, None, None]
                  For mass_conversion_enabled == True:
                      mass_conversion_factors = [double, double, double]
            comment (str, optional):
            params (dict, optional):
        '''

        # Client model
        clientObject = clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Static Analysis Type
        clientObject.analysis_type = StaticAnalysisType.GEOMETRICALLY_LINEAR.name

        # Load Multiplier Factor 
        clientObject.modify_loading_by_multiplier_factor = load_multiplier_factor 
        clientObject.number_of_iterations_for_loading_prestress = multiplier_factor
        clientObject.divide_results_by_loading_factor = dividing_results
        if load_multiplier_factor != False:
            load_multiplier_factor = True 
            multiplier_factor = int
            dividing_results = bool
            
        # Bourdon Effect Displacement 
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect 

        # Nonsymetric Direct Solver
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver

        # Equation System
        clientObject.method_of_equation_system = method_of_equation_system.name

        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name

        # Mass Conversion
        clientObject.mass_conversion_enabled = mass_conversion_enabled
        clientObject.mass_conversion_factor_in_direction_x = mass_conversion_factor_in_direction_x
        clientObject.mass_conversion_factor_in_direction_y = mass_conversion_factor_in_direction_y
        clientObject.mass_conversion_factor_in_direction_z = mass_conversion_factor_in_direction_z
        
        mass_conversion_enabled = mass_conversion[0]
        mass_conversion_factor_in_direction_x = mass_conversion[1]
        mass_conversion_factor_in_direction_y = mass_conversion[2]
        mass_conversion_factor_in_direction_z = mass_conversion[3]
        if mass_conversion_enabled != False:
            mass_conversion_factor_in_direction_x =  double
            mass_conversion_acceleration_in_direction_y = double
            mass_conversion_acceleration_in_direction_z = double
            
        if len(mass_conversion) != 4:
            raise Exception('WARNING: The mass conversion parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')    
            
        if type(mass_conversion[0]) != bool :
            raise Exception ('WARNING: Enabling the mass conversion at index 0 to be of type "bool"')
        if type(mass_conversion[1]) != double :
            raise Exception ('WARNING: Mass conversion factor in direction x at index 1 to be of type "double"')
        if type(mass_conversion[2]) != double :
            raise Exception ('WARNING: Mass conversion factor in direction y at index 2 to be of type "double"')
        if type(mass_conversion[3]) != double :
            raise Exception ('WARNING: Mass conversion factor in direction z at index 3 to be of type "double"')
            
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        clientModel.service.set_static_analysis_settings(clientObject)

    def LargeDeformation(self,
                 no: int = 1,
                 name: str = None,
                 iterative_method = StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis.NEWTON_RAPHSON,
                 standard_precision_and_tolerance_settings = [False, None, None, None],
                 control_nonlinear_analysis = [100, 1],
                 load_modification = [False, None, None],
                 instabil_structure_calculation : bool = True,
                 bourdon_effect: bool = True,
                 nonsymmetric_direct_solver: bool = True,
                 method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                 plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                 mass_conversion = [False, None, None, None],
                 comment: str = '',
                 params: dict = {}):  
        '''
        Args:
            no (int): 
            name (str, optional): Static Analysis Name
            iterative_method (enum): Static Analysis Settings Iterative Method for Non-linear Analysis Enumeration
                 For load_multiplier_factor == load_multiplier_factor == or load_multiplier_factor == or load_multiplier_factor:
                       max_number_of_iterations = int
                       number_of_load_increments = int
                 For load_multiplier_factor == :
                       max_number_of_iterations = None
                       number_of_load_increments = None
            standard_precision_and_tolerance_settings (list, optional): [standard_precision_and_tolerance_settings_enabled, precision_of_convergence_criteria_for_nonlinear_calculation, tolerance_for_detection_of_instability, robustness_of_iterative_calculation]
            control_nonlinear_analysis (list): [max_number_of_iterations, number_of_load_increments]
            load_modification (list, optional): [load_multiplier_factor, multiplier_factor, dividing_results]
            load_multiplier_factor (bool, optional): 
                 For load_multiplier_factor == False:
                      multiplier_factor = None
                      dividing_results = None
                 For load_multiplier_factor == True:
                      multiplier_factor = int
                      dividing_results = bool
            instabil_structure_calculation (bool, optional): 
            bourdon_effect (bool, optional): 
            nonsymmetric_direct_solver (bool, optional): 
            method_of_equation_system (enum): Static Analysis Settings Method of Equation System Enumeration
            plate_bending_theory (enum): Static Analysis Settings Plate Bending Theory Enumeration
            mass_conversion (list, optional): [mass_conversion_enabled, mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
                  For mass_conversion_enabled == False:
                      mass_conversion_factors = [None, None, None]
                  For mass_conversion_enabled == True:
                      mass_conversion_factors = [double, double, double]
            comment (str, optional): 
            params (dict, optional):
        '''  
    
        # Client model
        clientObject = clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Static Analysis Type
        clientObject.analysis_type = StaticAnalysisType.LARGE_DEFORMATIONS.name

        # Iterative Method
        clientObject.iterative_method_for_nonlinear_analysis = iterative_method.name

        # Standard Precision and Tolerance
        
        clientObject.standard_precision_and_tolerance_settings_enabled = standard_precision_and_tolerance_settings[0]
        clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = standard_precision_and_tolerance_settings[1]
        clientObject.instability_detection_tolerance = standard_precision_and_tolerance_settings[2]
        clientObject.iterative_calculation_robustness = standard_precision_and_tolerance_settings[3]
        
        clientObject.standard_precision_and_tolerance_settings_enabled = standard_precision_and_tolerance_settings_enabled
        clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = precision_of_convergence_criteria_for_nonlinear_calculation
        clientObject.instability_detection_tolerance = tolerance_for_detection_of_instability
        clientObject.iterative_calculation_robustness = robustness_of_iterative_calculation
        
        if standard_precision_and_tolerance_settings_enabled != False:
            clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = double
            clientObject.instability_detection_tolerance = double
            clientObject.iterative_calculation_robustness = double
            
        if len(mass_conversion) != 4:
            raise Exception('WARNING: The standard precision and tolerance settings parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')    
        
        if type(standard_precision_and_tolerance_settings[0]) != bool :
            raise Exception ('WARNING: Enabling the standard precision and tolerance settings at index 0 to be of type "bool"')
        if type(standard_precision_and_tolerance_settings[1]) != double :
            raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculation factor at index 1 to be of type "double"')
        if type(standard_precision_and_tolerance_settings[2]) != double :
            raise Exception ('WARNING: Tolerance for detection of instability factor at index 2 to be of type "double"')
        if type(standard_precision_and_tolerance_settings[3]) != double :
            raise Exception ('WARNING: Robustness of iterative calculation factor at index 3 to be of type "double"')
        
        if :
            raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculations at index 1 is out of range. Input has to be in the range [0.01 ... 100].')
        
        if :
            raise Exception ('WARNING: Tolerance for detection of instability at index 2 is out of range. Input has to be in the range [0.01 ... 100].')
        
        if :
            raise Exception ('WARNING: Robustness of iterative calculation at index 3 is out of range. Input has to be in the range [1.00 ... 100].')
        

        # Control nonlinear Analysis
        clientObject.max_number_of_iterations = control_nonlinear_analysis[0]
        clientObject.number_of_load_increments = control_nonlinear_analysis[1]
        
        clientObject.max_number_of_iterations = max_number_of_iterations
        clientObject.number_of_load_increments = number_of_load_increments
        
        if len(control_nonlinear_analysis) != 2:
            raise Exception('WARNING: The nonlinear analysis control parameter needs to be of length 2. Kindly check list inputs for completeness and correctness.')
        
        if type(control_nonlinear_analysis[0]) != int :
            raise Exception ('WARNING: Enabling the standard precision and tolerance settings at index 0 to be of type "int"')
        if type(control_nonlinear_analysis[1]) != int :
            raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculation factor at index 1 to be of type "int"')
            
    

        # Load Modification
        
        clientObject.modify_loading_by_multiplier_factor = load_modification[0]
        clientObject.number_of_iterations_for_loading_prestress = load_modification[1]
        clientObject.divide_results_by_loading_factor = load_modification[2]
        
        clientObject.modify_loading_by_multiplier_factor = load_multiplier_factor 
        clientObject.number_of_iterations_for_loading_prestress = multiplier_factor
        clientObject.divide_results_by_loading_factor = dividing_results
  
        if load_multiplier_factor != False:
            load_multiplier_factor = True 
            multiplier_factor = int
            dividing_results = bool
            
        if len(load_modification) != 3:
            raise Exception('WARNING: The load modification parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            
        if type(load_modification[0]) != bool :
            raise Exception ('WARNING: Load multiplier factor parameter at index 0 to be of type "int"')
        if type(load_modification[1]) != int :
            raise Exception ('WARNING: Multiplier factor parameter at index 1 to be of type "int"')
        if type(load_modification[2]) != bool :
            raise Exception ('WARNING: Dividing results parameter at index 0 to be of type "int"')
        
        if load_multiplier_factor != False:
            load_multiplier_factor = True 
            multiplier_factor = int
            dividing_results = bool
        
        
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
        clientObject.mass_conversion_enabled = mass_conversion_enabled
        clientObject.mass_conversion_factor_in_direction_x = mass_conversion_factor_in_direction_x
        clientObject.mass_conversion_factor_in_direction_y = mass_conversion_factor_in_direction_y
        clientObject.mass_conversion_factor_in_direction_z = mass_conversion_factor_in_direction_z
        
        mass_conversion_enabled = mass_conversion[0]
        mass_conversion_factor_in_direction_x = mass_conversion[1]
        mass_conversion_factor_in_direction_y = mass_conversion[2]
        mass_conversion_factor_in_direction_z = mass_conversion[3]
        if mass_conversion_enabled != False:
            mass_conversion_factor_in_direction_x =  double
            mass_conversion_acceleration_in_direction_y = double
            mass_conversion_acceleration_in_direction_z = double
            
        if len(mass_conversion) != 4:
            raise Exception('WARNING: The mass conversion parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')    
            
        if type(mass_conversion[0]) != bool :
            raise Exception ('WARNING: Enabling the mass conversion at index 0 to be of type "bool"')
        if type(mass_conversion[1]) != double :
            raise Exception ('WARNING: Mass conversion factor in direction x at index 1 to be of type "double"')
        if type(mass_conversion[2]) != double :
            raise Exception ('WARNING: Mass conversion factor in direction y at index 2 to be of type "double"')
        if type(mass_conversion[3]) != double :
            raise Exception ('WARNING: Mass conversion factor in direction z at index 3 to be of type "double"')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        clientModel.service.set_static_analysis_settings(clientObject)

        def SecondOrderPDelta (self,
                 no: int = 1,
                 name: str = None,
                 iterative_method = StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis.NEWTON_RAPHSON,
                 standard_precision_and_tolerance_settings_enabled : bool = False,
                 control_nonlinear_analysis = [100, 1],
                 load_modification = [False, None, None],
                 favorable_effect_due_to_tension_in_members : bool = False,
                 bourdon_effect: bool = True,
                 nonsymmetric_direct_solver: bool = True,
                 refer_internal_forces_to_deformed_structure : bool = False,
                 internal_forces = [None, None, None]
                 method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                 plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                 mass_conversion = [False, None, None, None],
                 comment: str = '',
                 params: dict = {}):  
            
        '''
        Args:
            no (int): 
            name (str, optional): Static Analysis Name
            iterative_method (enum): Static Analysis Settings Iterative Method for Non-linear Analysis Enumeration
            control_nonlinear_analysis (list): [max_number_of_iterations, number_of_load_increments]
            load_multiplier_factor (bool, optional): 
                 For load_multiplier_factor == False:
                      multiplier_factor = None
                      dividing_results = None
                 For load_multiplier_factor == True:
                      multiplier_factor = int
                      dividing_results = bool
            favorable_effect_due_to_tension_in_members (bool, optional): 
            bourdon_effect (bool, optional): 
            nonsymmetric_direct_solver (bool, optional): 
            refer_internal_forces_to_deformed_structure (bool, optional): 
                 For refer_internal_forces_to_deformed_structure == False:
                       internal_forces_to_deformed_structure_for_moments = None 
                       internal_forces_to_deformed_structure_for_normal_forces = None
                       internal_forces_to_deformed_structure_for_shear_forces = None
                 For refer_internal_forces_to_deformed_structure == True:
                       internal_forces_to_deformed_structure_for_moments = bool 
                       internal_forces_to_deformed_structure_for_normal_forces = bool
                       internal_forces_to_deformed_structure_for_shear_forces = bool
            method_of_equation_system (enum): Static Analysis Settings Method of Equation System Enumeration
            plate_bending_theory (enum): Static Analysis Settings Plate Bending Theory Enumeration
            mass_conversion (list, optional): [mass_conversion_enabled, mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
                  For mass_conversion_enabled == False:
                      mass_conversion_factors = [None, None, None]
                  For mass_conversion_enabled == True:
                      mass_conversion_factors = [double, double, double]
            comment (str, optional):
            params (dict, optional):
        '''        
    
        # Client model
        clientObject = clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name != None:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Static Analysis Type
        clientObject.analysis_type = StaticAnalysisType.SECOND_ORDER_P_DELTA.name

        # Iterative Method
        clientObject.iterative_method_for_nonlinear_analysis = iterative_method.name

        # Control nonlinear Analysis
        clientObject.max_number_of_iterations = control_nonlinear_analysis[0]
        clientObject.number_of_load_increments = control_nonlinear_analysis[1]
        
        clientObject.max_number_of_iterations = max_number_of_iterations
        clientObject.number_of_load_increments = number_of_load_increments
        
        if len(control_nonlinear_analysis) != 2:
            raise Exception('WARNING: The nonlinear analysis control parameter needs to be of length 2. Kindly check list inputs for completeness and correctness.')
        
        if type(control_nonlinear_analysis[0]) != int :
            raise Exception ('WARNING: Enabling the standard precision and tolerance settings at index 0 to be of type "int"')
        if type(control_nonlinear_analysis[1]) != int :
            raise Exception ('WARNING: Precision of convergence criteria for nonlinear calculation factor at index 1 to be of type "int"')
        
        
        # Load Modification
        
        clientObject.modify_loading_by_multiplier_factor = load_modification[0]
        clientObject.number_of_iterations_for_loading_prestress = load_modification[1]
        clientObject.divide_results_by_loading_factor = load_modification[2]
        
        clientObject.modify_loading_by_multiplier_factor = load_multiplier_factor 
        clientObject.number_of_iterations_for_loading_prestress = multiplier_factor
        clientObject.divide_results_by_loading_factor = dividing_results
  
        if load_multiplier_factor != False:
            load_multiplier_factor = True 
            multiplier_factor = int
            dividing_results = bool
            
        if len(load_modification) != 3:
            raise Exception('WARNING: The load modification parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')
            
        if type(load_modification[0]) != bool :
            raise Exception ('WARNING: Load multiplier factor parameter at index 0 to be of type "int"')
        if type(load_modification[1]) != int :
            raise Exception ('WARNING: Multiplier factor parameter at index 1 to be of type "int"')
        if type(load_modification[2]) != bool :
            raise Exception ('WARNING: Dividing results parameter at index 0 to be of type "int"')
        
        if load_multiplier_factor != False:
            load_multiplier_factor = True 
            multiplier_factor = int
            dividing_results = bool


        # Effect due to Tension in Members
        clientObject.consider_favorable_effect_due_to_tension_in_members = favorable_effect_due_to_tension_in_members

            
        # Bourdon Effect Displacement 
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect 


        # Nonsymetric Direct Solver
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver


        # Internal Forces to Deformed Structure
        clientObject.refer_internal_forces_to_deformed_structure = refer_internal_forces_to_deformed_structure
        clientObject.refer_internal_forces_to_deformed_structure_for_moments = internal_forces_to_deformed_structure_for_moments
        clientObject.refer_internal_forces_to_deformed_structure_for_normal_forces = internal_forces_to_deformed_structure_for_normal_forces
        clientObject.refer_internal_forces_to_deformed_structure_for_shear_forces = internal_forces_to_deformed_structure_for_shear_forces
        if refer_internal_forces_to_deformed_structure != False:
            internal_forces_to_deformed_structure_for_moments = bool 
            internal_forces_to_deformed_structure_for_normal_forces = bool
            internal_forces_to_deformed_structure_for_shear_forces = bool
            
        # Equation System
        clientObject.method_of_equation_system = method_of_equation_system.name
        
        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name

        # Mass Conversion
        clientObject.mass_conversion_enabled = mass_conversion_enabled
        clientObject.mass_conversion_factor_in_direction_x = mass_conversion_factor_in_direction_x
        clientObject.mass_conversion_factor_in_direction_y = mass_conversion_factor_in_direction_y
        clientObject.mass_conversion_factor_in_direction_z = mass_conversion_factor_in_direction_z
        
        mass_conversion_enabled = mass_conversion[0]
        mass_conversion_factor_in_direction_x = mass_conversion[1]
        mass_conversion_factor_in_direction_y = mass_conversion[2]
        mass_conversion_factor_in_direction_z = mass_conversion[3]
        if mass_conversion_enabled != False:
            mass_conversion_factor_in_direction_x =  double
            mass_conversion_acceleration_in_direction_y = double
            mass_conversion_acceleration_in_direction_z = double
            
        if len(mass_conversion) != 4:
            raise Exception('WARNING: The mass conversion parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')    
            
        if type(mass_conversion[0]) != bool :
            raise Exception ('WARNING: Enabling the mass conversion at index 0 to be of type "bool"')
        if type(mass_conversion[1]) != double :
            raise Exception ('WARNING: Mass conversion factor in direction x at index 1 to be of type "double"')
        if type(mass_conversion[2]) != double :
            raise Exception ('WARNING: Mass conversion factor in direction y at index 2 to be of type "double"')
        if type(mass_conversion[3]) != double :
            raise Exception ('WARNING: Mass conversion factor in direction z at index 3 to be of type "double"')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        clientModel.service.set_static_analysis_settings(clientObject)
