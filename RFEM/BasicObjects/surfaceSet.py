from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import SetType

class SurfaceSet():
    def __init__(self,
                 no: int = 1,
                 surfaces_no: str = '2 4 7',
                 surface_set_type = SetType.SET_TYPE_GROUP,
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Surfaces Set Tag
            surfaces_no (str): Tags of Surfaces Contained Within Surface Set
            surfaces_set_type (enum): Surface Set Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Surface Set
        clientObject = Model.clientModel.factory.create('ns0:surface_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Set No.
        clientObject.no = no

        # Surfaces number
        clientObject.surfaces = ConvertToDlString(surfaces_no)

        # Surface Set Type
        clientObject.set_type = surface_set_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface Set to client model
        Model.clientModel.service.set_surface_set(clientObject)

    def ContinuousSurfaces(self,
                 no: int = 1,
                 surfaces_no: str = '2 4 7',
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Surfaces Set Tag
            surfaces_no (str): Tags of Surfaces Contained Within Continuous Surface Set
            surfaces_set_type (enum): Surface Set Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Surface Set
        clientObject = Model.clientModel.factory.create('ns0:surface_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Set No.
        clientObject.no = no

        # Surfaces number
        clientObject.surfaces = ConvertToDlString(surfaces_no)

        # Surface Set Type
        clientObject.set_type = SetType.SET_TYPE_CONTINUOUS.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface Set to client model
        Model.clientModel.service.set_surface_set(clientObject)

    def GroupOfSurfaces(self,
                 no: int = 1,
                 surfaces_no: str = '2 4 7',
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Surfaces Set Tag
            surfaces_no (str): Tags of Surfaces Contained Within Group of Surfaces Surface Set
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Surface Set
        clientObject = Model.clientModel.factory.create('ns0:surface_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Set No.
        clientObject.no = no

        # Surfaces number
        clientObject.surfaces = ConvertToDlString(surfaces_no)

        # Surface Set Type
        clientObject.set_type = SetType.SET_TYPE_GROUP.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface Set to client model
        Model.clientModel.service.set_surface_set(clientObject)
