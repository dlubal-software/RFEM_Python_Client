import sys
sys.path.append(".")
from RFEM.Loads.lineLoad import LineLoad
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
from RFEM.LoadCasesAndCombinations.spectralAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.surfaceLoad import *
import pytest

def test_spectral_analysis_implemented():

    exist = method_exists(clientModel,'set_spectral_analysis_settings')
    assert exist == False #test fail once method is in T9 master or GM

@pytest.mark.skip("all tests still WIP")
def test_spectral_analysis_settings():

	clientModel.service.begin_modification('new')

	# Create Material
	Material(1, 'S235')

	#Create Spectral Analysis Settings
	SpectralAnalysisSettings(1, 'SpectralSettings_1', PeriodicResponseCombinationRule.SRSS, DirectionalComponentCombinationRule.SRSS)
	SpectralAnalysisSettings(2, 'SpectralSettings_2', PeriodicResponseCombinationRule.SRSS, DirectionalComponentCombinationRule.SCALED_SUM, equivalent_linear_combination=True, save_mode_results=True, signed_dominant_mode_results=True)
	SpectralAnalysisSettings(3, 'SpectralSettings_3', PeriodicResponseCombinationRule.SRSS, DirectionalComponentCombinationRule.SCALED_SUM, directional_component_scale_value=0.4)
	SpectralAnalysisSettings(4, 'SpectralSettings_4', PeriodicResponseCombinationRule.CQC, DirectionalComponentCombinationRule.SCALED_SUM, constant_d_for_each_mode=12)
	SpectralAnalysisSettings(5, 'SpectralSettings_5', PeriodicResponseCombinationRule.CQC, DirectionalComponentCombinationRule.SCALED_SUM, damping_for_cqc_rule=CqsDampingRule.DIFFERENT_FOR_EACH_MODE)
	SpectralAnalysisSettings(6, 'SpectralSettings_6', PeriodicResponseCombinationRule.CQC, DirectionalComponentCombinationRule.ABSOLUTE_SUM)

	print('Ready!')

	clientModel.service.finish_modification()

