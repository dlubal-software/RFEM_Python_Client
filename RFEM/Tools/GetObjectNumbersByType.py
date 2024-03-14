from RFEM.initModel import Model, ConvertStrToListOfInt, GetAllAddonStatuses
from RFEM.enums import ObjectTypes
from suds.sax.text import Text
import sys

class GetObjectNumbersByType:

    def __new__(cls,
                ObjectType = ObjectTypes.E_OBJECT_TYPE_NODE,
                model = Model):

        """
        Returns a sorted list which contains object numbers in RFEM tables.
        ObjectNumberList = [1, 2, ... ] or [[1,2], [2,2]]

        Args:
            ObjectType (enum): Object type enum
            model (RFEM Class, optional): Model to be edited
        Returns:
            ObjectNumberList (list): Sorted list of object numbers or list of lists if there is parent number (e.g. nodal_load).
        """

        ObjectNumber = model.clientModel.service.get_all_object_numbers_by_type(ObjectType.name)
        ObjectNumberList = []

        if len(ObjectNumber):
            for i in range(len(ObjectNumber.item)):
                # this is used when requesting objects in loads (E_OBJECT_TYPE_NODAL_LOAD, E_OBJECT_TYPE_LINE_LOAD etc.)
                try:
                    children = ConvertStrToListOfInt(ObjectNumber.item[i].children)
                    for c in children:
                        ObjectNumberList.append([c, ObjectNumber.item[i].no])
                # all other objects
                except:
                    ObjectNumberList.append(ObjectNumber.item[i].no)

            if isinstance(ObjectNumberList[0], list):
                ObjectNumberList = sorted(ObjectNumberList, key=lambda x: x[1])
            else:
                ObjectNumberList.sort()

        return ObjectNumberList

class GetAllObjects:
    """
    Returns tuple of 2 lists containing all objects and their parameters and list of imports needed to facilitate re-creating theese.
    Args:
        model(RFEM Class, optional): Model to be edited
    Returns:
        objects: List of all objects that can be created via Client.
        imports: List of imports needed to be able to create objects from the first list.
    """
    def __new__(cls,
                model = Model):

        # Steps to retrieve data from RFEM:
        # 1) get numbers of given object type via GetObjectNumbersByType(),
        # 2) get data from individual objects,
        # 3) set import of the type,
        # 4) set individual objects.
        # For each of these steps individual record is made (4 total).

        # Vector of all function
        func_vec = [[ObjectTypes.E_OBJECT_TYPE_COORDINATE_SYSTEM, lambda i: model.clientModel.service.get_coordinate_system(i), 'from RFEM.GuideObjects.coordinateSystem import CoordinateSystem\n', 'CoordinateSystem'],
            [ObjectTypes.E_OBJECT_TYPE_MATERIAL, lambda i: model.clientModel.service.get_material(i), 'from RFEM.BasicObjects.material import Material\n', 'Material'],
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

            [ObjectTypes.E_OBJECT_TYPE_INTERSECTION, lambda i: model.clientModel.service.get_intersection(i), 'from RFEM.SpecialObjects.intersection import Intersection\n', 'Intersection'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_RESULTS_ADJUSTMENT, lambda i: model.clientModel.service.get_surface_results_adjustment(i), 'from RFEM.SpecialObjects.surfaceResultAdjustment import SurfaceResultsAdjustment\n', 'SurfaceResultsAdjustment'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACES_CONTACT, lambda i: model.clientModel.service.get_surfaces_contact(i), 'from RFEM.SpecialObjects.surfaceContact import SurfaceContact\n', 'SurfaceContact'],
            [ObjectTypes.E_OBJECT_TYPE_RIGID_LINK, lambda i: model.clientModel.service.get_rigid_link(i), 'from RFEM.SpecialObjects.rigidLink import RigidLink\n', 'RigidLink'],
            [ObjectTypes.E_OBJECT_TYPE_RESULT_SECTION, lambda i: model.clientModel.service.get_result_section(i), 'from RFEM.SpecialObjects.resultSection import ResultSection\n', 'ResultSection'],
            # nodal_release
            [ObjectTypes.E_OBJECT_TYPE_LINE_RELEASE, lambda i: model.clientModel.service.get_line_release(i), 'from RFEM.SpecialObjects.lineRelease import LineRelease\n', 'LineRelease'],
            # surface_release
            # blocks
            # boreholes
            # soil_massif

            [ObjectTypes.E_OBJECT_TYPE_NODAL_SUPPORT, lambda i: model.clientModel.service.get_nodal_support(i), 'from RFEM.TypesForNodes.nodalSupport import NodalSupport\n', 'NodalSupport'],
            [ObjectTypes.E_OBJECT_TYPE_NODAL_MESH_REFINEMENT, lambda i: model.clientModel.service.get_nodal_mesh_refinement(i), 'from RFEM.TypesForNodes.nodalMeshRefinement import NodalMeshRefinement\n', 'NodalMeshRefinement'],

            [ObjectTypes.E_OBJECT_TYPE_LINE_SUPPORT, lambda i: model.clientModel.service.get_line_support(i), 'from RFEM.TypesForLines.lineSupport import LineSupport\n', 'LineSupport'],
            [ObjectTypes.E_OBJECT_TYPE_LINE_MESH_REFINEMENT, lambda i: model.clientModel.service.get_line_mesh_refinement(i), 'from RFEM.TypesForLines.lineMeshRefinements import LineMeshRefinement\n', 'LineMeshRefinement'],
            [ObjectTypes.E_OBJECT_TYPE_LINE_HINGE, lambda i: model.clientModel.service.get_line_hinge(i), 'from RFEM.TypesForLines.lineHinge import LineHinge\n', 'LineHinge'],
            [ObjectTypes.E_OBJECT_TYPE_LINE_WELDED_JOINT, lambda i: model.clientModel.service.get_line_welded_joint(i), 'from RFEM.TypesForLines.lineWeldedJoint import LineWeldedJoint\n', 'LineWeldedJoint'],

            [ObjectTypes.E_OBJECT_TYPE_MEMBER_HINGE, lambda i: model.clientModel.service.get_member_hinge(i), 'from RFEM.TypesForMembers.memberHinge import MemberHinge\n', 'MemberHinge'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_ECCENTRICITY, lambda i: model.clientModel.service.get_member_eccentricity(i), 'from RFEM.TypesForMembers.memberEccentricity import MemberEccentricity\n', 'MemberEccentricity'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_SUPPORT, lambda i: model.clientModel.service.get_member_support(i), 'from RFEM.TypesForMembers.memberSupport import MemberSupport\n', 'MemberSupport'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_TRANSVERSE_STIFFENER, lambda i: model.clientModel.service.get_member_transverse_stiffener(i), 'from RFEM.TypesForMembers.memberTransverseStiffeners import MemberTransverseStiffener\n', 'MemberTransverseStiffener'],
            # member_opening
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_STIFFNESS_MODIFICATION, lambda i: model.clientModel.service.get_member_stiffness_modification(i), 'from RFEM.TypesForMembers.memberStiffnessModification import MemberStiffnessModification\n', 'MemberStiffnessModification'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_NONLINEARITY, lambda i: model.clientModel.service.get_member_nonlinearity(i), 'from RFEM.TypesForMembers.memberNonlinearity import MemberNonlinearity\n', 'MemberNonlinearity'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_DEFINABLE_STIFFNESS, lambda i: model.clientModel.service.get_member_definable_stiffness(i), 'from RFEM.TypesForMembers.memberDefinableStiffness import MemberDefinableStiffness\n', 'MemberDefinableStiffness'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_RESULT_INTERMEDIATE_POINT, lambda i: model.clientModel.service.get_member_result_intermediate_point(i), 'from RFEM.TypesForMembers.memberResultIntermediatePoints import MemberResultIntermediatePoint\n', 'MemberResultIntermediatePoint'],
            # design_support
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_ROTATIONAL_RESTRAINT, lambda i: model.clientModel.service.get_member_rotational_restraint(i), 'from RFEM.TypesForMembers.memberRotationalRestraint import MemberRotationalRestraint\n', 'MemberRotationalRestraint'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_SHEAR_PANEL, lambda i: model.clientModel.service.get_member_shear_panel(i), 'from RFEM.TypesForMembers.memberShearPanel import MemberShearPanel\n', 'MemberShearPanel'],

            [ObjectTypes.E_OBJECT_TYPE_SURFACE_SUPPORT, lambda i: model.clientModel.service.get_surface_support(i), 'from RFEM.TypesForSurfaces.surfaceSupport import SurfaceSupport\n', 'SurfaceSupport'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_ECCENTRICITY, lambda i: model.clientModel.service.get_surface_eccentricity(i), 'from RFEM.TypesForSurfaces.surfaceEccentricity import SurfaceEccentricity\n', 'SurfaceEccentricity'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_STIFFNESS_MODIFICATION, lambda i: model.clientModel.service.get_surface_stiffness_modification(i), 'from RFEM.TypesForSurfaces.surfaceStiffnessModification import SurfaceStiffnessModification\n', 'SurfaceStiffnessModification'],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_MESH_REFINEMENT, lambda i: model.clientModel.service.get_surface_mesh_refinement(i), 'from RFEM.TypesForSurfaces.surfaceMeshRefinements import SurfaceMeshRefinement\n', 'SurfaceMeshRefinement'],

            [ObjectTypes.E_OBJECT_TYPE_SOLID_MESH_REFINEMENT, lambda i: model.clientModel.service.get_solid_mesh_refinement(i), 'from RFEM.TypesForSolids.solidMeshRefinement import SolidMeshRefinement\n', 'SolidMeshRefinement'],
            [ObjectTypes.E_OBJECT_TYPE_SOLID_GAS, lambda i: model.clientModel.service.get_solid_gas(i), 'from RFEM.TypesForSolids.solidGas import SolidGas\n', 'SolidGas'],
            [ObjectTypes.E_OBJECT_TYPE_SOLID_CONTACTS, lambda i: model.clientModel.service.get_solid_contacts(i), 'from RFEM.TypesForSolids.solidContact import SolidContacts\n', 'SolidContacts'],

            [ObjectTypes.E_OBJECT_TYPE_SURFACES_CONTACT, lambda i: model.clientModel.service.get_surfaces_contact(i), 'from RFEM.SpecialObjects.surfaceContact import SurfaceContact\n', 'SurfaceContact'],

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

            [ObjectTypes.E_OBJECT_TYPE_STEEL_DESIGN_SLS_CONFIGURATION, lambda i: model.clientModel.service.get_steel_design_sls_configuration(i), 'from RFEM.SteelDesign.steelServiceabilityConfiguration import SteelDesignServiceabilityConfigurations\n', 'SteelDesignServiceabilityConfigurations'],
            [ObjectTypes.E_OBJECT_TYPE_STEEL_DESIGN_ULS_CONFIGURATION, lambda i: model.clientModel.service.get_steel_design_uls_configuration(i), 'from RFEM.SteelDesign.steelUltimateConfigurations import SteelDesignUltimateConfigurations\n', 'SteelDesignUltimateConfigurations'],
            [ObjectTypes.E_OBJECT_TYPE_TIMBER_EFFECTIVE_LENGTHS, lambda i: model.clientModel.service.get_timber_effective_lengths(i), 'from RFEM.TypesForTimberDesign.timberEffectiveLengths import TimberEffectiveLengths\n', 'TimberEffectiveLengths'],
            [ObjectTypes.E_OBJECT_TYPE_TIMBER_SERVICE_CLASS, lambda i: model.clientModel.service.get_timber_service_class(i), 'from RFEM.TypesForTimberDesign.timberServiceClass import TimberServiceClass\n', 'TimberServiceClass'],
            [ObjectTypes.E_OBJECT_TYPE_ALUMINUM_MEMBER_LOCAL_SECTION_REDUCTION, lambda i: model.clientModel.service.get_timber_member_local_section_reduction(i), 'from RFEM.TypesForTimberDesign.timberMemberLocalSectionReduction import TimberMemberLocalSectionReduction\n', 'TimberMemberLocalSectionReduction'],
            [ObjectTypes.E_OBJECT_TYPE_TIMBER_DESIGN_SLS_CONFIGURATION, lambda i: model.clientModel.service.get_timber_design_sls_configuration(i), 'from RFEM.TimberDesign.timberServiceLimitStateConfigurations import TimberDesignServiceLimitStateConfigurations\n', 'TimberDesignServiceLimitStateConfigurations'],
            [ObjectTypes.E_OBJECT_TYPE_TIMBER_DESIGN_ULS_CONFIGURATION, lambda i: model.clientModel.service.get_timber_design_uls_configuration(i), 'from RFEM.TimberDesign.timberUltimateConfigurations import TimberDesignUltimateConfigurations\n', 'TimberDesignUltimateConfigurations'],
            [ObjectTypes.E_OBJECT_TYPE_ALUMINUM_EFFECTIVE_LENGTHS, lambda i: model.clientModel.service.get_aluminum_effective_lengths(i), 'from RFEM.TypesForAluminumDesign.aluminumEffectiveLengths import AluminumEffectiveLengths\n', 'AluminumEffectiveLengths'],
            [ObjectTypes.E_OBJECT_TYPE_ALUMINUM_MEMBER_LOCAL_SECTION_REDUCTION, lambda i: model.clientModel.service.get_aluminum_member_local_section_reduction(i), 'from RFEM.TypesForAluminumDesign.aluminumMemberLocalSectionReduction import AluminumMemberLocalSectionReduction\n', 'AluminumMemberLocalSectionReduction'],
            [ObjectTypes.E_OBJECT_TYPE_ALUMINUM_MEMBER_TRANSVERSE_WELD, lambda i: model.clientModel.service.get_aluminum_member_transverse_weld(i), 'from RFEM.TypesForAluminumDesign.aluminumMemberTransverseWelds import AluminumMemberTransverseWeld\n', 'AluminumMemberTransverseWeld'],
            # steel_joints
            # craneways
            # cran
            [ObjectTypes.E_OBJECT_TYPE_IMPERFECTION_CASE, lambda i: model.clientModel.service.get_imperfection_case(i), 'from RFEM.Imperfections.imperfectionCase import ImperfectionCase\n', 'ImperfectionCase'],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_IMPERFECTION, lambda i,j: model.clientModel.service.get_member_imperfection(i,j), 'from RFEM.Imperfections.memberImperfection import MemberImperfection\n', 'MemberImperfection(imperfection_case='],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_SET_IMPERFECTION, lambda i: model.clientModel.service.get_member_set_imperfection(i), 'from RFEM.Imperfections.membersetImperfection import MemberSetImperfection\n', 'MemberSetImperfection(imperfection_case='],
            # construction_stag
            [ObjectTypes.E_OBJECT_TYPE_LOAD_CASE, lambda i: model.clientModel.service.get_load_case(i), 'from RFEM.LoadCasesAndCombinations.loadCase import LoadCase\n', 'LoadCase'],
            [ObjectTypes.E_OBJECT_TYPE_DESIGN_SITUATION, lambda i: model.clientModel.service.get_design_situation(i), 'from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation\n', 'DesignSituation'],
            [ObjectTypes.E_OBJECT_TYPE_LOAD_COMBINATION, lambda i: model.clientModel.service.get_load_combination(i), 'from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination\n', 'LoadCombination'],
            #[ObjectTypes, lambda i: model.clientModel.service.get_load_cases_and_combinations(), 'from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations\n', 'LoadCasesAndCombinations']
            [ObjectTypes.E_OBJECT_TYPE_RESULT_COMBINATION, lambda i: model.clientModel.service.get_result_combination(i), 'from RFEM.LoadCasesAndCombinations.resultCombination import ResultCombination\n', 'ResultCombination'],
            [ObjectTypes.E_OBJECT_TYPE_STATIC_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_static_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings\n', 'StaticAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_STABILITY_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_stability_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.stabilityAnalysisSettings import StabilityAnalysisSettings\n', 'StabilityAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_MODAL_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_modal_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.modalAnalysisSettings import ModalAnalysisSettings\n', 'ModalAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_SPECTRAL_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_spectral_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.spectralAnalysisSettings import SpectralAnalysisSettings\n', 'SpectralAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_WIND_SIMULATION_ANALYSIS_SETTINGS, lambda i: model.clientModel.service.get_wind_simulation_analysis_settings(i), 'from RFEM.LoadCasesAndCombinations.windSimulationAnalysisSetting import WindSimulationAnalysisSettings\n', 'WindSimulationAnalysisSettings'],
            [ObjectTypes.E_OBJECT_TYPE_COMBINATION_WIZARD, lambda i: model.clientModel.service.get_combination_wizard(i), 'from RFEM.LoadCasesAndCombinations.combinationWizard import CombinationWizard\n', 'CombinationWizard'],

            [ObjectTypes.E_OBJECT_TYPE_STRUCTURE_MODIFICATION, lambda i: model.clientModel.service.get_structure_modification(i), 'from RFEM.SpecialObjects.structureModification import StructureModification\n', 'StructureModification'],
            # member_loads_from_area_loads
            # member_loads_from_free_line_load
            # snow_loads
            # wind_loads
            # wind_profiles
            # wind_simulatio
            [ObjectTypes.E_OBJECT_TYPE_NODAL_LOAD, lambda i,j: model.clientModel.service.get_nodal_load(i,j), 'from RFEM.Loads.nodalLoad import NodalLoad\n', 'NodalLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_LINE_LOAD, lambda i,j: model.clientModel.service.get_line_load(i,j), 'from RFEM.Loads.lineLoad import LineLoad\n', 'LineLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_LOAD, lambda i,j: model.clientModel.service.get_member_load(i,j), 'from RFEM.Loads.memberLoad import MemberLoad\n', 'MemberLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_LOAD, lambda i,j: model.clientModel.service.get_surface_load(i,j), 'from RFEM.Loads.surfaceLoad import SurfaceLoad\n', 'SurfaceLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_OPENING_LOAD, lambda i,j: model.clientModel.service.get_opening_load(i,j), 'from RFEM.Loads.openingLoad import OpeningLoad\n', 'OpeningLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_SOLID_LOAD, lambda i,j: model.clientModel.service.get_solid_load(i,j), 'from RFEM.Loads.solidLoad import SolidLoad\n', 'SolidLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_LINE_SET_LOAD, lambda i,j: model.clientModel.service.get_line_set_load(i,j), 'from RFEM.Loads.linesetLoad import LineSetLoad\n', 'LineSetLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_MEMBER_SET_LOAD, lambda i,j: model.clientModel.service.get_member_set_load(i,j), 'from RFEM.Loads.membersetload import MemberSetLoad\n', 'MemberSetLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_SURFACE_SET_LOAD, lambda i,j: model.clientModel.service.get_surface_set_load(i,j), 'from RFEM.Loads.surfacesetload import SurfaceSetLoad\n', 'SurfaceSetLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_SOLID_SET_LOAD, lambda i,j: model.clientModel.service.get_solid_set_load(i,j), 'from RFEM.Loads.solidSetLoad import SolidSetLoad\n', 'SolidSetLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_FREE_CONCENTRATED_LOAD, lambda i,j: model.clientModel.service.get_free_concentrated_load(i,j), 'from RFEM.Loads.freeLoad import FreeLoad\n', 'FreeLoad.ConcentratedLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_FREE_LINE_LOAD, lambda i,j: model.clientModel.service.get_free_line_load(i,j), 'from RFEM.Loads.freeLoad import FreeLoad\n', 'FreeLoad.LineLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_FREE_RECTANGULAR_LOAD, lambda i,j: model.clientModel.service.get_free_rectangular_load(i,j), 'from RFEM.Loads.freeLoad import FreeLoad\n', 'FreeLoad.RectangularLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_FREE_CIRCULAR_LOAD, lambda i,j: model.clientModel.service.get_free_circular_load(i,j), 'from RFEM.Loads.freeLoad import CircularLoad\n', 'CircularLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_FREE_POLYGON_LOAD, lambda i,j: model.clientModel.service.get_free_polygon_load(i,j), 'from RFEM.Loads.freeLoad import FreeLoad\n', 'FreeLoad.PolygonLoad(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_IMPOSED_NODAL_DEFORMATION, lambda i,j: model.clientModel.service.get_imposed_nodal_deformation(i,j), 'from RFEM.Loads.imposedNodalDeformation import ImposedNodalDeformation\n', 'ImposedNodalDeformation(load_case_no='],
            [ObjectTypes.E_OBJECT_TYPE_IMPOSED_LINE_DEFORMATION, lambda i,j: model.clientModel.service.get_imposed_line_deformation(i,j), 'from RFEM.Loads.imposedLineDeformation import ImposedLineDeformation\n', 'ImposedLineDeformation(load_case_no=']]
            # calculations_diagram
            #[ObjectTypes.E_OBJECT_TYPE_RESPONSE_SPECTRUM, lambda i: model.clientModel.service.get_response_spectrum(i), 'from RFEM.DynamicLoads.responseSpectrum import ResponseSpectrum\n', 'ResponseSpectrum']]

        def convertSubclases(param):
            '''
            Convert structures/parameters to approriate structure
            '''
            if isinstance(param, str) or isinstance(param, int) or isinstance(param, float) or isinstance(param, bool):
                pass
            elif isinstance(param, list):
                toDel = []
                for i,j in enumerate(param):
                    # Parameters of value None, UNKNOWN or "" are not exported
                    if j == None or j == 'UNKNOWN' or j == "":
                        toDel.append(i)
                    elif isinstance(j, Text):
                        # Change Text to string
                        param[i] = str(j)
                    else:
                        param[i] = convertSubclases(j)
                for td in toDel:
                    param.remove(td)
            else:
                param = dict(param)
                toDel = []
                for key in param.keys().__reversed__():
                    # Parameters of value None, UNKNOWN or "" are not exported
                    if param[key] == None or param[key] == 'UNKNOWN' or param[key] == "":
                        toDel.append(key)
                    elif isinstance(param[key], Text):
                        # Change Text to string
                        param[key] = str(param[key])
                    else:
                        param[key] = convertSubclases(param[key])
                for td in toDel:
                    del param[td]
            return param

        imports = [] # defines what to import with 'imports'
        objects = [] # individual lines written in file

        # Load Cases and Combinations setup
        loadCasesAndCombinations = convertSubclases(dict(model.clientModel.service.get_load_cases_and_combinations()))
        settingsAndOptions = dict(model.clientModel.service.get_model_settings_and_options())
        mainObjectsToActivate = dict(model.clientModel.service.get_main_objects_to_activate())
        addonStatuses = GetAllAddonStatuses(model.clientModel)
        del settingsAndOptions['date_of_zero_day']
        settingsAndOptions = convertSubclases(settingsAndOptions)

        objects.append('LoadCasesAndCombinations(params='+str(loadCasesAndCombinations)+')\n')
        objects.append('BaseSettings(params='+str(settingsAndOptions)+')\n')
        objects.append('MainObjectsToActivate(params='+str(mainObjectsToActivate)+')\n')
        objects.append('SetAddonStatuses('+str(addonStatuses)+')\n')

        imports.append('from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations\n')
        imports.append('from RFEM.baseSettings import BaseSettings, MainObjectsToActivate\n')

        # Get number of every type of object supported by Client.
        # Get info of each existing object.
        # Add import to lines.
        # Add each object to lines.
        for id, func in enumerate(func_vec):

            objNumbers = GetObjectNumbersByType(ObjectType=func[0])
            if objNumbers:
                addImport = False
                for idx,i in enumerate(objNumbers):

                    # Print status
                    percent = (idx/len(objNumbers))*100
                    sys.stdout.write("\r                                                                       ")
                    sys.stdout.write("\r{}: {:.0f}%, total progress: {:.1f}% ".format(func[3], (id/len(func_vec))*100, percent))
                    sys.stdout.flush()

                    try:
                        if isinstance(i, list):
                            params = dict(func[1](i[0], i[1]))
                        else:
                            params = dict(func[1](i))
                        addImport = True
                    except:
                        print('INFO: There seems to a be phantom object or issue in your model. Type:', func[3], ', number:', str(i))
                        continue
                    params = convertSubclases(params)
                    # don't set this parameter
                    del params['id_for_export_import']

                    if isinstance(i, list):
                        objects.append(func[3]+str(i[1])+', params='+str(params)+')\n')
                    else:
                        objects.append(func[3]+'(params='+str(params)+')\n')

                # Add import if at least one object was added
                if addImport:
                    imports.append(func[2])

        sys.stdout.write("\r                                                                       ")
        sys.stdout.write("\rDone 100%\n")
        sys.stdout.flush()
        return (objects, imports)
