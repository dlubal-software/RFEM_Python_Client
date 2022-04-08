import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model
from RFEM.enums import NodalSupportType, StaticAnalysisType, LoadDirectionType

if Model.clientModel is None:
    Model()

def test_nodal_load():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Section
    Section(1, 'IPE 300', 1)

    # Create Nodes
    Node(1, 0, 0, 0)
    Node(2, 0, 0, -5)

    Node(3, 3, 0, 0)
    Node(4, 3, 0, -5)

    Node(5, 6, 0, 0)
    Node(6, 6, 0, -5)

    Node(7, 9, 0, 0)
    Node(8, 9, 0, -5)

    # Create Nodal Supports
    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '3', NodalSupportType.FIXED)
    NodalSupport(3, '5', NodalSupportType.FIXED)
    NodalSupport(4, '7', NodalSupportType.FIXED)

    # Create Member
    Member(1,  1, 2, 0, 1, 1)
    Member(2,  3, 4, 0, 1, 1)
    Member(3,  5, 6, 0, 1, 1)
    Member(4,  7, 8, 0, 1, 1)

    # Create Static Analysis Settings
    StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Create Load Case
    LoadCase(1, 'DEAD', [True, 0.0, 0.0, 1.0])

    # Initial Nodal Load
    NodalLoad(1, 1, '2', LoadDirectionType.LOAD_DIRECTION_LOCAL_X, 5000)

    # Force Type Nodal Load
    NodalLoad.Force(2, 1, '2', LoadDirectionType.LOAD_DIRECTION_LOCAL_X, 5000)

    # Moment Type Nodal Load
    NodalLoad.Moment(3, 1, '4', LoadDirectionType.LOAD_DIRECTION_LOCAL_X, 5000)

    # Component Type Nodal Load
    NodalLoad.Components(4, 1, '6', [5000, 5000, 0, 0, 5000, 0])

    #Mass Type Nodal Load
    NodalLoad.Mass(5, 1, '8', True, [5000, 5000, 0, 0, 5000, 0])

    #Calculate_all() # Don't use in unit tests. See template for more info.

    Model.clientModel.service.finish_modification()
