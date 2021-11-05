#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')
# Import der Bibliotheken
# from RFEM.window import *
from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.solidSet import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.surfaceLoad import *


if __name__ == '__main__':
    l = float(input('Length of the cantilever in m: '))
    f = float(input('Force in kN: '))

    clientModel.service.begin_modification('new')

    Material(1, 'S235')

    Section(1, 'IPE 200')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, l, 0.0, 0.0)

    Member(1, MemberType.TYPE_BEAM, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)

    StaticAnalysisSettings(
        1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'Eigengewicht', [True, 0.0, 0.0, 1.0])

    NodalLoad(
        1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, f*1000)
    clientModel.service.finish_modification()

    Calculate_all()

    # model status
    modelStatus = clientModel.service.get_model_info()
    print("Model is calculated") if modelStatus.property_has_results else print("Model is not calculated")
    print("Model contains printout report") if modelStatus.property_has_printout_report else print("Model has not printout report")
    print ("Model contains " +  str(modelStatus.property_node_count) + " nodes")
    print ("Model contains " +  str(modelStatus.property_line_count) + " lines")
    print ("Model contains " +  str(modelStatus.property_member_count) + " members")
    print ("Model contains " +  str(modelStatus.property_surface_count) + " surfaces")
    print ("Model contains " +  str(modelStatus.property_solid_count) + " solids")
    print ("Model contains " +  str(modelStatus.property_lc_count) + " load cases")
    print ("Model contains " +  str(modelStatus.property_co_count) + " load combinations")
    print ("Model contains " +  str(modelStatus.property_rc_count) + " result classes")
    print ("Model weight " +   str(modelStatus.property_weight))
    print ("Model dimension x " + str(modelStatus.property_dimensions.x))
    print ("Model dimension y " + str(modelStatus.property_dimensions.y))
    print ("Model dimension z " + str(modelStatus.property_dimensions.z))


    # clientModel.service.save(r"D:/TEMP/model.rf6")

    # clientModel.service.export_to(r"D:/TEMP/model.gltf")
    # clientModel.service.export_to(r"D:/TEMP/model.glb")
    # clientModel.service.export_to(r"D:/TEMP/model.vtk")
   # clientObject = clientModel.factory.create('ns0:nodal_load')
    # export_to_ifc_object_location_type[] ifcLocation = null; // whole model will be exported
    # ifcSettings = clientModel.factory.create('ns0:export_to_ifc_settings_type')

    # ifcSettings.axis_rotation_sequence = "X'Y'Z'"
    # ifcSettings.mirror_axis_x = False
    # ifcSettings.mirror_axis_y = False
    # ifcSettings.mirror_axis_z = True
    # ifcSettings.origin_coordinate_x = 0.0
    # ifcSettings.origin_coordinate_y = 0.0
    # ifcSettings.origin_coordinate_z = 0.0
    # ifcSettings.export_type = export_to_ifc_export_type.E_EXPORT_IFC4_REFERENCE_VIEW.name
    # ifcSettings.rotation_angle_0 = 0.0
    # ifcSettings.rotation_angle_1 = 0.0
    # ifcSettings.rotation_angle_2 = 0.0
    # ifcSettings.switch_axis_x = export_to_ifc_axis_type.X.name
    # ifcSettings.switch_axis_y = export_to_ifc_axis_type.Y.name
    # ifcSettings.switch_axis_z = export_to_ifc_axis_type.Z.name
    # ifcSettings.remove_accents = False
    # clientModel.service.export_to_ifc(r'D:/TEMP/Mymodel.ifc', ifcSettings, None)

    # loadCases = [1]
    # CalculateSelectedCases(loadCases=loadCases)
    # ExportResulTablesWithDetailedMembersResultsToCsv(dirName)
    # ExportResulTablesWithDetailedMembersResultsToXML(dirName + "Results.xml")
    # #internalForces = ParseCSVResultsFromSelectedFileToDict(dirName + "\\My Model\\LC1_static_analysis_members_internal_forces.csv")
    # results = ParseXMLResultsFromSelectedFileToDict(dirName + "Results.xml")



