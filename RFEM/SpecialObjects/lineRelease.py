from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import LineReleaseReleaseLocation

class LineRelease():

    def __init__(self,
                 no: int = 1,
                 lines: str = '',
                 line_release_type: int = 1,
                 release_location = LineReleaseReleaseLocation.RELEASE_LOCATION_RELEASED,
                 released_members: str = None,
                 released_surfaces: str = None,
                 released_solids: str = None,
                 use_nodes_as_definition_nodes: str = None,
                 deactivated: bool = False,
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Line Release Tag
            lines (str): Assigned Lines
            line_release_type (int): Line Release Type Number
            release_location (enum): Line Release Release Location
            released_members (str): Assigned Release Members
            released_surfaces (str): Assigned Release Surfaces
            released_solids (str): Assigned Release Solids
            use_nodes_as_definition_nodes (str): Assigned Definition Nodes
            deactivated (bool): Activate/Deactivate Line Release
            name (str): User Defined Name
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Line Release
        clientObject = model.clientModel.factory.create('ns0:line_release')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Line Release No.
        clientObject.no = no

        # Assign Line
        clientObject.lines = ConvertToDlString(lines)

        # Assign Line Release Type
        clientObject.line_release_type = line_release_type

        # Line Release Location
        clientObject.release_location = release_location.name

        # Released Members
        clientObject.released_members = ConvertToDlString(released_members)

        # Released Surfaces
        clientObject.released_surfaces = ConvertToDlString(released_surfaces)

        # Released Solid
        clientObject.released_solids = ConvertToDlString(released_solids)

        # Assign Nodes as Definition Nodes
        clientObject.use_nodes_as_definition_nodes = ConvertToDlString(use_nodes_as_definition_nodes)

        # Activate/Deactivate Line Release
        clientObject.deactivated = deactivated

        # Line Release User defined name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        #Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Line Release Type to Client Model
        model.clientModel.service.set_line_release(clientObject)
