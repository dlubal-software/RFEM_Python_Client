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
from RFEM.enums import LineLoadDistribution, LoadDirectionType, StaticAnalysisType
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

    #   TESTING STANDARD LINE LOAD FUNCTION

    LoadCase(1, 'Standard')

    LineLoad(1, 1, '1', magnitude=1000)

    assert Model.clientModel.service.get_line_load(1, 1).magnitude == 1000

    #   TESTING FORCE TYPE LINE LOADS

    LoadCase(2, 'TYPE: Force')

    LineLoad.Force(1, 2, '1',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                   load_parameter=[1000])

    ll = Model.clientModel.service.get_line_load(1, 2)
    assert ll.lines == '1'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_UNIFORM'
    assert ll.magnitude == 1000

    LineLoad.Force(2, 2, '2',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1,
                   load_parameter=[False, 10000, 0.5])

    ll = Model.clientModel.service.get_line_load(2, 2)
    assert ll.lines == '2'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_1'
    assert ll.magnitude == 10000
    assert ll.distance_a_absolute == 0.5

    LineLoad.Force(3, 2, '3',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N,
                   load_parameter=[True, True, 25000, 3, 0.25, 0.5])

    ll = Model.clientModel.service.get_line_load(3, 2)
    assert ll.lines == '3'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_N'
    assert ll.magnitude == 25000
    assert ll.distance_b_relative == 0.5

    LineLoad.Force(4, 2, '4',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2,
                   load_parameter=[True, True, True, 17000, 0.25, 0.5, 0.25])

    ll = Model.clientModel.service.get_line_load(4, 2)
    assert ll.lines == '4'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_2x2'
    assert ll.magnitude == 17000
    assert ll.distance_c_relative == 0.25

    LineLoad.Force(5, 2, '5',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2,
                   load_parameter=[True, True, 5000, 7500, 0.4, 0.5])

    ll = Model.clientModel.service.get_line_load(5, 2)
    assert ll.lines == '5'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_2'
    assert ll.magnitude_2 == 7500
    assert ll.distance_a_relative == 0.4

    LineLoad.Force(6, 2, '6',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING,
                   load_parameter=[[1.5, 200], [2, 200]])

    ll = Model.clientModel.service.get_line_load(6, 2)
    assert ll.lines == '6'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_VARYING'
    assert ll.varying_load_parameters['line_load_varying_load_parameters'][0].row['distance'] == 1.5
    assert ll.varying_load_parameters['line_load_varying_load_parameters'][1].row['magnitude'] == 200


    LineLoad.Force(7, 2, '7',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL,
                   load_parameter=[True, True, 2000, 2000, 0.2, 0.5])

    ll = Model.clientModel.service.get_line_load(7, 2)
    assert ll.lines == '7'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_TRAPEZOIDAL'
    assert ll.magnitude_1 == 2000
    assert ll.distance_a_relative == 0.2
    assert ll.distance_b_is_defined_as_relative == True


    LineLoad.Force(8, 2, '8',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC,
                   load_parameter=[750, 1000, 2500])

    ll = Model.clientModel.service.get_line_load(8, 2)
    assert ll.lines == '8'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_PARABOLIC'
    assert ll.magnitude_2 == 1000

    LineLoad.Force(9, 2, '9',
                   load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_VARYING,
                   load_parameter=[[1.25, 75000], [2, 60000]])

    ll = Model.clientModel.service.get_line_load(9, 2)
    assert ll.lines == '9'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_VARYING'
    assert ll.varying_load_parameters['line_load_varying_load_parameters'][1].row['magnitude'] == 60000
    assert ll.varying_load_parameters['line_load_varying_load_parameters'][0].row['distance'] == 1.25

    #   TESTING MOMENT TYPE LINE LOADS

    LoadCase(3, 'TYPE: Moment')

    LineLoad.Moment(1, 3, '1',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[1000])

    ll = Model.clientModel.service.get_line_load(1, 3)
    assert ll.lines == '1'
    assert ll.load_direction == 'LOAD_DIRECTION_LOCAL_X'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_UNIFORM'
    assert ll.magnitude == 1000

    LineLoad.Moment(2, 3, '2',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[False, 12300, 0.5])

    ll = Model.clientModel.service.get_line_load(2, 3)
    assert ll.lines == '2'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_1'
    assert ll.magnitude == 12300
    assert ll.distance_a_absolute == 0.5

    LineLoad.Moment(3, 3, '3',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[True, True, 25000, 3, 0.25, 0.5])

    ll = Model.clientModel.service.get_line_load(3, 3)
    assert ll.lines == '3'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_N'
    assert ll.magnitude == 25000
    assert ll.distance_b_relative == 0.5

    LineLoad.Moment(4, 3, '4',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[True, True, True, 17000, 0.25, 0.5, 0.25])

    ll = Model.clientModel.service.get_line_load(4, 3)
    assert ll.lines == '4'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_2x2'
    assert ll.magnitude == 17000
    assert ll.distance_c_relative == 0.25

    LineLoad.Moment(5, 3, '5',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[True, True, 5000, 7500, 0.4, 0.5])

    ll = Model.clientModel.service.get_line_load(5, 3)
    assert ll.lines == '5'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_2'
    assert ll.magnitude_2 == 7500
    assert ll.distance_a_relative == 0.4

    LineLoad.Moment(6, 3, '6',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[[1.23, 200], [2.67, 200]])

    ll = Model.clientModel.service.get_line_load(6, 3)
    assert ll.lines == '6'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_CONCENTRATED_VARYING'
    assert ll.varying_load_parameters['line_load_varying_load_parameters'][0].row['distance'] == 1.23
    assert ll.varying_load_parameters['line_load_varying_load_parameters'][1].row['magnitude'] == 200

    LineLoad.Moment(7, 3, '7',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[True, True, 2000, 2000, 0.2, 0.5])

    ll = Model.clientModel.service.get_line_load(7, 3)
    assert ll.lines == '7'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_TRAPEZOIDAL'
    assert ll.magnitude_1 == 2000
    assert ll.distance_a_relative == 0.2
    assert ll.distance_b_is_defined_as_relative == True

    LineLoad.Moment(8, 3, '8',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_TAPERED,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[True, True, 2000, 2000, 0.2, 0.5])

    ll = Model.clientModel.service.get_line_load(8, 3)
    assert ll.lines == '8'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_TAPERED'
    assert ll.magnitude_1 == 2000
    assert ll.distance_a_relative == 0.2
    assert ll.distance_b_is_defined_as_relative == True

    LineLoad.Moment(9, 3, '9',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[750, 1000, 2500])

    ll = Model.clientModel.service.get_line_load(9, 3)
    assert ll.lines == '9'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_PARABOLIC'
    assert ll.magnitude_2 == 1000

    LineLoad.Moment(10, 3, '10',
                    load_distribution=LineLoadDistribution.LOAD_DISTRIBUTION_VARYING,
                    load_direction=LoadDirectionType.LOAD_DIRECTION_LOCAL_X,
                    load_parameter=[[0.96, 75000], [2.34, 60000]])

    ll = Model.clientModel.service.get_line_load(10, 3)
    assert ll.lines == '10'
    assert ll.load_distribution == 'LOAD_DISTRIBUTION_VARYING'
    assert ll.varying_load_parameters['line_load_varying_load_parameters'][1].row['magnitude'] == 60000
    assert ll.varying_load_parameters['line_load_varying_load_parameters'][0].row['distance'] == 0.96

    #   TESTING MASS TYPE LINE LOADS

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
