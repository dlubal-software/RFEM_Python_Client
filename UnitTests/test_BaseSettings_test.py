import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
import pytest
from RFEM.enums import *
from RFEM.baseSettings import BaseSettings
from RFEM.initModel import method_exists

def test_base_settings_implemented():

    exist = method_exists(clientModel,'set_model_settings_and_options')
    assert exist == False #test fail once method is in T9 master or GM

@pytest.mark.skip("all tests still WIP")
def test_baseSettings():

    Model.clientModel.service.begin_modification()

    # Set Base Settings
    BaseSettings(12, GlobalAxesOrientationType.E_GLOBAL_AXES_ORIENTATION_ZUP, LocalAxesOrientationType.E_LOCAL_AXES_ORIENTATION_ZUP, [0.001, 0.002, 0.003, 0.004])

    print('Ready!')

    Model.clientModel.service.finish_modification()

