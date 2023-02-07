import sys
import os
import pytest

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model, SetAddonStatus, GetAddonStatus
from RFEM.enums import WindSimulationAnalysisSettingsSimulationType, WindSimulationAnalysisSettingsMemberLoadDistribution
from RFEM.enums import WindSimulationAnalysisSettingsNumericalSolver, WindSimulationAnalysisSettingsTurbulenceModelType, AddOn
from RFEM.LoadCasesAndCombinations.windSimulationAnalysisSetting import WindSimulationAnalysisSettings

if Model.clientModel is None:
    Model()

#@pytest.mark.skipif(GetAddonStatus(Model.clientModel, AddOn.wind_simulation_active)==False, reason="wind_simulaion_active add on has to be checked manually")
def test_WindSimulationAnalysisSettings():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.wind_simulation_active, True)

    # Set Static Analysis Settings
    WindSimulationAnalysisSettings(1, 'Steady Flow', 1.25, 0.000015, WindSimulationAnalysisSettingsMemberLoadDistribution.CONCENTRATED,
                                    0.1, True, [False, False, 500, WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON],
                                    [True, False, False, False])
    WindSimulationAnalysisSettings.Transient_Flow(2,'Transient Flow', [True, 250, WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON, 0.03],
                                                    False, 10, 0, WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_LES, [0.01, 1000, 0.01, 1000],
                                                    True, True)
    WindSimulationAnalysisSettings.Surface_Roughness(3, 'Surface Roughness', True, 2.0, 0.500)

    Model.clientModel.service.finish_modification()

    steady_flow = Model.clientModel.service.get_wind_simulation_analysis_settings(1)
    assert steady_flow['simulation_type'] == WindSimulationAnalysisSettingsSimulationType.STEADY_FLOW.name
    assert steady_flow['density'] == 1.25
    assert steady_flow['kinematic_viscosity'] == 0.000015
    assert steady_flow['member_load_distribution'] == WindSimulationAnalysisSettingsMemberLoadDistribution.CONCENTRATED.name
    assert steady_flow['numerical_solver'] == WindSimulationAnalysisSettingsNumericalSolver.OPEN_FOAM.name
    assert steady_flow['consider_turbulence'] == True
    transient_flow = Model.clientModel.service.get_wind_simulation_analysis_settings(2)
    assert transient_flow['steady_flow_from_solver'] == True
    assert transient_flow['maximum_number_of_iterations'] == 250
    assert transient_flow['turbulence_model_type_for_initial_condition'] == WindSimulationAnalysisSettingsTurbulenceModelType.TURBULENCE_TYPE_EPSILON.name
    assert transient_flow['data_compression_error_tolerance'] == 0.03
    assert transient_flow['user_defined_in_point_probes'] == True
    surface_roughness= Model.clientModel.service.get_wind_simulation_analysis_settings(3)
    assert surface_roughness['consider_surface_roughness'] == True

