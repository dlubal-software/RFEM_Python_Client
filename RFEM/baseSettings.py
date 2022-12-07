from RFEM.initModel import Model
from RFEM.enums import GlobalAxesOrientationType, LocalAxesOrientationType

class BaseSettings():
    def __init__(self,
                gravitational_acceleration: int = 10,
                global_axes_orientation = GlobalAxesOrientationType.E_GLOBAL_AXES_ORIENTATION_ZDOWN,
                local_axes_orientation = LocalAxesOrientationType.E_LOCAL_AXES_ORIENTATION_ZDOWN,
                tolerances: list = [0.0005, 0.0005, 0.0005, 0.0005],
                member_representatives: bool = False,
                member_set_representatives: bool = False,
                model = Model):
        """
        Args:
            gravitational_acceleration (int): Gravitational Acceleration (m/sn2)
            global_axes_orientation (enum): Global Axes Orientation Enumeration
            local_axes_orientation (Enum): Local Axes Orientation Enumeration
            tolerances (list): Tolerances List
                tolerances = [tolerance_for_nodes, tolerance_for_lines, tolerance_for_surfaces_and_planes, tolerance_for_directions]
            member_representatives (bool): Member Representatives
            member_set_representatives (bool): Member Set Representatives
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Get Model Settings
        clientObject = model.clientModel.service.get_model_settings_and_options()

        # Gravitational Acceleration
        clientObject.gravitational_acceleration = gravitational_acceleration

        # Global Axes Orientation
        clientObject.global_axes_orientation = global_axes_orientation.name

        # Local Axes Orientation
        clientObject.local_axes_orientation = local_axes_orientation.name

        # Tolerances
        if len(tolerances) != 4:
            raise ValueError("WARNING:Expected size of the array. Kindly check the list correctness.")

        clientObject.tolerance_for_nodes = tolerances[0]
        clientObject.tolerance_for_lines = tolerances[1]
        clientObject.tolerance_for_surfaces_and_planes = tolerances[2]
        clientObject.tolerance_for_directions = tolerances[3]

        # Member Representatives
        clientObject.member_representatives_active = member_representatives

        # Member Set Representatives
        clientObject.member_set_representatives_active = member_set_representatives

        # Add Base Data Settings to client model
        model.clientModel.service.set_model_settings_and_options(clientObject)
