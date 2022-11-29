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
from RFEM.initModel import Model, SetAddonStatus
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member


if __name__ == '__main__':

    frame_number = 4
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
        Member(i+1, k+1, k+2 )
        Member(i+2, k+2, k+3)
        Member(i+3, k+3, k+4)
        Member(i+4, k+4, k+5)
        Member(i+5, k+5, k+6)
        Member(i+6, k+1, k+7)
        Member(i+7, k+5, k+8)
        i, k = i+13, k+9

    i, k = 9, 1
    for j in range(frame_number-1):

        m, n, o = i, k+1, k+10
        for l in range(5):
            Member(m, n, o)
            m, n, o = m+1, n+1, o+1
        # Member(i, k+1, k+10)
        # Member(i+1, k+2, k+11)
        # Member(i+2, k+3, k+12)
        # Member(i+3, k+4, k+13)
        # Member(i+4, k+5, k+14)
        i, k = i+13, k+9

    bracingV = input('Would you like to include vertical bracing? (Y/N) : ')

    if bracingV.lower() == 'yes' or bracingV.lower() == 'y':

        Material(3)
        Section(3, 'L 20x20x3', 3)
        i = frame_number*8 + (frame_number-1)*5
        bracingV1 = input('Would you like to repeat a vertical bracing in every block? (Y/N): ')

        if bracingV1.lower() == 'yes' or bracingV1.lower() == 'y':
            k = 1
            for j in range(frame_number-1):
                Member(i+1, k, k+11, 0, 3, 3)
                Member(i+2, k+2, k+9, 0, 3, 3)
                Member(i+3, k+6, k+13, 0, 3, 3)
                Member(i+4, k+4, k+15, 0, 3, 3)
                i, k = i+4, k+9

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

        bracingV3 = input('Would you like to repeat a vertical bracing in even/odd blocks? (Y/N): ')

        if bracingV3.lower() == 'yes' or bracingV3.lower() == 'y':

            bracingV4 = input()





    Model.clientModel.service.finish_modification()
