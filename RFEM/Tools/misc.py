from RFEM.BasicObjects.member import Member
from RFEM.initModel import Model
from RFEM.enums import ActionType, ImposedLoadCategory, ActionCombinationItems
from RFEM import connectionGlobals

###########################################
# Application functions
###########################################

def closeApplication():
    '''
    Close RFEM/RSTAB app
    '''
    connectionGlobals.client.service.close_application()

def closeModel(model_index, save_changes = True):
    '''
    Close model at given index
    Args:
        model_index (int): Index
        save_changes (bool): True by default
    '''
    connectionGlobals.client.service.close_model(model_index, save_changes)

def deleteProject(projectPath):
    '''
    Delete project
    '''
    connectionGlobals.client.service.delete_project(projectPath)

def newModel(model_name):
    '''
    Create new model

    Args:
        model_name(str): Model name
    '''
    connectionGlobals.client.service.new_model(model_name)

def newModelAsCopy(model_name, file_path):
    '''
    Create new model as copy

    Args:
        model_name (str): Name of the model
        file_path (str): Path to the file
    '''
    connectionGlobals.client.service.new_model_as_copy(model_name, file_path)

def newModelFromTemplate(model_name, file_path):
    '''
    Create newmodel from template

    Args:
        model_name (str): Name of the model
        file_path (str): Path to the file
    '''
    connectionGlobals.client.service.new_model_from_template(model_name, file_path)

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

def newTemplate(template_info): #ns0:template_info doesn't work
    '''
    Create new template

    Args:
        template_info
    '''
    connectionGlobals.client.service.new_template(template_info)

def openModel(model_path):
    '''
    Open existing model

    Args:
        model_path (str): Path to model
    '''
    connectionGlobals.client.service.open_model(model_path)

def saveModel(model_index):
    '''
    Save model

    Args:
        model_index (int): Index of model to be saved
    '''
    connectionGlobals.client.service.save_model(model_index)

def setAsCurrentProject(project_path):
    connectionGlobals.client.service.set_as_current_project(project_path)

def setDetailedLogging(logging = True):
    '''
    Enable detailed logging

    Args:
        logging (bool): Enable or disable detailed logging
    '''
    connectionGlobals.client.service.set_detailed_logging(logging)

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

def beginModification(modification_name):
    '''
    Begin modification.
    Needs to be set before settingnew values to RFEM.
    Modifications take place after executing finishModification (finish_modification).

    Args:
        modification_name (str): name of the modification. Not significant.
    '''
    Model.clientModel.service.begin_modification(modification_name)

def calculateSpecific(loadings, skip_warnings = True): #ns0:calculate_specific_loadings, list
    '''
    Calculate specified loadings

    Args:
        loadings (list): List of loadings
        skip_warnings (bool): Set to True if warnings should be skipped
    '''

    Model.clientModel.service.calculate_specific(loadings, skip_warnings)

def cancelModification():
    '''
    Abort modification
    '''
    Model.clientModel.service.cancel_modification()

def clearSelection():
    '''
    Empty selection
    '''
    Model.clientModel.service.clear_selection()

def closeConnection():
    '''
    Terminate connection to server(RFEM/RSTAB)
    '''
    Model.clientModel.service.close_connection()

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

def finishModification():
    '''
    Finish modification i.e. apply all changes.
    '''
    Model.clientModel.service.finish_modification()

def generateAndValidateXmlSolverInput(solver_input_file_path):
    '''
    Generate and validate XML input

    Args:
        solver_input_file_path(str): Path to XML
    '''
    Model.clientModel.service.generate_and_validate_xml_solver_input(solver_input_file_path)

def generateLoadCasesAndCombinations():
    '''
    Generate load cases and combinations
    '''
    Model.clientModel.service.generate_load_cases_and_combinations()

def reset():
    '''
    Needs no introduction.
    '''
    Model.clientModel.service.reset()

def runScript(script_file_path):
    '''
    Run JS script.

    Args:
        script_file_path (str): Path to JS script.
    '''
    Model.clientModel.service.run_script(script_file_path)

def save(file_path):
    '''
    Save As...

    Args:
        file_path (str): Path to the file
    '''
    Model.clientModel.service.save(file_path)

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

def setDxfFileModelObject(dxf_file_model_object): # ns0:Dxf_file_model_object
    '''
    Set DXF import parameters
    '''
    Model.clientModel.service.set_Dxf_file_model_object(dxf_file_model_object)

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

def setAction(action): # ns0:action
    '''
    Set Action
    '''
    Model.clientModel.service.set_action()

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



def setBorehole(bore_hole): # ns0:borehole
    Model.clientModel.service.set_borehole(bore_hole)

def setBuildingStory(building_story): # ns0:building_story
    Model.clientModel.service.set_building_story(building_story)

def setClippingBox(clipping_box): # ns0:clipping_box
    Model.clientModel.service.set_clipping_box(clipping_box)

def setClippingPlane(clipping_plane): # ns0:clipping_plane
    Model.clientModel.service.set_clipping_plane(clipping_plane)

def setCombinationWizard(combination_wizard): # ns0:combination_wizard
    Model.clientModel.service.set_combination_wizard(combination_wizard)

def setConstructionStage(construction_stag): # ns0:construction_stag
    Model.clientModel.service.set_construction_stage(construction_stag)

def setCoordinateSystem(coordinate_system): # ns0:coordinate_system
    Model.clientModel.service.set_coordinate_system(coordinate_system)

def setDesignSupport(design_situation): # ns0:design_situation
    Model.clientModel.service.set_design_support(design_situation)

def setDimension(dimension): # ns0:dimension
    Model.clientModel.service.set_dimension(dimension)

def setLineGrid(line_grid): #ns0:line_grid
    Model.clientModel.service.set_line_grid(line_grid)

def setLoadCasesAndCombinations(load_cases_and_combinations): # ns0:load_cases_and_combinations
    Model.clientModel.service.set_load_cases_and_combinations(load_cases_and_combinations)

def setMainObjectsToActivate(main_objects_to_activate): # ns0:main_objects_to_activate
    Model.clientModel.service.set_main_objects_to_activate(main_objects_to_activate)

def setMemberRepresentative(member_representative): # ns0:member_representative
    Model.clientModel.service.set_member_representative(member_representative)

def setMemberSetRepresentative(member_set_representative): # ns0:member_set_representative
    Model.clientModel.service.set_member_set_representative(member_set_representative)

def setModelHistory(history): # ns0:array_of_model_history
    Model.clientModel.service.set_model_history(history)

def setModelParameters(model_parameters): # ns0:array_of_model_parameters
    Model.clientModel.service.set_model_parameters(model_parameters)

def setModelParametersLocation(location): # ns0:array_of_model_parameters_location
    Model.clientModel.service.set_model_parameters_location(location)

def setModelSettingsAndOptions(model_settings_and_options): # ns0:model_settings_and_options
    Model.clientModel.service.set_model_settings_and_options(model_settings_and_options)

def setModelType(model_type): # ns0:model_type *
    Model.clientModel.service.set_model_type(model_type)

def setNote(note): # ns0:note should be string !?
    Model.clientModel.service.set_note(note)

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

def setTimberMoistureClass(timber_moisture_class): # ns0:timber_moisture_class
    Model.clientModel.service.set_timber_moisture_class(timber_moisture_class)

def setTimberServiceConditions(timber_service_conditions): # ns0:timber_service_conditions
    Model.clientModel.service.set_timber_service_conditions(timber_service_conditions)

def setVisualObject(visual_object): # ns0:visual_object
    Model.clientModel.service.set_visual_object(visual_object)

def setWindProfile(wind_profile): # ns0:wind_profile
    Model.clientModel.service.set_wind_profile(wind_profile)

def setWindSimulation(wind_simulation): # ns0:wind_simulation
    Model.clientModel.service.set_wind_simulation(wind_simulation)

def setWindSimulationAnalysisSettings(wind_simulation_analysis_settings): # ns0:wind_simulation_analysis_settings
    Model.clientModel.service.set_wind_simulation_analysis_settings(wind_simulation_analysis_settings)

def uniteNodesAndSupports(tolerance):
    Model.clientModel.service.unite_nodes_and_supports(tolerance)
