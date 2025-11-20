#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation
from RFEM.LoadCasesAndCombinations.modalAnalysisSettings import ModalAnalysisSettings
from RFEM.LoadCasesAndCombinations.spectralAnalysisSettings import SpectralAnalysisSettings
from RFEM.LoadCasesAndCombinations.combinationWizard import CombinationWizard
from RFEM.DynamicLoads.responseSpectrum import ResponseSpectrum
from RFEM.LoadCasesAndCombinations.resultCombination import ResultCombination
from RFEM.enums import DesignSituationType, StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis, StaticAnalysisSettingsMethodOfEquationSystem
from RFEM.enums import StaticAnalysisSettingsPlateBendingTheory, ModalSolutionMethod, ModalMassConversionType, ModalMassMatrixType
from RFEM.enums import ModalNeglectMasses, DirectionalComponentCombinationRule, PeriodicResponseCombinationRule, InitialStateDefintionType
from RFEM.enums import ResultCombinationType, OperatorType, ActionLoadType, ResultCombinationExtremeValueSign


if Model.clientModel is None:
    Model()

def test_design_situation():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    LoadCase()

    LoadCasesAndCombinations(params={"current_standard_for_combination_wizard": 6048,
                                      "combination_wizard_and_classification_active": True,
                                      "combination_wizard_active": True,
                                      "result_combinations_active": True,
                                      "result_combinations_parentheses_active": True,
                                      "result_combinations_consider_sub_results": True,
                                      "combination_name_according_to_action_category": True})

    StaticAnalysisSettings.SecondOrderPDelta(no=1, name="Analyse statique du second ordre",
                                              iterative_method = StaticAnalysisSettingsIterativeMethodForNonlinearAnalysis.NEWTON_RAPHSON,
                                              standard_precision_and_tolerance_settings = [False, 1.0, 1.0, 1.0],
                                              control_nonlinear_analysis = [100, 1],
                                              load_modification = [False, 1, False],
                                              favorable_effect_due_to_tension_in_members=False,
                                              bourdon_effect = False, nonsymmetric_direct_solver = True,
                                              internal_forces_to_deformed_structure = [True, True, True, True],
                                              method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                                              plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                                              mass_conversion = [False, 0, 0, 1])

    StaticAnalysisSettings.GeometricallyLinear(no=2, name="Analyse statique geometriquement lineaire",
                                               load_modification = [False, 1, False],
                                               bourdon_effect = False,
                                               nonsymmetric_direct_solver = False,
                                               method_of_equation_system = StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                                               plate_bending_theory = StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,
                                               mass_conversion = [False, 0, 0, 1])

    ModalAnalysisSettings(no=1, name="Analyse Lanczos 300 Modes",
                          solution_method = ModalSolutionMethod.METHOD_LANCZOS,
                          mass_conversion_type = ModalMassConversionType.MASS_CONVERSION_TYPE_Z_COMPONENTS_OF_LOADS,
                          mass_matrix_type = ModalMassMatrixType.MASS_MATRIX_TYPE_CONSISTENT,
                          number_of_modes = 300,
                          acting_masses=[False, False, False, True, True, False],
                          neglect_masses = ModalNeglectMasses.E_NEGLECT_MASSES_USER_DEFINED)

    SpectralAnalysisSettings(no=1, name='SRSS | SRSS', periodic_combination = PeriodicResponseCombinationRule.SRSS,
                             directional_combination = DirectionalComponentCombinationRule.SRSS,
                             equivalent_linear_combination = False, signed_dominant_mode_results = False)

    ResponseSpectrum(1, user_defined_spectrum=[[0, 0.66], [0.15, 1.66]])

    CombinationWizard(no=1, name = 'Analyse statique du second ordre',
                      static_analysis_settings = 1,
                      stability_analysis_setting = 0,
                      consider_imperfection_case = True,
                      generate_same_CO_without_IC = False,
                      initial_state_cases = [[1,InitialStateDefintionType.DEFINITION_TYPE_FINAL_STATE]],
                      structure_modification = 0)

    CombinationWizard.SetResultCombination(no = 3, name = 'Combinaisons de resultats',
                                           stability_analysis_setting = 0,
                                           consider_imperfection_case = True,
                                           generate_same_CO_without_IC = False,
                                           user_defined_action_combinations = False,
                                           favorable_permanent_actions = False,
                                           generate_subcombinations_of_type_superposition = False)
    #
    ResultCombination(no = 1, design_situation = 4,
                      combination_type = ResultCombinationType.COMBINATION_TYPE_GENERAL,
                      combination_items = [[1, OperatorType.OPERATOR_NONE, 1.0, ActionLoadType.LOAD_TYPE_PERMANENT]],
                      generate_subcombinations = False,
                      srss_combination = [False, ResultCombinationExtremeValueSign.EXTREME_VALUE_SIGN_POSITIVE_OR_NEGATIVE],
                      name = 'Combinaison de resultats sismiques')

    DesignSituation(no = 1, design_situation_type = DesignSituationType.DESIGN_SITUATION_TYPE_STR_PERMANENT_AND_TRANSIENT_6_10, active = True, params = {'combination_wizard': 1})
    DesignSituation(no = 2, design_situation_type = DesignSituationType.DESIGN_SITUATION_TYPE_SLS_CHARACTERISTIC, active = True, params = {'combination_wizard': 1})
    DesignSituation(no = 3, design_situation_type = DesignSituationType.DESIGN_SITUATION_TYPE_SEISMIC_MASS, active = True, params = {'combination_wizard': 1})
    DesignSituation(no = 4, design_situation_type = DesignSituationType.DESIGN_SITUATION_TYPE_STR_SEISMIC, active = True, params = {'combination_wizard': 3})
    DesignSituation(no = 5, design_situation_type = DesignSituationType.DESIGN_SITUATION_TYPE_STR_ACCIDENTAL_PSI_2_1, active = True, params = {'combination_wizard': 1})
    
    Model.clientModel.service.finish_modification()
