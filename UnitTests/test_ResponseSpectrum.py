import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, SetAddonStatus
from RFEM.enums import AddOn
from RFEM.DynamicLoads.responseSpectrum import ResponseSpectrum


if Model.clientModel is None:
    Model()

def test_response_spectrum():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    SetAddonStatus(Model.clientModel, AddOn.spectral_active)

    # create user defined response spectrum
    ResponseSpectrum(2, user_defined_spectrum=[[0, 0.66], [0.15, 1.66]])
    ResponseSpectrum.UserDefinedGFactor(3, 'secondSpectrum', 0.12, True, [[1, 0.5], [2, 1]])
    Model.clientModel.service.finish_modification()

    rsp_2 = Model.clientModel.service.get_response_spectrum(2)
    rsp_3 = Model.clientModel.service.get_response_spectrum(3)

    assert rsp_2.no == 2
    assert rsp_3.user_defined_response_spectrum_period_step == 0.12
    assert round(rsp_2.user_defined_response_spectrum[0][0]['row']['acceleration'], 2) == 0.66
    assert round(rsp_2.user_defined_response_spectrum[0][1]['row']['period'], 2) == 0.15

