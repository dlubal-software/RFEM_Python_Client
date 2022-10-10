from RFEM.initModel import Model
from RFEM.enums import ObjectTypes
from RFEM.Calculate.meshSettings import GetModelInfo

class GetObjectNumbersByType():

    @staticmethod
    def GetBasicObjects(model = Model):

        """
        Returns a dictionary which contains basic object numbers in RFEM tables.

        ObjectDictionary = {
            "Line": [],
            "Member": [],
            "Node": [],
            "Section": [],
            "Surface": []
        }
        """

        ObjectDictionary = {}

        # Line Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_LINE.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Line"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Line"].append(ObjectNumber.item[i].no)

        # Member Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_MEMBER.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Member"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Member"].append(ObjectNumber.item[i].no)

        # Node Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_NODE.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Node"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Node"].append(ObjectNumber.item[i].no)

        # Section Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_SECTION.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)
        if len(ObjectNumber) != 0:

            ObjectDictionary["Section"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Section"].append(ObjectNumber.item[i].no)

        # Surface Count


        ObjectType = ObjectTypes.E_OBJECT_TYPE_SURFACE.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Surface"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Surface"].append(ObjectNumber.item[i].no)

        return ObjectDictionary

