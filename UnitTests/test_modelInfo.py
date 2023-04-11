import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, client
from RFEM.initModel import GetModelParameters, GetModelMainParameters, GetModelId, GetName, GetLanguage, GetVersion

if Model.clientModel is None:
    Model()

def test_ModelParameters():

    Model.clientModel.service.delete_all()

    m = GetModelParameters()

    assert m.model_parameters[0].no == 1
    assert m.model_parameters[2].row['name'] == 'Client name'
    assert m.model_parameters[1].row['description_2'] == 'Unique project identifier'
    assert m.model_parameters[3].row['description_2'] in [None, 'g']

def test_ModelMainParameters():

    Model.clientModel.service.delete_all()

    m = GetModelMainParameters()
    mi = GetModelId()

    act_mi = Model.clientModel.service.get_model_main_parameters().model_id

    assert m.model_name == 'TestModel'
    assert mi == act_mi

def test_Application():

    Model.clientModel.service.delete_all()

    name = GetName()
    version = GetVersion()
    language = GetLanguage()

    an = client.service.get_information()

    assert an.name == name
    assert an.version == version
    assert an.language_name == language
