#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation

if Model.clientModel is None:
    Model()

def test_design_situation():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    StaticAnalysisSettings()

    # Testing: Automatic naming, design situation keys and manual comments
    DesignSituation(no= 1, user_defined_name= False, design_situation_type= 6122, comment= 'ULS (EQU) - Permanent and transient')
    ds = Model.clientModel.service.get_design_situation(1)
    assert ds.no == 1
    DesignSituation(no= 2, user_defined_name= False, design_situation_type= 6993, comment= 'ULS (EQU) - Accidental - psi-1,1')
    ds = Model.clientModel.service.get_design_situation(2)
    assert ds.no == 2
    DesignSituation(no= 3, user_defined_name= False, design_situation_type= 6994, comment= 'ULS (EQU) - Accidental - psi-2,1')
    ds = Model.clientModel.service.get_design_situation(3)
    assert ds.no == 3

    # Testing: Manual naming, design situation keys
    DesignSituation(no= 4, user_defined_name= True, name= 'MANUAL NAME: ULS (EQU) - Seismic', design_situation_type= 6997)
    ds = Model.clientModel.service.get_design_situation(4)
    assert ds.no == 4
    # Testing: Design situation keys
    DesignSituation(5, design_situation_type= 7007)
    ds = Model.clientModel.service.get_design_situation(5)
    assert ds.no == 5
    DesignSituation(6, design_situation_type= 7010)
    ds = Model.clientModel.service.get_design_situation(6)
    assert ds.no == 6
    DesignSituation(7, design_situation_type= 7011)
    ds = Model.clientModel.service.get_design_situation(7)
    assert ds.no == 7
    # Testing: Active toggle and design situation keys
    DesignSituation(8, design_situation_type= 7014, active= True)
    ds = Model.clientModel.service.get_design_situation(8)
    assert ds.no == 8
    DesignSituation(9, design_situation_type= 6193, active= True)
    ds = Model.clientModel.service.get_design_situation(9)
    assert ds.no == 9
    DesignSituation(10, design_situation_type= 6194, active= False)
    ds = Model.clientModel.service.get_design_situation(10)
    assert ds.no == 10
    DesignSituation(11, design_situation_type= 6195, active= False)
    ds = Model.clientModel.service.get_design_situation(11)
    assert ds.no == 11
    Model.clientModel.service.finish_modification()
