#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Loads.linesetLoad import LineSetLoad
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.TypesForLines.lineSupport import LineSupport
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.lineSet import LineSet
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model
from RFEM.enums import LineLoadDistribution, StaticAnalysisType, LoadDirectionType, LineSetLoadDistribution
from RFEM.Loads.lineLoad import LineLoad

if Model.clientModel is None:
    Model()

def test_line_loads():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Creating a lot of lines for line load testing

    Node(1, 0, 0, 0), Node(2, 2, 0, 0), Node(3, 4, 0, 0), Node( 4, 6, 0, 0), Node(5, 8, 0, 0), Node(6, 10, 0, 0)
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

    LoadCase(1, 'Standard')

    LineLoad(1, 1, '1', magnitude=1)

    # Testing Force Type Line Loads

    LoadCase(2, 'TYPE: Force')

    LineLoad.Force(1, 2, '1',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                   load_parameter=[1000])

    LineLoad.Force(2, 2, '2',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1,
                   load_parameter=[False, 10000, 0.5])

    LineLoad.Force(3, 2, '3',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N,
                   load_parameter=[True, True, 25000, 3, 0.25, 0.5])

    LineLoad.Force(4, 2, '4',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2,
                   load_parameter=[True, True, True, 17000, 0.25, 0.5, 0.25])

    LineLoad.Force(5, 2, '5',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2,
                   load_parameter=[True, True, 5000, 7500, 0.4, 0.5])

    LineLoad.Force(6, 2, '6',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING,
                   load_parameter=[[0.2, 0.1, 200], [0.5, 0.2, 200]])

    LineLoad.Force(7, 2, '7',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL,
                   load_parameter=[True, True, 2000, 2000, 0.2, 0.5])

    LineLoad.Force(8, 2, '8',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC,
                   load_parameter=[750, 1000, 2500])

    LineLoad.Force(9, 2, '9',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_VARYING,
                   load_parameter=[[1, 1, 75000], [2, 1, 60000]])

    # Testing Moment Type Line Loads

    LoadCase(3, 'TYPE: Moment')

    LineLoad.Moment(1, 3, '1',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                    load_parameter=[1000])

    LineLoad.Moment(2, 3, '2',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1,
                    load_parameter=[False, 10000, 0.5])

    LineLoad.Moment(3, 3, '3',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N,
                    load_parameter=[True, True, 25000, 3, 0.25, 0.5])

    LineLoad.Moment(4, 3, '4',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2,
                    load_parameter=[True, True, True, 17000, 0.25, 0.5, 0.25])

    LineLoad.Moment(5, 3, '5',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2,
                    load_parameter=[True, True, 5000, 7500, 0.4, 0.5])

    LineLoad.Moment(6, 3, '6',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING,
                    load_parameter=[[0.2, 0.1, 200], [0.5, 0.2, 200]])

    LineLoad.Moment(7, 3, '7',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL,
                    load_parameter=[True, True, 2000, 2000, 0.2, 0.5])

    LineLoad.Moment(8, 3, '8',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_TAPERED,
                    load_parameter=[True, True, 2000, 2000, 0.2, 0.5])

    LineLoad.Moment(9, 3, '9',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC,
                    load_parameter=[750, 1000, 2500])

    LineLoad.Moment(10, 3, '10',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_VARYING,
                    load_parameter=[[1, 1, 75000], [2, 1, 60000]])

    # Testing Mass Type Line Loads

    LoadCase(4, 'TYPE: Mass')

    LineLoad.Mass(1, 4, '1',
                  individual_mass_components=False,
                  mass_components=[10])

    LineLoad.Mass(2, 4, '2',
                  individual_mass_components=True,
                  mass_components=[1000, 1000, 10000])

    Model.clientModel.service.finish_modification()


def test_line_set_loads():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5.0, 0.0, 0.0)
    Node(3, 5.0, 6.0, 0.0)
    Node(4, 0.0, 6.0, 0.0)

    Node(5, 2.0, 2.0, 0.0)
    Node(6, 4.0, 2.0, 0.0)
    Node(7, 4.0, 4.0, 0.0)
    Node(8, 2.0, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '5 6')
    Line(6, '6 7')
    Line(7, '7 8')

    Thickness(1, 'My Thickness', 1, 0.05)
    Surface(1, '1-4', 1, 'My Test')

    LineSupport(1, '1 2 3 4')
    LineSet.ContinuousLines(1, '5-7')
    StaticAnalysisSettings(1, 'LINEAR', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')
    LineSetLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 1200.5, 'My Comment')
    LineSetLoad.Force(2, 1, '1', load_parameter=2500)
    LineSetLoad.Mass(3, 1, '1', False, [3100])
    LineSetLoad.Moment(4, load_parameter=4000)
    Model.clientModel.service.finish_modification()

    assert Model.clientModel.service.get_line_set_load(1, 1).magnitude == 1200.5
    assert Model.clientModel.service.get_line_set_load(2, 1).magnitude == 2500
    assert Model.clientModel.service.get_line_set_load(3, 1).mass_global == 3100
    assert Model.clientModel.service.get_line_set_load(4, 1).magnitude == 4000
