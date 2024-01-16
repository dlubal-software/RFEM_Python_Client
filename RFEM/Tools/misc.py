from RFEM import connectionGlobals
from RFEM.initModel import Model
from RFEM.tools.complexTypes import *
from RFEM.enums import ObjectTypes, ProgramLanguage, ASFExportDataType

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
# TODO: bug 158867
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

def newTemplate(template_info): #ns0:project_info
    '''
    Create new template
    TODO: project_info doesn't exist says WS

    Args:
        template_info
    '''
    connectionGlobals.client.service.new_template(template_info)

def saveModel(model_index):
    '''
    Saving existing model from application side by idex starting from 0

    Args:
        model_index (int): Index of model to be saved
    '''
    connectionGlobals.client.service.save_model(model_index)

def SetAsCurrentProject(project_path):
    '''
    Setting open model as active

    Args:
        project_path (str): Path to model which should be set as current
    '''
    connectionGlobals.client.service.set_as_current_project(project_path)

def SetDetailedLogging(logging=True):
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
def SetSettingsProgramLanguage(language:ProgramLanguage):
    '''
    Set program language
    TODO: set_settings_program_language doesn't work.
          The option in the settings does not change,
          nor does a message about change being applied after restart pop up.

    Args:
        language (enum ProgramLanguage): Program language
    '''
    connectionGlobals.client.service.set_settings_program_language(language)

###########################################
# Model functions
############################################

def calculateSpecific(loadings, skip_warnings=True):
    '''
    Calculate specified loadings. Equals to 'To Calculate' in RFEM.

    TODO: It is not clear in what format the loadings parameter should be set.
          Is it list of integers or list of strings? Putting any kind of load case for example returns same result:
          (calculation_result){
          succeeded = True
          errors_and_warnings = ""
          messages = None}

          which I question if it is correct, because I don't see any results.
          Also I see no calculation process in RFEM. In this case 'succeeded' parameter should be False and have some message.

    Args:
        loadings (list of strings): List of loadings
        skip_warnings (bool): Set to True if warnings should be skipped
    '''

    Model.clientModel.service.calculate_specific(loadings, skip_warnings)

def clearSelection():
    '''
    Clears the selection of objects
    '''
    Model.clientModel.service.clear_selection()

def deleteAll():
    '''
    Delete all objects
    '''
    Model.clientModel.service.delete_all()

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

def divideByIntersections(member_list, line_list, surface_list):
    '''
    Divide by intersections

    Args:
        member_list (list): List of members
        line_list (list): List of lines
        surface_list (list): List of surfaces
    '''
    Model.clientModel.service.divide_by_intersections(member_list, line_list, surface_list)

def generateAndValidateXmlSolverInput(target_file_path):
    '''
    Generate and validate XML solver input
    Returns generate_and_validate_xml_solver_input_result containing parameters: succeeded, result, and messages.

    Args:
        target_file_path(str): Path to XML
    '''
    return Model.clientModel.service.generate_and_validate_xml_solver_input(target_file_path)

def generateLoadCasesAndCombinations():
    '''
    Generate load cases and combinations
    TODO: Don't know if or how this works.
    '''
    Model.clientModel.service.generate_load_cases_and_combinations()

def reset():
    '''
    Reset everything
    '''
    Model.clientModel.service.reset()

def runScript(script_file_path):
    '''
    Run JS script

    Args:
        script_file_path (str): Path to JS script.
    '''
    Model.clientModel.service.run_script(script_file_path)

def UniteNodesAndSupports(tolerance:float):
    '''
    Unite Nodes And Supports

    Args:
        tolerance (float): Tolerance
    '''
    Model.clientModel.service.unite_nodes_and_supports(tolerance)

def UseDetailedMemberResults(use:bool):
    '''
    Set Use Detailed Member Results

    Args:
        use (bool): If to use detailed member results
    '''
    Model.clientModel.service.use_detailed_member_results(use)

def CalculateAllInCloud(machine_id:str, run_plausibility_check:bool, calculate_despite_warnings_or_errors:bool, email_notification:bool):
    '''
    Calculate All In Cloud

    Args:
        machine_id (str):
        run_plausibility_check (bool):
        calculate_despite_warnings_or_errors (bool):
        email_notification (bool):
    '''
    Model.clientModel.service.calculate_all_in_cloud(machine_id, run_plausibility_check, calculate_despite_warnings_or_errors, email_notification)

def ExportToAsf(file_path:str, type_of_reinforcement:ASFExportDataType, surfaces:list):
    '''
    Export to ASF

    Args:
        file_path (str): Path to target file
        type_of_reinforcement (enum): Enum of available types for ASF export data.
        surfaces (list of integers): List of surfaces
    '''
    Model.clientModel.service.export_to_asf(file_path, type_of_reinforcement, surfaces)


#################### SETTERS ####################


def SetDxfFileModelObject(dxf_file_model_object:DxfFileModelObject):
    '''
    Set DXF import parameters

    Args:
        dxf_file_model_object (DxfFileModelObject): Complex Type
    '''
    Model.clientModel.service.set_Dxf_file_model_object(dxf_file_model_object)

def SetDxfModelObject(parent_no, dxf_model_object):
    '''
    Set Dxf Model Object

    Args:
    '''
    Model.clientModel.service.set_Dxf_model_object(parent_no, dxf_model_object)

def SetBuildingStory(building_story:BuildingStory):
    '''
    Set Building Story
    '''
    Model.clientModel.service.set_building_story(building_story)

def SetClippingBox(clipping_box:ClippingBox):
    '''
    Set Clipping Box
    '''
    Model.clientModel.service.set_clipping_box(clipping_box)

def SetClippingPlane(clipping_plane:ClippingPlane):
    '''
    Set Clipping Plane
    '''
    Model.clientModel.service.set_clipping_plane(clipping_plane)

def SetConstructionStage(construction_stage:ConstructionStage):
    '''
    Set Construction Stage
    '''
    Model.clientModel.service.set_construction_stage(construction_stage)

def SetDesignSupport(design_support:DesignSupport):
    '''
    Set Design Support
    '''
    Model.clientModel.service.set_design_support(design_support)

def SetDimension(dimension:Dimension):
    '''
    Set Dimension
    '''
    Model.clientModel.service.set_dimension(dimension)

def SetMemberRepresentative(member_representative:MemberRepresentative):
    '''
    Set Member Representative
    '''
    Model.clientModel.service.set_member_representative(member_representative)

def SetMemberSetRepresentative(member_set_representative:MemberSetRepresentative):
    '''
    Set Member Set Representative
    '''
    Model.clientModel.service.set_member_set_representative(member_set_representative)

def SetModelHistory(history:ArrayOfModelHistory):
    '''
    Set Model History
    '''
    Model.clientModel.service.set_model_history(history)

def SetObjectSnap(snap:ObjectSnap):
    '''
    Set Object Snap
    '''
    Model.clientModel.service.set_object_snap(snap)

def SetPunchingReinforcement(punching_reinforcement:PunchingReinforcement):
    '''
    Set Punching Reinforcement
    '''
    Model.clientModel.service.set_punching_reinforcement(punching_reinforcement)

def SetRelationshipBetweenLoadCases(relationship_between_load_cases:RelationshipBetweenLoadCases):
    '''
    Set Relationship Between Load Cases
    '''
    Model.clientModel.service.set_relationship_between_load_cases(relationship_between_load_cases)

def SetSelectedObjects(selected_objects:ObjectLocationArray):
    '''
    Set Selected Objects
    '''
    Model.clientModel.service.set_selected_objects(selected_objects)

def SetSoilMassif(soil_massif:SoilMassif):
    '''
    Set Soil Massif
    '''
    Model.clientModel.service.set_soil_massif(soil_massif)

def SetSurfaceImperfection(imperfection_case_no, surface_imperfection:SurfaceImperfection):
    '''
    Set Surface Imperfection
    '''
    Model.clientModel.service.set_surface_imperfection(imperfection_case_no, surface_imperfection)

def SetSurfaceSetImperfection(imperfection_case_no, surface_set_imperfection:SurfaceSetImperfection):
    '''
    Set Surface Set Imperfection
    '''
    Model.clientModel.service.set_surface_set_imperfection(imperfection_case_no, surface_set_imperfection)

def SetTerrain(terrain:Terrain):
    '''
    Set Terrain
    '''
    Model.clientModel.service.set_terrain(terrain)

def SetVisualObject(visual_object:VisualObject):
    '''
    Set Visual Object
    '''
    Model.clientModel.service.set_visual_object(visual_object)

def SetWindProfile(wind_profile:WindProfile):
    '''
    Set Wind Profile
    '''
    Model.clientModel.service.set_wind_profile(wind_profile)

def SetWindSimulation(wind_simulation:WindSimulation):
    '''
    Set Wind Simulation
    '''
    Model.clientModel.service.set_wind_simulation(wind_simulation)

def SetAccelerogram(accelerogram:Accelerogram):
    '''
    Set Accelerogram
    '''
    Model.clientModel.service.set_accelerogram(accelerogram)

def SetBuildingGrid(building_grid:BuildingGrid):
    '''
    Set Building Grid
    '''
    Model.clientModel.service.set_building_grid(building_grid)

def SetCalculationDiagram(calculation_diagram:CalculationDiagram):
    '''
    Set Calculation Diagram
    '''
    Model.clientModel.service.set_calculation_diagram(calculation_diagram)

def SetFloorSet(floor_set:FloorSet):
    '''
    Set Floor Set
    '''
    Model.clientModel.service.set_floor_set(floor_set)

def SetMemberOpenings(member_openings:MemberOpenings):
    '''
    Set Member Openings
    '''
    Model.clientModel.service.set_member_openings(member_openings)

def SetModelID(id:str):
    '''
    Set Model ID
    '''
    Model.clientModel.service.set_model_id(id)

def SetPushoverAnalysisSettings(pushover_analysis_settings:GetPushoverAnalysisSettings):
    '''
    Set Pushover Analysis Settings
    '''
    Model.clientModel.service.set_pushover_analysis_settings(pushover_analysis_settings)

def SetShearWall(shear_wall:ShearWall):
    '''
    Set Shear Wall
    '''
    Model.clientModel.service.set_shear_wall(shear_wall)

def SetSteelDesignFRConfiguration(steel_design_fr_configuration:SteelDesignFrConfiguration):
    '''
    Set Steel Design FR Configuration
    '''
    Model.clientModel.service.set_steel_design_fr_configuration(steel_design_fr_configuration)

def SetSteelDesignSeismicConfiguration(steel_design_seismic_configuration:SteelDesignSeismicConfiguration):
    '''
    Set Steel Design Seismic Configuration
    '''
    Model.clientModel.service.set_steel_design_seismic_configuration(steel_design_seismic_configuration)

def SetTimberDesignFRConfiguration(timber_design_fr_configuration:TimberDesignFrConfiguration):
    '''
    Set Timber Design FR Configuration
    '''
    Model.clientModel.service.set_timber_design_fr_configuration(timber_design_fr_configuration)


#################### GETTERS #####################


def GetCurrentProject():
    '''
    Get Current Project
    TODO: "Server raised fault: 'Current project does not exist.'"
    '''
    connectionGlobals.client.service.get_current_project()

def GetListOfExistingProjects():
    '''
    Get List Of Existing Projects
    TODO: the result is empty
    '''
    connectionGlobals.client.service.get_list_of_existing_projects()

def GetListOfExistingTemplates():
    '''
    Get List Of Existing Templates
    TODO: the result is empty
    '''
    connectionGlobals.client.service.get_list_of_existing_templates()

def GetModelListWithIndexes():
    '''
    Get Model List With Indexes
    '''
    connectionGlobals.client.service.get_model_list_with_indexes()

def GetProject(project_path): #xs:string project_path
    '''
    Get Project
    TODO: ivalid file path
    '''
    connectionGlobals.client.service.get_project(project_path)

def GetSettingsProgramLanguage():
    '''
    Get Settings Program Language
    '''
    connectionGlobals.client.service.get_settings_program_language()

def GetTemplate(template_path): #xs:string template_path
    '''
    Get Template
    TODO: Invalid file path 'D:/BuildMaster/grandmaster/grandmaster_b234034_038703b7d8a/models/TestModel.ft6
    '''
    connectionGlobals.client.service.get_template(template_path)

def GetDXFFileModelObject(no): # xs:int no
    '''
    Get DXF File Model Object
    TODO: Do not know how this function works. I think there is missing paramter called 'path'.
    '''
    Model.clientModel.service.get_Dxf_file_model_object(no)

def GetDXFModelObject(no, parent_no): # xs:int no, xs:int parent_no
    '''
    Get DXF Model Object
    TODO: Do not know how this function works.
    '''
    Model.clientModel.service.get_Dxf_model_object(no, parent_no)

def GetAccelerogram(no): # xs:int no
    '''
    Get Accelerogram
    TODO: Not tested. Don't know which Add-on should be used. Harmonic Response Anaylsis is disabled.
    '''
    Model.clientModel.service.get_accelerogram(no)

def GetActionCategoriesForAction():
    '''
    Get all Action Categories for Action
    '''
    Model.clientModel.service.get_action_categories_for_action()

def GetActionCategoriesForLoadCase():
    '''
    Get all Action Categories for Load Cases
    '''
    Model.clientModel.service.get_action_categories_for_load_case()

def GetAllAvailableMachinesInCloud():
    '''
    Get list of available machines
    '''
    Model.clientModel.service.get_all_available_machines_in_cloud()

def GetAllSelectedObjects():
    '''
    Get list of selected objects, their type and no.
    '''
    Model.clientModel.service.get_all_selected_objects()

def GetAluminumDesignSLSConfiguration(no):
    '''
    Get Aluminum Design SLS Configuration
    '''
    Model.clientModel.service.get_aluminum_design_sls_configuration(no)

def GetAluminumDesignULSConfiguration(no):
    '''
    Get Aluminum Design ULS Configuration
    '''
    Model.clientModel.service.get_aluminum_design_uls_configuration(no)

def GetBuildingGrid(no): # xs:int no
    '''
    Get Building Grid
    TODO: Not tested. Don't know what it is.
    '''
    Model.clientModel.service.get_building_grid(no)

def GetBuildingStory(no):
    '''
    Get building story
    '''
    Model.clientModel.service.get_building_story(no)

def GetCalculationDiagram(no):
    '''
    Get Calculation Diagram
    TODO: Not tested. Don't know what it is.
    '''
    Model.clientModel.service.get_calculation_diagram(no)

def GetCalculationErrors():
    '''
    Get Calculation Errors
    '''
    Model.clientModel.service.get_calculation_errors()

def GetClippingBox(no):
    '''
    Get Clipping Box
    '''
    Model.clientModel.service.get_clipping_box(no)

def GetClippingPlane(no):
    '''
    Get Clipping Plane
    '''
    Model.clientModel.service.get_clipping_plane(no)

def GetConstructionStage(no):
    '''
    Get Construction Stage
    '''
    Model.clientModel.service.get_construction_stage(no)

def GetDesignSituationTypes():
    '''
    Get list of all Design Situation Types
    '''
    Model.clientModel.service.get_design_situation_types()

def GetDesignSupport(no):
    '''
    Get Design Support
    '''
    Model.clientModel.service.get_design_support(no)

def GetDimension(no):
    '''
    Get Dimension
    '''
    Model.clientModel.service.get_dimension(no)

def GetFloorSet(no):
    '''
    Get Floor Set
    '''
    Model.clientModel.service.get_floor_set(no)

def GetGlobalParameter(no):
    '''
    Get Global Parameter
    '''
    Model.clientModel.service.get_global_parameter(no)

def GetMemberOpenings(no):
    '''
    Get Member Openings
    '''
    Model.clientModel.service.get_member_openings(no)

def GetMemberRepresentative(no):
    '''
    Get Member Representative
    '''
    Model.clientModel.service.get_member_representative(no)

def GetMemberSetRepresentative(no):
    '''
    Get Member Set Representative
    '''
    Model.clientModel.service.get_member_set_representative(no)

def GetModelHistory():
    '''
    Get Model History
    '''
    Model.clientModel.service.get_model_history()

def GetNthObjectNumber(types:ObjectTypes, order:int, parent_no:int):
    '''
    Get Nth Object Number
    '''
    Model.clientModel.service.get_nth_object_number(types, order, parent_no)

def GetObjectCount(types:ObjectTypes, parent_no:int):
    '''
    Get Count of objects given by type
    '''
    Model.clientModel.service.get_object_count(types, parent_no)

def GetObjectInformation(types:ObjectTypes):
    '''
    Get Object Information
    '''
    Model.clientModel.service.get_object_information(types)

def GetObjectSnap(no):
    '''
    Get Object Snap
    '''
    Model.clientModel.service.get_object_snap(no)

def GetOptimizedValues():
    '''
    Get Optimized Values
    '''
    Model.clientModel.service.get_optimized_values()

def GetPartsListDeepBeamsByMaterial():
    '''
    Get Parts List Deep Beams By Material
    '''
    Model.clientModel.service.get_parts_list_deep_beams_by_material()

def GetPartsListMemberSetRepresentativesByMaterial():
    '''
    Get Parts List Member Set Representatives By Material
    '''
    Model.clientModel.service.get_parts_list_member_set_representatives_by_material()

def GetPartsListShearWallsByMaterial():
    '''
    Get Parts List Shear Walls By Material
    '''
    Model.clientModel.service.get_parts_list_shear_walls_by_material()

def GetPunchingReinforcement(no):
    '''
    Get Punching Reinforcement
    '''
    Model.clientModel.service.get_punching_reinforcement(no)

def GetPushoverAnalysisSettings(no):
    '''
    Get Pushover Analysis Settings
    '''
    Model.clientModel.service.get_pushover_analysis_settings(no)

def GetRelationshipBetweenLoadCases(no):
    '''
    Get Relationship Between Load Cases
    '''
    Model.clientModel.service.get_relationship_between_load_cases(no)

def GetShearWall(no):
    '''
    Get Shear Wall
    '''
    Model.clientModel.service.get_shear_wall(no)

def GetSoilMassif(no):
    '''
    Get Soil Massif
    '''
    Model.clientModel.service.get_soil_massif(no)

def GetSteelDesignFRConfiguration(no): # xs:int no
    '''
    Get Steel Design FR Configuration
    '''
    Model.clientModel.service.get_steel_design_fr_configuration(no)

def GetSteelDesignSeismicConfiguration(no):
    '''
    Get Steel Design Seismic Configuration
    '''
    Model.clientModel.service.get_steel_design_seismic_configuration(no)

def GetSurfaceImperfection(no:int, imperfection_case_no:int):
    '''
    Get Surface Imperfection
    '''
    Model.clientModel.service.get_surface_imperfection(no, imperfection_case_no)

def GetSurfaceReleaseType(no):
    '''
    Get Surface Release Type
    '''
    Model.clientModel.service.get_surface_release_type(no)

def GetSurfaceSetImperfection(no:int, imperfection_case_no:int):
    '''
    Get Surface Set Imperfection
    '''
    Model.clientModel.service.get_surface_set_imperfection(no, imperfection_case_no)

def GetTerrain(no):
    '''
    Get Terrain
    '''
    Model.clientModel.service.get_terrain(no)

def GetTimberDesignFRConfiguration(no):
    '''
    Get Timber Design FR Configuration
    '''
    Model.clientModel.service.get_timber_design_fr_configuration(no)

def GetVisualObject(no):
    '''
    Get Visual Object
    '''
    Model.clientModel.service.get_visual_object(no)

def GetWindProfile(no):
    '''
    Get Wind Profile
    '''
    Model.clientModel.service.get_wind_profile(no)
