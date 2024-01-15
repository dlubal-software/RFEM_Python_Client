#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

#Import all modules required to access RFEM
from RFEM.enums import MemberEccentricitySpecificationType, ActionCategoryType, NodalSupportType,\
     MemberSectionDistributionType, MemberSectionAlignment, SurfaceEccentricityAlignment
from RFEM.initModel import Model, Calculate_all, connectToServer
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForSurfaces.surfaceEccentricity import SurfaceEccentricity
from RFEM.TypesForMembers.memberEccentricity import MemberEccentricity
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.surfaceLoad import SurfaceLoad
from RFEM.Loads.freeLoad import FreeLoad
from RFEM.Tools.PlausibilityCheck import PlausibilityCheck
from RFEM import connectionGlobals


if __name__ == "__main__":
    # connect to server and establish a naming scheme
    connectToServer()
    array_of_models = connectionGlobals.client.service.get_model_list()
    if array_of_models:
        model_list = array_of_models[0]
        print("List of active models:", model_list)
    else:
        print("Creating new model.")
        model_list = []
    name_counter = 1
    model_name = "concrete_bridge_" + str(name_counter)
    while model_name in model_list:
        name_counter += 1
        model_name = "concrete_bridge_" + str(name_counter)

    # ----------------INPUT PARAMETERS------------------#
    # inicialize model and define parameters
    Model(model_name=model_name)

    num_bridge_fields = 9      # number of whole bridge fields (between pillars)
    bridge_height = float(7.5)   # primary parameters, input in meters
    bridge_width = float(4)
    bridge_length = float(14)   # length of one field/span
                                # secondary (derived) parameters, input optional in meters
    pillar_dimension = bridge_width/6
    girder_width = pillar_dimension
    girder_height = bridge_width/4
    beam_width = 0.4
    beam_height_inwards = bridge_width/8
    beam_height_outwards = bridge_width/16
    slab_thickness = 0.25
    # beam spacing setup
    for b in range(1, int(bridge_length)):
        if bridge_length/b < 5.0:
            beam_spacing = bridge_length/b
            beams_per_field = b
            break
    # LOADING SETUP - if, true, the live load will only be applied on odd bridge fields
    # if false, loading will be constant for the whole bridge length
    alternating_live_loads = False
    live_load_magnitude = 20000.0

    # ----------------INPUT PARAMETERS------------------#

    # starting modification of the model
    Model.clientModel.service.begin_modification()
    # materials
    Material(1, "C30/37")
    Material(2, "C50/60")
    # sections
    Section(1,"SQ_M1 " + str(pillar_dimension), 2, "pillar")
    Section(2,f"R_M1 {girder_width}/{girder_height}", 2, "girder")
    Section(3, f"R_M1 {beam_width}/{beam_height_inwards}", 2, "beam_1")
    Section(4, f"R_M1 {beam_width}/{beam_height_outwards}", 2, "beam_2")
    # thicknesses
    Thickness(1, material_no= 1, uniform_thickness_d= slab_thickness)

    # --------- BUILDING MODEL ----------- #
    print("Constructing bridge...")

    # nodes
    # pillar nodes
    node_counter = 1
    for i in range(1, num_bridge_fields+2):
        Node(node_counter,(i-1)*bridge_length, 0, 0)
        NodalSupport(i, f"{node_counter}", NodalSupportType.FIXED)
        Node(node_counter+1,(i-1)*bridge_length, 0, -bridge_height)
        node_counter += 2
    pillar_node_count = node_counter

    # girder nodes
    Node(node_counter, -pillar_dimension/2, 0, -bridge_height)
    Node(node_counter+1, num_bridge_fields*bridge_length+pillar_dimension/2, 0, -bridge_height)
    girder_node_1 = node_counter
    girder_node_2 = node_counter + 1
    node_counter += 2

    # beam nodes
    x_for_beams = beam_spacing/2
    beam_start_node = node_counter
    for n in range(beams_per_field*num_bridge_fields):
        if x_for_beams!=n*bridge_length:
            Node(node_counter, x_for_beams, 0, -bridge_height)
            Node(node_counter+1, x_for_beams, -bridge_width/2, -bridge_height)
            Node(node_counter+2, x_for_beams, bridge_width/2, -bridge_height)
            node_counter += 3
        x_for_beams += beam_spacing

    # slab nodes and lines
    Node(node_counter, -pillar_dimension/2, -bridge_width/2, -bridge_height)
    Node(node_counter+1, -pillar_dimension/2, bridge_width/2, -bridge_height)
    Node(node_counter+2, bridge_length*num_bridge_fields+pillar_dimension/2, -bridge_width/2, -bridge_height)
    Node(node_counter+3, bridge_length*num_bridge_fields+pillar_dimension/2, bridge_width/2, -bridge_height)
    line_counter = 1
    Line.DeleteLine("1 2 3 4")
    Line.Polyline(line_counter, f"{node_counter} {node_counter+1} {node_counter+3} {node_counter+2} {node_counter}")
    node_counter += 4

    # members - pillars
    m_count = 0
    MemberEccentricity(5, name= 'pillar ecc.', eccentricity_type = MemberEccentricitySpecificationType.TYPE_ABSOLUTE,
                           eccentricity_parameters= [1, 0, 0, girder_height+slab_thickness])
    for i in range(1, pillar_node_count, 2):
        m_count += 1
        Member(m_count, i, i+1, params= {"member_eccentricity_end":5})
    print(f"Generating {m_count} pillars.")
    num_pillars = m_count

    # members - girder
    print("Generating girder.")
    m_count += 1
    MemberEccentricity(4, name= 'girder ecc.', eccentricity_type = MemberEccentricitySpecificationType.TYPE_ABSOLUTE,
                           eccentricity_parameters= [1, 0, 0, girder_height/2+slab_thickness])
    Member(m_count, girder_node_1, girder_node_2, start_section_no=2, end_section_no=2,
           params= {"member_eccentricity_start":4, "member_eccentricity_end":4})
    # members - beams
    MemberEccentricity(1, name= 'beam ecc.1', eccentricity_type = MemberEccentricitySpecificationType.TYPE_ABSOLUTE,
                           eccentricity_parameters= [1, 0, 0, beam_height_outwards/2+slab_thickness])
    MemberEccentricity(2, name= 'beam ecc.2', eccentricity_type = MemberEccentricitySpecificationType.TYPE_ABSOLUTE,
                           eccentricity_parameters= [1, 0, -girder_width/2, beam_height_outwards/2+slab_thickness])
    MemberEccentricity(3, name= 'beam ecc.3', eccentricity_type = MemberEccentricitySpecificationType.TYPE_ABSOLUTE,
                           eccentricity_parameters= [1, 0, girder_width/2, beam_height_outwards/2+slab_thickness])
    for n in range(beams_per_field*num_bridge_fields):
        Member.Beam(
                    m_count+1, beam_start_node, beam_start_node+1,
                    MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_LINEAR,
                    start_section_no=3, end_section_no=4,
                    distribution_parameters= [MemberSectionAlignment.SECTION_ALIGNMENT_TOP],
                    params= {"member_eccentricity_start":2, "member_eccentricity_end":1}
                    )
        Member.Beam(
                    m_count+2, beam_start_node, beam_start_node+2,
                    MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_LINEAR,
                    start_section_no=3, end_section_no=4,
                    distribution_parameters= [MemberSectionAlignment.SECTION_ALIGNMENT_TOP],
                    params= {"member_eccentricity_start":3, "member_eccentricity_end":1}
                    )


        m_count += 2
        beam_start_node += 3

    print(f"Generating {m_count-num_pillars-1} support beams.")
    # bridge concrete slab
    print(f"Generating support slab, thickness {slab_thickness*1000}mm.")
    s_count = 1
    Surface(s_count, "1", 1, "bridge slab")
    SurfaceEccentricity(1, 0, f"{s_count}", thickness_alignment= SurfaceEccentricityAlignment.ALIGN_TOP,
                        transverse_offset_object= None)

    # loadcases
    LoadCase() # self weight
    LoadCase(2, "Active Load", [True, 0, 0, 1],
             ActionCategoryType.ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_F_TRAFFIC_AREA_VEHICLE_WEIGHT_LESS_OR_EQUAL_TO_30_KN_QI_F,
             )
    if alternating_live_loads:
        if num_bridge_fields == 1:
            FreeLoad.RectangularLoad(1, 2, "1", load_magnitude_parameter= [live_load_magnitude],
                                    load_location_parameter= [-pillar_dimension/2, -bridge_width/2, bridge_length+pillar_dimension/2, bridge_width/2, 0])
        else:
            # first field
            FreeLoad.RectangularLoad(1, 2, "1", load_magnitude_parameter= [live_load_magnitude],
                                        load_location_parameter= [-pillar_dimension/2, -bridge_width/2, bridge_length, bridge_width/2, 0])
            # inner fields
            for i in range(2, num_bridge_fields, 2):
                FreeLoad.RectangularLoad(1+i, 2, "1", load_magnitude_parameter= [live_load_magnitude],
                                        load_location_parameter= [bridge_length*i, -bridge_width/2, bridge_length*(i+1), bridge_width/2, 0])
            # last field
            if num_bridge_fields%2 != 0:
                FreeLoad.RectangularLoad(num_bridge_fields, 2, "1", load_magnitude_parameter= [live_load_magnitude],
                                        load_location_parameter= [bridge_length*(num_bridge_fields-1), -bridge_width/2, bridge_length*num_bridge_fields+pillar_dimension/2, bridge_width/2, 0])
    else:
        SurfaceLoad(1, 2, "1", 20000, "Road Traffic")

    Model.clientModel.service.finish_modification()
    PlausibilityCheck()
    print("Calculating results.")
    Calculate_all()
