import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, getPathToRunningRFEM
from RFEM.connectionGlobals import url
from RFEM.enums import NodalReleaseTypeReleaseNonlinearity, NodalReleaseTypePartialActivityAround, NodalReleaseTypeLocalAxisSystemObjectType
from RFEM.enums import NodalReleaseTypePartialActivityAlong, NodalReleaseTypeDiagram
from RFEM.TypesForSpecialObjects.nodalReleaseType import NodalReleaseType
import pytest

if Model.clientModel is None:
    Model()

@pytest.mark.skipif(url != 'http://127.0.0.1', reason="This test fails on remote PC due to incorrect file path. \
                    Althought it is easy to change, it would not be easy to update on every remote computer.\
                    It is not necessary to evaluate Client as functional. Localy this tests still gets executed.")

def test_NodalReleaseType():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Model.clientModel.service.run_script(os.path.join(getPathToRunningRFEM(),'scripts\\internal\\Demos\\Demo-002 Cantilever Beams.js'))

    NodalReleaseType(1, 'Local', 0.0, 1.0, 2.0, 1.5, 1.0, 2.0, [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE] , \
                    [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE, 0.3], [NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE, 1500.0, 0.3]], \
                    [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM, [True, NodalReleaseTypeDiagram.DIAGRAM_ENDING_TYPE_FAILURE], [[0.01, 1000], [0.02, 2000], [0.03, 500]]], \
                    [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], \
                    NodalReleaseTypeLocalAxisSystemObjectType.LOCAL_AXIS_SYSTEM_OBJECT_TYPE_MEMBER, 1)

    NodalReleaseType(2, 'Local', 0.0, 1.0, 2.0, 1.5, 1.0, 2.0, [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE, 1600, 0.2], [NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE, 1500.0, 0.3]] , \
                    [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM, [True, NodalReleaseTypeDiagram.DIAGRAM_ENDING_TYPE_FAILURE], [[0.01, 1000], [0.02, 2000], [0.03, 500]]], \
                    [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], \
                    [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FIXED, 0.6, 0.2], [NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT, 50.0, 0.4]], \
                    NodalReleaseTypeLocalAxisSystemObjectType.LOCAL_AXIS_SYSTEM_OBJECT_TYPE_MEMBER, 1)

    Model.clientModel.service.finish_modification()

    nrt_1 = Model.clientModel.service.get_nodal_release_type(1)
    assert nrt_1.partial_activity_along_y_positive_type == "PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE"
    assert nrt_1.partial_activity_along_y_positive_force == 1500
    assert nrt_1.diagram_around_x_start == "DIAGRAM_ENDING_TYPE_FAILURE"
    assert nrt_1.diagram_around_x_table[0][0].row['rotation'] == 0.01
    assert nrt_1.diagram_around_x_table[0][0].row['moment'] == 1000


    nrt_2 = Model.clientModel.service.get_nodal_release_type(2)
    assert nrt_2.axial_release_vy_nonlinearity == "NONLINEARITY_TYPE_DIAGRAM"
    assert nrt_2.partial_activity_along_x_positive_type == "PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE"
    assert nrt_2.partial_activity_along_x_negative_force == 1600
    assert nrt_2.partial_activity_around_z_positive_moment == 50
    assert nrt_2.diagram_along_y_start == "DIAGRAM_ENDING_TYPE_FAILURE"
    assert nrt_2.diagram_along_y_table[0][1].row['displacement'] == 0.02
    assert nrt_2.diagram_along_y_table[0][2].row['force'] == 500
