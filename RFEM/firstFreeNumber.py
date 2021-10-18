from RFEM.initModel import *
from RFEM.enums import ObjectTypes

def FirstFreeNumber(type = ObjectTypes.E_OBJECT_TYPE_MEMBER,
                    parent_no: int = 0):

                    return clientModel.service.get_first_free_number(type.name, parent_no)