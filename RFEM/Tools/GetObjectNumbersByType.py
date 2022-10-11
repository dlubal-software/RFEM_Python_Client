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
            "Line_Set": [],
            "Material": [],
            "Member": [],
            "Member_Set": [],
            "Node": [],
            "Opening": [],
            "Section": [],
            "Solid": [],
            "Solid_Set": [],
            "Surface": []
            "Surface_Set": [],
            "Thickness": [],
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
            ObjectDictionary["Line"].sort()

        # Line_Set Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_LINE_SET.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Line_Set"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Line_Set"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Line_Set"].sort()

        # Material Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_MATERIAL.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Material"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Material"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Material"].sort()

        # Member Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_MEMBER.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Member"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Member"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Member"].sort()

        # Member_Set Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_MEMBER_SET.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Member_Set"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Member_Set"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Member_Set"].sort()

        # Node Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_NODE.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Node"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Node"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Node"].sort()

        # Opening Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_OPENING.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Opening"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Opening"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Opening"].sort()

        # Section Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_SECTION.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)
        if len(ObjectNumber) != 0:

            ObjectDictionary["Section"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Section"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Section"].sort()

        # Solid Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_SOLID.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Solid"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Solid"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Solid"].sort()

        # Solid_Set Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_SOLID_SET.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Solid_Set"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Solid_Set"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Solid_Set"].sort()

        # Surface Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_SURFACE.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Surface"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Surface"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Surface"].sort()

        # Surface_Set Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_SURFACE_SET.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Surface_Set"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Surface_Set"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Surface_Set"].sort()

        # Thickness Count

        ObjectType = ObjectTypes.E_OBJECT_TYPE_THICKNESS.name
        ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(ObjectType)

        if len(ObjectNumber) != 0:

            ObjectDictionary["Thickness"] = []
            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Thickness"].append(ObjectNumber.item[i].no)
            ObjectDictionary["Thickness"].sort()

        return ObjectDictionary

