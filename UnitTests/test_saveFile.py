import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
dirName = os.path.dirname(__file__)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, saveFile, closeModel
from RFEM.BasicObjects.material import Material

if Model.clientModel is None:
    Model()

def test_SaveFile():

    if (os.path.isfile("/testResults/save.rf6")):
        os.remove("/testResults/save.rf6")

    Model(True, 'save.rf6')
    Model.clientModel.service.delete_all()

    Material(1, 'S235')

    saveFile(dirName + '/testResults/save.rf6')

    closeModel('save.rf6')

    assert os.path.isfile(dirName + "/testResults/save.rf6")
    os.remove(dirName + '/testResults/save.rf6')
