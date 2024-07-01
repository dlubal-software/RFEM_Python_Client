import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import *
from RFEM.initModel import Model, insertSpaces, Calculate_all, SetAddonStatus
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForLines.lineSupport import LineSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.combinationWizard import CombinationWizard
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.modalAnalysisSettings import ModalAnalysisSettings
from RFEM.LoadCasesAndCombinations.spectralAnalysisSettings import SpectralAnalysisSettings
from RFEM.DynamicLoads.responseSpectrum import ResponseSpectrum
from RFEM.Loads.surfaceLoad import SurfaceLoad
from RFEM.Results.resultTables import ResultTables

if __name__ == "__main__":
    # create structure
    Model(True, 'DynamicAnalysis.py')

    Material(1, 'C35/45')
    Section(1, 'SQ_M1 0.25')
    Thickness(1, 'Ceiling', 1, uniform_thickness_d=0.4)
    Thickness(2, 'Walls', 1, uniform_thickness_d=0.25)
    length = 10.5
    width = 13
    height = 0
    j = 0
    k = 0
    l = 0

    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, addOn=AddOn.modal_active, status=True)
    SetAddonStatus(Model.clientModel, addOn=AddOn.spectral_active, status=True)

    for i in range(3):
        Node(1 + j, 0, 0, height)
        Node(2 + j, length, 0, height)
        Node(3 + j, 0, width, height)
        Node(4 + j, length, width,height)
        Node(5 + j, length/3, 0, height)
        Node(6 + j, length/3, width, height)
        Node(7 + j, 2 * length/3, 0, height)
        Node(8 + j, 2 * length/3, width, height)
        Node(9 + j, 0, width/3, height)
        Node(10 + j, 0, 2 * width/3, height)
        Node(11 + j, length, width/3, height)
        Node(12 + j, length, 2 * width/3, height)

        j += 12
        height -= 5

    j = 0
    for i in range(2):
        Line(1 + l, insertSpaces([13 + j, 14 + j]))
        Line(2+ l, insertSpaces([13 + j, 15 + j]))
        Line(3 + l, insertSpaces([14 + j, 16 + j]))
        Line(4 + l, insertSpaces([15 + j, 16 + j]))

        l += 4
        j += 12

    # vertical lines
    l = 0
    j = 0
    for i in range(2):
        Line(9 + l, insertSpaces([1 + j, 13 + j]))
        Line(10 + l, insertSpaces([2 + j, 14 + j]))
        Line(11 + l, insertSpaces([3 + j, 15 + j]))
        Line(12 + l, insertSpaces([5 + j, 17 + j]))
        Line(13 + l, insertSpaces([7 + j, 19 + j]))
        Line(14 + l, insertSpaces([11 + j, 23 + j]))
        Line(15 + l, insertSpaces([6 + j, 18 + j]))
        Line(16 + l, insertSpaces([10 + j, 22 + j]))
        Line(17 + l, insertSpaces([9 + j, 21 + j]))

        l += 9
        j += 12

    # horizontal lines
    j = 0
    l = 0
    for i in range(3):
        Line(33 + l, insertSpaces([1 + j, 5 + j]))
        Line(34 + l, insertSpaces([1 + j, 9 + j]))
        Line(35 + l, insertSpaces([2 + j, 7 + j]))
        Line(36 + l, insertSpaces([2 + j, 11 + j]))
        Line(37 + l, insertSpaces([3 + j, 6 + j]))
        Line(38 + l, insertSpaces([3 + j, 10 + j]))

        l += 6
        j += 12

    # surfaces
    l = 0
    m = 0
    j = 0
    for i in range(2):
        Surface(1 + k, insertSpaces([1 + m, 2 + m, 3 + m, 4 + m]), 1)
        Surface(2 + k, insertSpaces([17 + l, 40 + j, 9 + l, 34 + j]), 2)
        Surface(3 + k, insertSpaces([12 + l, 33 + j, 9 + l, 39 + j]), 2)
        Surface(4 + k, insertSpaces([35 + j, 10 + l, 13 + l, 41 + j]), 2)
        Surface(5 + k, insertSpaces([36 + j, 10 + l, 14 + l, 42 + j]), 2)
        Surface(6 + k, insertSpaces([37 + j, 11 + l, 15 + l, 43 + j]), 2)
        Surface(7 + k, insertSpaces([38 + j, 11 + l, 16 + l, 44 + j]), 2)

        k += 7
        m += 4
        l += 9
        j += 6

    j = 0
    l = 0
    for i in range(2):
        Member(1 + j, 8 + l, 20 + l, 0, 1, 1)
        Member(2 + j, 4 + l, 16 + l, 0, 1, 1)
        Member(3 + j, 12 + l, 24 + l, 0, 1, 1)
        j += 3
        l += 12

    LineSupport(1, '33 34 35 36 37 38')
    NodalSupport(1, '4 8 12', NodalSupportType.HINGED)

    # Load Cases and Combinations/Settings
    LoadCasesAndCombinations({'activate_combination_wizard':'True'})
    CombinationWizard(1, 'Combi1', 1, 1, False, False, None, None)

    StaticAnalysisSettings(1)
    ModalAnalysisSettings(1)
    SpectralAnalysisSettings(1)

    ResponseSpectrum(1, params={'definition_type':'ACCORDING_TO_STANDARD'})

    LoadCase(1, 'Self-Weight', [True, 0, 0, 1], ActionCategoryType.ACTION_CATEGORY_PERMANENT_G)
    LoadCase(2, 'Dead Load', [False], ActionCategoryType.ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_A_DOMESTIC_RESIDENTIAL_AREAS_QI_A)
    LoadCase(3, 'Modal Analysis',action_category=ActionCategoryType.ACTION_CATEGORY_SEISMIC_ACTIONS_AE, params={'analysis_type':'ANALYSIS_TYPE_MODAL'})
    LoadCase(4, 'Spectral Analysis', action_category=ActionCategoryType.ACTION_CATEGORY_SEISMIC_ACTIONS_AE,
             params={
                        'analysis_type':'ANALYSIS_TYPE_RESPONSE_SPECTRUM',
                        'import_modal_analysis_from':'3',
                        'response_spectrum_is_enabled_in_any_direction':'True',
                        'response_spectrum_is_enabled_in_direction_x':'True',
                        'response_spectrum_is_enabled_in_direction_y':'True',
                        'response_spectrum_in_direction_x':'1',
                        'response_spectrum_in_direction_y':'1',
                        'response_spectrum_consider_accidental_torsion':'True',
                        'response_spectrum_eccentricity_for_x_direction_relative':'0.05',
                        'response_spectrum_eccentricity_for_y_direction_relative':'0.05'})

    LoadCombination(1, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 1, False, False, False, True, combination_items=[[1.35, 1, 0, False], [1.5, 2, 0, True]])
    DesignSituation(1, DesignSituationType.DESIGN_SITUATION_TYPE_EQU_PERMANENT_AND_TRANSIENT, True, params={'combination_wizard' :'1'})

    SurfaceLoad(1, 2, '1', 5000)

    Model.clientModel.service.finish_modification()

    Calculate_all()

    columnInternalForces = ResultTables.MembersInternalForces(loading_type=CaseObjectType.E_OBJECT_TYPE_DESIGN_SITUATION, loading_no=1)
    print(columnInternalForces)


    rsaSummaryX = ResultTables.SpectralAnalysisSummary(
        loading_type=CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no=4,
        envelope_type=SpectralAnalysisEnvelopeType.SPECTRAL_ANALYSIS_DIRECTION_X)
    print(rsaSummaryX)

    nodeDeformationsX = ResultTables.SpectralAnalysisNodesDeformations(
        loading_type=CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no=4,
        envelope_type=SpectralAnalysisEnvelopeType.SPECTRAL_ANALYSIS_DIRECTION_X)
    print(nodeDeformationsX)

    # membersDeformationsX = ResultTables.SpectralAnalysisMembersLocalDeformations(
    #     loading_type=CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
    #     loading_no=4,
    #     envelope_type=SpectralAnalysisEnvelopeType.SPECTRAL_ANALYSIS_DIRECTION_X)
    # print(membersDeformationsX)

    nodeDeformationsY = ResultTables.SpectralAnalysisSurfacesLocalDeformations(
        loading_type=CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no=4,
        envelope_type=SpectralAnalysisEnvelopeType.SPECTRAL_ANALYSIS_DIRECTION_X)
    print(nodeDeformationsY)