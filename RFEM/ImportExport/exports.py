import xmltodict
import csv
from RFEM.initModel import Model
from RFEM.enums import IFCExportType, ObjectTypes

def ExportDetailsOfDesignToCSV(targetDirectoryPath: str, model = Model):
    '''
    Export details of design to CSV format.

    Args:
        targetDirectoryPath (string): Destination path to the directory
    '''
    model.clientModel.service.export_details_of_design_to_csv(targetDirectoryPath)

def ExportResultTablesToCSV(targetDirectoryPath: str, model = Model):
    '''
    Export result tables to CSV format.

    Args:
        targetDirectoryPath (string): Destination path to the directory
    '''
    model.clientModel.service.export_result_tables_to_csv(targetDirectoryPath)

def ExportResultTablesToXML(targetFilePath: str, model = Model):
    '''
    Export result tables to XML format.

    Args:
        targetFilePath (string): Destination path to the file
    '''
    model.clientModel.service.export_result_tables_to_xml(targetFilePath)

def ExportResultTablesWithDetaliedMembersResultsToCSV(targetDirectoryPath: str, model = Model):
    '''
    Export result tables with detailed member results to CSV format.

    Args:
        targetDirectoryPath (string): Destination path to the directory
    '''
    model.clientModel.service.export_result_tables_with_detailed_members_results_to_csv(targetDirectoryPath)

def ExportResultTablesWithDetaliedMembersResultsToXML(targetFilePath: str, model = Model):
    '''
    Export result tables with detailed member results to XML format.

    Args:
        targetFilePath (string): Destination path to the file
    '''
    model.clientModel.service.export_result_tables_with_detailed_members_results_to_xml(targetFilePath)

def ExportTo(targetFilePath: str, model = Model):
    '''
    Export active model to format specified by suffix of the destination path to file.
    Supported formats are .xml, .vtk, .xlsx, .saf, .gltf, and .glb.

    Args:
        targetFilePath (string): Destination path to the file
    '''
    model.clientModel.service.export_to(targetFilePath)

IFCExportSettings = {
    'mirror_axis_x': False,
    'mirror_axis_y': False,
    'mirror_axis_z': False,
    'origin_coordinate_x': 0, # float
    'origin_coordinate_y': 0, # float
    'origin_coordinate_z': 0, # float
    'axis_rotation_sequence': 'X_Y_Z', # string
    'rotation_angle_0': 0, # float
    'rotation_angle_1': 0, # float
    'rotation_angle_2': 0, # float
    'switch_axis_x': 'X', # 'X','Y' or 'Z'
    'switch_axis_y': 'Y', # 'X','Y' or 'Z'
    'switch_axis_z': 'Z', # 'X','Y' or 'Z'
    'remove_accents': False,
    'export_type': IFCExportType.E_EXPORT_IFC4_REFERENCE_VIEW.name # export to ifc type
}

ObjectLocation = {
    'type':ObjectTypes.E_OBJECT_TYPE_MEMBER.name,
    'no': 1,
    'parent_no': 1
}
'''
Args:
    type (enum): Type of object to be exported to IFC
    no (int): Number of the object to be exoprted to IFC
    parent_no (int): Parrent number  of the object to be exoprted to IFC, if there is one. Usually 1.
'''

def ObjectLocations(locationsArray):
    '''
    Use this function to obtain 3rd parameter of ExportToIFC() function.
    If left out, all objects will be exported to IFC.

    Args:
        locationsVector (array): Array of ObjectLocation variables

    {'location': {'type':ObjectTypes.E_OBJECT_TYPE_MEMBER.name, 'no': 1, 'parent_no': 1}}
    '''

    return {'location': locationsArray}


def ExportToIFC(targetFilePath: str, IFCSettings: IFCExportSettings, ObjectLoc = None, model = Model):
    '''
    Use this function to export active model t o IFC.

    Args:
        targetFilePath (string): Target file path incl. suffix.
        IFCSettings (IFCExportSettings): IFC export settings dictionary.
        ObjectLoc (array): array of ObjectLocation dictionary. If left out, all objects will be exported to IFC.
    '''
    if ObjectLoc:
        model.clientModel.service.export_to_ifc(targetFilePath, IFCSettings, ObjectLoc)
    else:
        model.clientModel.service.export_to_ifc(targetFilePath, IFCSettings)

def ExportToTables(targetDirectoryPath: str, model = Model):
    '''
    Export active model to tables.

    Args:
        targetDirectoryPath (string): Destination path to the directory
    '''
    model.clientModel.service.export_to_tables(targetDirectoryPath)

def GetTableExportConfigManager(model = Model):
    '''
    Export active model to tables.
    Use this fuction to obtain input parameter to SetTableExportConfigManager()

    Return:
        Table export configuration.
    '''
    return model.clientModel.service.get_table_export_config_manager()

def SetTableExportConfigManager(TableExportConfigManager, model = Model):
    '''
    Create or change table export settings.
    To obtain input data (TableExportConfigManager) call GetTableExportConfigManager() first.

    Args:
        TableExportConfigManager (dict): Table export config
    '''
    model.clientModel.service.set_table_export_config_manager(TableExportConfigManager)

def ParseCSVResultsFromSelectedFileToDict(filePath: str):

    # Using encoding parameter ensures proper data translation, leaving out BOM etc.
    # TODO: fix the value assigment; it only works with simple one-line header
    #       consider all corner cases
    with open(filePath, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f,delimiter=';')
        my_dictionary = []
        for line in reader:
            my_dictionary.append(line)
    return my_dictionary

def ParseXMLResultsFromSelectedFileToDict(filePath: str):

    with open(filePath, "rb") as f:
        my_dictionary = xmltodict.parse(f, xml_attribs=True)
    return my_dictionary
