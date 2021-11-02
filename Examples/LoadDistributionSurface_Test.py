#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append(".")

# Import the relevant Libraries
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

    Model.clientModel.service.begin_modification('new')

    # Testing the Default Function
    Node(1, 0, -30, 0), Node(2, 10, -30, 0), Node(3, 10, -20, 0), Node(4, 0, -20, 0)
    Line(1, '1 2'), Line(2, '2 3'), Line(3, '3 4'), Line(4, '4 1')
    Material(name='C30/37')
    Thickness()
    Surface()

    # Standard Even Load Distribution
    Node(5, 0, -15, 0), Node(6, 10, -15, 0), Node(7, 10, -5, 0), Node(8, 0, -5, 0)
    Line(5, '5 6'), Line(6, '6 7'), Line(7, '7 8'), Line(8, '8 5')
    Surface.LoadDistribution(Surface, 2, boundary_lines_no= '5 6 7 8', load_distribution_direction=SurfaceLoadDistributionDirection.LOAD_DISTRIBUTION_DIRECTION_IN_BOTH,
                             surface_weight_enabled=True, surface_weight=10, loaded_lines='6 7 8', excluded_lines='5')

    Model.clientModel.service.finish_modification()

