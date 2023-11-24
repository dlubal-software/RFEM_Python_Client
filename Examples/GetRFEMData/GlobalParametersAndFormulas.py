import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.initModel import Model
from RFEM.enums import ObjectTypes, GlobalParameterUnitGroup, GlobalParameterDefinitionType
from RFEM.globalParameter import GlobalParameter
from RFEM.BasicObjects.node import Node

import xlwings as xw

dirname = os.path.join(os.getcwd(), os.path.dirname(__file__))
path = os.path.join(dirname,'ExcelGlobalParamTest.xlsx')
wb = xw.Book(path)

inputSheet = wb.sheets('Inputs')

formula =  inputSheet["B2"].formula # Test_1+Test_2

Model(True, "ExcelGlobalParams.rf6")
Model.clientModel.service.begin_modification()

GlobalParameter.AddParameter(
    no = 1,
    name = 'Test_1',
    symbol = 'Test_1',
    unit_group = GlobalParameterUnitGroup.LENGTH,
    definition_type = GlobalParameterDefinitionType.DEFINITION_TYPE_FORMULA,
    definition_parameter = ['1+1'],
    comment = 'Comment_1')

GlobalParameter.AddParameter(
    no = 2,
    name = 'Test_2',
    symbol = 'Test_2',
    unit_group = GlobalParameterUnitGroup.LOADS_FORCE_PER_UNIT_LENGTH,
    definition_type = GlobalParameterDefinitionType.DEFINITION_TYPE_VALUE,
    definition_parameter = [2000],
    comment = 'Comment_2')

Node(1)
GlobalParameter.SetFormula(ObjectTypes.E_OBJECT_TYPE_NODE, 1, 1, "coordinate_1", formula)

Model.clientModel.service.finish_modification()

get_formula = GlobalParameter.GetFormula(ObjectTypes.E_OBJECT_TYPE_NODE, 1, 1, "coordinate_1")
coord_1 = Node.GetNode(1).coordinate_1
assert coord_1 == 2002

outputSheet = wb.sheets('Nodes')
outputSheet["B2"].value = coord_1

wb.save(path)
wb.app.quit()
