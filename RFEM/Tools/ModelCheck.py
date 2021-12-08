#pylint: disable=W0614, W0401, W0622, C0103, C0114, C0115, C0116, C0301, C0413, R0913, R0914, R0915, C0305, C0411, W0102, W0702, E0602, E0401
from RFEM.initModel import *
from RFEM.enums import *

class ModelCheck():

    def __init__(self):
        pass

    def GetIdenticalNodes(self, tolerance):
        """
        Args:
            tolerance (float): Tolerance
        Returns:
            Identical Nodes Object Group
        """

        operation = ModelCheckGetOptionType.IDENTICAL_NODES.name
        object_groups = clientModel.service.model_check__get_object_groups_operation(operation, tolerance)

        return object_groups

    def DeleteUnusedNodes(self, tolerance, object_groups):
        """
        Args:
            tolerance (float): Tolerance
            object_groups (dict): Object Groups of Identical Nodes
        """

        process = ModelCheckProcessOptionType.DELETE_UNUSED_NODES.name
        clientModel.service.model_check__process_object_groups_operation(process, tolerance, object_groups)

    def UniteNodes(self, tolerance, object_groups):
        """
        Args:
            tolerance (float): Tolerance
            object_groups (dict): Object Groups of Identical Nodes
        """

        process = ModelCheckProcessOptionType.UNITE_NODES_AND_DELETE_UNUSED_NODES.name
        clientModel.service.model_check__process_object_groups_operation(process, tolerance, object_groups)

    def GetNotConnectedLines(self, tolerance):
        """
        Args:
            tolerance (float): Tolerance
        Returns:
            Not Connected Lines Line Groups
        """

        operation = ModelCheckGetOptionType.CROSSING_LINES.name
        line_groups = clientModel.service.model_check__get_object_groups_operation(operation, tolerance)

        return line_groups

    def CrossLines(self, tolerance, line_groups):
        """
        Args:
            tolerance (float): Tolerance
            line_groups (dict): Line Groups of Not Connected Lines
        """

        process = ModelCheckProcessOptionType.CROSS_LINES.name
        clientModel.service.model_check__process_object_groups_operation(process, tolerance, line_groups)

    def GetNotConnectedMembers(self, tolerance):
        """
        Args:
            tolerance (float): Tolerance
        Returns:
            Not Connected Members Member Groups
        """

        operation = ModelCheckGetOptionType.CROSSING_MEMBERS.name
        member_groups = clientModel.service.model_check__get_object_groups_operation(operation, tolerance)

        return member_groups

    def CrossMembers(self, tolerance, member_groups):
        """
        Args:
            tolerance (float): Tolerance
            member_groups (dict): Member Groups of Not Connected Members
        """

        process = ModelCheckProcessOptionType.CROSS_MEMBERS.name
        clientModel.service.model_check__process_object_groups_operation(process, tolerance, member_groups)

    def GetOverlappingLines(self):
        """
        Returns:
            Overlapping Line Groups
        """

        operation = ModelCheckGetOptionType.OVERLAPPING_LINES.name
        overlapping_lines = clientModel.service.model_check__get_object_groups_operation(operation)

        return overlapping_lines

    def GetOverlappingMembers(self):
        """
        Returns:
            Overlapping Member Groups
        """

        operation = ModelCheckGetOptionType.OVERLAPPING_MEMBERS.name
        overlapping_members = clientModel.service.model_check__get_object_groups_operation(operation)

        return overlapping_members
