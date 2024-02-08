import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import NodalSupportType, NodalLoadDirection, ActionCategoryType
from RFEM.initModel import CalculateSelectedCases, Model, insertSpaces, Calculate_all
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForLines.lineSupport import LineSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Calculate.meshSettings import GetModelInfo

if __name__ == "__main__":
    # create structure
    Model(True, "DynamicAnalysis.py")

    Material(1, "C35/45")
    Section(1, "SQ_M1 0.25")
    Thickness(1, "Ceiling", 1, uniform_thickness_d=0.4)
    Thickness(2, "Walls", 1, uniform_thickness_d=0.25)
    length = 10.5
    width = 13
    height = 0
    j = 0
    k = 0
    l = 0

    Model.clientModel.service.begin_modification()

    for i in range(3):
        Node(1 + j, 0, 0, height)
        Node(2 + j, length, 0, height)
        Node(3 + j, 0, width, height)
        Node(4 + j, length, width,height)
        Node(5 + j, length/3, 0, height)
        Node(6 + j, length/3, width, height)
        Node(7 + j, 2 * length/3, 0, height)
        Node(8 + j, 2 * length/3, width, height)
        Node(9 + j, 0, width/3, height)
        Node(10 + j, 0, 2 * width/3, height)
        Node(11 + j, length, width/3, height)
        Node(12 + j, length, 2 * width/3, height)

        j += 12
        height -= 5

    j = 0
    for i in range(2):
        Line(1 + l, insertSpaces([13 + j, 14 + j]))
        Line(2+ l, insertSpaces([13 + j, 15 + j]))
        Line(3 + l, insertSpaces([14 + j, 16 + j]))
        Line(4 + l, insertSpaces([15 + j, 16 + j]))

        l += 4
        j += 12

    # vertical lines
    l = 0
    j = 0
    for i in range(2):
        Line(9 + l, insertSpaces([1 + j, 13 + j]))
        Line(10 + l, insertSpaces([2 + j, 14 + j]))
        Line(11 + l, insertSpaces([3 + j, 15 + j]))
        Line(12 + l, insertSpaces([4 + j, 16 + j]))
        Line(13 + l, insertSpaces([5 + j, 17 + j]))
        Line(14 + l, insertSpaces([7 + j, 19 + j]))
        Line(15 + l, insertSpaces([11 + j, 23 + j]))
        Line(16 + l, insertSpaces([12 + j, 24 + j]))
        Line(17 + l, insertSpaces([8 + j, 20 + j]))
        Line(18 + l, insertSpaces([6 + j, 18 + j]))
        Line(19 + l, insertSpaces([10 + j, 22 + j]))
        Line(20 + l, insertSpaces([9 + j, 21 + j]))

        l += 12
        j += 12
    # horizontal lines
    j = 0
    l = 0
    for i in range(3):
        Line(33 + l, insertSpaces([1 + j, 5 + j]))
        Line(34 + l, insertSpaces([1 + j, 9 + j]))
        Line(35 + l, insertSpaces([2 + j, 7 + j]))
        Line(36 + l, insertSpaces([2 + j, 11 + j]))
        Line(37 + l, insertSpaces([3 + j, 6 + j]))
        Line(38 + l, insertSpaces([3 + j, 10 + j]))

        l += 6
        j += 12

    # surfaces
    l = 0
    m = 0
    j = 0
    for i in range(2):
        Surface(1 + k, insertSpaces([1 + m, 2 + m, 3 + m, 4 + m]), 1)
        Surface(2 + k, insertSpaces([20 + l, 40 + j, 9 + l, 34 + j]), 2)
        Surface(3 + k, insertSpaces([13 + l, 33 + j, 9 + l, 39 + j]), 2)
        Surface(4 + k, insertSpaces([35 + j, 10 + l, 14 + l, 41 + j]), 2)
        Surface(5 + k, insertSpaces([36 + j, 10 + l, 15 + l, 42 + j]), 2)
        Surface(6 + k, insertSpaces([37 + j, 11 + l, 18 + l, 43 + j]), 2)
        Surface(7 + k, insertSpaces([38 + j, 11 + l, 19 + l, 44 + j]), 2)

        k += 7
        m += 4
        l += 12
        j += 6


    j = 0
    l = 0
    for i in range(2):
        Member(1 + j, 8 + l, 20 + l, 0, 1, 1)
        Member(2 + j, 4 + l, 16 + l, 0, 1, 1)
        Member(3 + j, 12 + l, 24 + l, 0, 1, 1)

        j += 3
        l += 12

    LineSupport(1, '33 34 35 36 37 38')
    NodalSupport(1, '4 8 12', NodalSupportType.HINGED)

    LoadCase(1, 'Self-Weight', [True, 0, 0, 1], ActionCategoryType.ACTION_CATEGORY_PERMANENT_G)

    Calculate_all()

    Model.clientModel.service.finish_modification()

