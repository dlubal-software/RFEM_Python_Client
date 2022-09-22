from RFEM.initModel import Model, clearAttributes

class SolidMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Solid Mesh Refinement
        clientObject = Model.clientModel.factory.create('ns0:solid_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid Mesh Refinement No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Mesh Refinement to client model
        Model.clientModel.service.set_solid_mesh_refinement(clientObject)
