#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

# Import der Bibliotheken
#from RFEM.window import *

if __name__ == '__main__':

    clientModel.service.begin_modification()

    Material(1, 'S235')

    Section(1, 'IPE 200')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)

    Member(1, MemberType.TYPE_BEAM, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)

    StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'Eigengewicht', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)

    ## LOAD_DISTRIBUTION_UNIFORM ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 5000)
   
    ## LOAD_DISTRIBUTION_UNIFORM_TOTAL ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TOTAL, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 5000)

    ## LOAD_DISTRIBUTION_CONCENTRATED_N ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[True, True, 5000, 2, 0.4, 0.6])

    ## LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, load_parameter=[False, 5000, 1])
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, load_parameter=[True, 5000, 0.5])

    ## LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[True, True, True, 5000, 0.1, 0.2, 0.3])

    ## LOAD_DISTRIBUTION_CONCENTRATED_2 ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 6000, 1, 2])
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[True, True, 5000, 6000, 0.4, 0.6])

    ## LOAD_DISTRIBUTION_CONCENTRATED_VARYING ## 
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 5000], [2, 1, 10000]])

    ## LOAD_DISTRIBUTION_TRAPEZOIDAL and LOAD_DISTRIBUTION_TAPERED ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000,6000, 1, 2])
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[True, True, 5000,6000, 0.4, 0.6])

    ## LOAD_DISTRIBUTION_PARABOLIC ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000, 6000, 7000])

    ## LOAD_DISTRIBUTION_VARYING ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 5000], [3, 2, 10000]])

    ## LOAD_DISTRIBUTION_VARYING_IN_Z ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 1, 5000], [3, 2, 10000]])

    ## Eccentricity ##
    #MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 5000, force_eccentricity=True, params={'eccentricity_y_at_start': 0.0055})



    ## ERROR Mass ERROR ##
    MemberLoad.Mass(1, 1, 1, '1', [5000, 6000, 7000])
    ## ERROR Mass ERROR ##

    ## Temperature ##
   # MemberLoad.Temperature(1, 1, 1, '1', MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameters=[291, 297])


    Calculate_all()

    print('Ready!')

    clientModel.service.finish_modification()

