import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.thickness import Thickness
from RFEM.TypesForLines.lineSupport import LineSupport
from RFEM.TypesForLines.lineHinge import LineHinge
from RFEM.TypesForLines.lineWeldedJoint import LineWeldedJoint
from RFEM.TypesForLines.lineMeshRefinements import LineMeshRefinements


if Model.clientModel is None:
    Model()

def test_typesForLines():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Thickness(1, 'Thick', 1, 0.35)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 5, 5, 0)
    Node(4, 0, 5, 0)
    Node(5,2.5,2.5,-2.5)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '1 3')
    Line(6, '1 5')
    Line(7, '5 3')

    Surface(1, '1,2,5')
    Surface(2, '3,4,5')
    Surface(3, '5-7')

    LineSupport(1,'1', LineSupportType.HINGED)
    LineSupport(2,'2', LineSupportType.FREE)

    slab = LineHinge.slabWallConnection
    LineHinge(1,'2/5', params=slab)

    LineWeldedJoint(1,'5','1 2', LineWeldedJointType.BUTT_JOINT, WeldType.WELD_SINGLE_V, 0.005)

    params = LineMeshRefinements.TypeSpecificParams
    LineMeshRefinements(1,'3', LineMeshRefinementsType.TYPE_LENGTH, 2, '', params)

    LineMeshRefinements.TargetFELength(2, '4', 0.05)
    LineMeshRefinements.NumberFiniteElements(3,'5',15)
    LineMeshRefinements.Gradually(4,'6',4)

    Model.clientModel.service.finish_modification()

    assert Model.clientModel.service.get_line_support(1).rotational_restraint['x'] == 0
    assert Model.clientModel.service.get_line_support(1).rotational_restraint['y'] == 0
    assert Model.clientModel.service.get_line_support(1).rotational_restraint['z'] == 0
    assert Model.clientModel.service.get_line_support(1).spring['x'] > 10e100
    assert Model.clientModel.service.get_line_support(1).spring['y'] > 10e100
    assert Model.clientModel.service.get_line_support(1).spring['z'] > 10e100

    assert Model.clientModel.service.get_line_support(2).rotational_restraint['x'] == 0
    assert Model.clientModel.service.get_line_support(2).rotational_restraint['y'] == 0
    assert Model.clientModel.service.get_line_support(2).rotational_restraint['z'] == 0
    assert Model.clientModel.service.get_line_support(2).spring['x'] == 10000
    assert Model.clientModel.service.get_line_support(2).spring['y'] == 0
    assert Model.clientModel.service.get_line_support(2).spring['z'] == 0

    assert Model.clientModel.service.get_line_welded_joint(1).joint_type == 'BUTT_JOINT'
    assert Model.clientModel.service.get_line_welded_joint(1).weld_type == 'WELD_SINGLE_V'
    assert round(Model.clientModel.service.get_line_welded_joint(1).weld_size_a1, 3) == 0.005

    assert Model.clientModel.service.get_line_mesh_refinement(1).type == 'TYPE_LENGTH'
    assert Model.clientModel.service.get_line_mesh_refinement(1).lines == '3'
    assert Model.clientModel.service.get_line_mesh_refinement(1).number_of_layers == 2

    assert Model.clientModel.service.get_line_mesh_refinement(3).type == 'TYPE_ELEMENTS'
    assert Model.clientModel.service.get_line_mesh_refinement(3).elements_finite_elements == 15

    assert Model.clientModel.service.get_line_mesh_refinement(4).type == 'TYPE_GRADUAL'
    assert Model.clientModel.service.get_line_mesh_refinement(4).gradual_rows == 4
