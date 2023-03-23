import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, client
from RFEM.modelInfo import ModelParameters, ApplicationInfo, ModelMainParameters

if Model.clientModel is None:
    Model()

def test_ModelParameters():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    m = ModelParameters.ModelParameters()

    Model.clientModel.service.finish_modification()

    assert m.model_parameters[0].no == 1
    assert m.model_parameters[2].row['name'] == 'Client Name'
    assert m.model_parameters[3].row['description_1'] == 'Dlubal Software GmbH'
    assert m.model_parameters[4].row['description_2'] == 'h'


# Session ID changes with every call
# def test_ApplicationSessionID():

#     Model.clientModel.service.delete_all()
#     Model.clientModel.service.begin_modification()

#     sessionid = ApplicationSessionID.GetSessionId()

#     Model.clientModel.service.finish_modification()

#     s = client.service.get_session_id()

#     assert s == sessionid


def test_ModelMainParameters():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    m = ModelMainParameters.ModelMainParameters()
    mi = ModelMainParameters.ModelId()

    Model.clientModel.service.finish_modification()

    act_mi = Model.clientModel.service.get_model_main_parameters().model_id

    assert m.model_name == 'TestModel'
    assert mi == act_mi


def test_Application():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    name = ApplicationInfo.GetName()
    version = ApplicationInfo.GetVersion()
    language = ApplicationInfo.GetLanguage()

    Model.clientModel.service.finish_modification()

    an = client.service.get_information()

    assert an.name == name
    assert an.version == version
    assert an.language_name == language
