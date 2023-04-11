# Pytest fixtures
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model, closeAllModels

def pytest_exception_interact():
    '''
    Called when an exception was raised which can potentially be interactively handled,
    in our case after the failed test.
    '''

    # This ensures that the tests executed after failed test are not affected.
    if Model.clientModel:
        closeAllModels()
    Model()
