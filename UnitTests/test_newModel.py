import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, client, NewModelAsCopy

if Model.clientModel is None:
    Model()

def test_NewModelAsCopy():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    NewModelAsCopy('test_old.rf6', r'C:\Program Files\Dlubal\RFEM 6.02\models\TestFolder')

    Model.clientModel.service.finish_modification()

    modelList = client.service.get_model_list()
    inList = False
    if 'test_old_copy' in modelList[0]:
        inList = True

    assert inList == True
