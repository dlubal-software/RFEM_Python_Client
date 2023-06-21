from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString

class MemberDefinableStiffness():
    def __init__(self,
                 no: int = 1,
                 name: str = 'MemberDefinableStiffness',
                 members: str = "1",
                 torsional_stiffness: float = 0.0,
                 bending_stiffness_y: float = 0.0,
                 bending_stiffness_z: float = 0.0,
                 axial_stiffness: float = 0.0,
                 shear_stiffness_y: float = 0.0,
                 shear_stiffness_z: float = 0.0,
                 specific_weight: float = 0.0,
                 section_area: float = 0.0,
                 rotation: float = 0.0,
                 thermal_expansion_alpha: float = 0.0,
                 thermal_expansion_width: float = 0.0,
                 thermal_expansion_height: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Member Definable Stiffness Tag
            name (str): User Defined Name
            members (str): Assigned Members
            torsional_stiffness (float): Torsional Stiffness
            bending_stiffness_y (float): Bending Stiffness in Y Direction
            bending_stiffness_z (float): Bendign Stiffness in Z Direction
            axial_stiffness (float): Axial Stiffness
            shear_stiffness_y (float): Shear Stiffness in Y Direction
            shear_stiffness_z (float): Shear Stiffness in Z Direction
            specific_weight (float): Specific Weight
            section_area (float): Section Area
            rotation (float): Rotation
            thermal_expansion_alpha (float): Thermal Expansion Alpha Coefficient
            thermal_expansion_width (float): Thermal Expansion Witdh Coefficient
            thermal_expansion_height (float): Thermal Expansion Height Coefficient
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member Definable Stffness
        clientObject = model.clientModel.factory.create('ns0:member_definable_stiffness')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Definable Stffness No.
        clientObject.no = no

        # User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

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

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Definable Stffness to client model
        model.clientModel.service.set_member_definable_stiffness(clientObject)
