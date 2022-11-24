#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.BasicObjects.node import Node
from RFEM.formula import Formula
from RFEM.initModel import Model
from RFEM.enums import FormulaParameter
import pytest

if Model.clientModel is None:
    Model()

def test_global_parameters():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node()
    Formula()
    with pytest.raises(ValueError):
        Formula(attribute='coordinate_x')

    Model.clientModel.service.finish_modification()

    attr_lst = Formula.GetListOfParametersFormulaAllowedFor()
    assert attr_lst == ['coordinate_1', 'coordinate_2', 'coordinate_3', 'global_coordinate_1', 'global_coordinate_2', 'global_coordinate_3']
    assert Model.clientModel.service.get_node(1)['coordinate_1'] == 6
    assert Formula.Get() == '2*3'
    assert Formula.Get(formula_param=FormulaParameter.FORMULA) == '2*3'
    assert Formula.Get(formula_param=FormulaParameter.IS_VALID) == True
    assert Formula.Get(formula_param=FormulaParameter.CALCULATED_VALUE) == 6
