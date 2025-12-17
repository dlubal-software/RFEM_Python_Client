import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.initModel import Model, CalculateInCloud
from RFEM.initModel import saveFile
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.crossSection import CrossSection
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.enums import NodalSupportType, MemberLoadDirection, ActionCategoryType
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase

Model(new_model=True, model_name='Cloudtest.rf6', delete=False)

# Create RFEM model
Model.clientModel.service.begin_modification()
Node(1)
Node(2, 5, 0, 0)

Material(1, "S235")
CrossSection(1,"IPE 300", 1)

Member(1, 1,2, 0, 1, 1)
NodalSupport(1, "1", NodalSupportType.FIXED)
NodalSupport(2, "2", NodalSupportType.HINGED)

LoadCase.StaticAnalysis(1, 'Self-Weight',analysis_settings_no=1,self_weight=[True, 0.0, 0.0, 1.0])
LoadCase.StaticAnalysis(2, 'Variable',analysis_settings_no=1,action_category=ActionCategoryType.ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_B_OFFICE_AREAS_QI_B)

MemberLoad(1, 2, "1", MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, 5000)

Model.clientModel.service.finish_modification()

saveFile(dirName + "\Cloudtest.rf6")

# Define on which server the cloud calculation should be run
server_name = "Dlu_1"

# No plausibility check should be done before cloud calculation is started
run_plausibility_check = False

# When False cloud calculation is not started when there are errors in plausibility check
calculate_despite_warnings_and_errors = False

# When true, email notifications for start and end of cloud calculation are sent
email_notification = True

result = CalculateInCloud(server_name, run_plausibility_check, calculate_despite_warnings_and_errors, email_notification)

# First list object = task ID of cloud calculation task
# Second list object = status of calculation
if result:
    task_id = result[0]
    status = result[1]
    print(f"Task-ID: {task_id}")
    print(f"Status: {status}")