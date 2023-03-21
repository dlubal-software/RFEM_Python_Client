import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.enums import ModelHistoryStatusType, ModelLocationRowType, ModelType
from RFEM.modelInfo import ModelHistory, ModelParameters, ModelMainParameters, ModelInfo
from RFEM.BasicObjects.node import Node

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

def test_ModelMainParameters():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    ModelMainParameters(['ID1236', 'ABC', 'tralala', 'hupsi', 'C:\...\your\path'], ['ID4567','Company name', 'Dlubal Software GmbH - schwups', 'folder'])

    Model.clientModel.service.finish_modification()

    mp = Model.clientModel.service.get_model_main_parameters()

    assert mp.model_main_parameters[0][0] == 'ID1232'
    assert mp.model_main_parameters[0][2] == 'tralala'
    assert mp.model_main_parameters[1][2] == 'Dlubal Software GmbH - schwups'
    assert mp.model_main_parameters[1][3]== 'folder'

