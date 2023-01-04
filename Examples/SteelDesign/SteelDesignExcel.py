import xlwings as xw
import numpy as np
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
from RFEM.SteelDesign.steelUltimateConfigurations import SteelDesignUltimateConfigurations
from RFEM.Imperfections.imperfectionCase import ImperfectionCase
from RFEM.Imperfections.memberImperfection import MemberImperfection
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Results.resultTables import ResultTables, GetMaxValue, ConvertResultsToListOfDct
from RFEM.Results.designOverview import GetDesignOverview

#if __name__ == '__main__':
def main():

    # open the excel sheet
    wb = xw.Book.caller()

    # read inputs
    inputSheet = wb.sheets('Inputs')

    frame_number = 6
    width = 10
    frame_length = 4
    console_height = 3
    column_height = 4
    gable_height = 2

    # frame_number = int(input('Number of Frame : '))
    # width = float(input('Width of Frame (in m) : '))
    # frame_length = float(input('Length of Frame (in m) : '))
    # console_height = float(input('Height of console (in m) : '))
    # column_height = float(input('Height of column (in m) : '))
    # gable_height = float(input('Height of Gable (in m) : '))
    frame_number = int(inputSheet["G6"].value)  # number of frames
    width = inputSheet["G7"].value
    frame_length = inputSheet["G8"].value
    console_height = inputSheet["G9"].value
    column_height = inputSheet["G10"].value
    gable_height = inputSheet["G11"].value
    console_length = 0.3

    # verticalBracing = 'Every Blocks'
    # horizontalBracing = 'Yes'
    verticalBracing = inputSheet["K6:K8"].value[0]
    horizontalBracing = inputSheet["K9:K11"].value[0]

    column_mat = str(inputSheet["H15:I15"].value[0])
    beam_mat = str(inputSheet["H16:I16"].value[0])
    bracing_mat = str(inputSheet["H17:I17"].value[0])
    column = str(inputSheet["J15:K15"].value[0])
    beam = str(inputSheet["J16:K16"].value[0])
    bracing = str(inputSheet["J17:K17"].value[0])

    bracingV1, bracingV2, bracingV3 = 'None', 'None', 'None'

    if verticalBracing.lower != 'no':
        bracingV = 'yes'

        if verticalBracing == 'Every Blocks':
            bracingV1 = 'yes'

        elif verticalBracing == 'First and Last only':
            bracingV2 = 'yes'

        elif verticalBracing == 'Even Blocks':
            bracingV3 = 'even'

        elif verticalBracing == 'Odd Blocks':
            bracingV3 = 'odd'

    else:
        bracingV = 'no'

    if horizontalBracing == 'Yes':
        bracingH = 'yes'

    else:
        bracingH = 'no'

    Model(True, 'SteelHall', )
    Model.clientModel.service.begin_modification()

    print("Preparing...")
    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active)
    SetAddonStatus(Model.clientModel, AddOn.steel_design_active)
    Material(1, column_mat)
    Material(2, beam_mat)
    Material(3, bracing_mat)
    Section(1, column, 1)
    Section(2, beam, 2)
    Section(3, bracing, 3)
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
    nodes = i

    i, k = 1, 1
    for j in range(frame_number):

        Member(i, k, k+1, 0, 1, 1)
        Member(i+1, k+1, k+2, 0, 1, 1)
        Member(i+2, k+2, k+3, 0, 2, 2)
        Member(i+3, k+3, k+4, 0, 2, 2)
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


    #bracingV = input('Would you like to include vertical bracing? (Y/N) : ')
    i = frame_number*8 + (frame_number-1)*5
    beam_column = i
    if bracingV.lower() == 'yes' or bracingV.lower() == 'y':

        #bracingV1 = input('Would you like to repeat a vertical bracing in every block? (Y/N): ')

        if bracingV1.lower() == 'yes' or bracingV1.lower() == 'y':
            k = 1
            for j in range(frame_number-1):
                Member.Tension(i+1, k, k+11, section_no= 3)
                Member.Tension(i+2, k+2, k+9, section_no= 3)
                Member.Tension(i+3, k+6, k+13, section_no= 3)
                Member.Tension(i+4, k+4, k+15, section_no= 3)
                i, k = i+4, k+9

        # else:
        #     bracingV2 = input('Would you like to repeat a vertical bracing only in the first and last block? (Y/N): ')

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
        # elif bracingV2.lower() == 'no' or bracingV2.lower() == 'n':
        #     bracingV3 = input('Would you like to repeat a vertical bracing in even/odd blocks? (E/O/N): ')

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

    # bracingH = input('Would you like to include Horizontal bracing? (Y/N) : ')
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
    # Steel Boundary Conditions
    # n, k = 0, 0
    # for j in range(frame_number):
    #     if j not in [0, frame_number-1]:
    #         SteelBoundaryConditions(n+1, 'SBC '+str(n+1), str(k+3))
    #         SteelBoundaryConditions(n+2, 'SBC '+str(n+2), str(k+4))
    #         n = n+2
    #     k = k+13

    # Steel Member Shear Panel
    # n, k = 0, 0
    # for j in range(frame_number):
    #     SteelMemberShearPanel(n+1, 'SSP '+str(n+1), members=str(k+3), categories=[SteelMemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE, "HSW (-) E 160 - 1.00 (b: 1) | DIN 18807 | Hoesch E", SteelMemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_RIB], parameters=[15, 5, None, None])
    #     SteelMemberShearPanel(n+2, 'SSP '+str(n+2), members=str(k+4), categories=[SteelMemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE, "HSW (-) E 160 - 1.00 (b: 1) | DIN 18807 | Hoesch E", SteelMemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_RIB], parameters=[15, 5, None, None])
    #     n, k = n+2, k+13

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

    SteelDesignUltimateConfigurations(1, 'ULS1', 'All')

    print('Model Created!')

    Model.clientModel.service.finish_modification()

    print("Calculation started...")
    Calculate_all()
    print("Done!")

    # write outputs
    nodaldeformation = wb.sheets['Nodal Deformation']
    nodalsupport = wb.sheets['Nodal Support']
    deformationSheet = wb.sheets['Member Deformation']
    InternalForceSheet = wb.sheets['Internal Force']

    node_number, nodeSupportType, nodesupType = [], [], []
    nodeDisp_abs, nodeDisp_x, nodeDisp_y, nodeDisp_z = [], [], [], []
    nodeRotation_x, nodeRotation_y, nodeRotation_z = [], [], []
    nodeSupportForce_x, nodeSupportForce_y, nodeSupportForce_z = [], [], []
    nodeMoment_x, nodeMoment_y, nodeMoment_z = [], [], []

    for j in range(nodes):
        dispTab = ResultTables.NodesDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 7, j+1)
        nodisp_abs = GetMaxValue(dispTab, 'displacement_absolute') * 1000
        nodisp_x = GetMaxValue(dispTab, 'displacement_x') * 1000
        nodisp_y = GetMaxValue(dispTab, 'displacement_y') * 1000
        nodisp_z = GetMaxValue(dispTab, 'displacement_z') * 1000
        nodeRot_x = GetMaxValue(dispTab, 'rotation_x') * 1000
        nodeRot_y = GetMaxValue(dispTab, 'rotation_y') * 1000
        nodeRot_z = GetMaxValue(dispTab, 'rotation_z') * 1000
        node_number.append(j+1)
        nodeDisp_abs.append(round(nodisp_abs, 3))
        nodeDisp_x.append(round(nodisp_x, 3))
        nodeDisp_y.append(round(nodisp_y, 3))
        nodeDisp_z.append(round(nodisp_z, 3))
        nodeRotation_x.append(round(nodeRot_x, 3))
        nodeRotation_y.append(round(nodeRot_y, 3))
        nodeRotation_z.append(round(nodeRot_z, 3))

        nodeType = '-'
        if (j+1) in nodes_no:
            nodeType = 'Hinged'
            nodesupforce_x = GetMaxValue(dispTab, 'support_forces_p_x')
            nodesupforce_y = GetMaxValue(dispTab, 'support_forces_p_y')
            nodesupforce_z = GetMaxValue(dispTab, 'support_forces_p_z')
            nodemom_x = GetMaxValue(dispTab, 'support_moments_m_x')
            nodemom_y = GetMaxValue(dispTab, 'support_moments_m_y')
            nodemom_z = GetMaxValue(dispTab, 'support_moments_m_z')
            nodeSupportForce_x.append(round(nodesupforce_x, 3))
            nodeSupportForce_y.append(round(nodesupforce_y, 3))
            nodeSupportForce_z.append(round(nodesupforce_z, 3))
            nodeMoment_x.append(round(nodemom_x, 3))
            nodeMoment_y.append(round(nodemom_y, 3))
            nodeMoment_z.append(round(nodemom_z, 3))
            nodesupType.append(nodeType)

        nodeSupportType.append(nodeType)

    node_number = np.array([node_number]).T
    nodeSupportType = np.array([nodeSupportType]).T
    nodeDisp_abs = np.array([nodeDisp_abs]).T
    nodeDisp_x = np.array([nodeDisp_x]).T
    nodeDisp_y = np.array([nodeDisp_y]).T
    nodeDisp_z = np.array([nodeDisp_z]).T
    nodeRotation_x = np.array([nodeRotation_x]).T
    nodeRotation_y = np.array([nodeRotation_y]).T
    nodeRotation_z = np.array([nodeRotation_z]).T

    nodes_no = np.array([nodes_no]).T
    nodesupType = np.array([nodesupType]).T
    nodeSupportForce_x = np.array([nodeSupportForce_x]).T
    nodeSupportForce_y = np.array([nodeSupportForce_y]).T
    nodeSupportForce_z = np.array([nodeSupportForce_z]).T
    nodeMoment_x = np.array([nodeMoment_x]).T
    nodeMoment_y = np.array([nodeMoment_y]).T
    nodeMoment_z = np.array([nodeMoment_z]).T


    maxDisplacement_abs, maxDisplacement_x, maxDisplacement_y, maxDisplacement_z = [], [], [], []
    maxForce_n, maxForce_vy, maxForce_vz, maxMoment_mt, maxMoment_my, maxMoment_mz = [], [], [], [], [], []
    k = 1
    for j in range(beam_column):
        dispTable = ResultTables.MembersLocalDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 7, object_no=k)
        maxDisp_abs = GetMaxValue(dispTable, 'displacement_absolute') * 1000
        maxDisp_x = GetMaxValue(dispTable, 'displacement_x') * 1000
        maxDisp_y = GetMaxValue(dispTable, 'displacement_y') * 1000
        maxDisp_z = GetMaxValue(dispTable, 'displacement_z') * 1000
        maxDisplacement_abs.append(round(maxDisp_abs, 3))
        maxDisplacement_x.append(round(maxDisp_x, 3))
        maxDisplacement_y.append(round(maxDisp_y, 3))
        maxDisplacement_z.append(round(maxDisp_z, 3))

        momentTable = ResultTables.MembersInternalForces(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 7, object_no=k)
        maxFor_n = GetMaxValue(momentTable, 'internal_force_n') / 1000
        maxFor_y = GetMaxValue(momentTable, 'internal_force_vy') / 1000
        maxFor_z = GetMaxValue(momentTable, 'internal_force_vz') / 1000
        maxMoment_t = GetMaxValue(momentTable, 'internal_force_mt') / 1000
        maxMoment_y = GetMaxValue(momentTable, 'internal_force_my') / 1000
        maxMoment_z = GetMaxValue(momentTable, 'internal_force_mz') / 1000
        maxForce_n.append(round(maxFor_n, 3))
        maxForce_vy.append(round(maxFor_y, 3))
        maxForce_vz.append(round(maxFor_z, 3))
        maxMoment_mt.append(round(maxMoment_t, 3))
        maxMoment_my.append(round(maxMoment_y, 3))
        maxMoment_mz.append(round(maxMoment_z, 3))
        k += 1

    member_no, member_type = [], []
    k = 0
    for j in range(frame_number):
        members = [k+1, k+2, k+3, k+4, k+5, k+6, k+7, k+8, k+9, k+10, k+11, k+12, k+13]
        k += 13
        member_no.extend(members)

    types = ['Column', 'Column', 'Beam', 'Beam', 'Column', 'Column', 'Console', 'Console', 'Beam', 'Beam', 'Beam', 'Beam', 'Beam']
    member_type.extend((frame_number)*types)
    del member_no[-5:]
    del member_type[-5:]

    member_number = np.array([member_no]).T
    member_types = np.array([member_type]).T
    maxDisplacement_abs = np.array([maxDisplacement_abs]).T
    maxDisplacement_x = np.array([maxDisplacement_x]).T
    maxDisplacement_y = np.array([maxDisplacement_y]).T
    maxDisplacement_z = np.array([maxDisplacement_z]).T
    maxForce_n = np.array([maxForce_n]).T
    maxForce_vy = np.array([maxForce_vy]).T
    maxForce_vz = np.array([maxForce_vz]).T
    maxMoment_mt = np.array([maxMoment_mt]).T
    maxMoment_my = np.array([maxMoment_my]).T
    maxMoment_mz = np.array([maxMoment_mz]).T

    nodaldeformation["A2:J500"].clear_contents()
    nodalsupport["A2:J500"].clear_contents()
    deformationSheet["A2:J500"].clear_contents()
    InternalForceSheet["A2:J500"].clear_contents()

    nodaldeformation["A2"].value = node_number
    nodaldeformation["B2"].value = nodeSupportType
    nodaldeformation["C2"].value = nodeDisp_abs
    nodaldeformation["D2"].value = nodeDisp_x
    nodaldeformation["E2"].value = nodeDisp_y
    nodaldeformation["F2"].value = nodeDisp_z
    nodaldeformation["G2"].value = nodeRotation_x
    nodaldeformation["H2"].value = nodeRotation_y
    nodaldeformation["I2"].value = nodeRotation_z

    nodalsupport["A2"].value = nodes_no
    nodalsupport["B2"].value = nodesupType
    nodalsupport["C2"].value = nodeSupportForce_x
    nodalsupport["D2"].value = nodeSupportForce_y
    nodalsupport["E2"].value = nodeSupportForce_z
    nodalsupport["F2"].value = nodeMoment_x
    nodalsupport["G2"].value = nodeMoment_y
    nodalsupport["H2"].value = nodeMoment_z

    deformationSheet["A2"].value = member_number
    deformationSheet["B2"].value = member_types
    deformationSheet["C2"].value = maxDisplacement_abs
    deformationSheet["D2"].value = maxDisplacement_x
    deformationSheet["E2"].value = maxDisplacement_y
    deformationSheet["F2"].value = maxDisplacement_z

    InternalForceSheet["A2"].value = member_number
    InternalForceSheet["B2"].value = member_types
    InternalForceSheet["C2"].value = maxForce_n
    InternalForceSheet["D2"].value = maxForce_vy
    InternalForceSheet["E2"].value = maxForce_vz
    InternalForceSheet["F2"].value = maxMoment_mt
    InternalForceSheet["G2"].value = maxMoment_my
    InternalForceSheet["H2"].value = maxMoment_mz

