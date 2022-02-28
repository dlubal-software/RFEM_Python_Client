import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

# Import der Bibliotheken
from RFEM.enums import NodalSupportType, StaticAnalysisType, LoadDirectionType
from RFEM.initModel import Model, Calculate_all
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.TypesForSteelDesign.steelEffectiveLengths import SteelEffectiveLengths


Model(True, 'effect')
Model.clientModel.service.begin_modification()

Material(1, "S235")

Section(1, "HEA 200")

Node(1, 0, 0, 0)
Node(2, 0, 0, -5)

Member(1, 1, 2)

NodalSupport(1, '1', NodalSupportType.FIXED)

SteelEffectiveLengths()

Model.clientModel.service.finish_modification()

