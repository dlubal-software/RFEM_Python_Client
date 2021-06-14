from RFEM.initModel import *

class Solid():
    def __init__(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Solid
        clientObject = clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = boundary_surfaces_no

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_solid(clientObject)

    def Standard(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Solid
        clientObject = clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = boundary_surfaces_no

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_solid(clientObject)

    def Gas(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Solid
        clientObject = clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = boundary_surfaces_no

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_solid(clientObject)

    def Contact(self,
                 no: int = 1,
                 boundary_surfaces_no: str = '1 2',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Solid
        clientObject = clientModel.factory.create('ns0:solid')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid No.
        clientObject.no = no

        # Surfaces No. (e.g. "5 7 8 12 5")
        clientObject.boundary_surfaces = boundary_surfaces_no

        # Material
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface to client model
        clientModel.service.set_solid(clientObject)
