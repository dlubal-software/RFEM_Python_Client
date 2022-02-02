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
from RFEM.initModel import Model, CheckIfMethodOrTypeExists
# Unused imports are displayed in dark green as one below.
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
# If no specific need to atomize the testing procedure, pack as much funtionality as possible in one test function.
# Write sepatate test when used method/type is not in RFEM yet, to be able to skip it for example.
def template():
    """
    Optional docstring describing the testing procedure
    """
    # In every test function run 'delete_all' first to clean up the model. It deletes mesh, results and all objects.
    # reset() on the other hand erases modification stack and all objects.
    # If you run reset() inside modification stack (from begin_modification to finish_modification),
    # all modifications will not take place.
    Model.clientModel.service.delete_all()

    # Speed up the execution of the test.
    Model.clientModel.service.begin_modification()

    # Body of testing procedure

    # IMPORTANT:
    # Every functionality needs to be tested only once.
    # Avoid extensive duplicating since it only adds to cost of maintaining tests.
    # DON'T USE Calculate_all function in unit tests. It works when executing tests
    # individualy but when running all of them it causes RFEM to stuck and generates
    # failures, which are hard to investigate.

    # The best way to test corrrectness is by using asserts.
    # Get the object set by test and verify its parameterts. Asserts are
    # well recieved by pytest and messages are reported to user.
    # Always test type specific parameters if possible.
    # If not, test some general ones like type or length.
    assert Model.clientModel is not None, "WARNING: clientModel is not initialized"
    #assert member.length == 5
    #assert member.result_beam_z_minus == 4

    # COMMENTS
    # Broken object or type can by commented out assuming author will add
    # associated bug number so everybody else can understand and track the issue.
    # Also adding 'TODO' keyword is prudent practise.


    Model.clientModel.service.finish_modification()

# No print("Ready") is necessary. Pytest doesn't print stdout to user if not specified or asserted.
# No return code is necessary. Pytest doesn't use it.

# BEFORE COMMIT:
    # - use formating (SHIFT + ALT + F) & linter (pylint UnitTests\template.py)
    # - clean up all unused/prototype code
    # - run all tests and examples to ensure everything works

### END OF UNIT TEST TEMPLATE ###
