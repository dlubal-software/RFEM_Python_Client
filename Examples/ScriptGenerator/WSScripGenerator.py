#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

rfemDir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(rfemDir)
from RFEM.enums import ObjectTypes
from RFEM.initModel import Model
from RFEM.Tools.GetObjectNumbersByType import GetObjectNumbersByType

# Define name of the model from which the data should be exported
model_name = 'test.rf6'

# Export active model to XML
model = Model(True, model_name)

# Constant imports
cons_imports = ['import sys\n',
                'sys.path.append("'+rfemDir.replace('\\', '/')+'")\n',
                'from RFEM.enums import *\n',
                'from RFEM.initModel import *\n',
                'from RFEM.dataTypes import inf\n',
                '\n']

i = 0 # object number

# Steps to retrieve data from RFEM:
# 1) get numbers of given object type via GetObjectNumbersByType(),
# 2) get data from individual objects,
# 3) set import of the type,
# 4) set individual objects.
# For each of these steps individual record is made (4 total).

# Vector of all function
func_vec = [[ObjectTypes.E_OBJECT_TYPE_MATERIAL, lambda i: model.clientModel.service.get_material(i), 'from RFEM.BasicObjects.material import Material\n', 'Material'],
            [ObjectTypes.E_OBJECT_TYPE_SECTION, lambda i: model.clientModel.service.get_section(i), 'from RFEM.BasicObjects.section import Section\n', 'Section'],
            [ObjectTypes.E_OBJECT_TYPE_THICKNESS, lambda i: model.clientModel.service.get_thickness(i), 'from RFEM.BasicObjects.thickness import Thickness\n', 'Thickness'],
            [ObjectTypes.E_OBJECT_TYPE_NODE, lambda i: model.clientModel.service.get_node(i), 'from RFEM.BasicObjects.node import Node\n', 'Node'],
            [ObjectTypes.E_OBJECT_TYPE_LINE, lambda i: model.clientModel.service.get_line(i), 'from RFEM.BasicObjects.line import Line\n', 'Line'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER, lambda i: model.clientModel.service.get_member(i), 'from RFEM.BasicObjects.member import Member\n', 'Member'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE, lambda i: model.clientModel.service.get_surface(i), 'from RFEM.BasicObjects.surface import Surface\n', 'Surface'],
            [ObjectTypes.E_OBJECT_TYPE_OPENING, lambda i: model.clientModel.service.get_opening(i), 'from RFEM.BasicObjects.opening import Opening\n', 'Opening'],
            [ObjectTypes.E_OBJECT_TYPE_SOLID, lambda i: model.clientModel.service.get_solid(i), 'from RFEM.BasicObjects.solid import Solid\n', 'Solid'],
            [ObjectTypes.E_OBJECT_TYPE_LINE_SET, lambda i: model.clientModel.service.get_line_set(i), 'from RFEM.BasicObjects.lineSet import LineSet\n', 'LineSet'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_SET, lambda i: model.clientModel.service.get_member_set(i), 'from RFEM.BasicObjects.memberSet import MemberSet\n', 'MemberSet'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_SET, lambda i: model.clientModel.service.get_surface_set(i), 'from RFEM.BasicObjects.surfaceSet import SurfaceSet\n', 'SurfaceSet'],
            [ObjectTypes.E_OBJECT_TYPE_SOLID_SET, lambda i: model.clientModel.service.get_solid_set(i), 'from RFEM.BasicObjects.solidSet import SolidSet\n', 'SolidSet'],

            [ObjectTypes.E_OBJECT_TYPE_INTERSECTION, lambda i: model.clientModel.service.get_instersection(i), 'from RFEM.SpecialObjects.intersection import Instersection\n', 'Instersection'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_RESULTS_ADJUSTMENT, lambda i: model.clientModel.service.get_surface_results_adjustment(i), 'from RFEM.SpecialObjects.surfaceResultAdjustment import SurfaceResultsAdjustment\n', 'SurfaceResultsAdjustment'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACES_CONTACT, lambda i: model.clientModel.service.get_surface_contact(i), 'from RFEM.SpecialObjects.surfaceContact import SurfaceContact\n', 'SurfaceContact'],
            [ObjectTypes.E_OBJECT_TYPE_RIGID_LINK, lambda i: model.clientModel.service.get_rigid_link(i), 'from RFEM.SpecialObjects.rigidLink import RigidLink\n', 'RigidLink'],
            [ObjectTypes.E_OBJECT_TYPE_RESULT_SECTION, lambda i: model.clientModel.service.get_result_section(i), 'from RFEM.SpecialObjects.resultSection import ResultSection\n', 'ResultSection'],
            [ObjectTypes.E_OBJECT_TYPE_STRUCTURE_MODIFICATION, lambda i: model.clientModel.service.get_structure_modification(i), 'from RFEM.SpecialObjects.structureModification import StructureModification\n', 'StructureModification'],
            # nodal_release
            [ObjectTypes.E_OBJECT_TYPE_LINE_RELEASE, lambda i: model.clientModel.service.get_line_release(i), 'from RFEM.SpecialObjects.lineRelease import LineRelease\n', 'LineRelease'],
            # surface_release
            # blocks
            # boreholes
            # soil_massif

            [ObjectTypes.E_OBJECT_TYPE_NODAL_SUPPORT, lambda i: model.clientModel.service.get_nodal_support(i), 'from RFEM.TypesForNodes.nodalSupport import NodalSupport\n', 'NodalSupport'],
            [ObjectTypes.E_OBJECT_TYPE_NODAL_MESH_REFINEMENT, lambda i: model.clientModel.service.get_nodal_mesh_refinement(i), 'from RFEM.TypesForNodes.nodalMeshRefinement import NodalMeshRefinement\n', 'NodalMeshRefinement'],

            [ObjectTypes.E_OBJECT_TYPE_LINE_SUPPORT, lambda i: model.clientModel.service.get_line_support(i), 'from RFEM.TypesForLines.lineSupport import LineSupport\n', 'LineSupport'],
            [ObjectTypes.E_OBJECT_TYPE_LINE_MESH_REFINEMENT, lambda i: model.clientModel.service.get_line_mesh_refinements(i), 'from RFEM.TypesForLines.lineMeshRefinements import LineMeshRefinements\n', 'LineMeshRefinements'],
            [ObjectTypes.E_OBJECT_TYPE_LINE_HINGE, lambda i: model.clientModel.service.get_line_hinge(i), 'from RFEM.TypesForLines.lineHinge import LineHinge\n', 'LineHinge'],
            [ObjectTypes.E_OBJECT_TYPE_LINE_WELDED_JOINT, lambda i: model.clientModel.service.get_line_welded_joint(i), 'from RFEM.TypesForLines.lineWeldedJoint import LineWeldedJoint\n', 'LineWeldedJoint'],

            [ObjectTypes.E_OBJECT_TYPE_MEMBER_HINGE, lambda i: model.clientModel.service.get_member_hinge(i), 'from RFEM.TypesForMembers.memberHinge import MemberHinge\n', 'MemberHinge'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_ECCENTRICITY, lambda i: model.clientModel.service.get_member_eccentricity(i), 'from RFEM.TypesForMembers.memberEccentricity import MemberEccentricity\n', 'MemberEccentricity'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_SUPPORT, lambda i: model.clientModel.service.get_member_support(i), 'from RFEM.TypesForMembers.memberSupport import MemberSupport\n', 'MemberSupport'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_TRANSVERSE_STIFFENER, lambda i: model.clientModel.service.get_member_transverse_stiffeners(i), 'from RFEM.TypesForMembers.memberTransverseStiffeners import MemberTransverseStiffeners\n', 'MemberTransverseStiffeners'],
            # member_opening
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_STIFFNESS_MODIFICATION, lambda i: model.clientModel.service.get_member_stiffness_modification(i), 'from RFEM.TypesForMembers.memberStiffnessModification import MemberStiffnessModification\n', 'MemberStiffnessModification'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_NONLINEARITY, lambda i: model.clientModel.service.get_member_nonlinearity(i), 'from RFEM.TypesForMembers.memberNonlinearity import MemberNonlinearity\n', 'MemberNonlinearity'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_DEFINABLE_STIFFNESS, lambda i: model.clientModel.service.get_member_definable_stiffness(i), 'from RFEM.TypesForMembers.memberDefinableStiffness import MemberDefinableStiffness\n', 'MemberDefinableStiffness'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_RESULT_INTERMEDIATE_POINT, lambda i: model.clientModel.service.get_member_result_intermediate_point(i), 'from RFEM.TypesForMembers.memberResultIntermediatePoints import MemberResultIntermediatePoint\n', 'MemberResultIntermediatePoint'],
            # design_support
            # member_shear_panel
            # member_rotational_restraint

            [ObjectTypes.E_OBJECT_TYPE_SURFACE_SUPPORT, lambda i: model.clientModel.service.get_surface_support(i), 'from RFEM.TypesForSurfaces.surfaceSupport import SurfaceSupport\n', 'SurfaceSupport'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_ECCENTRICITY, lambda i: model.clientModel.service.get_surface_eccentricity(i), 'from RFEM.TypesForSurfaces.surfaceEccentricity import SurfaceEccentricity\n', 'SurfaceEccentricity'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_STIFFNESS_MODIFICATION, lambda i: model.clientModel.service.get_surface_stiffness_modification(i), 'from RFEM.TypesForSurfaces.surfaceStiffnessModification import SurfaceStiffnessModification\n', 'SurfaceStiffnessModification'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_MESH_REFINEMENT, lambda i: model.clientModel.service.get_surface_mesh_refinement(i), 'from RFEM.TypesForSurfaces.surfaceMeshRefinements import SurfaceMeshRefinement\n', 'SurfaceMeshRefinement'],

            [ObjectTypes.E_OBJECT_TYPE_SOLID_MESH_REFINEMENT, lambda i: model.clientModel.service.get_solid_mesh_refinement(i), 'from RFEM.TypesForSolids.solidMeshRefinement import SolidMeshRefinement\n', 'SolidMeshRefinement'],
            [ObjectTypes.E_OBJECT_TYPE_SOLID_GAS, lambda i: model.clientModel.service.get_solid_gas(i), 'from RFEM.TypesForSolids.solidGas import SolidGas\n', 'SolidGas'],
            [ObjectTypes.E_OBJECT_TYPE_SOLID_CONTACTS, lambda i: model.clientModel.service.get_solid_contact(i), 'from RFEM.TypesForSolids.solidContact import SolidContact\n', 'SolidContact'],

            [ObjectTypes.E_OBJECT_TYPE_SURFACES_CONTACT_TYPE, lambda i: model.clientModel.service.get_surface_contact_type(i), 'from RFEM.TypesForSpecialObjects.surfaceContactType import SurfaceContactType\n', 'SurfaceContactType'],

            # nodal_release_type
            [ObjectTypes.E_OBJECT_TYPE_LINE_RELEASE_TYPE, lambda i: model.clientModel.service.get_line_release_type(i), 'from RFEM.SpecialObjects.lineReleaseType import LineReleaseType\n', 'LineReleaseType'],
            # surface_release_ty
            [ObjectTypes.E_OBJECT_TYPE_CONCRETE_EFFECTIVE_LENGTHS, lambda i: model.clientModel.service.get_concrete_effective_lengths(i), 'from RFEM.TypesforConcreteDesign.ConcreteEffectiveLength import ConcreteEffectiveLength\n', 'ConcreteEffectiveLength'],
            [ObjectTypes.E_OBJECT_TYPE_CONCRETE_DURABILITY, lambda i: model.clientModel.service.get_concrete_durability(i), 'from RFEM.TypesforConcreteDesign.ConcreteDurability import ConcreteDurability\n', 'ConcreteDurability'],
            [ObjectTypes.E_OBJECT_TYPE_REINFORCEMENT_DIRECTION, lambda i: model.clientModel.service.get_reinforcement_direction(i), 'from RFEM.TypesforConcreteDesign.ConcreteReinforcementDirections import ConcreteReinforcementDirection\n', 'ConcreteReinforcementDirection'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_REINFORCEMENT, lambda i: model.clientModel.service.get_surface_reinforcement(i), 'from RFEM.TypesforConcreteDesign.ConcreteSurfaceReinforcements import ConcreteSurfaceReinforcements\n', 'ConcreteSurfaceReinforcements'],
            [ObjectTypes.E_OBJECT_TYPE_CONCRETE_DESIGN_SLS_CONFIGURATION, lambda i: model.clientModel.service.get_concrete_design_sls_configuration(i), 'from RFEM.ConcreteDesign.ConcreteServiceabilityConfigurations import ConcreteServiceabilityConfiguration\n', 'ConcreteServiceabilityConfiguration'],
            [ObjectTypes.E_OBJECT_TYPE_CONCRETE_DESIGN_ULS_CONFIGURATION, lambda i: model.clientModel.service.get_concrete_design_uls_configuration(i), 'from RFEM.ConcreteDesign.ConcreteUltimateConfigurations import ConcreteUltimateConfiguration\n', 'ConcreteUltimateConfiguration'],
            [ObjectTypes.E_OBJECT_TYPE_STEEL_EFFECTIVE_LENGTHS, lambda i: model.clientModel.service.get_steel_effective_lengths(i), 'from RFEM.TypesForSteelDesign.steelEffectiveLengths import SteelEffectiveLengths\n', 'SteelEffectiveLengths'],
            [ObjectTypes.E_OBJECT_TYPE_STEEL_BOUNDARY_CONDITIONS, lambda i: model.clientModel.service.get_steel_boundary_conditions(i), 'from RFEM.TypesForSteelDesign.steelBoundaryConditions import SteelBoundaryConditions\n', 'SteelBoundaryConditions'],
            [ObjectTypes.E_OBJECT_TYPE_STEEL_MEMBER_LOCAL_SECTION_REDUCTION, lambda i: model.clientModel.service.get_steel_member_local_section_reduction(i), 'from RFEM.TypesForSteelDesign.SteelMemberLocalSectionReduction import SteelMemberLocalSectionReduction\n', 'SteelMemberLocalSectionReduction'],
            ## E_OBJECT_TYPE_MEMBER_ROTATIONAL_RESTRAINT
            ## [ObjectTypes.E_OBJECT_TYPE_STEEL_MEMBER_ROTATIONAL_RESTRAINT, lambda i: model.clientModel.service.get_(i), 'from RFEM.TypesForSteelDesign.steelMemberRotationalRestraints import SteelMemberRotationalRestraint\n', 'SteelMemberRotationalRestraint'],
            #[ObjectTypes.E_OBJECT_TYPE_STEEL_MEMBER_SHEAR_PANEL, lambda i: model.clientModel.service.get_steel_member_shear_panel(i), 'from RFEM.TypesForSteelDesign.steelMemberShearPanel import SteelMemberShearPanel\n', 'SteelMemberShearPanel'],
            [ObjectTypes.E_OBJECT_TYPE_STEEL_DESIGN_SLS_CONFIGURATION, lambda i: model.clientModel.service.get_steel_design_sls_configuration(i), 'from RFEM.SteelDesign.steelServiceabilityConfiguration import SteelDesignServiceabilityConfigurations\n', 'SteelDesignServiceabilityConfigurations'],
            [ObjectTypes.E_OBJECT_TYPE_STEEL_DESIGN_ULS_CONFIGURATION, lambda i: model.clientModel.service.get_steel_design_uls_configuration(i), 'from RFEM.SteelDesign.steelUltimateConfigurations import SteelDesignUltimateConfigurations\n', 'SteelDesignUltimateConfigurations'],
            [ObjectTypes.E_OBJECT_TYPE_TIMBER_EFFECTIVE_LENGTHS, lambda i: model.clientModel.service.get_timber_effective_lengths(i), 'from RFEM.TypesForTimberDesign.timberEffectiveLengths import TimberEffectiveLengths\n', 'TimberEffectiveLengths'],
            [ObjectTypes.E_OBJECT_TYPE_TIMBER_SERVICE_CLASS, lambda i: model.clientModel.service.get_timber_service_class(i), 'from RFEM.TypesForTimberDesign.timberServiceClass import TimberServiceClass\n', 'TimberServiceClass'],
            [ObjectTypes.E_OBJECT_TYPE_ALUMINUM_MEMBER_LOCAL_SECTION_REDUCTION, lambda i: model.clientModel.service.get_timber_member_local_section_reduction(i), 'from RFEM.TypesForTimberDesign.timberMemberLocalSectionReduction import TimberMemberLocalSectionReduction\n', 'TimberMemberLocalSectionReduction'],
            #[ObjectTypes.E_OBJECT_TYPE_TIMBER_MEMBER_ROTATIONAL_RESTRAINT, lambda i: model.clientModel.service.get_timber_member_rotational_restraint(i), 'from RFEM.TypesForTimberDesign.timberMemberRotationalRestraint import TimberMemberRotationalRestraint\n', 'TimberMemberRotationalRestraint'],
            #[ObjectTypes.E_OBJECT_TYPE_TIMBER_MEMBER_SHEAR_PANEL, lambda i: model.clientModel.service.get_timber_member_shear_panel(i), 'from RFEM.TypesForTimberDesign.timberMemberShearPanel import TimberMemberShearPanel\n', 'TimberMemberShearPanel'],
            [ObjectTypes.E_OBJECT_TYPE_TIMBER_DESIGN_SLS_CONFIGURATION, lambda i: model.clientModel.service.get_timber_design_sls_configuration(i), 'from RFEM.TimberDesign.timberServiceLimitStateConfigurations import TimberDesignServiceLimitStateConfigurations\n', 'TimberDesignServiceLimitStateConfigurations'],
            [ObjectTypes.E_OBJECT_TYPE_TIMBER_DESIGN_ULS_CONFIGURATION, lambda i: model.clientModel.service.get_timber_design_uls_configuration(i), 'from RFEM.TimberDesign.timberUltimateConfigurations import TimberDesignUltimateConfigurations\n', 'TimberDesignUltimateConfigurations'],
            [ObjectTypes.E_OBJECT_TYPE_ALUMINUM_EFFECTIVE_LENGTHS, lambda i: model.clientModel.service.get_aluminum_effective_lengths(i), 'from RFEM.TypesForAluminumDesign.aluminumEffectiveLengths import AluminumEffectiveLengths\n', 'AluminumEffectiveLengths'],
            [ObjectTypes.E_OBJECT_TYPE_ALUMINUM_MEMBER_LOCAL_SECTION_REDUCTION, lambda i: model.clientModel.service.get_aluminum_member_local_section_reduction(i), 'from RFEM.TypesForAluminumDesign.aluminumMemberLocalSectionReduction import AluminumMemberLocalSectionReduction\n', 'AluminumMemberLocalSectionReduction'],
            #[ObjectTypes.E_OBJECT_TYPE_ALUMINUM_MEMBER_ROTATIONAL_RESTRAINT, lambda i: model.clientModel.service.get_aluminum_member_rotational_restraint(i), 'from RFEM.TypesForAluminumDesign.aluminumMemberRotationalRestraints import AluminumMemberRotationalRestraint\n', 'AluminumMemberRotationalRestraint'],
            #[ObjectTypes.E_OBJECT_TYPE_ALUMINUM_MEMBER_SHEAR_PANEL, lambda i: model.clientModel.service.get_aluminum_member_shear_panel(i), 'from RFEM.TypesForAluminumDesign.aluminumMemberShearPanel import AluminumMemberShearPanel\n', 'AluminumMemberShearPanel'],
            [ObjectTypes.E_OBJECT_TYPE_ALUMINUM_MEMBER_TRANSVERSE_WELD, lambda i: model.clientModel.service.get_aluminum_member_transverse_weld(i), 'from RFEM.TypesForAluminumDesign.aluminumMemberTransverseWelds import AluminumMemberTransverseWeld\n', 'AluminumMemberTransverseWeld'],
            # steel_joints
            # craneways
            # cran
            [ObjectTypes.E_OBJECT_TYPE_IMPERFECTION_CASE, lambda i: model.clientModel.service.get_imperfection_case(i), 'from RFEM.Imperfections.imperfectionCase import ImperfectionCase\n', 'ImperfectionCase'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_IMPERFECTION, lambda i: model.clientModel.service.get_member_imperfection(i), 'from RFEM.Imperfections.memberImperfection import MemberImperfection\n', 'MemberImperfection'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_SET_IMPERFECTION, lambda i: model.clientModel.service.get_member_set_imperfection(i), 'from RFEM.Imperfections.membersetImperfection import MemberSetImperfection\n', 'MemberSetImperfection'],
            # construction_stag
            [ObjectTypes.E_OBJECT_TYPE_LOAD_CASE, lambda i: model.clientModel.service.get_load_case(i), 'from RFEM.LoadCasesAndCombinations.loadCase import LoadCase\n', 'LoadCase'],
            [ObjectTypes.E_OBJECT_TYPE_DESIGN_SITUATION, lambda i: model.clientModel.service.get_design_situation(i), 'from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation\n', 'DesignSituation'],
            [ObjectTypes.E_OBJECT_TYPE_LOAD_COMBINATION, lambda i: model.clientModel.service.get_load_combination(i), 'from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination\n', 'LoadCombination'],
            #[ObjectTypes, lambda i: model.clientModel.service.get_(i), 'from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations',]
            [ObjectTypes.E_OBJECT_TYPE_RESULT_COMBINATION, lambda i: model.clientModel.service.get_result_combination(i), 'from RFEM.LoadCasesAndCombinations.resultCombination import ResultCombination\n', 'ResultCombination'],
            [ObjectTypes.E_OBJECT_TYPE_STATIC_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_static_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings\n', 'StaticAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_STABILITY_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_stability_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.stabilityAnalysisSettings import StabilityAnalysisSettings\n', 'StabilityAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_MODAL_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_modal_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.modalAnalysisSettings import ModalAnalysisSettings\n', 'ModalAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_SPECTRAL_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_spectral_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.spectralAnalysisSettings import SpectralAnalysisSettings\n', 'SpectralAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_WIND_SIMULATION_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_wind_simulation_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.windSimulationAnalysisSetting import WindSimulationAnalysisSettings\n', 'WindSimulationAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_COMBINATION_WIZARD, lambda i: model.clientModel.service.set_combination_wizard(i), 'from RFEM.LoadCasesAndCombinations.combinationWizard import CombinationWizard\n', 'CombinationWizard'],
            # member_loads_from_area_loads
            # member_loads_from_free_line_load
            # snow_loads
            # wind_loads
            # wind_profiles
            # wind_simulatio
            [ObjectTypes.E_OBJECT_TYPE_NODAL_LOAD, lambda i: model.clientModel.service.get_nodal_load(i), 'from RFEM.Loads.nodalLoad import NodalLoad\n', 'NodalLoad'],
            [ObjectTypes.E_OBJECT_TYPE_LINE_LOAD, lambda i: model.clientModel.service.get_line_load(i), 'from RFEM.Loads.lineLoad import LineLoad\n', 'LineLoad'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_LOAD, lambda i: model.clientModel.service.get_member_load(i), 'from RFEM.Loads.memberLoad import MemberLoad\n', 'MemberLoad'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_LOAD, lambda i: model.clientModel.service.get_surface_load(i), 'from RFEM.Loads.surfaceLoad import SurfaceLoad\n', 'SurfaceLoad'],
            [ObjectTypes.E_OBJECT_TYPE_OPENING_LOAD, lambda i: model.clientModel.service.get_opening_load(i), 'from RFEM.Loads.openingLoad import OpeningLoad\n', 'OpeningLoad'],
            [ObjectTypes.E_OBJECT_TYPE_SOLID_LOAD, lambda i: model.clientModel.service.get_solid_load(i), 'from RFEM.Loads.solidLoad import SolidLoad\n', 'SolidLoad'],
            [ObjectTypes.E_OBJECT_TYPE_LINE_SET_LOAD, lambda i: model.clientModel.service.get_line_set_load(i), 'from RFEM.Loads.linesetLoad import LineSetLoad\n', 'LineSetLoad'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_SET_LOAD, lambda i: model.clientModel.service.get_member_set_load(i), 'from RFEM.Loads.membersetload import MemberSetLoad\n', 'MemberSetLoad'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_SET_LOAD, lambda i: model.clientModel.service.get_surface_set_load(i), 'from RFEM.Loads.surfacesetload import SurfaceSetLoad\n', 'SurfaceSetLoad'],
            [ObjectTypes.E_OBJECT_TYPE_SOLID_SET_LOAD, lambda i: model.clientModel.service.get_solid_set_load(i), 'from RFEM.Loads.solidSetLoad import SolidSetLoad\n', 'SolidSetLoad'],
            [ObjectTypes.E_OBJECT_TYPE_FREE_CONCENTRATED_LOAD, lambda i: model.clientModel.service.get_free_concentrated_load(i), 'from RFEM.Loads.freeLoad import ConcentratedLoad\n', 'ConcentratedLoad'],
            [ObjectTypes.E_OBJECT_TYPE_FREE_LINE_LOAD, lambda i: model.clientModel.service.get_free_line_load(i), 'from RFEM.Loads.freeLoad import LineLoad\n', 'LineLoad'],
            [ObjectTypes.E_OBJECT_TYPE_FREE_RECTANGULAR_LOAD, lambda i: model.clientModel.service.get_free_rectangular_load(i), 'from RFEM.Loads.freeLoad import RectangularLoad\n', 'RectangularLoad'],
            [ObjectTypes.E_OBJECT_TYPE_FREE_CIRCULAR_LOAD, lambda i: model.clientModel.service.get_free_circular_load(i), 'from RFEM.Loads.freeLoad import CircularLoad\n', 'CircularLoad'],
            [ObjectTypes.E_OBJECT_TYPE_FREE_POLYGON_LOAD, lambda i: model.clientModel.service.get_free_polygon_load(i), 'from RFEM.Loads.freeLoad import PolygonLoad\n', 'PolygonLoad'],
            [ObjectTypes.E_OBJECT_TYPE_IMPOSED_NODAL_DEFORMATION, lambda i: model.clientModel.service.get_imposed_nodal_deformation(i), 'from RFEM.Loads.imposedNodalDeformation import ImposedNodalDeformation\n', 'ImposedNodalDeformation'],
            [ObjectTypes.E_OBJECT_TYPE_IMPOSED_LINE_DEFORMATION, lambda i: model.clientModel.service.get_imposed_line_deformation(i), 'from RFEM.Loads.imposedLineDeformation import ImposedLineDeformation\n', 'ImposedLineDeformation'],
            # calculations_diagra
            [ObjectTypes.E_OBJECT_TYPE_RESPONSE_SPECTRUM, lambda i: model.clientModel.service.get_response_spectrum(i), 'from RFEM.DynamicLoads.responseSpectrum import ResponseSpectrum\n', 'ResponseSpectrum']]

def convertSubclases(param):
    '''
    Convert structures/parameters
    '''

    if isinstance(param, str) or isinstance(param, int) or isinstance(param, float) or isinstance(param, bool):
        pass
    elif isinstance(param, list):
        toDel = []
        for i,j in enumerate(param):
            # Parameters of value None or UNKNOWN are not exported
            if j == None or j == 'UNKNOWN':
                toDel.append(i)
            else:
                param[i] = convertSubclases(j)
        for td in toDel:
            param.remove(td)
    else:
        param = dict(param)
        toDel = []
        for key in param.keys().__reversed__():
            # Parameters of value None or UNKNOWN are not exported
            if param[key] == None or param[key] == 'UNKNOWN':
                toDel.append(key)
            else:
                param[key] = convertSubclases(param[key])
        for td in toDel:
            del param[td]
    return param

importObjects = [''] # defines what to import with 'imports'
lines = cons_imports # individual lines written in file

# Get number of every type of object supported by Client.
# Get info of each existing object.
# Add import to lines.
# Add each object to lines.
for func in func_vec:
    objNumbers = GetObjectNumbersByType(ObjectType=func[0])
    if objNumbers:
        importObjects.append(func[2])
        for i in objNumbers:
            params = dict(func[1](i))
            params = convertSubclases(params)
            # don't set this parameter
            del params['id_for_export_import']

            lines.append(func[3]+'(params='+str(params)+')\n')

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

# Create file and write data
f = open(os.path.dirname(__file__)+"/WSgeneratedScript.py", "w", encoding="utf-8")
f.writelines(lines)
f.close()
