from http import client
from RFEM.initModel import Model, clearAttributes, ConvertToDlString

class SteelDesignUltimateConfigurations():

    def __init__(self,
                 no: int = 1,
                 user_defined_name: list = [False],
                 members_no: str = 'All',
                 member_sets_no: str = 'All',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client Model | Steel Design Ultimate Configurations
        clientObject = model.clientModel.factory.create('ns0:steel_design_uls_configuration')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # ULS Configuration No.
        clientObject.no = no

        # User Defined Name
        if user_defined_name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = user_defined_name[1]

        else:
            clientObject.user_defined_name_enabled = False

        # Assigned Members
        if members_no == 'All':
            clientObject.assigned_to_all_members = True

        else:
            clientObject.assigned_to_all_members = False
            clientObject.assigned_to_members = ConvertToDlString(members_no)

        #Assigned Member Sets
        if member_sets_no == 'All':
            clientObject.assigned_to_all_member_sets = True

        else:
            clientObject.assigned_to_all_member_sets = False
            clientObject.assigned_to_member_sets = ConvertToDlString(member_sets_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Global Parameters to Client Model
        model.clientModel.service.set_steel_design_uls_configuration(clientObject)

