import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
import pytest
from RFEM.enums import GlobalAxesOrientationType, LocalAxesOrientationType
from RFEM.baseSettings import BaseSettings
from RFEM.initModel import Model, CheckIfMethodOrTypeExists

if Model.clientModel is None:
    Model()

# TODO: US-8005
@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'ns0:model_settings_and_options_type', True), reason="ns0:model_settings_and_options_type not in RFEM GM yet")
def test_baseSettings():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Set Base Settings
    BaseSettings(12, GlobalAxesOrientationType.E_GLOBAL_AXES_ORIENTATION_ZUP, LocalAxesOrientationType.E_LOCAL_AXES_ORIENTATION_ZUP, [0.001, 0.002, 0.003, 0.004])

    Model.clientModel.service.finish_modification()
