from RFEM.initModel import *

class Thickness():
    def __init__(self,
                 no: int = 1,
                 thickness_name: str = '',
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        clientObject.name = thickness_name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Uniform(self,
                 no: int = 1,
                 thickness_name: str = '',
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        clientObject.name = thickness_name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_3Nodes(self,
                 no: int = 1,
                 thickness_name: str = '',
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        clientObject.name = thickness_name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_2NodesAndDirection(self,
                 no: int = 1,
                 thickness_name: str = '',
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        clientObject.name = thickness_name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_4SurfaceCorners(self,
                 no: int = 1,
                 thickness_name: str = '',
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        clientObject.name = thickness_name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Variable_Circle(self,
                 no: int = 1,
                 thickness_name: str = '',
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        clientObject.name = thickness_name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def Layers(self,
                 no: int = 1,
                 thickness_name: str = '',
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        clientObject.name = thickness_name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def ShapeOrthotropy(self,
                 no: int = 1,
                 thickness_name: str = '',
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        clientObject.name = thickness_name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)

    def StiffnessMAtrix(self,
                 no: int = 1,
                 thickness_name: str = '',
                 material_no: int = 1,
                 uniform_thickness_d: float = 0.20,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Thickness
        clientObject = clientModel.factory.create('ns0:thickness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Thickness No.
        clientObject.no = no

        # Thickness Name
        clientObject.name = thickness_name

        # Material No.
        clientObject.material = material_no

        # Uniform Thickness d
        clientObject.uniform_thickness = uniform_thickness_d

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Thickness to client model
        clientModel.service.set_thickness(clientObject)
