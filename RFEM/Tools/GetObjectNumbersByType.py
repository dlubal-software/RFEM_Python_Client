from RFEM.initModel import Model
from RFEM.enums import ObjectTypes

class GetObjectNumbersByType:

    def __new__(cls,
                ObjectType = ObjectTypes.E_OBJECT_TYPE_NODE,
                model = Model):

        """
        Returns a sorted list which contains object numbers in RFEM tables.
        ObjectNumberList = [1, 2, ... ]

        Args:
            ObjectType (enum): Object type enum
            model(RFEM Class, optional): Model to be edited
        Returns:
            Sorted list of object numbers.
        """

        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType.name)
        ObjectNumberList = []

        if len(ObjectNumber) != 0:
            for i in range(len(ObjectNumber.item)):
                ObjectNumberList.append(ObjectNumber.item[i].no)
            ObjectNumberList.sort()

        return ObjectNumberList
