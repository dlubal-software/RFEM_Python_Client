from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import TimberServiceClassServiceClass

class TimberServiceClass():
    def __init__(self,
                no: int = 1,
                name: str = '',
                members: str = '',
                member_sets: str = '',
                surfaces: str = '',
                surface_sets: str = '',
                service_class = TimberServiceClassServiceClass.TIMBER_SERVICE_CLASS_TYPE_1,
                comment: str = '',
                params: dict = None):
        """
        Args:
            no (int): Timber Member Shear Panel Tag
            name (str): User Defined Member Shear Panel Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            surfaces (str): Assigned Surfaces
            surface_sets (str): Assigned Surface Sets
            service_class (enum): Timber Service Class Service Class
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        """

         # Client Model | Types For Timber Design Service Class
        clientObject = Model.clientModel.factory.create('ns0:timber_service_class')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Service Class
        clientObject.no = no

        # Assigned Members
        clientObject.member = ConvertToDlString(members)

        # Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Assigned Surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Assigned Surface Sets
        clientObject.surface_sets = ConvertToDlString(surface_sets)

        # Service Class
        clientObject.service_class = service_class.name

        # User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Service Class to client model
        Model.clientModel.service.set_timber_service_class(clientObject)
