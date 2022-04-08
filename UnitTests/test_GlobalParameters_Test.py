#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import GlobalParameterUnitGroup, GlobalParameterDefinitionType
from RFEM.globalParameter import GlobalParameter
from RFEM.initModel import Model

if Model.clientModel is None:
    Model()

def test_global_parameters():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    GlobalParameter.AddParameter(
                                 no= 1,
                                 name= 'Test_1',
                                 symbol= 'Test_1',
                                 unit_group= GlobalParameterUnitGroup.LENGTH,
                                 definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_FORMULA,
                                 definition_parameter= ['1+1'],
                                 comment= 'Comment_1')
    GlobalParameter.AddParameter(
                                 no= 2,
                                 name= 'Test_2',
                                 symbol= 'Test_2',
                                 unit_group= GlobalParameterUnitGroup.LOADS_DENSITY,
                                 definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION,
                                 definition_parameter= [50, 0, 100, 4],
                                 comment= 'Comment_2')

    GlobalParameter.AddParameter(
                                no= 3,
                                name= 'Test_3',
                                symbol= 'Test_3',
                                unit_group= GlobalParameterUnitGroup.AREA,
                                definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION_ASCENDING,
                                definition_parameter= [50, 0, 100, 4],
                                comment= 'Comment_3')

    GlobalParameter.AddParameter(
                                no= 4,
                                name= 'Test_4',
                                symbol= 'Test_4',
                                unit_group= GlobalParameterUnitGroup.MATERIAL_QUANTITY_INTEGER,
                                definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION_ASCENDING,
                                definition_parameter= [50, 0, 100, 4],
                                comment= 'Comment_4')

    GlobalParameter.AddParameter(
                                no= 5,
                                name= 'Test_5',
                                symbol= 'Test_5',
                                unit_group= GlobalParameterUnitGroup.DIMENSIONLESS,
                                definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_VALUE,
                                definition_parameter= [0.25],
                                comment= 'Comment_5')

    Model.clientModel.service.finish_modification()
