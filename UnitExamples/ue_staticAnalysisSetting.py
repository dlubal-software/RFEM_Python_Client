import sys
sys.path.append(".")
from RFEM.enums import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *

if __name__ == '__main__':
    
    Model(True, "StaticAnalysisSettings")
    Model.clientModel.service.begin_modification()

    # Set Base Settings
    StaticAnalysisSettings(1, 'Geometrisch-linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Set Base Settings
    StaticAnalysisSettings.GeometricallyLinear(2, 2,'Geometric-linear',[True, 1.5, True],False,False,StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,[True,0,0,1.0])

    # Set Base Settings
    StaticAnalysisSettings.LargeDeformation(3, standard_precision_and_tolerance_settings = [True, 0.01, 0.01, 1.0],)

    StaticAnalysisSettings.SecondOrderPDelta(1)

    Model.clientModel.service.finish_modification()

