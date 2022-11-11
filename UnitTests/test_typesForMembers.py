#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

## Import the relevant Libraries
from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.TypesForMembers.memberResultIntermediatePoints import MemberResultIntermediatePoint
from RFEM.TypesForMembers.memberSupport import MemberSupport
from RFEM.dataTypes import inf
from RFEM.TypesForMembers.memberDefinableStiffness import MemberDefinableStiffness
from RFEM.TypesForMembers.memberEccentricity import MemberEccentricity
from RFEM.TypesForMembers.memberNonlinearity import MemberNonlinearity
from RFEM.TypesForMembers.memberStiffnessModification import MemberStiffnessModification
from RFEM.TypesForMembers.memberTransverseStiffeners import MemberTransverseStiffeners
from RFEM.BasicObjects.material import Material

if Model.clientModel is None:
    Model()

def test_memberDefinableStiffness():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    MemberDefinableStiffness(1, [False], "", 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12)

    Model.clientModel.service.finish_modification()

    memberStiffness_1 = Model.clientModel.service.get_member_definable_stiffness(1)

    assert memberStiffness_1.torsional_stiffness == 1

def test_memberEccentricity():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    MemberEccentricity()

    Model.clientModel.service.finish_modification()

    memberEccentricitiy_1 = Model.clientModel.service.get_member_eccentricity(1)

    assert memberEccentricitiy_1.specification_type == "TYPE_RELATIVE"

def test_memberHinge():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    MemberHinge(1, "Local", "", 4000, translational_release_n_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 8000], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_COMPLETE, 9000]])
    MemberHinge(2, "Local", "", 2000, translational_release_n_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1, [0.5]])
    MemberHinge(3, "Local", "", translational_release_vy=0, translational_release_vy_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_DIAGRAM, [MemberHingeDiagramType.DIAGRAM_ENDING_TYPE_CONTINUOUS, MemberHingeDiagramType.DIAGRAM_ENDING_TYPE_CONTINUOUS, [[1,2, 3], [3,4, 5]]]])
    MemberHinge(4, "Local", "", translational_release_vz=0, translational_release_vz_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY, [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.004], [MemberHingePartialActivityType.PARTIAL_ACTIVITY_TYPE_FIXED, 0.005]])

    Model.clientModel.service.finish_modification()

    memberHinge_1 = Model.clientModel.service.get_member_hinge(1)
    memberHinge_2 = Model.clientModel.service.get_member_hinge(2)
    memberHinge_3 = Model.clientModel.service.get_member_hinge(3)
    memberHinge_4 = Model.clientModel.service.get_member_hinge(4)

    assert memberHinge_1.no == 1
    assert memberHinge_2.axial_release_n == 2000
    assert memberHinge_3.axial_release_vy_nonlinearity == "NONLINEARITY_TYPE_DIAGRAM"
    assert memberHinge_4.axial_release_vy == inf


def test_memberNonlinearity():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    MemberNonlinearity()

    Model.clientModel.service.finish_modification()

    memberNonlinearity_1 = Model.clientModel.service.get_member_nonlinearity(1)

    assert memberNonlinearity_1.type == "TYPE_FAILURE_IF_TENSION"

def test_memberResultIntermediatePoint():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    MemberResultIntermediatePoint(1, "", 5)

    Model.clientModel.service.finish_modification()

    memberResultIntermediatePoint_1 = Model.clientModel.service.get_member_result_intermediate_point(1)

    assert memberResultIntermediatePoint_1.point_count == 5

def test_memberStiffnessModification():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    MemberStiffnessModification()

    Model.clientModel.service.finish_modification()

    memberStiffnessModification_1 = Model.clientModel.service.get_member_stiffness_modification(1)

    assert memberStiffnessModification_1.factor_of_bending_z_stiffness == 1

def test_memberSupport():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    MemberSupport()
    MemberSupport(2, '', 1,2, [inf, MemberSupportNonlinearity.NONLINEARITY_FAILURE_IF_NEGATIVE_CONTACT_STRESS_Z], 3, 4, 5, 6)

    Model.clientModel.service.finish_modification()

    memberSupport_1 = Model.clientModel.service.get_member_support(1)
    memberSupport_2 = Model.clientModel.service.get_member_support(2)

    assert memberSupport_1.no == 1
    assert memberSupport_2.spring_translation_y == 2


def test_memberTransverseStiffeners():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    MemberTransverseStiffeners(1)

    Model.clientModel.service.finish_modification()

    memberStiffener_1 = Model.clientModel.service.get_member_transverse_stiffener(1)

    assert memberStiffener_1.no == 1
    assert memberStiffener_1.name == "1 Stiffener | Flat"
