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
                 name: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Nodal Release Tag
            nodes (str): Assigned Nodes
            nodal_release_type (int): Nodale Release Type Number
            release_location (enums): Nodal Release Release Location Enumeration
            released_members (str): Assigned Released Members
            released_surfaces (str): Assigned Released Surfaces
            released_solids (str): Assigned Released Solids
            deactivate_release (bool): Activate/Deactivate Nodal Release
            name (str, optional): User Defined Nodal Release Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Nodal Release
        clientObject = model.clientModel.factory.create('ns0:nodal_release')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Nodal Release No.
        clientObject.no = no

        # Assigned Nodes
        clientObject.nodes = ConvertToDlString(nodes)

        # Nodal Release Type
        clientObject.nodal_release_type = nodal_release_type

        # Released Members
        clientObject.released_members = ConvertToDlString(released_members)

        # Released Surfaces
        clientObject.released_surfaces = ConvertToDlString(released_surfaces)

        # Released Solids
        clientObject.released_solids = ConvertToDlString(released_solids)

        # Nodal Release Location
        clientObject.release_location = release_location.name

        # Deactivate Release
        clientObject.deactivated = deactivate_release

        # Nodal Release User defined name
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

        # Add Nodal Release to client model
        model.clientModel.service.set_nodal_release(clientObject)
