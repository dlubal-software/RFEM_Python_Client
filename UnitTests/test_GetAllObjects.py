import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model, getPathToRunningRFEM
from RFEM.Tools.GetObjectNumbersByType import GetAllObjects

if Model.clientModel is None:
    Model()

def test_GetAllObjects():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.run_script(os.path.join(getPathToRunningRFEM(),'scripts\\internal\\Demos\\Demo-002 Cantilever Beams.js'))

    objects, imports = GetAllObjects()

    assert len(imports) > 18
    assert len(objects) > 160
