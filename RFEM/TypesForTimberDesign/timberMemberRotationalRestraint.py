from multiprocessing.sharedctypes import Value
from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString, GetAddonStatus, SetAddonStatus
from RFEM.enums import AddOn

class TimberMemberRotationalRestraint():
    def __init__(self,
                no: int = 1,
                name: str = '',
                members: str = "",
                member_sets: str = "",
                spring_stiffness: float = 20000,
                comment: str = '',
                params: dict = None,
                model = Model):
        """
        Args:
            no (int): Timber Member Rotational Restraint Tag
            name (str): User Defined Member Rotational Restraint Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            spring_stiffness (float): Total Rotational Spring Stiffness
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Deducing RFEM Language from timber_design_addon String:
        modelInfo = Model.clientModel.service.get_model_info()
        if modelInfo.property_addon_timber_design.split()[0] != 'Timber':
            raise ValueError("WARNING: The TimberMemberRotationalRestraints operates with the RFEM Application set to English. Kindly switch RFEM to English such that Database searches can completed successfully.")

        # Check if Timber Design Add-on is ON.
        if not GetAddonStatus(model.clientModel, AddOn.timber_design_active):
            SetAddonStatus(model.clientModel, AddOn.timber_design_active, True)

        # Client Model / Types For Timber Design Member Rotational Restraints
        clientObject = model.clientModel.factory.create('ns0:timber_member_rotational_restraint')

        # Clears Object Attributes / Sets all the attributes to None
        clearAttributes(clientObject)

        # Member Rotational Restraint No.
        clientObject.no = no

        # Member Rotational Restraint Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Member Rotational Restraint Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Rotational Restraint Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Rotational Restraint Type
        clientObject.type = 'TYPE_MANUALLY'

        # Member Rotational Spring Stiffness
        clientObject.total_rotational_spring_stiffness = spring_stiffness

        #Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Timber Member Rotational Restraint to Client Model
        model.clientModel.service.set_timber_member_rotational_restraint(clientObject)
