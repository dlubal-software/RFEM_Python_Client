import sys

from RFEM.BasicObjects.lineSet import LineSet
sys.path.append(".")
sys.path.append("./RFEM")
import pytest
from UnitTests import test_loads

from RFEM.Loads import nodalLoad
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
from RFEM.BasicObjects.opening import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForLines.lineSupport import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.freeLoad import *
from RFEM.Loads.lineLoad import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.surfaceLoad import *
from RFEM.Loads.lineLoad import *
#from RFEM.Loads.imposedLineDeformation import *
#from RFEM.Loads.openingLoad import *
from RFEM.Loads.linesetLoad import *

if __name__ == '__main__':
    #test_loads.test_free_polygon_load()
    #test_loads.test_imposed_line_deformation()
    #print(sys.path)
    #Model(True, "MyTest", True, True)
    Model.clientModel.service.begin_modification('new')

    Material(1, 'S235')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5.0, 0.0, 0.0)
    Node(3, 5.0, 6.0, 0.0)
    Node(4, 0.0, 6.0, 0.0)

    Node(5, 2.0, 2.0, 0.0)
    Node(6, 4.0, 2.0, 0.0)
    Node(7, 4.0, 4.0, 0.0)
    Node(8, 2.0, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '5 6')
    Line(6, '6 7')
    Line(7, '7 8')

    Thickness(1, 'My Thickness', 1, 0.05)
    Surface(1, '1-4', 1, 'My Test')

    inf = float('inf')
    supportDict = {
        "lines": "1 2 3 4",
        "spring_x": inf,
        "spring_y": inf,
        "spring_z": inf,
        "rotational_restraint_x": 0,
        "rotational_restraint_y": 0,
        "rotational_restraint_z": 0
    }
    LineSupport(1, 'Mein Lager', supportDict)

    LineSet.ContinuousLines(LineSet, 1, '5-7')

    StaticAnalysisSettings(1, 'LINEAR', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    LoadCase(1, 'DEAD')

    LinesetLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 1200.5, 'My Comment')

    Model.clientModel.service.finish_modification()

    print('Fertig!')

