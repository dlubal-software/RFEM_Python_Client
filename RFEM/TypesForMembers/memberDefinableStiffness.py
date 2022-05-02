from RFEM.initModel import Model, clearAtributes, ConvertToDlString

class MemberDefinableStiffness():
    def __init__(self,
                 no: int = 1,
                 name: list = [False],
                 members: str = "1",
                 torsional_stiffness: int = 0.0,
                 bending_stiffness_y: int = 0.0,
                 bending_stiffness_z: int = 0.0,
                 axial_stiffness: int = 0.0,
                 shear_stiffness_y: int = 0.0,
                 shear_stiffness_z: int = 0.0,
                 specific_weight: int = 0.0,
                 section_area: int = 0.0,
                 rotation: int = 0.0,
                 thermal_expansion_alpha: int = 0.0,
                 thermal_expansion_width: int = 0.0,
                 thermal_expansion_height: int = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Member Definable Stiffness Tag
            name (list): User Defined Name

                if name[0] == True:
                    name[1] == Uer Defined Name

            members (str): Assigned Members
            torsional_stiffness (int): Torsional Stiffness
            bending_stiffness_y (int): Bending Stiffness in Y Direction
            bending_stiffness_z (int): Bendign Stiffness in Z Direction
            axial_stiffness (int): Axial Stiffness
            shear_stiffness_y (int): Shear Stiffness in Y Direction
            shear_stiffness_z (int): Shear Stiffness in Z Direction
            specific_weight (int): Specific Weight
            section_area (int): Section Area
            rotation (int): Rotation
            thermal_expansion_alpha (int): Thermal Expansion Alpha Coefficient
            thermal_expansion_width (int): Thermal Expansion Witdh Coefficient
            thermal_expansion_height (int): Thermal Expansion Height Coefficient
            comment (str, optional): Comment
            params (dict, optional): Parameters
            model (class, optional): Model instance
        """

        # Client model | Member Definable Stffness
        clientObject = model.clientModel.factory.create('ns0:member_definable_stiffness')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Definable Stffness No.
        clientObject.no = no

        # User Defined Name
        if name[0]:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name[1]
        else:
            clientObject.user_defined_name_enabled = False

        # Assigned Members (e.g. '5 6 7 12')
        clientObject.assigned_to = ConvertToDlString(members)

        # Torsional Stiffness
        clientObject.torsional_stiffness = torsional_stiffness

        # Bending Stiffnesses
        clientObject.bending_stiffness_y = bending_stiffness_y
        clientObject.bending_stiffness_z = bending_stiffness_z

        # Axial Stiffness
        clientObject.axial_stiffness = axial_stiffness

        # Shear Stiffnesses
        clientObject.shear_stiffness_y = shear_stiffness_y
        clientObject.shear_stiffness_z = shear_stiffness_z

        # Specific Weight
        clientObject.specific_weight = specific_weight

        # Section Area
        clientObject.section_area = section_area

        # Rotation
        clientObject.rotation = rotation

        # Thermal Expansions
        clientObject.thermal_expansion_alpha = thermal_expansion_alpha
        clientObject.thermal_expansion_width = thermal_expansion_width
        clientObject.thermal_expansion_height = thermal_expansion_height

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Member Definable Stffness to client model
        model.clientModel.service.set_member_definable_stiffness(clientObject)
