#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.initModel import Model, CalculateInCloud


model = Model(new_model=False, model_name='0_Stahlbetonmodell.rf6', delete=False)

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
if result:
    task_id = result[0]
    status = result[1]
    print(f"Task-ID: {task_id}")
    print(f"Status: {status}")

# Second list object = status of calculation

