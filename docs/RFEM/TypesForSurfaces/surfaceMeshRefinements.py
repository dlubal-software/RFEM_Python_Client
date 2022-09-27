from RFEM.initModel import Model, clearAttributes

class SurfaceMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Surface Mesh Refinement
        clientObject = Model.clientModel.factory.create('ns0:surface_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Mesh Refinement No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface Mesh Refinement to client model
        Model.clientModel.service.set_surface_mesh_refinement(clientObject)
