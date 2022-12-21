from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes

class SolidMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 target_length: float = 0.15,
                 solids: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Solids Mesh Refinemet

        Args:
            no (int): Solid Contact Tag
            target_length (float): Target FE Length
            solids (str): Assigned to solids
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Solid Mesh Refinement
        clientObject = model.clientModel.factory.create('ns0:solid_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid Mesh Refinement No.
        clientObject.no = no

        # Target FE length
        clientObject.target_length = target_length

        # Assigned to solids
        clientObject.solids = solids

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Solid Mesh Refinement to client model
        model.clientModel.service.set_solid_mesh_refinement(clientObject)
