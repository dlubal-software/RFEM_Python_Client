import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import insertSpaces

def test_insertSpaces():
    """
    Test conversion of list to string with spaces between items
    """
    assert insertSpaces([1, 2, 3]) == "1 2 3"

