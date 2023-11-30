from RFEM.initModel import Model
from RFEM.enums import ActionType, ImposedLoadCategory, ActionCombinationItems
from RFEM import connectionGlobals

###########################################
# Application functions
###########################################

"""
Additional functions missing in this file.
Date: 29/11/2023,
RFEM 6.04.0009.197.2f47af57c08

['get_current_project', 'get_list_of_existing_projects',
'get_list_of_existing_templates', 'get_model_list_with_indexes', 'get_project', 'get_settings_program_language', 'get_template',
'calculate_all_in_cloud', 'export_to_asf', 'get_Dxf_file_model_object', 'get_Dxf_model_object', 'get_accelerogram',
'get_action', 'get_action_categories_for_action', 'get_action_categories_for_load_case', 'get_action_combination',
'get_all_available_machines_in_cloud', 'get_all_object_numbers_by_type', 'get_all_selected_objects',
'get_aluminum_design_sls_configuration', 'get_aluminum_design_uls_configuration', 'get_building_grid', 'get_building_story',
'get_calculation_diagram', 'get_calculation_errors', 'get_clipping_box', 'get_clipping_plane', 'get_construction_stage',
'get_design_situation_types', 'get_design_support', 'get_dimension', 'get_floor_set', 'get_global_parameter', 'get_member_openings',
'get_member_representative', 'get_member_set_representative', 'get_model_history', 'get_nodal_release', 'get_nodal_release_type',
'get_note', 'get_nth_object_number', 'get_object_count', 'get_object_information', 'get_object_snap', 'get_optimized_values',
'get_parts_list_deep_beams_by_material', 'get_parts_list_member_set_representatives_by_material', 'get_parts_list_shear_walls_by_material',
'get_punching_reinforcement', 'get_pushover_analysis_settings', 'get_relationship_between_load_cases', 'get_shear_wall', 'get_soil_massif',
'get_steel_design_fr_configuration', 'get_steel_design_seismic_configuration', 'get_surface_imperfection', 'get_surface_release',
'get_surface_release_type', 'get_surface_set_imperfection', 'get_surfaces_contact_type', 'get_terrain', 'get_timber_design_fr_configuration',
'get_timber_moisture_class', 'get_timber_service_conditions', 'get_visual_object', 'get_wind_profile', 'get_wind_simulation_analysis_settings',
'set_accelerogram', 'set_aluminum_design_sls_configuration', 'set_aluminum_design_uls_configuration', 'set_building_grid','set_calculation_diagram',
'set_floor_set', 'set_member_openings', 'set_model_id', 'set_pushover_analysis_settings','set_shear_wall',
'set_steel_design_fr_configuration', 'set_steel_design_seismic_configuration','set_timber_design_fr_configuration', 'use_detailed_member_results']

What is not here is somewhere else in the project often in initModel.py or excluded.

Excluded functions:
For these functions doesn't make sense to create dedicated function.

['beginModification', 'finishModeification', 'cancel_modification']
"""


def closeApplication():
    '''
    Close RFEM/RSTAB app
    '''
    connectionGlobals.client.service.close_application()

# For both / and \\ in file path I get invalid file path
def deleteProject(projectPath):
    '''
    Delete project
    '''
    connectionGlobals.client.service.delete_project(projectPath)

# Not in coverage results, but works
def newModel(model_name):
    '''
    Create new model

    Args:
        model_name(str): Model name
    '''
    connectionGlobals.client.service.new_model(model_name)

# Not tested, see newTemplate
def newModelFromTemplate(model_name, file_path):
    '''
    Create newmodel from template

    Args:
        model_name (str): Name of the model
        file_path (str): Path to the file
    '''
    connectionGlobals.client.service.new_model_from_template(model_name, file_path)

# Cannot figure out the parent path
def newProject(name, description, parent_path, folder_path):
    '''
    Create new project

    Args:
        name (str): Name of the project
        description (str): Project description
        parent_path (str): Parenth path
        folder_path (str): Folder path
    '''
    pi = connectionGlobals.client.factory.create('ns0:project_info')
    pi.name = name
    pi.description = description
    pi.parent_path = parent_path
    pi.folder_path = folder_path

    connectionGlobals.client.service.new_project(pi)

# Function changed? new_template(ns0:project_info template_info, )
# Also cannot create template_info
def newTemplate(template_info): #ns0:template_info doesn't work
    '''
    Create new template

    Args:
        template_info
    '''
    connectionGlobals.client.service.new_template(template_info)

# I am getting HTTP Error 500 Internal server error model at index cannot be saved
def saveModel(model_index):
    '''
    Save model

    Args:
        model_index (int): Index of model to be saved
    '''
    connectionGlobals.client.service.save_model(model_index)

# It seems that I don't understand the project conept, because it says, that i have invalid file path, but I think, that project is not a file but a folder, anyways, I don't know how to use it
def setAsCurrentProject(project_path):
    connectionGlobals.client.service.set_as_current_project(project_path)

def setDetailedLogging(logging=True):
    '''
    Enable detailed logging

    Args:
        logging (bool): Enable or disable detailed logging
    '''
    connectionGlobals.client.service.set_detailed_logging(logging)

def getDetailedLogging():
    '''
    Get the status of detailed logging (returns bool)
    '''
    return connectionGlobals.client.service.get_detailed_logging()

# Doesn't work (tested on: ProgramLanguage.CZECH, etc.)
def setSettingsProgramLanguage(language):
    '''
    Set program language

    Args:
        language (enum ProgramLanguage): Program language
    '''
    connectionGlobals.client.service.set_settings_program_language(language)

###########################################
# Model functions
############################################

# I think I dont understand the list of loadings -
# when I tried it with [0] and [1] i got same results, but when i tried with [1, 2, 3] I got "unexpected structure of data"
def calculateSpecific(loadings, skip_warnings=True):
# calculate_specific(ns0:calculate_specific_loadings loadings, xs:boolean skip_warnings, )
    '''
    Calculate specified loadings

    Args:
        loadings (list): List of loadings
        skip_warnings (bool): Set to True if warnings should be skipped
    '''

    Model.clientModel.service.calculate_specific(loadings, skip_warnings)

# Not tested, there is no set selection yet
def clearSelection():
    '''
    Empty selection
    '''
    Model.clientModel.service.clear_selection()

def deleteAll():
    '''
    Delete all objects
    '''
    Model.clientModel.service.delete_all()

# Not tested, because, when I modify the model nothing is added to the history, so I can't verify, if it works
def deleteAllHistory():
    '''
    Delete whole history
    '''
    Model.clientModel.service.delete_all_history()

def deleteAllResults(delete_mesh = True):
    '''
    Delete results

    Args:
        delete_mesh (bool): Put True if the mesh should be deleted
    '''
    Model.clientModel.service.delete_all_results(delete_mesh)

# Not tested, because I dont know what it should do
def divideByIntersections(member_list, line_list, surface_list):
    '''
    Divide by intersections

    Args:
        member_list (list): List of members
        line_list (list): List of lines
        surface_list (list): List of surfaces
    '''
    Model.clientModel.service.divide_by_intersections(member_list, line_list, surface_list)

# I think this function doesn't generate anything, so the name is wrong,
# and the validation also doesn't work - it returns Success on any file with .xml extension
def generateAndValidateXmlSolverInput(solver_input_file_path):
    '''
    Generate and validate XML input
    Returns result of validation

    Args:
        solver_input_file_path(str): Path to XML
    '''
    return Model.clientModel.service.generate_and_validate_xml_solver_input(solver_input_file_path)

# Don't know what this should produce, but neither LC or CO was generated
def generateLoadCasesAndCombinations():
    '''
    Generate load cases and combinations
    '''
    Model.clientModel.service.generate_load_cases_and_combinations()

def reset():
    '''
    Resets everything
    '''
    Model.clientModel.service.reset()

def runScript(script_file_path):
    '''
    Run JS script.

    Args:
        script_file_path (str): Path to JS script.
    '''
    Model.clientModel.service.run_script(script_file_path)


Dxf_file_model_object = {
   'no' : None,
   'origin_coordinate_x' : None,
   'origin_coordinate_y' : None,
   'origin_coordinate_z' : None,
   'rotation_angles_sequence' : {'value' : None},
   'rotation_angle_1' : None,
   'rotation_angle_2' : None,
   'rotation_angle_3' : None,
   'user_defined_name_enabled' : None,
   'name' : None,
   'filename' : None,
   'coordinate_system' : None,
   'insert_point' : {'value' : None},
   'scale_is_nonuniform' : None,
   'scale_is_defined_as_relative' : None,
   'scale_relative' : None,
   'scale_absolute' : None,
   'scale_relative_x' : None,
   'scale_relative_y' : None,
   'scale_relative_z' : None,
   'scale_absolute_x' : None,
   'scale_absolute_y' : None,
   'scale_absolute_z' : None
 }

# Not tested, I need dxf file
def setDxfFileModelObject(dxf_file_model_object): # ns0:Dxf_file_model_object
    '''
    Set DXF import parameters
    '''
    Model.clientModel.service.set_Dxf_file_model_object(dxf_file_model_object)

# Not tested, I need dxf file
def setDxfModelObject(parent_no, dxf_model_object): # ns0:Dxf_model_object
    Model.clientModel.service.set_Dxf_model_object(parent_no, dxf_model_object)

Action = {
   'no' : None,
   'name' : None,
   'is_active' : None,
   'action_category' : None,
   'action_type' : ActionType.ACTING_ALTERNATIVELY,
   'comment' : None,
   'is_generated' : None,
   'generating_object_info' : None,
   'items' : None, # array
   'has_short_duration' : None,
   'has_duration_shorter_than_one_month' : None,
   'imposed_load_category' : ImposedLoadCategory.IMPOSED_LOADS_CATEGORY_A,
   'has_short_duration_according_to_5132' : None,
   'for_temperature_apply_coefficients' : None,
   'short_time_variable_action' : None,
   'crane_operated_ware_housing_system_reduced_partial_factor' : None,
   'has_inclusive_action' : None,
   'inclusive_action' : None
 }

# Isn't this part of your PR?
def setAction(action): # ns0:action
    '''
    Set Action
    '''
    Model.clientModel.service.set_action()

# Isn't this part of your PR?
def setActionCombination(
    no : int = 1,
    design_situation = None,
    items = [],
    active = None,
    construction_stage = None,
    combination_type = ActionCombinationItems.GENERAL,
    generated_load_combinations : list = [1,2],
    generated_result_combinations : list = [1,2],
    name : str = '',
    attribute_always_editable: str = '',
    comment: str = '',
    params: dict = None,
    model = Model):
    '''
    Set Action combination
    '''
    clientObject = model.clientModel.factory.create('ns0:action_combination')

    clientObject.no = no
    clientObject.design_situation = design_situation
    clientObject.items = items
    clientObject.active = active
    clientObject.construction_stage = construction_stage
    clientObject.combination_type = combination_type
    clientObject.generated_load_combinations = generated_load_combinations
    clientObject.generated_result_combinations = generated_result_combinations
    if name:
        clientObject.user_defined_name_enabled = True
        clientObject.name = name
    clientObject.attribute_always_editable = attribute_always_editable
    clientObject.comment = comment

    # Adding optional parameters via dictionary
    if params:
        for key in params:
            clientObject[key] = params[key]

    model.clientModel.service.set_action_combination(clientObject)


############ BOOKMARK ###################################################
def setBuildingStory(building_story): # ns0:building_story
    Model.clientModel.service.set_building_story(building_story)

def setClippingBox(clipping_box): # ns0:clipping_box
    Model.clientModel.service.set_clipping_box(clipping_box)

def setClippingPlane(clipping_plane): # ns0:clipping_plane
    Model.clientModel.service.set_clipping_plane(clipping_plane)

def setConstructionStage(construction_stag): # ns0:construction_stag
    Model.clientModel.service.set_construction_stage(construction_stag)

def setDesignSupport(design_situation): # ns0:design_situation
    Model.clientModel.service.set_design_support(design_situation)

def setDimension(dimension): # ns0:dimension
    Model.clientModel.service.set_dimension(dimension)

def setMemberRepresentative(member_representative): # ns0:member_representative
    Model.clientModel.service.set_member_representative(member_representative)

def setMemberSetRepresentative(member_set_representative): # ns0:member_set_representative
    Model.clientModel.service.set_member_set_representative(member_set_representative)

def setModelHistory(history): # ns0:array_of_model_history
    Model.clientModel.service.set_model_history(history)

def setObjectSnap(snap): #ns0:object_snap
    Model.clientModel.service.set_object_snap(snap)

def setPunchingReinforcement(punching_reinforcement): # ns0:punching_reinforcement
    Model.clientModel.service.set_punching_reinforcement(punching_reinforcement)

def setRelationshipBetweenLoadCases(relationship_between_load_cases): #ns0:relationship_between_load_cases
    Model.clientModel.service.set_relationship_between_load_cases(relationship_between_load_cases)

def setSelectedObjects(selected_objects): # ns0:object_location_array
    Model.clientModel.service.set_selected_objects(selected_objects)

def setSoilMassif(soil_massif): # ns0:soil_massif
    Model.clientModel.service.set_soil_massif(soil_massif)

def setSurfaceImperfection(imperfection_case_no, surface_imperfection): # ns0:surface_imperfection
    Model.clientModel.service.set_surface_imperfection(imperfection_case_no, surface_imperfection)

def setSurfaceSetImperfection(imperfection_case_no, surface_set_imperfection): # ns0:surface_set_imperfection
    Model.clientModel.service.set_surface_set_imperfection(imperfection_case_no, surface_set_imperfection)

def setTerrain(terrain): # ns0:terrain
    Model.clientModel.service.set_terrain(terrain)

def setVisualObject(visual_object): # ns0:visual_object
    Model.clientModel.service.set_visual_object(visual_object)

def setWindProfile(wind_profile): # ns0:wind_profile
    Model.clientModel.service.set_wind_profile(wind_profile)

def setWindSimulation(wind_simulation): # ns0:wind_simulation
    Model.clientModel.service.set_wind_simulation(wind_simulation)

def uniteNodesAndSupports(tolerance):
    Model.clientModel.service.unite_nodes_and_supports(tolerance)
