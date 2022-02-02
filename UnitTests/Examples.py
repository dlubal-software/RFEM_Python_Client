import os
import sys
import subprocess
from fnmatch import fnmatch
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

root = PROJECT_ROOT+"\\Examples"
pattern = "*.py"

def test_examples():
    """
    Run this function in order to execute all *.py files in Examples folder.
    This routine is exempt from standard pytest collection because it requires manual input.
    """
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern) and name != "__init__.py":
                example = os.path.join(path, name)
                subprocess.call(example, shell=True)
