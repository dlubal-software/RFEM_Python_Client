import enum
from RFEM.initModel import Model
from RFEM.enums import CaseObjectType
from RFEM.dataTypes import inf

# We  can't extract lines with description: Extremes, Total, and Average. Those are language dependent.
# To do it set_settings_program_language() has to be called before calculation and the program needs to be restarted.

def GetResultTableParameters(results):
    '''
    Returns dict with 3 atributes: base, row and error.
    '''
    params = {'base':[], 'row':[], 'error': None}

    if not results:
        return ''

    if results[0][0]:
        for i in results[0]:
            params['base'] = list(set(params['base'] + i.__keylist__))
            if 'row' in i.__keylist__ and i.row:
                params['row'] = list(set(params['row'] + i.row.__keylist__))
            else:
                params['errors'] = "Result table doesn't have attribute 'row'."

    return params

def ConvertResultsToListOfDct(results, includeBase = False):
    '''
    Args:
        results (ResultTables class): ResultTables object
        includeBase (bool): Include base information of every line. Typicaly 'object number' and 'description'. Default is False.
    Returns:
        List of dictionaries. Each dictionary corresponds to one line in result table.
    '''
    if not results:
        return ''

    params = GetResultTableParameters(results)
    lstOfDct = []

    for r in results[0]:
        dct = {}
        if includeBase and params['base']:
            for i in params['base']:
                if i == 'row':
                    for y in params['row']:
                        # Sometimes the parameters are not in table or
                        # they are defined by type+value structure called 'variant',
                        # hence using try-except notation
                        try:
                            dct[y] = float(r.row[y].value)
                        except:
                            try:
                                dct[y] = r.row[y].value
                            except:
                                try:
                                    dct[y] = float(r.row[y])
                                except:
                                    try:
                                        dct[y] = r.row[y]
                                    except:
                                        pass
                else:
                    try:
                        dct[i] = float(r[i])
                    except:
                        try:
                            dct[i] = r[i]
                        except:
                            pass
            lstOfDct.append(dct)
        # include only row
        else:
            if params['row']:
                for i in params['row']:
                    try:
                        dct[i] = float(r.row[i].value)
                    except:
                        try:
                            dct[i] = r.row[i].value
                        except:
                            try:
                                dct[i] = float(r.row[i])
                            except:
                                try:
                                    dct[i] = r.row[i]
                                except:
                                    pass
                lstOfDct.append(dct)

    if params['error']:
        return lstOfDct.append({'error': params['error']})

    return lstOfDct

def GetMinValue(structured_results, parameter):

    '''
    Args:
        structured_results(list of dicts): Result of ConvertResultsToListOfDct() function
        parameter(str, mandatory): The parameter for which the minimum is sought.
    '''

    min_val = inf
    for i in structured_results:
        # Sometimes there is text where the float should be
        try:
            min_val = min(float(i[parameter]), min_val)
        except:
            pass

    assert min_val < inf, 'Check if the parameter is in the table.'

    return min_val

def GetMaxValue(structured_results, parameter):

    '''
    Args:
        structured_results(list of dicts): Result of ConvertResultsToListOfDct() function
        parameter(str, mandatory): The parameter for which the maximum is sought.
    '''

    max_val = -inf
    for i in structured_results:
        # Sometimes there is text where the float should be
        try:
            max_val = max(float(i[parameter]), max_val)
        except:
            pass

    assert max_val > -inf, 'Check if the parameter is in the table.'

    return max_val

class ResultTables():

    @staticmethod
    def BuildingStoriesForcesInSpandrels(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_building_stories_forces_in_spandrels(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def BuildingStoriesForcesInShearWalls(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_building_stories_forces_in_shear_walls(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def BuildingStoriesCentresMassRigidity(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_building_stories_centres_mass_rigidity(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def BuildingStoriesInterstoryDrifts(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_building_stories_interstory_drifts(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def BuildingStoriesStoryActions(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_building_stories_story_actions(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def CalculationDiagrams(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_calculation_diagrams(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def CriticalLoadFactors(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_critical_load_factors(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def EfeectiveLengthsAndCriticalLoadsByEigenvector(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_efeective_lengths_and_critical_loads_by_eigenvector(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def EfeectiveLengthsAndCriticalLoadsByMember(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_efeective_lengths_and_critical_loads_by_member(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def EigenvectorsByMember(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_eigenvectors_by_member(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def EigenvectorsByNode(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_eigenvectors_by_node(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def EigenvectorsBySolid(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_eigenvectors_by_solid(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def EigenvectorsBySurface(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_eigenvectors_by_surface(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def Errors(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_errors(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def LineHingesDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_line_hinges_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def LineHingesForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_line_hinges_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def LinesSlabWallConnections(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_lines_slab_wall_connections(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def LinesSupportForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_lines_support_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersByEigenvector(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_by_eigenvector(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersContactForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_contact_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersGlobalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_global_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersHingeDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_hinge_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersHingeForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_hinge_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersInternalForcesByMemberSet(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_internal_forces_by_member_set(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersInternalForcesBySection(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_internal_forces_by_section(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersLocalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_local_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def MembersStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_members_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisEffectiveModalMasses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_effective_modal_masses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisMassesInLocations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_masses_in_locations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisMembersByModeShape(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_members_by_mode_shape(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisModeShapesByMember(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_mode_shapes_by_member(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisModeShapesByNode(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_mode_shapes_by_node(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisModeShapesBySolid(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_mode_shapes_by_solid(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisModeShapesBySurface(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_mode_shapes_by_surface(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisNaturalFrequencies(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_natural_frequencies(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisNodesByModeShape(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_nodes_by_mode_shape(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisParticipationFactors(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_participation_factors(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisSolidsByModeShape(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_solids_by_mode_shape(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def ModalAnalysisSurfacesByModeShape(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_modal_analysis_surfaces_by_mode_shape(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def NodesByEigenvector(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_nodes_by_eigenvector(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def NodesDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_nodes_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def NodesSupportForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_nodes_support_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsBasicPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_basic_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsBasicStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_basic_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsBasicTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_basic_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsByEigenvector(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_by_eigenvector(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsEquivalentPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_equivalent_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsEquivalentStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_equivalent_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsEquivalentTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_equivalent_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsGasQuantities(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_gas_quantities(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsPrincipalPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_principal_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsPrincipalStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_principal_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SolidsPrincipalTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_solids_principal_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisBuildingStoriesCentresMassRigidity(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_building_stories_centres_mass_rigidity(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisBuildingStoriesForcesInShearWalls(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_building_stories_forces_in_shear_walls(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisBuildingStoriesForcesInSpandrels(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_building_stories_forces_in_spandrels(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisBuildingStoriesInterstoryDrifts(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_building_stories_interstory_drifts(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisBuildingStoriesStoryActions(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_building_stories_story_actions(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisLineHingesDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_line_hinges_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisLineHingesForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_line_hinges_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisLinesSlabWallConnections(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_lines_slab_wall_connections(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisLinesSupportForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_lines_support_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisMembersContactForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_members_contact_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisMembersGlobalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_members_global_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisMembersHingeDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_members_hinge_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisMembersHingeForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_members_hinge_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisMembersInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_members_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisMembersInternalForcesByMemberSet(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_members_internal_forces_by_member_set(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisMembersInternalForcesBySection(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_members_internal_forces_by_section(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisMembersLocalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_members_local_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisMembersStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_members_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisNodesDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_nodes_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisNodesPseudoAccelerations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_nodes_pseudo_accelerations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisNodesPseudoVelocities(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_nodes_pseudo_velocities(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisNodesSupportForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_nodes_support_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSolidsBasicStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_solids_basic_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSolidsBasicTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_solids_basic_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSolidsDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_solids_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSolidsEquivalentStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_solids_equivalent_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSolidsEquivalentTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_solids_equivalent_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSolidsGasQuantities(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_solids_gas_quantities(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSolidsPrincipalStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_solids_principal_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSolidsPrincipalTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_solids_principal_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSummary(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_summary(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesBasicInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_basic_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesBasicStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_basic_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesBasicTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_basic_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesContactStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_contact_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesDesignInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_design_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesElasticStressComponents(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_elastic_stress_components(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesEquivalentStressesBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_equivalent_stresses_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesEquivalentStressesMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_equivalent_stresses_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesEquivalentStressesRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_equivalent_stresses_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesEquivalentStressesTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_equivalent_stresses_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesEquivalentTotalStrainsBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_equivalent_total_strains_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesEquivalentTotalStrainsMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_equivalent_total_strains_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesEquivalentTotalStrainsRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_equivalent_total_strains_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesEquivalentTotalStrainsTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_equivalent_total_strains_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesGlobalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_global_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesLocalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_local_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesMaximumTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_maximum_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesPrincipalInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_principal_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesPrincipalStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_principal_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SpectralAnalysisSurfacesPrincipalTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_spectral_analysis_surfaces_principal_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisBuildingStoriesCentresMassRigidity(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_building_stories_centres_mass_rigidity(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisBuildingStoriesForcesInShearWalls(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_building_stories_forces_in_shear_walls(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisBuildingStoriesForcesInSpandrels(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_building_stories_forces_in_spandrels(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisBuildingStoriesInterstoryDrifts(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_building_stories_interstory_drifts(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisBuildingStoriesStoryActions(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_building_stories_story_actions(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisCalculationDiagrams(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_calculation_diagrams(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisLineHingesDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_line_hinges_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisLineHingesForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_line_hinges_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisLinesSlabWallConnections(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_lines_slab_wall_connections(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisLinesSupportForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_lines_support_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisMembersContactForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_members_contact_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisMembersGlobalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_members_global_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisMembersHingeDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_members_hinge_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisMembersHingeForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_members_hinge_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisMembersInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_members_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisMembersInternalForcesByMemberSet(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_members_internal_forces_by_member_set(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisMembersInternalForcesBySection(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_members_internal_forces_by_section(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisMembersLocalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_members_local_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisMembersStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_members_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisNodesDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_nodes_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisNodesSupportForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_nodes_support_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsBasicPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_basic_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsBasicStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_basic_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsBasicTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_basic_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsEquivalentPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_equivalent_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsEquivalentStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_equivalent_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsEquivalentTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_equivalent_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsGasQuantities(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_gas_quantities(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsPrincipalPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_principal_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsPrincipalStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_principal_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSolidsPrincipalTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_solids_principal_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSummary(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_summary(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesBasicInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_basic_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesBasicPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_basic_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesBasicStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_basic_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesBasicTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_basic_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesContactStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_contact_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesDesignInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_design_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesElasticStressComponents(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_elastic_stress_components(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentPlasticStrainsBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_plastic_strains_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentPlasticStrainsMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_plastic_strains_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentPlasticStrainsRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_plastic_strains_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentPlasticStrainsTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_plastic_strains_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentStressesBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_stresses_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentStressesMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_stresses_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentStressesRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_stresses_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentStressesTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_stresses_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentTotalStrainsBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_total_strains_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentTotalStrainsMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_total_strains_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentTotalStrainsRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_total_strains_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesEquivalentTotalStrainsTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_equivalent_total_strains_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesGlobalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_global_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesLocalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_local_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesMaximumPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_maximum_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesMaximumTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_maximum_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesPrincipalInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_principal_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesPrincipalPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_principal_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesPrincipalStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_principal_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def StabilityIncrementalAnalysisSurfacesPrincipalTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_stability_incremental_analysis_surfaces_principal_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def Summary(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_summary(loading_type.name, loading_no))

    @staticmethod
    def SurfacesBasicInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_basic_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesBasicPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_basic_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesBasicStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_basic_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesBasicTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_basic_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesByEigenvector(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_by_eigenvector(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesContactStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_contact_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesDesignInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_design_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesElasticStressComponents(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_elastic_stress_components(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentPlasticStrainsBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_plastic_strains_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentPlasticStrainsMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_plastic_strains_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentPlasticStrainsRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_plastic_strains_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentPlasticStrainsTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_plastic_strains_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentStressesBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_stresses_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentStressesMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_stresses_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentStressesRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_stresses_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentStressesTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_stresses_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentTotalStrainsBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_total_strains_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentTotalStrainsMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_total_strains_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentTotalStrainsRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_total_strains_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesEquivalentTotalStrainsTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_equivalent_total_strains_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesGlobalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_global_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesLocalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_local_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesMaximumPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_maximum_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesMaximumTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_maximum_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesPrincipalInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_principal_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesPrincipalPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_principal_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesPrincipalStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_principal_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def SurfacesPrincipalTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_surfaces_principal_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisBuildingStoriesCentresMassRigidity(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_building_stories_centres_mass_rigidity(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisBuildingStoriesForcesInShearWalls(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_building_stories_forces_in_shear_walls(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisBuildingStoriesForcesInSpandrels(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_building_stories_forces_in_spandrels(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisBuildingStoriesInterstoryDrifts(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_building_stories_interstory_drifts(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisBuildingStoriesStoryActions(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_building_stories_story_actions(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisLineHingesDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_line_hinges_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisLineHingesForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_line_hinges_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisLinesSlabWallConnections(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_lines_slab_wall_connections(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisLinesSupportForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_lines_support_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisMembersContactForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_members_contact_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisMembersGlobalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_members_global_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisMembersHingeDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_members_hinge_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisMembersHingeForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_members_hinge_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisMembersInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_members_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisMembersInternalForcesByMemberSet(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_members_internal_forces_by_member_set(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisMembersInternalForcesBySection(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_members_internal_forces_by_section(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisMembersLocalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_members_local_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisMembersStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_members_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisNodesAccelerations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_nodes_accelerations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisNodesDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_nodes_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisNodesSupportForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_nodes_support_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisNodesVelocities(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_nodes_velocities(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsBasicPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_basic_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsBasicStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_basic_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsBasicTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_basic_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsEquivalentPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_equivalent_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsEquivalentStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_equivalent_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsEquivalentTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_equivalent_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsGasQuantities(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_gas_quantities(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsPrincipalPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_principal_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsPrincipalStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_principal_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSolidsPrincipalTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_solids_principal_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSummary(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_summary(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesBasicInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_basic_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesBasicPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_basic_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesBasicStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_basic_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesBasicTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_basic_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesContactStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_contact_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesDesignInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_design_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesElasticStressComponents(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_elastic_stress_components(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentPlasticStrainsBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_plastic_strains_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentPlasticStrainsMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_plastic_strains_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentPlasticStrainsRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_plastic_strains_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentPlasticStrainsTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_plastic_strains_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentStressesBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_stresses_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentStressesMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_stresses_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentStressesRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_stresses_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentStressesTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_stresses_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentTotalStrainsBach(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_total_strains_bach(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentTotalStrainsMises(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_total_strains_mises(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentTotalStrainsRankine(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_total_strains_rankine(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesEquivalentTotalStrainsTresca(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_equivalent_total_strains_tresca(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesGlobalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_global_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesLocalDeformations(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_local_deformations(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesMaximumPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_maximum_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesMaximumTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_maximum_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesPrincipalInternalForces(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_principal_internal_forces(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesPrincipalPlasticStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_principal_plastic_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesPrincipalStresses(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_principal_stresses(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def TimeHistoryAnalysisSurfacesPrincipalTotalStrains(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        object_no: int = 0,
        include_base: bool = False,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            object_no (int): Object number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_time_history_analysis_surfaces_principal_total_strains(loading_type.name, loading_no, object_no), include_base)

    @staticmethod
    def HasAnyResults( model = Model):

        '''
         Args:
            model (class, optional): Model instance
        '''

        return model.clientModel.service.has_any_results()

    @staticmethod
    def HasResults(
        loading_type: enum = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 0,
        model = Model):

        '''
         Args:
            loading_type (emun): Loading type (LC2 = E_OBJECT_TYPE_LOAD_CASE)
            loading_no (int): Loading Number (CO2 = 2)
            model (class, optional): Model instance
        '''

        return model.clientModel.service.has_results(loading_type.name, loading_no)

    @staticmethod
    def AluminumDesignDesignRatiosMemberRepresentativesByConstructionStage(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_representatives_by_construction_stage(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberRepresentativesByDesignSituation(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_representatives_by_design_situation(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberRepresentativesByLoading(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_representatives_by_loading(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberRepresentativesByLocation(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_representatives_by_location(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberRepresentativesByMaterial(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_representatives_by_material(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberRepresentativesByMemberRepresentative(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_representatives_by_member_representative(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberRepresentativesBySection(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_representatives_by_section(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberSetRepresentativesByConstructionStage(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_set_representatives_by_construction_stage(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberSetRepresentativesByDesignSituation(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_set_representatives_by_design_situation(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberSetRepresentativesByLoading(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_set_representatives_by_loading(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberSetRepresentativesByLocation(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_set_representatives_by_location(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberSetRepresentativesByMaterial(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_set_representatives_by_material(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberSetRepresentativesByMemberSetRepresentative(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_set_representatives_by_member_set_representative(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMemberSetRepresentativesBySection(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_member_set_representatives_by_section(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMembersByConstructionStage(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_members_by_construction_stage(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMembersByDesignSituation(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_members_by_design_situation(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMembersByLoading(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_members_by_loading(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMembersByLocation(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_members_by_location(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMembersByMaterial(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_members_by_material(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMembersByMember(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_members_by_member(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMembersByMemberSet(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_members_by_member_set(), include_base)

    @staticmethod
    def AluminumDesignDesignRatiosMembersBySection(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_design_ratios_members_by_section(), include_base)

    @staticmethod
    def AluminumDesignGoverningInternalForcesByMember(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_governing_internal_forces_by_member(), include_base)

    @staticmethod
    def AluminumDesignGoverningInternalForcesByMemberEnds(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_governing_internal_forces_by_member_ends(), include_base)

    @staticmethod
    def AluminumDesignGoverningInternalForcesByMemberRepresentative(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_governing_internal_forces_by_member_representative(), include_base)

    @staticmethod
    def AluminumDesignGoverningInternalForcesByMemberRepresentativeEnds(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_governing_internal_forces_by_member_representative_ends(), include_base)

    @staticmethod
    def AluminumDesignGoverningInternalForcesByMemberSet(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_governing_internal_forces_by_member_set(), include_base)

    @staticmethod
    def AluminumDesignGoverningInternalForcesByMemberSetEnds(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_governing_internal_forces_by_member_set_ends(), include_base)

    @staticmethod
    def AluminumDesignGoverningInternalForcesByMemberSetRepresentative(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_governing_internal_forces_by_member_set_representative(), include_base)

    @staticmethod
    def AluminumDesignGoverningInternalForcesByMemberSetRepresentativeEnds(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_governing_internal_forces_by_member_set_representative_ends(), include_base)

    @staticmethod
    def AluminumDesignGoverningLoading(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_governing_loading(), include_base)

    @staticmethod
    def AluminumDesignOverviewErrorsAndWarnings(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_overview_errors_and_warnings(), include_base)

    @staticmethod
    def AluminumDesignOverviewNotValidDeactivated(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_overview_not_valid_deactivated(), include_base)

    @staticmethod
    def AluminumDesignSlendernessByMember(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_slenderness_by_member(), include_base)

    @staticmethod
    def AluminumDesignSlendernessByMemberRepresentative(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_slenderness_by_member_representative(), include_base)

    @staticmethod
    def AluminumDesignSlendernessByMemberSet(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_slenderness_by_member_set(), include_base)

    @staticmethod
    def AluminumDesignSlendernessByMemberSetRepresentative(
        include_base: bool = False,
        model = Model):

        '''
        Args:
            model(class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_results_for_aluminum_design_slenderness_by_member_set_representative(), include_base)
