
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import ImperfectionType, SetType, ImperfectionCaseAssignmentType
from RFEM.initModel import Model
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.Imperfections.imperfectionCase import ImperfectionCase
from RFEM.Imperfections.memberImperfection import MemberImperfection
from RFEM.Imperfections.membersetImperfection import MemberSetImperfection
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.enums import MemberImperfectionType, MemberImperfectionDefinitionType


if Model.clientModel is None:
    Model()

def test_imperfection_case():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Section
    Section(1, 'IPE 300')
    Section(2, 'CHS 100x4')

    # Create Nodes
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 2, 0.0, 0.0)
    Node(3, 4, 0, 0)

    Node(4, 0, 5, 0)
    Node(5, 2, 5, 0)
    Node(6, 4, 5, 0)

    # Create Member
    Member(1, 1, 2, 0, 1)
    Member(2, 2, 3, 0, 1)
    Member(3, 4, 6, 0, 2)
    Member(4, 6, 5, 0, 2)

    # Create Member Set
    MemberSet(1, '1 2', SetType.SET_TYPE_CONTINUOUS)
    MemberSet(2, '3 4', SetType.SET_TYPE_CONTINUOUS)

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

    MemberImperfection(1, 1)
    MemberImperfection(2, 1,'2',MemberImperfectionType.IMPERFECTION_TYPE_INITIAL_SWAY, MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1992_1, parameters=[250, 0.002, 2, 1,1,0.006, 220])
    MemberImperfection(3, 1,'3',MemberImperfectionType.IMPERFECTION_TYPE_INITIAL_SWAY, MemberImperfectionDefinitionType.DEFINITION_TYPE_EN_1995_1_1, parameters=[220, 0.002,1, 0.006, 230])

    MemberSetImperfection(1, 1)

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
