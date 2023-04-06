from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import NodalReleaseReleaseLocation


class NodalRelease():
    def __init__(self,
                 no: int = 1,
                 nodes: str = '',
                 nodal_release_type: int = 1,
                 release_location = NodalReleaseReleaseLocation.RELEASE_LOCATION_ORIGIN,
                 released_members: str = '1',
                 released_surfaces: str ='',
                 released_solids: str = '',
                 deactivate_release: bool = False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Nodal Release Tag
            nodes (str): Nodes
            nodal_release_type (int): Nodale Release Type
            release_location (enums): Nodal Release Release Location
            released_members (str): Released Members
            released_surfaces (str): Released Surfaces
            released_solids (str): Released Solids
            deactivate_release (bool): Deactivate Release
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:nodal_release')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Node No.
        clientObject.no = no

        # Assigned Node
        clientObject.nodes = ConvertToDlString(nodes)

        # Nodal Release Type
        clientObject.nodal_release_type = nodal_release_type

        # Released Members
        clientObject.released_members = ConvertToDlString(released_members)

        # Released Surfaces
        clientObject.released_surfaces = ConvertToDlString(released_surfaces)

        # Released Solids
        clientObject.released_solids = ConvertToDlString(released_solids)

        # Nodal Release
        clientObject.release_location = release_location.name

        # Deactivate Release
        clientObject.deactivated = deactivate_release

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Node to client model
        model.clientModel.service.set_nodal_release(clientObject)
