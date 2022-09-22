from RFEM.initModel import Model, clearAttributes, ConvertToDlString
from RFEM.enums import *

class ConcreteUltimateConfiguration():

    def __init__(self,
                no: int = 1,
                name: str = 'ULS',
                members = '1',
                member_sets = '',
                surfaces = '',
                surface_sets = '',
                nodes = '',
                comment: str = '',
                params: dict = {}):
        """
        Args:
            no (int): Configuration Tag
            name (str): User Defined Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            surfaces (str): Assigned Surfaces
            surface_sets (str): Assigned Surface Sets
            nodes (str): Assigned Nodes
            comment (str, optional): Comment
            params (dict, optional): Parameters
        """

        # Client model | Concrete Durabilities
        clientObject = Model.clientModel.factory.create('ns0:uls_configuration')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Concrete Durability No.
        clientObject.no = no

        # User Defined Name
        clientObject.user_defined_name_enabled = True
        clientObject.name = name

        # Assigned Members
        clientObject.assigned_to_members = ConvertToDlString(members)

        # Assigned Member Sets
        clientObject.assigned_to_member_sets = ConvertToDlString(member_sets)

        # Assigned Surfaces
        clientObject.assigned_to_surfaces = ConvertToDlString(surfaces)

        # Assigned Surface Sets
        clientObject.assigned_to_surface_sets = ConvertToDlString(surface_sets)

        #Assinged Nodes
        clientObject.assigned_to_nodes = ConvertToDlString(nodes)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Global Parameter to client model
        Model.clientModel.service.set_uls_configuration(clientObject)