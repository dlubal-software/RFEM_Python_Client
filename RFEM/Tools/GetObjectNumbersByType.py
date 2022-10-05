from RFEM.initModel import Model
from RFEM.enums import ObjectTypes


#Collecting Numbers
class GetObjectNumbersByType():


    def GetNumbers():

    #Ask for which type of object answer should be obtained

        x = input("From which object type would you like information?")
        objecttype = 0

        while objecttype == 0:

            #line
            if x == 'line':
                objecttype = ObjectTypes.E_OBJECT_TYPE_LINE

            #lineSet
            if x == 'line_set':
                objecttype = ObjectTypes.E_OBJECT_TYPE_LINE_SET

            #material
            if x == 'material':
                objecttype = ObjectTypes.E_OBJECT_TYPE_MATERIAL

            #member
            if x == 'member':
                objecttype = ObjectTypes.E_OBJECT_TYPE_MEMBER

            #memberSet
            if x == 'member_set':
                objecttype = ObjectTypes.E_OBJECT_TYPE_MEMBER_SET

            #node
            if x == 'node':
                objecttype = ObjectTypes.E_OBJECT_TYPE_NODE

            #opening
            if x == 'opening':
                objecttype = ObjectTypes.E_OBJECT_TYPE_OPENING

            #section
            if x == 'section':
                objecttype = ObjectTypes.E_OBJECT_TYPE_SECTION

            #solid
            if x == 'solid':
                objecttype = ObjectTypes.E_OBJECT_TYPE_SOLID

            #solidSet
            if x == 'solid_set':
                objecttype = ObjectTypes.E_OBJECT_TYPE_SOLID_SET

            #surface
            if x == 'surface':
                objecttype = ObjectTypes.E_OBJECT_TYPE_SURFACE

            #surfaceSet
            if x == 'surface_set':
                objecttype = ObjectTypes.E_OBJECT_TYPE_SURFACE_SET

            #thickness
            if x == 'thickness':
                objecttype = ObjectTypes.E_OBJECT_TYPE_THICKNESS

            else:
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
                x = input()



        eList = []

        #line
        if objecttype == ObjectTypes.E_OBJECT_TYPE_LINE:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)

        #line_set
        if objecttype == ObjectTypes.E_OBJECT_TYPE_LINE_SET:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #material
        if objecttype == ObjectTypes.E_OBJECT_TYPE_MATERIAL:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #member
        if objecttype == ObjectTypes.E_OBJECT_TYPE_MEMBER:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #member_set
        if objecttype == ObjectTypes.E_OBJECT_TYPE_MEMBER_SET:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #node
        if objecttype == ObjectTypes.E_OBJECT_TYPE_NODE:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #opening
        if objecttype == ObjectTypes.E_OBJECT_TYPE_OPENING:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #section
        if objecttype == ObjectTypes.E_OBJECT_TYPE_SECTION:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #solid
        if objecttype == ObjectTypes.E_OBJECT_TYPE_SOLID:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #solid_set
        if objecttype == ObjectTypes.E_OBJECT_TYPE_SOLID_SET:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #surface
        if objecttype == ObjectTypes.E_OBJECT_TYPE_SURFACE:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #surface_set
        if objecttype == ObjectTypes.E_OBJECT_TYPE_SURFACE_SET:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)
        #thickness
        if objecttype == ObjectTypes.E_OBJECT_TYPE_THICKNESS:

            k = Model.clientModel.service.get_all_object_numbers_by_type(objecttype)

            for i in k:
                eList.append(i)

        return eList


        #store all the values in a list
        #change the functions to a class
        #have both of the things in one function
        #just have the user type of what object the would like the numbers


