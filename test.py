import sys

from RFEM.BasicObjects.lineSet import LineSet
from RFEM.Imperfections.memberImpferfection import MemberImperfection
from RFEM.Loads.solidSetLoad import SolidSetLoad
sys.path.append(".")
sys.path.append("./RFEM")
import pytest
from UnitTests import test_loads

from RFEM.Loads import *
from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.solidSet import *
from RFEM.BasicObjects.opening import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForLines.lineSupport import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.designSituation import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.LoadCasesAndCombinations.loadCombination import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.freeLoad import *
from RFEM.Loads.lineLoad import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.surfaceLoad import *
from RFEM.Loads.lineLoad import *
from RFEM.Imperfections.imperfectionCase import *

if __name__ == '__main__':
    Model.clientModel.service.begin_modification('new')

    Material(1, 'S235')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 0.0, 0.0, -10.0)

    Section(1, 'IPE 300')
    Member(1, 1, 2, 0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, 'LINEAR', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    StaticAnalysisSettings(2, 'NONLINEAR', StaticAnalysisType.SECOND_ORDER_P_DELTA)

    DesignSituation(1, True,'My DS', True)

    LoadCase(1, 'Test 1')
    LoadCase(2, 'Test 2', [False])

    LoadCombination(1, AnalysisType.ANALYSIS_TYPE_STATIC, 1, [False], 2, False, False, False, True, [[1.1, 1, 0, False], [1.5, 2, 0, False]], 'My Combination')
    LoadCombination(2, AnalysisType.ANALYSIS_TYPE_STATIC, 1, [False], 2, False, False, False, True, [[1.1, 1, 0, False], [1.5, 2, 0, False]], 'My Combination')
    LoadCombination(3, AnalysisType.ANALYSIS_TYPE_STATIC, 1, [False], 2, False, False, False, True, [[1.1, 1, 0, False], [1.5, 2, 0, False]], 'My Combination')

    NodalLoad(1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 10000)
    NodalLoad(1, 2, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 5000)

    ImperfectionCase.Local(ImperfectionCase, 1, '1', '1-2', 'My Comment' )
    ImperfectionCase.Local(ImperfectionCase, 2, '2')
    ImperfectionCase.Local(ImperfectionCase, 3, '3')

    MemberImperfectionDict = {
        "imperfection_type"         : "IMPERFECTION_TYPE_INITIAL_BOW",
        "imperfection_direction"    : "IMPERFECTION_DIRECTION_LOCAL_Y",
        "definition_type"           : "DEFINITION_TYPE_RELATIVE",
        "basic_value_relative"      : 300.0
    }

    MemberImperfection(1, 1, '1', 'My Comment', MemberImperfectionDict)
    MemberImperfection.InitialSwayRelative(MemberImperfection, 2, 2, '1', 250.0, ImperfectionDirection.IMPERFECTION_DIRECTION_LOCAL_Y_NEGATIVE)
    MemberImperfection.InitialBowRelative(MemberImperfection,3, 3, '1', 200.0, ImperfectionDirection.IMPERFECTION_DIRECTION_LOCAL_Y_NEGATIVE)


    # Dieses Testprogramm wird noch etwas ausgebaut und schön gemacht. Dann wird es als
    # Beispiel veröffentlicht.






    #Calculate_all()

    Model.clientModel.service.finish_modification()


    print('Fertig!')

