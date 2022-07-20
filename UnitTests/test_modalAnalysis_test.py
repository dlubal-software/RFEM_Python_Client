import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import NodalSupportType, StaticAnalysisType, ModalSolutionMethod
from RFEM.enums import ModalMassConversionType, ModalMassMatrixType, AnalysisType, AddOn
from RFEM.initModel import Model, SetAddonStatus
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.modalAnalysisSettings import ModalAnalysisSettings

if Model.clientModel is None:
    Model()

def test_modal_analysis_settings():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Crate Section
    Section(1, 'IPE 300', 1)

    # Create Nodes
    Node(1, 0, 0, 0)
    Node(2, 0, 0, -5)

    # Create Member
    Member(1, 1, 2, 0, 1, 1)

    # Create Nodal Support
    NodalSupport(1, '1', NodalSupportType.FIXED)

    SetAddonStatus(Model.clientModel, AddOn.modal_active)

    # Static Analysis Settings
    StaticAnalysisSettings(1, 'Geometrically Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Modal Analysis Settings
    ModalAnalysisSettings(acting_masses=[True, False, True, False, True, False])
    ModalAnalysisSettings(2, 'Modal Analysis Settings 1', ModalSolutionMethod.METHOD_LANCZOS, ModalMassConversionType.MASS_CONVERSION_TYPE_Z_COMPONENTS_OF_LOADS,
                          ModalMassMatrixType.MASS_MATRIX_TYPE_DIAGONAL, 2, [False, False, False, False, True, True])

    # Load Case Static
    LoadCase(1, 'DEAD', [True, 0, 0, 1])
    modalParams = {
        "analysis_type": AnalysisType.ANALYSIS_TYPE_MODAL.name,
        "modal_analysis_settings":1,
    }

    # Load Case Modal
    LoadCase(2, 'MODAL',params=modalParams)

    Model.clientModel.service.finish_modification()

    actingMasses = Model.clientModel.service.get_modal_analysis_settings(1)
    assert actingMasses.acting_masses_about_axis_x_enabled == True
    assert actingMasses.acting_masses_about_axis_y_enabled == False
    assert actingMasses.acting_masses_about_axis_z_enabled == True
    assert actingMasses.acting_masses_in_direction_x_enabled == False
    assert actingMasses.acting_masses_in_direction_y_enabled == True
    assert actingMasses.acting_masses_in_direction_z_enabled == False

    actingMasses = Model.clientModel.service.get_modal_analysis_settings(2)
    assert actingMasses.acting_masses_about_axis_x_enabled == False
    assert actingMasses.acting_masses_about_axis_y_enabled == False
    assert actingMasses.acting_masses_about_axis_z_enabled == False
    assert actingMasses.acting_masses_in_direction_x_enabled == False
    assert actingMasses.acting_masses_in_direction_y_enabled == True
    assert actingMasses.acting_masses_in_direction_z_enabled == True
    assert actingMasses.solution_method == 'METHOD_LANCZOS'
    assert actingMasses.mass_conversion_type == 'MASS_CONVERSION_TYPE_Z_COMPONENTS_OF_LOADS'
    assert actingMasses.mass_matrix_type == 'MASS_MATRIX_TYPE_DIAGONAL'
    assert actingMasses.number_of_modes == 2
