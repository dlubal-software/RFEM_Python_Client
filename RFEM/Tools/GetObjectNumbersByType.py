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

        modelStatus = GetModelInfo()
        ObjectDictionary = {}

        # Line Count
        if modelStatus.property_line_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_LINE.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Line"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Line"].append(ObjectNumber.item[i].no)

        # Member Count
        if modelStatus.property_member_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_MEMBER.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Member"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Member"].append(ObjectNumber.item[i].no)

        # Node Count
        if modelStatus.property_node_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_NODE.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Node"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Node"].append(ObjectNumber.item[i].no)

        # Section Count
        if modelStatus.property_rsection_element_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_SECTION.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Section"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Section"].append(ObjectNumber.item[i].no)

        # Surface Count
        if modelStatus.property_surface_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_SURFACE.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Surface"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Surface"].append(ObjectNumber.item[i].no)

        return ObjectDictionary

