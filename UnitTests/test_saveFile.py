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

    Model.clientModel.service.delete_all()

    Material(1, 'S235')

    saveFile(dirName + r'/save')

    Model.clientModel.service.close_connection()

    modelS = Model(False, 'save')

    assert modelS.clientModel.service.get_material(1).name == "S235 | CYS EN 1993-1-1:2009-03"

    closeModel('save.rf6')

    if (os.path.isfile("save.rf6")):
        os.remove("save.rf6")
