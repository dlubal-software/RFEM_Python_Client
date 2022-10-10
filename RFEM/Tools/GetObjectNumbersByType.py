from statistics import mode
from RFEM.initModel import Model
from RFEM.enums import ObjectTypes
from RFEM.Calculate.meshSettings import GetModelInfo



#Collecting Numbers
class GetObjectNumbersByType():

    def GetNumbers():

        modelStatus = GetModelInfo()
        ObjectDictionary = {}

        #line
        if modelStatus.property_line_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_LINE.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Line"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Line"].append(ObjectNumber.item[i].no)


        #line_set
        #no function defined for get_line_set_count in getmodelinfo()

        #material
        #no function defined for get_material_count in getmodelinfo()

        #member
        if modelStatus.property_member_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_MEMBER.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Member"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Member"].append(ObjectNumber.item[i].no)

        #member_set
        #no function defined for get_member_set_count in getmodelinfo()

        #node
        if modelStatus.property_node_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_NODE.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Node"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Node"].append(ObjectNumber.item[i].no)

        #opening
        #no function defined for get_opening_count in getmodelinfo()

        #section
        if modelStatus.property_rsection_element_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_SECTION.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Section"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Section"].append(ObjectNumber.item[i].no)

        #solid
        #no function defined for get_solid_count in getmodelinfo()

        #solid_set
        #no function defined for get_solid_set_count in getmodelinfo()

        #surface
        if modelStatus.property_surface_count != 0:

            objecttype = ObjectTypes.E_OBJECT_TYPE_SURFACE.name
            ObjectNumber = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)
            ObjectDictionary["Surface"] = []

            for i in range(len(ObjectNumber.item)):
                ObjectDictionary["Surface"].append(ObjectNumber.item[i].no)

        #surface_set
        #no function defined for get_surface_set_count in getmodelinfo()
        #thickness
        #no function defined for get_thickness_count in getmodelinfo()


        print(ObjectDictionary)

        #store all the values in a list
        #change the functions to a class
        #have both of the things in one function
        #just have the user type of what object the would like the numbers


