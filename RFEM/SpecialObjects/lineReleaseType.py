from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import TranslationalReleaseNonlinearity, RotationalReleaseNonlinearity, LineReleaseLocalAxisSystem

class LineReleaseType():

    def __init__(self,
                 no: int = 1,
                 spring_constant: list = ['INF', 'INF', 'INF', 'INF'],
                 nonlinearity: list = [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE, TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE, \
                                       TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE, RotationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 local_axis_system = LineReleaseLocalAxisSystem.LOCAL_AXIS_SYSTEM_TYPE_ORIGINAL_LINE,
                 system_para: list = [0],
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Line Release Type

        Args:

        '''

        # Client model | Line Release Type
        clientObject = model.clientModel.factory.create('ns0:line_release_type')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Line Release Type No.
        clientObject.no = no

        # Line Release Type Condition
        clientObject.translational_release_u_x = spring_constant[0]
        clientObject.translational_release_u_y = spring_constant[1]
        clientObject.translational_release_u_z = spring_constant[2]
        clientObject.rotational_release_phi_x = spring_constant[3]

        # Line Release Nonlinearity Type
        clientObject.translational_release_u_x_nonlinearity = nonlinearity[0].name
        clientObject.translational_release_u_y_nonlinearity = nonlinearity[1].name
        clientObject.translational_release_u_z_nonlinearity = nonlinearity[2].name
        clientObject.rotational_release_phi_x_nonlinearity = nonlinearity[3].name

        # Line Release Local Axis System
        clientObject.local_axis_system_object_type = local_axis_system.name
        clientObject.rotation_angle = system_para[0]

        if local_axis_system == LineReleaseLocalAxisSystem.LOCAL_AXIS_SYSTEM_TYPE_Z_AXIS_PERPENDICULAR_TO_SURFACE:
            clientObject.local_axis_system_reference_object = system_para[1]

        elif local_axis_system == LineReleaseLocalAxisSystem.E_LOCAL_AXIS_SYSTEM_TYPE_HELP_NODE:
            clientObject.local_axis_system_reference_object = system_para[1]
            clientObject.local_axis_system_object_in_plane = system_para[2].name

        # Line Release Type User defined name
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
        model.clientModel.service.set_line_release_type(clientObject)
