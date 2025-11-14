#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../../')

from RFEM.enums import NodalSupportType, NodalLoadDirection
from RFEM.initModel import Model, Calculate_all
from RFEM.BasicObjects.material import Material
from RFEM.Tools.sectionDialogue import CreateSectionFromRsectionFile
from RFEM.BasicObjects.crossSection import CrossSection
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings

if __name__ == '__main__':

    filepath = os.path.join(os.path.dirname(__file__), 'thin_walled.rsc')
    f = float(input('Force in kN: '))
    l = float(input('Length in m: '))

    Model(True, "Demo_Rsection") # create new Model Demo_Rsection
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')
    CreateSectionFromRsectionFile(1, filepath)
    CrossSection(1, None, 1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, l, 0.0, 0.0)

    Member(1, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
    StaticAnalysisSettings.SecondOrderPDelta(2, "SecondOrder")
    StaticAnalysisSettings.LargeDeformation(3, "LargeDeformation")

    LoadCase(1, 'Self-Weight', [True, 0.0, 0.0, 1.0])

    NodalLoad(1, 1, '2', NodalLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, f*1000)

    Model.clientModel.service.finish_modification()

    Calculate_all()
