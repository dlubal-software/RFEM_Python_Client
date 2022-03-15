import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import ObjectTypes
from RFEM.initModel import Model, CheckIfMethodOrTypeExists
from RFEM.ImportExport.export import ExportToIFC, IFCExportSettings, ObjectLocations, ObjectLocation
import pytest


if Model.clientModel is None:
    Model()

@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'export_to_ifc', True), reason="export_to_ifc not in RFEM GM yet")
def test_exportToIFC():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.run_script('..\\scripts\\internal\\Demos\\Demo-002 Cantilever Beams.js')
    dirname = os.path.join(os.getcwd(), os.path.dirname(__file__))
    targetFile1 = os.path.join(dirname, 'testResults', 'test_ifcExport1.ifc')
    targetFile2 = os.path.join(dirname, 'testResults', 'test_ifcExport2.ifc')

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

    Model.clientModel.service.finish_modification()
