import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn
from RFEM.initModel import Model, GetAddonStatus
from RFEM.Results.designOverview import GetDesignOverview, GetPartialDesignOverview
from RFEM.Reports.partsList import GetPartsListAllByMaterial, GetPartsListMemberRepresentativesByMaterial
from RFEM.Reports.partsList import GetPartsListMemberSetsByMaterial, GetPartsListMembersByMaterial
from RFEM.Reports.partsList import GetPartsListSolidsByMaterial, GetPartsListSurfacessByMaterial

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

    a = GetPartsListAllByMaterial()
    assert len(a[0]) == 5
    assert a[0][0]['volume'] == a[0][1]['volume']

    b = GetPartsListMemberRepresentativesByMaterial()
    assert b == ''

    c = GetPartsListMemberSetsByMaterial()
    assert c == ''

    d = GetPartsListMembersByMaterial()
    assert len(d[0]) == 5
    assert d[0][0]['no'] == 1
    assert round(d[0][0]['total_weight']) == 1200
    assert round(d[0][-1]['total_weight']) == 2300

    e = GetPartsListSolidsByMaterial()
    assert e == ''

    f = GetPartsListSurfacessByMaterial()
    assert len(f[0]) == 6
    assert f[0][1]['thickness_name'] == 'Uniform | d : 120.0 mm | 2 - C20/25'

    GetAddonStatus(Model.clientModel, AddOn.concrete_design_active)
