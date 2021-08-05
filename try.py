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

    StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'Eigengewicht', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)

    MemberLoad.Force(1, 1, 1, '1', MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 50000, force_eccentricity=True, load_parameter=[True, MemberLoadEccentricityHorizontalAlignment.ALIGN_NONE, MemberLoadEccentricityVerticalAlignment.ALIGN_NONE, MemberLoadEccentricitySectionMiddle.LOAD_ECCENTRICITY_SECTION_MIDDLE_CENTER_OF_GRAVITY, 50, 60, 70, 80])


    Calculate_all()

    print('Ready!')

    clientModel.service.finish_modification()

