#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import NodalSupportType, NodalLoadDirection, DesignSituationType, ActionCategoryType, AddOn
from RFEM.initModel import Model, SetAddonStatus, Calculate_all, closeModel
from RFEM.dataTypes import inf
from RFEM.Results.resultTables import ResultTables
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.AluminumDesign.aluminumSLSConfiguration import AluminumDesignSLSConfigurations
from RFEM.AluminumDesign.aluminumULSConfiguration import AluminumDesignULSConfigurations
from RFEM.TypesForAluminumDesign.aluminumEffectiveLengths import AluminumEffectiveLengths
from RFEM.TimberDesign.timberUltimateConfigurations import TimberDesignUltimateConfigurations
from RFEM.TimberDesign.timberServiceLimitStateConfigurations import TimberDesignServiceLimitStateConfigurations
from RFEM.TypesForTimberDesign.timberEffectiveLengths import TimberEffectiveLengths

if Model.clientModel is None:
    Model()

def test_result_tables_aluminum_design_addon():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, addOn=AddOn.aluminum_design_active, status=True)

    Material(1, 'EN AW-3004 H14 | EN 1999-1-1:2007')

    Section(1, 'L 100x6 | DIN 1028:1994-03 | Ferona')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5, 0.0, 0.0)

    Member(1, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', [0, inf, inf, inf, 0, inf])

    AluminumEffectiveLengths()

    LoadCasesAndCombinations()
    LoadCase.StaticAnalysis(1, 'Self-Weight',analysis_settings_no=1,action_category= ActionCategoryType.ACTION_CATEGORY_PERMANENT_G,self_weight=[True, 0.0, 0.0, 1.0])

    DesignSituation(1, DesignSituationType.DESIGN_SITUATION_TYPE_EQU_PERMANENT_AND_TRANSIENT, True)

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")

    LoadCombination(1, combination_items=[[1,1,0,False]])

    NodalLoad(1, 1, '2', NodalLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 1000)

    AluminumDesignSLSConfigurations()
    AluminumDesignULSConfigurations()

    Model.clientModel.service.finish_modification()

    Calculate_all()

    assert Model.clientModel.service.has_any_results()
    assert ResultTables.AluminumDesignDesignRatiosMembersByDesignSituation()
    assert ResultTables.AluminumDesignDesignRatiosMembersByMember()
    assert ResultTables.AluminumDesignDesignRatiosMembersBySection()

    SetAddonStatus(Model.clientModel, addOn=AddOn.aluminum_design_active, status=False)

def test_result_tables_timber_design_addon():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, addOn=AddOn.timber_design_active, status=True)

    Material(1, 'GL20c')

    Section(1, 'Batten 50/100')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5, 0.0, 0.0)

    Member(1, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', [0, inf, inf, inf, 0, inf])

    TimberEffectiveLengths()

    LoadCasesAndCombinations(params={"current_standard_for_combination_wizard":6517})
    LoadCase.StaticAnalysis(1, 'Self-Weight',analysis_settings_no=1,action_category= ActionCategoryType.ACTION_CATEGORY_PERMANENT_G,self_weight=[True, 0.0, 0.0, 1.0])

    DesignSituation(1, DesignSituationType.DESIGN_SITUATION_TYPE_EQU_PERMANENT_AND_TRANSIENT, True)

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")

    LoadCombination(1, combination_items=[[1,1,0,False]])

    NodalLoad(1, 1, '2', NodalLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 1000)

    TimberDesignUltimateConfigurations()
    TimberDesignServiceLimitStateConfigurations()

    Model.clientModel.service.finish_modification()

    Calculate_all()

    assert Model.clientModel.service.has_any_results()
    assert ResultTables.TimberDesignDesignRatiosMembersByDesignSituation()
    assert ResultTables.TimberDesignDesignRatiosMembersByMember()
    assert ResultTables.TimberDesignDesignRatiosMembersBySection()

    SetAddonStatus(Model.clientModel, addOn=AddOn.timber_design_active, status=False)
    LoadCasesAndCombinations(params={"current_standard_for_combination_wizard":6207})
