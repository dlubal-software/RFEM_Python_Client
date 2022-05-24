import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model
from RFEM.enums import StaticAnalysisType, StaticAnalysisSettingsMethodOfEquationSystem, StaticAnalysisSettingsPlateBendingTheory
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings

if Model.clientModel is None:
    Model()

def test_StaticAnalysisSettings():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Set Static Analysis Settings
    StaticAnalysisSettings(1, 'Geometrisch-linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    StaticAnalysisSettings.GeometricallyLinear(2,'Geometric-linear',[True, 1.5, True],True,True,
                                               StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_ITERATIVE,
                                               StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_KIRCHHOFF,[True,0,0,2.0])
    StaticAnalysisSettings.LargeDeformation(3,standard_precision_and_tolerance_settings = [True, 0.02, 0.02, 2.0])
    StaticAnalysisSettings.SecondOrderPDelta(4)

    Model.clientModel.service.finish_modification()

    linear = Model.clientModel.service.get_static_analysis_settings(2)
    assert linear['modify_loading_by_multiplier_factor'] == True
    # TODO: bug 26685
    assert linear['loading_multiplier_factor'] == 1.5
    assert linear['divide_results_by_loading_factor'] == True
    largeDef= Model.clientModel.service.get_static_analysis_settings(3)
    assert largeDef['standard_precision_and_tolerance_settings_enabled'] == True
    # TODO: bug 26685
    assert largeDef['precision_of_convergence_criteria_for_nonlinear_calculation'] == 0.02
    assert largeDef['instability_detection_tolerance'] == 0.02
    assert largeDef['iterative_calculation_robustness'] == 2.0
    secondOrder = Model.clientModel.service.get_static_analysis_settings(4)
    assert secondOrder['analysis_type'] == StaticAnalysisType.SECOND_ORDER_P_DELTA.name
