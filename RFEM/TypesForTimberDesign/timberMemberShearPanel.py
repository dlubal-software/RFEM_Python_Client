from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import PositionOnSection

class TimberMemberShearPanel():
    def __init__(self,
                no: int = 1,
                name: str = '',
                members: str = "",
                member_sets: str = "",
                position_on_section = PositionOnSection.POSITION_ON_UPPER_FLANGE,
                stiffness: float = 1000,
                position_on_section_value: float = 0.005,
                comment: str = '',
                params: dict = None):
        """
        Args:
            no (int): Timber Member Shear Panel Tag
            name (str): User Defined Member Shear Panel Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            position_on_section (enum): Position On Section
            stiffness (float): Shear Panel Stiffness
            position_on_section_value (float): Position On Section Value if POsition On Section equals POSITION_DEFINE
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        """

         # Client Model | Types For Timber Design Member Shear Panel
        clientObject = Model.clientModel.factory.create('ns0:timber_member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Member Shear Panel Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Shear Panel User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Shear Panel Definition Type
        clientObject.definition_type = 'DEFINITION_TYPE_DEFINE_S_PROV'

        # Member Shear Panel Position On Section
        clientObject.position_on_section = position_on_section.name

        if clientObject.position_on_section == 'POSITION_DEFINE':
            clientObject.position_on_section_value = position_on_section_value

        # Member Shear Panel Stiffness
        clientObject.stiffness = stiffness

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Timber Effective Lengths to client model
        Model.clientModel.service.set_timber_member_shear_panel(clientObject)
