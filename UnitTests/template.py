#########################################################
## This is the unit test template.
## All good practices and requirements related to unit tests
## will be recorded here. Feel free to add whatever you feel
## as important or new to unit tests and testing procedure.
#########################################################

# Name of the test module/file starts with test_...
# Feel free to start the unit test by copying the content of this file
# to ensure that the latest requirements are met.

# import only used modules
# avoid wild-card import (from RFEM.enums import *) is possible
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

import pytest
from RFEM.initModel import Model, CheckIfMethodOrTypeExists
# Unused imports are displayed in dark green.
from RFEM.enums import MemberType

# When running tests individually the Model needs to be explicitly initialized.
# If all tests are executed together this expresion is False.
if Model.clientModel is None:
    Model()

# 'pytestmark' sets same parameters (in this case 'skipif') to all functions in the module or class at once.
#pytestmark = pytest.mark.skipif(CheckIfMethodOrTypeExists(Model...

# Use 'skipif' if you wish to skip individual test function conditionally
@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model().clientModel,'set_model_settings_and_options', True), reason="set_model_settings_and_options not in RFEM yet")

# Name of the test function starts with test_...
# If no specific need to atomize the testing procedure, pack as much funtionality as possible in one test.
# Write sepatate test when used method/type is not in RFEM yet, to be able to skip it for example.
def template():
    """
    Optional docstring describing the testing procedure
    """
    # In every test function run 'reset' first to clean up the model.
    # It is important to run it before begin_modification or after finish_modification,
    # otherwise begin_modification doesn't take effect.
    Model.clientModel.service.reset()

    # Speed up the execution of the test.
    Model.clientModel.service.begin_modification()

    # Body of testing procedure
    # IMPORTANT:
    # Every functionality needs to be tested only once.
    # Avoid duplicating since it only adds to cost of maintaining tests.

    # The best way to test corrrectness is either run Calculate_all or asserts.
    # Get the object set by test and verify its parameterts. Asserts are
    # well recieved by pytest and messages are reported to user.
    assert Model.clientModel is not None, "WARNING: clientModel is not initialized"

    Model.clientModel.service.finish_modification()

# No print("Ready") is necessary. Pytest doesnt print stdout to user if not specified.
# No return code is necessary. Pytest doesn't use it.

# BEFORE COMMIT:
    # - use formating (SHIFT + ALT + F) & linter (pylint UnitTests\template.py)
    # - clean up all unused/prototype code
    # - run all tests and examples to ensure everything works

### END OF UNIT TEST TEMPLATE ###
