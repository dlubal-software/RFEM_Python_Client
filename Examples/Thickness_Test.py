#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append(".")

# Import der Bibliotheken
from os import name
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
    
    Material(1, 'C30/37')
	
    ##  THICKNESS TYPE

    # Standard
    Thickness()

    # Constant
    Thickness.Uniform(Thickness,
                     no= 2,
                     name= 'Constant',
                     properties= [0.2],
                     comment= 'Comment')

    # Variable - 3 Nodes
    Node(1, 5, 5, 0)
    Node(2, 5, 10, 0)
    Node(3, 10, 7.5, 0)
    Thickness.Variable_3Nodes(Thickness,
                     no= 3,
                     name= 'Variable - 3 Nodes',
                     properties= [0.1, 1, 0.25, 2, 0.45, 3],
                     comment= 'Comment')
                                 
    # Variable - 2 Nodes and Direction
    Node(4, 20, -10, 0)
    Node(5, 20, 0, -5)
    Thickness.Variable_2NodesAndDirection(Thickness,
                     no= 4,
                     name= 'Variable - 2 Nodes and Direction',
                     properties= [0.32, 4, 0.45, 5, ThicknessDirection.THICKNESS_DIRECTION_IN_Z],
                     comment= 'Comment')

    # Variable - 4 Surface Corners
    Node(6, 5, -20, 0)
    Node(7, 5, -25, 0)
    Node(8, 10, -25, 0)
    Node(9, 10, -20, 0)
    Thickness.Variable_4SurfaceCorners(Thickness,
                     no= 5,
                     name= 'Variable - 4 Surface Corners',
                     properties= [0.15, 6, 0.25, 7, 0.32, 8, 0.15, 9],
                     comment= 'Comment')

    # Variable - Circle
    Thickness.Variable_Circle(Thickness,
                     no= 6,
                     name= 'Variable - Circle',
                     properties= [0.1, 0.5],
                     comment= 'Comment')

    # # Layers
    Thickness.Layers(Thickness,
                     no= 7,
                     name= 'Layers',
                     layers= [[1, 1, 0.123, 0, 'Schicht 1'],
                                       [0, 1, 0.456, 90, 'Schicht 2']],
                     comment= 'Comment')


    # Shape Orthotropy
    Thickness.ShapeOrthotropy(Thickness,
                     no= 8,
                     name= 'Shape Orthotropy',
                     orthotropy_type= ThicknessOrthotropyType.ORTHOTROPIC_THICKNESS_TYPE_HOLLOW_CORE_SLAB,
                     rotation_beta= 180,
                     consideration_of_self_weight= [ThicknessSelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, 0.234],
                     parameters= [0.4, 0.125, 0.05],
                     comment= 'Comment')

    # Stiffness Matrix
    Thickness.StiffnessMatrix(Thickness,
                     no= 9,
                     name= 'Stiffness Matrix',
                     stiffness_matrix= [[11000, 12000, 13000, 22000, 23000, 33000],
                                        [44000, 45000, 55000],
                                        [66000, 67000, 68000, 77000, 78000, 88000],
                                        [16000, 17000, 18000, 27000, 28000, 38000]],
                     comment= 'Comment')
    
    #Calculate_all()
    print('Ready!')
    
    clientModel.service.finish_modification()