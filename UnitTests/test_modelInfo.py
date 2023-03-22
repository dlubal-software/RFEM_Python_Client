import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, client
from RFEM.enums import ApplicationTypes
from RFEM.modelInfo import ModelParameters, SessionId, ApplicationInfo
import suds

if Model.clientModel is None:
    Model()

def test_ModelParameters():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    ModelParameters([['Client Name', 'ABC', 'c'], ['Company name', 'Dlubal Software GmbH', 'g'], ['Project name', 'Cantilever', 'h']])

    Model.clientModel.service.finish_modification()

    mp = Model.clientModel.service.get_model_parameters()

    assert mp.model_parameters[0].no == 1
    assert mp.model_parameters[2].row['name'] == 'Client Name'
    assert mp.model_parameters[3].row['description_1'] == 'Dlubal Software GmbH'
    assert mp.model_parameters[4].row['description_2'] == 'h'

def test_SessionID():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SessionId()

    Model.clientModel.service.finish_modification()

    s = Model.clientModel.service.get_session_id()
    x = type(s)

    assert x == suds.sax.text.Text

def test_ApplicationName():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    ApplicationInfo.GetName('RFEM 6.02.0054', ApplicationTypes.RFEM6)

    Model.clientModel.service.finish_modification()

    an = client.service.get_information()

    assert an.name == 'RFEM 6.02.0054'
    assert an.type == 'RFEM6'

def test_ApplicationVersion():
    pass

def test_ApplicationLanguage():
    pass
