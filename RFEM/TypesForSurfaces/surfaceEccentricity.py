from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import SurfaceEccentricityAlignment
from enum import Enum

class TransverseOffsetObject(Enum):
    MEMBER, SURFACE = range(2)

class SurfaceEccentricity():
    def __init__(self,
                 no: int = 1,
                 offset: float = 0.1,
                 assigned_to_surfaces: str = '1',
                 thickness_alignment = SurfaceEccentricityAlignment.ALIGN_MIDDLE,
                 transverse_offset_object = TransverseOffsetObject.SURFACE,
                 transverse_offset_object_no: int = 1,
                 transverse_offset_alignment = SurfaceEccentricityAlignment.ALIGN_MIDDLE,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Surfase Eccentricity

        Args:
            no (int): Surface Eccentricity Tag
            offset (float): Offset value
            assigned_to_surfaces (str): Eccentricity Assignmet to Surfaces
            thickness_alignment (enum): Surface Eccentricity Alignment Enumeration
            transverse_offset_object (enum): Transverse Offset Object Enumeration (member, surface or None)
            transverse_offset_object_no (int): Transverse offset reference number
            transverse_offset_alignment (enum): Surface Eccentricity Alignment Enumeration
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Eccentricity
        clientObject = model.clientModel.factory.create('ns0:surface_eccentricity')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Eccentricity No.
        clientObject.no = no

        # Offset
        clientObject.offset = offset

        # Assigned to Surfaces
        clientObject.assigned_to_surfaces = ConvertToDlString(assigned_to_surfaces)

        # Thickness Assigmnet
        clientObject.thickness_alignment = thickness_alignment.name

        # Transverse Offset Object,  Number, and Transverse Offset Alignment
        if transverse_offset_object == TransverseOffsetObject.MEMBER:
            clientObject.transverse_offset_reference_type = "TRANSVERSE_OFFSET_TYPE_FROM_MEMBER_SECTION"
            clientObject.transverse_offset_reference_member = transverse_offset_object_no
            clientObject.transverse_offset_alignment = transverse_offset_alignment.name
        elif transverse_offset_object == TransverseOffsetObject.SURFACE:
            clientObject.transverse_offset_reference_type = "TRANSVERSE_OFFSET_TYPE_FROM_SURFACE_THICKNESS"
            clientObject.transverse_offset_reference_surface = transverse_offset_object_no
            clientObject.transverse_offset_alignment = transverse_offset_alignment.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface Eccentricity to client model
        model.clientModel.service.set_surface_eccentricity(clientObject)
