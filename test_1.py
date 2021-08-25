from RFEM.Loads.surfaceLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.nodalLoad import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.BasicObjects.solidSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.material import *
from RFEM.initModel import *
from RFEM.dataTypes import *
from RFEM.enums import *


if __name__ == '__main__':

    clientModel.service.begin_modification()

    Material(1, 'S235')

    Thickness(1, '1', 1, 0.1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    Surface(1, '1 2 3 4', 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'Eigengewicht', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)

    #SurfaceLoad(1, 1, '1', 50)

    #SurfaceLoad.Force(1, 1, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR, load_parameter=[1000, 2000, 3000, '2', '3', '4'])

    #SurfaceLoad.Force(1, 1, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, load_parameter=[1000, 2000, '2', '3'])
    
    #SurfaceLoad.Force(1, 1, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_Y, load_parameter=[1000, 2000, '2', '3'])

    #SurfaceLoad.Force(1, 1, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_RADIAL, load_parameter=[1000, 2000, 2, 4, SurfaceLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS, [0, 0, 0], [0, 0, 1]])

    #SurfaceLoad.Force(1, 1, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z, load_parameter=[[-4, -4, 32000], [-3, -1, 16000], [-2, -1, 8000], [-1, -1, 4000], [0, 1, 1000]])

    #SurfaceLoad.Temperature(1, 1, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[18, 2])

    SurfaceLoad.Temperature(1, 1, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR, load_parameter=[16, 2, 18, 4, 20, 6, 1, 2, 4])




    #Calculate_all()

    print('Ready!')

    clientModel.service.finish_modification()

