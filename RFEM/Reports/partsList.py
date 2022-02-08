
from RFEM.initModel import Model

def GetPartsListAllByMaterial():
    '''
    Returns Parts List All By Material
    '''
    try:
        return Model.clientModel.service.get_parts_list_all_by_material()
    except:
        Model.clientModel.service.generate_parts_lists()
        return Model.clientModel.service.get_parts_list_all_by_material()

def GetPartsListMemberRepresentativesByMaterial():
    '''
    Returns Parts List Member Representatives By Material
    '''
    try:
        return Model.clientModel.service.get_parts_list_member_representatives_by_material()
    except:
        Model.clientModel.service.generate_parts_lists()
        return Model.clientModel.service.get_parts_list_member_representatives_by_material()

def GetPartsListMemberSetsByMaterial():
    '''
    Returns Parts List Member Sets By Material
    '''
    try:
        return Model.clientModel.service.get_parts_list_member_sets_by_material()
    except:
        Model.clientModel.service.generate_parts_lists()
        return Model.clientModel.service.get_parts_list_member_sets_by_material()

def GetPartsListMembersByMaterial():
    '''
    Returns Parts List Members By Material
    '''
    try:
        return Model.clientModel.service.get_parts_list_members_by_material()
    except:
        Model.clientModel.service.generate_parts_lists()
        return Model.clientModel.service.get_parts_list_members_by_material()

def GetPartsListSolidsByMaterial():
    '''
    Returns Parts List Solids By Material
    '''
    try:
        return Model.clientModel.service.get_parts_list_solids_by_material()
    except:
        Model.clientModel.service.generate_parts_lists()
        return Model.clientModel.service.get_parts_list_solids_by_material()

def GetPartsListSurfacessByMaterial():
    '''
    Returns Parts List Surfaces By Material
    '''
    try:
        return Model.clientModel.service.get_parts_list_surfaces_by_material()
    except:
        Model.clientModel.service.generate_parts_lists()
        return Model.clientModel.service.get_parts_list_surfaces_by_material()
