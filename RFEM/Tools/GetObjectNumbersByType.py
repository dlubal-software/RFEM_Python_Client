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

        if len(ObjectNumber):
            for i in range(len(ObjectNumber.item)):
                itemCount = 0
                # this is used when requesting objects in loads (E_OBJECT_TYPE_NODAL_LOAD, E_OBJECT_TYPE_LINE_LOAD etc.)
                try:
                    itemCount = ObjectNumber.item[i].children
                # all other objects
                except:
                    itemCount = ObjectNumber.item[i].no
                ObjectNumberList.append(itemCount)

        ObjectNumberList.sort()
        return ObjectNumberList
