from RFEM.initModel import Model, clearAtributes, ConvertToDlString

class ConcreteServiceabilityConfiguration():

    def __init__(self,
                no: int = 1,
                name: str = 'SLS',
                members: str = '1',
                member_sets: str = '',
                surfaces: str = '',
                surface_sets: str = '',
                nodes: str = '',
                comment: str = '',
                params: dict = None,
                model = Model):
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
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Concrete Durabilities
        clientObject = model.clientModel.factory.create('ns0:sls_configuration')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

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
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Global Parameter to client model
        model.clientModel.service.set_sls_configuration(clientObject)