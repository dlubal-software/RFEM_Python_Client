import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.initModel import Model
from RFEM.enums import ObjectTypes,GlobalParameterUnitGroup, GlobalParameterDefinitionType
from RFEM.globalParameter import GlobalParameter

if __name__ == "__main__":

    Model(True, "ExcelGlobalParamTest")

    Model.clientModel.service.begin_modification()

    GlobalParameter.AddParameter(
        no=1,
        name='Test_1',
        symbol='Test_1',
        unit_group=GlobalParameterUnitGroup.LENGTH,
        definition_type=GlobalParameterDefinitionType.DEFINITION_TYPE_FORMULA,
        definition_parameter=['1+1'],
        comment='Comment_1')

    GlobalParameter.AddParameter(
        no=2,
        name='Test_2',
        symbol='Test_2',
        unit_group=GlobalParameterUnitGroup.LOADS_FORCE_PER_UNIT_LENGTH,
        definition_type=GlobalParameterDefinitionType.DEFINITION_TYPE_VALUE,
        definition_parameter=[2000],
        comment='Comment_2')

    Model.clientModel.service.finish_modification()

    GlobalParameter.SetFormula(ObjectTypes.E_OBJECT_TYPE_LINE_LOAD,1,1,"magnitude_1","4 + Test_2")
    formula = GlobalParameter.GetFormula(ObjectTypes.E_OBJECT_TYPE_LINE_LOAD,1,1,"magnitude_1")

