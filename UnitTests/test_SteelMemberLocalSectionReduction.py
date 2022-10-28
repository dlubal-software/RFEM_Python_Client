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


@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel, 'steel_member_local_section_reduction', True), reason="steel_member_local_section_reduction not in RFEM GM yet")
def test_SteelMemberLocalSectionReduction():

    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.steel_design_active, True)

    SteelMemberLocalSectionReduction(1, "", "",
        [
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 1, False, FastenerDefinitionType.DEFINITION_TYPE_ABSOLUTE, 0.2, 0, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 0.0]
        ],
        "")

    SteelMemberLocalSectionReduction(2, "", "",
        [
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 1.2, True, FastenerDefinitionType.DEFINITION_TYPE_ABSOLUTE, 0.1, 2, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 2],
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 2.0, True, FastenerDefinitionType.DEFINITION_TYPE_RELATIVE, 0.20, 3, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_RELATIVE, 0.1]
        ],
        "")

    SteelMemberLocalSectionReduction(3, "", "",
        [
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 1.5, False, FastenerDefinitionType.DEFINITION_TYPE_RELATIVE, 0.15, 0, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 0.0],
            [SteelMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_DESIGN_PARAMETERS, 1.8, True, FastenerDefinitionType.DEFINITION_TYPE_RELATIVE, 0.25, 4, MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE, 0.3]
        ], ""
        )

    smlr_1 = Model.clientModel.service.get_steel_member_local_section_reduction(1)
    assert smlr_1.components[0][0].row['position'] == 1
    assert smlr_1.components[0][0].row['multiple'] == False
    assert smlr_1.components[0][0].row['fastener_definition_type'] == 'DEFINITION_TYPE_ABSOLUTE'
    assert smlr_1.components[0][0].row['reduction_area'] == 0.2

    smlr_2 = Model.clientModel.service.get_steel_member_local_section_reduction(2)
    assert smlr_2.components[0][0].row['position'] == 1.2
    assert smlr_2.components[0][0].row['multiple'] == True
    assert smlr_2.components[0][1].row['fastener_definition_type'] == 'DEFINITION_TYPE_RELATIVE'
    assert smlr_2.components[0][1].row['reduction_area_factor'] == 0.20
    assert smlr_2.components[0][0].row['multiple_offset'] == 2

    smlr_3 = Model.clientModel.service.get_steel_member_local_section_reduction(3)
    assert smlr_3.components[0][1].row['position'] == 1.8
    assert smlr_3.components[0][0].row['multiple'] == False
    assert smlr_3.components[0][1].row['multiple'] == True
    assert smlr_3.components[0][1].row['multiple_offset_definition_type'] == 'OFFSET_DEFINITION_TYPE_ABSOLUTE'
    assert smlr_3.components[0][1].row['multiple_offset'] == 0.3

    Model.clientModel.service.finish_modification()
