import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.dataTypes import inf
from RFEM.initModel import Model
from RFEM.enums import *
from RFEM.BasicObjects.node import Node
from RFEM.SpecialObjects.lineReleaseType import LineReleaseType

if Model.clientModel is None:
    Model()

def test_LineReleaseType():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0)

    LineReleaseType(1, [0.2, 0, 0, 0.1], [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE], [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE], \
        [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.1, 0.2], [PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE, 0.3, 1500]], \
        [RotationalReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM, [True, LineReleaseDiagram.DIAGRAM_ENDING_TYPE_FAILURE], [[0.01, 1000], [0.02, 2000], [0.03, 500]]], LineReleaseLocalAxisSystem.LOCAL_AXIS_SYSTEM_TYPE_ORIGINAL_LINE, [0.2], 'Type 1'
        )

    LineReleaseType(2, [0.2, 0, 0, 0.1], [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE], [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE], \
        [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM, [False, LineReleaseDiagram.DIAGRAM_ENDING_TYPE_YIELDING, LineReleaseDiagram.DIAGRAM_ENDING_TYPE_CONTINUOUS], [[0,0], [0.01, 1000], [0.02, 2000], [0.03, 500]]], \
        [RotationalReleaseNonlinearity.NONLINEARITY_TYPE_FORCE_MOMENT_DIAGRAM, [True, LineReleaseForceMomentDiagram.FORCE_MOMENT_DIAGRAM_ENDING_TYPE_YIELDING, LineReleaseForceMomentDepend.FORCE_MOMENT_DIAGRAM_DEPENDS_ON_N], [[1500, 100], [2500, 200], [3000, 450]]], \
        LineReleaseLocalAxisSystem.E_LOCAL_AXIS_SYSTEM_TYPE_HELP_NODE, [0.3, 1, LocalAxisSystemObjectInPlane.LOCAL_AXIS_SYSTEM_IN_PLANE_XY], 'Type 2'
        )

    Model.clientModel.service.finish_modification()

    lrt_1 = Model.clientModel.service.get_line_release_type(1)
    assert lrt_1.partial_activity_along_z_negative_type == "PARTIAL_ACTIVITY_TYPE_FIXED"
    assert lrt_1.partial_activity_along_z_positive_force == 1500
    assert lrt_1.diagram_around_x_start == "DIAGRAM_ENDING_TYPE_FAILURE"
    assert lrt_1.diagram_around_x_table[0][0].row['rotation'] == 0.01
    assert lrt_1.diagram_around_x_table[0][1].row['moment'] == 2000

    lrt_2 = Model.clientModel.service.get_line_release_type(2)
    assert lrt_2.diagram_along_z_end == "DIAGRAM_ENDING_TYPE_CONTINUOUS"
    assert lrt_2.diagram_along_z_table[0][3].row['force'] == 500
    assert lrt_2.force_moment_diagram_around_x_end == "FORCE_MOMENT_DIAGRAM_ENDING_TYPE_YIELDING"
    assert lrt_2.force_moment_diagram_around_x_table[0][0].row['force'] == 1500
    assert lrt_2.force_moment_diagram_around_x_table[0][2].row['max_moment'] == 450
