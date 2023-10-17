import enum
from RFEM.initModel import Model
from RFEM.enums import CaseObjectType
from RFEM.Results.resultTables import ConvertResultsToListOfDct

class AddOnResultTables():

    # # TODO
    # @staticmethod
    # def SteelDesignBraceConnectionByMemeber(
    #     type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION,
    #     no: int = 1,
    #     parent_no: int = 0,
    #     include_base: bool = False,
    #     model = Model):

    #     '''
    #      Args:
    #         type (enum): Load Combination (CO1 = E_OBJECT_TYPE_LOAD_COMBINATION)
    #         no (int): Member number
    #         parent_number (int): Number of parent
    #         model (class, optional): Model instance
    #     '''

    #     # <soap:Body>
    #     #     <n1:get_results_for_steel_design_brace_connection_by_memberResponse
    #     #         xmlns:n1="http://www.dlubal.com/rfem.xsd">
    #     #         <value/>
    #     #     </n1:get_results_for_steel_design_brace_connection_by_memberResponse>
    #     # </soap:Body>

    #     return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_steel_design_brace_connection_by_member(type.name, no, parent_no), include_base)

    # # TODO
    # @staticmethod
    # def SteelDesignBraceConncectionByMemberSet(
    #     type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION,
    #     no: int = 1,
    #     parent_no: int = 0,
    #     include_base: bool = False,
    #     model = Model):

    #     '''
    #      Args:
    #         type (enum): Load Combination (CO1 = E_OBJECT_TYPE_LOAD_COMBINATION)
    #         no (int): Member number
    #         parent_number (int): Number of parent
    #         model (class, optional): Model instance
    #     '''

    #     # <soap:Body>
    #     #     <n1:get_results_for_steel_design_brace_connection_by_memberResponse
    #     #         xmlns:n1="http://www.dlubal.com/rfem.xsd">
    #     #         <value/>
    #     #     </n1:get_results_for_steel_design_brace_connection_by_memberResponse>
    #     # </soap:Body>

    #     return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_steel_design_brace_connection_by_member_set(type.name, no, parent_no), include_base)
# get_results_for_steel_design_design_ratios_member_representatives_by_construction_stage()
# get_results_for_steel_design_design_ratios_member_representatives_by_design_situation()
# get_results_for_steel_design_design_ratios_member_representatives_by_loading()
# get_results_for_steel_design_design_ratios_member_representatives_by_location()
# get_results_for_steel_design_design_ratios_member_representatives_by_material()
# get_results_for_steel_design_design_ratios_member_representatives_by_member_representative()
# get_results_for_steel_design_design_ratios_member_representatives_by_section()
# get_results_for_steel_design_design_ratios_member_set_representatives_by_construction_stage()
# get_results_for_steel_design_design_ratios_member_set_representatives_by_design_situation()
# get_results_for_steel_design_design_ratios_member_set_representatives_by_loading()
# get_results_for_steel_design_design_ratios_member_set_representatives_by_location()
# get_results_for_steel_design_design_ratios_member_set_representatives_by_material()
# get_results_for_steel_design_design_ratios_member_set_representatives_by_member_set_representative()
# get_results_for_steel_design_design_ratios_member_set_representatives_by_section()
    # # TODO
    # @staticmethod
    # def SteelDesignDesignRatiosMembersByConstructionStage(
    #     type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION,
    #     no: int = 1,
    #     parent_no: int = 0,
    #     include_base: bool = False,
    #     model = Model):

    #     '''
    #      Args:
    #         type (enum): Load Combination (CO1 = E_OBJECT_TYPE_LOAD_COMBINATION)
    #         no (int): Member number
    #         parent_number (int): Number of parent
    #         model (class, optional): Model instance
    #     '''

    #     return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_steel_design_design_ratios_members_by_construction_stage(type.name, no, parent_no), include_base)


    @staticmethod
    def SteelDesignDesignRatiosMembersByDesignSituation(
        type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION,
        no: int = 1,
        parent_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            type (enum): Load Combination (CO1 = E_OBJECT_TYPE_LOAD_COMBINATION)
            no (int): Member number
            parent_number (int): Number of parent
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_steel_design_design_ratios_members_by_design_situation(type.name, no, parent_no), include_base)


    @staticmethod
    def SteelDesignDesignRatiosMembersByLoading(
        type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION,
        no: int = 1,
        parent_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            type (enum): Load Combination (CO1 = E_OBJECT_TYPE_LOAD_COMBINATION)
            no (int): Member number
            parent_number (int): Number of parent
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_steel_design_design_ratios_members_by_loading(type.name, no, parent_no), include_base)


    @staticmethod
    def SteelDesignDesignRatiosMembersByLocation(
        type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION,
        no: int = 1,
        parent_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            type (enum): Load Combination (CO1 = E_OBJECT_TYPE_LOAD_COMBINATION)
            no (int): Member number
            parent_number (int): Number of parent
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_steel_design_design_ratios_members_by_location(type.name, no, parent_no), include_base)


    @staticmethod
    def SteelDesignDesignRatiosMembersByMaterial(
        type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION,
        no: int = 1,
        parent_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            type (enum): Load Combination (CO1 = E_OBJECT_TYPE_LOAD_COMBINATION)
            no (int): Member number
            parent_number (int): Number of parent
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_steel_design_design_ratios_members_by_material(type.name, no, parent_no), include_base)


    @staticmethod
    def SteelDesignDesignRatiosMembersByMember(
        type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION,
        no: int = 1,
        parent_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            type (enum): Load Combination (CO1 = E_OBJECT_TYPE_LOAD_COMBINATION)
            no (int): Member number
            parent_number (int): Number of parent
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_steel_design_design_ratios_members_by_member(type.name, no, parent_no), include_base)

# get_results_for_steel_design_design_ratios_members_by_member_set()
# get_results_for_steel_design_design_ratios_members_by_section()
# get_results_for_steel_design_governing_internal_forces_by_member()
# get_results_for_steel_design_governing_internal_forces_by_member_ends()
# get_results_for_steel_design_governing_internal_forces_by_member_representative()
# get_results_for_steel_design_governing_internal_forces_by_member_representative_ends()
# get_results_for_steel_design_governing_internal_forces_by_member_set()
# get_results_for_steel_design_governing_internal_forces_by_member_set_ends()
# get_results_for_steel_design_governing_internal_forces_by_member_set_representative()
# get_results_for_steel_design_governing_internal_forces_by_member_set_representative_ends()
# get_results_for_steel_design_governing_loading()
# get_results_for_steel_design_moment_frame_connection_by_member()
# get_results_for_steel_design_moment_frame_connection_by_member_set()
# get_results_for_steel_design_overview_errors_and_warnings()
# get_results_for_steel_design_overview_not_valid_deactivated()
# get_results_for_steel_design_slenderness_by_member()
# get_results_for_steel_design_slenderness_by_member_representative()
# get_results_for_steel_design_slenderness_by_member_set()
# get_results_for_steel_design_slenderness_by_member_set_representative()
# get_results_for_steel_design_stability_bracing_by_member()
# get_results_for_steel_design_stability_bracing_by_member_set()