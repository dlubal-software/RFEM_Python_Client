#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from os import name
import sys
sys.path.append(".")

# Import der Bibliotheken
from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.LoadCasesAndCombinations.designSituation import *

def test_design_situation():

	clientModel.service.begin_modification('new')

	StaticAnalysisSettings()

	# Testing: Automatic naming, design situation keys and manual comments
	DesignSituation(no= 1, user_defined_name= False, design_situation_type= 6122, comment= 'ULS (EQU) - Permanent and transient')
	ds = clientModel.service.get_design_situation(1)
	assert ds.no == 1
	DesignSituation(no= 2, user_defined_name= False, design_situation_type= 6993, comment= 'ULS (EQU) - Accidental - psi-1,1')
	ds = clientModel.service.get_design_situation(2)
	assert ds.no == 2
	DesignSituation(no= 3, user_defined_name= False, design_situation_type= 6994, comment= 'ULS (EQU) - Accidental - psi-2,1')
	ds = clientModel.service.get_design_situation(3)
	assert ds.no == 3

	# Testing: Manual naming, design situation keys
	DesignSituation(no= 4, user_defined_name= True, name= 'MANUAL NAME: ULS (EQU) - Seismic', design_situation_type= 6997)
	ds = clientModel.service.get_design_situation(4)
	assert ds.no == 4
	# Testing: Design situation keys
	DesignSituation(5, design_situation_type= 7007)
	ds = clientModel.service.get_design_situation(5)
	assert ds.no == 5
	DesignSituation(6, design_situation_type= 7010)
	ds = clientModel.service.get_design_situation(6)
	assert ds.no == 6
	DesignSituation(7, design_situation_type= 7011)
	ds = clientModel.service.get_design_situation(7)
	assert ds.no == 7
	# Testing: Active toggle and design situation keys
	DesignSituation(8, design_situation_type= 7014, active= True)
	ds = clientModel.service.get_design_situation(8)
	assert ds.no == 8
	DesignSituation(9, design_situation_type= 6193, active= True)
	ds = clientModel.service.get_design_situation(9)
	assert ds.no == 9
	DesignSituation(10, design_situation_type= 6194, active= False)
	ds = clientModel.service.get_design_situation(10)
	assert ds.no == 10
	DesignSituation(11, design_situation_type= 6195, active= False)
	ds = clientModel.service.get_design_situation(11)
	assert ds.no == 11
	clientModel.service.finish_modification()