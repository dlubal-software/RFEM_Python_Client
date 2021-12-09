import sys
sys.path.append(".")
from RFEM.Loads.lineLoad import LineLoad
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
from RFEM.LoadCasesAndCombinations.spectralAnalysisSettings import SpectralAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Loads.surfaceLoad import SurfaceLoad
import pytest

def test_spectral_analysis_implemented():

    exist = method_exists(Model.clientModel,'set_spectral_analysis_settings')
    assert exist == False #test fail once method is in T9 master or GM

@pytest.mark.skip("all tests still WIP")
def test_spectral_analysis_settings():

	#spectral analysis is not yet supported in released RFEM6 in WS
	Model(True, "SpectralSettings")
	Model.clientModel.service.begin_modification('new')

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
	
	Model.clientModel.service.finish_modification()
