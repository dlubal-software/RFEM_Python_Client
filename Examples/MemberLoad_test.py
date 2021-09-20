import sys
sys.path.append(".")
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

    # Create Material 
    Material(1, 'S235')

    # Create Thickness
    Section(1, 'IPE 300')
    Section(2, 'CHS 100x4')

    # Create Nodes
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4.0, 0.0, 0.0)

    Node(3, 0, 5, 0)
    Node(4, 4, 5, 0)

    Member(1, MemberType.TYPE_BEAM, '1', '2', 0, 1, 1)
    Member(2, MemberType.TYPE_BEAM, '3', '4', 0, 2, 2)

    # Create Nodal Supports
    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    # Create Static Analysis Settings
    StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Create Load Case
    LoadCase(1, 'DEAD', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)

    ## Initial Member Load ##
    MemberLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 5000)

    ## Force Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Force(0, 2, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Force Type Member Load with LOAD_DISTRIBUTION_UNIFORM with Eccentricity ##
    MemberLoad.Force(0, 3, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000], force_eccentricity=True, params={'eccentricity_y_at_start' : 0.01, 'eccentricity_z_at_start': 0.02})

    ## Force Type Member Load with LOAD_DISTRIBUTION_UNIFORM_TOTAL ##
    MemberLoad.Force(0, 4, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TOTAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberLoad.Force(0, 5, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, 5000, 1.2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberLoad.Force(0, 6, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 2, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberLoad.Force(0, 7, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, False, 5000, 1, 2, 3])
    
    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x ##
    MemberLoad.Force(0, 8, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 6000, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberLoad.Force(0, 9, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])

    ## Force Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Force(0, 10, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Force(0, 11, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Force(0, 12, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[4000, 8000, 12000])
     
    ## Force Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Force(0, 13, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])
     
    ## Force Type Member Load with LOAD_DISTRIBUTION_VARYING_IN_Z ##
    MemberLoad.Force(0, 14, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])
     

    ## Moment Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Moment(0, 15, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberLoad.Moment(0, 16, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, 5000, 1.2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberLoad.Moment(0, 17, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 2, 1, 2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberLoad.Moment(0, 18, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, False, 5000, 1, 2, 3])
    
    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x ##
    MemberLoad.Moment(0, 19, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 6000, 1, 2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberLoad.Moment(0, 20, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Moment(0, 21, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Moment(0, 22, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Moment Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Moment(0, 23, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[4000, 8000, 12000])
     
    ## Moment Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Moment(0, 24, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 4000], [2, 1, 5000]])
  

    ## Mass Type Member Load ##
    MemberLoad.Mass(0, 25, 1, mass_components=[1000])


    ## Temperature Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Temperature(0, 26, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[18, 2])

    ## Temperature Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Temperature(0, 27, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## Temperature Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Temperature(0, 28, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## Temperature Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Temperature(0, 29, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3, 4, 5, 6])
     
    ## Temperature Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Temperature(0, 30, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285, 289], [2, 1, 293, 297]])

    
    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.TemperatureChange(0, 31, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[18, 2])

    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.TemperatureChange(0, 32, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.TemperatureChange(0, 33, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, 18, 20, False, False, 1, 2])

    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.TemperatureChange(0, 34, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3, 4, 5, 6])
     
    ## TemperatureChange Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.TemperatureChange(0, 35, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285, 289], [2, 1, 293, 297]])


    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.AxialStrain(0, 36, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[0.005])

    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.AxialStrain(0, 37, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[12, 16, False, False, 1, 2])

    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.AxialStrain(0, 38, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[12, 16, False, False, 1, 2])

    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.AxialStrain(0, 39, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[1, 2, 3])
     
    ## AxialStrain Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.AxialStrain(0, 40, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, load_parameter=[[1, 1, 285, 289], [2, 1, 293, 297]])


    ## AxialDisplacement Type Member Load ##
    MemberLoad.AxialDisplacement(0, 41, 1, '1', MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, 0.05)


    ## Precamber Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Precamber(0, 42, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[0.005])

    ## Precamber Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Precamber(0, 43, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Precamber Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Precamber(0, 44, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Precamber Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Precamber(0, 45, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3])
     
    ## Precamber Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Precamber(0, 46, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285], [2, 1, 293]])


    ## InitialPrestress Type Member Load ##
    MemberLoad.InitialPrestress(0, 47, 1, '1', MemberLoadDirection.LOAD_DIRECTION_LOCAL_X, 50)


    ## Displacement Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Displacement(0, 48, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberLoad.Displacement(0, 49, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, 1])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberLoad.Displacement(0, 50, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, 1, 2])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberLoad.Displacement(0, 51, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, False, 1, 2, 3])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2 ##
    MemberLoad.Displacement(0, 52, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, 0.6, False, False, 1, 2])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberLoad.Displacement(0, 53, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[0.001, 1, 1], [0.002, 2, 1]])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Displacement(0, 54, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Displacement(0, 55, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Displacement Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Displacement(0, 56, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3])
     
    ## Displacement Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Displacement(0, 57, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285], [2, 1, 293]])


    ## Rotation Type Member Load with LOAD_DISTRIBUTION_UNIFORM ##
    MemberLoad.Rotation(0, 58, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    MemberLoad.Rotation(0, 59, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, 1])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    MemberLoad.Rotation(0, 60, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, 1, 2])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    MemberLoad.Rotation(0, 61, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, False, False, False, 1, 2, 3])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2 ##
    MemberLoad.Rotation(0, 62, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [0.5, 0.6, False, False, 1, 2])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    MemberLoad.Rotation(0, 63, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[1, 1, 285], [2, 1, 293]])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    MemberLoad.Rotation(0, 64, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    MemberLoad.Rotation(0, 65, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[12, 16, False, False, 1, 2])

    ## Rotation Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    MemberLoad.Rotation(0, 66, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[1, 2, 3])
     
    ## Rotation Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    MemberLoad.Rotation(0, 67, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 285], [2, 1, 293]])


    ## PipeContentFull Type Member Load ## 
    MemberLoad.PipeContentFull(0, 68, 1, '2', MemberLoadDirectionOrientation.LOAD_DIRECTION_FORWARD, 50)
    
    
    Calculate_all()

    print('Ready!')

    clientModel.service.finish_modification()

