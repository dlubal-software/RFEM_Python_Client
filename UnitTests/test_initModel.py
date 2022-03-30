#########################################################
## This is the unit test template.
## All good practices and requirements related to unit tests
## will be recorded here. Feel free to add whatever you feel
## as important or new to unit tests and testing procedure.
#########################################################

# Name of the test module/file starts with test_...
# Start the unit test by copying the content of this file
# to ensure that the latest requirements are met.

# import only used modules
# avoid wild-card import (from RFEM.enums import *) if possible
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

import pytest
from RFEM.initModel import insertSpaces
# Unused imports are displayed in dark green as one below.
from RFEM.enums import MemberType

# When running tests individually the Model needs to be explicitly initialized.
# If all tests are executed together this expresion is False.
#if Model.clientModel is None:
#    Model()

# 'pytestmark' sets same parameters (in this case 'skipif') to all functions in the module or class at once.
#pytestmark = pytest.mark.skipif(CheckIfMethodOrTypeExists(Model...

# Use 'skipif' if you wish to skip individual test function conditionally
#@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'set_model_settings_and_options', True), reason="set_model_settings_and_options not in RFEM yet")

# Name of the test function starts with test_...
# If no specific need to atomize the testing procedure, pack as much funtionality as possible in one test function.
# Write sepatate test when used method/type is not in RFEM yet, to be able to skip it for example.
def test_insertSpaces():
    """
    Test conversion of list to string with spaces between items
    """
    assert insertSpaces([1, 2, 3]) == "1 2 3"

