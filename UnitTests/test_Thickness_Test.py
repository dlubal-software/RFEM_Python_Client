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
                     consideration_of_self_weight= [ThicknessShapeOrthotropySelfWeightDefinitionType.SELF_WEIGHT_DEFINED_VIA_FICTITIOUS_THICKNESS, 0.234],
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
