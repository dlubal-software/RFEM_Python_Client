import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.enums import ModelHistoryStatusType, ModelLocationRowType, ModelType
from RFEM.baseData import ModelHistory, ModelParameters, ModelParametersLocation, Modeltype
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

def test_ModelParametersLocation():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    ModelParametersLocation([[ModelLocationRowType.E_ROW_COUNTRY_ISO, 'Country', 'DEU', None], [ModelLocationRowType.E_ROW_STREET, 'Street', 'Lederstraße', None]])

    Model.clientModel.service.finish_modification()

    mpl = Model.clientModel.service.get_model_parameters_location()
    assert mpl.model_parameters_location[0].row['location_row_type'] == 'E_ROW_COUNTRY_ISO'
    assert mpl.model_parameters_location[1].row['name'] == 'Street'
    assert mpl.model_parameters_location[0].row['value'] == 'DEU'

def test_ModelType():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Modeltype(ModelType.E_MODEL_TYPE_2D_XY_3D)

    Model.clientModel.service.finish_modification()

    mt = Model.clientModel.service.get_model_type()

    assert mt == 'E_MODEL_TYPE_2D_XY_3D'
