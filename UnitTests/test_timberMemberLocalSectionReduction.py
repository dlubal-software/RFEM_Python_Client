import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import *
from RFEM.initModel import Model
from RFEM.TypesForTimberDesign.timberMemberLocalSectionReduction import TimberMemberLocalSectionReduction, Components
from RFEM.initModel import AddOn, SetAddonStatus

if Model.clientModel is None:
    Model()

def test_timberMemberLocalSectionReduction():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.timber_design_active, True)

    # TODO: Now only in pre-release version (8/11/2022)
    #comp1 = Components(TimberMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_RECTANGLE_OPENING)
    #comp2 = Components(TimberMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_CIRCLE_OPENING)
    comp3 = Components(TimberMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_START_NOTCH)
    comp4 = Components(TimberMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_INNER_NOTCH)
    comp5 = Components(TimberMemberLocalSectionReductionType.REDUCTION_COMPONENT_TYPE_END_NOTCH)

    #TimberMemberLocalSectionReduction(1,components=[comp1])
    #TimberMemberLocalSectionReduction(2,components=[comp2])
    TimberMemberLocalSectionReduction(3,components=[comp3])
    TimberMemberLocalSectionReduction(4,components=[comp4])
    TimberMemberLocalSectionReduction(5,components=[comp5])

    Model.clientModel.service.finish_modification()
    '''
    tmlsr_1 = Model.clientModel.service.get_timber_member_local_section_reduction(1)
    assert tmlsr_1.components[0][0].row['position'] == 1
    assert tmlsr_1.components[0][0].row['multiple'] == True
    assert tmlsr_1.components[0][0].row['multiple_number'] == 2
    assert tmlsr_1.components[0][0].row['multiple_offset'] == 1
    assert tmlsr_1.components[0][0].row['height'] == 0.5
    assert tmlsr_1.components[0][0].row['distance'] == 0.01

    tmlsr_2 = Model.clientModel.service.get_timber_member_local_section_reduction(2)
    assert tmlsr_2.components[0][0].row['position'] == 1
    assert tmlsr_2.components[0][0].row['distance'] == 0.01
    assert tmlsr_2.components[0][0].row['diameter'] == 0.05
    assert tmlsr_2.components[0][0].row['multiple'] == True
    assert tmlsr_2.components[0][0].row['multiple_number'] == 2
    assert tmlsr_2.components[0][0].row['multiple_offset'] == 2
    '''
    tmlsr_3 = Model.clientModel.service.get_timber_member_local_section_reduction(3)
    assert tmlsr_3.components[0][0].row['length'] == 0.2
    assert tmlsr_3.components[0][0].row['multiple'] == False
    assert tmlsr_3.components[0][0].row['depth'] == 0.001
