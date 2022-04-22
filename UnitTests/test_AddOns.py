import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
import RFEM.dependencies
from RFEM.enums import AddOn
from RFEM.initModel import Model, SetAddonStatus, GetAddonStatus

if Model.clientModel is None:
    Model()

def test_AddOns():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, True)
    SetAddonStatus(Model.clientModel, AddOn.concrete_design_active, True)
    SetAddonStatus(Model.clientModel, AddOn.modal_active, True)
    SetAddonStatus(Model.clientModel, AddOn.building_model_active, True)
    Model.clientModel.service.finish_modification()

    assert GetAddonStatus(Model.clientModel, AddOn.structure_stability_active)
    assert GetAddonStatus(Model.clientModel, AddOn.concrete_design_active)
    assert GetAddonStatus(Model.clientModel, AddOn.modal_active)
    assert GetAddonStatus(Model.clientModel, AddOn.building_model_active)

    Model.clientModel.service.begin_modification()
    SetAddonStatus(Model.clientModel, AddOn.structure_stability_active, False)
    SetAddonStatus(Model.clientModel, AddOn.concrete_design_active, False)
    SetAddonStatus(Model.clientModel, AddOn.modal_active, False)
    SetAddonStatus(Model.clientModel, AddOn.building_model_active, False)
    Model.clientModel.service.finish_modification()
