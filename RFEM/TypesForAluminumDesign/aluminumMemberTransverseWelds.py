from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertStrToListOfInt
from RFEM.enums import WeldComponentType, MultipleOffsetDefinitionType, WeldingMethod

transverseWeldComponent = {
    'weld_type' : WeldComponentType.WELD_COMPONENT_TYPE_BUTT,
    'position' : 0.3,
    'multiple' : True,
    'multiple_number' : 2,
    'multiple_offset_definition_type' : MultipleOffsetDefinitionType.OFFSET_DEFINITION_TYPE_ABSOLUTE,
    'multiple_offset' : 2.0,
    'size' : 0.005,
    'method_type' : WeldingMethod.WELDING_METHOD_MIG,
    'number_of_heat_paths' : 2,
    'welding_temperature' : 2000.0
}

class AluminumMemberTransverseWeld():

    def __init__(self,
                 no: int = 1,
                 name: str = '',
                 members: str = '1 2',
                 member_sets: str = '',
                 component: list = [transverseWeldComponent],
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Line Welded Joint Tag
            name (str): Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            component (struct): Weld Components
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Aluminum Member Transverse Weld
        clientObject = model.clientModel.factory.create('ns0:aluminum_member_transverse_weld')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Weld No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Assigned to members
        clientObject.members = ConvertStrToListOfInt(members)

        # Assigned to member sets
        clientObject.member_sets = ConvertStrToListOfInt(member_sets)

        # Weld Components
        clientObject.components = model.clientModel.factory.create('ns0:array_of_aluminum_member_transverse_weld_components')

        count = 0
        for comp in component:
            clientWeld = model.clientModel.factory.create('ns0:aluminum_member_transverse_weld_components_row')
            clientWeld.no = count+1
            count = count+1
            clientWeld.row.weld_type = comp['weld_type'].name
            clientWeld.row.position = comp['position']
            clientWeld.row.multiple = comp['multiple']
            clientWeld.row.multiple_number = comp['multiple_number']
            clientWeld.row.multiple_offset_definition_type = comp['multiple_offset_definition_type'].name
            clientWeld.row.multiple_offset = comp['multiple_offset']
            clientWeld.row.size = comp['size']
            clientWeld.row.method_type = comp['method_type'].name
            clientWeld.row.number_of_heat_paths = comp['number_of_heat_paths']
            clientWeld.row.welding_temperature = comp['welding_temperature']

            clientObject.components.aluminum_member_transverse_weld_components.append(clientWeld)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Aluminum Member Transverse Weld to client model
        model.clientModel.service.set_aluminum_member_transverse_weld(clientObject)
