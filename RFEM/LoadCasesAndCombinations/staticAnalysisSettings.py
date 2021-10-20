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
                 bourdon_effect: bool = True,
                 nonsymmetric_direct_solver: bool = True,
                 method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                 plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                 mass_conversion_enabled : bool = False,
                 comment: str = '',
                 params: dict = {}):   

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

        # Load Multiplier Factor  (add a list)
        clientObject.modify_loading_by_multiplier_factor = load_multiplier_factor 
        if load_multiplier_factor != False:
            clientObject.modify_loading_by_multiplier_factor = True 
            clientObject.number_of_iterations_for_loading_prestress: int
            clientObject.divide_results_by_loading_factor = 
            
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
        if mass_conversion_enabled != False:
            clientObject.mass_conversion_factor_in_direction_x =  
            clientObject.mass_conversion_acceleration_in_direction_y =
            clientObject.mass_conversion_acceleration_in_direction_z =

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
                 bourdon_effect: bool = True,
                 nonsymmetric_direct_solver: bool = True,
                 plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                 mass_conversion_enabled : bool = False,
                 comment: str = '',
                 params: dict = {}):  
    
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
            clientObject.relative_setting_of_time_step_for_dynamic_relaxation = 

        # Maximum Number of Iterations
        clientObject.max_number_of_iterations = max_number_of_iterations

        # Number of Load Increments
        clientObject.number_of_load_increments = number_of_load_increments

        # Load Multiplier Factor 
        clientObject.modify_loading_by_multiplier_factor = load_multiplier_factor 
        if load_multiplier_factor != False:
            clientObject.modify_loading_by_multiplier_factor = True 
            clientObject.number_of_iterations_for_loading_prestress = ??
            

        # Bourdon Effect Displacement 
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect 

        # Nonsymetric Direct Solver
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver

        
        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name

        # Mass Conversion
        clientObject.mass_conversion_enabled = mass_conversion_enabled
        if mass_conversion_enabled != False:
            clientObject.mass_conversion_factor_in_direction_x =  
            clientObject.mass_conversion_acceleration_in_direction_y =
            clientObject.mass_conversion_acceleration_in_direction_z =

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
                 max_number_of_iterations: int = 100, 
                 number_of_load_increments: int = 1,
                 load_multiplier_factor : bool = False,
                 favorable_effect_due_to_tension_in_members : bool = False,
                 bourdon_effect: bool = True,
                 nonsymmetric_direct_solver: bool = True,
                 refer_internal_forces_to_deformed_structure : bool = False,
                 method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                 plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                 mass_conversion_enabled : bool = False,
                 comment: str = '',
                 params: dict = {}):  
    
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
        if load_multiplier_factor != False:
            clientObject.modify_loading_by_multiplier_factor = True 
            clientObject.number_of_iterations_for_loading_prestress = ?? 


        # Effect due to Tension in Members
        clientObject.consider_favorable_effect_due_to_tension_in_members = favorable_effect_due_to_tension_in_members

            
        # Bourdon Effect Displacement 
        clientObject.displacements_due_to_bourdon_effect = bourdon_effect 


        # Nonsymetric Direct Solver
        clientObject.nonsymmetric_direct_solver = nonsymmetric_direct_solver


        # Internal Forces to Deformed Structure
        clientObject.refer_internal_forces_to_deformed_structure = refer_internal_forces_to_deformed_structure
        if refer_internal_forces_to_deformed_structure != False:
            clientObject.refer_internal_forces_to_deformed_structure_for_moments = bool 
            clientObject.refer_internal_forces_to_deformed_structure_for_normal_forces = bool
            clientObject.refer_internal_forces_to_deformed_structure_for_shear_forces = bool


        # Equation System
        clientObject.method_of_equation_system = method_of_equation_system.name
        
        # Plate Bending Theory
        clientObject.plate_bending_theory = plate_bending_theory.name

        # Mass Conversion
        clientObject.mass_conversion_enabled = mass_conversion_enabled
        if mass_conversion_enabled != False:
            clientObject.mass_conversion_factor_in_direction_x =  
            clientObject.mass_conversion_acceleration_in_direction_y =
            clientObject.mass_conversion_acceleration_in_direction_z =

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        clientModel.service.set_static_analysis_settings(clientObject)
