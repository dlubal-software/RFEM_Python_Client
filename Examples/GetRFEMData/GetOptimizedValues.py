import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')
from RFEM.initModel import Model, CheckIfMethodOrTypeExists

if __name__ == "__main__":

    Model()
    if CheckIfMethodOrTypeExists(Model.clientModel,'get_optimized_formula_parameters'):

        optimizationResults = Model.clientModel.service.get_optimized_formula_parameters()
        if len(optimizationResults) > 0:
            for i in range(0, len(optimizationResults.row)):
                for j in range(0, len(optimizationResults.row[i].section)):

                    if hasattr(optimizationResults.row[i].section[j], 'top_text'):
                        print(optimizationResults.row[i].section[j].top_text)

                    for k in range(0, len(optimizationResults.row[i].section[j].elements[0])):
                        print(optimizationResults.row[i].section[j].elements[0][k].column_name +
                              " " + optimizationResults.row[i].section[j].elements[0][k].value)
