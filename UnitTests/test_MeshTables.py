import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, Calculate_all
from RFEM.enums import *
from RFEM.dataTypes import inf
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Results.meshTables import MeshTables

if Model.clientModel is None:
    Model()

def test_mesh_tables():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Node(1, 0,0,0)
    Node(2, 0,10,0)
    Node(3, 10,10,0)
    Node(4, 10,0,0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Material(1, "S235")

    Thickness(1, 'Thickness', 1, 0.02)

    Surface(1, '1 2 3 4', 1)

    Section(1, "IPE 300", 1)

    Node(5, 0,20,0)
    Node(6, 20,20,0)

    Member(1, 5, 6, 0, 1, 1)

    Model.clientModel.service.generate_mesh(True)
    Model.clientModel.service.finish_modification()

    allFeNodes = MeshTables.GetAllFENodes()
    assert allFeNodes[4]['y'] == 20

    customNode = MeshTables.GetFENodeOriginalMesh(8)
    assert customNode['y'] == 1.5

    all1DElements = MeshTables.GetAllFE1DElements()
    assert all1DElements[12]['FE_node1_no'] == 454

    all2DElemets = MeshTables.GetAllFE2DElements()
    assert all2DElemets[5]['surface_no'] == 1

    custom1DElement = MeshTables.GetFE1DElement(5)
    assert custom1DElement['FE_node2_no'] == 447

    custom2DElement = MeshTables.GetFE2DElement(18)
    assert custom2DElement['FE_node3_no'] == 37

def test_deformed_mesh():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1)
    Section(1)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 5, 0.0, 0.0)

    Member(1, 1, 2, 0.0, 1, 1)

    NodalSupport(1, '1', NodalSupportType.HINGED)
    NodalSupport(2, '2', [0, inf, inf, inf, 0, inf])
    LoadCasesAndCombinations()
    LoadCase.StaticAnalysis(1, 'Self-Weight',analysis_settings_no=1,action_category= ActionCategoryType.ACTION_CATEGORY_PERMANENT_G,self_weight=[True, 0.0, 0.0, 1.0])
    DesignSituation(1, DesignSituationType.DESIGN_SITUATION_TYPE_EQU_PERMANENT_AND_TRANSIENT, True)
    StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
    LoadCombination(1, combination_items=[[1,1,0,False]])
    LoadCombination(2, combination_items=[[1.5,1,0,False]])
    NodalLoad(1, 1, '2', NodalLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 1000)
    Model.clientModel.service.finish_modification()

    Calculate_all()

    assert Model.clientModel.service.has_any_results()
    assert MeshTables.GetAllFENodesDeformed(CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION, 2)
    assert MeshTables.GetFENodeDeformed()
