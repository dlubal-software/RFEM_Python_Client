from RFEM.initModel import Model

# All export functions
def ExportDetailsOfDesignToCSV(targetDirectoryPath: str):
    Model.clientModel.service.export_details_of_design_to_csv(targetDirectoryPath)

def ExportResultTablesToCSV(targetDirectoryPath: str):
    Model.clientModel.service.export_result_tables_to_csv(targetDirectoryPath)

def ExportResultTablesToXML(targetFilePath: str):
    Model.clientModel.service.export_result_tables_to_xml(targetFilePath)

def ExportResultTablesWithDetaliedMmebersResultsToCSV(targetDirectoryPath: str):
    Model.clientModel.service.export_result_tables_with_detailed_members_results_to_csv(targetDirectoryPath)

def ExportResultTablesWithDetaliedMmebersResultsToXML(targetFilePath: str):
    Model.clientModel.service.export_result_tables_with_detailed_members_results_to_xml(targetFilePath)

def ExportTo(targetFilePath: str):
    Model.clientModel.service.export_to(targetFilePath)

def ExportToIFC(targetFilePath: str, IFCSettings, ObjectLocations):
    # ns0:export_to_ifc_settings settings,
    #(export_to_ifc_settings){
	#(export_to_ifc_settings){
	#   mirror_axis_x = None
	#   mirror_axis_y = None
	#   mirror_axis_z = None
	#   origin_coordinate_x = None
	#   origin_coordinate_y = None
	#   origin_coordinate_z = None
	#   axis_rotation_sequence =
	#      (export_to_ifc_axis_rotation_sequence_type){
	#         value = None
	#      }
	#   rotation_angle_0 = None
	#   rotation_angle_1 = None
	#   rotation_angle_2 = None
	#   switch_axis_x =
	#      (export_to_ifc_axis_type){
	#         value = None
	#      }
	#   switch_axis_y =
	#      (export_to_ifc_axis_type){
	#         value = None
	#      }
	#   switch_axis_z =
	#      (export_to_ifc_axis_type){
	#         value = None
	#      }
	#   remove_accents = None
	#   export_type =
	#      (export_to_ifc_export_type){
	#         value = None
	#      }
	#}

    # ns0:export_to_ifc_object_locations object_locations
    # (export_to_ifc_object_locations){
    #   location[] = <empty>
    #}
    Model.clientModel.service.export_to_ifc(targetFilePath, IFCSettings, ObjectLocations)

def ExportToTables(targetDirectoryPath: str):
    Model.clientModel.service.export_to_tables(targetDirectoryPath)

def GetTableExportConfigManager():
    Model.clientModel.service.get_table_export_config_manager()

def SetTableExportConfigManager(TableExportConfigManager):
    # ns0:TableExportConfigManager value

    #(TableExportConfigManager){
    #   property_active_config = None
    #   configs =
    #       (TableExportConfigManager_configs){
    #           config[] = <empty>
    #       }
    #}
    Model.clientModel.service.set_table_export_config_manager(TableExportConfigManager)
