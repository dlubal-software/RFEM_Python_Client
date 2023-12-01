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

    connectionGlobals.client.service.calculate_specific(loadings, skip_warnings)

# Not tested, there is no set selection yet
def clearSelection():
    '''
    Empty selection
    '''
    connectionGlobals.client.service.clear_selection()

def deleteAll():
    '''
    Delete all objects
    '''
    connectionGlobals.client.service.delete_all()

# Not tested, because, when I modify the model nothing is added to the history, so I can't verify, if it works
def deleteAllHistory():
    '''
    Delete whole history
    '''
    connectionGlobals.client.service.delete_all_history()

def deleteAllResults(delete_mesh = True):
    '''
    Delete results

    Args:
        delete_mesh (bool): Put True if the mesh should be deleted
    '''
    connectionGlobals.client.service.delete_all_results(delete_mesh)

# Not tested, because I dont know what it should do
def divideByIntersections(member_list, line_list, surface_list):
    '''
    Divide by intersections

    Args:
        member_list (list): List of members
        line_list (list): List of lines
        surface_list (list): List of surfaces
    '''
    connectionGlobals.client.service.divide_by_intersections(member_list, line_list, surface_list)

# I think this function doesn't generate anything, so the name is wrong,
# and the validation also doesn't work - it returns Success on any file with .xml extension
def generateAndValidateXmlSolverInput(solver_input_file_path):
    '''
    Generate and validate XML input
    Returns result of validation

    Args:
        solver_input_file_path(str): Path to XML
    '''
    return connectionGlobals.client.service.generate_and_validate_xml_solver_input(solver_input_file_path)

# Don't know what this should produce, but neither LC or CO was generated
def generateLoadCasesAndCombinations():
    '''
    Generate load cases and combinations
    '''
    connectionGlobals.client.service.generate_load_cases_and_combinations()

def reset():
    '''
    Resets everything
    '''
    connectionGlobals.client.service.reset()

def runScript(script_file_path):
    '''
    Run JS script.

    Args:
        script_file_path (str): Path to JS script.
    '''
    connectionGlobals.client.service.run_script(script_file_path)


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
    connectionGlobals.client.service.set_Dxf_file_model_object(dxf_file_model_object)

# Not tested, I need dxf file
def setDxfModelObject(parent_no, dxf_model_object): # ns0:Dxf_model_object
    connectionGlobals.client.service.set_Dxf_model_object(parent_no, dxf_model_object)

############ BOOKMARK ###################################################

def setBuildingStory(building_story): # ns0:building_story
    '''
    Description
    '''
    connectionGlobals.client.service.set_building_story(building_story)

def setClippingBox(clipping_box): # ns0:clipping_box
    '''
    Description
    '''
    connectionGlobals.client.service.set_clipping_box(clipping_box)

def setClippingPlane(clipping_plane): # ns0:clipping_plane
    '''
    Description
    '''
    connectionGlobals.client.service.set_clipping_plane(clipping_plane)

def setConstructionStage(construction_stag): # ns0:construction_stag
    '''
    Description
    '''
    connectionGlobals.client.service.set_construction_stage(construction_stag)

def setDesignSupport(design_situation): # ns0:design_situation
    '''
    Description
    '''
    connectionGlobals.client.service.set_design_support(design_situation)

def setDimension(dimension): # ns0:dimension
    '''
    Description
    '''
    connectionGlobals.client.service.set_dimension(dimension)

def setMemberRepresentative(member_representative): # ns0:member_representative
    '''
    Description
    '''
    connectionGlobals.client.service.set_member_representative(member_representative)

def setMemberSetRepresentative(member_set_representative): # ns0:member_set_representative
    '''
    Description
    '''
    connectionGlobals.client.service.set_member_set_representative(member_set_representative)

def setModelHistory(history): # ns0:array_of_model_history
    '''
    Description
    '''
    connectionGlobals.client.service.set_model_history(history)

def setObjectSnap(snap): #ns0:object_snap
    '''
    Description
    '''
    connectionGlobals.client.service.set_object_snap(snap)

def setPunchingReinforcement(punching_reinforcement): # ns0:punching_reinforcement
    '''
    Description
    '''
    connectionGlobals.client.service.set_punching_reinforcement(punching_reinforcement)

def setRelationshipBetweenLoadCases(relationship_between_load_cases): #ns0:relationship_between_load_cases
    '''
    Description
    '''
    connectionGlobals.client.service.set_relationship_between_load_cases(relationship_between_load_cases)

def setSelectedObjects(selected_objects): # ns0:object_location_array
    '''
    Description
    '''
    connectionGlobals.client.service.set_selected_objects(selected_objects)

def setSoilMassif(soil_massif): # ns0:soil_massif
    '''
    Description
    '''
    connectionGlobals.client.service.set_soil_massif(soil_massif)

def setSurfaceImperfection(imperfection_case_no, surface_imperfection): # ns0:surface_imperfection
    '''
    Description
    '''
    connectionGlobals.client.service.set_surface_imperfection(imperfection_case_no, surface_imperfection)

def setSurfaceSetImperfection(imperfection_case_no, surface_set_imperfection): # ns0:surface_set_imperfection
    '''
    Description
    '''
    connectionGlobals.client.service.set_surface_set_imperfection(imperfection_case_no, surface_set_imperfection)

def setTerrain(terrain): # ns0:terrain
    '''
    Description
    '''
    connectionGlobals.client.service.set_terrain(terrain)

def setVisualObject(visual_object): # ns0:visual_object
    '''
    Description
    '''
    connectionGlobals.client.service.set_visual_object(visual_object)

def setWindProfile(wind_profile): # ns0:wind_profile
    '''
    Description
    '''
    connectionGlobals.client.service.set_wind_profile(wind_profile)

def setWindSimulation(wind_simulation): # ns0:wind_simulation
    '''
    Description
    '''
    connectionGlobals.client.service.set_wind_simulation(wind_simulation)

def uniteNodesAndSupports(tolerance):
    '''
    Description
    '''
    connectionGlobals.client.service.unite_nodes_and_supports(tolerance)

########## ADDED FUNCTIONS 30.11.2023 ###########
#################### SETTERS ####################

def SetAccelerogram():
    '''
    Description
    '''
    connectionGlobals.client.service.set_accelerogram()

def SetAluminumDesignSLSConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.set_aluminum_design_sls_configuration()

def SetAluminumDesignULSConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.set_aluminum_design_uls_configuration()

def SetBuildingGrid():
    '''
    Description
    '''
    connectionGlobals.client.service.set_building_grid()

def SetCalculationDiagram():
    '''
    Description
    '''
    connectionGlobals.client.service.set_calculation_diagram()

def SetFloorSet():
    '''
    Description
    '''
    connectionGlobals.client.service.set_floor_set()

def SetMemberOpenings():
    '''
    Description
    '''
    connectionGlobals.client.service.set_member_openings()

def SetModelId():
    '''
    Description
    '''
    connectionGlobals.client.service.set_model_id()

def SetPushoverAnalysisSettings():
    '''
    Description
    '''
    connectionGlobals.client.service.set_pushover_analysis_settings()

def SetShearWall():
    '''
    Description
    '''
    connectionGlobals.client.service.set_shear_wall()

def SetSteelDesignFRConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.set_steel_design_fr_configuration()

def SetSteelDesignSeismicConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.set_steel_design_seismic_configuration()

def SetTimberDesignFRConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.set_timber_design_fr_configuration()

def UseDetailedMemberResults():
    '''
    Description
    '''
    connectionGlobals.client.service.use_detailed_member_results()

def CalculateAllInCloud():
    '''
    Description
    '''
    connectionGlobals.client.service.calculate_all_in_cloud()

def ExportToAsf():
    '''
    Description
    '''
    connectionGlobals.client.service.export_to_asf()

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

def GetProject():
    '''
    Description
    '''
    connectionGlobals.client.service.get_project()

def GetSettingsProgramLanguage():
    '''
    Description
    '''
    connectionGlobals.client.service.get_settings_program_language()

def GetTemplate():
    '''
    Description
    '''
    connectionGlobals.client.service.get_template()

def GetDXFFileModelObject():
    '''
    Description
    '''
    connectionGlobals.client.service.get_Dxf_file_model_object()

def GetDXFModelObject():
    '''
    Description
    '''
    connectionGlobals.client.service.get_Dxf_model_object()

def GetAccelerogram():
    '''
    Description
    '''
    connectionGlobals.client.service.get_accelerogram()

def GetActionCategoriesForAction():
    '''
    Description
    '''
    connectionGlobals.client.service.get_action_categories_for_action()

def GetActionCategoriesForLoadCase():
    '''
    Description
    '''
    connectionGlobals.client.service.get_action_categories_for_load_case()

def GetAllAvailableMachinesInCloud():
    '''
    Description
    '''
    connectionGlobals.client.service.get_all_available_machines_in_cloud()

def GetAllSelectedObjects():
    '''
    Description
    '''
    connectionGlobals.client.service.get_all_selected_objects()

def GetAluminumDesignSLSConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.get_aluminum_design_sls_configuration()

def GetAluminumDesignUlsConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.get_aluminum_design_uls_configuration()

def GetBuildingGrid():
    '''
    Description
    '''
    connectionGlobals.client.service.get_building_grid()

def GetBuildingStory():
    '''
    Description
    '''
    connectionGlobals.client.service.get_building_story()

def GetCalculationDiagram():
    '''
    Description
    '''
    connectionGlobals.client.service.get_calculation_diagram()

def GetCalculationErrors():
    '''
    Description
    '''
    connectionGlobals.client.service.get_calculation_errors()

def GetClippingBox():
    '''
    Description
    '''
    connectionGlobals.client.service.get_clipping_box()

def GetClippingPlane():
    '''
    Description
    '''
    connectionGlobals.client.service.get_clipping_plane()

def GetConstructionStage():
    '''
    Description
    '''
    connectionGlobals.client.service.get_construction_stage()

def GetDesignSituationTypes():
    '''
    Description
    '''
    connectionGlobals.client.service.get_design_situation_types()

def GetDesignSupport():
    '''
    Description
    '''
    connectionGlobals.client.service.get_design_support()

def GetDimension():
    '''
    Description
    '''
    connectionGlobals.client.service.get_dimension()

def GetFloorSet():
    '''
    Description
    '''
    connectionGlobals.client.service.get_floor_set()

def GetGlobalParameter():
    '''
    Description *
    '''
    connectionGlobals.client.service.get_global_parameter()

def GetMemberOpenings():
    '''
    Description
    '''
    connectionGlobals.client.service.get_member_openings()

def GetMemberRepresentative():
    '''
    Description
    '''
    connectionGlobals.client.service.get_member_representative()

def GetMemberSetRepresentative():
    '''
    Description
    '''
    connectionGlobals.client.service.get_member_set_representative()

def GetModelHistory():
    '''
    Description
    '''
    connectionGlobals.client.service.get_model_history()

def GetNthObjectNumber():
    '''
    Description
    '''
    connectionGlobals.client.service.get_nth_object_number()

def GetObjectCount():
    '''
    Description
    '''
    connectionGlobals.client.service.get_object_count()

def GetObjectInformation():
    '''
    Description
    '''
    connectionGlobals.client.service.get_object_information()

def GetObjectSnap():
    '''
    Description
    '''
    connectionGlobals.client.service.get_object_snap()

def GetOptimizedValues():
    '''
    Description
    '''
    connectionGlobals.client.service.get_optimized_values()

def GetPartsListDeepBeamsByMaterial():
    '''
    Description
    '''
    connectionGlobals.client.service.get_parts_list_deep_beams_by_material()

def GetPartsListMemberSetRepresentativesByMaterial():
    '''
    Description
    '''
    connectionGlobals.client.service.get_parts_list_member_set_representatives_by_material()

def GetPartsListShearWallsByMaterial():
    '''
    Description
    '''
    connectionGlobals.client.service.get_parts_list_shear_walls_by_material()

def GetPunchingReinforcement():
    '''
    Description
    '''
    connectionGlobals.client.service.get_punching_reinforcement()

def GetPushoverAnalysisSettings():
    '''
    Description
    '''
    connectionGlobals.client.service.get_pushover_analysis_settings()

def GetRelationshipBetweenLoadCases():
    '''
    Description
    '''
    connectionGlobals.client.service.get_relationship_between_load_cases()

def GetShearWall():
    '''
    Description
    '''
    connectionGlobals.client.service.get_shear_wall()

def GetSoilMassif():
    '''
    Description
    '''
    connectionGlobals.client.service.get_soil_massif()

def GetSteelDesignFRConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.get_steel_design_fr_configuration()

def GetSteelDesignSeismicConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.get_steel_design_seismic_configuration()

def GetSurfaceImperfection():
    '''
    Description
    '''
    connectionGlobals.client.service.get_surface_imperfection()

def GetSurfaceReleaseType():
    '''
    Description
    '''
    connectionGlobals.client.service.get_surface_release_type()

def GetSurfaceSetImperfection():
    '''
    Description
    '''
    connectionGlobals.client.service.get_surface_set_imperfection()

def GetTerrain():
    '''
    Description
    '''
    connectionGlobals.client.service.get_terrain()

def GetTimberDesignFrConfiguration():
    '''
    Description
    '''
    connectionGlobals.client.service.get_timber_design_fr_configuration()

def GetVisualObject():
    '''
    Description
    '''
    connectionGlobals.client.service.get_visual_object()

def GetWindProfile():
    '''
    Description
    '''
    connectionGlobals.client.service.get_wind_profile()
