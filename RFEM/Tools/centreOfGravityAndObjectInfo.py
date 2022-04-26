from RFEM.initModel import Model
from RFEM.enums import ObjectTypes, SelectedObjectInformation

class ObjectInformation():

    @staticmethod
    def CentreOfGravity(
                        object_type = ObjectTypes.E_OBJECT_TYPE_MEMBER,
                        parent_no = 0,
                        no: int = 1,
                        coord: str = 'X'):
        '''
        This function returns the centre of gravity position (X, Y or Z) for a selected object.
        Args:
           type (enum): Object Type
           parent_no (int): Object Parent Number
                Note:
                (1) A geometric object has, in general, a parent_no = 0
                (2) The parent_no parameter becomes significant for example with loads
           no (int):  The Object Tag
           coord (str): Desired global basis vector component of the Centre of Gravity (i.e. X, Y or Z)
        '''
        result = ObjectInformation.__BuildResultsArray(object_type, no, parent_no)
        if coord == 'X' or coord.lstrip().rstrip().upper() == 'X':
            return result['section'][0].rows[0][0].value
        elif coord == 'Y' or coord.lstrip().rstrip().upper() == 'Y':
            return result['section'][0].rows[0][1].value
        elif coord == 'Z' or coord.lstrip().rstrip().upper() == 'Z':
            return result['section'][0].rows[0][2].value
        else:
            raise Exception ('WARNING: The desired Coordinate input not requested. Please provide either "X", "Y" or "Z"')

    @staticmethod
    def MemberInformation(
                          no: int = 1,
                          information = SelectedObjectInformation.LENGTH):
        '''
        This function returns further information associated with a member.
        Args:
           no (int): Member Tag
           information (enum): Desired Information (Length / Volume / Mass)
        '''
        if information.name == 'AREA':
            raise Exception ('WARNING: Area information is only relevant for Surface and Volume Information.')

        result = ObjectInformation.__BuildResultsArray(ObjectTypes.E_OBJECT_TYPE_MEMBER, no, 0)
        return ObjectInformation.__AreaVolumeMassInformationLength(information, result, 2)

    @staticmethod
    def SurfaceInformation(
                           no: int = 1,
                           information = SelectedObjectInformation.AREA):
        '''
        This function returns further information associated with a surface.
        Args:
           no (int): Surface Tag
           information (enum): Desired Information (Area / Volume / Mass)
        '''
        if information.name == 'LENGTH':
            raise Exception ('WARNING: Length information is only relevant for Member Information.')

        result = ObjectInformation.__BuildResultsArray(ObjectTypes.E_OBJECT_TYPE_SURFACE, no, 0)
        return ObjectInformation.__AreaVolumeMassInformationLength(information, result, 3)

    @staticmethod
    def SolidInformation(
                         no: int = 1,
                         information = SelectedObjectInformation.AREA):
        '''
        This function returns further information associated with a solid.
        Args:
           no (int): Solid Tag
           information (enum): Desired Information (Area / Volume / Mass)
        '''
        if information.name == 'LENGTH':
            raise Exception ('WARNING: Length information is only relevant for Member Information.')

        result = ObjectInformation.__BuildResultsArray(ObjectTypes.E_OBJECT_TYPE_SOLID, no, 0)
        return ObjectInformation.__AreaVolumeMassInformationLength(information,result, 4)

    @staticmethod
    def __BuildResultsArray(object_type, no, parent_no, model = Model):
        elements = model.clientModel.factory.create('ns0:array_of_get_center_of_gravity_and_objects_info_elements_type')
        clientObject = model.clientModel.factory.create('ns0:get_center_of_gravity_and_objects_info_element_type')
        clientObject.parent_no = parent_no
        clientObject.no = no
        clientObject.type = object_type.name
        elements.element.append(clientObject)
        result = model.clientModel.service.get_center_of_gravity_and_objects_info(elements)
        result = model.clientModel.dict(result)
        return result

    @staticmethod
    def __AreaVolumeMassInformationLength(information, result, row_key):
        if information.name == "LENGTH" or information.name == "AREA":
            return result['section'][row_key].rows[0][0].value
        elif information.name == "VOLUME":
            return result['section'][row_key].rows[0][1].value
        elif information.name == "MASS":
            return result['section'][row_key].rows[0][2].value
