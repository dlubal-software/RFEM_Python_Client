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

    Node(3, 0.0, 4.0, 0.0)
    Node(4, 4.0, 4.0, 0.0)

    Node(5, 0.0, 8.0, 0.0)
    Node(6, 4.0, 8.0, 0.0)

    Node(7, 0.0, 12.0, 0.0)
    Node(8, 4.0, 12.0, 0.0)

    Node(9, 0.0, 16.0, 0.0)
    Node(10, 4.0, 16.0, 0.0)

    Node(11, 0.0, 20.0, 0.0)
    Node(12, 4.0, 20.0, 0.0)

    Node(13, 0.0, 24.0, 0.0)
    Node(14, 4.0, 24.0, 0.0)

    Node(15, 0.0, 28.0, 0.0)
    Node(16, 4.0, 28.0, 0.0)

    Node(17, 0.0, 32.0, 0.0)
    Node(18, 4.0, 32.0, 0.0)


    Member(1, MemberType.TYPE_BEAM, 1, 2, 0.0, 1, 1)
    Member(2, MemberType.TYPE_BEAM, 3, 4, 0.0, 1, 1)
    Member(3, MemberType.TYPE_BEAM, 5, 6, 0.0, 1, 1)
    Member(4, MemberType.TYPE_BEAM, 7, 8, 0.0, 1, 1)
    Member(5, MemberType.TYPE_BEAM, 9, 10, 0.0, 1, 1)
    Member(6, MemberType.TYPE_BEAM, 11, 12, 0.0, 1, 1)
    Member(7, MemberType.TYPE_BEAM, 13, 14, 0.0, 1, 1)
    Member(8, MemberType.TYPE_BEAM, 15, 16, 0.0, 1, 1)
    Member(9, MemberType.TYPE_BEAM, 17, 18, 0.0, 1, 1)


    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '3', NodalSupportType.FIXED)
    NodalSupport(3, '5', NodalSupportType.FIXED)
    NodalSupport(4, '7', NodalSupportType.FIXED)
    NodalSupport(5, '9', NodalSupportType.FIXED)
    NodalSupport(6, '11', NodalSupportType.FIXED)
    NodalSupport(7, '13', NodalSupportType.FIXED)
    NodalSupport(8, '15', NodalSupportType.FIXED)
    NodalSupport(9, '17', NodalSupportType.FIXED)


    StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'Eigengewicht', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)


    ## FORCE TYPE ##
    NodalLoad.Force(1, 1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 500, specific_direction=True, params={'specific_direction': [NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES, NodalLoadAxesSequence.SEQUENCE_XYZ, 0, 0.5, 0, 0, 0.5, 0]})
    NodalLoad.Force(1, 2, 1, '4', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 500, force_eccentricity=True, params={'force_eccentricity' : [0,0,1]})
    NodalLoad.Force(1, 3, 1, '6', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 500, shifted_display=True, params = {'shifted_display': [0.1, 0.2, 0.3, 0.4]})


    ## MASS TYPE ##
    NodalLoad.Mass(1, 4, 1, '8', 500, individual_mass_components=True, params={'individual_mass_components' : [10,20,30,40,50,60]})

    ## MOMENT TYPE ##
    NodalLoad.Moment(1, 5, 1, '10', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 500, specific_direction=True, params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES, NodalLoadAxesSequence.SEQUENCE_XYZ, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]})
    NodalLoad.Moment(1, 6, 1, '12', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 500, shifted_display=True, params={'shifted_display': [1,2,3,4]})

    ## COMPONENT TYPE ##
    NodalLoad.Components(1, 7, 1, '14', 10, 20, 30, 40, 50, 60, specific_direction=True, params={'specific_direction' : [NodalLoadSpecificDirectionType.DIRECTION_TYPE_ROTATED_VIA_3_ANGLES, NodalLoadAxesSequence.SEQUENCE_XYZ, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]})
    NodalLoad.Components(1, 8, 1, '16', 10, 20, 30, 40, 50, 60, shifted_display=True, params={'shifted_display': [1,2,3,4]})
    NodalLoad.Components(1, 9, 1, '18', 10, 20, 30, 40, 50, 60, force_eccentricity=True, params={'force_eccentricity' : [0,0,1]}) 

    Calculate_all()
    print('Ready!')

    clientModel.service.finish_modification()

