import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, client
from RFEM.newModel import NewModelAsCopy, NewModelFromTemplate

if Model.clientModel is None:
    Model()

def test_NewModelAsCopy():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    nm = NewModelAsCopy('TestModel.rf6')

    Model.clientModel.service.finish_modification()

    nmserver = client.service.new_model_as_copy().model_name

    assert nm.model_name == 'TestModel.rf6'


def test_NewModelFromTemplate():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    nm = NewModelFromTemplate()

    Model.clientModel.service.finish_modification()

    nmserver = client.service.new_model_from_template().model_name
    assert nm.model_name == nmserver
