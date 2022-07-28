import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
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
    SetAddonStatus(Model.clientModel, AddOn.stress_analysis_active, True)
    SetAddonStatus(Model.clientModel, AddOn.steel_design_active, True)
    SetAddonStatus(Model.clientModel, AddOn.timber_design_active, True)
    SetAddonStatus(Model.clientModel, AddOn.aluminum_design_active, True)
    SetAddonStatus(Model.clientModel, AddOn.steel_joints_active, True)
    #SetAddonStatus(Model.clientModel, AddOn.timber_joints_active, True)                :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    #SetAddonStatus(Model.clientModel, AddOn.craneway_design_active, True)              :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    SetAddonStatus(Model.clientModel, AddOn.masonry_design_active, True)
    SetAddonStatus(Model.clientModel, AddOn.multilayer_surfaces_design_active, True)
    SetAddonStatus(Model.clientModel, AddOn.material_nonlinear_analysis_active, True)
    SetAddonStatus(Model.clientModel, AddOn.construction_stages_active, True)
    SetAddonStatus(Model.clientModel, AddOn.time_dependent_active, True)
    SetAddonStatus(Model.clientModel, AddOn.form_finding_active, True)
    #SetAddonStatus(Model.clientModel, AddOn.cutting_patterns_active, True)             :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    SetAddonStatus(Model.clientModel, AddOn.torsional_warping_active, True)
    SetAddonStatus(Model.clientModel, AddOn.cost_estimation_active, True)
    SetAddonStatus(Model.clientModel, AddOn.spectral_active, True)
    #SetAddonStatus(Model.clientModel, AddOn.time_history_active, True)                 :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    #SetAddonStatus(Model.clientModel, AddOn.pushover_active, True)                     :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    #SetAddonStatus(Model.clientModel, AddOn.harmonic_response_active, True)            :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    #SetAddonStatus(Model.clientModel, AddOn.wind_simulation_active, True)              :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    SetAddonStatus(Model.clientModel, AddOn.geotechnical_analysis_active, True)

    Model.clientModel.service.finish_modification()

    assert GetAddonStatus(Model.clientModel, AddOn.structure_stability_active)
    assert GetAddonStatus(Model.clientModel, AddOn.concrete_design_active)
    assert GetAddonStatus(Model.clientModel, AddOn.modal_active)
    assert GetAddonStatus(Model.clientModel, AddOn.building_model_active)
    assert GetAddonStatus(Model.clientModel, AddOn.stress_analysis_active)
    assert GetAddonStatus(Model.clientModel, AddOn.steel_design_active)
    assert GetAddonStatus(Model.clientModel, AddOn.timber_design_active)
    assert GetAddonStatus(Model.clientModel, AddOn.aluminum_design_active)
    assert GetAddonStatus(Model.clientModel, AddOn.steel_joints_active)
    #assert GetAddonStatus(Model.clientModel, AddOn.timber_joints_active)               :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    #assert GetAddonStatus(Model.clientModel, AddOn.craneway_design_active)             :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    assert GetAddonStatus(Model.clientModel, AddOn.masonry_design_active)
    assert GetAddonStatus(Model.clientModel, AddOn.multilayer_surfaces_design_active)
    assert GetAddonStatus(Model.clientModel, AddOn.material_nonlinear_analysis_active)
    assert GetAddonStatus(Model.clientModel, AddOn.construction_stages_active)
    assert GetAddonStatus(Model.clientModel, AddOn.time_dependent_active)
    assert GetAddonStatus(Model.clientModel, AddOn.form_finding_active)
    #assert GetAddonStatus(Model.clientModel, AddOn.cutting_patterns_active)            :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    assert GetAddonStatus(Model.clientModel, AddOn.torsional_warping_active)
    assert GetAddonStatus(Model.clientModel, AddOn.cost_estimation_active)
    assert GetAddonStatus(Model.clientModel, AddOn.spectral_active)
    #assert GetAddonStatus(Model.clientModel, AddOn.time_history_active)                :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    #assert GetAddonStatus(Model.clientModel, AddOn.pushover_active)                    :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    #assert GetAddonStatus(Model.clientModel, AddOn.harmonic_response_active)           :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    #assert GetAddonStatus(Model.clientModel, AddOn.wind_simulation_active)             :   Add-Ons greyed out in RFEM GUI. Assumedly still WIP
    assert GetAddonStatus(Model.clientModel, AddOn.geotechnical_analysis_active)
