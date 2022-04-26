from RFEM.initModel import Model, clearAtributes

class SurfaceMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Surface Mesh Refinement
        clientObject = model.clientModel.factory.create('ns0:surface_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Mesh Refinement No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Mesh Refinement to client model
        model.clientModel.service.set_surface_mesh_refinement(clientObject)
