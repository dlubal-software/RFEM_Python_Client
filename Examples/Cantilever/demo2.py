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
Model(False, "Demo1.rf6")
nr = Model.clientModel.service.get_nodal_release_type(1)
print(nr)