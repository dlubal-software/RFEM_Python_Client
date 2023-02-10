import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import NodalSupportType, MemberLoadDirection, AnalysisType, ActionCategoryType, AddOn, SetType
from RFEM.initModel import Model, insertSpaces, Calculate_all, SetAddonStatus
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation, DesignSituationType
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.dataTypes import inf
from RFEM.TypesForSteelDesign.steelEffectiveLengths import SteelEffectiveLengths
from RFEM.TypesForSteelDesign.steelBoundaryConditions import SteelBoundaryConditions

Model()
Model.clientModel.service.begin_modification()

SetAddonStatus(Model.clientModel, AddOn.steel_design_active, True)

Node(1, 0.0, 0.0, 0.0)
Node(2, 5.0, 0.0, 0.0)
Node(3, 10.0, 0.0, 0.0)

Material(1, 'S235')

Section(1, 'IPE 300')

NodalSupport(1, '1 3', NodalSupportType.FIXED)



#Member(1, 1, 2, params=p)
Member(1, 1, 2)
#Member(2, 2, 3, params=p)
Member(2, 2, 3)

p = {
    "design_properties_activated": True
}

#MemberSet(1, '1 2', SetType.SET_TYPE_CONTINUOUS, params=p) nicht notwendig
MemberSet(1, '1 2', SetType.SET_TYPE_CONTINUOUS)

p = {
    "design_properties_via_parent_member_set": True,
    "design_properties_parent_member_set": 1
}

Member(1, 1, 2, params=p)
Member(2, 2, 3, params=p)

Model.clientModel.service.finish_modification()