from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString

class SurfaceContact():
    def __init__(self,
                 no: int = 1,
                 surfaces_contact_type: int = 1,
                 surfaces_group_1: str = '1',
                 surfaces_group_2: str = '2',
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Surface Contact

        Args:
            no (int, optional): Surface Conatct Tag
            surfaces_contact_type (int, optional): Surface Contact Type Number
            surface_group_1 (str, optional): Surfaces Group 1
            surface_group_2 (str, optional): Surfaces Group 2
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surfaces Contact
        clientObject = model.clientModel.factory.create('ns0:surfaces_contact')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surfaces Contact No.
        clientObject.no = no

        # Surface Contact Type
        clientObject.surfaces_contact_type = surfaces_contact_type

        # Surface Numbers
        clientObject.surfaces_group1 = ConvertToDlString(surfaces_group_1)
        clientObject.surfaces_group2 = ConvertToDlString(surfaces_group_2)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surfaces Contact to client model
        model.clientModel.service.set_surfaces_contact(clientObject)
