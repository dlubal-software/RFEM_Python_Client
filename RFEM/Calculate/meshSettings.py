from RFEM.initModel import *
from RFEM.enums import *

class MeshSettings():
    class meshConfig():
        general_target_length_of_fe = None
        general_maximum_distance_between_node_and_line = None
        general_maximum_number_of_mesh_nodes = None
        members_number_of_divisions_for_special_types = None
        members_activate_division_for_large_deformation_and_post_critical_analysis = None
        members_number_of_divisions_for_result_diagram = None
        members_number_of_divisions_for_min_max_values = None
        members_use_division_for_concrete_members = None
        members_number_of_divisions_for_concrete_members = None
        members_use_division_for_straight_members = None
        members_division_for_straight_members_type = None
        members_length_of_fe = None
        members_minimum_number_of_divisions = None
        members_use_division_for_members_with_nodes = None
        surfaces_maximum_ratio_of_fe = None
        surfaces_maximum_out_of_plane_inclination = None
        surfaces_mesh_refinement = None
        surfaces_relationship = None
        surfaces_integrate_also_unutilized_objects = None
        surfaces_shape_of_finite_elements = None
        surfaces_same_squares = None
        surfaces_triangles_for_membranes = None
        surfaces_mapped_mesh_preferred = None
        solids_use_refinement_if_containing_close_nodes = None
        solids_maximum_number_of_elements = None

    def __init__(self, meshConfig):
        """
        The object is automaticaly created therefore we can assume, that it will not be created but only
        updated/changed.

        Args:
            no (int): Setting Tag
            name (str): Setting Name
            analysis_type (enum): Analysis Type Enumeration
            comment (str): Comments
            params (dict): Parameters
        """
        # Get current mesh settings
        clientObject = clientModel.service.get_mesh_settings()
        
        for key in meshConfig:
            if meshConfig[key]:
                clientObject[key] = meshConfig[key]


        # Add Mesh Settings to client model
        clientModel.service.set_mesh_settings(clientObject)

    def get_mesh_settings(self):
        return clientModel.service.get_mesh_settings()
    def set_mesh_settings(self):
        pass
    def get_model_info(self):
        return clientModel.service.get_model_info()