import sys
import os
import pytest
from suds import WebFault

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model, getPathToRunningRFEM
from RFEM.connectionGlobals import url
from RFEM.enums import CaseObjectType
from RFEM.Results.resultTables import ResultTables

if Model.clientModel is None:
    Model()

@pytest.mark.skipif(url != 'http://127.0.0.1', reason="This test fails on remote PC due to incorrect file path. \
                    Althought it is easy to change, it would not be easy to update on every remote computer.\
                    It is not necessary to evaluate Client as functional. Localy this tests still gets executed.")

def test_result_tables():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.run_script(os.path.join(getPathToRunningRFEM(),'scripts\\internal\\Demos\\Demo-004 Bus Station-Concrete Design.js'))
    Model.clientModel.service.calculate_all(False)

    assert Model.clientModel.service.has_any_results()

    # CO1
    assert not ResultTables.LinesSupportForces(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 1)
    assert ResultTables.LinesSupportForces(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 2)
    assert ResultTables.MembersGlobalDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 3)
    assert ResultTables.MembersInternalForces(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 2)
    assert ResultTables.MembersInternalForcesBySection(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 2)
    assert ResultTables.MembersLocalDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 1)
    with pytest.raises(WebFault, match='Specified object does not exist.'):
         ResultTables.MembersLocalDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 4)
    with pytest.raises(WebFault, match='Specified object does not exist.'):
         ResultTables.MembersInternalForcesBySection(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 3)

    # LC1
    assert ResultTables.MembersStrains(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 1,1)
    assert ResultTables.NodesDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 1, 20)
    with pytest.raises(WebFault, match='Specified object does not exist.'):
         ResultTables.NodesDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 1, 5)
    assert ResultTables.NodesSupportForces(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 1, 16)
    assert ResultTables.Summary(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 1)
    assert ResultTables.SurfacesBasicInternalForces(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 1, 4)

    # LC2
    with pytest.raises(WebFault, match='Specified object does not exist.'):
         ResultTables.SurfacesBasicStresses(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 2, 5)
    assert ResultTables.SurfacesBasicStresses(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 2, 4)
    assert ResultTables.SurfacesBasicTotalStrains(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 2, 1)
    assert ResultTables.SurfacesDesignInternalForces(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 2, 2)
    assert ResultTables.SurfacesElasticStressComponents(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 2, 3)
    assert ResultTables.SurfacesEquivalentStressesBach(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 2, 1)

    # RC1
    assert ResultTables.SurfacesEquivalentStressesRankine(CaseObjectType.E_OBJECT_TYPE_RESULT_COMBINATION, 1, 1)
    assert ResultTables.SurfacesEquivalentStressesTresca(CaseObjectType.E_OBJECT_TYPE_RESULT_COMBINATION, 1, 2)
    assert ResultTables.SurfacesEquivalentStressesMises(CaseObjectType.E_OBJECT_TYPE_RESULT_COMBINATION, 1, 3)
    assert ResultTables.SurfacesEquivalentTotalStrainsBach(CaseObjectType.E_OBJECT_TYPE_RESULT_COMBINATION, 1, 4)
    assert ResultTables.SurfacesEquivalentTotalStrainsMises(CaseObjectType.E_OBJECT_TYPE_RESULT_COMBINATION, 1, 1)
    assert ResultTables.SurfacesEquivalentTotalStrainsRankine(CaseObjectType.E_OBJECT_TYPE_RESULT_COMBINATION, 1, 2)

    # DS1
    assert ResultTables.SurfacesEquivalentTotalStrainsTresca(CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, 1, 3)
    assert ResultTables.SurfacesGlobalDeformations(CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, 1, 4)
    assert ResultTables.SurfacesLocalDeformations(CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, 1, 1)
    assert ResultTables.SurfacesMaximumTotalStrains(CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, 1, 2)
    assert ResultTables.SurfacesPrincipalInternalForces(CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, 1, 3)
    assert ResultTables.SurfacesPrincipalStresses(CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, 1, 4)
    assert ResultTables.SurfacesPrincipalTotalStrains(CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, 1, 1)

    # Object selection all versus specific
    table3 = ResultTables.MembersLocalDeformations(CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, 1, 0)
    table4 = ResultTables.MembersLocalDeformations(CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, 1, 2)
    assert table3[18] == table4[0]

    table5 = ResultTables.MembersInternalForces(CaseObjectType.E_OBJECT_TYPE_RESULT_COMBINATION, 1, 0)
    table6 = ResultTables.MembersInternalForces(CaseObjectType.E_OBJECT_TYPE_RESULT_COMBINATION, 1, 3)
    assert table5[32] == table6[0]

    table7 = ResultTables.MembersStrains(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 0)
    table8 = ResultTables.MembersStrains(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 2)
    assert table7[16] == table8[0]

    table9 = ResultTables.MembersStrains(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 0, True)
    table10 = ResultTables.MembersStrains(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 1, 2, True)
    assert not table9[16] == table10[0]

    table2 = ResultTables.MembersGlobalDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 1, 3)
    # TODO: Reseting object_locations parameter for test_resultTableAddOn.py.
    # Should be done automatically in WS Core before every calculate_all().
    table1 = ResultTables.MembersGlobalDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, 1, 0)
    assert table1[32] == table2[0]
