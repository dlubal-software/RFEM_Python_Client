#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

rfemDir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(rfemDir)
from RFEM.initModel import Model
from RFEM.Tools.GetObjectNumbersByType import GetAllObjects

# Define name of the model from which the data should be exported
model_name = 'test.rf6'

# Export active model to XML
model = Model(True, model_name)

# Constant imports
lines = ['import sys\n',
         'sys.path.append("'+rfemDir.replace('\\', '/')+'")\n',
         'from RFEM.enums import *\n',
         'from RFEM.initModel import *\n',
         'from RFEM.dataTypes import inf, nan\n',
         '\n']

objects, importObjects = GetAllObjects()
lines += objects

# Add imports to 'lines'
for i,v in enumerate(importObjects):
    lines.insert(i+6, v)

# Add mandatory steps
lines.insert(6+len(importObjects), '\n')
lines.insert(6+len(importObjects)+1, 'Model()\n')
lines.insert(6+len(importObjects)+2, 'Model.clientModel.service.begin_modification()\n')
lines.insert(6+len(importObjects)+3, '\n')

# Add finish modification and list all excluded objects
lines.append('\n')
lines.append('Model.clientModel.service.finish_modification()\n')
lines.append('\n')

# Create file and write data
f = open(os.path.dirname(__file__)+"/WSgeneratedScript.py", "w", encoding="utf-8")
f.writelines(lines)
f.close()
