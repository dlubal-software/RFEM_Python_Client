import sys
import os
import pytest
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn
from RFEM.initModel import Model, SetAddonStatus, getPathToRunningRFEM
from RFEM.connectionGlobals import url
from RFEM.Results.designOverview import GetDesignOverview, GetPartialDesignOverview
from RFEM.Reports.partsList import GetPartsListAllByMaterial, GetPartsListMemberRepresentativesByMaterial
from RFEM.Reports.partsList import GetPartsListMemberSetsByMaterial, GetPartsListMembersByMaterial
from RFEM.Reports.partsList import GetPartsListSolidsByMaterial, GetPartsListSurfacessByMaterial

if Model.clientModel is None:
    Model()

@pytest.mark.skipif(url != 'http://127.0.0.1', reason="This test fails on remote PC due to incorrect file path. \
                    Althought it is easy to change, it would not be easy to update on every remote computer.\
                    It is not necessary to evaluate Client as functional. Localy this tests still gets executed.")

def test_designOverview():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.run_script(os.path.join(getPathToRunningRFEM(),'scripts\\internal\\Demos\\Demo-004 Bus Station-Concrete Design.js'))
    SetAddonStatus(Model.clientModel, AddOn.concrete_design_active)
    Model.clientModel.service.calculate_all(False)

    designOverview = GetDesignOverview()
    assert round(designOverview[0][0].row['design_ratio']) == 3
    assert designOverview[0][0].row['design_check_type'] == 'DM0210.00'

    partialDesignOverview = GetPartialDesignOverview(False)
    assert len(partialDesignOverview) > 1

    partialDesignOverview = GetPartialDesignOverview(True)
    assert len(partialDesignOverview) > 1

    a = GetPartsListAllByMaterial()
    assert len(a[0]) == 5
    assert a[0][0].row['volume'] == a[0][1].row['volume']

    b = GetPartsListMemberRepresentativesByMaterial()
    assert b == ''

    c = GetPartsListMemberSetsByMaterial()
    assert c == ''

    d = GetPartsListMembersByMaterial()
    assert len(d[0][0].row) == 13
    assert d[0][0].row['members_no'] == '1'

    e = GetPartsListSolidsByMaterial()
    assert e == ''

    f = GetPartsListSurfacessByMaterial()
    assert len(f[0][0].row) == 13
    assert 'Uniform | d : 120.0 mm | 2 - C20/25' in f[0][0].row['thickness_name']
