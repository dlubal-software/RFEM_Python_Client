from statistics import mode
from RFEM.initModel import Model
from RFEM.enums import ObjectTypes
from RFEM.Calculate.meshSettings import GetModelInfo



#Collecting Numbers
class GetObjectNumbersByType():

    def GetNumbers():


        print(""" Please enter a valid object type!
                    - line
                    - line_set
                    - material
                    - member
                    - member_set
                    - node
                    - opening
                    - section
                    - solid
                    - solid_set
                    - surface
                    - surface_set
                    - thickness""")
        #x = input()


        modelStatus = GetModelInfo()
        ObjectDictionary = {}

        #line
        if modelStatus.property_line_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_LINE.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Lines"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Lines"].append(i+1)


        #line_set
        if modelStatus.property_line_set_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_LINE_SET.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Line_Set"] = []

            print(k)

            for i in range(len(k.item)):
                ObjectDictionary["Line_Set"].append(i+1)

        #material
        if modelStatus.property_material_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_MATERIAL.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Material"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Material"].append(i+1)


        #member
        if modelStatus.property_member_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_MEMBER.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Member"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Member"].append(i+1)



        #member_set
        if modelStatus.property_member_set_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_MEMBER_SET.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Member_Set"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Member_Set"].append(i+1)



        #node
        if modelStatus.property_node_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_NODE.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Nodes"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Nodes"].append(i+1)


        #opening
        if modelStatus.property_opening_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_OPENING.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Opening"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Opening"].append(i+1)



        #section
        if modelStatus.property_section_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_SECTION.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Section"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Section"].append(i+1)



        #solid
        if modelStatus.property_solid_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_SOLID.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Solid"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Solid"].append(i+1)



        #solid_set
        if modelStatus.property_solid_set_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_SOLID_SET.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Solid_Set"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Solid_Set"].append(i+1)



        #surface
        if modelStatus.property_surface_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_SURFACE.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Surface"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Surface"].append(i+1)



        #surface_set
        if modelStatus.property_surface_set_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_SURFACE_SET.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Surface_Set"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Surface_Set"].append(i+1)



        #thickness
        if modelStatus.property_thickness_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_THICKNESS.name
            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Thickness"] = []

            for i in range(len(k.item)):
                ObjectDictionary["Thickness"].append(i+1)






        print(ObjectDictionary)


        #store all the values in a list
        #change the functions to a class
        #have both of the things in one function
        #just have the user type of what object the would like the numbers


