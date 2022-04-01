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
from RFEM.enums import DesignSituationType

if Model.clientModel is None:
    Model()

def test_design_situation():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    StaticAnalysisSettings()

    # Testing: Automatic naming, design situation keys and manual comments
    DesignSituation(1, DesignSituationType.DESIGN_SITUATION_TYPE_EQU_PERMANENT_AND_TRANSIENT, True, 'ULS (EQU) - Permanent and transient', 'ULS (EQU) - Permanent and transient')
    ds = Model.clientModel.service.get_design_situation(1)
    assert ds.no == 1
    DesignSituation(2, DesignSituationType.DESIGN_SITUATION_TYPE_EQU_ACCIDENTAL_PSI_1_1, comment='ULS (EQU) - Accidental - psi-1,1')
    ds = Model.clientModel.service.get_design_situation(2)
    assert ds.no == 2
    DesignSituation(3, DesignSituationType.DESIGN_SITUATION_TYPE_EQU_ACCIDENTAL_PSI_2_1, comment='ULS (EQU) - Accidental - psi-2,1')
    ds = Model.clientModel.service.get_design_situation(3)
    assert ds.no == 3

    # Testing: Manual naming, design situation keys
    DesignSituation(4, DesignSituationType.DESIGN_SITUATION_TYPE_EQU_SEISMIC, comment='MANUAL NAME: ULS (EQU) - Seismic')
    ds = Model.clientModel.service.get_design_situation(4)
    assert ds.no == 4
    assert ds.design_situation_type == DesignSituationType.DESIGN_SITUATION_TYPE_EQU_SEISMIC.name

    Model.clientModel.service.finish_modification()
