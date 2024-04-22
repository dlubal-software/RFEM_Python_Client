from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import DesignSupportOrientationZType

class DesignSupport():

    def __init__(self,
                 no: int = 1,
                 members: str = '1',
                 member_sets: str = None,
                 nodes: str = '1 2',
                 support_in_z: list = [True, True, DesignSupportOrientationZType.DESIGN_SUPPORT_ORIENTATION_ZAXIS_POSITIVE, 0.1],
                 support_in_y: list = None,
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Design Support Type General

        Args:
            no (int): Design Support Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            nodes (str): Assigned Nodes
            support_in_z (list): List of Parameters for Support in Z Axis
            support_in_y (list): List of Parameters for Support in Y Axis
                for support_depth_by_section_width_of_member_z/y_enabled = True:
                    support_in_z/y = [activate support in z/y (bool), consider support in deflection design z/y (bool), design support orientation z/y type (enum), support width z/y (float)]
                for support_depth_by_section_width_of_member_z/y_enabled = False:
                    support_in_z/y = [activate support in z/y (bool), consider support in deflection design z/y (bool), design support orientation z/y type (enum), support width z/y (float), support depth z/y (float)]
            name (str, option): User Defined Design Support Name
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Design Support
        clientObject = model.clientModel.factory.create('ns0:design_support')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Design Support No.
        clientObject.no = no

        # Design Support Type
        clientObject.type = 'DESIGN_SUPPORT_TYPE_GENERAL'

        # Assigned Members (e.g. '5 6 7 12')
        if members:
            clientObject.assigned_to_members = ConvertToDlString(members)

        # Assigned Member Sets (e.g. '5 6 7 12')
        if member_sets:
            clientObject.assigned_to_member_sets = ConvertToDlString(member_sets)

        # Assigned Nodes (e.g. '5 6 7 12')
        clientObject.assigned_to_nodes = ConvertToDlString(nodes)

        # Support in Z
        if isinstance(support_in_z, list) and support_in_z[0] == True:
            clientObject.activate_in_z = support_in_z[0]
            clientObject.consider_in_deflection_design_z = support_in_z[1]
            clientObject.design_support_orientation_z = support_in_z[2].name
            clientObject.support_width_z = support_in_z[3]
            if len(support_in_z) == 5:
                clientObject.support_depth_by_section_width_of_member_z_enabled = False
                clientObject.support_depth_z = support_in_z[4]
            elif len(support_in_z) == 4:
                clientObject.support_depth_by_section_width_of_member_z_enabled = True
            else:
                raise ValueError('WARNING!: The suport in Z parameter needs to be length of 4 or 5. Kindly check list inputs for completeness and correctness.')

        elif support_in_z == None or support_in_z == False:
            clientObject.activate_in_z = False

        else:
            raise TypeError("WARNING! First parameter of list must be type bool. Kindly check list inputs completeness and correctness.")

        # Support in Y
        if isinstance(support_in_y, list) and support_in_y[0] == True:
            clientObject.activate_in_y = support_in_y[0]
            clientObject.consider_in_deflection_design_y = support_in_y[1]
            clientObject.design_support_orientation_y = support_in_y[2].name
            clientObject.support_width_y = support_in_y[3]
            if len(support_in_y) == 5:
                clientObject.support_depth_by_section_width_of_member_y_enabled = False
                clientObject.support_depth_y = support_in_y[4]
            elif len(support_in_y) == 4:
                clientObject.support_depth_by_section_width_of_member_y_enabled = True
            else:
                raise ValueError('WARNING!: The suport in Y parameter needs to be length of 4 or 5. Kindly check list inputs for completeness and correctness.')

        elif support_in_y == None or support_in_y == False:
            clientObject.activate_in_y = False

        else:
            raise TypeError("WARNING! First parameter of list must be type bool. Kindly check list inputs completeness and correctness.")

        # User Defined Name
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

        # Add Design Support to client model
        model.clientModel.service.set_design_support(clientObject)
