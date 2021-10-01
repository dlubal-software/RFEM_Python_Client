#from RFEM.Loads.solidLoad import SolidLoad
from RFEM.Loads.solidLoad import SolidLoad
from RFEM.enums import *
from RFEM.window import *
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
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.solidSet import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.surfaceLoad import *

if __name__ == '__main__':
    clientModel.service.begin_modification('new')

    Material(1, 'S235')
    
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10.0, 0.0, 0.0)
    Node(3, 10.0, 10.0, 0.0)
    Node(4, 0.0, 10.0, 0.0)

    Node(5, 0.0, 0.0, -5.0)
    Node(6, 10.0, 0.0, -5.0)
    Node(7, 10.0, 10.0, -5.0)
    Node(8, 0.0, 10.0, -5.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '5 6')
    Line(6, '6 7')
    Line(7, '7 8')
    Line(8, '8 5')

    Line(9, '1 5')
    Line(10, '2 6')
    Line(11, '3 7')
    Line(12, '4 8')
    
    Thickness(1, 'My Test Thickness', 1, 0.05)

    Surface(1, '1-4', 1)
    Surface(2, '5-8', 1)
    Surface(3, '1 9 5 10', 1)
    Surface(4, '2 10 6 11', 1)
    Surface(5, '3 11 7 12', 1)
    Surface(6, '4 12 8 9', 1)
    
    Solid(1, '1-6', 1)
    
    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', NodalSupportType.HINGED)
    NodalSupport(3, '3', NodalSupportType.HINGED)
    NodalSupport(4, '4', NodalSupportType.HINGED)
    
    StaticAnalysisSettings(1, 'Geometric linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    
    LoadCase(1 , 'Test load case', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)

    NodalLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_X, 12.8)
    
    SolidLoad(1, 1, '1', SolidLoadType.LOAD_TYPE_FORCE, SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 1289.0, 'My Comment')
    SolidLoad.Force(SolidLoad, 2, 1, '1', SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 8569.21, 'My 2nd Comment')
    SolidLoad.Force(SolidLoad, 3, 1, '1', SolidLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, 78548.21, 'My 2nd Comment')

    #Calculate_all()
    print('Ready!')
    
    clientModel.service.finish_modification()
