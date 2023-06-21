from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString

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
            no (int): Surface Mesh Refinement Tag
            surfaces (str): Assigned to Surfaces
            target_length (float): Target FE Length
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Mesh Refinement
        clientObject = model.clientModel.factory.create('ns0:surface_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

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

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface Mesh Refinement to client model
        model.clientModel.service.set_surface_mesh_refinement(clientObject)
