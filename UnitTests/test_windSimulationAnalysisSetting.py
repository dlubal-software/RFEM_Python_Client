import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model, SetAddonStatus
from RFEM.enums import WindSimulationAnalysisSettingsSimulationType, WindSimulationAnalysisSettingsMemberLoadDistribution
from RFEM.enums import WindSimulationAnalysisSettingsNumericalSolver, WindSimulationAnalysisSettingsTurbulenceModelType, AddOn
from RFEM.LoadCasesAndCombinations.windSimulationAnalysisSetting import WindSimulationAnalysisSettings

if Model.clientModel is None:
    Model()

def test_WindSimulationAnalysisSettings():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.wind_simulation_active, True)

    # Set Static Analysis Settings
    WindSimulationAnalysisSettings(1, 'Steady Flow', 1.25, 0.000015, WindSimulationAnalysisSettingsMemberLoadDistribution.CONCENTRATED,
                                    0.1, True, [False, False, 500, WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON])
    WindSimulationAnalysisSettings.TransientFlow(2,'Transient Flow', 1.3, 0.00002, 0.3, [True, 250, WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON, 0.03])

    Model.clientModel.service.finish_modification()

    steady_flow =  WindSimulationAnalysisSettings.Get(1)
    assert steady_flow['simulation_type'] == WindSimulationAnalysisSettingsSimulationType.STEADY_FLOW.name
    assert steady_flow['density'] == 1.25
    assert steady_flow['kinematic_viscosity'] == 0.000015
    assert steady_flow['member_load_distribution'] == WindSimulationAnalysisSettingsMemberLoadDistribution.CONCENTRATED.name
    assert steady_flow['numerical_solver'] == WindSimulationAnalysisSettingsNumericalSolver.OPEN_FOAM.name
    assert steady_flow['consider_turbulence'] == True

    transient_flow =  WindSimulationAnalysisSettings.Get(2)
    assert transient_flow['steady_flow_from_solver'] == True
    assert transient_flow['maximum_number_of_iterations'] == 250
    assert transient_flow['turbulence_model_type_for_initial_condition'] == WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON.name
    assert transient_flow['data_compression_error_tolerance'] == 0.03
