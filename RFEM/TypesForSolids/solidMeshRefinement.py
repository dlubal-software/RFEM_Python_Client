from RFEM.initModel import Model, clearAtributes

class SolidMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Solid Mesh Refinement
        clientObject = model.clientModel.factory.create('ns0:solid_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Mesh Refinement No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Solid Mesh Refinement to client model
        model.clientModel.service.set_solid_mesh_refinement(clientObject)
