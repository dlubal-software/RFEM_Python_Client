from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import SurfaceReleaseReleaseLocation

class SurfaceRelease():

    def __init__(self,
                 no: int = 1,
                 surfaces: str = '',
                 surface_release_type: int = 1,
                 release_location = SurfaceReleaseReleaseLocation.RELEASE_LOCATION_ORIGIN,
                 released_members: str = None,
                 released_surfaces: str = None,
                 released_solids: str = None,
                 use_nodes_as_definition_nodes: str = None,
                 use_lines_as_definition_lines: str = None,
                 deactivated: bool = False,
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Surface Release Tag
            surfaces (str): Assigned Surfaces
            surface_release_type (int): Surface Release Type Number
            release_location (enum): Surface Release Release Location Enumeration
            released_members (str): Assigned Released Members
            released_surfaces (str): Assigned Released Surfaces
            released_solids (str): Assigned Released Solids
            use_nodes_as_definition_nodes (str): Assigned Definition Nodes
            use_lines_as_definition_lines (str): Assigned Definition Lines
            deactivated (bool): Activate/Deactivate Surface Release
            name (str, optional): User Defined Surface Release Name
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Surface Release
        clientObject = model.clientModel.factory.create('ns0:surface_release')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Release No.
        clientObject.no = no

        # Assign Surface
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Assign Surface Release Type
        clientObject.surface_release_type = surface_release_type

        # Surface Release Location
        clientObject.release_location = release_location.name

        # Released Members
        clientObject.released_members = ConvertToDlString(released_members)

        # Released Surfaces
        clientObject.released_surfaces = ConvertToDlString(released_surfaces)

        # Released Solid
        clientObject.released_solids = ConvertToDlString(released_solids)

        # Assign Nodes as Definition Nodes
        clientObject.use_nodes_as_definition_nodes = ConvertToDlString(use_nodes_as_definition_nodes)

        # Assign Nodes as Definition Nodes
        clientObject.use_lines_as_definition_lines = ConvertToDlString(use_lines_as_definition_lines)

        # Activate/Deactivate Surface Release
        clientObject.deactivated = deactivated

        # Surface Release User defined name
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

        # Add Surface Release Type to Client Model
        model.clientModel.service.set_surface_release(clientObject)
