#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append(".")

# Import der Bibliotheken
from RFEM.Loads.lineLoad import LineLoad
from RFEM.enums import *
#from RFEM.window import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.solidSet import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.surfaceLoad import *

if __name__ == '__main__':
	
	clientModel.service.begin_modification('new')

	# Creating a lot of lines for line load testing
	
	Node(1, 0, 0, 0), Node(2, 2, 0, 0), Node(3, 4, 0, 0), Node(4, 6, 0, 0), Node(5, 8, 0, 0), Node(6, 10, 0, 0)
	Node(7, 10, 2, 0), Node(8, 10, 4, 0), Node(9, 10, 6, 0), Node(10, 10, 8, 0), Node(11, 10, 10, 0)
	Node(12, 8, 10, 0), Node(13, 6, 10, 0), Node(14, 4, 10, 0), Node(15, 2, 10, 0), Node(16, 0, 10, 0)
	Node(17, 0, 8, 0), Node(18, 0, 6, 0), Node(19, 0, 4, 0), Node(20, 0, 2, 0)

	surface_str = ''
	nodes_no = ''
	for i in range(1, 21):
		if i < 20:
				surface_str += str(i)+' '
				nodes_no = str(i)+' '+str(i+1)
				Line(i, nodes_no)
		else:
				surface_str += str(i)
				nodes_no = str(i)+' 1'
				Line(i, nodes_no)
	
	Material()
	Thickness()
	Surface(1, surface_str)

	# Testing Standard (i.e. default) Function

	LoadCase(1 , 'Standard', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, False)

	LineLoad(1,1,'1', magnitude=1)
	
	# Testing Force Type Line Loads

	LoadCase(2 , 'TYPE: Force', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, False)

	LineLoad.Force(LineLoad, 1, 2, '1',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
					 load_parameter=[1000])

	LineLoad.Force(LineLoad, 2, 2, '2',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1,
					 load_parameter=[False, 10000, 0.5])

	LineLoad.Force(LineLoad, 3, 2, '3',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N,
					 load_parameter=[True, True, 25000, 3, 0.25, 0.5])

	LineLoad.Force(LineLoad, 4, 2, '4',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2,
					 load_parameter=[True, True, True, 17000, 0.25, 0.5, 0.25])

	LineLoad.Force(LineLoad, 5, 2, '5',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2,
					 load_parameter=[True, True, 5000, 7500, 0.4, 0.5])

	LineLoad.Force(LineLoad, 6, 2, '6',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING,
					 load_parameter=[[0.2, 0.1, 200], [0.5, 0.2, 200]])

# NOTE. THESE OFFSET PARAMETERS AREN'T WORKING. THE ERROR IS APPARENTLY A BUG IN BACK-END AND HAS BEEN REPORTED. NOT SURE HOW TO PROCEED (?)
	# LineLoad.Force(LineLoad, 7, 2, '7',
	# 				 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL,
	# 				 load_parameter=[True, True, 2000, 2000, 0.2, 0.5])

	LineLoad.Force(LineLoad, 8, 2, '8',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC,
					 load_parameter=[750, 1000, 2500])

# NOTE. THESE OFFSET PARAMETERS AREN'T WORKING. THE ERROR IS APPARENTLY A BUG IN BACK-END AND HAS BEEN REPORTED. NOT SURE HOW TO PROCEED (?)
	# LineLoad.Force(LineLoad, 9, 2, '9',
	# 				 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_VARYING,
	# 				 load_parameter=[[1000, 500, 750], [250, 200, 600]])

	# Testing Moment Type Line Loads

	LoadCase(3 , 'TYPE: Moment', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, False)

	LineLoad.Moment(LineLoad, 1, 3, '1',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
					 load_parameter=[1000])

	LineLoad.Moment(LineLoad, 2, 3, '2',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1,
					 load_parameter=[False, 10000, 0.5])

	LineLoad.Moment(LineLoad, 3, 3, '3',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N,
					 load_parameter=[True, True, 25000, 3, 0.25, 0.5])

	LineLoad.Moment(LineLoad, 4, 3, '4',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2,
					 load_parameter=[True, True, True, 17000, 0.25, 0.5, 0.25])

	LineLoad.Moment(LineLoad, 5, 3, '5',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2,
					 load_parameter=[True, True, 5000, 7500, 0.4, 0.5])

	LineLoad.Moment(LineLoad, 6, 3, '6',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING,
					 load_parameter=[[0.2, 0.1, 200], [0.5, 0.2, 200]])

# NOTE. THESE OFFSET PARAMETERS AREN'T WORKING. THE ERROR IS APPARENTLY A BUG IN BACK-END AND HAS BEEN REPORTED. NOT SURE HOW TO PROCEED (?)
	# LineLoad.Moment(LineLoad, 7, 3, '7',
	# 				 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL,
	# 				 load_parameter=[True, True, 2000, 2000, 0.2, 0.5])

# NOTE. THESE OFFSET PARAMETERS AREN'T WORKING. THE ERROR IS APPARENTLY A BUG IN BACK-END AND HAS BEEN REPORTED. NOT SURE HOW TO PROCEED (?)
	# LineLoad.Moment(LineLoad, 8, 3, '8',
	# 				 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_TAPERED,
	# 				 load_parameter=[True, True, 2000, 2000, 0.2, 0.5])

	LineLoad.Moment(LineLoad, 9, 3, '9',
					 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC,
					 load_parameter=[750, 1000, 2500])

# NOTE. THESE OFFSET PARAMETERS AREN'T WORKING. THE ERROR IS APPARENTLY A BUG IN BACK-END AND HAS BEEN REPORTED. NOT SURE HOW TO PROCEED (?)
	# LineLoad.Moment(LineLoad, 10, 3, '10',
	# 				 load_distribution= LineLoadDistribution.LOAD_DISTRIBUTION_VARYING,
	# 				 load_parameter=[[1000, 500, 750], [250, 200, 600]])

	# Testing Mass Type Line Loads

	LoadCase(4 , 'TYPE: Mass', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, False)

	LineLoad.Mass(LineLoad, 1, 4, '1',
					 individual_mass_components= False,
					 mass_components= [10])
	
	LineLoad.Mass(LineLoad, 2, 4, '2',
					 individual_mass_components=True,
					 mass_components=[1000,1000,10000])


	print('Ready!')
	
	clientModel.service.finish_modification()
	
