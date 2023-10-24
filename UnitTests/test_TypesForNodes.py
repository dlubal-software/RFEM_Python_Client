import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

import pytest
from RFEM.enums import NodalMeshRefinementType, NodalSupportType, NodalSupportNonlinearity, NodalSupportDiagramType, SupportPartialActivityAlongType, \
    SupportPartialActivityAroundType, SupportStiffnessDiagramDependOn, NodalSupportStiffnessDiagramType
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.opening import Opening
from RFEM.BasicObjects.thickness import Thickness
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForNodes.nodalMeshRefinement import NodalMeshRefinement, FElengthArrangement
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.dataTypes import inf


if Model.clientModel is None:
    Model()

def test_typesForNodes():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Thickness(1, "12mm", 1, 0.012)

    Node(1, 0,0,0)
    Node(2, 5,0,0)
    Node(3, 0,5,0)
    Node(4, 5,5,0)
    Node(5, 2,2,0)
    Node(6, 1,2,0)
    Node(7, 2,1,0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '3 4')
    Line(4, '1 3')
    Line.Circle(5, [2,2,0], 1, [0,0,1])

    Surface()

    Opening(1, '5')

    NodalSupport(1, '1 2', [inf, inf, inf, 0.0, 0.0, inf])
    NodalSupport(2, '3', NodalSupportType.FIXED)
    NodalSupport(3, '4', NodalSupportType.ROLLER_IN_X)
    with pytest.raises(ValueError):
        NodalSupport(4, '5', [inf, inf, inf, 0.0])

    NodalMeshRefinement(1, '8', NodalMeshRefinementType.TYPE_CIRCULAR, [0.3, 0.04, 0.08, FElengthArrangement.LENGTH_ARRANGEMENT_RADIAL])
    NodalMeshRefinement.Circular(2, '7', 0.6, 0.05, 0.09, FElengthArrangement.LENGTH_ARRANGEMENT_RADIAL)
    NodalMeshRefinement.Rectangular(3, '6', 0.8, 0.1, False)

    Model.clientModel.service.finish_modification()

    nodalSupport = Model.clientModel.service.get_nodal_support(1)
    assert nodalSupport.spring_x == inf
    assert nodalSupport.spring_y == inf
    assert nodalSupport.spring_z == inf
    assert nodalSupport.rotational_restraint_x == 0
    assert nodalSupport.rotational_restraint_y == 0
    assert nodalSupport.rotational_restraint_z == inf

    nodalSupport = Model.clientModel.service.get_nodal_support(2)
    assert nodalSupport.spring_x == inf
    assert nodalSupport.spring_y == inf
    assert nodalSupport.spring_z == inf
    assert nodalSupport.rotational_restraint_x == inf
    assert nodalSupport.rotational_restraint_y == inf
    assert nodalSupport.rotational_restraint_z == inf

    nodalSupport = Model.clientModel.service.get_nodal_support(3)
    assert nodalSupport.spring_x == 0
    assert nodalSupport.spring_y == inf
    assert nodalSupport.spring_z == inf
    assert nodalSupport.rotational_restraint_x == 0
    assert nodalSupport.rotational_restraint_y == 0
    assert nodalSupport.rotational_restraint_z == inf

    nodalMeshRefinement = Model.clientModel.service.get_nodal_mesh_refinement(1)
    assert nodalMeshRefinement.circular_radius == 0.3

    nodalMeshRefinement = Model.clientModel.service.get_nodal_mesh_refinement(2)
    assert nodalMeshRefinement.circular_target_inner_length == 0.05

    nodalMeshRefinement = Model.clientModel.service.get_nodal_mesh_refinement(3)
    assert nodalMeshRefinement.rectangular_side == 0.8

def test_nodalsupportnonlinearity():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, "S235")
    Thickness(1, "12mm", 1, 0.012)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 10, 0, 0)

    NodalSupport.Nonlinearity(1, "1", 1, [1.0, 2.0, inf, inf, 3, inf], [NodalSupportNonlinearity.NONLINEARITY_TYPE_DIAGRAM, [True, NodalSupportDiagramType.DIAGRAM_ENDING_TYPE_CONTINUOUS], [[0.5, 1], [1, 2], [2, 3]]], \
                              [NodalSupportNonlinearity.NONLINEARITY_TYPE_DIAGRAM, [False, NodalSupportDiagramType.DIAGRAM_ENDING_TYPE_FAILURE, NodalSupportDiagramType.DIAGRAM_ENDING_TYPE_YIELDING], [[-1, -1.5], [-0.5, -1], [0, 0], [1, 1], [2, 2.5]]], \
                                rotational_y_nonlinearity= [NodalSupportNonlinearity.NONLINEARITY_TYPE_DIAGRAM, [True, NodalSupportDiagramType.DIAGRAM_ENDING_TYPE_STOP], [[1,0.5], [2, 1], [3, 3]]], name='Nonlinear')

    NodalSupport.Nonlinearity(2, '2', 1, [100.0, 200.0, 0.1, 400, 300, 0.2], [NodalSupportNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [SupportPartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE], [SupportPartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 1]], \
                              [NodalSupportNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [SupportPartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.0, 2], [SupportPartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 3]], \
                              [NodalSupportNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE], [NodalSupportNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [SupportPartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.0, 150], [SupportPartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_FAILURE]], \
                              [NodalSupportNonlinearity.NONLINEARITY_TYPE_FAILURE_ALL_IF_POSITIVE], [NodalSupportNonlinearity.NONLINEARITY_TYPE_NONE], "Nonlinearity2")

    NodalSupport.Nonlinearity(3, '3', 1, [1,2,3,4,5,6], [NodalSupportNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1, 10], [NodalSupportNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2, 20], [NodalSupportNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2, 30, 40], \
                              [NodalSupportNonlinearity.NONLINEARITY_TYPE_STIFFNESS_DIAGRAM, [SupportStiffnessDiagramDependOn.STIFFNESS_DIAGRAM_DEPENDS_ON_PX, True, NodalSupportStiffnessDiagramType.STIFFNESS_DIAGRAM_ENDING_TYPE_YIELDING], [[1,1],[2,3],[3,4]]], \
                              [NodalSupportNonlinearity.NONLINEARITY_TYPE_STIFFNESS_DIAGRAM, [SupportStiffnessDiagramDependOn.STIFFNESS_DIAGRAM_DEPENDS_ON_PZ, False, NodalSupportStiffnessDiagramType.STIFFNESS_DIAGRAM_ENDING_TYPE_FAILURE, NodalSupportStiffnessDiagramType.STIFFNESS_DIAGRAM_ENDING_TYPE_CONTINUOUS], [[-2,-3],[-1.5,1],[0,0],[1,2],[2,5]]], \
                              [NodalSupportNonlinearity.NONLINEARITY_TYPE_STIFFNESS_DIAGRAM, [SupportStiffnessDiagramDependOn.STIFFNESS_DIAGRAM_DEPENDS_ON_P, True, NodalSupportStiffnessDiagramType.STIFFNESS_DIAGRAM_ENDING_TYPE_CONTINUOUS], [[0,1],[10,2],[15,4]]], 'Nonlinearity3')

    Model.clientModel.service.finish_modification()

    nsn = Model.clientModel.service.get_nodal_support(1)
    assert nsn.name == 'Nonlinear'
    assert nsn.spring_x_nonlinearity == 'NONLINEARITY_TYPE_DIAGRAM'
    assert nsn.diagram_along_y_table[0][0].row['displacement'] == -1
    assert nsn.rotational_restraint_y == 3

    nsn2 = Model.clientModel.service.get_nodal_support(2)
    assert nsn2.name == 'Nonlinearity2'
    assert nsn2.partial_activity_around_x_negative_type == 'PARTIAL_ACTIVITY_TYPE_FIXED'

    nsn3 = Model.clientModel.service.get_nodal_support(3)
    assert nsn3.name == 'Nonlinearity3'
    assert nsn3.spring_z_nonlinearity == 'NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2'
    assert nsn3.stiffness_diagram_around_y_symmetric == False
    assert nsn3.stiffness_diagram_around_z_table[0][2].row['force'] == 15
