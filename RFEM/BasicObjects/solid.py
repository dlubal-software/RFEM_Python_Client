from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString, ConvertStrToListOfInt
from RFEM.enums import SolidType, ObjectTypes

class Solid():
    def __init__(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Numbers of Surfaces defining Solid
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Solid
        clientObject = model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = ConvertToDlString(boundary_surfaces_no)

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface to client model
        model.clientModel.service.set_solid(clientObject)

    @staticmethod
    def Standard(
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Numbers of Surfaces defining Solid
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Solid
        clientObject = model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Solid Type
        clientObject.type = SolidType.TYPE_STANDARD.name

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = ConvertToDlString(boundary_surfaces_no)

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface to client model
        model.clientModel.service.set_solid(clientObject)

    @staticmethod
    def Gas(
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Numbers of Surfaces defining Gas
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Solid
        clientObject = model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Solid Type
        clientObject.type = SolidType.TYPE_GAS.name

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = ConvertToDlString(boundary_surfaces_no)

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface to client model
        model.clientModel.service.set_solid(clientObject)

    @staticmethod
    def Contact(
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Numbers of Surfaces defining Contact
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Solid
        clientObject = model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Solid Type
        clientObject.type = SolidType.TYPE_CONTACT.name

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = ConvertToDlString(boundary_surfaces_no)

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface to client model
        model.clientModel.service.set_solid(clientObject)

    @staticmethod
    def Soil(
             no: int = 1,
             boundary_surfaces_no: str = '1 2',
             material_no: int = 1,
             comment: str = '',
             params: dict = None,
             model = Model):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Numbers of Surfaces defining Soil
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Solid
        clientObject = model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Solid Type
        clientObject.type = SolidType.TYPE_SOIL.name

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = ConvertToDlString(boundary_surfaces_no)

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface to client model
        model.clientModel.service.set_solid(clientObject)

    @staticmethod
    def DeleteSolid(solids_no: str = '1 2', model = Model):

        '''
        Args:
            solids_no (str): Numbers of Solids to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete solids from client model
        for solid in ConvertStrToListOfInt(solids_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_SOLID.name, solid)