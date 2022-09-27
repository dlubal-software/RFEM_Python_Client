from RFEM.initModel import Model, clearAttributes, ConvertToDlString
from RFEM.enums import LineMeshRefinementsType

class LineMeshRefinements():
    TypeSpecificParams = {'target_length': 0.1, #Target FE Length Type
                          'elements_finite_elements': 0, # Number Finite Elements Type
                          'gradual_rows': 0} # Gradually Type
    def __init__(self,
                 no: int = 1,
                 lines: str = '3 4 5',
                 type = LineMeshRefinementsType.TYPE_LENGTH,
                 number_of_layers: int = 2,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line Mesh Refinement
        clientObject = Model.clientModel.factory.create('ns0:line_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Line Mesh Refinement No.
        clientObject.no = no

        # Assigned to lines
        clientObject.lines = ConvertToDlString(lines)

        # Line Mesh Refinement Type
        clientObject.type = type.name

        # Number of layers
        clientObject.number_of_layers = number_of_layers

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line Mesh Refinement to client model
        Model.clientModel.service.set_line_mesh_refinement(clientObject)

    def TargetFELength(self,
                       no: int = 1,
                       lines: str = '3 4 5',
                       target_length: float = 0.1,
                       number_of_layers: int = 2,
                       comment: str = '',
                       params: dict = {}):

        # Client model | Line Mesh Refinement
        clientObject = Model.clientModel.factory.create('ns0:line_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Line Mesh Refinement No.
        clientObject.no = no

        # Assigned to lines
        clientObject.lines = ConvertToDlString(lines)

        # Line Mesh Refinement Type
        clientObject.type = LineMeshRefinementsType.TYPE_LENGTH.name

        # Target Length
        clientObject.target_length = target_length

        # Number of layers
        clientObject.number_of_layers = number_of_layers

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line Mesh Refinement to client model
        Model.clientModel.service.set_line_mesh_refinement(clientObject)

    def NumberFiniteElements(self,
                             no: int = 1,
                             lines: str = '3 4 5',
                             elements_finite_elements: int = 10,
                             number_of_layers: int = 2,
                             comment: str = '',
                             params: dict = {}):

        # Client model | Line Mesh Refinement
        clientObject = Model.clientModel.factory.create('ns0:line_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Line Mesh Refinement No.
        clientObject.no = no

        # Assigned to lines
        clientObject.lines = ConvertToDlString(lines)

        # Line Mesh Refinement Type
        clientObject.type = LineMeshRefinementsType.TYPE_ELEMENTS.name

        # Target Length
        clientObject.elements_finite_elements = elements_finite_elements

        # Number of layers
        clientObject.number_of_layers = number_of_layers

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line Mesh Refinement to client model
        Model.clientModel.service.set_line_mesh_refinement(clientObject)

    def Gradually(self,
                  no: int = 1,
                  lines: str = '3 4 5',
                  gradual_rows: int = 10,
                  number_of_layers: int = 2,
                  comment: str = '',
                  params: dict = {}):

        # Client model | Line Mesh Refinement
        clientObject = Model.clientModel.factory.create('ns0:line_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Line Mesh Refinement No.
        clientObject.no = no

        # Assigned to lines
        clientObject.lines = ConvertToDlString(lines)

        # Line Mesh Refinement Type
        clientObject.type = LineMeshRefinementsType.TYPE_GRADUAL.name

        # Target Length
        clientObject.gradual_rows = gradual_rows

        # Number of layers
        clientObject.number_of_layers = number_of_layers

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line Mesh Refinement to client model
        Model.clientModel.service.set_line_mesh_refinement(clientObject)
