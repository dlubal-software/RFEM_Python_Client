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
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination

if __name__ == '__main__':

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
    console_length = 0.3

    Model(True, 'SteelHall')
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.steel_design_active)
    Material(1, 'S235')
    Material(3)
    Section(1, 'IPE 200', 1)
    Section(3, 'L 20x20x3', 3)
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
        Member(i+4, k+4, k+5, 0, 1, 1)
        Member(i+5, k+5, k+6, 0, 1, 1)
        Member(i+6, k+1, k+7, 0, 1, 1)
        Member(i+7, k+5, k+8, 0, 1, 1)
        i, k = i+13, k+9

    i, k = 9, 1
    for j in range(frame_number-1):

        m, n, o = i, k+1, k+10
        for l in range(5):
            Member(m, n, o, 0, 1, 1)
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
                Member(i+1, k, k+11, 0, 3, 3)
                Member(i+2, k+2, k+9, 0, 3, 3)
                Member(i+3, k+6, k+13, 0, 3, 3)
                Member(i+4, k+4, k+15, 0, 3, 3)
                i, k = i+4, k+9

        else:
            bracingV2 = input('Would you like to repeat a vertical bracing only in the first and last block? (Y/N): ')

        if bracingV2.lower() == 'yes' or bracingV2.lower() == 'y':
            k = 1
            for j in range(frame_number-1):
                if j in [0, frame_number-2]:
                    Member(i+1, k, k+11, 0, 3, 3)
                    Member(i+2, k+2, k+9, 0, 3, 3)
                    Member(i+3, k+6, k+13, 0, 3, 3)
                    Member(i+4, k+4, k+15, 0, 3, 3)
                    i = i+4
                k = k+9
        elif bracingV2.lower() == 'no' or bracingV2.lower() == 'n':
            bracingV3 = input('Would you like to repeat a vertical bracing in even/odd blocks? (E/O/N): ')

        if bracingV3.lower() == 'even' or bracingV3.lower() == 'e':
            k = 1
            for j in range(frame_number-1):
                if j % 2 != 0:
                    Member(i+1, k, k+11, 0, 3, 3)
                    Member(i+2, k+2, k+9, 0, 3, 3)
                    Member(i+3, k+6, k+13, 0, 3, 3)
                    Member(i+4, k+4, k+15, 0, 3, 3)
                    i = i + 4
                k = k+9

        elif bracingV3.lower() == 'odd' or bracingV3.lower() == 'o':
            k = 1
            for j in range(frame_number-1):
                if j % 2 == 0:
                    Member(i+1, k, k+11, 0, 3, 3)
                    Member(i+2, k+2, k+9, 0, 3, 3)
                    Member(i+3, k+6, k+13, 0, 3, 3)
                    Member(i+4, k+4, k+15, 0, 3, 3)
                    i = i + 4
                k = k+9

    bracingH = input('Would you like to include Horizontal bracing? (Y/N) : ')
    if bracingH.lower() == 'yes' or bracingH.lower() == 'y':

        if bracingV.lower() == 'no' or bracingV.lower() == 'n':
            k = 1
            for j in range(frame_number-1):
                Member(i+1, k+2, k+12, 0, 3, 3)
                Member(i+2, k+3, k+11, 0, 3, 3)
                Member(i+3, k+3, k+13, 0, 3, 3)
                Member(i+4, k+4, k+12, 0, 3, 3)
                i, k = i+4, k+9

        if bracingV1.lower() == 'yes' or bracingV1.lower() == 'y':
            k = 1
            for j in range(frame_number-1):
                Member(i+1, k+2, k+12, 0, 3, 3)
                Member(i+2, k+3, k+11, 0, 3, 3)
                Member(i+3, k+3, k+13, 0, 3, 3)
                Member(i+4, k+4, k+12, 0, 3, 3)
                i, k = i+4, k+9

        if bracingV2.lower() == 'yes' or bracingV2.lower() == 'y':
            k = 1
            for j in range(frame_number-1):
                if j in [0, frame_number-2]:
                    Member(i+1, k+2, k+12, 0, 3, 3)
                    Member(i+2, k+3, k+11, 0, 3, 3)
                    Member(i+3, k+3, k+13, 0, 3, 3)
                    Member(i+4, k+4, k+12, 0, 3, 3)
                    i = i+4
                k = k+9

        if bracingV3.lower() == 'even' or bracingV3.lower() == 'e':
            k = 1
            for j in range(frame_number-1):
                if j % 2 != 0:
                    Member(i+1, k+2, k+12, 0, 3, 3)
                    Member(i+2, k+3, k+11, 0, 3, 3)
                    Member(i+3, k+3, k+13, 0, 3, 3)
                    Member(i+4, k+4, k+12, 0, 3, 3)
                    i = i + 4
                k = k+9

        elif bracingV3.lower() == 'odd' or bracingV3.lower() == 'o':
            k = 1
            for j in range(frame_number-1):
                if j % 2 == 0:
                    Member(i+1, k+2, k+12, 0, 3, 3)
                    Member(i+2, k+3, k+11, 0, 3, 3)
                    Member(i+3, k+3, k+13, 0, 3, 3)
                    Member(i+4, k+4, k+12, 0, 3, 3)
                    i = i + 4
                k = k+9

    # Nodal Support
    nodes_no = []
    k = 1
    for j in range(frame_number):
        nodes_no.extend([k, k+6])
        k = k + 9

    NodalSupport(1, insertSpaces(nodes_no), NodalSupportType.HINGED)

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
    StaticAnalysisSettings.SecondOrderPDelta(2, "SecondOrder")
    StaticAnalysisSettings.LargeDeformation(3, "LargeDeformation")

    LoadCase(1, 'Self-Weight', [True, 0.0, 0.0, 1.0])
    LoadCase.StaticAnalysis(2, 'Wind-Load', True, 1, ActionCategoryType.ACTION_CATEGORY_WIND_QW, [False])
    LoadCase.StaticAnalysis(3, 'Snow-Load', True, 1, ActionCategoryType.ACTION_CATEGORY_SNOW_ICE_LOADS_H_LESS_OR_EQUAL_TO_1000_M_QS, [False])
    LoadCase.StaticAnalysis(4, 'Seismic-Action', True, 1, ActionCategoryType.ACTION_CATEGORY_SEISMIC_ACTIONS_AE, [False])

    LoadCombination(1, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,2,0,False]])
    LoadCombination(2, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,3,0,False]])
    LoadCombination(3, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,4,0,False]])
    LoadCombination(4, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1,1,0,False],[1,2,0,False],[1,3,0,False],[1,4,0,False]])

    Model.clientModel.service.finish_modification()

    Calculate_all()
