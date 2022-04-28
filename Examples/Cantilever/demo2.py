#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import MemberHingeDiagramType, MemberHingeNonlineartiy, MemberHingePartialActivityType, NodalSupportType, LoadDirectionType
from RFEM.initModel import Model, Calculate_all
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.TypesForMembers.memberResultIntermediatePoints import MemberResultIntermediatePoint


Model(True, "Demo3")
Model.clientModel.service.begin_modification()

Node(1, 0,0,0)
Node(2, 5,0,0)
Material(1, "S235")
Section(1, "IPE 200", 1)
Member(1, 1, 2, 0, 1, 1)

# MemberHinge(1, "Local", "", 4000, translational_release_n_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 8000], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 9000]])
# MemberHinge(2, "Local", "", 2000, translational_release_n_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.004], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.005]])
# #MemberHinge(3, "Local", "", 0, translational_release_n_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_TEARING, 3000, 0.004], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_YIELDING, 5000, 0.006]])
# MemberHinge(4, "Local", "", 0, translational_release_n_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_DIAGRAM, [MemberHingeDiagramType.DIAGRAM_ENDING_TYPE_CONTINUOUS, MemberHingeDiagramType.DIAGRAM_ENDING_TYPE_CONTINUOUS, [[1,2, 3], [3,4, 5]]]])
# MemberHinge(5, "Local", "", 0, translational_release_n_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_1, [0.5]])
# MemberHinge(6, "Local", "", 0, translational_release_n_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2, [0.6]])
# MemberHinge(7, "Local", "", 0, translational_release_n_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_2, [0.7]])
# MemberHinge(8, "Local", "", 0, translational_release_n_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2, [0.8, 0.9]])

# MemberHinge(1, "Local", "", translational_release_vy=0, translational_release_vy_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 8000], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 9000]])
# MemberHinge(2, "Local", "", translational_release_vy=0, translational_release_vy_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.004], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.005]])
# #MemberHinge(3, "Local", "", translational_release_vy=0, translational_release_vy_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_TEARING, 3000, 0.004], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_YIELDING, 5000, 0.006]])
# MemberHinge(4, "Local", "", translational_release_vy=0, translational_release_vy_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_DIAGRAM, [MemberHingeDiagramType.DIAGRAM_ENDING_TYPE_CONTINUOUS, MemberHingeDiagramType.DIAGRAM_ENDING_TYPE_CONTINUOUS, [[1,2, 3], [3,4, 5]]]])
# MemberHinge(5, "Local", "", translational_release_vy=0, translational_release_vy_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_1, [0.5]])
# MemberHinge(6, "Local", "", translational_release_vy=0, translational_release_vy_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2, [0.6]])
# MemberHinge(7, "Local", "", translational_release_vy=0, translational_release_vy_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_2, [0.7]])
# MemberHinge(8, "Local", "", translational_release_vy=0, translational_release_vy_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2, [0.8, 0.9]])

# MemberHinge(1, "Local", "", translational_release_vz=0, translational_release_vz_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 8000], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 9000]])
# MemberHinge(2, "Local", "", translational_release_vz=0, translational_release_vz_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.004], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.005]])
# #MemberHinge(3, "Local", "", translational_release_vz=0, translational_release_vz_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_TEARING, 3000, 0.004], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_YIELDING, 5000, 0.006]])
# MemberHinge(4, "Local", "", translational_release_vz=0, translational_release_vz_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_DIAGRAM, [MemberHingeDiagramType.DIAGRAM_ENDING_TYPE_CONTINUOUS, MemberHingeDiagramType.DIAGRAM_ENDING_TYPE_CONTINUOUS, [[1,2, 3], [3,4, 5]]]])
# MemberHinge(5, "Local", "", translational_release_vz=0, translational_release_vz_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_1, [0.5]])
# MemberHinge(6, "Local", "", translational_release_vz=0, translational_release_vz_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2, [0.6]])
# MemberHinge(7, "Local", "", translational_release_vz=0, translational_release_vz_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_2, [0.7]])
# MemberHinge(8, "Local", "", translational_release_vz=0, translational_release_vz_nonlinearity=[MemberHingeNonlineartiy.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2, [0.8, 0.9]])


# MemberResultIntermediatePoint(1, "", 5)
## MemberResultIntermediatePoint(2, "", 2, False, [[0.3], [0.6]])



Model.clientModel.service.finish_modification()

