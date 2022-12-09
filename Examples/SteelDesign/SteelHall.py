#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import *
from RFEM.initModel import Model, SetAddonStatus, insertSpaces, Calculate_all
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForSteelDesign.steelEffectiveLengths import SteelEffectiveLengths
from RFEM.TypesForSteelDesign.steelBoundaryConditions import SteelBoundaryConditions
from RFEM.TypesForSteelDesign.steelMemberShearPanel import SteelMemberShearPanel
from RFEM.Imperfections.imperfectionCase import ImperfectionCase
from RFEM.Imperfections.memberImperfection import MemberImperfection
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Loads.memberLoad import MemberLoad

if __name__ == '__main__':

    frame_number = 6
    width = 10
    frame_length = 4
    console_height = 3
    column_height = 4
    gable_height = 2

    frame_number = int(input('Number of Frame : '))
    # width = float(input('Width of Frame (in m) : '))
    # frame_length = float(input('Length of Frame (in m) : '))
    # console_height = float(input('Height of console (in m) : '))
    # column_height = float(input('Height of column (in m) : '))
    # gable_height = float(input('Height of Gable (in m) : '))
    console_length = 0.3

    Model(True, 'SteelHall')
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active)
    SetAddonStatus(Model.clientModel, AddOn.steel_design_active)
    Material(1, 'S235')
    Material(2)
    Material(3)
    Section(1, 'IPE 500', 1)
    Section(2, 'IPE 300', 2)
    Section(3, 'R 40', 3)
    i = 0
    for j in range(frame_number):

        y = frame_length * j
        Node(i+1, 0, y, 0)
        Node(i+2, 0, y, -console_height)
        Node(i+3, 0, y, -column_height)
        Node(i+4, width/2, y, -console_height-gable_height)
        Node(i+5, width, y, -column_height)
        Node(i+6, width, y, -console_height)
        Node(i+7, width, y, 0)
        Node(i+8, console_length, y, -console_height)
        Node(i+9, width-console_length, y, -console_height)
        i = i+9

    i, k = 1, 1
    for j in range(frame_number):

        Member(i, k, k+1, 0, 1, 1)
        Member(i+1, k+1, k+2, 0, 1, 1)
        Member(i+2, k+2, k+3, 0, 1, 1)
        Member(i+3, k+3, k+4, 0, 1, 1)
        Member(i+4, k+5, k+4, 0, 1, 1)
        Member(i+5, k+6, k+5, 0, 1, 1)
        Member(i+6, k+1, k+7, 0, 1, 1)
        Member(i+7, k+5, k+8, 0, 1, 1)
        i, k = i+13, k+9

    i, k = 9, 1
    for j in range(frame_number-1):

        m, n, o = i, k+1, k+10
        for l in range(5):
            Member(m, n, o, 0, 2, 2)
            m, n, o = m+1, n+1, o+1
        i, k = i+13, k+9

    bracingV1, bracingV2, bracingV3 = 'None', 'None', 'None'
    bracingV = input('Would you like to include vertical bracing? (Y/N) : ')
    i = frame_number*8 + (frame_number-1)*5
    if bracingV.lower() == 'yes' or bracingV.lower() == 'y':

        bracingV1 = input('Would you like to repeat a vertical bracing in every block? (Y/N): ')

        if bracingV1.lower() == 'yes' or bracingV1.lower() == 'y':
            k = 1
            for j in range(frame_number-1):
                Member.Tension(i+1, k, k+11, section_no= 3)
                Member.Tension(i+2, k+2, k+9, section_no= 3)
                Member.Tension(i+3, k+6, k+13, section_no= 3)
                Member.Tension(i+4, k+4, k+15, section_no= 3)
                i, k = i+4, k+9

        else:
            bracingV2 = input('Would you like to repeat a vertical bracing only in the first and last block? (Y/N): ')

        if bracingV2.lower() == 'yes' or bracingV2.lower() == 'y':
            k = 1
            for j in range(frame_number-1):
                if j in [0, frame_number-2]:
                    Member.Tension(i+1, k, k+11, section_no= 3)
                    Member.Tension(i+2, k+2, k+9, section_no= 3)
                    Member.Tension(i+3, k+6, k+13, section_no= 3)
                    Member.Tension(i+4, k+4, k+15, section_no= 3)
                    i = i+4
                k = k+9
        elif bracingV2.lower() == 'no' or bracingV2.lower() == 'n':
            bracingV3 = input('Would you like to repeat a vertical bracing in even/odd blocks? (E/O/N): ')

        if bracingV3.lower() == 'even' or bracingV3.lower() == 'e':
            k = 1
            for j in range(frame_number-1):
                if j % 2 != 0:
                    Member.Tension(i+1, k, k+11, section_no= 3)
                    Member.Tension(i+2, k+2, k+9, section_no= 3)
                    Member.Tension(i+3, k+6, k+13, section_no= 3)
                    Member.Tension(i+4, k+4, k+15, section_no= 3)
                    i = i + 4
                k = k+9

        elif bracingV3.lower() == 'odd' or bracingV3.lower() == 'o':
            k = 1
            for j in range(frame_number-1):
                if j % 2 == 0:
                    Member.Tension(i+1, k, k+11, section_no= 3)
                    Member.Tension(i+2, k+2, k+9, section_no= 3)
                    Member.Tension(i+3, k+6, k+13, section_no= 3)
                    Member.Tension(i+4, k+4, k+15, section_no= 3)
                    i = i + 4
                k = k+9

    bracingH = input('Would you like to include Horizontal bracing? (Y/N) : ')
    if bracingH.lower() == 'yes' or bracingH.lower() == 'y':

        if bracingV.lower() != 'yes' or bracingV.lower() != 'y':
            k = 1
            for j in range(frame_number-1):
                Member.Tension(i+1, k+2, k+12, section_no= 3)
                Member.Tension(i+2, k+3, k+11, section_no= 3)
                Member.Tension(i+3, k+3, k+13, section_no= 3)
                Member.Tension(i+4, k+4, k+12, section_no= 3)
                i, k = i+4, k+9

        if bracingV1.lower() == 'yes' or bracingV1.lower() == 'y':
            k = 1
            for j in range(frame_number-1):
                Member.Tension(i+1, k+2, k+12, section_no= 3)
                Member.Tension(i+2, k+3, k+11, section_no= 3)
                Member.Tension(i+3, k+3, k+13, section_no= 3)
                Member.Tension(i+4, k+4, k+12, section_no= 3)
                i, k = i+4, k+9

        if bracingV2.lower() == 'yes' or bracingV2.lower() == 'y':
            k = 1
            for j in range(frame_number-1):
                if j in [0, frame_number-2]:
                    Member.Tension(i+1, k+2, k+12, section_no= 3)
                    Member.Tension(i+2, k+3, k+11, section_no= 3)
                    Member.Tension(i+3, k+3, k+13, section_no= 3)
                    Member.Tension(i+4, k+4, k+12, section_no= 3)
                    i = i+4
                k = k+9

        if bracingV3.lower() == 'even' or bracingV3.lower() == 'e':
            k = 1
            for j in range(frame_number-1):
                if j % 2 != 0:
                    Member.Tension(i+1, k+2, k+12, section_no= 3)
                    Member.Tension(i+2, k+3, k+11, section_no= 3)
                    Member.Tension(i+3, k+3, k+13, section_no= 3)
                    Member.Tension(i+4, k+4, k+12, section_no= 3)
                    i = i + 4
                k = k+9

        elif bracingV3.lower() == 'odd' or bracingV3.lower() == 'o':
            k = 1
            for j in range(frame_number-1):
                if j % 2 == 0:
                    Member.Tension(i+1, k+2, k+12, section_no= 3)
                    Member.Tension(i+2, k+3, k+11, section_no= 3)
                    Member.Tension(i+3, k+3, k+13, section_no= 3)
                    Member.Tension(i+4, k+4, k+12, section_no= 3)
                    i = i + 4
                k = k+9

    # Nodal Support
    nodes_no = []
    k = 1
    for j in range(frame_number):
        nodes_no.extend([k, k+6])
        k = k + 9

    NodalSupport(1, insertSpaces(nodes_no), NodalSupportType.HINGED)

    # Imperfections
    ImperfectionCase(1, ImperfectionType.IMPERFECTION_TYPE_LOCAL_IMPERFECTIONS, '4', assign_to_combinations_without_assigned_imperfection_case=True, active= True, params={'user_defined_name_enabled': True, 'name': 'Imp in X'})
    ImperfectionCase(2, ImperfectionType.IMPERFECTION_TYPE_LOCAL_IMPERFECTIONS, '5', assign_to_combinations_without_assigned_imperfection_case=True, active= True, params={'user_defined_name_enabled': True, 'name': 'Imp in Y'})

    # Member Imperfections
    n, k = 0, 0
    for j in range(frame_number):
        MemberImperfection(n+1, 1, str(k+1)+' '+str(k+2)+' '+str(k+5)+' '+str(k+6), MemberImperfectionType.IMPERFECTION_TYPE_INITIAL_SWAY, MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1993_1_1, ImperfectionDirection.IMPERFECTION_DIRECTION_LOCAL_Z, [None, column_height, 2, None, None, None, None])
        MemberImperfection(n+1, 2, str(k+1)+' '+str(k+2)+' '+str(k+5)+' '+str(k+6), MemberImperfectionType.IMPERFECTION_TYPE_INITIAL_SWAY, MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1993_1_1, ImperfectionDirection.IMPERFECTION_DIRECTION_LOCAL_Y, [None, column_height, frame_number, None, None, None, None])
        n, k = n+1, k+13

    # Steel Effective Lengths
    n, k, l = 0, 0, 0
    for j in range(frame_number):
        if j in [0, frame_number-1]:
            SteelEffectiveLengths(n+1, str(k+3), name='SEL'+str(n+1), nodal_supports=[[SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, str(l+3)],
                      [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, str(l+4)]])
            SteelEffectiveLengths(n+2, str(k+4), name='SEL'+str(n+2), nodal_supports=[[SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, str(l+4)],
                      [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, str(l+5)]])
            n = n+2
        k, l = k+13, l+9

    # Steel Boundary Conditions
    n, k = 0, 0
    for j in range(frame_number):
        if j not in [0, frame_number-1]:
            SteelBoundaryConditions(n+1, 'SBC '+str(n+1), str(k+3))
            SteelBoundaryConditions(n+2, 'SBC '+str(n+2), str(k+4))
            n = n+2
        k = k+13

    # Steel Member Shear Panel
    n, k = 0, 0
    for j in range(frame_number):
        SteelMemberShearPanel(n+1, 'SSP '+str(n+1), members=str(k+3), categories=[SteelMemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE, "HSW (-) E 160 - 1.00 (b: 1) | DIN 18807 | Hoesch E", SteelMemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_RIB], parameters=[15, 5, None, None])
        SteelMemberShearPanel(n+2, 'SSP '+str(n+2), members=str(k+4), categories=[SteelMemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE, "HSW (-) E 160 - 1.00 (b: 1) | DIN 18807 | Hoesch E", SteelMemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_RIB], parameters=[15, 5, None, None])
        n, k = n+2, k+13

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
    StaticAnalysisSettings.SecondOrderPDelta(2, "SecondOrder")
    StaticAnalysisSettings.LargeDeformation(3, "LargeDeformation")

    LoadCasesAndCombinations()
    LoadCase.StaticAnalysis(1, 'Self-Weight', True, 1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_G, [True, 0.0, 0.0, 1.0])
    LoadCase.StaticAnalysis(2, 'Live Load', True, 1, ActionCategoryType.ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_H_ROOFS_QI_H, [False])
    LoadCase.StaticAnalysis(3, 'Snow-Load', True, 1, ActionCategoryType.ACTION_CATEGORY_SNOW_ICE_LOADS_H_LESS_OR_EQUAL_TO_1000_M_QS, [False])
    LoadCase.StaticAnalysis(4, 'Wind-Load_x', True, 1, ActionCategoryType.ACTION_CATEGORY_WIND_QW, [False])
    LoadCase.StaticAnalysis(5, 'Wind-Load_y', True, 1, ActionCategoryType.ACTION_CATEGORY_WIND_QW, [False])

    # Manual Load Combinations
    # LoadCombination(1, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,2,0,False]])
    # LoadCombination(2, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,3,0,False]])
    # LoadCombination(3, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,4,0,False]])
    # LoadCombination(4, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,5,0,False]])
    # LoadCombination(5, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,2,0,False],[1,3,0,False],[1,4,0,False]])
    # LoadCombination(6, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,2,0,False],[1,3,0,False],[1,5,0,False]])

    # n,k = 0,0
    # for j in range(frame_number):
    #     MemberLoad(n+1, 1, str(k+3), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 500)
    #     MemberLoad(n+2, 1, str(k+4), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 500)
    #     MemberLoad(n+3, 1, str(k+7), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 500)
    #     MemberLoad(n+4, 1, str(k+8), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 500)
    #     n, k = n+4, k+13

    # k = 0
    # for j in range(frame_number-1):
    #     MemberLoad(n+1, 1, str(k+9), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 500)
    #     MemberLoad(n+2, 1, str(k+10), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 500)
    #     MemberLoad(n+3, 1, str(k+11), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 500)
    #     MemberLoad(n+4, 1, str(k+12), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 500)
    #     MemberLoad(n+5, 1, str(k+13), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 500)
    #     n, k = n+5, k+13

    # Loads for LC2:Live Load
    n, k, l = 0, 0, 0
    for j in range(frame_number):
        MemberLoad(n+1, 2, str(k+3), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 3500)
        MemberLoad(n+2, 2, str(k+4), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 3500)
        NodalLoad.Components(n+1, 2, str(l+8), [0,0,10000,0,0,0])
        NodalLoad.Components(n+2, 2, str(l+9), [0,0,10000,0,0,0])
        n, k, l = n+2, k+13, l+9

    # Loads for LC3:Snow Load
    n, k = 0, 0
    for j in range(frame_number):
        MemberLoad(n+1, 3, str(k+3), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, 1500)
        MemberLoad(n+2, 3, str(k+4), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, 1500)
        n, k = n+2, k+13

    # Loads for LC4:Wind-Load_x
    n, k = 0, 0
    for j in range(frame_number):
        MemberLoad(n+1, 4, str(k+1), LoadDirectionType.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 2000)
        MemberLoad(n+2, 4, str(k+2), LoadDirectionType.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 2000)
        MemberLoad(n+3, 4, str(k+5), LoadDirectionType.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 2000)
        MemberLoad(n+4, 4, str(k+6), LoadDirectionType.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 2000)
        n, k = n+4, k+13

    k = 0
    for j in range(frame_number-1):
        MemberLoad(n+1, 4, str(k+9), LoadDirectionType.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        MemberLoad(n+2, 4, str(k+10), LoadDirectionType.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        MemberLoad(n+3, 4, str(k+11), LoadDirectionType.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        MemberLoad(n+4, 4, str(k+12), LoadDirectionType.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        MemberLoad(n+5, 4, str(k+13), LoadDirectionType.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        n, k = n+5, k+13

    # Loads for LC5:Wind-Load_y
    n, k = 0, 0
    for j in range(frame_number):
        MemberLoad(n+1, 5, str(k+1), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 1500)
        MemberLoad(n+2, 5, str(k+2), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 1500)
        MemberLoad(n+3, 5, str(k+3), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 2500)
        MemberLoad(n+4, 5, str(k+4), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 2500)
        MemberLoad(n+5, 5, str(k+5), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 1500)
        MemberLoad(n+6, 5, str(k+6), LoadDirectionType.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 1500)
        n, k = n+6, k+13

    Model.clientModel.service.finish_modification()

    # Calculate_all()
