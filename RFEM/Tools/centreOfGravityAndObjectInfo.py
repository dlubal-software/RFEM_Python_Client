from RFEM.initModel import *
from RFEM.enums import *

class ObjectInformation():

        def CentreOfGravity(self,
                            object_type = ObjectTypes.E_OBJECT_TYPE_MEMBER,
                            no: int = 1,
                            parent_no = 0,
                            coord: str = 'X'):

                self.object_type = object_type
                self.no = no
                self.parent_no = parent_no
                
                result = ObjectInformation.__BuildResultsArray(self)

                if coord == 'X' or coord.lstrip().rstrip().upper() == 'X':
                        return result['section'][0].rows[0][0].value
                elif coord == 'Y' or coord.lstrip().rstrip().upper() == 'Y':
                        return result['section'][0].rows[0][1].value
                elif coord == 'Z' or coord.lstrip().rstrip().upper() == 'Z':
                        return result['section'][0].rows[0][2].value
                else:
                        raise Exception ('WARNING: The desired Coordinate input not requested. Please provide either "X", "Y" or "Z"')

        def MemberInformation(self,
                              no: int = 1,
                              information = SelectedObjectsInformation.LENGTH):

                if information.name == 'AREA':
                        raise Exception ('WARNING: Area information is only relevant for Surface and Volume Information.')
                
                self.object_type = ObjectTypes.E_OBJECT_TYPE_MEMBER
                self.no = no
                self.parent_no = 0
                self.information = information
                self.row_key = 2
                self.result = ObjectInformation.__BuildResultsArray(self)

                return ObjectInformation.__AreaVolumeMassInformationLength(self)

        def SurfaceInformation(self,
                              no: int = 1,
                              information = SelectedObjectsInformation.AREA):

                if information.name == 'LENGTH':
                        raise Exception ('WARNING: Length information is only relevant for Member Information.')

                self.object_type = ObjectTypes.E_OBJECT_TYPE_SURFACE
                self.no = no
                self.parent_no = 0
                self.information = information
                self.row_key = 3              
                self.result = ObjectInformation.__BuildResultsArray(self)

                return ObjectInformation.__AreaVolumeMassInformationLength(self)

        def SolidInformation(self,
                              no: int = 1,
                              information = SelectedObjectsInformation.AREA):

                if information.name == 'LENGTH':
                        raise Exception ('WARNING: Length information is only relevant for Member Information.')

                self.object_type = ObjectTypes.E_OBJECT_TYPE_SOLID
                self.no = no
                self.parent_no = 0
                self.information = information
                self.row_key = 4
                self.result = ObjectInformation.__BuildResultsArray(self)

                return ObjectInformation.__AreaVolumeMassInformationLength(self)

        def __BuildResultsArray(self):
                
                elements = clientModel.factory.create('ns0:array_of_get_center_of_gravity_and_objects_info_elements_type')
                clientObject = clientModel.factory.create('ns0:get_center_of_gravity_and_objects_info_element_type')
                clientObject.parent_no = self.parent_no
                clientObject.no = self.no
                clientObject.type = self.object_type.name
                elements.element.append(clientObject)
                result = clientModel.service.get_center_of_gravity_and_objects_info(elements)
                result = clientModel.dict(result)
                
                return result
        
        def __AreaVolumeMassInformationLength(self):

                if self.information.name == "LENGTH" or self.information.name == "AREA":
                        return self.result['section'][self.row_key].rows[0][0].value
                elif self.information.name == "VOLUME":
                        return self.result['section'][self.row_key].rows[0][1].value
                elif self.information.name == "MASS":
                        return self.result['section'][self.row_key].rows[0][2].value