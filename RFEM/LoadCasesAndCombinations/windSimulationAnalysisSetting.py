from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import WindSimulationAnalysisSettingsSimulationType
from RFEM.enums import WindSimulationAnalysisSettingsMemberLoadDistribution
from RFEM.enums import WindSimulationAnalysisSettingsMeshRefinementType
from RFEM.enums import WindSimulationAnalysisSettingsNumericalSolver
from RFEM.enums import WindSimulationAnalysisSettingsTurbulenceModelType



class WindSimulaionAnalysisSettings():


    def __init__(self,
                 no: int = 1,
                 name: str = None,
                 simulation_type= WindSimulationAnalysisSettingsSimulationType.STEADY_FLOW,
                 density: float = 1.25,
                 kinematic_viscosity: float = 0.000015,
                 member_load_distribution = WindSimulationAnalysisSettingsMemberLoadDistribution.CONCENTRATED,
                 numerical_solver = WindSimulationAnalysisSettingsNumericalSolver.OPEN_FOAM,
                 finite_volume_mesh_density: float = 20.00,
                 turbulence_model = WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON,
                 maximum_number_of_iterations: float = 500,
                 mesh_refinement = WindSimulationAnalysisSettingsMeshRefinementType.DISTANCE_FROM_SURFACE,
                 consider_turbulence: bool = True,
                 slip_boundary_on_bottom_boundary: bool=False,
                 user_defined_dimensions_of_wind_tunnel: bool = False,

                 use_potential_flow_for_initial_condition: bool=False,
                 use_second_order_numerical_scheme: bool=False,
                 save_solver_data_to_continue_calculation: bool=False,

                 boundary_layers_checked: bool=False,
                 boundary_layers_value: float = 5,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Wind Simulation Analysis Setting Tag
            name (str): Wind Simulation Analysis Setting Name
            simulation_type (enum): Simulation Type Enumeration
            member_load_distribution (enum): Member Load Distribution Enumeration
            numerical_solver (enum): Numerical Solver Enumeration
            mesh_refinement (enum): Mesh Refinement Enumeration
            turbulence_model (enum): Turbulence Model Enumeration
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
        clientObject.simulation_type = simulation_type.name

        # Density
        clientObject.density = density

        # Member Load Distribution
        clientObject.member_load_distribution = member_load_distribution.name

        # Numerical Solver
        clientObject.numerical_solver = numerical_solver.name

        # Finite Volume Mesh Density
        clientObject.finite_volume_mesh_density = finite_volume_mesh_density

        # Mesh Refinement
        clientObject.mesh_refinement = mesh_refinement

        # Consider Turbulence
        clientObject.consider_turbulence = consider_turbulence

        # "Slip" Bounday Condition
        clientObject.slip_boundary_on_bottom_boundary = slip_boundary_on_bottom_boundary



        # User-Defined Dimensions of Wind Tunnel
        clientObject.user_defined_dimensions_of_wind_tunnel = user_defined_dimensions_of_wind_tunnel

        # Save Solver Data to continue Calculation
        clientObject.save_solver_data_to_continue_calculation = save_solver_data_to_continue_calculation

        # Boundary Layers
        clientObject.boundary_layers_checked = boundary_layers_checked
        if boundary_layers_checked == True:
            clientObject.boundary_layers_value = boundary_layers_value

        # Use Potential Flow to calculate initial Condition
        clientObject.use_potential_flow_for_initial_condition = use_potential_flow_for_initial_condition

        # Use Second Order numerical Scheme
        clientObject.use_second_order_numerical_scheme = use_second_order_numerical_scheme

        # Maximum number of Iterations

        # Turbulence Model
        clientObject.turbulence_model = turbulence_model


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
    def Transient_Flow(self,
                 no: int = 1,
                 name: str = None,
                 simulation_type= WindSimulationAnalysisSettingsSimulationType.TRANSIENT_FLOW,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

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
        clientObject.simulation_type = simulation_type.name

        # Maximum Numer of Iterations of steady flow solver
        # User defined simulation time and time steps
        # ...


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
    def Surface_Roughness(self,
                 no: int = 1,
                 name: str = None,
                 consider_surface_roughness: bool=False,
                 sand_grain_roughness_height: float=2.0,
                 roughness_constant: float=0.500,
                 comment: str = '',
                 params: dict = None,
                 model = Model):


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
        if consider_surface_roughness==True:
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


