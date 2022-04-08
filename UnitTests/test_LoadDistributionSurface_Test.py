#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

# Import the relevant Libraries
from RFEM.enums import SurfaceLoadDistributionDirection
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface

if Model.clientModel is None:
    Model()

def test_load_distribution_surface():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Testing the Default Function
    Node(1, 0, -30, 0), Node(2, 10, -30, 0), Node(3, 10, -20, 0), Node(4, 0, -20, 0)
    Line(1, '1 2'), Line(2, '2 3'), Line(3, '3 4'), Line(4, '4 1')
    Material(name='C30/37')
    Thickness()
    Surface(params={'grid_enabled':True})

    # Standard Even Load Distribution
    Node(5, 0, -15, 0), Node(6, 10, -15, 0), Node(7, 10, -5, 0), Node(8, 0, -5, 0)
    Line(5, '5 6'), Line(6, '6 7'), Line(7, '7 8'), Line(8, '8 5')
    Surface.LoadDistribution(2, '5 6 7 8', SurfaceLoadDistributionDirection.LOAD_TRANSFER_DIRECTION_IN_BOTH,
                         True, 10, loaded_lines='6 7 8', excluded_lines='5')

    Model.clientModel.service.finish_modification()
