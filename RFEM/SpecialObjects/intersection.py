from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes

class Instersection():
    def __init__(self,
                 no: int = 1,
                 surface_1: int = 1,
                 surface_2: int = 2,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Intersection

        Args:
            no (int): Intersection Tag
            surface_1 (int): Surface number 1
            surface_2 (int): Surface number 2
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Intersection
        clientObject = model.clientModel.factory.create('ns0:intersection')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Intersection No.
        clientObject.no = no

        # Assigned surfaces
        clientObject.surface_a = surface_1
        clientObject.surface_b = surface_2

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Intersection to client model
        model.clientModel.service.set_intersection(clientObject)
