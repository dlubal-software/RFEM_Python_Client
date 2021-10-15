import sys
sys.path.append(".")

from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *

print(clientModel.service.get_center_of_gravity_and_objects_info())

# class CentreOfGravityAndObjectInformation():

#     def Member(self,
#                ElmNum: int = 1,
#                ParentNo: int = 0):


#             type = ObjectTypes.E_OBJECT_TYPE_MEMBER.name
#             centerOfGravityAndObjectInformation = clientModel.service.get_center_of_gravity_and_objects_info(type, ElmNum, ParentNo)
#             print(centerOfGravityAndObjectInformation)

        # if centerOfGravityAndObjectInformation != None:
        #     for i in range(0, len(centerOfGravityAndObjectInformation.row)):
        #         for j in range(0, len(centerOfGravityAndObjectInformation.row[i].section)):

        #             if hasattr(centerOfGravityAndObjectInformation.row[i].section[j], 'top_text'):
        #                 print(centerOfGravityAndObjectInformation.row[i].section[j].top_text)

        #             for k in range(0, len(centerOfGravityAndObjectInformation.row[i].section[j].elements[0])):
        #                 print(centerOfGravityAndObjectInformation.row[i].section[j].elements[0][k].column_name +
        #                       " " + centerOfGravityAndObjectInformation.row[i].section[j].elements[0][k].value)