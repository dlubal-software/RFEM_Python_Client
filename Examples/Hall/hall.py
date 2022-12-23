#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')
from RFEM.enums import NodalSupportType, MemberRotationSpecificationType
from RFEM.initModel import Model, insertSpaces
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport

if __name__ == '__main__':

    l = float(input('Length of the clear span in m: '))
    n = int(input('Number of frames: '))
    d = float(input('Distance between frames in m: '))
    h = float(input('Height of frame in m: '))

    Model()
    Model.clientModel.service.begin_modification()

    # nodes
    for i in range(n):
        j = i * 5
        Node(j+1, 0.0, -i*d, 0.0)
        Node(j+2, 0.0, -i*d, -h)
        Node(j+3, l/2, -i*d, -h)
        Node(j+4, l, -i*d, -h)
        Node(j+5, l, -i*d, 0.0)

    # nodal supports
    nodes_no = []
    for i in range(n):
        j = 5*i
        nodes_no.extend([j+1, j+5])
    NodalSupport(1, insertSpaces(nodes_no), NodalSupportType.HINGED, "Hinged support")

    # members
    Material(1, 'S235')

    # sections
    Section(1, 'HEM 700', 1)
    Section(2, 'IPE 500', 1)

    # members x direction
    for i in range(n):
        j = i * 5
        k = i * 4
        Member(k+1,  j+1, j+2, 0.0,  1, 1)
        Member(k+2,  j+2, j+3, 0.0,  2, 2)
        Member(k+3,  j+3, j+4, 0.0,  2, 2)
        Member(k+4,  j+4, j+5, 0.0,  1, 1)

    # members y direction
    for i in range(1,n):
        j = (i-1) * 5
        Member(4*n+i,  j+2, j+7, 0.0, 2, 2)
        Member(4*n+i + n-1,  j+4, j+9, 0.0, 2, 2)

    # vertical bracing
    # add a question about repeating in every block, one yes one no, only beginning and end

    BracingV = input('Would you like to include vertical bracing? (Y/N)')
    if BracingV.lower() == 'yes' or BracingV.lower() == 'y':
        BracingV_C1 = input(
            'Would you like to repeat a vertical bracing in every block? (Y/N)')
        if BracingV_C1.lower() == 'yes' or BracingV_C1.lower() == 'y':
            Material(3, 'EN AW-3004 H14')
            Section(3, 'IPE 80', 3)
            j = 4*n + 3*(n-1)
            k = 4*n + 2*(n-1)
            for i in range(n):
                Member(k+1+4*i, i*5+1, i*5+7, 0.0, 3, 3)
                Member(k+2+4*i, i*5+2, i*5+6, 0.0, 3, 3)
                Member(k+3+4*i, i*5+5, i*5+9, 0.0, 3, 3)
                Member(k+4+4*i, i*5+4, i*5+10, 0.0, 3, 3)

        BracingV_C2 = input(
            'Would you like to repeat a vertical bracing only in the first and last block? (Y/N)')
        if BracingV_C2.lower() == 'yes' or BracingV_C2.lower() == 'y':
            Material(3, 'EN AW-3004 H14')
            Section(3, 'IPE 80', 3)

            k = n*4+(n-1)*2
            for i in range(n):
                if i in (0, n-2):
                    Member.Tension(k+1+4*i, i*5+1, i*5+7,
                                   MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
                    Member.Tension(k+2+4*i, i*5+2, i*5+6,
                                   MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
                    Member.Tension(k+3+4*i, i*5+5, i*5+9,
                                   MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
                    Member.Tension(k+4+4*i, i*5+4, i*5+10,
                                   MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)

        # MAKE IT MORE GENERAL!
        BracingV_C3 = input(
            'Would you like to repeat a vertical bracing in even/odd blocks? (Y/N)')
        if BracingV_C3.lower() == 'yes' or BracingV_C3.lower() == 'y':
            Material(3, 'EN AW-3004 H14')
            Section(3, 'IPE 80', 3)

            j = 4*n + 3*(n-1)
            k = 4*n + 2*(n-1)
            for i in range(n):
                if i % 2 == 0:
                    Member.Tension(k+1+4*i, i*5+1, i*5+7,
                                   MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
                    Member.Tension(k+2+4*i, i*5+2, i*5+6,
                                   MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
                    Member.Tension(k+3+4*i, i*5+5, i*5+9,
                                   MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)
                    Member.Tension(k+4+4*i, i*5+4, i*5+10,
                                   MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 3)

    # horizontal bracing
    # add a question about repeating in every block, one yes one no, only beginning and end

    member_count = n*4+(n-1)*2
    BracingH = input('Would you like to include horizontal bracing? (Y/N)')
    if BracingV.lower() == 'yes' or BracingV.lower() == 'y':
        member_count += (n-1)*4
        BracingH = 'yes'
        if BracingH.lower() == 'yes' or BracingH.lower() == 'y':

            for i in range(n-1):
                j = i * 5
                Member(int(member_count+1+4*i), j+2, j+8, 0.0, 3, 3)
                Member(int(member_count+2+4*i), j+3, j+7, 0.0, 3, 3)
                Member(int(member_count+3+4*i), j+3, j+9, 0.0, 3, 3)
                Member(int(member_count+4+4*i), j+4, j+8, 0.0, 3, 3)

    print("Preparing...")
    print('Ready!')
    Model.clientModel.service.finish_modification()
