import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model, closeModel

if Model.clientModel is None:
    Model()

def test_multiple_models_with_parameter():

    model1 = Model(True, 'TestModel5')
    Material(1,'S235', model = model1)

    model2 = Model(True, 'TestModel6')
    Material(2,'S235', model = model1)
    Material(3,'S275', model = model2)
    Material(4,'S235', model = model1)
    Material(5,'S275', model = model2)

    assert model1.clientModel.service.get_material(1).name == "S235 | CYS EN 1993-1-1:2009-03"
    assert model1.clientModel.service.get_material(2).name == "S235 | CYS EN 1993-1-1:2009-03"
    assert model1.clientModel.service.get_material(4).name == "S235 | CYS EN 1993-1-1:2009-03"

    assert model2.clientModel.service.get_material(3).name == "S275 | CYS EN 1993-1-1:2009-03"
    assert model2.clientModel.service.get_material(5).name == "S275 | CYS EN 1993-1-1:2009-03"

    closeModel(2)
    closeModel(1)

def test_multiple_models_calling_class():

    model1 = Model(True, 'TestModel5')
    Material(1,'S235')
    Material(2,'S235')

    model2 = Model(True, 'TestModel6')
    Material(3,'S275')

    Model(False, 'TestModel5')
    Material(4,'S235')

    Model(False, 'TestModel6')
    Material(5,'S275')

    assert model1.clientModel.service.get_material(1).name == "S235 | CYS EN 1993-1-1:2009-03"
    assert model1.clientModel.service.get_material(2).name == "S235 | CYS EN 1993-1-1:2009-03"
    assert model1.clientModel.service.get_material(4).name == "S235 | CYS EN 1993-1-1:2009-03"

    assert model2.clientModel.service.get_material(3).name == "S275 | CYS EN 1993-1-1:2009-03"
    assert model2.clientModel.service.get_material(5).name == "S275 | CYS EN 1993-1-1:2009-03"

    closeModel(2)
    closeModel(1)
