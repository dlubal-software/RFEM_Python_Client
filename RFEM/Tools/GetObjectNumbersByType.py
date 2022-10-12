from RFEM.initModel import Model
from RFEM.enums import ObjectTypes

class GetObjectNumbersByType():

    @staticmethod
    def GetObjectNumbers(ObjectType = ObjectTypes.E_OBJECT_TYPE_NODE, model = Model):

        """Returns a sorted list which contains object numbers in RFEM tables:

            ObjectNumberList = [1, 2, ... ]

        """

        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType.name)

        if len(ObjectNumber) != 0:
            ObjectNumberList = []
            for i in range(len(ObjectNumber.item)):
                ObjectNumberList.append(ObjectNumber.item[i].no)
            ObjectNumberList.sort()
        else:
            None

        return ObjectNumberList
