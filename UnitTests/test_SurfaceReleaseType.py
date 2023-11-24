import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.enums import *
from RFEM.dataTypes import inf
from RFEM.TypesForSpecialObjects.surfaceReleaseType import SurfaceReleaseType

if Model.clientModel is None:
    Model()

def test_SurfaceReleaseType():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SurfaceReleaseType(1, [inf, 1, 0.1], SurfaceTranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE, SurfaceTranslationalReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE,
                       SurfaceTranslationalReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE, SurfaceReleaseTypeLocalAxisSystemType.LOCAL_AXIS_SYSTEM_TYPE_SAME_AS_ORIGINAL_SURFACE,
                       name = 'Surface Release')

    Model.clientModel.service.finish_modification()

    sr = Model.clientModel.service.get_surface_release_type(1)

    assert sr.translational_release_u_y == 1
    assert sr.name == 'Surface Release'
