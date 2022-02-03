import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.Imperfections.imperfectionCase import ImperfectionCase
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings

if Model.clientModel is None:
    Model()

def test_member_set():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()
    StaticAnalysisSettings()
    LoadCase(2, 'LC2')
    ImperfectionCase(2, '2')
    Model.clientModel.service.finish_modification()

    imp = Model.clientModel.service.get_imperfection_case(2)
    assert imp.type == 'IMPERFECTION_TYPE_LOCAL_IMPERFECTIONS'
    assert imp.assigned_to_load_cases == '2'
