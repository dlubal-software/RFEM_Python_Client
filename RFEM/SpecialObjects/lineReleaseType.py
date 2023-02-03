from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.dataTypes import inf
from RFEM.enums import TranslationalReleaseNonlinearity, RotationalReleaseNonlinearity, LineReleaseLocalAxisSystem, \
    PartialActivityAlongType, PartialActivityAroundType

class LineReleaseType():

    def __init__(self,
                 no: int = 1,
                 spring_constant: list = [inf, inf, inf, inf],
                 translational_release_ux_nonlinearity: list = [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE, [None], [None]],
                 translational_release_uy_nonlinearity: list = [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE, [None], [None]],
                 translational_release_uz_nonlinearity: list = [TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE, [None], [None]],
                 rotational_release_phi_x_nonlinearity: list = [RotationalReleaseNonlinearity.NONLINEARITY_TYPE_NONE, [None], [None]],
                 local_axis_system = LineReleaseLocalAxisSystem.LOCAL_AXIS_SYSTEM_TYPE_ORIGINAL_LINE,
                 system_para: list = [0],
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Line Release Type

        Args:
            no (int): Line Release Type Tag
            spring_constant (list): Spring Constant List
            translational_release_ux_nonlinearity (list of lists): Nonlinearity Parameter for Translation Release along X Direction
            translational_release_ux_nonlinearity (list of lists): Nonlinearity Parameter for Translation Release along Y Direction
            translational_release_ux_nonlinearity (list of lists): Nonlinearity Parameter for Translation Release along Z Direction
                for translational_release_ux/y/z_nonlinearity[0] == TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
                    translational_release_ux/y/z_nonlinearity = [nonlinearity type Partial_Activity, negative zone, positive zone]
                    for negative/positive zone[0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                        negative/positive zone = [negative/positive zone type, slippage]
                    for negative/positive zone[0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED:
                        negative/positive zone = [negative/positive zone type, slippage, displacement]  (Note: Displacement must be greater than slippage)
                    for negative/positive zone[0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE/PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                        negative/positive zone = [negative/positive zone type, slippage, force]
                for translational_release_ux/y/z_nonlinearity[0] == TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
                    translational_release_ux/y/z_nonlinearity = [nonlinearity type Diagram, [symmetric(bool), LineReleaseDiagram Enumeration(start), LineReleaseDiagram Enumeration(end)], [[displacement, force],...]]
            rotational_release_phi_x_nonlinearity (list of lists): Nonlinearity Parameter for Rotational Release around X Direction
                for rotational_release_phi_x_nonlinearity[0] == RotationalReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:
                    rotational_release_phi_x_nonlinearity = [nonlinearity type Partial_Activity, negative zone, positive zone]
                    for negative/positive zone[0] == RotationalReleaseNonlinearity.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                        negative/positive zone = [negative/positive zone type, slippage]
                    for negative/positive zone[0] == RotationalReleaseNonlinearity.PARTIAL_ACTIVITY_TYPE_FIXED:
                        negative/positive zone = [negative/positive zone type, slippage, rotation]
                    for negative/positive zone[0] == RotationalReleaseNonlinearity.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT/PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                        negative/positive zone = [negative/positive zone type, slippage, moment]
                for rotational_release_phi_x_nonlinearity[0] == RotationalReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
                    rotational_release_phi_x_nonlinearity = [nonlinearity type Diagram, [symmetric(bool), LineReleaseDiagram Enumeration(start), LineReleaseDiagram Enumeration(end)], [[rotation, moment],...]]
                for rotational_release_phi_x_nonlinearity[0] == RotationalReleaseNonlinearity.NONLINEARITY_TYPE_FORCE_MOMENT_DIAGRAM:
                    rotational_release_phi_x_nonlinearity = [nonlinearity type Force_Moment_Diagram, [symmetric(bool), LineReleaseForceMomentDiagram Enumeration(end), LineReleaseForceMomentDepend Enumeration],
                                                             [[force, max_moment, min_moment(if not symetric)],...]]
            local_axis_system (enum): Line Release Local Axis System Enumeration
            system_para (list): System Parameters
                for local_axis_system ==LineReleaseLocalAxisSystem.LOCAL_AXIS_SYSTEM_TYPE_ORIGINAL_LINE:
                    system_para = [rotational_angle]
                for local_axis_system ==LineReleaseLocalAxisSystem.LOCAL_AXIS_SYSTEM_TYPE_Z_AXIS_PERPENDICULAR_TO_SURFACE:
                    system_para = [rotational_angle, surface_tag]
                for local_axis_system ==LineReleaseLocalAxisSystem.E_LOCAL_AXIS_SYSTEM_TYPE_HELP_NODE:
                    system_para = [rotational_angle, node_tag, local_axis_system_object_in_plane]
            name (str): User Defined Name
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
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
        clientObject.translational_release_u_x_nonlinearity = translational_release_ux_nonlinearity[0].name
        clientObject.translational_release_u_y_nonlinearity = translational_release_uy_nonlinearity[0].name
        clientObject.translational_release_u_z_nonlinearity = translational_release_uz_nonlinearity[0].name
        clientObject.rotational_release_phi_x_nonlinearity = rotational_release_phi_x_nonlinearity[0].name

        # Line Release Nonlinearity Parameters for Partial Activity
        # For translational_release_u_x_nonlinearity
        if translational_release_ux_nonlinearity[0] == TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:

            # Negative Zone
            clientObject.partial_activity_along_x_negative_type = translational_release_ux_nonlinearity[1][0].name

            if translational_release_ux_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_x_negative_slippage = translational_release_ux_nonlinearity[1][1]

            elif translational_release_ux_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_x_negative_slippage = translational_release_ux_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_displacement = translational_release_ux_nonlinearity[1][2]

            elif translational_release_ux_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE \
            or translational_release_ux_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_x_negative_slippage = translational_release_ux_nonlinearity[1][1]
                clientObject.partial_activity_along_x_negative_force = translational_release_ux_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_x_positive_type = translational_release_ux_nonlinearity[2][0].name

            if translational_release_ux_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_x_positive_slippage = translational_release_ux_nonlinearity[2][1]

            elif translational_release_ux_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_x_positive_slippage = translational_release_ux_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_displacement = translational_release_ux_nonlinearity[2][2]

            elif translational_release_ux_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE \
            or translational_release_ux_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_x_positive_slippage = translational_release_ux_nonlinearity[2][1]
                clientObject.partial_activity_along_x_positive_force = translational_release_ux_nonlinearity[2][2]

        # For translational_release_u_y_nonlinearity
        if translational_release_uy_nonlinearity[0] == TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:

            # Negative Zone
            clientObject.partial_activity_along_y_negative_type = translational_release_uy_nonlinearity[1][0].name

            if translational_release_uy_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_y_negative_slippage = translational_release_uy_nonlinearity[1][1]

            elif translational_release_uy_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_y_negative_slippage = translational_release_uy_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_displacement = translational_release_uy_nonlinearity[1][2]

            elif translational_release_uy_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE \
            or translational_release_uy_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_y_negative_slippage = translational_release_uy_nonlinearity[1][1]
                clientObject.partial_activity_along_y_negative_force = translational_release_uy_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_y_positive_type = translational_release_uy_nonlinearity[2][0].name

            if translational_release_uy_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_y_positive_slippage = translational_release_uy_nonlinearity[2][1]

            elif translational_release_uy_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_y_positive_slippage = translational_release_uy_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_displacement = translational_release_uy_nonlinearity[2][2]

            elif translational_release_uy_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE \
            or translational_release_uy_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_y_positive_slippage = translational_release_uy_nonlinearity[2][1]
                clientObject.partial_activity_along_y_positive_force = translational_release_uy_nonlinearity[2][2]

        # For translational_release_u_z_nonlinearity
        if translational_release_uz_nonlinearity[0] == TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:

            # Negative Zone
            clientObject.partial_activity_along_z_negative_type = translational_release_uz_nonlinearity[1][0].name

            if translational_release_uz_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_z_negative_slippage = translational_release_uz_nonlinearity[1][1]

            elif translational_release_uz_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_z_negative_slippage = translational_release_uz_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_displacement = translational_release_uz_nonlinearity[1][2]

            elif translational_release_uz_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE \
            or translational_release_uz_nonlinearity[1][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_z_negative_slippage = translational_release_uz_nonlinearity[1][1]
                clientObject.partial_activity_along_z_negative_force = translational_release_uz_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_along_z_positive_type = translational_release_uz_nonlinearity[2][0].name

            if translational_release_uz_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_along_z_positive_slippage = translational_release_uz_nonlinearity[2][1]

            elif translational_release_uz_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_along_z_positive_slippage = translational_release_uz_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_displacement = translational_release_uz_nonlinearity[2][2]

            elif translational_release_uz_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_FORCE \
            or translational_release_uz_nonlinearity[2][0] == PartialActivityAlongType.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_FORCE:
                clientObject.partial_activity_along_z_positive_slippage = translational_release_uz_nonlinearity[2][1]
                clientObject.partial_activity_along_z_positive_force = translational_release_uz_nonlinearity[2][2]

        # For rotational_release_phi_x_nonlinearity
        if rotational_release_phi_x_nonlinearity[0] == RotationalReleaseNonlinearity.NONLINEARITY_TYPE_PARTIAL_ACTIVITY:

            # Negative Zone
            clientObject.partial_activity_around_x_negative_type = rotational_release_phi_x_nonlinearity[1][0].name

            if rotational_release_phi_x_nonlinearity[1][0] == PartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_phi_x_nonlinearity[1][1]

            elif rotational_release_phi_x_nonlinearity[1][0] == PartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_phi_x_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_rotation = rotational_release_phi_x_nonlinearity[1][2]

            elif rotational_release_phi_x_nonlinearity[1][0] == PartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT \
            or rotational_release_phi_x_nonlinearity[1][0] == PartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_x_negative_slippage = rotational_release_phi_x_nonlinearity[1][1]
                clientObject.partial_activity_around_x_negative_moment = rotational_release_phi_x_nonlinearity[1][2]

            # Positive Zone
            clientObject.partial_activity_around_x_positive_type = rotational_release_phi_x_nonlinearity[2][0].name

            if rotational_release_phi_x_nonlinearity[2][0] == PartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_COMPLETE:
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_phi_x_nonlinearity[2][1]

            elif rotational_release_phi_x_nonlinearity[2][0] == PartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_FIXED:
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_phi_x_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_rotation = rotational_release_phi_x_nonlinearity[2][2]

            elif rotational_release_phi_x_nonlinearity[2][0] == PartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_FAILURE_FROM_MOMENT \
            or rotational_release_phi_x_nonlinearity[2][0] == PartialActivityAroundType.PARTIAL_ACTIVITY_TYPE_YIELDING_FROM_MOMENT:
                clientObject.partial_activity_around_x_positive_slippage = rotational_release_phi_x_nonlinearity[2][1]
                clientObject.partial_activity_around_x_positive_moment = rotational_release_phi_x_nonlinearity[2][2]

        # Line Release Nonlinearity Parameters for Diagram
        # For translational_release_u_x_nonlinearity
        if translational_release_ux_nonlinearity[0] == TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.diagram_along_x_symmetric = translational_release_ux_nonlinearity[1][0]
            clientObject.diagram_along_x_is_sorted = True

            if translational_release_ux_nonlinearity[1][0]:
                clientObject.diagram_along_x_start = translational_release_ux_nonlinearity[1][1].name
                clientObject.diagram_along_x_end = translational_release_ux_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_x_start = translational_release_ux_nonlinearity[1][1].name
                clientObject.diagram_along_x_end = translational_release_ux_nonlinearity[1][2].name

            clientObject.diagram_along_x_table = Model.clientModel.factory.create('ns0:line_release_type.diagram_along_x_table')

            for i,j in enumerate(translational_release_ux_nonlinearity[2]):
                lrtdx = Model.clientModel.factory.create('ns0:line_release_type_diagram_along_x_table_row')
                lrtdx.no = i+1
                lrtdx.row.displacement = translational_release_ux_nonlinearity[2][i][0]
                lrtdx.row.force = translational_release_ux_nonlinearity[2][i][1]

                clientObject.diagram_along_x_table.line_release_type_diagram_along_x_table.append(lrtdx)

        # For translational_release_u_y_nonlinearity
        if translational_release_uy_nonlinearity[0] == TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.diagram_along_y_symmetric = translational_release_uy_nonlinearity[1][0]
            clientObject.diagram_along_y_is_sorted = True

            if translational_release_uy_nonlinearity[1][0]:
                clientObject.diagram_along_y_start = translational_release_uy_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = translational_release_uy_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_y_start = translational_release_uy_nonlinearity[1][1].name
                clientObject.diagram_along_y_end = translational_release_uy_nonlinearity[1][2].name

            clientObject.diagram_along_y_table = Model.clientModel.factory.create('ns0:line_release_type.diagram_along_y_table')

            for i,j in enumerate(translational_release_uy_nonlinearity[2]):
                lrtdy = Model.clientModel.factory.create('ns0:line_release_type_diagram_along_y_table_row')
                lrtdy.no = i+1
                lrtdy.row.displacement = translational_release_uy_nonlinearity[2][i][0]
                lrtdy.row.force = translational_release_uy_nonlinearity[2][i][1]

                clientObject.diagram_along_y_table.line_release_type_diagram_along_y_table.append(lrtdy)

        # For translational_release_u_z_nonlinearity
        if translational_release_uz_nonlinearity[0] == TranslationalReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.diagram_along_z_symmetric = translational_release_uz_nonlinearity[1][0]
            clientObject.diagram_along_z_is_sorted = True

            if translational_release_uz_nonlinearity[1][0]:
                clientObject.diagram_along_z_start = translational_release_uz_nonlinearity[1][1].name
                clientObject.diagram_along_z_end = translational_release_uz_nonlinearity[1][1].name

            else:
                clientObject.diagram_along_z_start = translational_release_uz_nonlinearity[1][1].name
                clientObject.diagram_along_z_end = translational_release_uz_nonlinearity[1][2].name

            clientObject.diagram_along_z_table = Model.clientModel.factory.create('ns0:line_release_type.diagram_along_z_table')

            for i,j in enumerate(translational_release_uz_nonlinearity[2]):
                lrtdz = Model.clientModel.factory.create('ns0:line_release_type_diagram_along_z_table_row')
                lrtdz.no = i+1
                lrtdz.row.displacement = translational_release_uz_nonlinearity[2][i][0]
                lrtdz.row.force = translational_release_uz_nonlinearity[2][i][1]

                clientObject.diagram_along_z_table.line_release_type_diagram_along_z_table.append(lrtdz)

        # For rotational_release_phi_x_nonlinearity
        if rotational_release_phi_x_nonlinearity[0] == RotationalReleaseNonlinearity.NONLINEARITY_TYPE_DIAGRAM:
            clientObject.diagram_around_x_symmetric = rotational_release_phi_x_nonlinearity[1][0]
            clientObject.diagram_around_x_is_sorted = True

            if rotational_release_phi_x_nonlinearity[1][0]:
                clientObject.diagram_around_x_start = rotational_release_phi_x_nonlinearity[1][1].name
                clientObject.diagram_around_x_end = rotational_release_phi_x_nonlinearity[1][1].name

            else:
                clientObject.diagram_around_x_start = rotational_release_phi_x_nonlinearity[1][1].name
                clientObject.diagram_around_x_end = rotational_release_phi_x_nonlinearity[1][2].name

            clientObject.diagram_around_x_table = Model.clientModel.factory.create('ns0:array_of_line_release_type_diagram_around_x_table')

            for i,j in enumerate(rotational_release_phi_x_nonlinearity[2]):
                lrtdr = Model.clientModel.factory.create('ns0:line_release_type_diagram_around_x_table_row')
                lrtdr.no = i+1
                lrtdr.row.rotation = rotational_release_phi_x_nonlinearity[2][i][0]
                lrtdr.row.moment = rotational_release_phi_x_nonlinearity[2][i][1]

                clientObject.diagram_around_x_table.line_release_type_diagram_around_x_table.append(lrtdr)

        # Line Release Nonlinearity Parameters for Force Moment Diagram
        # For For rotational_release_phi_x_nonlinearity
        if rotational_release_phi_x_nonlinearity[0] == RotationalReleaseNonlinearity.NONLINEARITY_TYPE_FORCE_MOMENT_DIAGRAM:
            clientObject.force_moment_diagram_around_x_symmetric = rotational_release_phi_x_nonlinearity[1][0]
            clientObject.force_moment_diagram_around_x_is_sorted = True
            clientObject.force_moment_diagram_around_x_end = rotational_release_phi_x_nonlinearity[1][1].name
            clientObject.force_moment_diagram_around_x_depends_on = rotational_release_phi_x_nonlinearity[1][2].name

            clientObject.force_moment_diagram_around_x_table = Model.clientModel.factory.create('ns0:line_release_type.force_moment_diagram_around_x_table')

            for i,j in enumerate(rotational_release_phi_x_nonlinearity[2]):
                lrtfm = Model.clientModel.factory.create('ns0:line_release_type_force_moment_diagram_around_x_table_row')
                lrtfm.no = i+1
                lrtfm.row.force = rotational_release_phi_x_nonlinearity[2][i][0]
                lrtfm.row.max_moment = rotational_release_phi_x_nonlinearity[2][i][1]
                if rotational_release_phi_x_nonlinearity[1][0]:
                    lrtfm.row.min_moment = rotational_release_phi_x_nonlinearity[2][i][1]
                else:
                    lrtfm.row.min_moment = rotational_release_phi_x_nonlinearity[2][i][2]

                clientObject.force_moment_diagram_around_x_table.line_release_type_force_moment_diagram_around_x_table.append(lrtfm)

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
