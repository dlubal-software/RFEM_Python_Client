import sys
sys.path.append(".")
import pytest
from RFEM.enums import *
from RFEM.baseSettings import *


def test_base_settings_implemented():

    exist = method_exists(clientModel,'set_model_settings_and_options')
    assert exist == False #test fail once method is in T9 master or GM


@pytest.mark.skip("all tests still WIP")
def test_baseSettings():

    clientModel.service.begin_modification()

    # Set Base Settings
    BaseSettings(12, GlobalAxesOrientationType.E_GLOBAL_AXES_ORIENTATION_ZUP, LocalAxesOrientationType.E_LOCAL_AXES_ORIENTATION_ZUP, [0.001, 0.002, 0.003, 0.004])

    print('Ready!')

    clientModel.service.finish_modification()

