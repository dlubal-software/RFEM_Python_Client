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
from RFEM.SpecialObjects.nodalReleaseType import NodalReleaseType

if Model.clientModel is None:
    Model()

def test_LineReleaseType():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0)


    NodalReleaseType(1, 'Local', 0.0, 1.0, 2.0, 1.5, 1.0, 2.0, [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY] , [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY], \
                    translational_release_vz_nonlinearity=[NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], rotational_release_mt_nonlinearity=[NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], \
                    rotational_release_my_nonlinearity=[NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], rotational_release_mz_nonlinearity=[NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE], \
                    local_axis_system=NodalReleaseTypeLocalAxisSystemObjectType.LOCAL_AXIS_SYSTEM_OBJECT_TYPE_MEMBER, local_axis_system_reference_object=1)

    Model.clientModel.service.finish_modification()

    nrt_1 = Model.clientModel.service.get_nodal_release_type(1)
    print(nrt_1)
    # assert nrt_1.partial_activity_along_x_negative_type == "PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE"
    # assert nrt_1.partial_activity_along_y_positive_force == 1500
    # assert nrt_1.diagram_around_x_start == "DIAGRAM_ENDING_TYPE_FAILURE"
    # assert lrt_1.diagram_around_x_table[0][0].row['rotation'] == 0.01
    # assert lrt_1.diagram_around_x_table[0][1].row['moment'] == 2000

test_LineReleaseType()
