#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import name
import sys
sys.path.append(".")

# Import der Bibliotheken
from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.modelType import *

if __name__ == '__main__':
	
	clientModel.service.begin_modification('new')

	ModelType()

	clientModel.service.finish_modification()