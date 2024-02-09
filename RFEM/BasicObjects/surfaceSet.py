from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString, ConvertStrToListOfInt
from RFEM.enums import SetType, ObjectTypes

class SurfaceSet():
    def __init__(self,
                 no: int = 1,
                 surfaces_no: str = '2 4 7',
                 surface_set_type = SetType.SET_TYPE_GROUP,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surfaces Set Tag
            surfaces_no (str): Numbers of Surfaces Contained Within Surface Set
            surfaces_set_type (enum): Surface Set Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Surface Set
        clientObject = model.clientModel.factory.create('ns0:surface_set')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Set No.
        clientObject.no = no

        # Surfaces number
        clientObject.surfaces = ConvertToDlString(surfaces_no)

        # Surface Set Type
        clientObject.set_type = surface_set_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface Set to client model
        model.clientModel.service.set_surface_set(clientObject)

    @staticmethod
    def ContinuousSurfaces(
                 no: int = 1,
                 surfaces_no: str = '2 4 7',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surfaces Set Tag
            surfaces_no (str): Numbers of Surfaces Contained Within Continuous Surface Set
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Surface Set
        clientObject = model.clientModel.factory.create('ns0:surface_set')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Set No.
        clientObject.no = no

        # Surfaces number
        clientObject.surfaces = ConvertToDlString(surfaces_no)

        # Surface Set Type
        clientObject.set_type = SetType.SET_TYPE_CONTINUOUS.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface Set to client model
        model.clientModel.service.set_surface_set(clientObject)

    @staticmethod
    def GroupOfSurfaces(
                 no: int = 1,
                 surfaces_no: str = '2 4 7',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surfaces Set Tag
            surfaces_no (str): Numbers of Surfaces Contained Within Group of Surfaces Surface Set
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Surface Set
        clientObject = model.clientModel.factory.create('ns0:surface_set')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Set No.
        clientObject.no = no

        # Surfaces number
        clientObject.surfaces = ConvertToDlString(surfaces_no)

        # Surface Set Type
        clientObject.set_type = SetType.SET_TYPE_GROUP.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface Set to client model
        model.clientModel.service.set_surface_set(clientObject)

    @staticmethod
    def DeleteSurfaceSet(surfaces_no: str = '1 2', model = Model):

        '''
        Args:
            surfaces_no (str): Numbers of Surface Sets to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete surface sets from the client model
        for surface in ConvertStrToListOfInt(surfaces_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_SURFACE_SET.name, surface)

    @staticmethod
    def GetSurfaceSet(object_index: int = 1, model = Model):

        '''
        Args:
            obejct_index (int): Surface Set Index
            model (RFEM Class, optional): Model to be edited
        '''

        # Get Surface Set from client model
        return model.clientModel.service.get_surface_set(object_index)
