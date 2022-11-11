from RFEM.initModel import Model, GetAddonStatus
from RFEM.enums import AddOn

class MeshSettings():
    ComonMeshConfig: dict = {
        'general_target_length_of_fe': None,
        'general_maximum_distance_between_node_and_line': None,
        'general_maximum_number_of_mesh_nodes': None,
        'members_number_of_divisions_for_special_types': None,
        'members_activate_division_for_large_deformation_and_post_critical_analysis': None,
        'members_number_of_divisions_for_result_diagram': None,
        'members_number_of_divisions_for_min_max_values': None,
        'members_use_division_for_concrete_members': None,
        'members_number_of_divisions_for_concrete_members': None,
        'members_use_division_for_straight_members': None,
        'members_division_for_straight_members_type': None,
        'members_length_of_fe': None,
        'members_minimum_number_of_divisions': None,
        'members_use_division_for_members_with_nodes': None,
        'surfaces_maximum_ratio_of_fe': None,
        'surfaces_maximum_out_of_plane_inclination': None,
        'surfaces_mesh_refinement': None,
        'surfaces_relationship': None,
        'surfaces_integrate_also_unutilized_objects': None,
        'surfaces_shape_of_finite_elements': None,
        'surfaces_same_squares': None,
        'surfaces_triangles_for_membranes': None,
        'surfaces_mapped_mesh_preferred': None,
        'solids_use_refinement_if_containing_close_nodes': None,
        'solids_maximum_number_of_elements': None}
    SurfacesMeshQualityConfig: dict = {
        'mesh_quality_color_indicator_ok_color': None,
        'mesh_quality_color_indicator_warning_color': None,
        'mesh_quality_color_indicator_failure_color': None,
        'QualityCriteriaConfigForSurfaces': {
            'quality_criterion_check_aspect_ratio': None,
            'quality_criterion_check_aspect_ratio_warning': None,
            'quality_criterion_check_aspect_ratio_failure': None,
            'quality_criterion_parallel_deviations': None,
            'quality_criterion_parallel_deviations_warning': None,
            'quality_criterion_parallel_deviations_failure': None,
            'quality_criterion_corner_angles_of_triangle_elements': None,
            'quality_criterion_corner_angles_of_triangle_elements_warning': None,
            'quality_criterion_corner_angles_of_triangle_elements_failure': None,
            'quality_criterion_corner_angles_of_quadrangle_elements': None,
            'quality_criterion_corner_angles_of_quadrangle_elements_warning': None,
            'quality_criterion_corner_angles_of_quadrangle_elements_failure': None,
            'quality_criterion_warping_of_membrane_elements': None,
            'quality_criterion_warping_of_membrane_elements_warning': None,
            'quality_criterion_warping_of_membrane_elements_failure': None,
            'quality_criterion_warping_of_non_membrane_elements': None,
            'quality_criterion_warping_of_non_membrane_elements_warning': None,
            'quality_criterion_warping_of_non_membrane_elements_failure': None,
            'quality_criterion_jacobian_ratio': None,
            'quality_criterion_jacobian_ratio_warning': None,
            'quality_criterion_jacobian_ratio_failure': None}}
    SolidsMeshQualityConfig: dict = {
        'mesh_quality_color_indicator_ok_color': None,
        'mesh_quality_color_indicator_warning_color': None,
        'mesh_quality_color_indicator_failure_color': None,
        'QualityCriteriaConfigForSolids': {
            'quality_criterion_check_aspect_ratio': None,
            'quality_criterion_check_aspect_ratio_warning': None,
            'quality_criterion_check_aspect_ratio_failure': None,
            'quality_criterion_parallel_deviations': None,
            'quality_criterion_parallel_deviations_warning': None,
            'quality_criterion_parallel_deviations_failure': None,
            'quality_criterion_corner_angles_of_triangle_elements': None,
            'quality_criterion_corner_angles_of_triangle_elements_warning': None,
            'quality_criterion_corner_angles_of_triangle_elements_failure': None,
            'quality_criterion_corner_angles_of_quadrangle_elements': None,
            'quality_criterion_corner_angles_of_quadrangle_elements_warning': None,
            'quality_criterion_corner_angles_of_quadrangle_elements_failure': None,
            'quality_criterion_warping': None,
            'quality_criterion_warping_warning': None,
            'quality_criterion_warping_failure': None,
            'quality_criterion_jacobian_ratio': None,
            'quality_criterion_jacobian_ratio_warning': None,
            'quality_criterion_jacobian_ratio_failure': None}}
    WindSimulationMeshConfig: dict = {
        'windsimulation_mesh_config_value_simplify_model': None,
        'windsimulation_mesh_config_value_determine_details_by': None,
        'windsimulation_mesh_config_value_level_of_details': None,
        'windsimulation_mesh_config_value_detail_size': None,
        'windsimulation_mesh_config_value_small_openings_closure_type': None,
        'windsimulation_mesh_config_value_small_openings_closure_value': None,
        'windsimulation_mesh_config_value_optimized_member_topology': None,
        'windsimulation_mesh_config_value_optimized_member_topo_value': None,
        'windsimulation_mesh_config_value_active_objects_only': None,
        'windsimulation_mesh_config_value_terrain': None,
        'windsimulation_mesh_config_value_terrain_from_model': None,
        'windsimulation_mesh_config_value_terrain_objects_id': None,
        'windsimulation_mesh_config_value_terrain_objects_all': None,
        'windsimulation_mesh_config_value_surrounding_model': None,
        'windsimulation_mesh_config_value_surrounding_model_ifc_objects_id': None,
        'windsimulation_mesh_config_value_surrounding_model_ifc_objects_all': None,
        'windsimulation_mesh_config_value_surrounding_model_visual_objects_id': None,
        'windsimulation_mesh_config_value_surrounding_model_visual_objects_all': None,
        'windsimulation_mesh_config_value_keep_results_if_mesh_deleted': None,
        'windsimulation_mesh_config_value_consider_surface_thickness': None,
        'windsimulation_mesh_config_value_run_rwind_silent': None}

    def __init__(self,
                 commonConfig: dict = ComonMeshConfig,
                 surfaceConfig: dict = SurfacesMeshQualityConfig,
                 solidConfig: dict = SolidsMeshQualityConfig,
                 windConfig: dict = WindSimulationMeshConfig,
                 model = Model):
        """
        The object is automaticaly created therefore we can assume that it will not be created but only updated.
        Only posititve values are recognized.

        Args:
            commonConfig: common parameters settings
            surfaceConfig: surface specific parameters
            solidConfig: solid specific parameters
            windConfig: wind specific parameters; use only when Wind Simulation Add-on is active
        """
        # Get current mesh settings
        config = model.clientModel.service.get_mesh_settings()

        clientObject = {}
        for i in config:
            if i[0] == 'windSimulationMeshConfig':
                if GetAddonStatus(model.clientModel, AddOn.wind_simulation_active):
                    clientObject[i[0]] = config[i[0]]
            else:
                clientObject[i[0]] = config[i[0]]

        # No parameter can be set to None
        for key in commonConfig:
            if commonConfig[key]:
                clientObject[key] = commonConfig[key]
        for key in surfaceConfig:
            if key == 'QualityCriteriaConfigForSurfaces':
                for key_ in surfaceConfig['QualityCriteriaConfigForSurfaces']:
                    if surfaceConfig['QualityCriteriaConfigForSurfaces'][key_]:
                        clientObject['SurfacesMeshQualityConfig']['QualityCriteriaConfigForSurfaces'][key_] = surfaceConfig['QualityCriteriaConfigForSurfaces'][key_]
            elif surfaceConfig[key]:
                clientObject['SurfacesMeshQualityConfig'][key] = surfaceConfig[key]
        for key in solidConfig:
            if key == 'QualityCriteriaConfigForSolids':
                for key_ in solidConfig['QualityCriteriaConfigForSolids']:
                    if solidConfig['QualityCriteriaConfigForSolids'][key_]:
                        clientObject['SolidsMeshQualityConfig']['QualityCriteriaConfigForSolids'][key_] = solidConfig['QualityCriteriaConfigForSolids'][key_]
            elif solidConfig[key]:
                clientObject['SolidsMeshQualityConfig'][key] = solidConfig[key]
        if  GetAddonStatus(model.clientModel, AddOn.wind_simulation_active):
            for key in windConfig:
                if windConfig[key]:
                    clientObject['windSimulationMeshConfig'][key] = windConfig[key]

        # Add Mesh Settings to client model
        model.clientModel.service.set_mesh_settings(clientObject)

    @staticmethod
    def set_mesh_settings(all_settings, model = Model):
        new_sett = {}

        for i in all_settings:
            if i[0] == 'windSimulationMeshConfig':
                if GetAddonStatus(model.clientModel, AddOn.wind_simulation_active):
                    new_sett['wind_simulation_active'] = all_settings['wind_simulation_active']
            else:
                new_sett[i[0]] = all_settings[i[0]]

        model.clientModel.service.set_mesh_settings(new_sett)

def GetModelInfo(model = Model):
    return model.clientModel.service.get_model_info()

def GetMeshStatistics(model = Model):
    mesh_stats = model.clientModel.service.get_mesh_statistics()
    return model.clientModel.dict(mesh_stats)

def GenerateMesh(model = Model, skip_warnings = True):
    model.clientModel.service.generate_mesh(skip_warnings)

def GetMeshSettings(model = Model):
    return model.clientModel.service.get_mesh_settings()
