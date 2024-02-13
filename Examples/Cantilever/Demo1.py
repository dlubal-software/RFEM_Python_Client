#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import NodalSupportType, NodalLoadDirection, ActionCategoryType
from RFEM.initModel import CalculateSelectedCases, Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Calculate.meshSettings import GetModelInfo

if __name__ == '__main__':
    l = float(input('Length of the cantilever in m: '))
    f = float(input('Force in kN: '))

    Model(True, "Demo1") # crete new model called Demo1
    Model.clientModel.service.begin_modification()


    Material(1, 'S235')

    Section(1, 'IPE 200')

    Node(1, 0.0, 0.0, 0.0)
    Node(2, l, 0.0, 0.0)

    Member(1, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.FIXED)

    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
    StaticAnalysisSettings.SecondOrderPDelta(2, "SecondOrder")
    StaticAnalysisSettings.LargeDeformation(3, "LargeDeformation")

    LoadCase.StaticAnalysis(1, 'Self-Weight',analysis_settings_no=1,self_weight=[True, 0.0, 0.0, 1.0])
    LoadCase.StaticAnalysis(2, 'Variable',analysis_settings_no=1,action_category=ActionCategoryType.ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_B_OFFICE_AREAS_QI_B)

    NodalLoad(1, 1, '2', NodalLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, f*1000)
    Model.clientModel.service.finish_modification()

    # Calculate_all()
    messages = CalculateSelectedCases([1])
    if not messages:
        print("Calculation finished unsuccessfully")
        print(messages)
        # for message in messages:
        #     print("{0}\t{1}: {2} - {3} {4} {5}".format("Yes" if message.result else "No", message.message_type.ToString(), message.message, message.@object, message.current_value, message.input_field))
    else:
        print("Calculation finished successfully")

    # model status
    modelStatus = GetModelInfo()
    print("Model is calculated" if modelStatus.property_has_results else "Model is not calculated")
    print("Model contains printout report" if modelStatus.property_has_printout_report else "Model has not printout report")
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

    node = Model.clientModel.service.get_node(1)
    print ("Node x coordinate " + str(node.coordinate_1))

    # ExportDetailsOfDesignToCSV(r"C:/WORK/TEMP/")
