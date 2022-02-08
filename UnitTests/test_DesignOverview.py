import sys
import os
dirName = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(
                  dirName,
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.Results.designOverview import GetDesignOverview, GetPartialDesignOverview

if Model.clientModel is None:
    Model()

def test_designOverview():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.run_script('..\\scripts\\internal\\Demos\\Demo-004 Bus Station-Concrete Design.js')
    Model.clientModel.service.calculate_all(False)

    designOverview = GetDesignOverview()
    assert designOverview[0][0]['design_ratio'] == 2.851
    assert designOverview[0][0]['design_check_type'] == 'DM0210.00'

    partialDesignOverview = GetPartialDesignOverview(False)
    assert len(partialDesignOverview) == 18

    partialDesignOverview = GetPartialDesignOverview(True)
    assert len(partialDesignOverview) == 37

