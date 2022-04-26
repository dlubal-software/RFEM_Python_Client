from RFEM.initModel import Model, clearAtributes, ConvertToDlString

class SurfaceMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 surfaces: str = "1",
                 target_length: float = 0.2,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Surface Mesh Refinement

        Args:
            no (int, optional): _description_. Defaults to 1.
            surfaces (str, optional): _description_. Defaults to "1".
            target_length (float, optional): _description_. Defaults to 0.1.
            comment (str, optional): _description_. Defaults to ''.
            params (dict, optional): _description_. Defaults to None.
        """

        # Client model | Surface Mesh Refinement
        clientObject = model.clientModel.factory.create('ns0:surface_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Mesh Refinement No.
        clientObject.no = no

        # Assigned to Surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Target FE Length
        clientObject.target_length = target_length

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Mesh Refinement to client model
        model.clientModel.service.set_surface_mesh_refinement(clientObject)
