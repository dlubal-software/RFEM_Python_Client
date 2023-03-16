#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
rfemDir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(rfemDir)
from RFEM.initModel import Model
import xml.etree.ElementTree as ET
from RFEM.ImportExport.exports import ExportTo

# Define name of the model from which the data should be exported
model_name = 'test.rf6'

# Export active model to XML
model = Model(False, model_name)
ExportTo(os.path.dirname(__file__)+"/export.xml", model)

# Parse exported XML
tree = ET.parse(os.path.dirname(__file__)+"/export.xml")
root = tree.getroot()

# Constant imports
cons_imports = ['import sys\n',
                  'sys.path.append("'+rfemDir.replace('\\', '/')+'")\n',
                  'from RFEM.enums import *\n',
                  'from RFEM.initModel import *\n',
                  'from RFEM.dataTypes import inf\n',
                  '\n']

# Import variables
imports = {'formula': 'from RFEM.formula import Formula',
           'line': 'from RFEM.BasicObjects.line import Line',
           'line_set': 'from RFEM.BasicObjects.lineSet import LineSet',
           'material': 'from RFEM.BasicObjects.material import Material',
           'member': 'from RFEM.BasicObjects.member import Member',
           'member_set': 'from RFEM.BasicObjects.memberSet import MemberSet',
           'node': 'from RFEM.BasicObjects.node import Node',
           'opening': 'from RFEM.BasicObjects.opening import Opening',
           'section': 'from RFEM.BasicObjects.section import Section',
           'solid': 'from RFEM.BasicObjects.solid import Solid',
           'solid_set': 'from RFEM.BasicObjects.solidSet import SolidSet',
           'surface': 'from RFEM.BasicObjects.surface import Surface',
           'surface_set': 'from RFEM.BasicObjects.surfaceSet import SurfaceSet',
           'thickness': 'from RFEM.BasicObjects.thickness import Thickness',
           'concrete_serviceability_configuration': 'from RFEM.ConcreteDesign.ConcreteServiceabilityConfigurations import ConcreteServiceabilityConfiguration',
           'concrete_ultimate_configuration': 'from RFEM.ConcreteDesign.ConcreteUltimateConfigurations import ConcreteUltimateConfiguration',
           'response_spectrum': 'from RFEM.DynamicLoads.responseSpectrum import ResponseSpectrum',
           'imperfection_case': 'from RFEM.Imperfections.imperfectionCase import ImperfectionCase',
           'member_imperfection': 'from RFEM.Imperfections.memberImperfection import MemberImperfection',
           'member_set_imperfection': 'from RFEM.Imperfections.membersetImperfection import MemberSetImperfection',
           'combination_wizard': 'from RFEM.LoadCasesAndCombinations.combinationWizard import CombinationWizard',
           'design_situation': 'from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation',
           'load_case': 'from RFEM.LoadCasesAndCombinations.loadCase import LoadCase',
           'load_cases_and_combinations': 'from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations',
           'load_combination': 'from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination',
           'modal_analysis_settings': 'from RFEM.LoadCasesAndCombinations.modalAnalysisSettings import ModalAnalysisSettings',
           'result_combination': 'from RFEM.LoadCasesAndCombinations.resultCombination import ResultCombination',
           'spectral_analysis_settings': 'from RFEM.LoadCasesAndCombinations.spectralAnalysisSettings import SpectralAnalysisSettings',
           'stability_analysis_settings': 'from RFEM.LoadCasesAndCombinations.stabilityAnalysisSettings import StabilityAnalysisSettings ',
           'static_analysis_settings': 'from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings',
           'wind_simulation_analysis_settings': 'from RFEM.LoadCasesAndCombinations.windSimulationAnalysisSetting import WindSimulationAnalysisSettings',
           'free_load': 'from RFEM.Loads.freeLoad import FreeLoad',
           'imposed_line_deformation': 'from RFEM.Loads.imposedLineDeformation import ImposedLineDeformation',
           'imposed_nodal_deformation': 'from RFEM.Loads.imposedNodalDeformation import ImposedNodalDeformation',
           'line_load': 'from RFEM.Loads.lineLoad import LineLoad',
           'line_set_load': 'from RFEM.Loads.linesetLoad import LineSetLoad',
           'member_load': 'from RFEM.Loads.memberLoad import MemberLoad',
           'member_set_load': 'from RFEM.Loads.membersetload import MemberSetLoad',
           'nodal_load': 'from RFEM.Loads.nodalLoad import NodalLoad',
           'opening_load': 'from RFEM.Loads.openingLoad import OpeningLoad',
           'solid_load': 'from RFEM.Loads.solidLoad import SolidLoad',
           'solid_set_load': 'from RFEM.Loads.solidSetLoad import SolidSetLoad',
           'surface_load': 'from RFEM.Loads.surfaceLoad import SurfaceLoad',
           'surface_set_load': 'from RFEM.Loads.surfacesetload import SurfaceSetLoad',
           'instersection': 'from RFEM.SpecialObjects.intersection import Instersection',
           'line_release': 'from RFEM.SpecialObjects.lineRelease import LineRelease',
           'line_release_type': 'from RFEM.SpecialObjects.lineReleaseType import LineReleaseType',
           'result_section': 'from RFEM.SpecialObjects.resultSection import ResultSection',
           'rigid_link': 'from RFEM.SpecialObjects.rigidLink import RigidLink',
           'structure_modification': 'from RFEM.SpecialObjects.structureModification import StructureModification',
           'surface_contact': 'from RFEM.SpecialObjects.surfaceContact import SurfaceContact',
           'surface_results_adjustment': 'from RFEM.SpecialObjects.surfaceResultAdjustment import SurfaceResultsAdjustment',
           'steel_design_serviceability_configurations': 'from RFEM.SteelDesign.steelServiceabilityConfiguration import SteelDesignServiceabilityConfigurations',
           'steel_design_ultimate_configurations': 'from RFEM.SteelDesign.steelUltimateConfigurations import SteelDesignUltimateConfigurations',
           'timber_design_service_limit_state_configurations': 'from RFEM.TimberDesign.timberServiceLimitStateConfigurations import TimberDesignServiceLimitStateConfigurations',
           'timber_design_ultimate_configurations': 'from RFEM.TimberDesign.timberUltimateConfigurations import TimberDesignUltimateConfigurations',
           'aluminum_effective_lengths': 'from RFEM.TypesForAluminumDesign.aluminumEffectiveLengths import AluminumEffectiveLengths',
           'aluminum_member_local_section_reduction': 'from RFEM.TypesForAluminumDesign.aluminumMemberLocalSectionReduction import AluminumMemberLocalSectionReduction',
           'aluminum_member_rotational_restraint': 'from RFEM.TypesForAluminumDesign.aluminumMemberRotationalRestraints import AluminumMemberRotationalRestraint',
           'aluminum_member_shear_panel': 'from RFEM.TypesForAluminumDesign.aluminumMemberShearPanel import AluminumMemberShearPanel',
           'aluminum_member_transverse_weld': 'from RFEM.TypesForAluminumDesign.aluminumMemberTransverseWelds import AluminumMemberTransverseWeld',
           'concrete_durability': 'from RFEM.TypesforConcreteDesign.ConcreteDurability import ConcreteDurability',
           'concrete_effective_length': 'from RFEM.TypesforConcreteDesign.ConcreteEffectiveLength import ConcreteEffectiveLength',
           'concrete_reinforcement_direction': 'from RFEM.TypesforConcreteDesign.ConcreteReinforcementDirections import ConcreteReinforcementDirection',
           'concrete_surface_reinforcements': 'from RFEM.TypesforConcreteDesign.ConcreteSurfaceReinforcements import ConcreteSurfaceReinforcements',
           'line_hinge': 'from RFEM.TypesForLines.lineHinge import LineHinge',
           'line_mesh_refinements': 'from RFEM.TypesForLines.lineMeshRefinements import LineMeshRefinements',
           'line_support': 'from RFEM.TypesForLines.lineSupport import LineSupport',
           'line_welded_joint': 'from RFEM.TypesForLines.lineWeldedJoint import LineWeldedJoint',
           'member_definable_stiffness': 'from RFEM.TypesForMembers.memberDefinableStiffness import MemberDefinableStiffness',
           'member_eccentricity': 'from RFEM.TypesForMembers.memberEccentricity import MemberEccentricity',
           'member_hinge': 'from RFEM.TypesForMembers.memberHinge import MemberHinge',
           'member_nonlinearity': 'from RFEM.TypesForMembers.memberNonlinearity import MemberNonlinearity',
           'member_result_intermediate_point': 'from RFEM.TypesForMembers.memberResultIntermediatePoints import MemberResultIntermediatePoint',
           'member_stiffness_modification': 'from RFEM.TypesForMembers.memberStiffnessModification import MemberStiffnessModification',
           'member_support': 'from RFEM.TypesForMembers.memberSupport import MemberSupport',
           'member_transverse_stiffeners': 'from RFEM.TypesForMembers.memberTransverseStiffeners import MemberTransverseStiffeners',
           'nodal_mesh_refinement': 'from RFEM.TypesForNodes.nodalMeshRefinement import NodalMeshRefinement',
           'nodal_support': 'from RFEM.TypesForNodes.nodalSupport import NodalSupport',
           'solid_contact': 'from RFEM.TypesForSolids.solidContact import SolidContact',
           'solid_gas': 'from RFEM.TypesForSolids.solidGas import SolidGas',
           'solid_mesh_refinement': 'from RFEM.TypesForSolids.solidMeshRefinement import SolidMeshRefinement',
           'surface_contact_type': 'from RFEM.TypesForSpecialObjects.surfaceContactType import SurfaceContactType',
           'steel_boundary_conditions': 'from RFEM.TypesForSteelDesign.steelBoundaryConditions import SteelBoundaryConditions',
           'steel_effective_lengths': 'from RFEM.TypesForSteelDesign.steelEffectiveLengths import SteelEffectiveLengths',
           'steel_member_local_section_reduction': 'from RFEM.TypesForSteelDesign.SteelMemberLocalSectionReduction import SteelMemberLocalSectionReduction',
           'steel_member_rotational_restraint': 'from RFEM.TypesForSteelDesign.steelMemberRotationalRestraints import SteelMemberRotationalRestraint',
           'steel_member_shear_panel': 'from RFEM.TypesForSteelDesign.steelMemberShearPanel import SteelMemberShearPanel',
           'surface_eccentricity': 'from RFEM.TypesForSurfaces.surfaceEccentricity import SurfaceEccentricity',
           'surface_mesh_refinement': 'from RFEM.TypesForSurfaces.surfaceMeshRefinements import SurfaceMeshRefinement',
           'surface_stiffness_modification': 'from RFEM.TypesForSurfaces.surfaceStiffnessModification import SurfaceStiffnessModification',
           'surface_support': 'from RFEM.TypesForSurfaces.surfaceSupport import SurfaceSupport',
           'timber_effective_lengths': 'from RFEM.TypesForTimberDesign.timberEffectiveLengths import TimberEffectiveLengths',
           'timber_member_local_section_reduction': 'from RFEM.TypesForTimberDesign.timberMemberLocalSectionReduction import TimberMemberLocalSectionReduction',
           'timber_member_rotational_restraint': 'from RFEM.TypesForTimberDesign.timberMemberRotationalRestraint import TimberMemberRotationalRestraint',
           'timber_member_shear_panel': 'from RFEM.TypesForTimberDesign.timberMemberShearPanel import TimberMemberShearPanel',
           'timber_service_class': 'from RFEM.TypesForTimberDesign.timberServiceClass import TimberServiceClass'}

def convertSnakeCaseToCamelCase(str):
    '''
    Convert snake_case to CamelCase
    '''
    # split underscore using split
    temp = str.split('_')
    # joining result
    res = temp[0].title() + ''.join(ele.title() for ele in temp[1:])
    return res

importObjects = [''] # defines what to import with 'imports'
missingInClient = [] #objects that can't be defined because they are not in Client, yet.
lines = cons_imports # individual lines written in file

# Process XML data
for child in range(len(root)):
    if root[child].tag == 'model_configuration':
        pass
    elif root[child].tag == 'model':
        for id_1 in range(len(root[child])):
            for id_2 in range(len(root[child][id_1])):
                if root[child][id_1][id_2].tag in imports.keys():
                    importObjects.append(imports[root[child][id_1][id_2].tag]+'\n')

                    for id_3 in range(len(root[child][id_1][id_2])):
                        tags = {}
                        for id_4 in range(len(root[child][id_1][id_2][id_3])):
                            if root[child][id_1][id_2][id_3][id_4].text == '\n                        ':
                                items = {}
                                if len(root[child][id_1][id_2][id_3][id_4][0]):
                                    for id_5 in range(len(root[child][id_1][id_2][id_3][id_4][0])):
                                        items[root[child][id_1][id_2][id_3][id_4][0][id_5].tag] = root[child][id_1][id_2][id_3][id_4][0][id_5].text
                                    tags[root[child][id_1][id_2][id_3][id_4].tag] = items
                                # skipped: empty dicts like 'coordinates:{}'
                                #else:
                                #    for id_5 in range(len(root[child][id_1][id_2][id_3][id_4])):
                                #        items[root[child][id_1][id_2][id_3][id_4][id_5].tag] = root[child][id_1][id_2][id_3][id_4][id_5].text

                            else:
                                tags[root[child][id_1][id_2][id_3][id_4].tag] = root[child][id_1][id_2][id_3][id_4].text

                        params = ''
                        for key in tags:
                            params = params+'"'+key+'"'+':"'+str(tags[key])+'", '
                        params = params[:-2]
                        lines.append(convertSnakeCaseToCamelCase(root[child][id_1][id_2].tag)+'(params={'+params+'})'+'\n')

                else:
                    if root[child][id_1][id_2].tag == 'item':
                        missingInClient.append(convertSnakeCaseToCamelCase(root[child][id_1][id_2].tag)+', '+str(root[child][id_1].tag)+'\n')
                    else:
                        missingInClient.append(convertSnakeCaseToCamelCase(root[child][id_1][id_2].tag)+'\n')

    elif root[child].tag == 'addons':
        pass
    else:
        ValueError('Branch "'+root[child].tag+'" was not recognized. Only model informatin is currently processed.')

# Add imports to 'lines'
for i,v in enumerate(importObjects):
    lines.insert(i+6, v)

# Add mandatory steps
lines.insert(6+len(importObjects), '\n')
lines.insert(6+len(importObjects)+1, 'Model()\n')
lines.insert(6+len(importObjects)+2, 'Model.clientModel.service.begin_modification()\n')
lines.insert(6+len(importObjects)+3, '\n')

# Add finish modification and list all excluded objects
lines.append('\n')
lines.append('Model.clientModel.service.finish_modification()\n')
lines.append('\n')
lines.append('# Following are the objects that can NOT be set because they are not implemented in Client:\n')
for l in missingInClient:
    lines.append('#    '+l)

# Create file and write data
f = open(os.path.dirname(__file__)+"/generatedScript.py", "w", encoding="utf-8")
f.writelines(lines)
f.close()
