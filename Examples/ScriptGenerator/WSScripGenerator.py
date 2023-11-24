#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

rfemDir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(rfemDir)
from RFEM.initModel import Model
from RFEM.Tools.GetObjectNumbersByType import GetAllObjects

# Define name of the model from which the data should be exported
model_name = '000874_99_Hochhaus.rf6'
folderPath = 'c:/Users/MichalO/Desktop/RFEM_modely/script_generator/000874_99_Hochhaus/'

# Connect to model
model = Model(False, model_name)

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

modelNameStr = ""
if '.' in model_name:
    idx = model_name.rfind('.')
    postfix = model_name[idx:]
    modelNameStr = '"'+model_name[:idx-1]+'_gen'+postfix+'"'
else:
    modelNameStr = '"'+model_name+'_gen.rf6"'

# Add mandatory steps
lines.insert(6+len(importObjects), '\n')
lines.insert(6+len(importObjects)+1, 'Model(True,'+modelNameStr+')\n')
lines.insert(6+len(importObjects)+2, 'Model.clientModel.service.begin_modification()\n')
lines.insert(6+len(importObjects)+3, '\n')

# Add finish modification and list all excluded objects
lines.append('\n')
lines.append('Model.clientModel.service.finish_modification()\n')
lines.append('\n')

# Create file and write data
if not folderPath:
    folderPath = os.path.dirname(__file__)

model_name = model_name[:-3]+'py'
with open(folderPath+'/'+model_name, 'w', encoding='utf-8') as f:
    f.writelines(lines)
    f.close()
