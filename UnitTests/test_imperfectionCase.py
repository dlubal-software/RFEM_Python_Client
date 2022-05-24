from importlib import import_module
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import ImperfectionType, ImperfectionCaseAssignmentType, ActionCategoryType
from RFEM.initModel import Model
from RFEM.Imperfections.imperfectionCase import ImperfectionCase
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings

if Model.clientModel is None:
    Model()

def test_imperfection_case():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    StaticAnalysisSettings()

    LoadCase(1, 'LC1')
    LoadCase(2, 'LC2')
    LoadCase(3, 'LC3')
    LoadCase(4, 'LC4')
    LoadCase(5, 'LC5')

    ImperfectionCase(1, ImperfectionType.IMPERFECTION_TYPE_LOCAL_IMPERFECTIONS, '2')
    ImperfectionCase.Local(2)
    ImperfectionCase.InitialSwayViaTable(3,'1')
    ImperfectionCase.NotionalLoads(4,'3')
    ImperfectionCase.StaticDeformation(5,'4',magnitude_assignment_type = ImperfectionCaseAssignmentType.MAGNITUDE_ASSIGNMENT_LOCATION_WITH_LARGEST_DISPLACEMENT)
    ImperfectionCase.Group(6,'1')

    Model.clientModel.service.finish_modification()

    imp = Model.clientModel.service.get_imperfection_case(1)
    assert imp.type == ImperfectionType.IMPERFECTION_TYPE_LOCAL_IMPERFECTIONS.name
    assert imp.assigned_to_load_cases == '2'

    imp = Model.clientModel.service.get_imperfection_case(2)
    assert imp.type == ImperfectionType.IMPERFECTION_TYPE_LOCAL_IMPERFECTIONS.name

    imp = Model.clientModel.service.get_imperfection_case(3)
    assert imp.type == ImperfectionType.IMPERFECTION_TYPE_INITIAL_SWAY_VIA_TABLE.name
    assert imp.level_imperfections.imperfection_case_level_imperfections[0].row.level == 3

    imp = Model.clientModel.service.get_imperfection_case(4)
    assert imp.type == ImperfectionType.IMPERFECTION_TYPE_NOTIONAL_LOADS_FROM_LOAD_CASE.name
    assert imp.assigned_to_load_cases == '3'

    imp = Model.clientModel.service.get_imperfection_case(5)
    assert imp.type == ImperfectionType.IMPERFECTION_TYPE_STATIC_DEFORMATION.name
    assert imp.assigned_to_load_cases == '4'

    imp = Model.clientModel.service.get_imperfection_case(6)
    assert imp.type == ImperfectionType.IMPERFECTION_TYPE_IMPERFECTION_CASES_GROUP.name
    assert round(imp.imperfection_cases_items.imperfection_case_imperfection_cases_items[0].row.factor, 2) == 1.1
