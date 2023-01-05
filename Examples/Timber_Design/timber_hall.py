#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

#This script follows the basic design of conrete beams / slabs
#It is based on the following webinar: https://www.dlubal.com/en/support-and-learning/learning/webinars/002410

#Import all modules required to access RFEM

from RFEM.enums import *
from RFEM.initModel import Model, SetAddonStatus, SetModelType, Calculate_all
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

#timber specific modules

from RFEM.TimberDesign.timberUltimateConfigurations import TimberDesignUltimateConfigurations
from RFEM.TimberDesign.timberServiceLimitStateConfigurations import TimberDesignServiceLimitStateConfigurations
from RFEM.TypesForTimberDesign.timberServiceClass import TimberServiceClass

from RFEM.LoadCasesAndCombinations.combinationWizard import CombinationWizard

from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation

from RFEM.Tools.GetObjectNumbersByType import GetObjectNumbersByType

from RFEM.Calculate.meshSettings import GetModelInfo

from RFEM.Results.resultTables import ResultTables

#Create a new Model

name = input('Please type the model name: ')
Model(True, name)

#deleting all available objects/materials/sections

Model.clientModel.service.delete_all()

#activate required add-ons

SetAddonStatus(Model.clientModel, AddOn.timber_design_active, True)

#creating requiered materials

Material(1, 'GL28c | EN 14080:2013-08')
Material(2, 'C24 | EN 338:2016-04')

#create section

Section(1, 'R_M1 0.14/0.28', 1)
Section(2, 'R_M1 0.14/0.14', 2)
Section(3, 'R_M1 0.14/0.26', 1)
Section(4, 'R_M1 0.12/0.12', 2)

# setting static analysis settings
StaticAnalysisSettings(1, analysis_type = StaticAnalysisType.GEOMETRICALLY_LINEAR)

# Setting Loadcases & Combinations
LoadCasesAndCombinations({
                    "current_standard_for_combination_wizard": 6066,
                    "activate_combination_wizard_and_classification": True,
                    "activate_combination_wizard": True,
                    "result_combinations_active": False,
                    "result_combinations_parentheses_active": False,
                    "result_combinations_consider_sub_results": False,
                    "combination_name_according_to_action_category": False
                 })

# Creating requiered load cases
LoadCase(1, 'self-weight', [True, 0, 0, 1], ActionCategoryType.ACTION_CATEGORY_PERMANENT_G)
LoadCase(2, 'snow', [False], ActionCategoryType.ACTION_CATEGORY_SNOW_ICE_LOADS_H_LESS_OR_EQUAL_TO_1000_M_QS)

CombinationWizard(1, 'Load Wizard 1', 'GENERATE_LOAD_COMBINATIONS', 1)
#creating the model

# Creating variables for the loading in later stage of the script
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

    #creating members for the first beam type

    Member(j + 1,start_node_no = j + 1, end_node_no = j + 2, start_section_no = 2, end_section_no = 2)
    Member(j + 2,start_node_no = j + 3, end_node_no = j + 4,start_section_no = 2, end_section_no = 2)
    Member(j + 3,start_node_no = j + 2, end_node_no = j + 5,start_section_no = 1, end_section_no = 1)
    Member(j + 4,start_node_no = j + 5, end_node_no = j + 4,start_section_no = 1, end_section_no = 1)
    Member.Truss(j + 5,start_node_no = j + 2, end_node_no = j + 4, section_no = 3)

    #Creating nodes on existing members to finish design of truss

    Node.OnMember(j + 6, j + 3, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.3333])
    Node.OnMember(j + 7, j + 3, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.6667])
    Node.OnMember(j + 8, j + 4, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.3333])
    Node.OnMember(j + 9, j + 4, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.6667])
    Node.OnMember(j + 10, j + 5, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.3333])
    Node.OnMember(j + 11, j + 5, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.6667])

    #creating truss member

    Member.Truss(j + 6, start_node_no = j + 6, end_node_no = j + 10, section_no = 4)
    Member.Truss(j + 7, start_node_no = j + 10, end_node_no = j + 7, section_no = 4)
    Member.Truss(j + 8, start_node_no = j + 10, end_node_no = j + 5, section_no = 4)
    Member.Truss(j + 9, start_node_no = j + 5, end_node_no = j + 11, section_no = 4)
    Member.Truss(j + 10, start_node_no = j + 11, end_node_no = j + 8, section_no = 4)
    Member.Truss(j + 11, start_node_no = j + 11, end_node_no = j + 9, section_no = 4)


    # Adding loading to the trusses

    if j + 1 == 1 or j + 1 == 45:
        loading1 = loading1 + ' ' +  str(j + 3) + ' ' + str(j + 4)
        MemberLoad(1, 1, loading1, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 1000)
        MemberLoad(3, 2, loading1, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 1600)

    else:
        loading2 = loading2 + ' ' + str(j + 3) + ' ' + str(j + 4)
        MemberLoad(2, 1, loading2, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 2000)
        MemberLoad(4, 2, loading2, MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 3300)

    #Loading on the structure is simplified in this example

# Connecting trusses with each other

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

# Creating the stiffening of the hall
# Deleting unused members

Member.DeleteMember('49 50 51 52 53 54 55')
Node.DeleteNode('54 55')
Line.DeleteLine('49 50 51 52 53 54 55')

# Adding Bracing

# Walls
Node.OnMember(58, 64, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.5])
Member.Truss(84, start_node_no = 25, end_node_no  = 58, section_no = 2)
Member.Truss(85, start_node_no = 58, end_node_no  = 14, section_no = 2)


Node.OnMember(59, 63, NodeReferenceType.REFERENCE_TYPE_L, parameters = [True, 0.5])
Member.Truss(86, start_node_no = 12, end_node_no = 59, section_no = 2)
Member.Truss(87, start_node_no = 59, end_node_no = 23, section_no = 2)


# Roof
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


# Replacing the front of the hall and bracing it
Node(56, 4.667, 20, 0)
Member.Truss(100, start_node_no = 56, end_node_no = 51, section_no = 2)

Node(57, 9.333, 20, 0)
Member.Truss(101, start_node_no = 57, end_node_no = 52, section_no = 2)


Member.Truss(102, start_node_no = 45, end_node_no = 51, section_no = 2)
Member.Truss(103, start_node_no = 52, end_node_no = 47, section_no = 2)


# Adding suppoerts to the structure
NodalSupport(1, '1 3 12 14 23 25 34 36 45 47 56 57', NodalSupportType.HINGED)

# Defining service class for the hall
TimberServiceClass(1, members = ' '.join(str(x) for x in GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_MEMBER)), service_class = TimberServiceClassServiceClass.TIMBER_SERVICE_CLASS_TYPE_1)

# Defining Design Situations
DesignSituation(1, DesignSituationType.DESIGN_SITUATION_TYPE_STR_PERMANENT_AND_TRANSIENT_6_10, True, params = {'combination_wizard': 1})
DesignSituation(2, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_CHARACTERISTIC, True, params = {'combination_wizard': 1})
DesignSituation(3, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_QUASI_PERMANENT, True, params = {'combination_wizard': 1})
DesignSituation(4, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_CHARACTERISTIC_QUASI_PERMANENT, True, params = {'combination_wizard': 1})

TimberDesignUltimateConfigurations(1, 'ULS1', members_no = 'All')
TimberDesignServiceLimitStateConfigurations(1, 'SLS1', members_no = 'All')
Calculate_all()

