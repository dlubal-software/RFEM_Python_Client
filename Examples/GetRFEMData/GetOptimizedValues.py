from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.solidSet import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.surfaceLoad import *
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
