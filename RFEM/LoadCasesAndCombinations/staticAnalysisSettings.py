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
                 load_multiplier_factor : bool = False,
                 multiplier_factor = None,
                 dividing_results = None,
                 bourdon_effect: bool = True,
                 nonsymmetric_direct_solver: bool = True,
                 method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                 plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                 mass_conversion_enabled : bool = False,
                 mass_conversion_factors = [None, None, None]
                 comment: str = '',
                 params: dict = {}):   
        
        '''
        Args:
            no (int): 
            name (str, optional): Static Analysis Name
            load_multiplier_factor (bool, optional): 
                 For load_multiplier_factor == False:
                      multiplier_factor = None
                      dividing_results = None
                 For load_multiplier_factor == True:
                      multiplier_factor = int
                      dividing_results = bool
            bourdon_effect (bool, optional): 
            nonsymmetric_direct_solver (bool, optional): 
            method_of_equation_system (enum): Static Analysis Settings Method of Equation System Enumeration
            plate_bending_theory (enum): Static Analysis Settings Plate Bending Theory Enumeration
            mass_conversion_enabled (bool, optional): 
            mass_conversion_factors (list, optional): [mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
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
        
        mass_conversion_factor_in_direction_x = mass_conversion_factors[0]
        mass_conversion_factor_in_direction_y = mass_conversion_factors[1]
        mass_conversion_factor_in_direction_z = mass_conversion_factors[2]
        if mass_conversion_enabled != False:
            mass_conversion_factor_in_direction_x =  double
            mass_conversion_acceleration_in_direction_y = double
            mass_conversion_acceleration_in_direction_z = double
        if len(mass_conversion_factors) != 3:
            raise Exception('WARNING: The mass conversion factors parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')    

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
                 standard_precision_and_tolerance_settings_enabled : bool = False,
                 max_number_of_iterations: int = 100, 
                 number_of_load_increments: int = 1,
                 load_multiplier_factor : bool = False,
                 multiplier_factor = None,
                 dividing_results = None,
                         unstable function
                 bourdon_effect: bool = True,
                 nonsymmetric_direct_solver: bool = True,
                 method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                 plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                 mass_conversion_enabled : bool = False,
                 mass_conversion_factors = [None, None, None]
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
            standard_precision_and_tolerance_settings_enabled (bool, optional):
            max_number_of_iterations (int): Maximum Number of Iterations
            number_of_load_increments (int): Number of Load Increments
            load_multiplier_factor (bool, optional): 
                 For load_multiplier_factor == False:
                      multiplier_factor = None
                      dividing_results = None
                 For load_multiplier_factor == True:
                      multiplier_factor = int
                      dividing_results = bool
            bourdon_effect (bool, optional): 
            nonsymmetric_direct_solver (bool, optional): 
            method_of_equation_system (enum): Static Analysis Settings Method of Equation System Enumeration
            plate_bending_theory (enum): Static Analysis Settings Plate Bending Theory Enumeration
            mass_conversion_enabled (bool, optional): 
            mass_conversion_factors (list, optional): [mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
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
        clientObject.standard_precision_and_tolerance_settings_enabled = standard_precision_and_tolerance_settings_enabled
        if standard_precision_and_tolerance_settings_enabled != False:
            clientObject.precision_of_convergence_criteria_for_nonlinear_calculation = int = 1
            clientObject.relative_setting_of_time_step_for_dynamic_relaxation = double

        # Maximum Number of Iterations
        clientObject.max_number_of_iterations = max_number_of_iterations

        # Number of Load Increments
        clientObject.number_of_load_increments = number_of_load_increments

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
        
        mass_conversion_factor_in_direction_x = mass_conversion_factors[0]
        mass_conversion_factor_in_direction_y = mass_conversion_factors[1]
        mass_conversion_factor_in_direction_z = mass_conversion_factors[2]
        if mass_conversion_enabled != False:
            mass_conversion_factor_in_direction_x =  double
            mass_conversion_acceleration_in_direction_y = double
            mass_conversion_acceleration_in_direction_z = double
        if len(mass_conversion_factors) != 3:
            raise Exception('WARNING: The mass conversion factors parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')    

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
                 max_number_of_iterations: int = 100, 
                 number_of_load_increments: int = 1,
                 load_multiplier_factor : bool = False,
                 multiplier_factor = None,
                 dividing_results = None,
                 favorable_effect_due_to_tension_in_members : bool = False,
                 bourdon_effect: bool = True,
                 nonsymmetric_direct_solver: bool = True,
                 refer_internal_forces_to_deformed_structure : bool = False,
                 internal_forces = [None, None, None]
                 method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                 plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                 mass_conversion_enabled : bool = False,
                 mass_conversion_factors = [None, None, None]
                 comment: str = '',
                 params: dict = {}):  
            
        '''
        Args:
            no (int): 
            name (str, optional): Static Analysis Name
            iterative_method (enum): Static Analysis Settings Iterative Method for Non-linear Analysis Enumeration
            max_number_of_iterations (int): Maximum Number of Iterations
            number_of_load_increments (int): Number of Load Increments
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
            mass_conversion_enabled (bool, optional): 
            mass_conversion_factors (list, optional): [mass_conversion_factor_in_direction_x, mass_conversion_factor_in_direction_y, mass_conversion_factor_in_direction_z]
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


        # Maximum Number of Iterations
        clientObject.max_number_of_iterations = max_number_of_iterations


        # Number of Load Increments
        clientObject.number_of_load_increments = number_of_load_increments


        # Load Multiplier Factor 
        clientObject.modify_loading_by_multiplier_factor = load_multiplier_factor 
        clientObject.number_of_iterations_for_loading_prestress = multiplier_factor
        clientObject.divide_results_by_loading_factor = dividing_results
  
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
        
        mass_conversion_factor_in_direction_x = mass_conversion_factors[0]
        mass_conversion_factor_in_direction_y = mass_conversion_factors[1]
        mass_conversion_factor_in_direction_z = mass_conversion_factors[2]
        if mass_conversion_enabled != False:
            mass_conversion_factor_in_direction_x =  double
            mass_conversion_acceleration_in_direction_y = double
            mass_conversion_acceleration_in_direction_z = double
        if len(mass_conversion_factors) != 3:
            raise Exception('WARNING: The mass conversion factors parameter needs to be of length 3. Kindly check list inputs for completeness and correctness.')    

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        clientModel.service.set_static_analysis_settings(clientObject)
