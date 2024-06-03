from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import DesignSupportOrientationZType, DesignSupportOrientationYType

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
            support_in_z (list/bool): List of Parameters for Support in Z Axis
            support_in_y (list/bool): List of Parameters for Support in Y Axis
                for deactive support in z/y:
                    support_in_z/y (bool): Deactivate support in Z/Y (= False/None)
                for active support in z/y:
                    support_in_z/y[0] (bool): Activate Support in Z/Y (= True)
                    support_in_z/y[1] (bool): Consider Support in Deflection Design Z/Y
                    support_in_z/y[2] (enum): Design Support Orientation Z/Y Type Enumeration
                    support_in_z/y[3] (float): Support Width Z/Y (in meter)
                    for manual support depth:
                        support_in_z/y[4] (float): Support Depth Z/Y (in meter)
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

    @staticmethod
    def Concrete(no: int = 1,
                 members: str = '1',
                 member_sets: str = None,
                 nodes: str = '1 2',
                 support_in_z: list = [True, True, True, True, 1.0, 0.1],
                 support_in_y: bool = True,
                 name: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Design Support Type Concrete

        Args:
            no (int): Design Support Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            nodes (str): Assigned Nodes
            support_in_z (list): List of Parameters for Support in Z Axis
                for deactive support in z:
                    support_in_z (bool): Deactivate support in Z (= False/None)
                for active support in z:
                    support_in_z[0] (bool): Activate Support in Z (= True)
                    support_in_z[1] (bool): Consider Support in Deflection Design Z
                    support_in_z[2] (bool): Enable/Disable Direct Support Z
                    support_in_z[3] (bool): Enable/Disable Concrete Monolithic Connection Z
                    for inner_support_z_enabled == True:
                        support_in_z[4] (float): Concrete Ratio of Moment Redistribution Z (It must be in between 0.65 and 1.0)
                    for inner_support_z_enabled == False:
                        support_in_z[4] (bool): Deactivate Inner Support in Z (= False)
                    support_in_z[5] (float): Support Width Z (in meter)
                    for manual support depth:
                        support_in_z[6] (float): Support Depth Z (in meter)
            support_in_y (bool): Consider Support in Y Axis for Deflection Design (= True/False)
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
        clientObject.type = 'DESIGN_SUPPORT_TYPE_CONCRETE'

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
            clientObject.direct_support_z_enabled = support_in_z[2]
            clientObject.concrete_monolithic_connection_z_enabled = support_in_z[3]

            if isinstance(support_in_z[4], bool) and support_in_z[4] == False:
                clientObject.inner_support_z_enabled = False

            elif isinstance(support_in_z[4], (float, int)) and (0.65 <= support_in_z[4] <= 1):
                clientObject.inner_support_z_enabled = True
                clientObject.concrete_ratio_of_moment_redistribution_z = support_in_z[4]

            else:
                raise ValueError('WARNING!: The concrete ratio of moment redistribution in Z parameter must be between 0.65 and 1.0. Kindly check list inputs for completeness and correctness.')

            clientObject.support_width_z = support_in_z[5]

            if len(support_in_z) == 7:
                clientObject.support_depth_by_section_width_of_member_z_enabled = False
                clientObject.support_depth_z = support_in_z[6]

            elif len(support_in_z) == 6:
                clientObject.support_depth_by_section_width_of_member_z_enabled = True

            else:
                raise ValueError('WARNING!: The suport in Z parameter needs to be length of 6 or 7. Kindly check list inputs for completeness and correctness.')

        elif support_in_z == None or support_in_z == False:
            clientObject.activate_in_z = False

        else:
            raise TypeError("WARNING! First parameter of list must be type bool. Kindly check list inputs completeness and correctness.")

        # Support in Y
        if isinstance(support_in_y, bool) and support_in_y == True:
            clientObject.activate_in_y = True
            clientObject.consider_in_deflection_design_y = True

        elif support_in_y == None or support_in_y == False:
            clientObject.activate_in_y = False
            clientObject.consider_in_deflection_design_y = False

        else:
            raise TypeError("WARNING! Parameter must be type bool. Kindly check input completeness and correctness.")

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

    @staticmethod
    def Steel(no: int = 1,
              members: str = '1',
              member_sets: str = None,
              nodes: str = '1 2',
              support_in_z: list = [True, True, DesignSupportOrientationZType.DESIGN_SUPPORT_ORIENTATION_ZAXIS_POSITIVE, 0.01, 0.2, 0.25],
              support_in_y: list = None,
              name: str = None,
              comment: str = '',
              params: dict = None,
              model = Model):

        '''
        Design Support Type Steel

        Args:
            no (int): Design Support Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            nodes (str): Assigned Nodes
            support_in_z (list/bool): List of Parameters for Support in Z Axis
                for deactive support in z:
                    support_in_z (bool): Deactivate support in Z (= False/None)
                for active support in z:
                    support_in_z[0] (bool): Activate Support in Z (= True)
                    support_in_z[1] (bool): Consider Support in Deflection Design Z
                    support_in_z[2] (enum): Design Support Orientation Z Type Enumeration
                    for end_support_z_enabled == True:
                        support_in_z[3] (float): Overhanging Length for Support Z (in meter)
                    for end_support_z_enabled == False:
                        support_in_z[3] (bool): Deactivate End Support in Z (= False)
                    support_in_z[4] (float): Support Width Z (in meter)
                    for manual support depth:
                        support_in_z[5] (float): Support Depth Z (in meter)
            support_in_y (bool): Consider Support in Y Axis for Deflection Design (= True/False)
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
        clientObject.type = 'DESIGN_SUPPORT_TYPE_STEEL'

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

            if isinstance(support_in_z[3], bool) and support_in_z[3] == False:
                clientObject.end_support_z_enabled = False

            elif isinstance(support_in_z[3], (float, int)):
                clientObject.end_support_z_enabled = True
                clientObject.overhang_length_z = support_in_z[3]

            else:
                raise ValueError('WARNING!: Invalid list of parameters. Kindly check list inputs for completeness and correctness.')

            clientObject.support_width_z = support_in_z[4]

            if len(support_in_z) == 6:
                clientObject.support_depth_by_section_width_of_member_z_enabled = False
                clientObject.support_depth_z = support_in_z[5]

            elif len(support_in_z) == 5:
                clientObject.support_depth_by_section_width_of_member_z_enabled = True

            else:
                raise ValueError('WARNING!: The suport in Z parameter needs to be length of 5 or 6. Kindly check list inputs for completeness and correctness.')

        elif support_in_z == None or support_in_z == False:
            clientObject.activate_in_z = False

        else:
            raise TypeError("WARNING! First parameter of list must be type bool. Kindly check list inputs completeness and correctness.")

        # Support in Y
        if isinstance(support_in_y, bool) and support_in_y == True:
            clientObject.consider_in_deflection_design_y = True

        elif support_in_y == None or support_in_y == False:
            clientObject.consider_in_deflection_design_y = False

        else:
            raise TypeError("WARNING! Parameter must be type bool. Kindly check input completeness and correctness.")

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

    @staticmethod
    def Timber(no: int = 1,
               members: str = '1',
               member_sets: str = None,
               nodes: str = '1 2',
               support_in_z: list = [True, True, True, True, DesignSupportOrientationZType.DESIGN_SUPPORT_ORIENTATION_ZAXIS_POSITIVE, True, 1.25, 0.2, 0.25],
               support_in_y: list = [True, False, True, True, DesignSupportOrientationYType.DESIGN_SUPPORT_ORIENTATION_YAXIS_BOTH],
               name: str = None,
               comment: str = '',
               params: dict = None,
               model = Model):

        '''
        Design Support Type Timber

        Args:
            no (int): Design Support Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            nodes (str): Assigned Nodes
            support_in_z (list/bool): List of Parameters for Support in Z Axis
            support_in_y (list/bool): List of Parameters for Support in Y Axis
                for deactive support in z/y:
                    support_in_z/y (bool): Deactivate support in Z/Y (= False/None)
                for active support in z/y:
                    support_in_z/y[0] (bool): Activate Support in Z/Y (= True)
                    support_in_z/y[1] (bool): Enable/Disable Direct Support in Z/Y
                    support_in_z/y[2] (bool): Enable/Disable Inner Support in Z/Y
                    support_in_z/y[3] (bool): Consider Support in Deflection Design Z/Y
                    support_in_z/y[4] (enum): Design Support Orientation Z/Y Type Enumeration
                --> if direct support in z/y is enabled: (support_in_z/y[1] == True)
                        support_in_z/y[5] (bool): Consider Support in Fire Design Z/Y
                        support_in_z/y[6] (float): Timber Factor of Compression Z/Y (It must be in between 1.0 and 2.2)
                        support_in_z/y[7] (float): Support Width Z/Y (in meter)
                        for manual support depth:
                            support_in_z/y[8] (float): Support Depth Z/Y (in meter)
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
        clientObject.type = 'DESIGN_SUPPORT_TYPE_TIMBER'

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
            clientObject.direct_support_z_enabled = support_in_z[1]
            clientObject.inner_support_z_enabled = support_in_z[2]
            clientObject.consider_in_deflection_design_z = support_in_z[3]
            clientObject.design_support_orientation_z = support_in_z[4].name

            if support_in_z[1] == True:
                clientObject.consider_in_fire_design_z = support_in_z[5]

                if (1.0 <= support_in_z[6] <= 2.20):
                    clientObject.timber_factor_of_compression_z = support_in_z[6]

                else:
                    raise ValueError('WARNING!: The timber factor of compression in Z parameter must be between 1.0 and 2.2. Kindly check list inputs for completeness and correctness.')

                clientObject.support_width_z = support_in_z[7]

                if len(support_in_z) == 9:
                    clientObject.support_depth_by_section_width_of_member_z_enabled = False
                    clientObject.support_depth_z = support_in_z[8]

                elif len(support_in_z) == 8:
                    clientObject.support_depth_by_section_width_of_member_z_enabled = True

                else:
                    raise ValueError('WARNING!: The suport in Z parameter needs to be length of 8 or 9. Kindly check list inputs for completeness and correctness.')

        elif support_in_z == None or support_in_z == False:
            clientObject.activate_in_z = False

        else:
            raise TypeError("WARNING! First parameter of support in Z list must be type bool. Kindly check list inputs completeness and correctness.")

        # Support in Y
        if isinstance(support_in_y, list) and support_in_y[0] == True:
            clientObject.activate_in_y = support_in_y[0]
            clientObject.direct_support_y_enabled = support_in_y[1]
            clientObject.inner_support_y_enabled = support_in_y[2]
            clientObject.consider_in_deflection_design_y = support_in_y[3]
            clientObject.design_support_orientation_y = support_in_y[4].name

            if support_in_y[1] == True:
                clientObject.consider_in_fire_design_y = support_in_y[5]

                if (1.0 <= support_in_y[6] <= 2.20):
                    clientObject.timber_factor_of_compression_y = support_in_y[6]

                else:
                    raise ValueError('WARNING!: The timber factor of compression in Y parameter must be between 1.0 and 2.2. Kindly check list inputs for completeness and correctness.')

                clientObject.support_width_y = support_in_y[7]

                if len(support_in_y) == 9:
                    clientObject.support_depth_by_section_width_of_member_y_enabled = False
                    clientObject.support_depth_y = support_in_y[8]

                elif len(support_in_y) == 8:
                    clientObject.support_depth_by_section_width_of_member_y_enabled = True

                else:
                    raise ValueError('WARNING!: The suport in Y parameter needs to be length of 8 or 9. Kindly check list inputs for completeness and correctness.')

        elif support_in_y == None or support_in_y == False:
            clientObject.activate_in_y = False

        else:
            raise TypeError("WARNING! First parameter of support in Y list must be type bool. Kindly check list inputs completeness and correctness.")

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
