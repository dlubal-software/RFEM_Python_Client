import sys
import os
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.enums import NodalSupportType, StaticAnalysisType, LoadDirectionType, MemberLoadDistribution, MemberLoadDirection, MemberRotationSpecificationType
from Examples.window import window
from RFEM.dataTypes import inf
from RFEM.initModel import Model, Calculate_all, insertSpaces, modelLst
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.solid import Solid
from RFEM.BasicObjects.opening import Opening
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Loads.surfaceLoad import SurfaceLoad

def main(hall_width_L, hall_height_h_o, hall_height_h_m, number_frames, frame_spacing, new_model, model_name, delete_res, delete_all):
# -------------------------------------------------------------
    Model(new_model, model_name, delete_res, delete_all)
    Model.clientModel.service.begin_modification()
# -------------------------------------------------------------
    # Materials
    Material(1)
    Material(3, "Concrete f'c = 20 MPa | CSA A23.3-19", "Test")

# -------------------------------------------------------------
    # Sections
    Section(1, "HEB 220")
    Section(2, "IPE 300")
    Section(3, "U 100")
    Section(4, "Cable 14.00")

# -------------------------------------------------------------
    # Thicknesses
    Thickness(1, "Slab", 3, 0.24, "Test")

# -------------------------------------------------------------
    # Nodes
    i = 1
    while i <= number_frames:
        j = (i-1) * 5
        Node(j+1, 0.0           , -(i-1) * frame_spacing)
        Node(j+2, 0.0           , -(i-1) * frame_spacing, -hall_height_h_o)
        Node(j+3, hall_width_L/2, -(i-1) * frame_spacing, -hall_height_h_m)
        Node(j+4, hall_width_L  , -(i-1) * frame_spacing, -hall_height_h_o)
        Node(j+5, hall_width_L  , -(i-1) * frame_spacing)
        i += 1

    # Nodes for openings
    k = number_frames*5
    open_dim_x = hall_width_L/10
    open_dim_y = -(number_frames*frame_spacing)/15

    Node(k+1, hall_width_L-open_dim_x,   open_dim_y)
    Node(k+2, hall_width_L-open_dim_x,   2*open_dim_y)
    Node(k+3, hall_width_L-2*open_dim_x, 2*open_dim_y)
    Node(k+4, hall_width_L-2*open_dim_x, open_dim_y)

    params = {'coordinate_system':1, 'coordinate_system_type':'COORDINATE_SYSTEM_CARTESIAN'}
    Node(k+5, 1, 1, 0, '', params)
    Node(k+6, 2, 1, 0, '', params)
    Node(k+7, 2, 2, 0, '', params)
    Node(k+8, 1, 2, 0, '', params)
    solid_support = str(k+5)+" "+str(k+6)+" "+str(k+7)+" "+str(k+8)

    Node(k+9, 1, 1, -1)
    Node(k+10, 2, 1, -1)
    Node(k+11, 2, 2, -1)
    Node(k+12, 1, 2, -1)

# -------------------------------------------------------------
    # Lines

    # List (str) of line nodes
    nodes_no = ""
    i = 1
    while i <= number_frames:
        nodes_no += str((i-1)*5+1) + " "
        i += 1
    i = number_frames
    while i >= 1:
        nodes_no += str((i-1)*5+5) + " "
        i -= 1
    Line(1, nodes_no + "1")

    #Line for opening
    Line(2, insertSpaces([k+1, k+2, k+3, k+4, k+1]))

    # Lines for solid
    Line(3, insertSpaces([k+5, k+6, k+7, k+8, k+5]))
    Line(4, insertSpaces([k+9, k+10, k+11, k+12, k+9]))
    Line(5, insertSpaces([k+5, k+6, k+10, k+9, k+5]))
    Line(6, insertSpaces([k+6, k+7, k+11, k+10, k+6]))
    Line(7, insertSpaces([k+7, k+8, k+12, k+11, k+7]))
    Line(8, insertSpaces([k+8, k+5, k+9, k+12, k+8]))

# -------------------------------------------------------------
    # Member Hinges
    MemberHinge(1, "Local", rotational_release_mz=inf)


# -------------------------------------------------------------
    # Members

    member = Member()
    # Frames
    i = 1
    while i <= number_frames:
        j = (i-1) * 5
        k = (i-1) * 4
        Member(k+1,  j+1, j+2, 0.0,  1, 1)
        Member(k+2,  j+2, j+3, 0.0,  2, 2)
        Member(k+3,  j+3, j+4, 0.0,  2, 2)
        Member(k+4,  j+4, j+5, 0.0,  1, 1)
        i += 1

    # Purlins
    i = 1
    while i <= number_frames-1:
        j = (i-1) * 5
        Member(4*number_frames+i                    ,  j+2, j+7,   0.0,  3, 3,  1, 1)
        Member(4*number_frames+i +   number_frames-1,  j+3, j+8,   0.0,  3, 3)
        Member(4*number_frames+i + 2*number_frames-2,  j+4, j+9, 180.0,  3, 3,  1, 1)
        i += 1

    # Diagonals on the wall
    i = 1
    j = 4*number_frames + 3*(number_frames-1)
    while i <= number_frames-1:
        k = j + (i-1)*4
        member.Tension(k+1, (i-1)*5+1, (i-1)*5+7 , MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 4)
        member.Tension(k+2, (i-1)*5+2, (i-1)*5+6 , MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 4)
        member.Tension(k+3, (i-1)*5+5, (i-1)*5+9 , MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 4)
        member.Tension(k+4, (i-1)*5+4, (i-1)*5+10, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 4)
        i += 1

    # Diagonals on the roof
    j += 4*(number_frames-1)
    if number_frames > 1:
        member.Tension(j+1, 2, 8, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 4)
        member.Tension(j+2, 7, 3, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 4)
        member.Tension(j+3, 3, 9, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 4)
        member.Tension(j+4, 4, 8, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 4)

# -------------------------------------------------------------
    # Surfaces
    Surface(1, "1", 1)

    Surface(2, "3", 1)
    Surface(3, "4", 1)
    Surface(4, "5", 1)
    Surface(5, "6", 1)
    Surface(6, "7", 1)
    Surface(7, "8", 1)

# -------------------------------------------------------------
    # Openings
    Opening(1, "2", "waste passage")

# -------------------------------------------------------------
    # Nodal Supports

    # List (str) of supported nodes
    i = 1
    nodes_no = ""
    while i <= number_frames:
        j = (i-1) * 5
        nodes_no += str(j+1) + " "
        nodes_no += str(j+5) + " "
        i += 1
    nodes_no = nodes_no.rstrip(nodes_no[-1])    # Removes one character from the end of the string

    NodalSupport(1, nodes_no, NodalSupportType.HINGED, "Hinged support")

    # Support of solid
    NodalSupport(2, solid_support, NodalSupportType.HINGED, "Hinged support")

# -------------------------------------------------------------
    # Solids
    Solid(1, "2 3 4 5 6 7", 3)

# -------------------------------------------------------------
    print('Load Cases/Loads...')

# -------------------------------------------------------------
    # Static Analysis Settings
    StaticAnalysisSettings(1, "Linear calculation", StaticAnalysisType.GEOMETRICALLY_LINEAR)

# -------------------------------------------------------------
    # Load Cases
    LoadCase(1 , "Self-weight",[True, 0.0, 0.0, 10.0])
    LoadCase(2 , "Live loads")
    LoadCase(3 , "Test 1" )
    LoadCase(4 , "Test 2" )
    LoadCase(5 , "Test 3" )
    LoadCase(6 , "Test 4" )
    LoadCase(7 , "Test 5" )
    LoadCase(8 , "Test 6" )
    LoadCase(9 , "Test 7" )
    LoadCase(10, "Test 8" )
    LoadCase(11, "Test 9" )
    LoadCase(12, "Test 10")
    LoadCase(13, "Test 11")
    LoadCase(14, "Test 12")

# -------------------------------------------------------------
    # Nodal Forces
    NodalLoad(1, 3, "9 4 7 2", LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 2000.0)

# -------------------------------------------------------------
    # Member Loads
    memberLoad = MemberLoad()

    memberLoad.Force(2, 1, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Force Type Member Load with LOAD_DISTRIBUTION_UNIFORM with Eccentricity ##
    memberLoad.Force(3, 2, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000], force_eccentricity=True, params={'eccentricity_y_at_start' : 0.01, 'eccentricity_z_at_start': 0.02})

    ## Force Type Member Load with LOAD_DISTRIBUTION_UNIFORM_TOTAL ##
    memberLoad.Force(4, 3, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TOTAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[5000])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_1 ##
    memberLoad.Force(5, 4, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, 5000, 1.2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_N ##
    memberLoad.Force(6, 5, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 2, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x2 ##
    memberLoad.Force(7, 6, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, False, 5000, 1, 2, 3])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_2x ##
    memberLoad.Force(8, 7, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 5000, 6000, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_CONCENTRATED_VARYING ##
    memberLoad.Force(9, 8, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 4000], [2, 5000]])

    ## Force Type Member Load with LOAD_DISTRIBUTION_TRAPEZOIDAL ##
    memberLoad.Force(10, 9, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_TAPERED ##
    memberLoad.Force(11, 10, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[False, False, 4000, 8000, 1, 2])

    ## Force Type Member Load with LOAD_DISTRIBUTION_PARABOLIC ##
    memberLoad.Force(12, 11, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[4000, 8000, 12000])

    ## Force Type Member Load with LOAD_DISTRIBUTION_VARYING ##
    memberLoad.Force(13, 12, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 4000], [2, 5000]])

    ## Force Type Member Load with LOAD_DISTRIBUTION_VARYING_IN_Z ##
    memberLoad.Force(14, 13, "2 3 6 7", MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z, MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, load_parameter=[[1, 4000], [2, 5000]])

# -------------------------------------------------------------
    # Surface Loads
    SurfaceLoad(1, 3, "3", 20000)

# -------------------------------------------------------------
    # Finish client model
    print("Calculating...")
    Model.clientModel.service.finish_modification()

# -------------------------------------------------------------
    # Calculate all
    Calculate_all()

    print("Done")
    sys.exit()

if __name__ == '__main__':
    window(main, modelLst)
