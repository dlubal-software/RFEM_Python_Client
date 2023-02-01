#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

# This script follows the basic design of timber structures
# It is based on the following webinar: https://www.dlubal.com/en/support-and-learning/learning/webinars/002410

import xlwings as xw
import numpy as np

#Import all modules required to access RFEM
from RFEM.enums import AddOn, StaticAnalysisType, ActionCategoryType, NodeReferenceType, MemberLoadDirection, NodalSupportType, ObjectTypes, \
    TimberServiceClassServiceClass, DesignSituationType, CaseObjectType
from RFEM.initModel import Model, SetAddonStatus, Calculate_all
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Tools.PlausibilityCheck import PlausibilityCheck

# importing modules requiered for timber design
from RFEM.TimberDesign.timberUltimateConfigurations import TimberDesignUltimateConfigurations
from RFEM.TimberDesign.timberServiceLimitStateConfigurations import TimberDesignServiceLimitStateConfigurations
from RFEM.TypesForTimberDesign.timberServiceClass import TimberServiceClass
from RFEM.LoadCasesAndCombinations.combinationWizard import CombinationWizard
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation
from RFEM.TypesForTimberDesign.timberEffectiveLengths import TimberEffectiveLengths
from RFEM.Tools.GetObjectNumbersByType import GetObjectNumbersByType
from RFEM.Results.resultTables import ResultTables, GetMaxValue, GetMinValue

# import additional modules
import xlwings as xw
import numpy as np

# create a new model
name = input('Please type the model name: ')
Model(True, name)

# starting modification of the model
Model.clientModel.service.begin_modification()

# deleting all available objects/materials/sections
Model.clientModel.service.delete_all()

# activate required add-ons
SetAddonStatus(Model.clientModel, AddOn.timber_design_active, True)

# creating requiered materials
Material(1, 'GL28c | EN 14080:2013-08')
Material(2, 'C24 | EN 338:2016-04')

# create section
Section(1, 'R_M1 0.14/0.28', 1)
Section(2, 'R_M1 0.14/0.14', 2)
Section(3, 'R_M1 0.14/0.26', 1)
Section(4, 'R_M1 0.12/0.12', 2)

# setting static analysis settings
StaticAnalysisSettings(1, analysis_type = StaticAnalysisType.GEOMETRICALLY_LINEAR)

# Setting loadcases & combinations
LoadCasesAndCombinations({
                    "current_standard_for_combination_wizard": 6066,
                    "activate_combination_wizard_and_classification": True,
                    "activate_combination_wizard": True,
                    "result_combinations_active": False,
                    "result_combinations_parentheses_active": False,
                    "result_combinations_consider_sub_results": False,
                    "combination_name_according_to_action_category": False
                        })

# creating requiered load cases
LoadCase(1, 'self-weight', [True, 0, 0, 1], ActionCategoryType.ACTION_CATEGORY_PERMANENT_G)
LoadCase(2, 'snow', [False], ActionCategoryType.ACTION_CATEGORY_SNOW_ICE_LOADS_H_LESS_OR_EQUAL_TO_1000_M_QS)

CombinationWizard(1, 'Load Wizard 1', static_analysis_settings = 1)

# creating variables for the loading in later stage of the script
loading1 = ''
loading2 = ''

for i in range(5):
    j = i * 11
    k = i * 5

    Node(j + 1 , 0, k, 0)
    Node(j + 2, 0, k, -4)
    Node(j + 3, 14, k, 0)
    Node(j + 4, 14, k, -4)
    Node(j + 5, 7, k, -5.8)

    # creating members for the first beam type
    Member(j + 1,start_node_no = j + 1, end_node_no = j + 2, start_section_no = 2, end_section_no = 2)
    Member(j + 2,start_node_no = j + 3, end_node_no = j + 4,start_section_no = 2, end_section_no = 2)
    Member(j + 3,start_node_no = j + 2, end_node_no = j + 5,start_section_no = 1, end_section_no = 1)
    Member(j + 4,start_node_no = j + 5, end_node_no = j + 4,start_section_no = 1, end_section_no = 1)
    Member.Truss(j + 5,start_node_no = j + 2, end_node_no = j + 4, section_no = 3)

    # creating nodes on existing members to finish design of truss
    Node.OnMember(j + 6, j + 3, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.3333])
    Node.OnMember(j + 7, j + 3, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.6667])
    Node.OnMember(j + 8, j + 4, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.3333])
    Node.OnMember(j + 9, j + 4, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.6667])
    Node.OnMember(j + 10, j + 5, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.3333])
    Node.OnMember(j + 11, j + 5, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.6667])

    # creating truss member
    Member.Truss(j + 6, start_node_no = j + 6, end_node_no = j + 10, section_no = 4)
    Member.Truss(j + 7, start_node_no = j + 10, end_node_no = j + 7, section_no = 4)
    Member.Truss(j + 8, start_node_no = j + 10, end_node_no = j + 5, section_no = 4)
    Member.Truss(j + 9, start_node_no = j + 5, end_node_no = j + 11, section_no = 4)
    Member.Truss(j + 10, start_node_no = j + 11, end_node_no = j + 8, section_no = 4)
    Member.Truss(j + 11, start_node_no = j + 11, end_node_no = j + 9, section_no = 4)

    # adding loading to the trusses
    # loading on the structure is simplified in this example
    if j + 1 == 1 or j + 1 == 45:
        loading1 = loading1 + ' ' +  str(j + 3) + ' ' + str(j + 4)
        MemberLoad(1, 1, loading1, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 1000)
        MemberLoad(3, 2, loading1, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 1600)

    else:
        loading2 = loading2 + ' ' + str(j + 3) + ' ' + str(j + 4)
        MemberLoad(2, 1, loading2, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 2000)
        MemberLoad(4, 2, loading2, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 3150)

# connecting trusses with each other
j = 55
for i in range(4):
    m = i * 11
    Member.Truss(j + 1, start_node_no = m + 2, end_node_no = m + 13, section_no = 2)
    Member.Truss(j + 2, start_node_no = m + 4, end_node_no = m + 15, section_no = 2)
    Member.Truss(j + 3, start_node_no = m + 5, end_node_no = m + 16, section_no = 2)
    Member.Truss(j + 4, start_node_no = m + 6, end_node_no = m + 17, section_no = 2)
    Member.Truss(j + 5, start_node_no = m + 7, end_node_no = m + 18, section_no = 2)
    Member.Truss(j + 6, start_node_no = m + 8, end_node_no = m + 19, section_no = 2)
    Member.Truss(j + 7, start_node_no = m + 9, end_node_no = m + 20, section_no = 2)
    j = j + 7

# creating the stiffening of the hall
# deleting unused members
Member.DeleteMember('49 50 51 52 53 54 55')
Node.DeleteNode('54 55')
Line.DeleteLine('49 50 51 52 53 54 55 153 154 155 156 157 158')

# adding bracing
# walls
Node.OnMember(58, 64, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.5])
Member.Truss(84, start_node_no = 25, end_node_no  = 58, section_no = 2)
Member.Truss(85, start_node_no = 58, end_node_no  = 14, section_no = 2)

Node.OnMember(59, 63, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.5])
Member.Truss(86, start_node_no = 12, end_node_no = 59, section_no = 2)
Member.Truss(87, start_node_no = 59, end_node_no = 23, section_no = 2)

# roof
Member.Truss(88, start_node_no = 9, end_node_no = 15, section_no = 2)
Member.Truss(89, start_node_no = 20, end_node_no = 26, section_no = 2)
Member.Truss(90, start_node_no = 31, end_node_no = 37, section_no = 2)
Member.Truss(91, start_node_no = 42, end_node_no = 48, section_no = 2)

Member.Truss(92, start_node_no = 6, end_node_no = 13, section_no = 2)
Member.Truss(93, start_node_no = 17, end_node_no = 24, section_no = 2)
Member.Truss(94, start_node_no = 28, end_node_no = 35, section_no = 2)
Member.Truss(95, start_node_no = 39, end_node_no = 46, section_no = 2)

Member.Truss(96, start_node_no = 20, end_node_no = 30, section_no = 2)
Member.Truss(97, start_node_no = 30, end_node_no = 16, section_no = 2)
Member.Truss(98, start_node_no = 16, end_node_no = 29, section_no = 2)
Member.Truss(99, start_node_no = 29, end_node_no = 17, section_no = 2)

# replacing the front of the hall and bracing it
Node(56, 4.667, 20, 0)
Member.Truss(100, start_node_no = 56, end_node_no = 51, section_no = 2)

Node(57, 9.333, 20, 0)
Member.Truss(101, start_node_no = 57, end_node_no = 52, section_no = 2)

Member.Truss(102, start_node_no = 45, end_node_no = 51, section_no = 2)
Member.Truss(103, start_node_no = 52, end_node_no = 47, section_no = 2)

# adding suppoerts to the structure
nodes_no = [1, 3, 12, 14, 23, 25, 34, 36, 45, 47, 56, 57]
NodalSupport(1, '1 3 12 14 23 25 34 36 45 47 56 57', NodalSupportType.HINGED)

# defining service class for the hall
member_lst = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_MEMBER)
# this is a temporary fix, as GetObjetNumbersByType returns a list with 0 value
if member_lst[0] == 0:
    member_lst.remove(0)
TimberServiceClass(1, members = ' '.join(str(x) for x in member_lst), service_class = TimberServiceClassServiceClass.TIMBER_SERVICE_CLASS_TYPE_1)

# assigning effective lengths
member_lst = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_MEMBER)
# this is a temporary fix, as GetObjetNumbersByType returns a list with 0 value
if member_lst[0] == 0:
    member_lst.remove(0)
for i in [3,4,14,15,25,26,36,37,47,48]:
    member_lst.remove(i)
TimberEffectiveLengths(1, members = ' '.join(str(x) for x in member_lst))

# defining design situations
DesignSituation(1, DesignSituationType.DESIGN_SITUATION_TYPE_STR_PERMANENT_AND_TRANSIENT_6_10, True, params = {'combination_wizard': 1})
DesignSituation(2, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_CHARACTERISTIC, True, params = {'combination_wizard': 1})
DesignSituation(3, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_QUASI_PERMANENT, True, params = {'combination_wizard': 1})
DesignSituation(4, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_CHARACTERISTIC_QUASI_PERMANENT, True, params = {'combination_wizard': 1})

# set the design configurations
TimberDesignUltimateConfigurations(1, 'ULS1', members_no = 'All')
TimberDesignServiceLimitStateConfigurations(1, 'SLS1', members_no = 'All')

# finishing modification and calculating the model
Model.clientModel.service.finish_modification()
PlausibilityCheck(True)
Calculate_all()

# write outputs to an excel sheet
wb = xw.Book()

# Creating excel sheet for different outputs
wb.sheets.add('Nodal Deformation')
wb.sheets.add('Nodal Support')
wb.sheets.add('Member Deformation')
wb.sheets.add('Internal Force')
wb.sheets['Sheet1'].delete()

nodaldeformation = wb.sheets['Nodal Deformation']
nodalsupport = wb.sheets['Nodal Support']
deformationSheet = wb.sheets['Member Deformation']
InternalForceSheet = wb.sheets['Internal Force']

# Adding headers for different output columns
node_number, nodeSupportType, nodesupType = ['Node Number'], ['Support Type'], [' ']
nodeDisp_abs, nodeDisp_x, nodeDisp_y, nodeDisp_z = ['Nodal Deformation (abs) (mm)'], ['Nodal Deformation (ux) (mm)'], ['Nodal Deformation (uy) (mm)'], ['Nodal Deformation (uz) (mm)']
nodeRotation_x, nodeRotation_y, nodeRotation_z = ['Rotation (ϕx) (mrad)'], ['Rotation (ϕy) (mrad)'], ['Rotation (ϕz) (mrad)']
nodeSupportForce_x, nodeSupportForce_y, nodeSupportForce_z = ['Support Force (Px) (kN)'], ['Support Force (Py) (kN)'], ['Support Force (Pz) (kN)']
nodeMoment_x, nodeMoment_y, nodeMoment_z = ['Support Moment (Mx) (kNm)'], ['Support Moment (My) (kNm)'], ['Support Moment (Mz) (kNm)']

# Getting nodal result values
nodes = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_NODE)
nodes_no = ['', 1, 3, 12, 14, 23, 25, 34, 36, 45, 47, 56, 57]
for j in nodes:
    dispTab = ResultTables.NodesDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 2, j)
    nodisp_abs = GetMaxValue(dispTab, 'displacement_absolute') * 1000
    nodisp_x = GetMaxValue(dispTab, 'displacement_x') * 1000
    nodisp_y = GetMaxValue(dispTab, 'displacement_y') * 1000
    nodisp_z = GetMaxValue(dispTab, 'displacement_z') * 1000
    nodeRot_x = GetMaxValue(dispTab, 'rotation_x') * 1000
    nodeRot_y = GetMaxValue(dispTab, 'rotation_y') * 1000
    nodeRot_z = GetMaxValue(dispTab, 'rotation_z') * 1000
    node_number.append(j)
    nodeDisp_abs.append(round(nodisp_abs, 3))
    nodeDisp_x.append(round(nodisp_x, 3))
    nodeDisp_y.append(round(nodisp_y, 3))
    nodeDisp_z.append(round(nodisp_z, 3))
    nodeRotation_x.append(round(nodeRot_x, 3))
    nodeRotation_y.append(round(nodeRot_y, 3))
    nodeRotation_z.append(round(nodeRot_z, 3))

    nodeType = '-'
    if j in nodes_no:
        nodeType = 'Hinged'
        nodesupforce_x = GetMaxValue(dispTab, 'support_forces_p_x')
        nodesupforce_y = GetMaxValue(dispTab, 'support_forces_p_y')
        nodesupforce_z = GetMaxValue(dispTab, 'support_forces_p_z')
        nodemom_x = GetMaxValue(dispTab, 'support_moments_m_x')
        nodemom_y = GetMaxValue(dispTab, 'support_moments_m_y')
        nodemom_z = GetMaxValue(dispTab, 'support_moments_m_z')
        nodeSupportForce_x.append(round(nodesupforce_x, 3))
        nodeSupportForce_y.append(round(nodesupforce_y, 3))
        nodeSupportForce_z.append(round(nodesupforce_z, 3))
        nodeMoment_x.append(round(nodemom_x, 3))
        nodeMoment_y.append(round(nodemom_y, 3))
        nodeMoment_z.append(round(nodemom_z, 3))
        nodesupType.append(nodeType)

    nodeSupportType.append(nodeType)

node_number = np.array([node_number]).T
nodeSupportType = np.array([nodeSupportType]).T
nodeDisp_abs = np.array([nodeDisp_abs]).T
nodeDisp_x = np.array([nodeDisp_x]).T
nodeDisp_y = np.array([nodeDisp_y]).T
nodeDisp_z = np.array([nodeDisp_z]).T
nodeRotation_x = np.array([nodeRotation_x]).T
nodeRotation_y = np.array([nodeRotation_y]).T
nodeRotation_z = np.array([nodeRotation_z]).T

nodes_no = np.array([nodes_no]).T
nodesupType = np.array([nodesupType]).T
nodeSupportForce_x = np.array([nodeSupportForce_x]).T
nodeSupportForce_y = np.array([nodeSupportForce_y]).T
nodeSupportForce_z = np.array([nodeSupportForce_z]).T
nodeMoment_x = np.array([nodeMoment_x]).T
nodeMoment_y = np.array([nodeMoment_y]).T
nodeMoment_z = np.array([nodeMoment_z]).T

# adding headers for output sheets
maxDisplacement_abs, maxDisplacement_x, maxDisplacement_y, maxDisplacement_z = ['Maximum Deformation (abs) (mm)'], ['Maximum Deformation (in x) (mm)'], ['Maximum Deformation (in y) (mm)'], ['Maximum Deformation (in z) (mm)']
maxForce_n, maxForce_vy, maxForce_vz, maxMoment_mt, maxMoment_my, maxMoment_mz = ['Maximum Internal Force (N) (kN)'], ['Maximum Internal Force (Vy) (kN)'], ['Maximum Internal Force (Vz) (kN)'], ['Maximum Internal Moment (Mt) (kNm)'], ['Maximum Internal Moment (My) (kNm)'], ['Maximum Internal Moment (Mz) (kNm)']

# getting member result values
beam_column = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_MEMBER)
k = 1
for j in beam_column:
    dispTable = ResultTables.MembersLocalDeformations(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 2, j)
    maxDisp_abs = GetMaxValue(dispTable, 'displacement_absolute') * 1000
    maxDisp_x = GetMaxValue(dispTable, 'displacement_x') * 1000
    maxDisp_y = GetMaxValue(dispTable, 'displacement_y') * 1000
    maxDisp_z = GetMaxValue(dispTable, 'displacement_z') * 1000
    maxDisplacement_abs.append(round(maxDisp_abs, 3))
    maxDisplacement_x.append(round(maxDisp_x, 3))
    maxDisplacement_y.append(round(maxDisp_y, 3))
    maxDisplacement_z.append(round(maxDisp_z, 3))

    momentTable = ResultTables.MembersInternalForces(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 2, j)
    # maximum normal force
    if abs(GetMinValue(momentTable, 'internal_force_n')) > abs(GetMaxValue(momentTable, 'internal_force_n')):
        maxFor_n = GetMinValue(momentTable, 'internal_force_n') / 1000
    else:
        maxFor_n = GetMaxValue(momentTable, 'internal_force_n') / 1000

    # maximum shear force
    if abs(GetMinValue(momentTable, 'internal_force_vy')) > abs(GetMaxValue(momentTable, 'internal_force_vy')):
        maxFor_y = GetMinValue(momentTable, 'internal_force_vy') / 1000
    else:
        maxFor_y = GetMaxValue(momentTable, 'internal_force_vy') / 1000

    if abs(GetMinValue(momentTable, 'internal_force_vz')) > abs(GetMaxValue(momentTable, 'internal_force_vz')):
        maxFor_z = GetMinValue(momentTable, 'internal_force_vz') / 1000
    else:
        maxFor_z = GetMaxValue(momentTable, 'internal_force_vz') / 1000

    # maximum moment
    if abs(GetMinValue(momentTable, 'internal_force_mt')) > abs(GetMaxValue(momentTable, 'internal_force_mt')):
        maxMoment_t = GetMinValue(momentTable, 'internal_force_mt') / 1000
    else:
        maxMoment_t = GetMaxValue(momentTable, 'internal_force_mt') / 1000

    maxMoment_t = GetMaxValue(momentTable, 'internal_force_mt') / 1000
    maxMoment_y = GetMaxValue(momentTable, 'internal_force_my') / 1000
    maxMoment_z = GetMaxValue(momentTable, 'internal_force_mz') / 1000

    maxForce_n.append(round(maxFor_n, 3))
    maxForce_vy.append(round(maxFor_y, 3))
    maxForce_vz.append(round(maxFor_z, 3))
    maxMoment_mt.append(round(maxMoment_t, 3))
    maxMoment_my.append(round(maxMoment_y, 3))
    maxMoment_mz.append(round(maxMoment_z, 3))
    k += 1

member_no = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_MEMBER)
member_no.insert(0, 'Member Number')

member_number = np.array([member_no]).T
maxDisplacement_abs = np.array([maxDisplacement_abs]).T
maxDisplacement_x = np.array([maxDisplacement_x]).T
maxDisplacement_y = np.array([maxDisplacement_y]).T
maxDisplacement_z = np.array([maxDisplacement_z]).T
maxForce_n = np.array([maxForce_n]).T
maxForce_vy = np.array([maxForce_vy]).T
maxForce_vz = np.array([maxForce_vz]).T
maxMoment_mt = np.array([maxMoment_mt]).T
maxMoment_my = np.array([maxMoment_my]).T
maxMoment_mz = np.array([maxMoment_mz]).T

# adding values to the excel sheet
nodaldeformation["A2:J500"].clear_contents()
nodaldeformation["A2:I2"].font.bold = True

nodalsupport["A2:J500"].clear_contents()
nodalsupport["A2:H2"].font.bold = True

deformationSheet["A2:J500"].clear_contents()
deformationSheet["A2:F2"].font.bold = True

InternalForceSheet["A2:J500"].clear_contents()
InternalForceSheet["A2:H2"].font.bold = True

nodaldeformation["A2"].value = node_number
nodaldeformation["B2"].value = nodeSupportType
nodaldeformation["C2"].value = nodeDisp_abs
nodaldeformation["D2"].value = nodeDisp_x
nodaldeformation["E2"].value = nodeDisp_y
nodaldeformation["F2"].value = nodeDisp_z
nodaldeformation["G2"].value = nodeRotation_x
nodaldeformation["H2"].value = nodeRotation_y
nodaldeformation["I2"].value = nodeRotation_z

nodalsupport["A2"].value = nodes_no
nodalsupport["B2"].value = nodesupType
nodalsupport["C2"].value = nodeSupportForce_x
nodalsupport["D2"].value = nodeSupportForce_y
nodalsupport["E2"].value = nodeSupportForce_z
nodalsupport["F2"].value = nodeMoment_x
nodalsupport["G2"].value = nodeMoment_y
nodalsupport["H2"].value = nodeMoment_z

deformationSheet["A2"].value = member_number

deformationSheet["B2"].value = maxDisplacement_abs
deformationSheet["C2"].value = maxDisplacement_x
deformationSheet["D2"].value = maxDisplacement_y
deformationSheet["E2"].value = maxDisplacement_z

InternalForceSheet["A2"].value = member_number
InternalForceSheet["B2"].value = maxForce_n
InternalForceSheet["C2"].value = maxForce_vy
InternalForceSheet["D2"].value = maxForce_vz
InternalForceSheet["E2"].value = maxMoment_mt
InternalForceSheet["F2"].value = maxMoment_my
InternalForceSheet["G2"].value = maxMoment_mz

print('Done')
