import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import SteelMemberLocalSectionReductionType, FastenerDefinitionType, MultipleOffsetDefinitionType
from RFEM.initModel import Model, CheckIfMethodOrTypeExists
from RFEM.TypesForSteelDesign.SteelMemberLocalSectionReduction import SteelMemberLocalSectionReduction
from RFEM.initModel import AddOn, SetAddonStatus
import pytest


if Model.clientModel is None:
    Model()


@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel, 'set_model_settings_and_options', True), reason="set_model_settings_and_options not in RFEM GM yet")

def test_SteelMemberLocalSectionReduction():

    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.steel_design_active, True)

    SteelMemberLocalSectionReduction(1, "", "",
        [
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 1, False, 0, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 0.0, FastenerDefinitionType.DEFINITION_TYPE_ABSOLUTE, 0.2]
        ],
        [False])

    SteelMemberLocalSectionReduction(2, "", "",
        [
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 1.2, True, 2, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 0.2, FastenerDefinitionType.DEFINITION_TYPE_ABSOLUTE, 0.1],
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 2.0, True, 3, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_RELATIVE, 10.0, FastenerDefinitionType.DEFINITION_TYPE_RELATIVE, 20]
        ],
        [False])

    SteelMemberLocalSectionReduction(3, "", "",
        [
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 1.5, False, 0, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 0.0, FastenerDefinitionType.DEFINITION_TYPE_RELATIVE, 15],
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 1.8, True, 4, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 0.3, FastenerDefinitionType.DEFINITION_TYPE_RELATIVE, 25]
        ],
        [False])

    smlr_1 = Model.clientModel.service.get_steel_member_local_section_reduction(1)
    assert smlr_1.components[0][1].row['position'] == 1
    assert smlr_1.components[0][2].row['multiple'] == False
    assert smlr_1.components[0][6].row['fastener_definition_type'] == 'DEFINITION_TYPE_ABSOLUTE'
    assert smlr_1.components[0][7].row['reduction_area'] == 0.2

    smlr_2 = Model.clientModel.service.get_steel_member_local_section_reduction(2)
    assert smlr_2.components[0][1].row['position'] == 1.2
    assert smlr_2.components[0][2].row['multiple'] == True
    assert smlr_2.components[1][6].row['fastener_definition_type'] == 'DEFINITION_TYPE_RELATIVE'
    assert smlr_2.components[1][7].row['reduction_area'] == 20

    smlr_3 = Model.clientModel.service.get_steel_member_local_section_reduction(3)
    assert smlr_3.components[0][1].row['position'] == 1.5
    assert smlr_3.components[0][2].row['multiple'] == False
    assert smlr_3.components[1][4].row['multiple_offset_definition_type'] == 'OFFSET_DEFINITION_TYPE_ABSOLUTE'
    assert smlr_3.components[1][5].row['multiple_offset'] == 0.3

    # assert smlr_1.components[][].row[''] ==
    # assert Model.clientModel is not None, "WARNING: clientModel is not initialized"

    Model.clientModel.service.finish_modification()

