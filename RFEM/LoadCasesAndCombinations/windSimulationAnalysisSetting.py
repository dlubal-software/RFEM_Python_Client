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
                 calculation_parameters: list = [False, 500, WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON],
                 options: list = [True, False, False, False],
                 advanced_options: list = [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                 residual_pressure: float = 0.001,
                 boundary_layers_value: float = None,
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
                calculation_parameters = [Use Second Order numerical Scheme, Maximum number of Iterations, Turbulence Model]
            options (list): Options List
                options = [Consider Turbulence, Slip Boundary on Bottom Boundary, User Defined Dimensions of Wind Tunnel, Save Solver Data To Continue Calculation]
            advanced_options (list): Relaxation Factors
                advanced_options = [Pressure Field, Velocity field, Turbulence Kinetic Energy, Turbulence dissipation Rate, Specific Turbulence Dissipation Rate,
                    Modified Turbulence kinetic Viscosity, Turbulence Intermittency, Momentum Thickness Reynolds Number]
            residual_pressure (float): Residual Pressure
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
        clientObject.snap_to_model_edges = snap_to_model_edges

        # Boundary Layers
        if boundary_layers_value:
            clientObject.boundary_layers_checked = True
            clientObject.boundary_layers_value = boundary_layers_value
        else:
            clientObject.boundary_layers_checked = False

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

        # Use Second Order numerical Scheme
        clientObject.use_second_order_numerical_scheme = calculation_parameters[0]

        # Maximum number of Iterations
        clientObject.maximum_number_of_iterations = calculation_parameters[1]

        # Turbulence Model
        clientObject.turbulence_model_type = calculation_parameters[2].name

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
                 density: float = 1.25,
                 kinematic_viscosity: float = 0.000015,
                 finite_volume_mesh_density: float = 0.2,
                 calculation_parameters: list = [True, 300, WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON, 0.1],
                 simulation_time: float = None,
                 start_time_for_saving_transient_result: float = None,
                 turbulence_model_type = WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_LES,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        """
        Args:
            no (int): Wind Simulation Analysis Setting Tag
            name (str): User Defined Name
            density (float): Density
            kinematic_viscosity (float): Kinematic Viscosity
            finite_volume_mesh_density (float): Finite Volume Mesh Density
            calculation_parameters (list): Calculation Parameters List
                calculation_parameters = [Use Steady Flow Solver To Calculate Initial Condition, Maximum Number Of Iterations Of Steady Flow Solver, Turbulence Type For Initial Condition, Error Tolerance for Data Compression]
            simulation_time (float): Simulation Time
            start_time_for_saving_transient_result (float): Start Time For Saving Transient Result
            turbulence_model_type (enum): Wind Simulation Analysis Settings Turbulence Model Type Enumeration
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

        # Density
        clientObject.density = density

        # Kinematic Viscosity
        clientObject.kinematic_viscosity = kinematic_viscosity

        # Simulation Type
        clientObject.simulation_type = WindSimulationAnalysisSettingsSimulationType.TRANSIENT_FLOW.name

        # Finite Volume Mesh Density
        clientObject.finite_volume_mesh_density = finite_volume_mesh_density

        # Use steady flow solver to calculate initial condition
        clientObject.steady_flow_from_solver = calculation_parameters[0]

        # Maximum Number of Iterations of steady flow solver
        clientObject.maximum_number_of_iterations = calculation_parameters[1]

        # Turbulence Type For Initial Condition
        clientObject.turbulence_model_type_for_initial_condition = calculation_parameters[2].name

        # Error Tolerance for Data Compression
        clientObject.data_compression_error_tolerance = calculation_parameters[3]

        # User defined simulation time and time steps
        if simulation_time is not None and start_time_for_saving_transient_result is not None:
            clientObject.user_defined_simulation_time = True
            clientObject.simulation_time = simulation_time
            clientObject.start_time_for_saving_transient_result = start_time_for_saving_transient_result

        # Spalart-Allmaras DDES
        clientObject.turbulence_model_type = turbulence_model_type.name

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
