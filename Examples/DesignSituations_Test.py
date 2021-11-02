#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

if __name__ == '__main__':
	
	Model.clientModel.service.begin_modification('new')

	StaticAnalysisSettings()

	# Testing: Automatic naming, design situation keys and manual comments
	DesignSituation(no= 1, user_defined_name= False, design_situation_type= 6122, comment= 'ULS (EQU) - Permanent and transient')
	DesignSituation(no= 2, user_defined_name= False, design_situation_type= 6993, comment= 'ULS (EQU) - Accidental - psi-1,1')
	DesignSituation(no= 3, user_defined_name= False, design_situation_type= 6994, comment= 'ULS (EQU) - Accidental - psi-2,1')
	DesignSituation(no= 4, user_defined_name= False, design_situation_type= 6995, comment= 'ULS (EQU) - Accidental - Snow - psi-1,1')

	# Testing: Manual naming, design situation keys
	DesignSituation(no= 5, user_defined_name= True, name= 'MANUAL NAME: ULS (EQU) - Accidental - Snow - psi-2,1', design_situation_type= 6996)
	DesignSituation(no= 6, user_defined_name= True, name= 'MANUAL NAME: ULS (EQU) - Seismic', design_situation_type= 6997)

	# Testing: Design situation keys
	DesignSituation(7, design_situation_type= 7007)
	DesignSituation(8, design_situation_type= 7010)
	DesignSituation(9, design_situation_type= 7011)
	DesignSituation(10, design_situation_type= 7012)
	DesignSituation(11, design_situation_type= 7013)

	# Testing: Active toggle and design situation keys
	DesignSituation(12, design_situation_type= 7014, active= True)
	DesignSituation(13, design_situation_type= 6193, active= True)
	DesignSituation(14, design_situation_type= 6194, active= False)
	DesignSituation(15, design_situation_type= 6195, active= False)

	Model.clientModel.service.finish_modification()