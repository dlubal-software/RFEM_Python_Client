import sys
import os
import pytest
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import ObjectTypes
from RFEM.initModel import client, Model, url
from RFEM.ImportExport.exports import IFCExportSettings, ObjectLocation, ObjectLocations, ExportToIFC, GetTableExportConfigManager, SetTableExportConfigManager, ExportTo
from RFEM.ImportExport.imports import getConversionTables, setConversionTables, getSAFSettings, setSAFSettings, importFrom


if Model.clientModel is None:
    Model()


def test_export():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.run_script('..\\scripts\\internal\\Demos\\Demo-002 Cantilever Beams.js')

    dirname = os.path.join(os.getcwd(), os.path.dirname(__file__), 'testResults')
    targetFile1 = os.path.join(dirname, 'test_ifcExport1.ifc')
    targetFile2 = os.path.join(dirname, 'test_ifcExport2.ifc')

    IFCSettings = IFCExportSettings
    IFCSettings['mirror_axis_x'] = True

    ObjectLoc1 = ObjectLocation
    ObjectLoc2 = ObjectLocation

    ObjectLoc2['type'] = ObjectTypes.E_OBJECT_TYPE_SURFACE.name
    ObjectLoc2['no'] = 5
    ObjectLoc = ObjectLocations([ObjectLoc1, ObjectLoc2])

    Model.clientModel.service.begin_modification()
    ExportToIFC(targetFile1, IFCSettings)
    ExportToIFC(targetFile2, IFCSettings, ObjectLoc)

    config = GetTableExportConfigManager()
    config[1][0][0][2][0]['property_export_target'] = 'E_EXPORT_TARGET_CSV'
    SetTableExportConfigManager(config)
    assert config[1][0][0][2][0]['property_export_target'] == 'E_EXPORT_TARGET_CSV'

    # supported formats
    formats = ['.xml','.xlsx', '.gltf', '.glb'] # export to .vtk doesn't work
    for i in formats:
        try:
            ExportTo(os.path.join(dirname, 'export'+i))
        except RuntimeError:
            print(f'Export to {i} does not work!')

    Model.clientModel.service.finish_modification()

@pytest.mark.skipif(url != 'http://127.0.0.1', reason="This test fails on remote PC due to incorrect file paths. \
                    Althought it is easy to change, it would not be easy to update on every remote computer.\
                    It is not necessary to evaluate Client as functional. Localy this tests still gets executed.")
def test_import():

    Model.clientModel.service.delete_all()
    ct = getConversionTables()
    setConversionTables(ct)

    safc = getSAFSettings()
    safc['property_general_run_excel_application'] = False
    safc['property_import_surface_support_consolidate_import'] = True
    safc['property_import_edge_support_consolidate_import'] = True
    safc['property_import_show_conversion_tables_after_import'] = False
    safc['property_import_section_thin_walled_model'] = False
    safc['property_export_set_unit_system_imperial'] = False
    safc['property_export_set_gcs'] = 'minus_Z_vertical'
    safc['property_export_saf_version'] = '1_0_5'
    safc['property_export_loads'] = True
    safc['property_export_supports'] = True
    setSAFSettings(safc)

    dirname = os.path.join(os.getcwd(), os.path.dirname(__file__), 'src')
    importFrom(os.path.join(dirname, 'import_test_saf.saf'))
    importFrom(os.path.join(dirname, 'import_test_xlsx.xlsx'))
    importFrom(os.path.join(dirname, 'import_test_xml.xml'))

    client.service.close_model(3, False)
    client.service.close_model(2, False)
    client.service.close_model(1, False)

    assert getSAFSettings().property_general_run_excel_application == False
    assert getSAFSettings().property_export_saf_version == '1_0_5'
    assert getSAFSettings().property_import_show_conversion_tables_after_import == False
