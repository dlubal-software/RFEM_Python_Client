import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
sys.path.append(dirName + r'/../..')
import pyvista as pv
from RFEM.enums import LineSupportType, SurfaceGeometry, SurfaceLoadDirection, SurfaceLoadDistribution
from RFEM.initModel import Calculate_all, Model, client
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.surface import Surface
from RFEM.TypesForLines.lineSupport import LineSupport
from RFEM.Results.resultTables import GetMaxValue, ResultTables
from RFEM.Loads.surfaceLoad import SurfaceLoad
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.ImportExport.exports import ExportTo

def calculateTank(d, h, util):

    """
    Args:
        d (float): Tank Diameter
        h (float): Tank Height
        util (float) : Utilization of Tank Capacity (in %)
    """
    lst = None
    lst = client.service.get_model_list()

    if lst:

        if 'responsiveTank' in lst[0]:
            print('Editing old Model...!')
            Model(False, 'responsiveTank.rf6', True)

        else:
            print('Creating new model...!')
            Model(True, 'responsiveTank.rf6', delete_all= True)

    else:
        print('Creating new model...!')
        Model(True, 'responsiveTank.rf6', delete_all= True)

    Material(1, "S235")
    Node(1, d/2, 0,0)
    Node(2, d/2, 0, -h)
    Node(3, 0,0, -(h+2))

    Line.Circle(1, [0,0,0], d/2, [0,0,1])
    Line.Circle(2, [0,0, -h], d/2, [0,0,1])
    Line(3, '1 2')
    Line.Arc(4, [2,3], [d/3.5, 0, -(h+(2/1.5))])

    LineSupport(1, '1', LineSupportType.HINGED)

    Thickness(1, '12 mm', 1, 0.012)

    Surface.Standard(1, SurfaceGeometry.GEOMETRY_QUADRANGLE, [1,2,0,0], '1 2 3', 1)
    Surface.Standard(2, SurfaceGeometry.GEOMETRY_ROTATED, [360, [0,0,0], [0,0,1], 4], "2 3", 1)

    LoadCase()

    load_height = util * (h + 2)

    SurfaceLoad.Force(no = 1,
                      load_case_no = 1,
                      surface_no = '1 2',
                      load_direction = SurfaceLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                      load_distribution = SurfaceLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z,
                      load_parameter = [[-load_height, -load_height, 0],[0, load_height, 9.81 * load_height * 1000]])

    Calculate_all()

    global maxStress
    maxStressinit = ResultTables.SurfacesEquivalentStressesMises()
    maxStress = GetMaxValue(maxStressinit, 'equivalent_stresses_sigma_eqv_max') / 1000000

    ExportTo(dirName + r"/export.vtk")
    Model.clientModel.service.close_connection()

    file = dirName + r"/export/export_0.vtp"
    mesh = pv.read(file)
    plotter = pv.Plotter()
    plotter.add_mesh(mesh)
    plotter.export_obj(dirName + '/export.obj')

    return maxStress
