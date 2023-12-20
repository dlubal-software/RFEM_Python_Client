from RFEM import connectionGlobals
from RFEM.initModel import Model

###########################################
# Application functions
###########################################

"""
Additional functions missing in this file.
Date: 29/11/2023,
RFEM 6.04.0009.197.2f47af57c08


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

# Not tested, I need dxf file
def setDxfFileModelObject(dxf_file_model_object): # ns0:Dxf_file_model_object
    '''
    Set DXF import parameters
    '''
    Model.clientModel.service.set_Dxf_file_model_object(dxf_file_model_object)

# Not tested, I need dxf file
def setDxfModelObject(parent_no, dxf_model_object): # ns0:Dxf_model_object
    Model.clientModel.service.set_Dxf_model_object(parent_no, dxf_model_object)

############ BOOKMARK ###################################################
# Functions below are not tested yet, I am creating objects for them

# Type added to specialObjects.py
def setBuildingStory(building_story): # ns0:building_story
    '''
    Description
    '''
    Model.clientModel.service.set_building_story(building_story)

def setClippingBox(clipping_box): # ns0:clipping_box
    '''
    Description
    '''
    Model.clientModel.service.set_clipping_box(clipping_box)

def setClippingPlane(clipping_plane): # ns0:clipping_plane
    '''
    Description
    '''
    Model.clientModel.service.set_clipping_plane(clipping_plane)

def setConstructionStage(construction_stage): # ns0:construction_stage
    '''
    Description
    '''
    Model.clientModel.service.set_construction_stage(construction_stage)

def setDesignSupport(design_situation): # ns0:design_situation
    '''
    Description
    '''
    Model.clientModel.service.set_design_support(design_situation)

def setDimension(dimension): # ns0:dimension
    '''
    Description
    '''
    Model.clientModel.service.set_dimension(dimension)

def setMemberRepresentative(member_representative): # ns0:member_representative
    '''
    Description
    '''
    Model.clientModel.service.set_member_representative(member_representative)

def setMemberSetRepresentative(member_set_representative): # ns0:member_set_representative
    '''
    Description
    '''
    Model.clientModel.service.set_member_set_representative(member_set_representative)

def setModelHistory(history): # ns0:array_of_model_history
    '''
    Description
    '''
    Model.clientModel.service.set_model_history(history)

def setObjectSnap(snap): #ns0:object_snap
    '''
    Description
    '''
    Model.clientModel.service.set_object_snap(snap)

def setPunchingReinforcement(punching_reinforcement): # ns0:punching_reinforcement
    '''
    Description
    '''
    Model.clientModel.service.set_punching_reinforcement(punching_reinforcement)

def setRelationshipBetweenLoadCases(relationship_between_load_cases): #ns0:relationship_between_load_cases
    '''
    Description
    '''
    Model.clientModel.service.set_relationship_between_load_cases(relationship_between_load_cases)

def setSelectedObjects(selected_objects): # ns0:object_location_array
    '''
    Description
    '''
    Model.clientModel.service.set_selected_objects(selected_objects)

def setSoilMassif(soil_massif): # ns0:soil_massif
    '''
    Description
    '''
    Model.clientModel.service.set_soil_massif(soil_massif)

def setSurfaceImperfection(imperfection_case_no, surface_imperfection): # ns0:surface_imperfection
    '''
    Description
    '''
    Model.clientModel.service.set_surface_imperfection(imperfection_case_no, surface_imperfection)

def setSurfaceSetImperfection(imperfection_case_no, surface_set_imperfection): # ns0:surface_set_imperfection
    '''
    Description
    '''
    Model.clientModel.service.set_surface_set_imperfection(imperfection_case_no, surface_set_imperfection)

def setTerrain(terrain): # ns0:terrain
    '''
    Description
    '''
    Model.clientModel.service.set_terrain(terrain)

def setVisualObject(visual_object): # ns0:visual_object
    '''
    Description
    '''
    Model.clientModel.service.set_visual_object(visual_object)

def setWindProfile(wind_profile): # ns0:wind_profile
    '''
    Description
    '''
    Model.clientModel.service.set_wind_profile(wind_profile)

def setWindSimulation(wind_simulation): # ns0:wind_simulation
    '''
    Description
    '''
    Model.clientModel.service.set_wind_simulation(wind_simulation)

def uniteNodesAndSupports(tolerance):
    '''
    Description
    '''
    Model.clientModel.service.unite_nodes_and_supports(tolerance)

########## ADDED FUNCTIONS 30.11.2023 ###########
#################### SETTERS ####################

def SetAccelerogram(accelerogram): #ns0:accelerogram
    '''
    Description
    '''
    Model.clientModel.service.set_accelerogram(accelerogram)

def SetAluminumDesignSLSConfiguration(aluminum_design_sls_configuration): #ns0:aluminum_design_sls_configuration
    '''
    Description
    '''
    Model.clientModel.service.set_aluminum_design_sls_configuration(aluminum_design_sls_configuration)

def SetAluminumDesignULSConfiguration(aluminum_design_uls_configuration): # ns0:aluminum_design_uls_configuration
    '''
    Description
    '''
    Model.clientModel.service.set_aluminum_design_uls_configuration(aluminum_design_uls_configuration)

def SetBuildingGrid(building_grid): # ns0:building_grid
    '''
    Description
    '''
    Model.clientModel.service.set_building_grid(building_grid)

def SetCalculationDiagram(calculation_diagram): # ns0:calculation_diagram
    '''
    Description
    '''
    Model.clientModel.service.set_calculation_diagram(calculation_diagram)

def SetFloorSet(floor_set): # ns0:floor_set
    '''
    Description
    '''
    Model.clientModel.service.set_floor_set(floor_set)

def SetMemberOpenings(member_openings): # ns0:member_openings
    '''
    Description
    '''
    Model.clientModel.service.set_member_openings(member_openings)

def SetModelId(id): # xs:string id
    '''
    Description
    '''
    Model.clientModel.service.set_model_id(id)

def SetPushoverAnalysisSettings(pushover_analysis_settings): # ns0:pushover_analysis_settings
    '''
    Description
    '''
    Model.clientModel.service.set_pushover_analysis_settings(pushover_analysis_settings)

def SetShearWall(shear_wall): # ns0:shear_wall
    '''
    Description
    '''
    Model.clientModel.service.set_shear_wall(shear_wall)

def SetSteelDesignFRConfiguration(steel_design_fr_configuration): # ns0:steel_design_fr_configuration
    '''
    Description
    '''
    Model.clientModel.service.set_steel_design_fr_configuration(steel_design_fr_configuration)

def SetSteelDesignSeismicConfiguration(steel_design_seismic_configuration): # ns0:steel_design_seismic_configuration
    '''
    Description
    '''
    Model.clientModel.service.set_steel_design_seismic_configuration(steel_design_seismic_configuration)

def SetTimberDesignFRConfiguration(timber_design_fr_configuration): # ns0:timber_design_fr_configuration
    '''
    Description
    '''
    Model.clientModel.service.set_timber_design_fr_configuration(timber_design_fr_configuration)

def UseDetailedMemberResults(use): # xs:boolean use
    '''
    Description
    '''
    Model.clientModel.service.use_detailed_member_results(use)

def CalculateAllInCloud(machine_id, run_plausibility_check, calculate_despite_warnings_or_errors, email_notification): # xs:string machine_id, xs:boolean run_plausibility_check, xs:boolean calculate_despite_warnings_or_errors, xs:boolean email_notification
    '''
    Description
    '''
    Model.clientModel.service.calculate_all_in_cloud(machine_id, run_plausibility_check, calculate_despite_warnings_or_errors, email_notification)

def ExportToAsf(file_path, type_of_reinforcement, surfaces): #xs:string file_path, ns0:asf_export_data_type type_of_reinforcement, ns0:array_of_int surfaces
    '''
    Description
    '''
    Model.clientModel.service.export_to_asf(file_path, type_of_reinforcement, surfaces)

#################### GETTERS #####################

def GetCurrentProject():
    '''
    Description
    '''
    connectionGlobals.client.service.get_current_project()

def GetListOfExistingProjects():
    '''
    Description
    '''
    connectionGlobals.client.service.get_list_of_existing_projects()

def GetListOfExistingTemplates():
    '''
    Description
    '''
    connectionGlobals.client.service.get_list_of_existing_templates()

def GetModelListWithIndexes():
    '''
    Description
    '''
    connectionGlobals.client.service.get_model_list_with_indexes()

def GetProject(project_path): #xs:string project_path
    '''
    Description
    '''
    connectionGlobals.client.service.get_project(project_path)

def GetSettingsProgramLanguage():
    '''
    Description
    '''
    connectionGlobals.client.service.get_settings_program_language()

def GetTemplate(template_path): #xs:string template_path
    '''
    Description
    '''
    connectionGlobals.client.service.get_template(template_path)

def GetDXFFileModelObject(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_Dxf_file_model_object(no)

def GetDXFModelObject(no, parent_no): # xs:int no, xs:int parent_no
    '''
    Description
    '''
    Model.clientModel.service.get_Dxf_model_object(no, parent_no)

def GetAccelerogram(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_accelerogram(no)

def GetActionCategoriesForAction():
    '''
    Description
    '''
    Model.clientModel.service.get_action_categories_for_action()

def GetActionCategoriesForLoadCase():
    '''
    Description
    '''
    Model.clientModel.service.get_action_categories_for_load_case()

def GetAllAvailableMachinesInCloud():
    '''
    Description
    '''
    Model.clientModel.service.get_all_available_machines_in_cloud()

def GetAllSelectedObjects():
    '''
    Description
    '''
    Model.clientModel.service.get_all_selected_objects()

def GetAluminumDesignSLSConfiguration(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_aluminum_design_sls_configuration(no)

def GetAluminumDesignUlsConfiguration(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_aluminum_design_uls_configuration(no)

def GetBuildingGrid(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_building_grid(no)

def GetBuildingStory(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_building_story(no)

def GetCalculationDiagram(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_calculation_diagram(no)

def GetCalculationErrors():
    '''
    Description
    '''
    Model.clientModel.service.get_calculation_errors()

def GetClippingBox(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_clipping_box(no)

def GetClippingPlane(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_clipping_plane(no)

def GetConstructionStage(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_construction_stage(no)

def GetDesignSituationTypes():
    '''
    Description
    '''
    Model.clientModel.service.get_design_situation_types()

def GetDesignSupport(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_design_support(no)

def GetDimension(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_dimension(no)

def GetFloorSet(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_floor_set(no)

def GetGlobalParameter(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_global_parameter(no)

def GetMemberOpenings(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_member_openings(no)

def GetMemberRepresentative(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_member_representative(no)

def GetMemberSetRepresentative(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_member_set_representative(no)

def GetModelHistory():
    '''
    Description
    '''
    Model.clientModel.service.get_model_history()

def GetNthObjectNumber(types, order, parent_no): # ns0:object_types types, xs:int order, xs:int parent_no
    '''
    Description
    '''
    Model.clientModel.service.get_nth_object_number(types, order, parent_no)

def GetObjectCount(types, parent_no): # ns0:object_types types, xs:int parent_no
    '''
    Description
    '''
    Model.clientModel.service.get_object_count(types, parent_no)

def GetObjectInformation(types): # ns0:object_types types
    '''
    Description
    '''
    Model.clientModel.service.get_object_information(types)

def GetObjectSnap(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_object_snap(no)

def GetOptimizedValues():
    '''
    Description
    '''
    Model.clientModel.service.get_optimized_values()

def GetPartsListDeepBeamsByMaterial():
    '''
    Description
    '''
    Model.clientModel.service.get_parts_list_deep_beams_by_material()

def GetPartsListMemberSetRepresentativesByMaterial():
    '''
    Description
    '''
    Model.clientModel.service.get_parts_list_member_set_representatives_by_material()

def GetPartsListShearWallsByMaterial():
    '''
    Description
    '''
    Model.clientModel.service.get_parts_list_shear_walls_by_material()

def GetPunchingReinforcement(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_punching_reinforcement(no)

def GetPushoverAnalysisSettings(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_pushover_analysis_settings(no)

def GetRelationshipBetweenLoadCases(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_relationship_between_load_cases(no)

def GetShearWall(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_shear_wall(no)

def GetSoilMassif(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_soil_massif(no)

def GetSteelDesignFRConfiguration(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_steel_design_fr_configuration(no)

def GetSteelDesignSeismicConfiguration(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_steel_design_seismic_configuration(no)

def GetSurfaceImperfection(no, imperfection_case_no): # xs:int no, xs:int imperfection_case_no
    '''
    Description
    '''
    Model.clientModel.service.get_surface_imperfection(no, imperfection_case_no)

def GetSurfaceReleaseType(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_surface_release_type(no)

def GetSurfaceSetImperfection(no, imperfection_case_no): #xs:int no, xs:int imperfection_case_no
    '''
    Description
    '''
    Model.clientModel.service.get_surface_set_imperfection(no, imperfection_case_no)

def GetTerrain(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_terrain(no)

def GetTimberDesignFrConfiguration(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_timber_design_fr_configuration(no)

def GetVisualObject(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_visual_object(no)

def GetWindProfile(no): # xs:int no
    '''
    Description
    '''
    Model.clientModel.service.get_wind_profile(no)
