#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import NodalSupportType, LoadDirectionType
from RFEM.initModel import Model, Calculate_all, client
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Results.resultTables import ResultTables, GetMaxValue
from RFEM.Calculate.meshSettings import GetModelInfo

if __name__ == '__main__':

    l = float(input('Length of the beam in m : '))
    f = float(input('Nodal force for beam in kN : '))
    defo = float(input('Maximum allowed deformation in mm : '))

    sec = ['IPE 100', 'IPE 120', 'IPE 140', 'IPE 160', 'IPE 180', 'IPE 200', 'IPE 220', 'IPE 240', 'IPE 270', 'IPE 300', 'IPE 330', 'IPE 360', 'IPE 400', 'IPE 450', 'IPE 500', 'IPE 600']
    lst = None
    lst = client.service.get_model_list()
    maxdef = float('inf')
    maxdef2 = float('inf')
    for i in range(len(sec)):

        if maxdef > defo:

            if lst:
                if "Beam" in lst[0]:
                    Model(False, 'Beam', True)
                else:
                    Model(True, 'Beam', delete_all= True)
            else:
                Model(True, 'Beam', delete_all= True) # crete new model for Beam

            Material(1, 'S235')

            Section(1, sec[i])

            Node(1, 0.0, 0.0, 0.0)
            Node(2, l, 0.0, 0.0)
            Member(1, 1, 2, 0.0, 1, 1)

            NodalSupport(1, '1', NodalSupportType.FIXED)

            StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
            StaticAnalysisSettings.SecondOrderPDelta(2, "SecondOrder")
            StaticAnalysisSettings.LargeDeformation(3, "LargeDeformation")

            LoadCase(1, 'Self-Weight', [True, 0.0, 0.0, 1.0])

            NodalLoad(1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 2*1000)

            Calculate_all()
            maxdef = GetMaxValue(ResultTables.NodesDeformations(object_no= 2), 'displacement_absolute')*1000

            print('Maximun deformation for section', sec[i], 'is' ,maxdef, 'mm')

        elif maxdef <= defo:
            print(sec[i-1], 'is optimised section as deformation', maxdef, 'mm is below permited deformation', defo, 'mm')
            break
        else:
            print('There is not matching section for the requirment')

    # Model.clientModel.service.close_connection()

    # Model for Surface
    t = 3
    while True:
        t = t + 1
        if maxdef2 > 5000:

            if lst:

                if "Surface" in lst[0]:
                    Model(False, 'Surface', True)
                else:
                    Model(True, 'Surface', delete_all= True)
            else:
                Model(True, 'Surface', delete_all= True) # crete new model for Surface

            Material(1, 'S235')

            Section(1, 'IPE 200')

            # Nodes and lines for Surface
            Node(1, 0, 0, 0)
            Node(2, 10, 0, 0)
            Node(3, 10, 10, 0)
            Node(4, 0, 10, 0)
            Node(5, 5, 5, 0)
            Line(1, '1 2')
            Line(2, '2 3')
            Line(3, '3 4')
            Line(4, '4 1')
            Thickness(1, uniform_thickness_d= t/1000)
            Surface(1, '1 2 3 4', 1)

            NodalSupport(1, '1 2 3 4', NodalSupportType.HINGED)     # Hinged Support for Surface

            StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
            StaticAnalysisSettings.SecondOrderPDelta(2, "SecondOrder")
            StaticAnalysisSettings.LargeDeformation(3, "LargeDeformation")

            LoadCase(1, 'Self-Weight', [True, 0.0, 0.0, 1.0])

            NodalLoad(1, 1, '5', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 0.1*1000)

            Calculate_all()

            maxdef2 = GetMaxValue(ResultTables.NodesDeformations(object_no=5), 'displacement_absolute') * 1000
            print('Maximun deformation for Surface thickness', t, '(mm) is' ,maxdef2, 'mm')

        elif maxdef2 < 10000:
            print(t-1, 'mm is optimised thickness for Surface')
            break