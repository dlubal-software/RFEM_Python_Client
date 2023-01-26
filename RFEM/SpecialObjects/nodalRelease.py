from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import NodeType, NodalReleaseReleaseLocation
from RFEM.enums import NodeCoordinateSystemType
from RFEM.enums import NodeReferenceType, ObjectTypes


class NodalRelease():
    def __init__(self,
                 no: int = 1,
                 nodal_release_type: int = 0,
                 release_location = NodalReleaseReleaseLocation.RELEASE_LOCATION_ORIGIN,
                 released: str = '',
                 deactivate_release: bool = False,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Node Tag
            coordinate_X (float): X-Coordinate
            coordinate_Y (float): Y-Coordinate
            coordinate_Z (float): Z-Coordinate
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

        # Nodal Release Type
        clientObject.nodal_release_type = nodal_release_type

        # Released Members
        clientObject.released_members = ConvertToDlString(released)

        # Released Surfaces
        clientObject.released_surfaces = ConvertToDlString(released)

        # Released Solids
        clientObject.released_solids = ConvertToDlString(released)

        # Nodal Release
        clientObject.release_location = release_location.name

        # Generated Released Objects
        clientObject.generated_released_objects = ConvertToDlString(released)

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
        model.clientModel.service.set_node(clientObject)


