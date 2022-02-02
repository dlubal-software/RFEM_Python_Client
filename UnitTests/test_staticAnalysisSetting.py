import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model
from RFEM.enums import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings

if Model.clientModel is None:
    Model()

def test_StaticAnalysisSettings():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Set Static Analysis Settings
    StaticAnalysisSettings(1, 'Geometrisch-linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)
    StaticAnalysisSettings.GeometricallyLinear(0,2,'Geometric-linear',[True, 1.5, True],False,False,
                                               StaticAnalysisSettingsMethodOfEquationSystem.METHOD_OF_EQUATION_SYSTEM_DIRECT,
                                               StaticAnalysisSettingsPlateBendingTheory.PLATE_BENDING_THEORY_MINDLIN,[True,0,0,1.0])
    StaticAnalysisSettings.LargeDeformation(0,3,standard_precision_and_tolerance_settings = [True, 0.01, 0.01, 1.0])
    StaticAnalysisSettings.SecondOrderPDelta(0,4)

    Model.clientModel.service.finish_modification()
