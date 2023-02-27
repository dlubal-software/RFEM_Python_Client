from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import WindSimulationAnalysisSettingsSimulationType
from RFEM.enums import WindSimulationAnalysisSettingsMemberLoadDistribution
from RFEM.enums import WindSimulationAnalysisSettingsMeshRefinementType
from RFEM.enums import WindSimulationAnalysisSettingsNumericalSolver
from RFEM.enums import WindSimulationAnalysisSettingsTurbulenceModelType


class WindSimulationAnalysisSettings():

    def __init__(self,
                 no: int = 1,
                 name: str = None,
                 density: float = 1.25,
                 kinematic_viscosity: float = 0.000015,
                 member_load_distribution = WindSimulationAnalysisSettingsMemberLoadDistribution.CONCENTRATED,
                 finite_volume_mesh_density: float = 0.2,
                 snap_to_model_edges: bool = True,
                 calculation_parameters: list = [False, False, 500, WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON],
                 options: list = [True, False, False, False],
                 advanced_options: list = [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                 residual_pressure: float = 0.001,
                 boundary_layers_checked: bool = False,
                 boundary_layers_value: float = 5.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Wind Simulation Analysis Setting Tag
            name (str): User Defined Name
            density (float): Density
            kinematic_viscosity (float): Kinematic Viscosity
            member_load_distribution (enum): Wind Simulation Analysis Settings Member Load Distribution Enumeration
            finite_volume_mesh_density (float): Finite Volume Mesh Density
            snap_to_model_edges (bool): Enable/disable Snap to Model Edges
            calculation_parameters (list): Calculation Parameters List
                calculation_parameters = [Use Potential Flow to calculate initial Condition, Use Second Order numerical Scheme, Maximum number of Iterations, Turbulence Model]
            options (list): Options List
                options = [Consider Turbulence, Slip Boundary on Bottom Boundary, User Defined Dimensions of Wind Tunnel, Save Solver Data To Continue Calculation]
            advanced_options (list): Relaxation Factors
                advanced_options = [Pressure Field, Velocity field, Turbulence Kinetic Energy, Turbulence dissipation Rate, Specific Turbulence Dissipation Rate,
                    Modified Turbulence kinetic Viscosity, Turbulence Intermittency, Momentum Thickness Reynolds Number]
            residual_pressure (float): Residual Pressure
            boundary_layers_checked (bool): Enable/disable Boundary Layers Checked
            boundary_layers_value (float): Boundary Layers Value
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface
        clientObject = model.clientModel.factory.create('ns0:wind_simulation_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Wind Simulation Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Simulation Type
        clientObject.simulation_type = WindSimulationAnalysisSettingsSimulationType.STEADY_FLOW.name

        # Density
        clientObject.density = density

        # Kinematic Viscosity
        clientObject.kinematic_viscosity = kinematic_viscosity

        # Numerical Solver
        clientObject.numerical_solver = WindSimulationAnalysisSettingsNumericalSolver.OPEN_FOAM.name

        # Finite Volume Mesh Density
        clientObject.finite_volume_mesh_density = finite_volume_mesh_density

        # Mesh Refinement Type
        clientObject.mesh_refinement_type = WindSimulationAnalysisSettingsMeshRefinementType.DISTANCE_FROM_SURFACE.name

        # Snap to model edges
        clientObject.snap_to_model_edges=snap_to_model_edges

        # Boundary Layers
        clientObject.boundary_layers_checked = boundary_layers_checked
        if boundary_layers_checked:
            clientObject.boundary_layers_value = boundary_layers_value

        # Consider Turbulence
        clientObject.consider_turbulence = options[0]

        # "Slip" Boundary Condition
        clientObject.slip_boundary_condition_on_bottom_boundary = options[1]

        # User-Defined Dimensions of Wind Tunnel
        clientObject.user_defined_dimensions_of_wind_tunnel = options[2]

        # Save Solver Data to continue Calculation
        clientObject.save_solver_data_to_continue_calculation = options[3]

        # Member Load Distribution
        clientObject.member_load_distribution = member_load_distribution.name

        # Use Potential Flow to calculate initial Condition
        clientObject.use_potential_flow_for_initial_condition = calculation_parameters[0]

        # Use Second Order numerical Scheme
        clientObject.use_second_order_numerical_scheme = calculation_parameters[1]

        # Maximum number of Iterations
        clientObject.maximum_number_of_iterations = calculation_parameters[2]

        # Turbulence Model
        clientObject.turbulence_model_type = calculation_parameters[3].name

        # Pressure Field
        clientObject.pressure_field = advanced_options[0]

        # Velocity field
        clientObject.velocity_field = advanced_options[1]

        # turbulence kinetic energy
        clientObject.turbulence_kinetic_energy = advanced_options[2]

        # Turbulence dissipation Rate
        clientObject.turbulence_dissipation_rate = advanced_options[3]

        # Specific Turbulence Dissipation Rate
        clientObject.specific_turbulence_dissipation_rate = advanced_options[4]

        # Modified Turbulence kinetic Viscosity
        clientObject.turbulence_kinetic_viscosity = advanced_options[5]

        # Turbulence Intermittency
        clientObject.turbulence_intermittency = advanced_options[6]

        # Momentum Thickness Reynolds Number
        clientObject.momentum_thickness_reynolds_number = advanced_options[7]

        # Residual Pressure
        clientObject.residual_pressure = residual_pressure

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Wind Simulation Analysis Settings to client model
        model.clientModel.service.set_wind_simulation_analysis_settings(clientObject)


    @staticmethod
    def TransientFlow(
                 no: int = 1,
                 name: str = None,
                 calculation_parameters: list = [True, 300, WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON, 0.1],
                 user_defined_simulation_time: bool = False,
                 simulation_time: float = 10.0,
                 start_time_for_saving_transient_result: float = 0.0,
                 turbulence_model_type = WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_LES,
                 saving_results: list = [0.01, 1000, 0.01, 1000],
                 user_defined_in_domain_for_flow_animation: bool = True,
                 user_defined_in_point_probes: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        """
        Args:
            no (int): Wind Simulation Analysis Setting Tag
            name (str): User Defined Name
            calculation_parameters (list): Calculation Parameters List
                calculation_parameters = [Use Steady Flow Solver To Calculate Initial Condition, Maximum Number Of Iterations Of Steady Flow Solver, Turbulence Type For Initial Condition, Error Tolerance for Data Compression]
            user_defined_simulation_time (bool): Enable/disable User defined simulation time and time steps
            simulation_time (flaot): Simulation Time
            start_time_for_saving_transient_result (float): Start Time For Saving Transient Result
            turbulence_model_type (enums): Wind Simulation Analysis Settings Turbulence Model Type
            saving_results (list): Saving Results
                saving_results = [Transient Flow Time Step For Animation, Transient Flow Number Of Time Layers, Transient Flow Time Step Probes, Transient Flow Number Of Time Layers Probes]
            user_defined_in_domain_for_flow_animation (bool): Enable/disable User Defined In Domain For Flow Animation
            user_defined_in_point_probes (bool): Enable/disable User Defined In Point Probes
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited

        """

        # Client model | Surface
        clientObject = model.clientModel.factory.create('ns0:wind_simulation_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Wind Simulation Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Simulation Type
        clientObject.simulation_type = WindSimulationAnalysisSettingsSimulationType.TRANSIENT_FLOW.name

        # Use steady flow solver to calculate initial condition
        clientObject.steady_flow_from_solver = calculation_parameters[0]

        # Maximum Number of Iterations of steady flow solver
        clientObject.maximum_number_of_iterations = calculation_parameters[1]

        # Turbulence Type For Initial Condition
        clientObject.turbulence_model_type_for_initial_condition = calculation_parameters[2].name

        # Error Tolerance for Data Compression
        clientObject.data_compression_error_tolerance = calculation_parameters[3]

        # User defined simulation time and time steps
        clientObject.user_defined_simulation_time = user_defined_simulation_time
        if user_defined_simulation_time:
            clientObject.simulation_time = simulation_time
            clientObject.start_time_for_saving_transient_result=start_time_for_saving_transient_result

        # Spalart-Allmaras DDES
        clientObject.turbulence_model_type = turbulence_model_type.name

        # in domain for Flow Animation
        clientObject.user_defined_in_domain_for_flow_animation = user_defined_in_domain_for_flow_animation
        if user_defined_simulation_time and user_defined_in_domain_for_flow_animation:
            clientObject.transient_flow_time_step_for_animation = saving_results[1]
            clientObject.transient_flow_number_of_time_layers = saving_results[2]

        # in Probe points for graphics
        clientObject.user_defined_in_point_probes = user_defined_in_point_probes
        if user_defined_simulation_time and user_defined_in_point_probes:
            clientObject.transient_flow_time_step_probes = saving_results[3]
            clientObject.transient_flow_number_of_time_layers_probes = saving_results[4]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Wind Simulation Analysis Settings to client model
        model.clientModel.service.set_wind_simulation_analysis_settings(clientObject)


    @staticmethod
    def SurfaceRoughness(
                 no: int = 1,
                 name: str = None,
                 consider_surface_roughness: bool = False,
                 sand_grain_roughness_height: float = 2.0,
                 roughness_constant: float = 0.5,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        """
        Args:
            no (int): Wind Simulation Analysis Setting Tag
            name (str): User Defined Name
            consider_surface_roughness (bool): Enable/disable Surface Roughness
            sand_grain_roughness_height (float): Sand Grain Roughness Height
            roughness_constant (float): Roughness Constant
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited

        """

        # Client model | Surface
        clientObject = model.clientModel.factory.create('ns0:wind_simulation_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Wind Simulation Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Consider Surface Roughness
        clientObject.consider_surface_roughness = consider_surface_roughness
        if consider_surface_roughness:
            clientObject.sand_grain_roughness_height = sand_grain_roughness_height
            clientObject.roughness_constant = roughness_constant

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Wind Simulation Analysis Settings to client model
        model.clientModel.service.set_wind_simulation_analysis_settings(clientObject)


