from RFEM.BasicObjects.member import Member
from RFEM.initModel import Model
from RFEM.enums import ModelCheckGetOptionType, ModelCheckProcessOptionType

class ModelCheck():

    @staticmethod
    def GetIdenticalNodes(tolerance, model = Model):
        """
        Args:
            tolerance (float): Tolerance
        Returns:
            Identical Nodes Object Group
        """

        operation = ModelCheckGetOptionType.IDENTICAL_NODES.name
        object_groups = model.clientModel.service.model_check__get_object_groups_operation(operation, tolerance)

        return object_groups

    @staticmethod
    def DeleteUnusedNodes(tolerance, object_groups, model = Model):
        """
        Args:
            tolerance (float): Tolerance
            object_groups (dict): Object Groups of Identical Nodes
        """

        process = ModelCheckProcessOptionType.DELETE_UNUSED_NODES.name
        model.clientModel.service.model_check__process_object_groups_operation(process, tolerance, object_groups)

    @staticmethod
    def UniteNodes(tolerance, object_groups, model = Model):
        """
        Args:
            tolerance (float): Tolerance
            object_groups (dict): Object Groups of Identical Nodes
        """

        process = ModelCheckProcessOptionType.UNITE_NODES_AND_DELETE_UNUSED_NODES.name
        model.clientModel.service.model_check__process_object_groups_operation(process, tolerance, object_groups)

    @staticmethod
    def GetNotConnectedLines(tolerance, model = Model):
        """
        Args:
            tolerance (float): Tolerance
        Returns:
            Not Connected Lines Line Groups
        """

        operation = ModelCheckGetOptionType.CROSSING_LINES.name
        line_groups = model.clientModel.service.model_check__get_object_groups_operation(operation, tolerance)

        return line_groups

    @staticmethod
    def CrossLines(tolerance, line_groups, model = Model):
        """
        Args:
            tolerance (float): Tolerance
            line_groups (dict): Line Groups of Not Connected Lines
        """

        process = ModelCheckProcessOptionType.CROSS_LINES.name
        model.clientModel.service.model_check__process_object_groups_operation(process, tolerance, line_groups)

    @staticmethod
    def GetNotConnectedMembers(tolerance, model = Model):
        """
        Args:
            tolerance (float): Tolerance
        Returns:
            Not Connected Members Member Groups
        """

        operation = ModelCheckGetOptionType.CROSSING_MEMBERS.name
        member_groups = model.clientModel.service.model_check__get_object_groups_operation(operation, tolerance)

        return member_groups

    @staticmethod
    def CrossMembers(tolerance, member_groups, model = Model):
        """
        Args:
            tolerance (float): Tolerance
            member_groups (dict): Member Groups of Not Connected Members
        """

        process = ModelCheckProcessOptionType.CROSS_MEMBERS.name
        model.clientModel.service.model_check__process_object_groups_operation(process, tolerance, member_groups)

    @staticmethod
    def GetOverlappingLines(model = Model):
        """
        Returns:
            Overlapping Line Groups
        """

        operation = ModelCheckGetOptionType.OVERLAPPING_LINES.name
        overlapping_lines = model.clientModel.service.model_check__get_object_groups_operation(operation)

        return overlapping_lines

    @staticmethod
    def GetOverlappingMembers(model = Model):
        """
        Returns:
            Overlapping Member Groups
        """

        operation = ModelCheckGetOptionType.OVERLAPPING_MEMBERS.name
        overlapping_members = model.clientModel.service.model_check__get_object_groups_operation(operation)

        return overlapping_members
