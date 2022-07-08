import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import ThicknessDirection, ThicknessOrthotropyType
from RFEM.enums import ThicknessShapeOrthotropySelfWeightDefinitionType, ThicknessStiffnessMatrixSelfWeightDefinitionType
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node

if Model.clientModel is None:
    Model()

def test_thickness():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    Material(1, 'C30/37')

    ##  THICKNESS TYPE

    # Standard
    Thickness()

    # Constant
    Thickness.Uniform(
                     no= 2,
                     name= 'Constant',
                     properties= [0.2],
                     comment= 'Comment')

    # Variable - 3 Nodes
    Node(1, 5, 5, 0)
    Node(2, 5, 10, 0)
    Node(3, 10, 7.5, 0)
    Thickness.Variable_3Nodes(
                     no= 3,
                     name= 'Variable - 3 Nodes',
                     properties= [0.1, 1, 0.25, 2, 0.45, 3],
                     comment= 'Comment')

    # Variable - 2 Nodes and Direction
    Node(4, 20, -10, 0)
    Node(5, 20, 0, -5)
    Thickness.Variable_2NodesAndDirection(
                     no= 4,
                     name= 'Variable - 2 Nodes and Direction',
                     properties= [0.32, 4, 0.45, 5, ThicknessDirection.THICKNESS_DIRECTION_IN_Z],
                     comment= 'Comment')

    # Variable - 4 Surface Corners
    Node(6, 5, -20, 0)
    Node(7, 5, -25, 0)
    Node(8, 10, -25, 0)
    Node(9, 10, -20, 0)
    Thickness.Variable_4SurfaceCorners(
                     no= 5,
                     name= 'Variable - 4 Surface Corners',
                     properties= [0.15, 6, 0.25, 7, 0.32, 8, 0.15, 9],
                     comment= 'Comment')

    # Variable - Circle
    Thickness.Variable_Circle(
                     no= 6,
                     name= 'Variable - Circle',
                     properties= [0.1, 0.5],
                     comment= 'Comment')

    # Layers
    Thickness.Layers(
                     no= 7,
                     name= 'Layers',
                     layers= [[0, 1, 0.123],
                              [0, 1, 0.456]],
                     comment= 'Comment')

    # Shape Orthotropy
    Thickness.ShapeOrthotropy(
                     no= 8,
                     name= 'Shape Orthotropy',
                     orthotropy_type= ThicknessOrthotropyType.HOLLOW_CORE_SLAB,
                     rotation_beta= 180,
                     consideration_of_self_weight= [ThicknessShapeOrthotropySelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, 0.350],
                     parameters= [0.4, 0.125, 0.05],
                     comment= 'Comment')

    # Stiffness Matrix
    Thickness.StiffnessMatrix(
                     no= 9,
                     name= 'Stiffness Matrix',
                     rotation_beta= 90,
                     stiffness_matrix= [[11000, 12000, 13000, 22000, 23000, 33000],
                                        [44000, 45000, 55000],
                                        [66000, 67000, 68000, 77000, 78000, 88000],
                                        [16000, 17000, 18000, 27000, 28000, 38000]],
                     consideration_of_self_weight= [ThicknessStiffnessMatrixSelfWeightDefinitionType.SELF_WEIGHT_DEFINITION_TYPE_DEFINED_VIA_BULK_DENSITY_AND_AREA_DENSITY, 10, 10],
                     coefficient_of_thermal_expansion= 1,
                     comment= 'Comment')

    Model.clientModel.service.finish_modification()

    assert Model.clientModel.service.get_thickness(2).uniform_thickness == 0.2

    assert Model.clientModel.service.get_thickness(3).type == 'TYPE_VARIABLE_THREE_NODES'
    assert Model.clientModel.service.get_thickness(3).thickness_2 == 0.25
    assert Model.clientModel.service.get_thickness(3).node_3 == 3

    assert Model.clientModel.service.get_thickness(4).direction == 'THICKNESS_DIRECTION_IN_Z'
    assert Model.clientModel.service.get_thickness(4).thickness_2 == 0.45
    assert Model.clientModel.service.get_thickness(4).node_1 == 4

    assert Model.clientModel.service.get_thickness(5).node_2 == 7
    assert Model.clientModel.service.get_thickness(5).thickness_4 == 0.15

    assert Model.clientModel.service.get_thickness(6).thickness_circle_center == 0.1
    assert Model.clientModel.service.get_thickness(6).thickness_circle_line == 0.5

    assert Model.clientModel.service.get_thickness(7).layers_reference_table['thickness_layers_reference_table'][0].row['thickness'] == 0.123
    assert Model.clientModel.service.get_thickness(7).layers_reference_table['thickness_layers_reference_table'][1].row['thickness'] == 0.456

    assert Model.clientModel.service.get_thickness(8).orthotropy_type == 'ORTHOTROPIC_THICKNESS_TYPE_HOLLOW_CORE_SLAB'
    assert Model.clientModel.service.get_thickness(8).shape_orthotropy_self_weight_definition_type == 'SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS'
    #assert Model.clientModel.service.get_thickness(8).orthotropy_fictitious_thickness == 0.350
    assert Model.clientModel.service.get_thickness(8).slab_thickness == 0.4
    assert Model.clientModel.service.get_thickness(8).void_spacing == 0.125
    assert Model.clientModel.service.get_thickness(8).void_diameter == 0.05

    assert Model.clientModel.service.get_thickness(9).stiffness_matrix_self_weight_definition_type == 'SELF_WEIGHT_DEFINITION_TYPE_DEFINED_VIA_BULK_DENSITY_AND_AREA_DENSITY'
    assert Model.clientModel.service.get_thickness(9).stiffness_matrix_area_density == 10
    assert Model.clientModel.service.get_thickness(9).stiffness_matrix_coefficient_of_thermal_expansion == 1
    assert Model.clientModel.service.get_thickness(9).D33 == 33000
    assert Model.clientModel.service.get_thickness(9).D67 == 67000
    assert Model.clientModel.service.get_thickness(9).D28 == 28000