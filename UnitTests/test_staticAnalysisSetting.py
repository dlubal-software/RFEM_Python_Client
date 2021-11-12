import sys
sys.path.append(".")
import pytest
from RFEM.enums import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *

def test_default():
    
    clientModel.service.begin_modification()

    # Set Base Settings
    StaticAnalysisSettings(1, 'Geometrisch-linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    clientModel.service.finish_modification()

def test_GeometricallyLinear():

    clientModel.service.begin_modification()

    # Set Base Settings
    StaticAnalysisSettings.GeometricallyLinear(1,2,'Geometric-linear',[True, 1.5, True],False,False,StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,[True,0,0,1.0])

    clientModel.service.finish_modification()

def test_LargeDeformation():

    clientModel.service.begin_modification()

    # Set Base Settings
    StaticAnalysisSettings.LargeDeformation(1,standard_precision_and_tolerance_settings = [True, 0.01, 0.01, 1.0],)

    clientModel.service.finish_modification()

def test_SecondOrderPDelta():

    clientModel.service.begin_modification()

    # Set Base Settings
    StaticAnalysisSettings.SecondOrderPDelta(1)

    clientModel.service.finish_modification()

