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
from RFEM.initModel import Calculate_all, Model, SetAddonStatus, insertSpaces
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.crossSection import CrossSection
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForSteelDesign.steelEffectiveLengths import SteelEffectiveLengths
from RFEM.SteelDesign.steelUltimateConfigurations import SteelDesignUltimateConfigurations
from RFEM.Imperfections.imperfectionCase import ImperfectionCase
from RFEM.Imperfections.memberImperfection import MemberImperfection
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Loads.memberLoad import MemberLoad

if __name__ == '__main__':

    frame_number = 6
    width = 10
    frame_length = 4
    console_height = 3
    column_height = 4
    gable_height = 2

    print('Give a integer as a number of frame!')
    frame_number = int(input('Number of frames : '))
    width = float(input('Frame width(in m) : '))
    print('Frame length is the distance between the each frame!')
    frame_length = float(input('Frame length(in m) : '))
    console_height = float(input('Console height(in m) : '))
    print('Column height msut be more than console height!')
    column_height = float(input('Column height(in m) : '))
    print('Gable height must be more than difference of column height and console height!')
    gable_height = float(input('Gable Height(in m) : '))
    console_length = 0.3

    Model(True, 'SteelHall.rf6', True)

    Model.clientModel.service.begin_modification()
    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active)
    SetAddonStatus(Model.clientModel, AddOn.steel_design_active)
    Material(1, 'S235')
    Material(2)
    Material(3)
    CrossSection(1, 'HEA 220', 1)
    CrossSection(2, 'IPE 160', 2)
    CrossSection(3, 'R 30', 3)
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

    bracingH = input('Would you like to include horizontal bracing? (Y/N) : ')
    if bracingH.lower() == 'yes' or bracingH.lower() == 'y':

        if bracingV.lower() != 'yes' and bracingV.lower() != 'y':
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
        SteelEffectiveLengths(n+3, str(k+1)+' '+str(k+2)+' '+str(k+5)+' '+str(k+6)+' '+str(k+7)+' '+str(k+8), name='SEL'+str(n+3), nodal_supports=[[SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, str(l+1)+' '+str(l+2)+' '+str(l+5)+' '+str(l+6)+' '+str(l+2)+' '+str(l+6)],
                      [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, str(l+2)+' '+str(l+3)+' '+str(l+6)+' '+str(l+7)+' '+str(l+8)+' '+str(l+9)]])
        n, k, l = n+3, k+13, l+9

    k, l = 0, 0
    for j in range(frame_number-1):
        SteelEffectiveLengths(n+1, str(k+9)+' '+str(k+10)+' '+str(k+11)+' '+str(k+12)+' '+str(k+13), name='SEL'+str(n+1), nodal_supports=[[SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, str(l+2)+' '+str(l+3)+' '+str(l+4)+' '+str(l+5)+' '+str(l+6)],
                      [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, str(l+11)+' '+str(l+12)+' '+str(l+13)+' '+str(l+14)+' '+str(l+15)]])
        n, k, l = n+1, k+13, l+9

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
    StaticAnalysisSettings.SecondOrderPDelta(2, "SecondOrder")
    StaticAnalysisSettings.LargeDeformation(3, "LargeDeformation")

    # Load Cases and Combinations
    LoadCasesAndCombinations()
    LoadCase.StaticAnalysis(1, 'Self-Weight', True, 1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_G, [True, 0.0, 0.0, 1.0])
    LoadCase.StaticAnalysis(2, 'Live Load', True, 1, ActionCategoryType.ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_H_ROOFS_QI_H, [False])
    LoadCase.StaticAnalysis(3, 'Snow-Load', True, 1, ActionCategoryType.ACTION_CATEGORY_SNOW_ICE_LOADS_H_LESS_OR_EQUAL_TO_1000_M_QS, [False])
    LoadCase.StaticAnalysis(4, 'Wind-Load_x', True, 1, ActionCategoryType.ACTION_CATEGORY_WIND_QW, [False])
    LoadCase.StaticAnalysis(5, 'Wind-Load_y', True, 1, ActionCategoryType.ACTION_CATEGORY_WIND_QW, [False])

    # Loads for LC2:Live Load
    n, k, l = 0, 0, 0
    for j in range(frame_number):
        MemberLoad(n+1, 2, str(k+3), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 3500)
        MemberLoad(n+2, 2, str(k+4), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 3500)
        NodalLoad.Components(n+1, 2, str(l+8), [0,0,10000,0,0,0])
        NodalLoad.Components(n+2, 2, str(l+9), [0,0,10000,0,0,0])
        n, k, l = n+2, k+13, l+9

    # Loads for LC3:Snow Load
    n, k = 0, 0
    for j in range(frame_number):
        MemberLoad(n+1, 3, str(k+3), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, 1500)
        MemberLoad(n+2, 3, str(k+4), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, 1500)
        n, k = n+2, k+13

    # Loads for LC4:Wind-Load_x
    n, k = 0, 0
    for j in range(frame_number):
        MemberLoad(n+1, 4, str(k+1), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 2000)
        MemberLoad(n+2, 4, str(k+2), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 2000)
        MemberLoad(n+3, 4, str(k+5), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 2000)
        MemberLoad(n+4, 4, str(k+6), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 2000)
        n, k = n+4, k+13

    k = 0
    for j in range(frame_number-1):
        MemberLoad(n+1, 4, str(k+9), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        MemberLoad(n+2, 4, str(k+10), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        MemberLoad(n+3, 4, str(k+11), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        MemberLoad(n+4, 4, str(k+12), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        MemberLoad(n+5, 4, str(k+13), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 1500)
        n, k = n+5, k+13

    # Loads for LC5:Wind-Load_y
    n, k = 0, 0
    for j in range(frame_number):
        MemberLoad(n+1, 5, str(k+1), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 1500)
        MemberLoad(n+2, 5, str(k+2), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 1500)
        MemberLoad(n+3, 5, str(k+3), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 2500)
        MemberLoad(n+4, 5, str(k+4), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 2500)
        MemberLoad(n+5, 5, str(k+5), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 1500)
        MemberLoad(n+6, 5, str(k+6), MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE, 1500)
        n, k = n+6, k+13

    SteelDesignUltimateConfigurations(1, 'ULS1', 'All')

    Model.clientModel.service.finish_modification()
    Model.clientModel.service.generate_load_cases_and_combinations()
    Calculate_all()
