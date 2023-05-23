from RFEM.enums import MemberSupportNonlinearity
from RFEM.initModel import Model, clearAttributes, ConvertToDlString, deleteEmptyAttributes
from RFEM.dataTypes import inf

class MemberSupport():

    def __init__(self,
                 no: int = 1,
                 members: str = '',
                 spring_translation_x: float = 0.0,
                 spring_translation_y: float = 0.0,
                 spring_translation_z: list = [inf, MemberSupportNonlinearity.NONLINEARITY_NONE],
                 spring_rotation: float = 0.0,
                 spring_shear_x: float = 0.0,
                 spring_shear_y: float = 0.0,
                 spring_shear_z: float = 0.0,
                 member_shear_panel: int = 0,
                 member_rotational_restraint: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        """
        Args:
            no (int): Member Support Tag
            members (str): Assigned Members
            spring_translation_x (float): Translational X Spring Constant
            spring_translation_y (float): Translational Y Spring Constant
            spring_translation_z (list): [Translational Z Spring Constant, Nonlinearity Type]
            spring_rotation (float): Rotational Spring Constant
            spring_shear_x (float): Shear X Spring Constant
            spring_shear_y (float): Shear Y Spring Constant
            spring_shear_z (float): Shear Z Spring Constant
            member_shear_panel (list): Member Shear Panel Option
                if member_shear_panel[0] == True:
                    member_shear_panel[1] (int): Member Shear Panel Number
            member_rotational_restraint (list): Member Rotational Restraint Option
                if member_rotational_restraint[0] == True:
                    member_rotational_restraint[1] (int): Member Rotational Restraint Number
                    member_rotational_restraint[2] (float): Load Introduced from Sheeting to Beam
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member Support
        clientObject = model.clientModel.factory.create('ns0:member_support')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Support No.
        clientObject.no = no

        # Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Spring Translation
        clientObject.spring_rotation = spring_rotation
        clientObject.spring_translation_x = spring_translation_x
        clientObject.spring_translation_y = spring_translation_y
        clientObject.spring_translation_z = spring_translation_z[0]
        #clientObject.nonlinearity = spring_translation_z[1].name

        # Spring Shear
        clientObject.spring_shear_x = spring_shear_x
        clientObject.spring_shear_y = spring_shear_y
        clientObject.spring_shear_z = spring_shear_z

        # Member Shear Panel
        #clientObject.member_shear_panel_z = member_shear_panel
        #if member_shear_panel[0]:
        #    clientObject.member_shear_panel = member_shear_panel[1]

        # Member Rotational Restraint
        #☻clientObject.rotational_restraint_enabled = member_rotational_restraint[0]
        if member_rotational_restraint:
            clientObject.member_rotational_restraint = member_rotational_restraint[0]
            clientObject.load_introduced_from_sheeting_to_beam = member_rotational_restraint[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Support to client model
        model.clientModel.service.set_member_support(clientObject)
