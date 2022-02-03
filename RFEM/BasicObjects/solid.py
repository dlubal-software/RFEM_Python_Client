from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import SolidType

class Solid():
    def __init__(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Tags of Surfaces defining Solid
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Solid
        clientObject = Model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = ConvertToDlString(boundary_surfaces_no)

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        Model.clientModel.service.set_solid(clientObject)

    def Standard(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Tags of Surfaces defining Solid
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Solid
        clientObject = Model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        Model.clientModel.service.set_solid(clientObject)

    def Gas(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Tags of Surfaces defining Gas
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Solid
        clientObject = Model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        Model.clientModel.service.set_solid(clientObject)

    def Contact(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Tags of Surfaces defining Contact
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Solid
        clientObject = Model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        Model.clientModel.service.set_solid(clientObject)

    def Soil(self,
             no: int = 1,
             boundary_surfaces_no: str = '1 2',
             material_no: int = 1,
             comment: str = '',
             params: dict = {}):

        '''
        Args:
            no (int): Solid Tag
            boundary_surfaces_no (str): Tags of Surfaces defining Soil
            material_no (int): Tag of Material assigned to Solid
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Solid
        clientObject = Model.clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        Model.clientModel.service.set_solid(clientObject)