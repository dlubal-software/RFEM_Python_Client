#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.initModel import Model
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.surface import Surface
from RFEM.enums import *
from RFEM.Loads.lineLoad import LineLoad



Model(False, "Demo1")
Model.clientModel.service.begin_modification()

Model.clientModel.service.delete_object("E_OBJECT_TYPE_MEMBER", 1, 1)

Model.clientModel.service.finish_modification()

