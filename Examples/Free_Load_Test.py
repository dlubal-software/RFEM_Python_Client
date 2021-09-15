import sys
sys.path.append(".")

from RFEM.Loads.freeLoad import *
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
    
    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    
    Thickness(1, 'My Test Thickness', 1, 0.05)
    Surface(1, '1-4', 1)
    
    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', NodalSupportType.HINGED)
    NodalSupport(3, '3', NodalSupportType.HINGED)
    NodalSupport(4, '4', NodalSupportType.HINGED)
    
    StaticAnalysisSettings(1, 'Geometric linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    
    LoadCase(1 , 'freie Last', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)

    # Testing the free concentrated loads
    FreeLoad.ConcentratedLoad(FreeLoad, 1, 1, load_parameter= [5000, 4, 2])
    FreeLoad.ConcentratedLoad(FreeLoad, 2, 1, load_parameter= [50, 8, 8], load_type= FreeConcentratedLoadLoadType.LOAD_TYPE_MOMENT, load_direction= FreeConcentratedLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Y)

    # Testing the free line loads
    FreeLoad.LineLoad(FreeLoad, 3, 1, FreeLineLoadLoadDirection.LOAD_DIRECTION_LOCAL_Z, FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                     FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV, load_parameter= [5000, 1, 4, 3, 2])
    FreeLoad.LineLoad(FreeLoad, 4, 1, FreeLineLoadLoadDirection.LOAD_DIRECTION_LOCAL_Z, FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR,
                    FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV, load_parameter= [5000, 3000, 7, 2, 5, 9])

    #print(clientModel)
    #Calculate_all()
    print('Ready!')
    
    clientModel.service.finish_modification()