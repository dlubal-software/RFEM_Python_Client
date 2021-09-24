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
    Node(5, 0.0, 0.0, 10.0)
    Node(6, 0.0, 10.0, 10.0)
    
    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    
    Thickness(1, 'Dicke', 1, 0.05)
    Surface(1, '1-4', 1)
    
    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', NodalSupportType.HINGED)
    NodalSupport(3, '3', NodalSupportType.HINGED)
    NodalSupport(4, '4', NodalSupportType.HINGED)
    
    StaticAnalysisSettings(1, 'Geometrisch-linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    
    LoadCase(1 , 'Einzell- u. Linienlast', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, False, 0.0, 0.0, 0.0)
    LoadCase(2 , 'Rechtecklast 1', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, False, 0.0, 0.0, 0.0)
    LoadCase(3 , 'Rechtecklast 2', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, False, 0.0, 0.0, 0.0)
    LoadCase(4 , 'Kreislast', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, False, 0.0, 0.0, 0.0)
    LoadCase(5 , 'Polygonlast', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, False, 0.0, 0.0, 0.0)

    # Prüfung der freien Einzellasten
    FreeLoad.ConcentratedLoad(FreeLoad, 1, 1, load_parameter= [5000, 4, 2])
    FreeLoad.ConcentratedLoad(FreeLoad, 2, 1, load_parameter= [50, 8, 8], load_type= FreeConcentratedLoadLoadType.LOAD_TYPE_MOMENT, load_direction= FreeConcentratedLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Y)

    # Prüfung der freien Linienlasten
    FreeLoad.LineLoad(FreeLoad, 3, 1, '1',
                        FreeLineLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                        FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                        FreeLineLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE, 
                        [5000, 2, 2, 4, 4])
    
    # Prüfung der freien Rechtecklasten

    ##  LOAD_LOCATION_RECTANGLE_CORNER_POINTS
    FreeLoad.RectangularLoad(FreeLoad, 1, 2, '1',
                             FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                             FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                             FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                             [5000], 
                             FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CORNER_POINTS,
                             [1, 8, 3, 10, 0])

    FreeLoad.RectangularLoad(FreeLoad, 2, 2, '1',
                            FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_FIRST,
                            FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                            FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                            [5000, 2000], 
                            FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CORNER_POINTS,
                            [4, 8, 6, 10, 0])

    FreeLoad.RectangularLoad(FreeLoad, 3, 2, '1',
                            FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_SECOND,
                            FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                            FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                            [5000, 2000], 
                            FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CORNER_POINTS,
                            [7, 8, 9, 10, 0])

    FreeLoad.RectangularLoad(FreeLoad, 4, 2, '1',
                             FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z,
                             FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                             FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                             [5000], 
                             FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CORNER_POINTS,
                             [1, 5, 3, 7, [[-3, 0.3], [-1, 0.4], [0, 1]]])

    FreeLoad.RectangularLoad(FreeLoad, 5, 2, '1',
                            FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_ALONG_PERIMETER,
                            FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                            FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                            [5000], 
                            FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CORNER_POINTS,
                            [4, 5, 6, 7, [5, 7, 0], [5, 9, 2], 0, [[0, 0.5], [90, 1.75], [180, 1.25], [270, 1], [360, 0.5]]])

    FreeLoad.RectangularLoad(FreeLoad, 6, 2, '1',
                            FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z_AND_ALONG_PERIMETER,
                            FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                            FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                            [5000], 
                            FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CORNER_POINTS,
                            [7, 5, 9, 7, [[-3, 0.3], [-1, 0.4], [0, 1]], [5, 7, 0], [5, 9, 2], 0, [[0, 0.5], [90, 1.75], [180, 1.25], [270, 1], [360, 0.5]]])

    ##  LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES
    FreeLoad.RectangularLoad(FreeLoad, 1, 3, '1',
                             FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                             FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                             FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                             [5000], 
                             FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES,
                             [2, 9, 2, 2, 0])

    FreeLoad.RectangularLoad(FreeLoad, 2, 3, '1',
                            FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_FIRST,
                            FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                            FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                            [5000, 2000], 
                            FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES,
                            [5, 9, 2, 2, 0])

    FreeLoad.RectangularLoad(FreeLoad, 3, 3, '1',
                            FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_SECOND,
                            FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                            FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                            [5000, 2000], 
                            FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES,
                            [8, 9, 2, 2, 0])

    FreeLoad.RectangularLoad(FreeLoad, 4, 3, '1',
                             FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z,
                             FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                             FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                             [5000], 
                             FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES,
                             [2, 6, 2, 2, [[-3, 0.3], [-1, 0.4], [0, 1]]])

    FreeLoad.RectangularLoad(FreeLoad, 5, 3, '1',
                            FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_ALONG_PERIMETER,
                            FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                            FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                            [5000], 
                            FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES,
                            [5, 6, 2, 2, [5, 7, 0], [5, 9, 2], 0, [[0, 0.5], [90, 1.75], [180, 1.25], [270, 1], [360, 0.5]]])

    FreeLoad.RectangularLoad(FreeLoad, 6, 3, '1',
                            FreeRectangularLoadLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z_AND_ALONG_PERIMETER,
                            FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                            FreeRectangularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                            [5000], 
                            FreeRectangularLoadLoadLocationRectangle.LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES,
                            [8, 6, 2, 2, [[-3, 0.3], [-1, 0.4], [0, 1]], [5, 7, 0], [5, 9, 2], 0, [[0, 0.5], [90, 1.75], [180, 1.25], [270, 1], [360, 0.5]]])

    # Prüfung der freien Kreislasten
    FreeLoad.CircularLoad(FreeLoad, 1, 4, '1',
                             FreeCircularLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                             FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                             FreeCircularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                             [10000, 7.5, 5, 2])

    FreeLoad.CircularLoad(FreeLoad, 2, 4, '1',
                             FreeCircularLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR,
                             FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                             FreeCircularLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                             [10000, 2500, 2.5, 5, 2])

    # Prüfung der freien Polygonlasten
    FreeLoad.PolygonLoad(FreeLoad, 1, 5, '1',
                         FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                         FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                         FreePolygonLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                         [[1, 0], [0, 2], [2, 2]],
                         [5000])

    FreeLoad.PolygonLoad(FreeLoad, 2, 5, '1',
                         FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR,
                         FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                         FreePolygonLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                         [[6, 0], [4, 2], [8, 2]],
                         [5000, 2500, 1000, 1, 2, 3])

    FreeLoad.PolygonLoad(FreeLoad, 3, 5, '1',
                         FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_FIRST,
                         FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                         FreePolygonLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                         [[6, 4], [4, 6], [8, 6]],
                         [5000, 2500, 1, 3])

    FreeLoad.PolygonLoad(FreeLoad, 4, 5, '1',
                         FreePolygonLoadLoadDistribution.LOAD_DISTRIBUTION_LINEAR_SECOND,
                         FreeLoadLoadProjection.LOAD_PROJECTION_XY_OR_UV,
                         FreePolygonLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z_TRUE,
                         [[1, 4], [0, 6], [2, 6]],
                         [1500, 7500, 2, 1])

    #print(clientModel)
    #Calculate_all()
    print('Ready!')
    
    clientModel.service.finish_modification()