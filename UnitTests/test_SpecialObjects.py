import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface
from RFEM.SpecialObjects.intersection import Instersection
from RFEM.SpecialObjects.surfaceResultAdjustment import SurfaceResultsAdjustment
from RFEM.SpecialObjects.surfaceContact import SurfaceContact
from RFEM.SpecialObjects.resultSection import ResultSection
from RFEM.SpecialObjects.structureModification import StructureModification
from RFEM.TypesForSpecialObjects.surfaceContactType import SurfaceContactType
from RFEM.enums import SurfaceResultsAdjustmentShape, SurfaceResultsAdjustmentType, SurfaceResultsAdjustmentProjection
from RFEM.enums import SurfaceContactPerpendicularType, SurfaceContactParallelType, SurfaceContactFrictionType
from RFEM.enums import ResultSectionType, ResultSectionProjection, ResultSectionResultDirection

# Rigid Links tested separately in test_RigidLinks.py

if Model.clientModel is None:
    Model()

def test_special_objects():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Thickness
    Thickness(1, '1', 1, 0.01)

    # Create Nodes
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 0.0, 2.0, 0.0)
    Node(3, 2.0, 2.0, 0.0)
    Node(4, 2.0, 0.0, 0.0)
    Node(5, 0.0, 4.0, 0.0)
    Node(6, 2.0, 4.0, 0.0)

    Node(7, 0.0, 0.0, 1)
    Node(8, 0.0, 2.0, 1)
    Node(9, 2.0, 2.0, 1)
    Node(10, 2.0, 0.0, 1)
    Node(11, 0.0, 4.0, 1)
    Node(12, 2.0, 4.0, 1)

    # Create Lines
    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line(5, '2 5')
    Line(6, '5 6')
    Line(7, '6 3')

    Line(8, '7 8')
    Line(9, '8 9')
    Line(10, '9 10')
    Line(11, '10 7')
    Line(12, '8 11')
    Line(13, '11 12')
    Line(14, '12 9')

    # Create Surfaces
    Surface(1, '1 2 3 4', 1)
    Surface(2, '2 5 6 7', 1)

    Surface(3, '8 9 10 11', 1)
    Surface(4, '12 13 14 9', 1)

    Instersection()

    SurfaceResultsAdjustment(1,SurfaceResultsAdjustmentShape.SHAPE_RECTANGLE, [1,1.2,0])

    SurfaceContactType(1, SurfaceContactPerpendicularType.FULL_FORCE_TRANSMISSION, SurfaceContactParallelType.ELASTIC_FRICTION, [2000, SurfaceContactFrictionType.FRICTION_COEFFICIENT, 0.25])
    SurfaceContactType.FullForce(2)
    SurfaceContactType.RigidFriction(3)
    SurfaceContactType.ElasticFriction(4)
    SurfaceContactType.ElasticSurface(5)

    SurfaceContact(1, 1, '1', '3')

    ResultSection(1,ResultSectionType.TYPE_2_POINTS_AND_VECTOR, ResultSectionResultDirection.SHOW_RESULTS_IN_GLOBAL_MINUS_X,True,[1, [1,0,0], [0,2,0], ResultSectionProjection.PROJECTION_IN_VECTOR, [1,1,1]],)
    ResultSection.Line(2,ResultSectionResultDirection.SHOW_RESULTS_IN_LOCAL_PLUS_Z,False, '2')
    ResultSection.TwoPointsAndVector(3,1,ResultSectionResultDirection.SHOW_RESULTS_IN_GLOBAL_MINUS_Y,False, [10,0,0], [5,5,5], ResultSectionProjection.PROJECTION_IN_GLOBAL_X)
    ResultSection.TwoPointsAndVector(4,1,ResultSectionResultDirection.SHOW_RESULTS_IN_GLOBAL_MINUS_Y,False, [10,0,0], [5,5,5], ResultSectionProjection.PROJECTION_IN_VECTOR, [-1,1,-1])

    StructureModification()


    Model.clientModel.service.finish_modification()