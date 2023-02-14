from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertStrToListOfInt
from RFEM.enums import NodalReleaseTypeReleaseNonlinearity, NodalReleaseTypeDiagram
from RFEM.enums import NodalReleaseTypePartialActivityAlong, NodalReleaseTypePartialActivityAround, NodalReleaseTypeLocalAxisSystemObjectType
from RFEM.dataTypes import inf


class NodalReleaseType():
    def __init__(self,
                 no: int = 1,
                 coordinate_system: str = "Local",
                 translational_release_n: float = inf,
                 translational_release_vy: float = inf,
                 translational_release_vz: float = inf,
                 rotational_release_mt: float = inf,
                 rotational_release_my: float = 0.0,
                 rotational_release_mz: float = 0.0,
                 translational_release_n_nonlinearity = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 translational_release_vy_nonlinearity = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 translational_release_vz_nonlinearity = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 rotational_release_mt_nonlinearity = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 rotational_release_my_nonlinearity = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 rotational_release_mz_nonlinearity = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 local_axis_system = NodalReleaseTypeLocalAxisSystemObjectType.LOCAL_AXIS_SYSTEM_OBJECT_TYPE_MEMBER,
                 local_axis_system_reference_object: int = 1,
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Member Hinge Tag
            coordinate_system (str): Coordinate System Selection
            translational_release_n (float): Translational Spring Constant X
            translational_release_vy (float): Translational Spring Constant Y
            translational_release_vz (float): Translational Spring Constant Z
            rotational_release_mt (float): Rotational Spring Constant X
            rotational_release_my (float): Rotational Spring Constant Y
            rotational_release_mz (float): Rotational Spring Constant Z
            translational_release_n_nonlinearity (list): Nonlinearity Options Translational X
            translational_release_vy_nonlinearity (list): Nonlinearity Options Translational Y
            translational_release_vz_nonlinearity (list): Nonlinearity Options Translational Z
            rotational_release_mt_nonlinearity (list): Nonlinearity Options Rotational X
            rotational_release_my_nonlinearity (list): Nonlinearity Options Rotational Y
            rotational_release_mz_nonlinearity (list): Nonlinearity Options Rotational Z
            translational_release_diagram ,
            local_axis_system = [NodalReleaseTypeLocalAxisSystemObjectType.LOCAL_AXIS_SYSTEM_OBJECT_TYPE_MEMBER],
            local_axis_system_reference_object: int = 1,
            name: str = None,
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:nodal_release_type')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Node No.
        clientObject.no = no

        # Nodal Release Typ
        clientObject.coordinate_system = coordinate_system

         # Translational Release/Spring [N/m] N
        clientObject.axial_release_n = translational_release_n

        # Translational Release/Spring [N/m] Vy
        clientObject.axial_release_vy = translational_release_vy

        # Translational Release/Spring [N/m] Vz
        clientObject.axial_release_vz = translational_release_vz

        # Rotational Release/Spring [Nm/rad] Mt
        clientObject.moment_release_mt = rotational_release_mt

        # Rotational Release/Spring [Nm/rad] My
        clientObject.moment_release_my = rotational_release_my

        # Rotational Release/Spring [Nm/rad] Mz
        clientObject.moment_release_mz = rotational_release_mz

        # Translational Release N Nonlinearity

        # Nonlinearity Types None, Fixed if Negative N, Fixed if Positive N
        if translational_release_n_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or translational_release_n_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or translational_release_n_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name

        # Partial Activity
        elif translational_release_n_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_along_x_negative_type = translational_release_n_nonlinearity[1][0].name

            if translational_release_n_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_x_negative_slippage = translational_release_n_nonlinearity[1][1]

            elif translational_release_n_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_x_negative_displacement = translational_release_n_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_slippage = translational_release_n_nonlinearity[1][2]

            elif translational_release_n_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_x_negative_force = translational_release_n_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_slippage = translational_release_n_nonlinearity[1][2]

            elif translational_release_n_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_x_negative_force = translational_release_n_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_slippage = translational_release_n_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_x_positive_type = translational_release_n_nonlinearity[2][0].name

            if translational_release_n_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_x_positive_slippage = translational_release_n_nonlinearity[2][1]

            elif translational_release_n_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_x_positive_displacement = translational_release_n_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_slippage = translational_release_n_nonlinearity[2][2]

            elif translational_release_n_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_x_positive_force = translational_release_n_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_slippage = translational_release_n_nonlinearity[2][2]

            elif translational_release_n_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_x_positive_force = translational_release_n_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_slippage = translational_release_n_nonlinearity[2][2]

        elif translational_release_n_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name
            clientObject.diagram_along_x_symmetric = translational_release_n_nonlinearity[1][0]
            clientObject.diagram_along_x_is_sorted = True

            if translational_release_n_nonlinearity[1][0]:
                clientObject.diagram_along_y_start = translational_release_n_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = translational_release_n_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_y_start = translational_release_n_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = translational_release_n_nonlinearity[1][2].name

            clientObject.diagram_along_x_table = Model.clientModel.factory.create('ns0:nodal_release_type.diagram_along_x_table')

            for i,j in enumerate(translational_release_n_nonlinearity[1][2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_along_x_table_row')
                mlvlp.no = i+1
                mlvlp.row.displacement = translational_release_n_nonlinearity[1][2][i][0]
                mlvlp.row.force = translational_release_n_nonlinearity[1][2][i][1]
                mlvlp.row.spring = translational_release_n_nonlinearity[1][2][i][2]

                clientObject.diagram_along_x_table.nodal_release_type_diagram_along_x_table.append(mlvlp)

        elif translational_release_n_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1 \
        or translational_release_n_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_2 \
        or translational_release_n_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2:
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name
            clientObject.friction_coefficient_x = translational_release_n_nonlinearity[1][0]

        elif translational_release_n_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2:
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name
            clientObject.friction_coefficient_xy = translational_release_n_nonlinearity[1][0]
            clientObject.friction_coefficient_xz = translational_release_n_nonlinearity[1][1]

        # Translational Release Vy Nonlinearity
        if translational_release_vy_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or translational_release_vy_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or translational_release_vy_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE:
            clientObject.axial_release_vy_nonlinearity = translational_release_vy_nonlinearity[0].name

        # Partial Activity
        elif translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.axial_release_vy_nonlinearity = translational_release_vy_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_along_y_negative_type = translational_release_vy_nonlinearity[1][0].name

            if translational_release_vy_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_y_negative_slippage = translational_release_vy_nonlinearity[1][1]

            elif translational_release_vy_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_y_negative_displacement = translational_release_vy_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_slippage = translational_release_vy_nonlinearity[1][2]

            elif translational_release_vy_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_y_negative_force = translational_release_vy_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_slippage = translational_release_vy_nonlinearity[1][2]

            elif translational_release_vy_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_y_negative_force = translational_release_vy_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_slippage = translational_release_vy_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_y_positive_type = translational_release_vy_nonlinearity[2][0].name

            if translational_release_vy_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_y_positive_slippage = translational_release_vy_nonlinearity[2][1]

            elif translational_release_vy_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_y_positive_displacement = translational_release_vy_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_slippage = translational_release_vy_nonlinearity[2][2]

            elif translational_release_vy_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_y_positive_force = translational_release_vy_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_slippage = translational_release_vy_nonlinearity[2][2]

            elif translational_release_vy_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE :
                clientObject.partial_activity_along_y_positive_force = translational_release_vy_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_slippage = translational_release_vy_nonlinearity[2][2]

        elif translational_release_vy_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.axial_release_vy_nonlinearity = translational_release_vy_nonlinearity[0].name

            clientObject.diagram_along_y_symmetric = translational_release_vy_nonlinearity[1][0]
            clientObject.diagram_along_y_is_sorted = True

            if translational_release_vy_nonlinearity[1][0]:
                clientObject.diagram_along_y_start = translational_release_vy_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = translational_release_vy_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_y_start = translational_release_vy_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = translational_release_vy_nonlinearity[1][2].name

            clientObject.diagram_along_y_table = Model.clientModel.factory.create('ns0:nodal_release_type.diagram_along_y_table')

            for i,j in enumerate(translational_release_vy_nonlinearity[1][2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_along_y_table_row')
                mlvlp.no = i+1
                mlvlp.row.displacement = translational_release_vy_nonlinearity[1][2][i][0]
                mlvlp.row.force = translational_release_vy_nonlinearity[1][2][i][1]
                mlvlp.row.spring = translational_release_vy_nonlinearity[1][2][i][2]

                clientObject.diagram_along_y_table.nodal_release_type_diagram_along_y_table.append(mlvlp)

        elif translational_release_vy_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1 \
        or translational_release_vy_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_2 \
        or translational_release_vy_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2:
            clientObject.axial_release_vy_nonlinearity = translational_release_vy_nonlinearity[0].name
            clientObject.friction_coefficient_y = translational_release_vy_nonlinearity[1][0]

        elif translational_release_vy_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2:
            clientObject.axial_release_vy_nonlinearity = translational_release_vy_nonlinearity[0].name
            clientObject.friction_coefficient_yx = translational_release_vy_nonlinearity[1][0]
            clientObject.friction_coefficient_yz = translational_release_vy_nonlinearity[1][1]

        # Translational Release Vz Nonlinearity
        if translational_release_vz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or translational_release_vz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or translational_release_vz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name

        # Partial Activity
        elif translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_along_z_negative_type = translational_release_vz_nonlinearity[1][0].name

            if translational_release_vz_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_z_negative_slippage = translational_release_vz_nonlinearity[1][1]

            elif translational_release_vz_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_z_negative_displacement = translational_release_vz_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_slippage = translational_release_vz_nonlinearity[1][2]

            elif translational_release_vz_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_z_negative_force = translational_release_vz_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_slippage = translational_release_vz_nonlinearity[1][2]

            elif translational_release_vz_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_z_negative_force = translational_release_vz_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_slippage = translational_release_vz_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_z_positive_type = translational_release_vz_nonlinearity[2][0].name

            if translational_release_vz_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_z_positive_slippage = translational_release_vz_nonlinearity[2][1]

            elif translational_release_vz_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_z_positive_displacement = translational_release_vz_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_slippage = translational_release_vz_nonlinearity[2][2]

            elif translational_release_vz_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_z_positive_force = translational_release_vz_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_slippage = translational_release_vz_nonlinearity[2][2]

            elif translational_release_vz_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_z_positive_force = translational_release_vz_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_slippage = translational_release_vz_nonlinearity[2][2]

        elif translational_release_vz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name

            clientObject.diagram_along_z_symmetric = translational_release_vz_nonlinearity[1][0]
            clientObject.diagram_along_z_is_sorted = True

            if translational_release_vz_nonlinearity[1][0]:
                clientObject.diagram_along_y_start = translational_release_vz_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = translational_release_vz_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_y_start = translational_release_vz_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = translational_release_vz_nonlinearity[1][2].name

            clientObject.diagram_along_z_table = Model.clientModel.factory.create('ns0:member_hinge.diagram_along_z_table')

            for i,j in enumerate(translational_release_vz_nonlinearity[1][2]):
                mlvlp = Model.clientModel.factory.create('ns0:member_hinge_diagram_along_z_table_row')
                mlvlp.no = i+1
                mlvlp.row.displacement = translational_release_vz_nonlinearity[1][2][i][0]
                mlvlp.row.force = translational_release_vz_nonlinearity[1][2][i][1]
                mlvlp.row.spring = translational_release_vz_nonlinearity[1][2][i][2]

                clientObject.diagram_along_z_table.member_hinge_diagram_along_z_table.append(mlvlp)

        elif translational_release_vz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1 \
        or translational_release_vz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_2 \
        or translational_release_vz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2:
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name
            clientObject.friction_coefficient_z = translational_release_vz_nonlinearity[1][0]

        elif translational_release_vz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2:
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name
            clientObject.friction_coefficient_zx = translational_release_vz_nonlinearity[1][0]
            clientObject.friction_coefficient_zy = translational_release_vz_nonlinearity[1][1]

        # Rotational Release Mt Nonlinearity
        if rotational_release_mt_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or rotational_release_mt_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or rotational_release_mt_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.moment_release_mt_nonlinearity = rotational_release_mt_nonlinearity[0].name

        # Partial Activity
        elif rotational_release_mt_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.moment_release_mt_nonlinearity = rotational_release_mt_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_around_x_negative_type = rotational_release_mt_nonlinearity[1][0].name

            if rotational_release_mt_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_mt_nonlinearity[1][1]

            elif rotational_release_mt_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_x_negative_displacement = rotational_release_mt_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_mt_nonlinearity[1][2]

            elif rotational_release_mt_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_x_negative_moment = rotational_release_mt_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_mt_nonlinearity[1][2]

            elif rotational_release_mt_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_x_negative_moment = rotational_release_mt_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_mt_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_x_positive_type = rotational_release_mt_nonlinearity[2][0].name

            if rotational_release_mt_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_mt_nonlinearity[2][1]

            elif rotational_release_mt_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_x_positive_displacement = rotational_release_mt_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_mt_nonlinearity[2][2]

            elif rotational_release_mt_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_x_positive_moment = rotational_release_mt_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_mt_nonlinearity[2][2]

            elif rotational_release_mt_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_x_positive_moment = rotational_release_mt_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_mt_nonlinearity[2][2]

        elif rotational_release_mt_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.moment_release_mt_nonlinearity = rotational_release_mt_nonlinearity[0].name

            clientObject.diagram_around_x_symmetric = rotational_release_mt_nonlinearity[1][0]
            clientObject.diagram_around_x_is_sorted = True

            if rotational_release_mt_nonlinearity[1][0]:
                clientObject.diagram_along_y_start = rotational_release_mt_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = rotational_release_mt_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_y_start = rotational_release_mt_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = rotational_release_mt_nonlinearity[1][2].name


            clientObject.diagram_around_x_table = Model.clientModel.factory.create('ns0:nodal_release_type.diagram_around_x_table')

            for i,j in enumerate(rotational_release_mt_nonlinearity[1][2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_around_x_table_row')
                mlvlp.no = i+1
                mlvlp.row.rotation = rotational_release_mt_nonlinearity[1][2][i][0]
                mlvlp.row.moment = rotational_release_mt_nonlinearity[1][2][i][1]
                mlvlp.row.spring = rotational_release_mt_nonlinearity[1][2][i][2]

                clientObject.diagram_around_x_table.nodal_release_type_diagram_around_x_table.append(mlvlp)

        # Rotational Release My Nonlinearity
        if rotational_release_my_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE\
        or rotational_release_my_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or rotational_release_my_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.moment_release_my_nonlinearity = rotational_release_my_nonlinearity[0].name

        # Partial Activity
        elif rotational_release_my_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.moment_release_my_nonlinearity = rotational_release_my_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_around_y_negative_type = rotational_release_my_nonlinearity[1][0].name

            if rotational_release_my_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_y_negative_slippage = rotational_release_my_nonlinearity[1][1]

            elif rotational_release_my_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_x_negative_displacement = rotational_release_my_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_my_nonlinearity[1][2]

            elif rotational_release_my_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_y_negative_force = rotational_release_my_nonlinearity[1][1]
                clientObject.partial_activity_around_y_negative_slippage = rotational_release_my_nonlinearity[1][2]

            elif rotational_release_my_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_y_negative_force = rotational_release_my_nonlinearity[1][1]
                clientObject.partial_activity_around_y_negative_slippage = rotational_release_my_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_y_positive_type = rotational_release_my_nonlinearity[2][0].name

            if rotational_release_my_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_y_positive_slippage = rotational_release_my_nonlinearity[2][1]

            elif rotational_release_my_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_x_positive_displacement = rotational_release_my_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_my_nonlinearity[2][2]

            elif rotational_release_my_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_y_positive_force = rotational_release_my_nonlinearity[2][1]
                clientObject.partial_activity_around_y_positive_slippage = rotational_release_my_nonlinearity[2][2]

            elif rotational_release_my_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_y_positive_force = rotational_release_my_nonlinearity[2][1]
                clientObject.partial_activity_around_y_positive_slippage = rotational_release_my_nonlinearity[2][2]

        elif rotational_release_my_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.moment_release_my_nonlinearity = rotational_release_my_nonlinearity[0].name

            clientObject.diagram_around_y_symmetric = rotational_release_my_nonlinearity[1][0]
            clientObject.diagram_around_y_is_sorted = True

            if rotational_release_my_nonlinearity[1][0]:
                clientObject.diagram_along_y_start = rotational_release_my_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = rotational_release_my_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_y_start = rotational_release_my_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = rotational_release_my_nonlinearity[1][2].name


            clientObject.diagram_around_y_table = Model.clientModel.factory.create('ns0:nodal_release_type.diagram_around_y_table')

            for i,j in enumerate(rotational_release_my_nonlinearity[1][2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_around_y_table_row')
                mlvlp.no = i+1
                mlvlp.row.rotation = rotational_release_my_nonlinearity[1][2][i][0]
                mlvlp.row.moment = rotational_release_my_nonlinearity[1][2][i][1]
                mlvlp.row.spring = rotational_release_my_nonlinearity[1][2][i][2]

                clientObject.diagram_around_y_table.nodal_release_type_diagram_around_y_table.append(mlvlp)

        # Rotational Release Mz Nonlinearity
        if rotational_release_mz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or rotational_release_mz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or rotational_release_mz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.moment_release_mz_nonlinearity = rotational_release_mz_nonlinearity[0].name

        # Partial Activity
        elif rotational_release_mz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.moment_release_mz_nonlinearity = rotational_release_mz_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_around_z_negative_type = rotational_release_mz_nonlinearity[1][0].name

            if rotational_release_mz_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_z_negative_slippage = rotational_release_mz_nonlinearity[1][1]

            elif rotational_release_mz_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_z_negative_displacement = rotational_release_mz_nonlinearity[1][1]
                clientObject.partial_activity_around_z_negative_slippage = rotational_release_mz_nonlinearity[1][2]

            elif rotational_release_mz_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_z_negative_moment = rotational_release_mz_nonlinearity[1][1]
                clientObject.partial_activity_around_z_negative_slippage = rotational_release_mz_nonlinearity[1][2]

            elif rotational_release_mz_nonlinearity[1][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_z_negative_moment = rotational_release_mz_nonlinearity[1][1]
                clientObject.partial_activity_around_z_negative_slippage = rotational_release_mz_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_z_positive_type = rotational_release_mz_nonlinearity[2][0].name

            if rotational_release_mz_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_z_positive_slippage = rotational_release_mz_nonlinearity[2][1]

            elif rotational_release_mz_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_z_positive_displacement = rotational_release_mz_nonlinearity[2][1]
                clientObject.partial_activity_around_z_positive_slippage = rotational_release_mz_nonlinearity[2][2]

            elif rotational_release_mz_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_z_positive_force = rotational_release_mz_nonlinearity[2][1]
                clientObject.partial_activity_around_z_positive_slippage = rotational_release_mz_nonlinearity[2][2]

            elif rotational_release_mz_nonlinearity[2][0].name == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_z_positive_force = rotational_release_mz_nonlinearity[2][1]
                clientObject.partial_activity_around_z_positive_slippage = rotational_release_mz_nonlinearity[2][2]

        elif rotational_release_mz_nonlinearity[0].name == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.moment_release_mz_nonlinearity = rotational_release_mz_nonlinearity[0].name

            clientObject.diagram_around_z_symmetric = rotational_release_my_nonlinearity[1][0]
            clientObject.diagram_around_z_is_sorted = True

            if rotational_release_mz_nonlinearity[1][0]:
                clientObject.diagram_along_y_start = rotational_release_mz_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = rotational_release_mz_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_y_start = rotational_release_mz_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = rotational_release_mz_nonlinearity[1][2].name


            clientObject.diagram_around_z_table = Model.clientModel.factory.create('ns0:nodal_release_type.diagram_around_z_table')

            for i,j in enumerate(rotational_release_mz_nonlinearity[1][2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_around_z_table_row')
                mlvlp.no = i+1
                mlvlp.row.rotation = rotational_release_mz_nonlinearity[1][2][i][0]
                mlvlp.row.moment = rotational_release_mz_nonlinearity[1][2][i][1]
                mlvlp.row.spring = rotational_release_mz_nonlinearity[1][2][i][2]

                clientObject.diagram_around_z_table.nodal_release_type_diagram_around_z_table.append(mlvlp)

        # Nodal Release Local Axis System Object Type
        clientObject.local_axis_system_object_type = local_axis_system.name

        # Nodal Release Local Axis System Reference Object
        clientObject.local_axis_system_reference_object = local_axis_system_reference_object

        # Line Release Type User defined name
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

        # Add Node to client model
        model.clientModel.service.set_nodal_release_type(clientObject)
