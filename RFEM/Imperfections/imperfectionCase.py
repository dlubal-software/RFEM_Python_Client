from pydoc import cli
from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import ImperfectionType, ImperfectionCaseDirection, DirectionForLevelDirection
from RFEM.enums import ImperfectionCaseSourceType, ImperfectionCaseAssignmentType

class ImperfectionCase():

    level_imperfection_item: dict = {'no':1,'level':3,'e_1':0,'theta_1':0,'e_2':0,'theta_2':0,'comment':''}
    imperfection_case_item: dict = {'no':1,'name':1, 'factor':1.1,'operator_type': 'OPERATOR_NONE','comment':''}

    def __init__(self,
                 no: int = 1,
                 type = ImperfectionType.IMPERFECTION_TYPE_LOCAL_IMPERFECTIONS,
                 assigned_to_load_cases: str = '',
                 assigned_to_load_combinations: str = '',
                 assign_to_combinations_without_assigned_imperfection_case: bool = True,
                 active: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Imperfection Case

        Args:
            no (int): Imperfection Case Tag
            type (enum): Imperfection Type
            assigned_to_load_cases (str, optional): Assigned to Load Case
            assigned_to_load_combinations (str, optional): Assigned to Load Combinations
            assign_to_combinations_without_assigned_imperfection_case (bool): Assign to all Load Combinations without Assigned Imperfection Case
            active (bool): Active
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Imperfection Case
        clientObject = model.clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Type of imperfection
        clientObject.type = type.name

        # Assign to Load Combinations
        if assigned_to_load_combinations:
            clientObject.assigned_to_load_combinations = ConvertToDlString(assigned_to_load_combinations)

        # Assign to Load Cases
        if assigned_to_load_cases:
            clientObject.assigned_to_load_cases = ConvertToDlString(assigned_to_load_cases)

        # Assign to Combinations Without Assigned Imperfection Case
        clientObject.assign_to_combinations_without_assigned_imperfection_case = assign_to_combinations_without_assigned_imperfection_case

        # Active
        clientObject.is_active = active

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Imperfection Case to client model
        model.clientModel.service.set_imperfection_case(clientObject)

    @staticmethod
    def Local(
              no: int = 1,
              assigned_to_load_combinations: str = '',
              assigned_to_load_cases: str = '',
              comment: str = '',
              params: dict = None,
              model = Model):
        """
        Imperfection Case Local Imperfections

        Args:
            no (int): Imperfection Case Tag
            assigned_to_load_combinations (str, optional): Assigned Load Combinations
            assigned_to_load_cases (str, optional): Assigned Load Cases
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # assigned_to_load_combinations XY is first in parameter list because imperfections are
        # usually assigned to load combinations.

        # Client model | Imperfection Case
        clientObject = model.clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Local Type
        clientObject.type = ImperfectionType.IMPERFECTION_TYPE_LOCAL_IMPERFECTIONS.name

        # Assign to Load Combinations
        if assigned_to_load_combinations:
            clientObject.assigned_to_load_combinations = ConvertToDlString(assigned_to_load_combinations)

        # Assign to Load Cases
        if assigned_to_load_cases:
            clientObject.assigned_to_load_cases = ConvertToDlString(assigned_to_load_cases)

        if len(assigned_to_load_cases) + len(assigned_to_load_combinations) == 0:
            print('Warning: An imperfection case should be assigned to a load case or load combination.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Imperfection Case to client model
        model.clientModel.service.set_imperfection_case(clientObject)

    @staticmethod
    def InitialSwayViaTable(
                            no: int = 1,
                            assigned_to_load_cases: str = '',
                            assigned_to_load_combinations: str = '',
                            assign_to_combinations_without_assigned_imperfection_case: bool = True,
                            direction = ImperfectionCaseDirection.IMPERFECTION_CASE_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
                            direction_for_level_direction = DirectionForLevelDirection.DIRECTION_X,
                            coordinate_system: int = 1,
                            sway_coefficients_reciprocal: bool = True,
                            level_imperfections: list = [level_imperfection_item],
                            active: bool = True,
                            comment: str = '',
                            params: dict = None,
                            model = Model):
        """
        Imperfection Case Initial Sway via Table

        Args:
            no (int): Imperfection Case Tag
            assigned_to_load_cases (str, optional): Assigned to Load Case
            assigned_to_load_combinations (str, optional): Assigned to Load Combinations
            assign_to_combinations_without_assigned_imperfection_case (bool): Assign to all Load Combinations without assigned Imperfection Case
            direction (enum): Imperfection Case Direction Enumeration
            direction_for_level_direction (enum): Direction For Level Direction Enumeration
            coordinate_system (int): Coordinate system
            sway_coefficients_reciprocal (bool): Sway Coefficient as reciprocal of 1
            level_imperfections (list): Level Imperfections
            active (bool): Active
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Imperfection Case
        clientObject = model.clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Type of imperfection
        clientObject.type = ImperfectionType.IMPERFECTION_TYPE_INITIAL_SWAY_VIA_TABLE.name

        # Assign to Load Combinations
        if assigned_to_load_combinations:
            clientObject.assigned_to_load_combinations = ConvertToDlString(assigned_to_load_combinations)

        # Assign to Load Cases
        if assigned_to_load_cases:
            clientObject.assigned_to_load_cases = ConvertToDlString(assigned_to_load_cases)

        # Assign to Combinations Without Assigned Imperfection Case
        clientObject.assign_to_combinations_without_assigned_imperfection_case = assign_to_combinations_without_assigned_imperfection_case

        # Level Direction
        clientObject.direction = direction.name

        # Imperfection Direction
        clientObject.direction_for_level_direction = direction_for_level_direction.name

        # Coordinate System
        clientObject.coordinate_system = coordinate_system

        # Sway Coeefficient as Reciprocal of 1
        clientObject.sway_coefficients_reciprocal = sway_coefficients_reciprocal

        # Level Imperfections Table
        clientObject.level_imperfections = model.clientModel.factory.create('ns0:array_of_imperfection_case_level_imperfections')

        for i in level_imperfections:
            li_proto = model.clientModel.factory.create('ns0:imperfection_case_level_imperfections_row')
            li_proto.no = i['no']
            li_proto.row.level = i['level']
            li_proto.row.e_1 = i['e_1']
            li_proto.row.theta_1 = i['theta_1']
            li_proto.row.e_2 = i['e_2']
            li_proto.row.theta_2 = i['theta_2']
            li_proto.row.comment = i['comment']

            clientObject.level_imperfections.imperfection_case_level_imperfections.append(li_proto)

        # Active
        clientObject.is_active = active

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Imperfection Case to client model
        model.clientModel.service.set_imperfection_case(clientObject)

    @staticmethod
    def NotionalLoads(
                 no: int = 1,
                 assigned_to_load_cases: str = '',
                 assigned_to_load_combinations: str = '',
                 assign_to_combinations_without_assigned_imperfection_case: bool = True,
                 load_case_for_notional_loads: int = 1,
                 active: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Imperfection Case

        Args:
            no (int): Imperfection Case Tag
            assigned_to_load_cases (str, optional): Assigned to Load Case
            assigned_to_load_combinations (str, optional): Assigned to Load Combinations
            assign_to_combinations_without_assigned_imperfection_case (bool): Assign to all Load Combinations without assigned Imperfection Case
            load_case_for_notional_loads(int): Load Case for Notional Loads
            active (bool): Active
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Imperfection Case
        clientObject = model.clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Type of imperfection
        clientObject.type = ImperfectionType.IMPERFECTION_TYPE_NOTIONAL_LOADS_FROM_LOAD_CASE.name

        # Assign to Load Combinations
        if assigned_to_load_combinations:
            clientObject.assigned_to_load_combinations = ConvertToDlString(assigned_to_load_combinations)

        # Assign to Load Cases
        if assigned_to_load_cases:
            clientObject.assigned_to_load_cases = ConvertToDlString(assigned_to_load_cases)

        # Assign to Combinations Without Assigned Imperfection Case
        clientObject.assign_to_combinations_without_assigned_imperfection_case = assign_to_combinations_without_assigned_imperfection_case

        # Load Case for Notional Loads
        clientObject.load_case_for_notional_loads = load_case_for_notional_loads

        # Active
        clientObject.is_active = active

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Imperfection Case to client model
        model.clientModel.service.set_imperfection_case(clientObject)

    @staticmethod
    def StaticDeformation(
                 no: int = 1,
                 assigned_to_load_cases: str = '',
                 assigned_to_load_combinations: str = '',
                 assign_to_combinations_without_assigned_imperfection_case: bool = True,
                 direction = ImperfectionCaseDirection.IMPERFECTION_CASE_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
                 coordinate_system: int = 1,
                 source = ImperfectionCaseSourceType.SOURCE_TYPE_LOAD_CASE,
                 imperfection_shape_from: int = 1,
                 imperfection_magnitude: float = 0.3,
                 magnitude_assignment_type = ImperfectionCaseAssignmentType.MAGNITUDE_ASSIGNMENT_SPECIFIC_NODE,
                 reference_node: int = None,
                 active: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Static Deformation Type

        Args:
            no (int): Imperfection Case Tag
            assigned_to_load_cases (str, optional): Assigned to Load Case
            assigned_to_load_combinations (str, optional): Assigned to Load Combinations
            assign_to_combinations_without_assigned_imperfection_case (bool): Assign to all Load Combinations without assigned Imperfection Case
            direction (enum): Imperfection Case Direction Enumeration
            coordinate_system (int): Coordinate System
            source (enum): Imperfection Case Source Type Enumeration
            imperfection_shape_from (int): Imperfection Shape From
            imperfection_magnitude (float): Imperfection Magnitude
            magnitude_assignment_type (enum): Imperfection Case Assignment Type Enumeration
            reference_node (int): Reference Node
            active (bool): Active
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Imperfection Case
        clientObject = model.clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Type of imperfection
        clientObject.type = ImperfectionType.IMPERFECTION_TYPE_STATIC_DEFORMATION.name

        # Assign to Load Combinations
        if assigned_to_load_combinations:
            clientObject.assigned_to_load_combinations = ConvertToDlString(assigned_to_load_combinations)

        # Assign to Load Cases
        if assigned_to_load_cases:
            clientObject.assigned_to_load_cases = ConvertToDlString(assigned_to_load_cases)

        # Assign to Combinations Without Assigned Imperfection Case
        clientObject.assign_to_combinations_without_assigned_imperfection_case = assign_to_combinations_without_assigned_imperfection_case

        # Direction
        clientObject.direction = direction.name

        # Coordinate System number
        clientObject.coordinate_system = coordinate_system

        # Source
        clientObject.source = source.name

        # Shape from Load Case/Combination
        if source == ImperfectionCaseSourceType.SOURCE_TYPE_LOAD_CASE:
            clientObject.shape_from_load_case = imperfection_shape_from
        else:
            clientObject.shape_from_load_combination = imperfection_shape_from

        # Imperfection Magnuítude
        clientObject.delta_zero = imperfection_magnitude

        # Reference Location
        clientObject.magnitude_assignment_type = magnitude_assignment_type.name

        # Reference Node
        if magnitude_assignment_type == ImperfectionCaseAssignmentType.MAGNITUDE_ASSIGNMENT_SPECIFIC_NODE:
            clientObject.reference_node = reference_node

        # Active
        clientObject.is_active = active

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Imperfection Case to client model
        model.clientModel.service.set_imperfection_case(clientObject)

    @staticmethod
    def Group(
                 no: int = 1,
                 assigned_to_load_cases: str = '',
                 assigned_to_load_combinations: str = '',
                 assign_to_combinations_without_assigned_imperfection_case: bool = True,
                 imperfection_cases: list = [imperfection_case_item],
                 active: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Imperfection Case

        Args:
            no (int): Imperfection Case Tag
            assigned_to_load_cases (str, optional): Assigned to Load Case
            assigned_to_load_combinations (str, optional): Assigned to Load Combinations
            assign_to_combinations_without_assigned_imperfection_case (bool): Assign to all Load Combinations without assigned Imperfection Case
            imperfection_cases (list): Imperfection Cases items
            active (bool): Active
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Imperfection Case
        clientObject = model.clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Type
        clientObject.type = ImperfectionType.IMPERFECTION_TYPE_IMPERFECTION_CASES_GROUP.name

        # Assign to Load Combinations
        if assigned_to_load_combinations:
            clientObject.assigned_to_load_combinations = ConvertToDlString(assigned_to_load_combinations)

        # Assign to Load Cases
        if assigned_to_load_cases:
            clientObject.assigned_to_load_cases = ConvertToDlString(assigned_to_load_cases)

        # Assign to Combinations Without Assigned Imperfection Case
        clientObject.assign_to_combinations_without_assigned_imperfection_case = assign_to_combinations_without_assigned_imperfection_case

        # Imperfection Case Items
        clientObject.imperfection_cases_items = model.clientModel.factory.create('ns0:array_of_imperfection_case_imperfection_cases_items')

        for i in imperfection_cases:
            li_proto = model.clientModel.factory.create('ns0:imperfection_case_imperfection_cases_items_row')
            li_proto.no = i['no']
            li_proto.row.name = i['name']
            li_proto.row.factor = i['factor']
            li_proto.row.operator_type = i['operator_type']
            li_proto.row.comment = i['comment']

            clientObject.imperfection_cases_items.imperfection_case_imperfection_cases_items.append(li_proto)

        # Active
        clientObject.is_active = active

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Imperfection Case to client model
        model.clientModel.service.set_imperfection_case(clientObject)
