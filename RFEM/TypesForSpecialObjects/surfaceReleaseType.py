from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.dataTypes import inf
from RFEM.enums import SurfaceTranslationalReleaseNonlinearity, SurfaceReleaseTypeLocalAxisSystemType

class SurfaceReleaseType():

    def __init__(self,
                 no: int = 1,
                 spring_constant: list = [inf, inf, inf],
                 translational_release_ux_nonlinearity = SurfaceTranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE,
                 translational_release_uy_nonlinearity = SurfaceTranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE,
                 translational_release_uz_nonlinearity = SurfaceTranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE,
                 local_axis_system_type = SurfaceReleaseTypeLocalAxisSystemType.LOCAL_AXIS_SYSTEM_TYPE_REVERSED_TO_ORIGINAL_SURFACE,
                 surface_releases: str = None,
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Surface Release Type

        Args:
            no (int): Surface Release Type Tag
            spring_constant (list): Spring Constant List
                spring_constant = [translational_release_u_x, translational_release_u_y, translational_release_u_z]
            translational_release_ux_nonlinearity (enum): Surface Translation Release along X Direction Nonliniearity Enumeration
            translational_release_uy_nonlinearity (enum): Surface Translation Release along Y Direction Nonliniearity Enumeration
            translational_release_uz_nonlinearity (enum): Surface Translation Release along Z Direction Nonliniearity Enumeration
            local_axis_system_type (enum): Surface Release Local Axis System Enumeration
            surface_releases (str, optional): Assign Surface Release
            name (str, optional): User Defined Surface Release Type Name
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Surface Release Type
        clientObject = model.clientModel.factory.create('ns0:surface_release_type')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Release Type No.
        clientObject.no = no

        # Surface Release Type Condition
        clientObject.translational_release_u_x = spring_constant[0]
        clientObject.translational_release_u_y = spring_constant[1]
        clientObject.translational_release_u_z = spring_constant[2]

        # Surface Release Nonlinearity Type
        clientObject.translational_release_u_x_nonlinearity = translational_release_ux_nonlinearity.name
        clientObject.translational_release_u_y_nonlinearity = translational_release_uy_nonlinearity.name
        clientObject.translational_release_u_z_nonlinearity = translational_release_uz_nonlinearity.name

        # Surface Release Local Axis System
        clientObject.local_axis_system_type = local_axis_system_type.name

        # Assign Surface Releases
        if surface_releases:
            clientObject.surface_releases = ConvertToDlString(surface_releases)

        # Surface Release Type User defined name
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
        model.clientModel.service.set_surface_release_type(clientObject)
