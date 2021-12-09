from RFEM.enums import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness 
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.solid import Solid
from RFEM.BasicObjects.opening import Opening
from RFEM.BasicObjects.lineSet import LineSet
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.BasicObjects.surfaceSet import SurfaceSet
from RFEM.BasicObjects.solidSet import SolidSet
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Loads.surfaceLoad import SurfaceLoad
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

if __name__ == "__main__":

    optimizationResults = Model.clientModel.service.get_optimized_formula_parameters()

    if optimizationResults != None:
        for i in range(0, len(optimizationResults.row)):
            for j in range(0, len(optimizationResults.row[i].section)):

                if hasattr(optimizationResults.row[i].section[j], 'top_text'):
                    print(optimizationResults.row[i].section[j].top_text)

                for k in range(0, len(optimizationResults.row[i].section[j].elements[0])):
                    print(optimizationResults.row[i].section[j].elements[0][k].column_name +
                          " " + optimizationResults.row[i].section[j].elements[0][k].value)
