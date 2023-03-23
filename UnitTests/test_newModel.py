import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, client
from RFEM.enums import ApplicationTypes
from RFEM.newModel import NewModelAsCopy, NewModelFromTemplate
import suds

if Model.clientModel is None:
    Model()

def test_NewModelAsCopy():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    NewModelAsCopy('Model1', 'C:...yourpath')

    Model.clientModel.service.finish_modification()

    nm = client.service.new_model_as_copy()

    assert nm.model_name == 'Model1'
    assert type(nm.file_path) == str

def test_NewModelFromTemplate():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    NewModelFromTemplate('Model1', 'C:...yourpath')

    Model.clientModel.service.finish_modification()

    nm = client.service.new_model_from_template()

    assert nm.model_name == 'Model1'
    assert type(nm.file_path) == str
