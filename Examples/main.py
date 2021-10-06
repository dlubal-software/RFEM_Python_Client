from RFEM.enums import *
from RFEM.window import *
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

def main(hall_width_L, hall_height_h_o, hall_height_h_m, number_frames, frame_spacing):
# -------------------------------------------------------------
    clientModel.service.begin_modification('new')
    print('Geometry...')

# -------------------------------------------------------------
    # Materials
    Material(1)
    Material(2, "S275", "Test")
    Material(3, "Concrete f'c = 20 MPa | CSA A23.3-19", "Test")

# -------------------------------------------------------------
    # Sections
    Section(1, "HEB 220")
    Section(2, "IPE 300")
    Section(3, "U 100", 2)
    Section(4, "Cable 14.00", 2)

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
    MemberHinge(1, "Local", inf, inf, inf,  inf, 0, inf, "Rotational Release My")

# -------------------------------------------------------------
    # Members

    # Frames
    i = 1
    while i <= number_frames:
        j = (i-1) * 5
        k = (i-1) * 4
        Member(k+1, MemberType.TYPE_BEAM, j+1, j+2, 0.0,  1, 1)
        Member(k+2, MemberType.TYPE_BEAM, j+2, j+3, 0.0,  2, 2)
        Member(k+3, MemberType.TYPE_BEAM, j+3, j+4, 0.0,  2, 2)
        Member(k+4, MemberType.TYPE_BEAM, j+4, j+5, 0.0,  1, 1)
        i += 1

    # Purlins
    i = 1
    while i <= number_frames-1:
        j = (i-1) * 5
        Member(4*number_frames+i                    , MemberType.TYPE_BEAM, j+2, j+7,   0.0,  3, 3,  1, 1)
        Member(4*number_frames+i +   number_frames-1, MemberType.TYPE_BEAM, j+3, j+8,   0.0,  3, 3)
        Member(4*number_frames+i + 2*number_frames-2, MemberType.TYPE_BEAM, j+4, j+9, 180.0,  3, 3,  1, 1)
        i += 1

    # Diagonals on the wall
    i = 1
    j = 4*number_frames + 3*(number_frames-1)
    while i <= number_frames-1:
        k = j + (i-1)*4
        Member(k+1, MemberType.TYPE_TENSION, (i-1)*5+1, (i-1)*5+7 , 0.0,  4, 4)
        Member(k+2, MemberType.TYPE_TENSION, (i-1)*5+2, (i-1)*5+6 , 0.0,  4, 4)
        Member(k+3, MemberType.TYPE_TENSION, (i-1)*5+5, (i-1)*5+9 , 0.0,  4, 4)
        Member(k+4, MemberType.TYPE_TENSION, (i-1)*5+4, (i-1)*5+10, 0.0,  4, 4)
        i += 1

    # Diagonals on the roof
    j += 4*(number_frames-1)
    if number_frames > 1:
        Member(j+1, MemberType.TYPE_TENSION, 2, 8, 0.0,  4, 4)
        Member(j+2, MemberType.TYPE_TENSION, 7, 3, 0.0,  4, 4)
        Member(j+3, MemberType.TYPE_TENSION, 3, 9, 0.0,  4, 4)
        Member(j+4, MemberType.TYPE_TENSION, 4, 8, 0.0,  4, 4)

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
    Solid(1, "2 3 4 5 6 7", 2)

# -------------------------------------------------------------
    # Sets
    LineSet()
    MemberSet()
    SurfaceSet()
    #SolidSet()

# -------------------------------------------------------------
    print('Load Cases/Loads...')

# -------------------------------------------------------------
    # Static Analysis Settings
    StaticAnalysisSettings(1, "Large deformations", StaticAnalysisType.LARGE_DEFORMATIONS)

# -------------------------------------------------------------
    # Load Cases
    LoadCase(1 , "Self-weight", AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)
    LoadCase(2 , "Live loads" , AnalysisType.ANALYSIS_TYPE_STATIC, 1,  4)
    LoadCase(3 , "Test 1"     , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(4 , "Test 2"     , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(5 , "Test 3"     , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(6 , "Test 4"     , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(7 , "Test 5"     , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(8 , "Test 6"     , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(9 , "Test 7"     , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(10, "Test 8"     , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(11, "Test 9"     , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(12, "Test 10"    , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(13, "Test 11"    , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)
    LoadCase(14, "Test 12"    , AnalysisType.ANALYSIS_TYPE_STATIC, 1, 14)


# -------------------------------------------------------------
    # Nodal Forces
    NodalLoad(1, 3, "9 4 7 2", LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 2000.0)

# -------------------------------------------------------------
    # Member Loads
    # Eccentricity is not implemented (worth consideration)
    MemberLoad(1, 3, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, 4000.0)

    MemberLoad(1, 4, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TOTAL,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, 4000.0)

    MemberLoad(1, 5, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [4000.0, 2.000])

    MemberLoad(1, 6, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [4000.0, 3, 0.800, 1.100])

    MemberLoad(1, 7, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [4000.0, 1.000, 0.500, 3.000])

    MemberLoad(1, 8, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [4000.0, 3000, 2.500, 3.000])

    MemberLoad(1, 9, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[0.500, 0.500, 2000.0]])
    # bug 15314 - load position is not saved in RFEM
    #MemberLoad(1,10, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL,\
    #           MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [1000.0, 1500.0, 3.000, 8.000])
    # bug 15314 - load position is not saved in RFEM
    MemberLoad(1,11, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [2000.0, 4000.0, 2.000, 5.000])

    MemberLoad(1,12, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [2000.0, 4000.0, 3000.0])

    MemberLoad(1,13, "2 3 6 7", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[4.000, 4.000, 2000.0], [5.000, 1.000, 3000.0]])

    MemberLoad(1,14, "1 4", MemberLoadType.LOAD_TYPE_FORCE, MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z,\
               MemberLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[-4.000, -4.000, 1000.0], [-2.000, 2.000, 2000.0]])

# -------------------------------------------------------------
    # Surface Loads
    SurfaceLoad(1, 3, "3", 20000)

# -------------------------------------------------------------
    # Finish client model
    print("Calculating...")
    clientModel.service.finish_modification()

# -------------------------------------------------------------
    # Calculate all
    Calculate_all()
    print("Done")

if __name__ == '__main__':
    window(main)
