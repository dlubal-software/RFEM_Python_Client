from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import NodalReleaseTypePartialActivityAlong, NodalReleaseTypePartialActivityAround, NodalReleaseTypeLocalAxisSystemObjectType, NodalReleaseTypeReleaseNonlinearity
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
                 translational_release_n_nonlinearity: list = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 translational_release_vy_nonlinearity: list = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 translational_release_vz_nonlinearity: list = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 rotational_release_mt_nonlinearity: list = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 rotational_release_my_nonlinearity: list = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 rotational_release_mz_nonlinearity: list = [NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 local_axis_system = NodalReleaseTypeLocalAxisSystemObjectType.LOCAL_AXIS_SYSTEM_OBJECT_TYPE_MEMBER,
                 local_axis_system_reference_object: int = 1,
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Nodal Release Type Tag
            coordinate_system (str/int): Coordinate System Selection
            translational_release_n (float): Spring Constant for Translation Release along X Direction
            translational_release_vy (float): Spring Constant for Translation Release along Y Direction
            translational_release_vz (float): Spring Constant for Translation Release along Z Direction
            rotational_release_mt (float): Spring Constant for Rotational Release around X Direction
            rotational_release_my (float): Spring Constant for Rotational Release around Y Direction
            rotational_release_mz (float): Spring Constant for Rotational Release around Z Direction
            translational_release_n_nonlinearity (list/list of lists): Nonlinearity Parameter for Translation Release along X Direction
            translational_release_vy_nonlinearity (list/list of lists): Nonlinearity Parameter for Translation Release along Y Direction
            translational_release_vz_nonlinearity (list/list of lists): Nonlinearity Parameter for Translation Release along Z Direction
                for translational_release_n/vy/vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
                    translational_release_n/vy/vz_nonlinearity = [nonlinearity type Partial_Activity, negative zone, positive zone]
                    for negative/positive zone[0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                        negative/positive zone = [negative/positive zone type, slippage]
                    for negative/positive zone[0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                        negative/positive zone = [negative/positive zone type, displacement, slippage]  (Note: Displacement must be greater than slippage)
                    for negative/positive zone[0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE/PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                        negative/positive zone = [negative/positive zone type, force, slippage]
                for translational_release_n/vy/vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
                    translational_release_n/vy/vz_nonlinearity = [nonlinearity type Diagram, [symmetric(bool), NodalReleaseTypeDiagram Enumeration(start), NodalReleaseTypeDiagram Enumeration(end)], [[displacement, force],...]]
                for translational_release_n/vy/vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1/NONLINEARITY_TYPE_FRICTION_DIRECTION_2/NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2:
                    translational_release_n/vy/vz_nonlinearity = [nonlinearity type Diagram, [friction coefficient(float)]]
                for translational_release_n/vy/vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2:
                    translational_release_n/vy/vz_nonlinearity = [nonlinearity type Diagram, [friction coefficient 1(float), friction coefficient 2(float)]]
            rotational_release_mt_nonlinearity (list/list of lists): Nonlinearity Parameter for Rotational Release around X Direction
            rotational_release_my_nonlinearity (list/list of lists): Nonlinearity Parameter for Rotational Release around Y Direction
            rotational_release_mz_nonlinearity (list/list of lists): Nonlinearity Parameter for Rotational Release around Z Direction
                for rotational_release_mt/my/mz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
                    rotational_release_mt/my/mz_nonlinearity = [nonlinearity type Partial_Activity, negative zone, positive zone]
                    for negative/positive zone[0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                        negative/positive zone = [negative/positive zone type, slippage]
                    for negative/positive zone[0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FIXED:
                        negative/positive zone = [negative/positive zone type, rotation, slippage]
                    for negative/positive zone[0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT/PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                        negative/positive zone = [negative/positive zone type, moment, slippage]
                for rotational_release_mt/my/mz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
                    rotational_release_mt/my/mz_nonlinearity = [nonlinearity type Diagram, [symmetric(bool), NodalReleaseTypeDiagram Enumeration(start), NodalReleaseTypeDiagram Enumeration(end)], [[rotation, moment],...]]
            local_axis_system (enum): Nodal Release Local Axis System Enumeration
            local_axis_system_reference_object (int): Nodal Release Local Axis System Reference Object Number
            name (str, optional): User Defined Nodal Release Type Name
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Nodal Release Type
        clientObject = model.clientModel.factory.create('ns0:nodal_release_type')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Nodal Release Type No.
        clientObject.no = no

        # Nodal Release Type
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
        if translational_release_n_nonlinearity[0]== NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or translational_release_n_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or translational_release_n_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name

        # Partial Activity
        elif translational_release_n_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_along_x_negative_type = translational_release_n_nonlinearity[1][0].name

            if translational_release_n_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_x_negative_slippage = translational_release_n_nonlinearity[1][1]

            elif translational_release_n_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_x_negative_displacement = translational_release_n_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_slippage = translational_release_n_nonlinearity[1][2]

            elif translational_release_n_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_x_negative_force = translational_release_n_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_slippage = translational_release_n_nonlinearity[1][2]

            elif translational_release_n_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_x_negative_force = translational_release_n_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_slippage = translational_release_n_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_x_positive_type = translational_release_n_nonlinearity[2][0].name

            if translational_release_n_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_x_positive_slippage = translational_release_n_nonlinearity[2][1]

            elif translational_release_n_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_x_positive_displacement = translational_release_n_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_slippage = translational_release_n_nonlinearity[2][2]

            elif translational_release_n_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_x_positive_force = translational_release_n_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_slippage = translational_release_n_nonlinearity[2][2]

            elif translational_release_n_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_x_positive_force = translational_release_n_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_slippage = translational_release_n_nonlinearity[2][2]

        elif translational_release_n_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name
            clientObject.diagram_along_x_symmetric = translational_release_n_nonlinearity[1][0]
            clientObject.diagram_along_x_is_sorted = True

            if translational_release_n_nonlinearity[1][0]:
                clientObject.diagram_along_x_start = translational_release_n_nonlinearity[1][1].name
                clientObject.diagram_along_x_end = translational_release_n_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_x_start = translational_release_n_nonlinearity[1][1].name
                clientObject.diagram_along_x_end = translational_release_n_nonlinearity[1][2].name

            clientObject.diagram_along_x_table = Model.clientModel.factory.create('ns0:nodal_release_type.diagram_along_x_table')

            for i,j in enumerate(translational_release_n_nonlinearity[2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_along_x_table_row')
                mlvlp.no = i+1
                mlvlp.row.displacement = translational_release_n_nonlinearity[2][i][0]
                mlvlp.row.force = translational_release_n_nonlinearity[2][i][1]

                clientObject.diagram_along_x_table.nodal_release_type_diagram_along_x_table.append(mlvlp)

        elif translational_release_n_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1 \
        or translational_release_n_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_2 \
        or translational_release_n_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2:
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name
            clientObject.friction_coefficient_x = translational_release_n_nonlinearity[1][0]

        elif translational_release_n_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2:
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name
            clientObject.friction_coefficient_xy = translational_release_n_nonlinearity[1][0]
            clientObject.friction_coefficient_xz = translational_release_n_nonlinearity[1][1]

        else:
            raise TypeError('Incorrect Nodal Release Nonlinearity Type')

        # Translational Release Vy Nonlinearity
        if translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE:
            clientObject.axial_release_vy_nonlinearity = translational_release_vy_nonlinearity[0].name

        # Partial Activity
        elif translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.axial_release_vy_nonlinearity = translational_release_vy_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_along_y_negative_type = translational_release_vy_nonlinearity[1][0].name

            if translational_release_vy_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_y_negative_slippage = translational_release_vy_nonlinearity[1][1]

            elif translational_release_vy_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_y_negative_displacement = translational_release_vy_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_slippage = translational_release_vy_nonlinearity[1][2]

            elif translational_release_vy_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_y_negative_force = translational_release_vy_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_slippage = translational_release_vy_nonlinearity[1][2]

            elif translational_release_vy_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_y_negative_force = translational_release_vy_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_slippage = translational_release_vy_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_y_positive_type = translational_release_vy_nonlinearity[2][0].name

            if translational_release_vy_nonlinearity[2][0]== NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_y_positive_slippage = translational_release_vy_nonlinearity[2][1]

            elif translational_release_vy_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_y_positive_displacement = translational_release_vy_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_slippage = translational_release_vy_nonlinearity[2][2]

            elif translational_release_vy_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_y_positive_force = translational_release_vy_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_slippage = translational_release_vy_nonlinearity[2][2]

            elif translational_release_vy_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE :
                clientObject.partial_activity_along_y_positive_force = translational_release_vy_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_slippage = translational_release_vy_nonlinearity[2][2]

        elif translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
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

            for i,j in enumerate(translational_release_vy_nonlinearity[2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_along_y_table_row')
                mlvlp.no = i+1
                mlvlp.row = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_along_y_table')
                clearAttributes(mlvlp.row)
                mlvlp.row.displacement = translational_release_vy_nonlinearity[2][i][0]
                mlvlp.row.force = translational_release_vy_nonlinearity[2][i][1]

                clientObject.diagram_along_y_table.nodal_release_type_diagram_along_y_table.append(mlvlp)

        elif translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1 \
        or translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_2 \
        or translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2:
            clientObject.axial_release_vy_nonlinearity = translational_release_vy_nonlinearity[0].name
            clientObject.friction_coefficient_y = translational_release_vy_nonlinearity[1][0]

        elif translational_release_vy_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2:
            clientObject.axial_release_vy_nonlinearity = translational_release_vy_nonlinearity[0].name
            clientObject.friction_coefficient_yx = translational_release_vy_nonlinearity[1][0]
            clientObject.friction_coefficient_yz = translational_release_vy_nonlinearity[1][1]

        else:
            raise TypeError('Incorrect Nodal Release Nonlinearity Type')

        # Translational Release Vz Nonlinearity
        if translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name

        # Partial Activity
        elif translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_along_z_negative_type = translational_release_vz_nonlinearity[1][0].name

            if translational_release_vz_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_z_negative_slippage = translational_release_vz_nonlinearity[1][1]

            elif translational_release_vz_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_z_negative_displacement = translational_release_vz_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_slippage = translational_release_vz_nonlinearity[1][2]

            elif translational_release_vz_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_z_negative_force = translational_release_vz_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_slippage = translational_release_vz_nonlinearity[1][2]

            elif translational_release_vz_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_z_negative_force = translational_release_vz_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_slippage = translational_release_vz_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_z_positive_type = translational_release_vz_nonlinearity[2][0].name

            if translational_release_vz_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_z_positive_slippage = translational_release_vz_nonlinearity[2][1]

            elif translational_release_vz_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_z_positive_displacement = translational_release_vz_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_slippage = translational_release_vz_nonlinearity[2][2]

            elif translational_release_vz_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE:
                clientObject.partial_activity_along_z_positive_force = translational_release_vz_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_slippage = translational_release_vz_nonlinearity[2][2]

            elif translational_release_vz_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_z_positive_force = translational_release_vz_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_slippage = translational_release_vz_nonlinearity[2][2]

        elif translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name

            clientObject.diagram_along_z_symmetric = translational_release_vz_nonlinearity[1][0]
            clientObject.diagram_along_z_is_sorted = True

            if translational_release_vz_nonlinearity[1][0]:
                clientObject.diagram_along_z_start = translational_release_vz_nonlinearity[1][1].name
                clientObject.diagram_along_z_end = translational_release_vz_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_z_start = translational_release_vz_nonlinearity[1][1].name
                clientObject.diagram_along_z_end = translational_release_vz_nonlinearity[1][2].name

            clientObject.diagram_along_z_table = Model.clientModel.factory.create('ns0:member_hinge.diagram_along_z_table')

            for i,j in enumerate(translational_release_vz_nonlinearity[2]):
                mlvlp = Model.clientModel.factory.create('ns0:member_hinge_diagram_along_z_table_row')
                mlvlp.no = i+1
                mlvlp.row.displacement = translational_release_vz_nonlinearity[2][i][0]
                mlvlp.row.force = translational_release_vz_nonlinearity[2][i][1]

                clientObject.diagram_along_z_table.member_hinge_diagram_along_z_table.append(mlvlp)

        elif translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1 \
        or translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_2 \
        or translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2:
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name
            clientObject.friction_coefficient_z = translational_release_vz_nonlinearity[1][0]

        elif translational_release_vz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2:
            clientObject.axial_release_vz_nonlinearity = translational_release_vz_nonlinearity[0].name
            clientObject.friction_coefficient_zx = translational_release_vz_nonlinearity[1][0]
            clientObject.friction_coefficient_zy = translational_release_vz_nonlinearity[1][1]

        else:
            raise TypeError('Incorrect Nodal Release Nonlinearity Type')

        # Rotational Release Mt Nonlinearity
        if rotational_release_mt_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or rotational_release_mt_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or rotational_release_mt_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.moment_release_mt_nonlinearity = rotational_release_mt_nonlinearity[0].name

        # Partial Activity
        elif rotational_release_mt_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.moment_release_mt_nonlinearity = rotational_release_mt_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_around_x_negative_type = rotational_release_mt_nonlinearity[1][0].name

            if rotational_release_mt_nonlinearity[1][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_mt_nonlinearity[1][1]

            elif rotational_release_mt_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_x_negative_displacement = rotational_release_mt_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_mt_nonlinearity[1][2]

            elif rotational_release_mt_nonlinearity[1][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_x_negative_moment = rotational_release_mt_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_mt_nonlinearity[1][2]

            elif rotational_release_mt_nonlinearity[1][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_x_negative_moment = rotational_release_mt_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_mt_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_x_positive_type = rotational_release_mt_nonlinearity[2][0].name

            if rotational_release_mt_nonlinearity[2][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_mt_nonlinearity[2][1]

            elif rotational_release_mt_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_x_positive_displacement = rotational_release_mt_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_mt_nonlinearity[2][2]

            elif rotational_release_mt_nonlinearity[2][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_x_positive_moment = rotational_release_mt_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_mt_nonlinearity[2][2]

            elif rotational_release_mt_nonlinearity[2][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_x_positive_moment = rotational_release_mt_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_mt_nonlinearity[2][2]

        elif rotational_release_mt_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.moment_release_mt_nonlinearity = rotational_release_mt_nonlinearity[0].name

            clientObject.diagram_around_x_symmetric = rotational_release_mt_nonlinearity[1][0]
            clientObject.diagram_around_x_is_sorted = True

            if rotational_release_mt_nonlinearity[1][0]:
                clientObject.diagram_around_x_start = rotational_release_mt_nonlinearity[1][1].name
                clientObject.diagram_around_x_end = rotational_release_mt_nonlinearity[1][1].name

            else:
                clientObject.diagram_around_x_start = rotational_release_mt_nonlinearity[1][1].name
                clientObject.diagram_around_x_end = rotational_release_mt_nonlinearity[1][2].name

            clientObject.diagram_around_x_table = Model.clientModel.factory.create('ns0:nodal_release_type.diagram_around_x_table')

            for i,j in enumerate(rotational_release_mt_nonlinearity[2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_around_x_table_row')
                mlvlp.no = i+1
                mlvlp.row = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_around_x_table')
                clearAttributes(mlvlp.row)
                mlvlp.row.rotation = rotational_release_mt_nonlinearity[2][i][0]
                mlvlp.row.moment = rotational_release_mt_nonlinearity[2][i][1]

                clientObject.diagram_around_x_table.nodal_release_type_diagram_around_x_table.append(mlvlp)

        else:
            raise TypeError('Incorrect Nodal Release Nonlinearity Type')

        # Rotational Release My Nonlinearity
        if rotational_release_my_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE\
        or rotational_release_my_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or rotational_release_my_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.moment_release_my_nonlinearity = rotational_release_my_nonlinearity[0].name

        # Partial Activity
        elif rotational_release_my_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.moment_release_my_nonlinearity = rotational_release_my_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_around_y_negative_type = rotational_release_my_nonlinearity[1][0].name

            if rotational_release_my_nonlinearity[1][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_y_negative_slippage = rotational_release_my_nonlinearity[1][1]

            elif rotational_release_my_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_y_negative_displacement = rotational_release_my_nonlinearity[1][1]
                clientObject.partial_activity_around_y_negative_slippage = rotational_release_my_nonlinearity[1][2]

            elif rotational_release_my_nonlinearity[1][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_y_negative_moment = rotational_release_my_nonlinearity[1][1]
                clientObject.partial_activity_around_y_negative_slippage = rotational_release_my_nonlinearity[1][2]

            elif rotational_release_my_nonlinearity[1][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_y_negative_moment = rotational_release_my_nonlinearity[1][1]
                clientObject.partial_activity_around_y_negative_slippage = rotational_release_my_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_y_positive_type = rotational_release_my_nonlinearity[2][0].name

            if rotational_release_my_nonlinearity[2][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_y_positive_slippage = rotational_release_my_nonlinearity[2][1]

            elif rotational_release_my_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_y_positive_displacement = rotational_release_my_nonlinearity[2][1]
                clientObject.partial_activity_around_y_positive_slippage = rotational_release_my_nonlinearity[2][2]

            elif rotational_release_my_nonlinearity[2][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_y_positive_moment = rotational_release_my_nonlinearity[2][1]
                clientObject.partial_activity_around_y_positive_slippage = rotational_release_my_nonlinearity[2][2]

            elif rotational_release_my_nonlinearity[2][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_y_positive_moment = rotational_release_my_nonlinearity[2][1]
                clientObject.partial_activity_around_y_positive_slippage = rotational_release_my_nonlinearity[2][2]

        elif rotational_release_my_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.moment_release_my_nonlinearity = rotational_release_my_nonlinearity[0].name

            clientObject.diagram_around_y_symmetric = rotational_release_my_nonlinearity[1][0]
            clientObject.diagram_around_y_is_sorted = True

            if rotational_release_my_nonlinearity[1][0]:
                clientObject.diagram_around_y_start = rotational_release_my_nonlinearity[1][1].name
                clientObject.diagram_around_y_end = rotational_release_my_nonlinearity[1][1].name

            else:
                clientObject.diagram_around_y_start = rotational_release_my_nonlinearity[1][1].name
                clientObject.diagram_around_y_end = rotational_release_my_nonlinearity[1][2].name

            clientObject.diagram_around_y_table = Model.clientModel.factory.create('ns0:nodal_release_type.diagram_around_y_table')

            for i,j in enumerate(rotational_release_my_nonlinearity[2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_around_y_table_row')
                mlvlp.no = i+1
                mlvlp.row = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_around_y_table')
                clearAttributes(mlvlp.row)
                mlvlp.row.rotation = rotational_release_my_nonlinearity[2][i][0]
                mlvlp.row.moment = rotational_release_my_nonlinearity[2][i][1]

                clientObject.diagram_around_y_table.nodal_release_type_diagram_around_y_table.append(mlvlp)

        else:
            raise TypeError('Incorrect Nodal Release Nonlinearity Type')

        # Rotational Release Mz Nonlinearity
        if rotational_release_mz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_NONE \
        or rotational_release_mz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE \
        or rotational_release_mz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_FAILURE_IF_POSITIVE :
            clientObject.moment_release_mz_nonlinearity = rotational_release_mz_nonlinearity[0].name

        # Partial Activity
        elif rotational_release_mz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
            clientObject.moment_release_mz_nonlinearity = rotational_release_mz_nonlinearity[0].name

            # Negative Zone
            clientObject.partial_activity_around_z_negative_type = rotational_release_mz_nonlinearity[1][0].name

            if rotational_release_mz_nonlinearity[1][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_z_negative_slippage = rotational_release_mz_nonlinearity[1][1]

            elif rotational_release_mz_nonlinearity[1][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_z_negative_displacement = rotational_release_mz_nonlinearity[1][1]
                clientObject.partial_activity_around_z_negative_slippage = rotational_release_mz_nonlinearity[1][2]

            elif rotational_release_mz_nonlinearity[1][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_z_negative_moment = rotational_release_mz_nonlinearity[1][1]
                clientObject.partial_activity_around_z_negative_slippage = rotational_release_mz_nonlinearity[1][2]

            elif rotational_release_mz_nonlinearity[1][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_z_negative_moment = rotational_release_mz_nonlinearity[1][1]
                clientObject.partial_activity_around_z_negative_slippage = rotational_release_mz_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_z_positive_type = rotational_release_mz_nonlinearity[2][0].name

            if rotational_release_mz_nonlinearity[2][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_z_positive_slippage = rotational_release_mz_nonlinearity[2][1]

            elif rotational_release_mz_nonlinearity[2][0] == NodalReleaseTypePartialActivityAlong.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_z_positive_displacement = rotational_release_mz_nonlinearity[2][1]
                clientObject.partial_activity_around_z_positive_slippage = rotational_release_mz_nonlinearity[2][2]

            elif rotational_release_mz_nonlinearity[2][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT:
                clientObject.partial_activity_around_z_positive_moment = rotational_release_mz_nonlinearity[2][1]
                clientObject.partial_activity_around_z_positive_slippage = rotational_release_mz_nonlinearity[2][2]

            elif rotational_release_mz_nonlinearity[2][0] == NodalReleaseTypePartialActivityAround.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_z_positive_moment = rotational_release_mz_nonlinearity[2][1]
                clientObject.partial_activity_around_z_positive_slippage = rotational_release_mz_nonlinearity[2][2]

        elif rotational_release_mz_nonlinearity[0] == NodalReleaseTypeReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.moment_release_mz_nonlinearity = rotational_release_mz_nonlinearity[0].name

            clientObject.diagram_around_z_symmetric = rotational_release_my_nonlinearity[1][0]
            clientObject.diagram_around_z_is_sorted = True

            if rotational_release_mz_nonlinearity[1][0]:
                clientObject.diagram_around_z_start = rotational_release_mz_nonlinearity[1][1].name
                clientObject.diagram_around_z_end = rotational_release_mz_nonlinearity[1][1].name

            else:
                clientObject.diagram_around_z_start = rotational_release_mz_nonlinearity[1][1].name
                clientObject.diagram_around_z_end = rotational_release_mz_nonlinearity[1][2].name

            clientObject.diagram_around_z_table = Model.clientModel.factory.create('ns0:nodal_release_type.diagram_around_z_table')

            for i,j in enumerate(rotational_release_mz_nonlinearity[2]):
                mlvlp = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_around_z_table_row')
                mlvlp.no = i+1
                mlvlp.row = Model.clientModel.factory.create('ns0:nodal_release_type_diagram_around_z_table')
                clearAttributes(mlvlp.row)
                mlvlp.row.rotation = rotational_release_mz_nonlinearity[2][i][0]
                mlvlp.row.moment = rotational_release_mz_nonlinearity[2][i][1]

                clientObject.diagram_around_z_table.nodal_release_type_diagram_around_z_table.append(mlvlp)

        else:
            raise TypeError('Incorrect Nodal Release Nonlinearity Type')

        # Nodal Release Local Axis System Object Type
        clientObject.local_axis_system_object_type = local_axis_system.name

        # Nodal Release Local Axis System Reference Object
        clientObject.local_axis_system_reference_object = local_axis_system_reference_object

        # Nodal Release Type User defined name
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

        # Add Nodal Release Type to client model
        model.clientModel.service.set_nodal_release_type(clientObject)
